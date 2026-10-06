#!/usr/bin/env python3
"""
Verify a rendered report PDF against TYPOGRAPHY.md.

Typst substitutes missing fonts silently and an out-of-date Quarto quietly
ignores several of the options this project relies on, so neither failure is
visible by eye. Run this after any change to `_partials/`, `_fonts/`, or the
`format: typst` block, and after upgrading Quarto.

    pip install pypdf pdfplumber
    python tools/verify_pdf.py _site/reports/r01/r01-the-agentic-inflection.pdf
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import pdfplumber
    from pypdf import PdfReader
except ImportError:
    sys.exit("needs: pip install pypdf pdfplumber")

A4_MM = (210, 297)
EXPECT_FONTS = {"Inter-SemiBold", "Inter-Regular", "SourceSerif4-Regular"}

# Faces a correct render may embed. Anything else means Typst substituted a
# font it could not find, which it does silently.
#
# DejaVuSansMono is the exception, and a deliberate one: it is one of the four
# fonts Typst bundles, and it is what `show raw` resolves to because the
# project sets no `codefont`. It is not a substitution — a build with
# `--ignore-system-fonts` still embeds it, which is the proof that it comes
# from Typst rather than from the machine. The series carries about ten inline
# literals in total (file and field names), so committing a monospace face of
# our own would add weight for nothing.
# NewCMMath is Typst's math face. It appears only where a report actually
# sets equations -- Report 13 does. Its presence in a report that sets none
# means a `$...$` pair was read as math by accident; that used to be the
# way such a bug surfaced, and is now prevented in tools/split_manuscript.py.
# LibertinusSerif is Typst's fallback for a character the pinned faces do
# not carry. Report 14 needs it for five glyphs in total -- the circled
# digits in its scorecard header and one element-of sign. Allowing it is a
# deliberate trade: the check no longer notices if a whole passage falls
# back to the substitute. To see what actually used it:
#   {ch["text"] for p in pdf.pages for ch in p.chars
#    if "Libertinus" in ch["fontname"]}
ALLOWED_PREFIXES = ("Inter", "SourceSerif4", "DejaVuSansMono", "NewCMMath",
                    "LibertinusSerif")
EXPECT_HEADING_PT = {1: 15.0, 2: 12.0, 3: 11.0}
EXPECT_BODY_PT = 11.0
# Headings are found by face and size, and a figure defeats that on its own:
# an SVG sets its labels in the heading face too, and scaling a 1600px drawing
# into the text block lands them around 4-5pt, which read as an undersized
# level-3 heading. Nothing below this floor is a heading — the smallest the
# template sets is 11pt — so the floor separates the two with room to spare
# while still catching a real heading rendered at the wrong size.
MIN_HEADING_PT = 8.0
EXPECT_H1_RGB = (0.184, 0.294, 0.561)   # 2F4B8F
PRIME = "′"                        # Typst renders 1's as 1′s unescaped

results: list[tuple[bool | None, str]] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    results.append((ok, f"{label}{'  — ' + detail if detail else ''}"))


def skip(label: str, detail: str = "") -> None:
    """Record a check this document cannot answer — a heading level it does
    not use. The Prologue and the Epilogue are single-level documents, and
    failing them for an absent level would be a false alarm."""
    results.append((None, f"{label}{'  — ' + detail if detail else ''}"))


def main(path: Path) -> int:
    reader = PdfReader(str(path))
    page1 = reader.pages[0]

    # --- page geometry ---------------------------------------------------
    w_mm = float(page1.mediabox.width) / 72 * 25.4
    h_mm = float(page1.mediabox.height) / 72 * 25.4
    check(round(w_mm) == A4_MM[0] and round(h_mm) == A4_MM[1],
          "A4 page size", f"{w_mm:.0f}x{h_mm:.0f} mm")

    # --- engine ----------------------------------------------------------
    creator = (reader.metadata or {}).get("/Creator", "")
    check(creator.startswith("Typst"), "rendered by Typst", creator)

    # --- fonts actually embedded ----------------------------------------
    embedded: set[str] = set()
    for page in reader.pages:
        fonts = page.get("/Resources", {}).get("/Font", {})
        for key in fonts:
            embedded.add(str(fonts[key]["/BaseFont"]).split("+")[-1]
                         .replace("-Identity-H", ""))
    missing = EXPECT_FONTS - embedded
    check(not missing, "expected fonts embedded",
          f"missing {sorted(missing)}" if missing else ", ".join(sorted(embedded)))
    strays = {f for f in embedded
              if not f.startswith(ALLOWED_PREFIXES)}
    check(not strays, "no substituted faces",
          f"unexpected {sorted(strays)}" if strays else "")

    # --- cover page ------------------------------------------------------
    cover = page1.extract_text()
    check("Table of contents" in cover, "contents on page 1")
    check(cover.count("\n") >= 4, "cover header present")

    # --- the digit-apostrophe defect ------------------------------------
    # Typst reads an apostrophe after a digit as a unit mark.
    # `_filters/typst-apostrophe.lua` prevents it; this catches a regression
    # in the filter, which is otherwise invisible at a glance.
    full = "".join(page.extract_text() or "" for page in reader.pages)
    primes = re.findall(r"\d" + PRIME, full)
    check(not primes, "no primes after digits",
          f"{len(primes)} found" if primes else "")

    # --- type sizes ------------------------------------------------------
    with pdfplumber.open(str(path)) as pdf:
        body_sizes: dict[float, int] = {}
        h1 = h2 = h3 = None
        h1_colour = None
        for page in pdf.pages[1:]:
            for ch in page.chars:
                if "SourceSerif4-Regular" in ch["fontname"]:
                    body_sizes[round(ch["size"], 1)] = \
                        body_sizes.get(round(ch["size"], 1), 0) + 1
                if "Inter-SemiBold" in ch["fontname"]:
                    size = round(ch["size"], 1)
                    if size < MIN_HEADING_PT:
                        continue            # figure label, not a heading
                    if size >= EXPECT_HEADING_PT[1] - 0.05:
                        h1 = size
                        h1_colour = ch.get("non_stroking_color")
                    elif size >= EXPECT_HEADING_PT[2] - 0.05:
                        h2 = size
                    else:
                        h3 = size

    body = max(body_sizes, key=body_sizes.get) if body_sizes else None
    check(body == EXPECT_BODY_PT, "body 11pt", f"{body}pt")
    for level, found in ((1, h1), (2, h2), (3, h3)):
        expected = EXPECT_HEADING_PT[level]
        label = f"level-{level} heading {expected:g}pt"
        if found is None:
            skip(label, "not used in this document")
        else:
            check(found == expected, label, f"{found}pt")

    if isinstance(h1_colour, (list, tuple)) and len(h1_colour) == 3:
        near = all(abs(a - b) < 0.02 for a, b in zip(h1_colour, EXPECT_H1_RGB))
        check(near, "level-1 heading colour 2F4B8F",
              str(tuple(round(c, 3) for c in h1_colour)))
    else:
        check(False, "level-1 heading colour 2F4B8F", f"read {h1_colour}")

    # --- report ----------------------------------------------------------
    width = max(len(label) for _, label in results)
    for ok, label in results:
        mark = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
        print(f"  {mark}  {label:<{width}}")
    applicable = [ok for ok, _ in results if ok is not None]
    failed = sum(1 for ok in applicable if not ok)
    skipped = len(results) - len(applicable)
    print(f"\n{len(applicable) - failed}/{len(applicable)} checks passed"
          f"{f' ({skipped} n/a)' if skipped else ''}"
          f" — {path.name}, {len(reader.pages)} pages")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    raise SystemExit(main(Path(sys.argv[1])))
