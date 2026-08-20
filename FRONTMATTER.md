# Front Matter Specification

Normative rules for YAML metadata across *The Intelligence Economy*.
Report 1 (`reports/r01/`) is the reference implementation — copy its shape.

---

## Governing principle

**A value is declared once, at the highest layer where it is true.**

Five rendered layers, from widest to narrowest, plus the unrendered manuscript
that feeds them. Never repeat a value that a lower layer already inherits.

| Layer | File | Scope |
| --- | --- | --- |
| 0 | `manuscripts/<slug>.md` | the manuscript: one whole report, not rendered |
| 1 | `_quarto.yml` | every document in the series |
| 2 | `index.qmd` | the series listing page only |
| 3 | `reports/rNN/_metadata.yml` | every file in one report |
| 4 | `reports/rNN/index.qmd` | that report's cover page |
| 5 | `reports/rNN/NN-*.qmd` | one chapter page |

If a field appears in two layers, the narrower one silently wins and the two
will drift apart. Treat any duplicate as a defect.

---

## Layer 1 — `_quarto.yml`

Series-wide identity. Do not repeat any of this in a report file.

```yaml
lang: en

author:
  - name: "Wisdom Hill Research"
    affiliation: "Wisdom Hill"
    url: https://www.wisdomhill.net

copyright:
  holder: "Wisdom Hill"
  year: "2026"

license: "CC BY-NC-ND 4.0"

citation: true
```

**The author is the institution, not a person.** No individual byline appears
anywhere in the series. `Wisdom Hill Research` is the research imprint;
`Wisdom Hill` is the publishing entity and the copyright holder.

`citation: true` generates each document's canonical URL from `site-url` plus
its path. Never hard-code a URL in a `citation:` block — when the site moves to
`research.wisdomhill.net`, changing `site-url` alone must be sufficient.

---

## Layer 2 — `index.qmd`

The series listing. Its `fields:` list must name only keys that Layer 4
actually supplies; naming an absent key renders an empty column.

```yaml
title: "The Intelligence Economy"
subtitle: "How agentic AI is reorganising the economy, layer by layer"
listing:
  id: reports
  contents: reports/*/index.qmd
  type: default
  sort: "order asc"
  sort-ui: [order, title]
  filter-ui: true
  fields: [title, subtitle, description, date]
  page-size: 20
toc: false
```

`categories` is **not used in this series.** Do not add `categories:` to any
report, and do not re-enable `categories: true` here.

---

## Layer 3 — `reports/rNN/_metadata.yml`

Values shared by the report cover, its chapter pages, and its PDF source.
This file exists to stop the cover and the PDF source drifting apart.

```yaml
title-block-style: none
date: 2026-08-24
date-modified: 2026-08-24
citation:
  type: report
  title: "1. The Agentic Inflection"
  container-title: "The Intelligence Economy"
  number: 1
  publisher: "Wisdom Hill"
  url: https://wisdomhill.github.io/intelligence-economy/reports/r01/
```

`citation.title` and `citation.url` are required here. Without them each
chapter page cites itself rather than the report.

`title-block-style: none` suppresses the Author / Affiliation / Published /
Modified strip. A reader meets that information once, on the cover; repeating
it above all eight chapter pages is noise. The page title and the breadcrumbs
are unaffected. The cover turns it back on — see Layer 4 — and the option is
inert in the PDF. Write it at the top level, **not** inside a `format:` block,
for the reason given below.

- `date` is the publication date. All fifteen reports publish on **2026-08-24**.
- `date-modified` starts equal to `date`. Change it only when a substantive
  correction is issued, and log that correction in `errata.qmd`.
- `citation.number` is the series position, and is the **only** place the
  report number is recorded as metadata.

**Do not put `format:` or `title:` in this file.** Quarto merges `format:`
blocks from `_metadata.yml` rather than replacing them, which silently
re-enables HTML on the PDF-only source. `title:` would overwrite every chapter
page's own title.

---

## Layer 4 — `reports/rNN/index.qmd`

The report cover: executive summary, contents table, PDF download link.

```yaml
format:
  html: default
title-block-style: default
title: "1. The Agentic Inflection"
subtitle: "How AI crossed from conversation to labor"

description: >-
  The four-stage phase transition from chatbot to agent, and the three-way
  contest for the agentic value layer. Why user share and value capture have
  decoupled.

order: 1
keywords:
  - agentic AI
  - task horizon
  - agent harness
  - context lock-in
  - model commoditization
```

| Field | Rule |
| --- | --- |
| `title` | `N. Report Title` — the series number, a period, then the title. No series name, no colon-clause carrying a second idea. |
| `subtitle` | One clause naming the report's move. Required on the cover. |
| `description` | One or two sentences. Feeds the listing card and the link-preview card when the URL is shared. Not a summary of the whole report. |
| `order` | Series position. Must equal `citation.number` and the number prefixing `title`. Drives listing sort. |
| `keywords` | Five to eight subject terms. Not displayed; carried in document metadata. |
| `format` | `html: default` only. The cover is never a PDF. |
| `title-block-style` | `default`, overriding Layer 3. The cover is where the author, affiliation and dates belong. |

Not used: `categories`, `abstract`, `image`. `abstract` is redundant because
every report opens with an Executive Summary; adding one makes the reader
traverse the same argument twice.

---

## Layer 5 — `reports/rNN/NN-*.qmd` (chapter wrappers)

Four lines. Title and one include.

```yaml
---
format:
  html: default
title: "Part I. The Phase Transition"
---

{{< include _01-phase-transition.qmd >}}
```

**`subtitle` is not used on chapter pages.** A chapter heading is one thing,
not two; do not manufacture a second clause to fill the field.

The title must stand alone, because it is reused verbatim in three places:
the page heading, the sidebar entry, and the previous/next arrow labels at the
foot of adjacent pages. Write it so it is unambiguous with no surrounding
context.

---

## Layer 5b — `reports/rNN/rNN-*.qmd` (PDF source)

Assembles the fragments into one document. Carries only what the PDF needs
that `_metadata.yml` does not already provide.

```yaml
---
title: "1. The Agentic Inflection"
subtitle: "How AI crossed from conversation to labor"
format:
  typst: default
---

# Executive Summary

{{< include _00-executive-summary.qmd >}}

# Part I. The Phase Transition

{{< include _01-phase-transition.qmd >}}
```

`format: typst: default` in file front matter **replaces** the project format
list, so no HTML twin is produced. This only works from front matter — putting
it in `_metadata.yml` merges instead and yields both formats.

Level-1 headings live here, not in the fragments, so the same body text can be
a standalone page (title from front matter) and a PDF section (heading from
this file).

---

## Layer 0 — `manuscripts/<slug>.md` (the manuscript)

The manuscript is the only place a report exists as one document. PDF and HTML
are read-optimised artifacts; the fragments are split by chapter. **Any edit to
report content is applied here as well as to the fragment** — the manuscript
must stay identical to the published prose.

One file per document, named for the published slug so the two line up:

```
manuscripts/prologue-about-this-series.md   ->  prologue.qmd
manuscripts/r01-the-agentic-inflection.md   ->  reports/r01/
manuscripts/r02-the-idea-bottleneck.md      ->  reports/r02/
```

Revisions are **not** put in the filename — that changes links every time the
text is corrected. `manuscript-revision:` in the front matter records it, and
git carries the history.

Its front matter makes the file self-describing. It mirrors the cover's
identity fields and adds the mapping the cover cannot hold:

```yaml
title: "2. The Idea Bottleneck"
subtitle: "Why agentic AI's productivity dividend hides in data, not code"
series: "The Intelligence Economy"
number: 2                       # null for the Prologue and the Epilogue
manuscript-revision: 1
date: 2026-08-24
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"
description: >-
  …
keywords: […]
published:
  dir: reports/r02/
  pdf: r02-the-idea-bottleneck.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r02/
chapters:
  - manuscript: "1. Introduction: The Productivity Paradox of Agentic AI"
    published:  "1. The Productivity Paradox"
    fragment:   _01-productivity-paradox.qmd
    page:       01-productivity-paradox.qmd
```

`chapters:` is the load-bearing part. Published titles are shortened, because
each is reused verbatim in the sidebar and in the previous/next labels, where
a manuscript heading with a colon-clause reads badly. Recording both sides
keeps the manuscript's fuller headings *and* states what was published, so the
one legitimate difference between the two layers is data rather than drift.
Where several manuscript headings collapse onto one page — the appendices —
`manuscript:` is a list.

`title`, `subtitle`, `description`, `keywords` and `number` must equal the
cover's values in Layer 4 (`number` matches the cover's `order`). Nothing here
is read by Quarto: `manuscripts/` is outside `project.render`.

---

## Content fragments — `_NN-*.qmd`

No front matter at all. Body text starting at `##`.

The leading underscore keeps Quarto from rendering them standalone. They must
sit in the same directory as the file that includes them; a missing or moved
fragment produces `could not find file _00-executive-summary.qmd`.

**Edit fragments. Never edit a wrapper except to change its title.**

Every fragment closes with a `---` rule, which the PDF renders as the part
separator (`TYPOGRAPHY.md` § 3). It is the source that places the rule, not the
template, so a fragment written without one produces a report whose parts run
together. The Prologue was the one document written without them.

---

## Checklist for each new report

1. Put the manuscript at `manuscripts/rNN-<slug>.md` and give it the front matter
   of Layer 0. Then `mkdir reports/rNN`.
2. Write `_metadata.yml` with `title-block-style: none`, `date`,
   `date-modified`, `citation` (number = NN). `citation.number` is also what
   selects the numbered form of the PDF colophon.
3. Split the source into `_NN-*.qmd` fragments, each starting at `##` and
   closing with the manuscript's `---` rule. Copy the prose as written —
   including apostrophes after digits (`Report 1's`), which
   `_filters/typst-apostrophe.lua` handles.
4. Write one wrapper per fragment: `format: html`, `title`, one include.
5. Write `index.qmd`: cover fields, `title-block-style: default`, PDF link,
   contents table.
6. Write `rNN-*.qmd`: `format: typst`, level-1 headings, all includes.
7. Add the report's section to `website.sidebar.contents` in `_quarto.yml`.
   The `section:` label must be identical to the cover's `title`.
8. Fill in the manuscript's `chapters:` map with the published titles chosen
   in steps 4 and 6.
9. `quarto render`, then confirm: A4 (210×297 mm), no stray HTML twin of the
   PDF source, previous/next arrows chain correctly through the chapters.
10. `python tools/verify_pdf.py` on the report PDF — expect 12/12.

---

---

## PDF cover page and typography

Page 1 carries a left-aligned title section, a rule, and the full table of
contents. The body starts on page 2.

**Exact sizes, weights, colours and spacing are specified in
[`TYPOGRAPHY.md`](TYPOGRAPHY.md).** That file is the single place to change
them; do not scatter typographic values through report front matter.

### Choosing a different body serif

Any replacement must be redistributable, so that it can be committed to
`_fonts/` and render identically on a GitHub Actions runner. Candidates that
qualify, all under the SIL Open Font License:

| Face | Character | Note |
| --- | --- | --- |
| Source Serif 4 | Contemporary transitional, large x-height | Current choice. Six weights, good italics. |
| Literata | Sturdier, warmer, book-like | Variable font — pin a static instance, Typst may pick an unintended weight. |
| IBM Plex Serif | Corporate, slightly slab | Pairs with IBM Plex Sans if the sans is changed too. |
| Spectral | Distinctive, screen-designed | More stylised; sets slightly narrower. |
| PT Serif | Plain, economical | Fits more text per page; less refined italics. |

Two criteria matter more than taste for this series:

- **Lining figures by default.** These reports are dense with numbers
  (`$285B`, `46.4%`, `2026`). Old-style figures — the default in EB Garamond
  and several other literary serifs — read as decorative in a table of
  percentages. All five faces above default to lining figures.
- **A real italic, not a slanted roman.** Emphasis carries argument in these
  reports; a synthesised oblique degrades it.

To swap: place the files in `_fonts/`, change `mainfont`, re-render, and check
the embedded font table with `pypdf` rather than trusting the visual — Typst
falls back silently.

### Web typography

The site is set entirely in Inter, self-hosted from `assets/fonts/*.woff2`.
No CDN request is made, so the site has no third-party dependency and the web
matches the PDF's heading face exactly.

The `@font-face` `url()` in `assets/fonts/inter.scss` is written relative to
the **project root**, not to the partial. Quarto resolves it at compile time
and copies the files next to the generated theme CSS.

### Typst format block

```yaml
format:
  typst:
    template-partials:
      - _partials/typst-show.typ
      - _partials/typst-template.typ
    papersize: a4
    margin: { x: 2.5cm, y: 2.5cm }
    fontsize: 11pt
    linestretch: 1.15
    font-paths: ["_fonts"]
    mainfont: "Source Serif 4"
    headingfont: "Inter"
    titlecolor: "2251FF"        # no leading '#' — Typst rejects it
    series-label: "The Intelligence Economy · A Wisdom Hill Research Series"
    series-title: "The Intelligence Economy"
    series-url: "https://wisdomhill.github.io/intelligence-economy/"
    toc: true
    toc-depth: 2
```

`headingfont`, `titlecolor`, `series-label`, `series-title` and `series-url`
are **custom** keys read only by the overridden partials. They are not standard Quarto options; renaming them
requires editing `_partials/typst-show.typ` as well.

`series-label` is display text for the cover eyebrow. The citation metadata
still comes from `citation.container-title`, which stays clean
(`The Intelligence Economy`) so exported citations are not polluted with the
descriptor.

`series-title` and `series-url` feed the closing colophon on the last page of
every PDF (`TYPOGRAPHY.md` § 3b). They exist because the template cannot reach
the values otherwise: `citation.container-title` carries the series name but
only inside `reports/rNN/`, and `website.site-url` is not passed through to
Typst at all. `series-url` therefore duplicates `site-url` by necessity — both
are covered by the domain-change check in `HANDOFF.md`.

Because `series-label` lives here, in Layer 1, **every** document in the series
carries the eyebrow — the Prologue and the Epilogue as much as a numbered
report, and without any of them needing a `_metadata.yml`. The template used to
gate the eyebrow on `citation.container-title`, a Layer 3 value, which silently
dropped it from anything outside `reports/rNN/`; it now gates on `series-label`
and falls back to the citation field.

### What the partials do

- `typst-show.typ` forwards `citation.container-title`, `series-label`,
  `headingfont` and `titlecolor` into the template.
- `typst-template.typ` renders the left-aligned cover block, applies
  `headingfont` to every document heading, sets the contents in the sans face
  at 10.5pt, and breaks the page after the contents.

Four Typst constraints govern these edits, and each will bite anyone changing
the partials:

1. `set page(...)` is illegal inside a container; page configuration belongs at
   the template's top level.
2. A `set` rule is scoped to its enclosing block, so a rule inside
   `if toc { }` affects only the contents.
3. `rgb()` rejects a leading `#`, so `titlecolor` is stored without one.
4. The template's default `heading-line-height` (0.65em) collides the title
   and subtitle baselines; the cover block sets its own leading instead.

Do not edit `_partials/` to change per-report content. They are series-wide
typography. Everything report-specific belongs in front matter.

---

## Settled

`copyright.holder` is `Wisdom Hill` — confirmed as the correct legal entity for
the copyright notice. `LICENSE`, `README.md`, and the page footer match.
`Wisdom Hill Research` is the research imprint and the author only; it holds no
copyright of its own in this series.
