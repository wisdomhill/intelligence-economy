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
| `_filters/typst-apostrophe.lua` | Rescues the apostrophe next to a digit. Without it every `Report 1's` in the PDF becomes `Report 1′s`, and every `Cloud Next '26` becomes `Cloud Next ‘26`. |
| `_fonts/` (3.7 MB, 14 files) | Inter and Source Serif 4. Typst substitutes silently if absent. |
| `assets/fonts/` (700 KB) | Inter woff2 for the website. |
| `styles.scss`, `theme-light.scss`, `theme-dark.scss` | Web typography and colour. |
| `reports/r01/` | The reference implementation of the document structure. |
| `manuscripts/` | The manuscripts. The only place a report exists as one document; the fragments are this text split by chapter. |
| `tools/split_manuscript.py` | Performs that split. The pandoc round-trip it runs is not optional — see below. |

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

## Splitting a manuscript into fragments

```
python tools/split_manuscript.py r08 --check     # compare, change nothing
python tools/split_manuscript.py r08 --write     # overwrite the fragments
```

A fragment is **not** the manuscript chapter copied across. The prose goes
through a pandoc markdown round-trip, and skipping it is not cosmetic: a
references chapter written with bare URLs renders as plain text rather than as
links. Report 10 shipped that way, with all thirty-seven of its reference URLs
dead, because the fragments were produced by a plain split.

Three details in that round-trip were each established by reproducing an
already-published report byte for byte:

| Detail | What goes wrong without it |
| --- | --- |
| `-tex_math_dollars` on the reader | `$1 billion ... $9 billion` parses as a math span |
| Output read from a file, not stdout | `quarto pandoc` clips its stdout on Windows, dropping ~2 KB mid-word, no error, exit 0 |
| Tables passed through verbatim | pandoc rewrites a compact pipe table as a multiline table |

`tbl-colwidths` lives only in the qmd and never in the manuscript, so
regenerating a fragment drops it. The tool reads the widths back off the
fragment it is about to overwrite and re-attaches them per table; a **new**
table, or one that has gained a column, still needs its proportions chosen by
hand.

A report whose chapter is served as two web pages — Report 5's Part IV,
Report 10's chapter 5 — has more fragments than the manuscript has chapters.
The tool stops rather than guess where the boundary falls; give it by hand.

## Figures

Report 11 is the first with figures. A manuscript references them by bare
filename:

```
![Figure 1. The AI Stack value chain — …](R11_fig1_value_chain.svg)
```

so the file has to sit **next to the qmd that includes it**, in `reports/rNN/`.
The author's copy lives in `manuscripts/` beside the manuscript, which is what
makes the manuscript render on its own; the conversion copies it across. Both
copies are committed, the same way the fragments duplicate the manuscript
prose. SVG is the format — it stays sharp in the PDF and costs a few KB.

Set figure text in **Inter**, the series heading face, and give it a fallback
stack. Typst finds it through `--font-path _fonts`, so the PDF matches the web
page.

**Size the drawing for the page, not the screen.** The text block is 16 cm, or
453.5 pt, and Quarto scales a figure to fill it, so a label's printed size is

```
printed_pt = label_px * 453.5 / canvas_width_px
```

Report 11's figures are 1600 px wide with 17 px labels, which prints at 4.8 pt
against an 11 pt body — legible but small. A canvas around **950 px** wide at
the same nominal font sizes puts labels near 8 pt. Scaling the fonts up on the
existing canvas does the same thing.

A figure also defeats `tools/verify_pdf.py`'s heading check, which finds
headings by face and size: SVG labels are set in the heading face at 4–5 pt and
read as an undersized level-3 heading. The script now ignores anything below
`MIN_HEADING_PT`, 8 pt, which nothing in the template ever sets.

## When the PDF and the web page need different column widths

`tbl-colwidths` drives both formats and there is no way to split it. Quarto
consumes the attribute before any filter runs -- including one pinned at
`pre-quarto` -- and rewrites `colspecs` afterwards, so a Lua filter cannot
reach it from either side. That was tested; do not spend the afternoon again.

What works is writing the table twice, once per format:

```
::: {.content-visible when-format="html"}
| ... |
: {tbl-colwidths="[28,16,16,40]"}
:::

::: {.content-visible when-format="typst"}
| ... |
: {tbl-colwidths="[28,30,24,18]"}
:::
```

Only in the qmd. The manuscript keeps **one** copy of the table, so it stays
readable as a document; the duplication is a publication value like
`tbl-colwidths` itself. `tools/split_manuscript.py` refuses to overwrite a
fragment containing `.content-visible`, because regenerating it from the
manuscript would collapse the pair and silently drop the print widths.

Use it sparingly -- it is two copies to keep in step. It earns its cost when
the same proportions cannot serve both: a browser column reflows to the
reader's window, while a PDF column is fixed against 16 cm of A4. Report 11's
matrix needed a wide GPU column and a narrow Storage column in print, and the
same widths on the web wrapped `Very High (direct - media files)` over four
lines.

**Forcing a break inside a word.** Typst's hyphenation dictionary will not
split every word -- it breaks `nominal` as `nomi-nal` but refuses `weighted`
at any column width. A soft hyphen (U+00AD) in the source authorises the
break. Keep it in the typst copy only: it is a print control, not the author's
text, and the manuscript should stay clean.

## Dollar signs, and the `tex-math` switch

The reports quote dollar amounts constantly, and `$1 billion ... $9 billion`
parses as a TeX math span that swallows the text between. So the conversion
reads with `tex_math_dollars` **off** by default, and
`tools/split_manuscript.py` escapes `$` inside table rows as well -- tables
never reach pandoc, and Report 12's header
`| Cumulative chip cost ($B) | YoY adds ($B) |` welded two columns into one
before that was added. `~` is escaped alongside it, for the same reason in
subscript form.

A manuscript that writes real equations turns it back on with one line in its
Layer 0 front matter:

```yaml
tex-math: true
```

Report 13 is the case: 154 dollar signs, an appendix of formulations, and
`$A_{DC}$` and `$d^2Y/dt^2$` throughout the prose. With the switch on the
reader keeps math and the table escaping leaves `$` alone. Leave it off unless
the manuscript genuinely needs it; a report cannot have it both ways, so an
author who wants both must escape the prices by hand.

`NewCMMath-Book` in the embedded-font list is the signature of math having
been typeset. `tools/verify_pdf.py` allows it, because Report 13 legitimately
sets equations -- but in a report that sets none it means a `$...$` pair was
read as math by accident, which is how Report 12's bug surfaced.

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

## Apostrophes next to digits

**Write them normally. Do not rephrase around them.**

Typst mis-sets the mark in **both** directions, and one filter covers both.

*After* a digit it is read as a unit mark and rendered as a prime, so
`Report 1's` came out as `Report 1′s`. *Before* a digit it is read as an
opening quotation mark, so a year elision comes out reversed: `Cloud Next '26`
printed as `Cloud Next ‘26`, and `'000 accelerators` as `‘000`. The second case
was found in Report 10 and had been silently wrong in Reports 5–8 as well;
correcting it changed five occurrences in four already-published PDFs.

Both are handled by `_filters/typst-apostrophe.lua`, a pandoc filter wired into
`format.typst` in `_quarto.yml`. It re-emits only apostrophes adjacent to a
digit as raw Typst, which the writer cannot normalise and Typst cannot
reinterpret. Ordinary apostrophes and both kinds of quotation mark keep their
normal smart-quote treatment, and HTML is untouched because HTML never had
either defect — which is also how to spot the defect: compare the web page
against the PDF.

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

`tools/verify_pdf.py` checks the prime case automatically — the **no primes
after digits** line. It is the fastest way to catch a regression in the filter,
which is otherwise easy to miss at a glance. The reversed-quote case has no
check of its own; it is caught by reading `'` followed by two digits in the
PDF text layer.

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

The DNS and `CNAME` steps that go with it are in `SETUP.md` § 7.

## Still open

1. Reports 2–14 and the Epilogue are not yet converted. `about.qmd` has been
   removed; the Prologue serves that purpose. The navbar keeps a commented
   slot for `epilogue.qmd`.
