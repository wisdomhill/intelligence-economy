#!/usr/bin/env python3
"""
Convert the existing Markdown reports into Quarto documents with a
front-matter skeleton in place.

For each source file the script:

  1. detects and preserves any front matter that is already present;
  2. lifts the leading level-1 heading into the `title` field and removes it
     from the body (Quarto renders the title itself, so leaving the heading
     produces a duplicate);
  3. inserts every remaining field as a TODO placeholder, preserving key
     order so that all fifteen files look alike in review;
  4. writes the result as `rNN-<slug>.qmd`.

Nothing is overwritten unless --force is given, and the source files are
left untouched. Run with --dry-run first.

Usage:
    python tools/init_frontmatter.py --src drafts --out reports --dry-run
    python tools/init_frontmatter.py --src drafts --out reports
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import unicodedata
from pathlib import Path

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"\A\s*#\s+(?P<title>.+?)\s*$", re.MULTILINE)
LEADING_NUMBER_RE = re.compile(r"\A\s*(?:report\s*)?(\d{1,2})\s*[.):\-]\s*", re.I)

TODO = "TODO"


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return re.sub(r"-{2,}", "-", text)[:48] or "report"


def infer_order(path: Path, title: str) -> int | None:
    """Read a series number from the filename first, then the title."""
    for candidate in (path.stem, title):
        m = re.search(r"(?:^|[^0-9])(\d{1,2})(?:[^0-9]|$)", candidate)
        if m:
            n = int(m.group(1))
            if 0 <= n <= 20:
                return n
    return None


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_front_matter(title: str, order: int | None, today: str) -> str:
    number = str(order) if order is not None else TODO
    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f'subtitle: "{TODO}: descriptive subtitle"',
        f'description: >-',
        f"  {TODO}: one or two sentences for the listing card and link preview.",
        "abstract: |",
        f"  {TODO}: 150-250 words, adapted from the report's opening summary.",
        f"date: {today}",
        f"date-modified: {today}",
        f"order: {number}",
        f"categories: [{TODO}]",
        f"keywords: [{TODO}]",
        "citation:",
        "  type: report",
        '  container-title: "The Intelligence Economy"',
        f"  number: {number}",
        '  publisher: "Wisdom Hill Research"',
        "---",
        "",
    ]
    return "\n".join(lines)


def strip_leading_number(title: str) -> str:
    """'Report 4. The SaaS Apocalypse Question' -> 'The SaaS Apocalypse Question'"""
    return LEADING_NUMBER_RE.sub("", title).strip()


def convert(path: Path, out_dir: Path, today: str, force: bool, dry_run: bool) -> str:
    raw = path.read_text(encoding="utf-8")

    if FRONT_MATTER_RE.match(raw):
        return f"skip   {path.name}  (front matter already present)"

    m = H1_RE.search(raw)
    if m and raw[: m.start()].strip() == "":
        raw_title = m.group("title").strip()
        body = raw[m.end():].lstrip("\n")
    else:
        raw_title = path.stem.replace("-", " ").replace("_", " ").title()
        body = raw

    title = strip_leading_number(raw_title)
    order = infer_order(path, raw_title)

    prefix = f"r{order:02d}-" if order is not None else "rXX-"
    target = out_dir / f"{prefix}{slugify(title)}.qmd"

    if target.exists() and not force:
        return f"skip   {path.name}  ({target.name} exists; use --force)"

    content = build_front_matter(title, order, today) + body.rstrip() + "\n"

    if dry_run:
        return f"would write {target.name:<44} title={title!r} order={order}"

    out_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return f"wrote  {target.name:<44} title={title!r} order={order}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=Path, required=True, help="directory of source .md files")
    ap.add_argument("--out", type=Path, default=Path("reports"), help="output directory")
    ap.add_argument("--date", default=dt.date.today().isoformat(),
                    help="value for date and date-modified (YYYY-MM-DD)")
    ap.add_argument("--force", action="store_true", help="overwrite existing .qmd files")
    ap.add_argument("--dry-run", action="store_true", help="report actions without writing")
    args = ap.parse_args()

    if not args.src.is_dir():
        print(f"error: {args.src} is not a directory", file=sys.stderr)
        return 1

    sources = sorted(p for p in args.src.glob("*.md") if not p.name.startswith("_"))
    if not sources:
        print(f"error: no .md files found in {args.src}", file=sys.stderr)
        return 1

    for path in sources:
        print(convert(path, args.out, args.date, args.force, args.dry_run))

    if args.dry_run:
        print("\nDry run only. Re-run without --dry-run to write files.")
    else:
        print(f"\n{len(sources)} file(s) processed. Search for 'TODO' to find "
              f"the fields still to be filled in.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
