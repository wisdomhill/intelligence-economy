# Setup

## 1. Requirements

Quarto 1.9 or later. Check with:

```
quarto --version
```

If the version is below 1.9, download the current release from
https://quarto.org/docs/download/ and reinstall. Typst-based PDF output
and the `grid` layout options used here need 1.9+.

No LaTeX installation is required — Typst ships inside Quarto.

## 2. Unpack

Unzip this archive so that the directory structure is preserved. The tree
must look exactly like this:

```
intelligence-economy/
  _quarto.yml
  index.qmd
  prologue.qmd
  about.qmd
  errata.qmd
  styles.scss
  theme-light.scss
  theme-dark.scss
  reports/
    r01/
      index.qmd
      01-phase-transition.qmd          <- page wrapper
      _01-phase-transition.qmd         <- body text
      ... (eight wrapper / body pairs)
      r01-the-agentic-inflection.qmd   <- PDF source
```

Files beginning with an underscore hold the body text. They are pulled in by
`{{< include >}}` and are never rendered on their own. **They must sit in the
same folder as the file that includes them.** If they are missing or moved,
Quarto reports `could not find file _00-executive-summary.qmd`.

## 3. Build

Run from the project root — the folder containing `_quarto.yml`:

```
cd intelligence-economy
quarto preview          # live preview
quarto render           # build everything into _site/
```

Running Quarto from any other folder, or on a single `.qmd` outside the
project, silently drops the theme, the sidebar, the page geometry and the
A4 paper size, because none of `_quarto.yml` is in scope.

## 4. What gets built

| Output | Source |
| --- | --- |
| One HTML page per chapter | the wrapper files |
| One PDF per report | `reports/rNN/rNN-*.qmd` |
| Listing of all reports | `index.qmd` |

## 5. Editing

Edit the underscore files. The wrappers are four lines each and only exist so
the same body text can be served as separate web pages and assembled into a
single PDF.
