# The Intelligence Economy

A fifteen-part research series on how agentic artificial intelligence is
reorganising the software, consumer, and hardware-infrastructure layers of the
economy.

**Read the series:** https://wisdomhill.github.io/intelligence-economy/

Published by Wisdom Hill Research, an imprint of [Wisdom Hill](https://www.wisdomhill.net).

---

## Licensing

This repository carries two licenses.

| Content | License |
| --- | --- |
| Reports and all written material | [CC BY-NC-ND 4.0](LICENSE) |
| Source code under `code/` | [MIT](code/LICENSE) |
| Fonts under `_fonts/` | SIL Open Font License 1.1 (Inter, Source Serif 4) |

**Quotation and summary are freely permitted.** Notwithstanding the
NoDerivatives condition, brief quotation, excerpting, and short summary or
commentary are permitted for review, reporting, teaching, scholarly
discussion, and public commentary — including in commercial media — provided
the report is credited by name and linked. Translation or republication of a
report in full or in substantial part requires prior written permission,
which is generally granted on request. See [LICENSE](LICENSE) for the full
terms.

---

## Corrections

Typographical fixes are applied silently. Substantive corrections — any change
to a figure, a source, or a load-bearing claim — are recorded on the
[Errata page](https://wisdomhill.github.io/intelligence-economy/errata.html)
and reflected in the report's `date-modified` field.

To report an error, open an issue.

---

## Building locally

Requires [Quarto](https://quarto.org/docs/download/) 1.9 or later. No LaTeX
installation is needed; PDF output is produced by Typst, which ships with
Quarto.

```bash
quarto preview          # live preview at localhost:4200
quarto render           # build the full site into _site/
```

### Repository layout

```
_quarto.yml              project configuration and shared metadata
index.qmd                listing page for the series
about.qmd                series overview and methodology
errata.qmd               log of substantive corrections
reports/                 one .qmd per report
  _template.qmd          annotated front-matter template (not rendered)
  figures/               images referenced by reports
code/                    simulation and analysis code (MIT licensed)
tools/                   authoring utilities
_fonts/                  fonts bundled for reproducible PDF rendering
```

---

## Deployment

Pushing to `main` triggers `.github/workflows/publish.yml`, which renders the
site and pushes the output to the `gh-pages` branch.

Before the first automated run, initialise the branch once from a local
checkout:

```bash
quarto publish gh-pages
```

### Moving to the custom domain

Planned migration: `research.wisdomhill.net`.

1. Add a `CNAME` DNS record pointing `research` at `wisdomhill.github.io`.
2. Set the custom domain in the repository's Pages settings and enable
   *Enforce HTTPS*.
3. Create a file named `CNAME` in the project root containing the single line
   `research.wisdomhill.net`, and add `resources: [CNAME]` to `_quarto.yml`
   so that it survives each render.
4. Update `site-url` in `_quarto.yml`. Every citation URL regenerates from
   that one value.

Do not create the `CNAME` file before the DNS record resolves; doing so takes
the site offline until it does.

PDFs embed their own URL, and unlike the site they cannot be redirected.
Hold off on distributing PDF files externally until the domain is settled.
