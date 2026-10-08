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
# Zenodo's own licence id, from /api/licenses.
LICENSE = "cc-by-nc-nd-4.0"
CREATOR = {"name": "Wisdom Hill Research", "affiliation": "Wisdom Hill"}


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
    description = "<p><strong>%s</strong></p><p>%s</p>" % (subtitle, summary) \
        if subtitle else "<p>%s</p>" % summary
    description += ('<p>Part of <em>%s</em>, a research series by Wisdom Hill '
                    'Research. The full series is at <a href="%s/">%s</a>.</p>'
                    % (series, SITE, SITE))

    return {
        "order": order,
        "pdf": pdf,
        "url": url,
        "metadata": {
            "upload_type": "publication",
            "publication_type": "report",
            "title": title,
            "creators": [CREATOR],
            "description": description,
            "publication_date": str(fm.get("date-modified") or fm["date"]),
            "access_right": "open",
            "license": LICENSE,
            "keywords": [series] + list(fm.get("keywords") or []),
            "language": "eng",
            "version": "1.0.0",
            "related_identifiers": [
                {"identifier": url, "relation": "isIdenticalTo",
                 "resource_type": "publication-report"},
                {"identifier": SITE + "/", "relation": "isPartOf",
                 "resource_type": "publication-report"},
            ],
            "notes": "Series position: %s." % (
                "Prologue" if order == 0 else
                "Epilogue" if order == 15 else "Report %d of 14" % order),
        },
    }


def main():
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
