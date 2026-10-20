#!/usr/bin/env python3
"""
Write the reserved Zenodo DOIs into the documents' own metadata.

    python tools/zenodo_upload.py --reserve
    python tools/zenodo_doi_writeback.py
    quarto render

Zenodo reserves a DOI on a draft before it is published, which is what lets a
PDF carry the identifier that will resolve to it. This copies each reserved
DOI into the source the site renders from, so it reaches three places at once:
the web page's citation block, the BibTeX Quarto generates, and the PDF
colophon.

Reports and the Epilogue have a `citation:` block of their own and take
`citation.doi`. The Prologue inherits its citation from `_quarto.yml`, so it
takes a document-level `doi:` instead -- `_partials/typst-show.typ` accepts
either.

Idempotent: a document that already carries the right DOI is left alone, and
one that carries a different DOI is reported rather than overwritten.
"""
import argparse, io, json, os, re, sys

STATE = "zenodo-state.json"
MANIFEST = "zenodo.json"


def target(order):
    """Which file holds this document's citation metadata, and under what key."""
    if order == 0:
        return "prologue.qmd", "document"
    if order == 15:
        return "epilogue/_metadata.yml", "citation"
    return "reports/r%02d/_metadata.yml" % order, "citation"


def put_citation_doi(text, doi):
    """Add or replace `doi:` inside an existing `citation:` block."""
    m = re.search(r"(?m)^citation:\n((?:[ \t]+.*\n|\n)*)", text)
    if not m:
        return None, "no citation: block"
    block = m.group(1)
    if re.search(r"(?m)^\s+doi:", block):
        current = re.search(r"(?m)^\s+doi:\s*(\S+)", block).group(1)
        if current == doi:
            return text, "unchanged"
        return None, "already has a different doi (%s)" % current
    # Match the block's own indentation.
    indent = re.match(r"[ \t]+", block).group(0)
    return text[:m.end(1)] + "%sdoi: %s\n" % (indent, doi) + text[m.end(1):], "added"


def put_document_doi(text, doi):
    """Add or replace a top-level `doi:` in a .qmd's front matter."""
    head, sep, rest = text.partition(chr(10) + "---")
    if not sep:
        return None, "no front matter"
    if re.search(r"(?m)^doi:", head):
        current = re.search(r"(?m)^doi:\s*(\S+)", head).group(1)
        if current == doi:
            return text, "unchanged"
        return None, "already has a different doi (%s)" % current
    head = re.sub(r"(?m)^(order:.*\n)", r"\1doi: %s\n" % doi, head, count=1)
    return head + sep + rest, "added"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sandbox", action="store_true",
                   help="read the sandbox state; rehearsal only -- sandbox "
                        "DOIs are 10.5072 test identifiers and must never be "
                        "committed")
    args = p.parse_args()
    global STATE
    if args.sandbox:
        STATE = "zenodo-state-sandbox.json"
        print("SANDBOX: these are test DOIs. Revert the files afterwards." + chr(10))

    if not os.path.exists(STATE):
        sys.exit("%s not found -- run `python tools/zenodo_upload.py --reserve` "
                 "first" % STATE)
    state = json.load(io.open(STATE, encoding="utf-8"))
    records = json.load(io.open(MANIFEST, encoding="utf-8"))

    problems = 0
    for rec in records:
        here = state.get(rec["url"]) or {}
        # A record published already carries its DOI under `doi`;
        # one still in draft carries the reservation.
        doi = here.get("reserved") or here.get("doi")
        label = "[%2s]" % rec["order"]
        if not doi:
            print("%s no reserved DOI in the state file" % label)
            problems += 1
            continue

        path, kind = target(rec["order"])
        text = io.open(path, encoding="utf-8").read()
        new, how = (put_document_doi(text, doi) if kind == "document"
                    else put_citation_doi(text, doi))
        if new is None:
            print("%s %-34s %s" % (label, path, how))
            problems += 1
            continue
        if how == "added":
            io.open(path, "w", encoding="utf-8", newline="\n").write(new)
        print("%s %-34s %-9s %s" % (label, path, how, doi))

    print()
    if problems:
        sys.exit("%d document(s) not written -- resolve the above first" % problems)
    print("Now re-render so the PDFs pick the DOIs up:")
    print("  quarto render")


if __name__ == "__main__":
    main()
