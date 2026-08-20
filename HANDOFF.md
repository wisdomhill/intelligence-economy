# Handoff

## Short answer

**No.** `TYPOGRAPHY.md` on its own will not reproduce this PDF.

It is a *specification* — it records what the values are, so they can be
discussed and adjusted. It is not the *implementation*. The formatting is
produced by 575 lines of Typst across three template partials and by 14 font
binaries, none of which can be reconstructed from prose without drift.

Carry the whole project directory. Use `TYPOGRAPHY.md` to change things, not
to rebuild them.

---

## What must travel

| Item | Why it cannot be re-derived |
| --- | --- |
| `_partials/typst-template.typ` (192 lines) | Modified copy of a Quarto internal file. Cover block, heading rules, contents styling. |
| `_partials/typst-show.typ` (118 lines) | Forwards the custom YAML keys into the template. |
| `_partials/definitions.typ` (265 lines) | Quarto internal; only the separator rule is changed. |
| `_quarto.yml` | Wires the partials and holds the format block. |
| `_filters/typst-apostrophe.lua` | Rescues the apostrophe after a digit. Without it every `Report 1's` in the PDF becomes `Report 1′s`. |
| `_fonts/` (3.7 MB, 14 files) | Inter and Source Serif 4. Typst substitutes silently if absent. |
| `assets/fonts/` (700 KB) | Inter woff2 for the website. |
| `styles.scss`, `theme-light.scss`, `theme-dark.scss` | Web typography and colour. |
| `reports/r01/` | The reference implementation of the document structure. |
| `manuscripts/` | The manuscripts. The only place a report exists as one document; the fragments are this text split by chapter. |

The three partials began as copies of files inside the Quarto installation.
Asking a fresh session to write them from scratch produces something that
compiles but does not match — the defaults being overridden are not documented
anywhere except in those files.

## What to say in the new session

> This is a Quarto website + Typst PDF project. Read `SETUP.md`,
> `FRONTMATTER.md` and `TYPOGRAPHY.md` before changing anything.
>
> `reports/r01/` is the reference implementation. Follow its structure exactly
> for reports 2–14: content fragments as `_NN-*.qmd` with no front matter,
> four-line page wrappers that include them, an `index.qmd` cover, and a
> single `rNN-*.qmd` that assembles the fragments for the PDF.
>
> Do not edit `_partials/` unless I ask for a typographic change, and do not
> add typographic settings to report front matter.
>
> Every change to report content goes into the manuscript in `manuscripts/` as
> well as the fragment. The manuscript must stay identical to the published
> prose; its front matter records the chapter-title mapping, which is the one
> place the two layers differ by design.
>
> After rendering, run `python tools/verify_pdf.py` on the report PDF and show
> me the output.

## Required environment

- Quarto **1.9 or later**. Check with `quarto --version`.
  Below 1.9 the `grid` options are ignored; below the Typst 0.12 that Quarto
  1.9 bundles, the per-level contents sizing is ignored. Both fail silently.
- No LaTeX. Typst ships inside Quarto.
- `pip install pypdf pdfplumber` for the verification script.

**A system-installed Inter shadows `_fonts/`.** Typst merges system fonts into
the family before it reaches `--font-path`, so if the machine has Inter
installed — in particular the *variable* build
(`Inter-VariableFont_opsz,wght.ttf`, weight axis 100–900) — it satisfies every
requested weight and the committed static faces are never loaded. The PDF still
looks right, because the variable axis renders the weights, but every embedded
subset reports `Inter-Regular`, and `verify_pdf.py` then fails four checks:
`expected fonts embedded`, and all three heading sizes (which it locates by
`Inter-SemiBold`). CI runners have no Inter installed and are unaffected.

To confirm the project rather than the machine, compile the intermediate Typst
with the system fonts excluded:

```
quarto render reports/r01/r01-the-agentic-inflection.qmd --to typst -M keep-typ:true
quarto typst compile --ignore-system-fonts --font-path _fonts   reports/r01/r01-the-agentic-inflection.typ out.pdf
python tools/verify_pdf.py out.pdf
```

`quarto typst fonts --font-path _fonts --variants` lists what Typst actually
resolved, and is the fastest way to spot the shadowing.

Always run Quarto from the directory containing `_quarto.yml`. Rendering a
single `.qmd` from elsewhere drops the theme, the sidebar, the page geometry
and the A4 paper size without warning — that is what produced the earlier
US-Letter, unthemed output.

## Verifying

```
quarto render
python tools/verify_pdf.py _site/reports/r01/r01-the-agentic-inflection.pdf
```

Expected: 12/12 checks passed (a document using only one heading level,
such as the Prologue, reports the levels it does not use as n/a). The script checks page size, that Typst was the
engine, that both font families are embedded and no substitute face crept in,
that the contents sit on page 1, and that body and heading sizes and the
level-1 heading colour match `TYPOGRAPHY.md`.

If a new report renders but the check fails on fonts, the cause is almost
always a working directory outside the project root.

## Settled

- `copyright.holder` is **Wisdom Hill** — the company, not its research
  division. `Wisdom Hill Research` is the author only.
- The website is set entirely in Inter. Litera, the base theme, overrides
  paragraphs with a serif (`p { font-family: Georgia, … serif }`); `styles.scss`
  hands `p`, `li`, `dd`, `blockquote` and related elements back to the body
  font with `font-family: inherit`. Setting `$font-family-base` alone is not
  enough, and the symptom — sans headings over serif body copy — looks
  deliberate rather than broken.

## Digit-apostrophe constructions

**Write them normally. Do not rephrase around them.**

Typst reads an apostrophe following a digit as a unit mark and renders it as a
prime, so `Report 1's` came out as `Report 1′s`. This is now handled by
`_filters/typst-apostrophe.lua`, a pandoc filter wired into `format.typst` in
`_quarto.yml`. It re-emits only those apostrophes as raw Typst, which the
writer cannot normalise and Typst cannot reinterpret. Ordinary apostrophes and
both kinds of quotation mark keep their normal smart-quote treatment, and HTML
is untouched because HTML never had the defect.

Nothing simpler works, and each of these was tested through the real pipeline
before the filter was written:

| Attempt | Result |
| --- | --- |
| Plain `Report 1's` | prime |
| Curly `Report 1’s` typed into the source | prime — pandoc normalises U+2019 back to ASCII before Typst sees it |
| Word joiner or zero-width space between digit and apostrophe | prime |
| Typst `set smartquote(quotes: …)` | prime |
| Typst `set smartquote(enabled: false)` | fixed, but every quote in the document turns straight |

The earlier note in this file said rephrasing was the only fix. It was wrong
about the cause — the curly apostrophe never reaches Typst — and the twelve
rephrasings it produced across Reports 1 and 2 have been reverted to the
author's wording.

`tools/verify_pdf.py` checks for this automatically — the **no primes after
digits** line. It is the fastest way to catch a regression in the filter, which
is otherwise easy to miss at a glance.

## Colour scheme

The site defaults to light. `_quarto.yml` lists the schemes in this order:

```yaml
theme:
  light: [litera, styles.scss, theme-light.scss]
  dark:  [darkly, styles.scss, theme-dark.scss]
```

Quarto treats the **first** entry as the default — it compiles the order into
`const authorPrefersDark` in every page, which is `false` while `light:` leads.
Swapping the two lines reverts to a dark default; deleting one removes the
toggle entirely.

The toggle is remembered in `localStorage` under `quarto-color-scheme`, but
Quarto skips storage when the page is opened over `file://` and falls back to
a page-local variable, so the choice resets on every navigation. Preview over
`http://localhost` (`quarto preview`) or on the deployed site to test
persistence; opening `_site/*.html` directly will always appear to forget it.

`theme-dark.scss` sets `$navbar-bg`, `$sidebar-bg` and `$footer-bg`
explicitly. Without them Quarto paints the header with `$primary`, which is a
pale blue here because it also drives headings and links — the header text
then sits at about 1.3:1 contrast. The explicit surfaces bring it to 14.7:1.

## Citation

Every page in a report cites the **report**, not the chapter. The override
lives in `reports/rNN/_metadata.yml`, which applies to the cover, all chapter
pages and the PDF source:

```yaml
citation:
  type: report
  title: "1. The Agentic Inflection"
  container-title: "The Intelligence Economy"
  number: 1
  publisher: "Wisdom Hill"
  url: https://wisdomhill.github.io/intelligence-economy/reports/r01/
```

Without `title` and `url` here, Quarto builds the citation from each page's own
title and URL, so Part I cited itself as a work.

The author is declared in `_quarto.yml` as `name.literal`. Written as a plain
string, BibTeX parses "Wisdom Hill Research" as a personal name and emits
`author = {Hill Research, Wisdom}`. `literal` marks it as an organisation and
produces `author = {{Wisdom Hill Research}}` — the doubled braces are BibTeX's
convention for a corporate author and render as the plain name.

Quarto derives the BibTeX key from author and year and offers no override —
`citation.id` and `citation-key` are both ignored, so all fifteen reports
would emit `@report{wisdom_hill_research2026, …}`. `tools/fix_bibtex_keys.py`
runs as a project `post-render` hook and rewrites the key to
`wisdomhill_ie_rNN`, taken from the report directory name. It touches only the
rendered HTML; nothing in the source changes.

### Adding a DOI later

`citation.doi` works, but only alongside `citation.url` — with a DOI and no
URL the field is dropped. When SSRN issues one, add both to
`reports/rNN/_metadata.yml`:

```yaml
citation:
  doi: "10.2139/ssrn.1234567"
  url: "https://doi.org/10.2139/ssrn.1234567"
```

The BibTeX then carries `doi = {…}` and the rendered citation resolves through
doi.org. Replacing the GitHub Pages URL with the DOI resolver is the right
move at that point: the DOI survives a domain change, which the Pages URL does
not.

**When the domain changes**, `citation.url` must be updated in each
`reports/rNN/_metadata.yml`, and both `site-url` and `series-url` in
`_quarto.yml`. `series-url` is the copy the PDF colophon prints; it duplicates
`site-url` because `website.site-url` is not passed through to Typst:

```
grep -rn "wisdomhill.github.io" _quarto.yml reports/*/_metadata.yml
```

## Still open

1. Reports 2–14 and the Epilogue are not yet converted. `about.qmd` has been
   removed; the Prologue serves that purpose. The navbar keeps a commented
   slot for `epilogue.qmd`.
