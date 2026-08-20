#!/usr/bin/env python3
"""
Give each report a distinct BibTeX key.

Quarto derives the key from author and year and offers no override, so all
fifteen reports emit `@report{wisdom_hill_research2026, ...}`. A reader who
collects more than one report into a single `.bib` gets duplicate keys.

This runs as a Quarto `post-render` hook and rewrites the key in the rendered
HTML to `wisdomhill_ie_rNN`, taken from the report directory name. Nothing in
the source changes; only the copy-ready BibTeX block the reader sees.

Wired up in _quarto.yml:

    project:
      post-render: tools/fix_bibtex_keys.py
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

KEY_TEMPLATE = "wisdomhill_ie_{report}"
REPORT_DIR = re.compile(r"(?:^|/)reports/(r\d{2})/")
BIBTEX_KEY = re.compile(r"(@\w+\{)([^,\s]+)(,)")


def main() -> int:
    out = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
    if not out.is_dir():
        print(f"fix_bibtex_keys: {out} not found; skipping", file=sys.stderr)
        return 0

    changed = 0
    for html in out.rglob("*.html"):
        match = REPORT_DIR.search(html.as_posix())
        if not match:
            continue
        key = KEY_TEMPLATE.format(report=match.group(1))
        text = html.read_text(encoding="utf-8")
        new, n = BIBTEX_KEY.subn(lambda m: f"{m.group(1)}{key}{m.group(3)}", text)
        if n:
            html.write_text(new, encoding="utf-8")
            changed += 1

    print(f"fix_bibtex_keys: rewrote keys in {changed} page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
