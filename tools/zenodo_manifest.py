#!/usr/bin/env python3
"""
Collect the Zenodo metadata for every published document into one JSON file.

Everything here already exists in the site's own front matter -- title,
subtitle, description, keywords, dates, series position -- so the manifest is
derived rather than retyped, and regenerating it after a revision picks the
changes up. Review the result before uploading; `tools/zenodo_upload.py`
reads it and nothing else.

    python tools/zenodo_manifest.py > zenodo.json
"""
import io, json, os, re, sys, glob
import yaml

SITE = "https://wisdomhill.github.io/intelligence-economy"
# Zenodo's own licence id, from /api/vocabularies/licenses.
LICENSE = "cc-by-nc-nd-4.0"
PUBLISHER = "Wisdom Hill"


def copyright_line():
    """`Copyright (c) YEAR HOLDER`, from the same place the PDF colophon takes
    it. The holder is the institution, Wisdom Hill; the creator is the imprint,
    Wisdom Hill Research. The series has kept those apart from the start."""
    q = yaml.safe_load(io.open("_quarto.yml", encoding="utf-8").read())
    c = q.get("copyright") or {}
    return "Copyright © %s %s" % (c["year"], c["holder"])
# `organizational` is the point of using Zenodo's InvenioRDM API rather than
# the legacy deposit API: the legacy one has no creator type, so it files an
# imprint as a person and makes the whole name a surname. See HANDOFF.md.
COPYRIGHT = None
CREATOR = {"person_or_org": {"type": "organizational",
                             "name": "Wisdom Hill Research"}}


def front_matter(path):
    """YAML out of a .qmd's `---` fence, or a whole `_metadata.yml`."""
    text = io.open(path, encoding="utf-8").read()
    if path.endswith((".yml", ".yaml")):
        return yaml.safe_load(text) or {}
    if not text.startswith("---"):
        return {}
    fence = chr(10) + "---"
    return yaml.safe_load(text.split(fence, 1)[0][3:]) or {}


def merged(index_qmd, metadata_yml):
    """Page front matter, with the directory's `_metadata.yml` underneath it."""
    m = front_matter(metadata_yml) if os.path.exists(metadata_yml) else {}
    m.update({k: v for k, v in front_matter(index_qmd).items() if v is not None})
    return m


def record(fm, pdf, url, order):
    title = fm["title"]
    subtitle = fm.get("subtitle", "")
    summary = " ".join(str(fm.get("description", "")).split())
    series = (fm.get("citation") or {}).get("container-title", "The Intelligence Economy")

    # Zenodo renders description as HTML. Lead with the subtitle, which carries
    # as much of the argument as the title does in this series.
    description = "<p><strong>%s</strong></p><p>%s</p>" % (subtitle, summary)         if subtitle else "<p>%s</p>" % summary
    description += ('<p>Part of <em>%s</em>, a research series by Wisdom Hill '
                    'Research. The full series is at <a href="%s/">%s</a>.</p>'
                    % (series, SITE, SITE))

    position = ("Prologue" if order == 0 else
                "Epilogue" if order == 15 else "Report %d of 14" % order)

    return {
        "order": order,
        "pdf": pdf,
        "url": url,
        "metadata": {
            "resource_type": {"id": "publication-report"},
            "title": title,
            "publisher": PUBLISHER,
            "copyright": COPYRIGHT,
            "publication_date": str(fm.get("date-modified") or fm["date"]),
            "creators": [CREATOR],
            "description": description,
            "rights": [{"id": LICENSE}],
            "subjects": [{"subject": s} for s in
                         [series] + list(fm.get("keywords") or [])],
            "languages": [{"id": "eng"}],
            "version": "1.0.0",
            "related_identifiers": [
                {"identifier": url, "relation_type": {"id": "isidenticalto"},
                 "scheme": "url"},
                {"identifier": SITE + "/", "relation_type": {"id": "ispartof"},
                 "scheme": "url"},
            ],
            "additional_descriptions": [
                {"description": "Series position: %s." % position,
                 "type": {"id": "other"}},
            ],
        },
    }


def main():
    global COPYRIGHT
    COPYRIGHT = copyright_line()
    out = []

    fm = front_matter("prologue.qmd")
    out.append(record(fm, "_site/prologue.pdf", SITE + "/prologue.html", 0))

    # glob returns backslashes on Windows; these become URLs.
    for d in sorted(p.replace(chr(92), "/") for p in glob.glob("reports/r??")):
        n = int(d[-2:])
        fm = merged(os.path.join(d, "index.qmd"), os.path.join(d, "_metadata.yml"))
        pdfs = glob.glob(os.path.join("_site", d, "*.pdf"))
        if len(pdfs) != 1:
            sys.exit("expected one PDF in _site/%s, found %d" % (d, len(pdfs)))
        out.append(record(fm, pdfs[0].replace("\\", "/"), "%s/%s/" % (SITE, d), n))

    fm = merged("epilogue/index.qmd", "epilogue/_metadata.yml")
    out.append(record(fm, "_site/epilogue/epilogue.pdf", SITE + "/epilogue/", 15))

    out.sort(key=lambda r: r["order"])
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    print("%d records" % len(out), file=sys.stderr)


if __name__ == "__main__":
    main()
