# PDF Typography Specification

Every value below is a named parameter in `_partials/typst-template.typ`.
To adjust the PDF, change the default in that file's parameter list — nothing
else needs editing, and the HTML output is unaffected.

Base measurements: A4, 2.5 cm margins on all four sides, body 11 pt,
`linestretch: 1.15`. `1em` in the cover block equals 11 pt.

---

## 1. Title section (page 1, top)

Rendered in this order, left-aligned, all in Inter.

```
1. The Agentic Inflection                                 ← title
                                    ↕ cover-gap-title-subtitle
How AI crossed from conversation to labor                 ← subtitle
                                    ↕ cover-gap-subtitle-series
THE INTELLIGENCE ECONOMY · A WISDOM HILL RESEARCH SERIES  ← series label
                                    ↕ cover-gap-series-byline
Wisdom Hill Research    2026-08-24                        ← byline
                                    ↕ cover-gap-byline-rule
─────────────────────────────────────────────────────     ← rule
                                    ↕ cover-gap-rule-toc
Table of contents
```

### Type

| Line | Parameter | Value | Face / weight | Colour |
| --- | --- | --- | --- | --- |
| Title | `cover-title-size` / `cover-title-weight` | `22pt` / `"bold"` | Inter Bold | `titlecolor` = `2251FF` |
| Subtitle | `cover-subtitle-size` / `cover-subtitle-weight` | `14pt` / `"semibold"` | Inter SemiBold | `subtitlecolor` = `2F4B8F` |
| Series label | `cover-series-size` | `9pt` | Inter Medium, uppercase, `tracking: 0.06em` | `serieslabelcolor` = `6E7B87` |
| Byline | `cover-byline-size` | `10pt` | Inter Regular | `bylinecolor` = `3C4A57` |
| Rule | — | `0.6pt` | — | `rulecolor` = `C8D0D8` |

Colours are hex **without** a leading `#`. Typst's `rgb()` rejects the hash.

The subtitle colour is chosen to sit in the title's hue family while ranking
below it:

| Role | Hex | Hue | Saturation | Value |
| --- | --- | --- | --- | --- |
| Title | `2251FF` | 227° | 87% | 100% |
| Subtitle | `2F4B8F` | 223° | 67% | 56% |
| Byline / body grey | `3C4A57` | 209° | 31% | 34% |

Hue is held nearly constant while saturation and value fall, so the three
lines read as one family in a clear order of prominence. To make the subtitle
more assertive without competing with the title, raise its value (e.g.
`3358A8`); to recede it, lower saturation toward the byline grey.

### Vertical spacing

| Gap | Parameter | Value |
| --- | --- | --- |
| Title → subtitle | `cover-gap-title-subtitle` | `1.2em` |
| Subtitle → series label | `cover-gap-subtitle-series` | `1em` |
| Series label → byline | `cover-gap-series-byline` | `0.75em` |
| Byline → rule | `cover-gap-byline-rule` | `1em` |
| Rule → contents | `cover-gap-rule-toc` | `2em` |
| Leading inside title block | hard-coded `set par(leading:)` | `0.5em` |
| Paragraph spacing inside title block | hard-coded `set par(spacing:)` | `0em` |

Separator between author and date: `h(1.2em)`.

### Why the title/subtitle gap is now linear

The title block sets `par(spacing: 0em)`. Without it, the `parbreak()` between
the two lines contributed Typst's default paragraph spacing — roughly `1.2em`
— **before** `cover-gap-title-subtitle` was added on top. Changing the
parameter from `0.75em` to `0.25em` therefore moved the visible gap by only
5.5 pt out of about 22 pt, and setting it to `0em` would still have left a
wide gap.

With paragraph spacing zeroed, the parameter now controls the whole gap:
`0.1em` ≈ `1.1pt` at an 11 pt base. Negative values are legal in Typst
(`v(-0.25em)` compiles and pulls the lines together), but they are not needed
here — `0em` now genuinely means baseline-to-baseline at the block's leading.

The same latent paragraph spacing applies to the series-label → byline gap,
which is inside a second block that does **not** zero `par(spacing)`. If that
gap ever needs fine control, zero it there too.

---

## 2. Table of contents (page 1, below the rule)

| Element | Parameter | Value | Face / weight |
| --- | --- | --- | --- |
| "Table of contents" | `toc-title-size` | `13pt` | Inter SemiBold |
| Gap below that heading | `toc-gap-after-title` | `0.9em` | — |
| Level 1 entries (Part I, Appendices, References) | `toc-level1-size` | `10.5pt` | Inter Medium |
| Level 2 entries (1.1, 2.3, …) | `toc-level2-size` | `9pt` | Inter Regular |
| Depth shown | `toc-depth` in `_quarto.yml` | `2` | — |

Level sizes are applied with `show outline.entry.where(level: n)`, which
requires Typst 0.12 or later. Quarto 1.10 ships Typst 0.15.

A page break follows the contents, so the body always begins on page 2.
Page numbers run from 1 and appear on every page including the cover.

---

## 3. Body (page 2 onward)

| Element | Value |
| --- | --- |
| Body face | Source Serif 4 Regular, 11 pt |
| Body leading | `linestretch: 1.15` |
| Level-1 heading (`# Part I.`) | Inter SemiBold, `heading1-size` = `15pt`, `heading1-color` = `2F4B8F` |
| Level-2 heading (`## 2.1`) | Inter SemiBold, `heading2-size` = `12pt`, body colour |
| Level-3 heading (`### 2.1.1`) | Inter SemiBold, `heading3-size` = `11pt`, body colour |
| Space added after a level-1 heading | `heading1-gap-after` = `0.5em` |
| Space added after a level-2 heading | `heading2-gap-after` = `0.3em` |
| Part separator rule | 25%–75% of text width, `horizontalrule-gap` = `1em` above and below |
| Emphasis | Source Serif 4 Italic |
| Inline literal | DejaVu Sans Mono at `raw-scale` × body = `9.57pt` — see § 3c |
| Bold runs in body | Source Serif 4 Bold |
| Text block width | 16.0 cm (210 mm − 2 × 25 mm) |

Heading sizes are **fixed in points**, not left to Typst's default relative
scale (which was 1.4 / 1.2 / 1.0 × body, i.e. 15.4 / 13.2 / 11.0 pt). Pinning
them means a future Typst or Quarto release cannot change the document
silently.

The level-1 colour matches the cover subtitle, so the Part headings and the
subtitle read as one system. Levels 2 and 3 stay in the body colour; colouring
them as well would flatten the hierarchy the sizes establish.

`heading1-gap-after` and `heading2-gap-after` are **added to** Typst's own
block spacing, not a replacement for it, because the spacer is inserted
non-weak:

```typst
show heading.where(level: 1): it => { it; v(heading1-gap-after) }
```

Making it `weak: true` would take the larger of the two values instead of the
sum, which is usually not what is wanted when tuning by small increments.

### 3a. The part separator comes from the source

The rule is styled here but placed by the document: a `---` at the end of each
chapter. Every report manuscript already carries them between its parts, and
the conversion keeps them as the closing line of each `_NN-*.qmd` fragment.

Do not move this into the template. Drawing the rule automatically before every
level-1 heading works, but it then has to be stripped from every manuscript on
the way in — extra work on the common case (a manuscript that already has the
rules) to guard against the rare one. It also fails badly when made
conditional: suppressing the rule where a part starts at the top of a page
shortens the block, which can pull the heading back onto the previous page,
which restores the rule, and Typst reports *document did not converge within
five attempts*.

The Prologue was the one document written without the separators. They were
added to `manuscripts/prologue-about-this-series.md` rather than worked around.

A manuscript may also place `---` *inside* a part, between its subsections;
those are the author's and are carried through. Report 5 Part IV is the case
that established the rule.

---

## 3b. Closing colophon (last page)

Every PDF ends with a licence and citation block. The web pages get this from
Quarto's own Reuse/Citation apparatus; a PDF travels on its own and had
neither.

| Element | Parameter | Value |
| --- | --- | --- |
| Type size | `colophon-size` | `8.5pt`, Inter |
| Colour | `colophon-color` | `6E7B87` (the cover series-label grey) |
| Space above | `colophon-gap-before` | `1.5em` |
| Leading | `colophon-leading` | `0.55em` |

It renders in two forms, selected by whether `citation.number` exists:

```
The Intelligence Economy · Report 1          <- numbered report
The Intelligence Economy                     <- Prologue, Epilogue
© 2026 Wisdom Hill. Licensed under CC BY-NC-ND 4.0.
Quotation and summary are freely permitted with attribution.

Cite as: Wisdom Hill Research. 2026. “1. The Agentic Inflection.”
In The Intelligence Economy, No. 1. Wisdom Hill.
https://wisdomhill.github.io/intelligence-economy/
```

Every value is inherited, so later reports acquire the block without declaring
anything:

| Line | Source |
| --- | --- |
| Series name | `series-title` (`_quarto.yml`) |
| `· Report N`, `, No. N` | `citation.number`; absent means the short form |
| © year, holder, publisher | `copyright.year`, `copyright.holder` |
| Licence | `license.text` |
| Author | `author.name.literal` |
| Cited title | the document's own `title` |
| URL | `series-url` (`_quarto.yml`) |

No rule is drawn by the colophon. Each chapter already closes with one, so the
last chapter's rule is the separator above this block. Where the body fills its
last page the colophon moves to a page of its own.

Two Typst constraints shaped the implementation:

- The document title is passed as **both** content (`title`) and a string
  (`title-text`). A title beginning `1. ` is parsed as an enum item when
  inserted as markup, which drops the number and breaks the citation over three
  lines. The citation line uses the string.
- Pandoc writes a double slash as `/\/` when emitting Typst, and the escape
  survives into a quoted string, so `series-url` is unescaped before use.

---

## 3c. Inline literals are set in the bundled monospace

The series carries about ten inline literals in total — file and field names
such as `ai-catalog.json` — and no code blocks. They are set in **DejaVu Sans
Mono**, one of the four faces Typst bundles, because the project deliberately
leaves `codefont` unset.

This is the one face in the PDFs that is not committed to `_fonts/`, and it is
not a substitution. A build with `--ignore-system-fonts` still embeds it, which
is the proof that it comes from Typst rather than from the machine, so it is as
reproducible as the pinned faces and costs the repository nothing.
`tools/verify_pdf.py` lists it in `ALLOWED_PREFIXES` with that reasoning.

Committing a monospace face of our own would add 200 KB to 1 MB to serve ten
literals. Revisit that only if a report arrives with real code blocks.

**Size.** Quarto's own Typst output already sets raw text to `0.8em`, which
leaves a literal reading noticeably smaller than the body around it:

| | x-height at an 11 pt body |
| --- | --- |
| Source Serif 4 (x-height 0.475em) | 5.22 pt |
| DejaVu Sans Mono at Quarto's `0.8em` | 4.81 pt |
| DejaVu Sans Mono at `raw-scale` = `0.87` | 5.23 pt |

`raw-scale` is applied as `fontsize * raw-scale`, **not** in `em`. Inside a
`show raw` rule `em` resolves against the already-reduced raw size and the two
reductions compound — `0.92em` there yields 8.1 pt, not 10.1 pt.

---

## 3d. Tables

Cells are **ragged-right**, so a PDF table reads the way the web one does.
Body copy is justified; a justified column a few centimetres wide stretches
every line to the cell edge, which made cells read as grey blocks rather than
as text.

Hyphenation must be switched back on by hand alongside it. Typst's default is
`hyphenate: auto`, meaning *only when justified*, so turning justification off
also turns hyphenation off — and a word wider than its column then overflows
into its neighbour instead of breaking. A 13% column rendered
`ClassificatioSnegment`, two cells printed over each other. Both rules are
therefore required:

```typst
show table: set par(justify: false)
show table: set text(hyphenate: true)
```

**Column widths.** Quarto divides a table equally unless told otherwise, which
is unreadable past four or five columns — a seven-column roster came out at
one or two characters per line. Give any table of four or more columns explicit
proportions:

```
: {tbl-colwidths="[4,13,13,28,14,14,14]"}
```

The line goes after the table, separated by a blank line, and applies to both
HTML and PDF. Numeric columns need enough width for the header, not the
figures: `Mkt Cap, End-2025 ($B)` sets the minimum, not `568.85`.

---

## 4. Where the values live

```
_filters/typst-apostrophe.lua     apostrophe after a digit (PDF only)
_partials/definitions.typ         Part separator rule (`horizontalrule`)
_quarto.yml                       per-series switches
  format.typst.fontsize           body size (11pt)
  format.typst.margin             page margins (2.5cm)
  format.typst.mainfont           body face (Source Serif 4)
  format.typst.headingfont        heading/cover face (Inter)
  format.typst.titlecolor         title colour (2251FF)
  format.typst.series-label       cover eyebrow text
  format.typst.series-title       series name in the colophon
  format.typst.series-url         series root URL in the colophon
  (no format.typst.codefont)      inline literals — see § 3c
  format.typst.toc-depth          contents depth (2)

_partials/typst-template.typ      everything else in this document,
                                  as named parameters at the top of
                                  the `article()` function

_fonts/                           Inter and Source Serif 4, committed
```

`headingfont`, `titlecolor`, `series-label`, `series-title` and `series-url`
are custom keys read only by
`_partials/typst-show.typ`. The cover and contents parameters in section 1 and
2 are template defaults, not YAML options — change them in the template.

---

## 5. Reproducing this output elsewhere

This file records the values; it does not produce them. The formatting comes
from `_partials/` (three Typst partials, 575 lines) and `_fonts/` (14 binaries).
See `HANDOFF.md` before moving the project to a new working directory.

To confirm a rendered PDF matches this specification:

```
python tools/verify_pdf.py _site/reports/r01/r01-the-agentic-inflection.pdf
```

Expected: 12/12 checks passed. A document that uses only one heading level,
such as the Prologue, reports the levels it does not use as n/a.

```
```

---

## 6. Adjusting

To request a change, name the parameter and the new value, e.g.
"`cover-title-size` to 26pt" or "`toc-level2-size` to 9.5pt".

Two behaviours to keep in mind when tuning:

- Typst substitutes a missing font **silently**. After changing a face, verify
  with the embedded font table rather than by eye:
  ```python
  from pypdf import PdfReader
  r = PdfReader("_site/reports/r01/r01-the-agentic-inflection.pdf")
  res = r.pages[1]["/Resources"]["/Font"]
  print(sorted({res[k]["/BaseFont"].split("+")[-1] for k in res}))
  ```
- `v(x, weak: true)` collapses against an adjacent paragraph break. Where a
  gap must survive, either drop `weak` or place `parbreak()` before the spacer.
- The separator rule is defined as `line(start: (25%,0%), end: (75%,0%))`.
  Those percentages already centre it within the text block, so wrapping it in
  `align(center, …)` shifts it right instead. Its gaps are added around
  Typst's own block spacing rather than replacing it — replacing it pulls the
  rule up against the preceding paragraph.
