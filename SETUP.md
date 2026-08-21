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
    r02/
      ... (the same shape, eleven pairs)
  manuscripts/
    r01-the-agentic-inflection.md      <- the whole report, one file
  _partials/                           <- Typst template
  _filters/                            <- pandoc filter (PDF only)
  _fonts/                              <- Inter, Source Serif 4
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

## 6. Publishing to GitHub Pages

`.github/workflows/publish.yml` renders and deploys on every push to `main`.
It runs `quarto publish gh-pages`, which pushes the rendered site to the
`gh-pages` branch; GitHub Pages then serves that branch.

**The workflow cannot create the branch.** On a repository that has never
published, the run fails with:

```
ERROR: Unable to publish to GitHub Pages (the remote origin does not have a
branch named "gh-pages"). Use first `quarto publish gh-pages` locally ...
```

The advice in that message assumes an interactive terminal; `quarto publish
gh-pages --no-prompt` refuses to create the branch and repeats the same error.
Create it directly instead — this touches no files in the working tree:

```
blob=$(printf '' | git hash-object -w --stdin)
tree=$(printf '100644 blob %s	.nojekyll
' "$blob" | git mktree)
commit=$(git commit-tree "$tree" -m "Initialise gh-pages")
git push origin "$commit":refs/heads/gh-pages
```

Then re-run the workflow (`gh workflow run publish.yml --ref main`). It is a
one-time step; every later push deploys on its own.

`.nojekyll` matters: without it GitHub Pages runs Jekyll, which ignores
directories beginning with an underscore and would drop `site_libs/`. Quarto
writes the file on each publish, and the bootstrap commit above seeds it.

**Settings -> Pages** should read *Source: Deploy from a branch*, *Branch:
`gh-pages` / (root)*. GitHub selects this by itself when the branch appears.

### Why CI output is the reference

Render the PDFs on the runner rather than trusting a local build. A machine
with Inter installed shadows the committed `_fonts/` copies, and
`tools/verify_pdf.py` then fails four checks (see `HANDOFF.md`). The runner has
no Inter, so the deployed PDFs are the ones that match `TYPOGRAPHY.md`.

## 7. Moving to the custom domain

Planned migration: `research.wisdomhill.net`.

1. Add a `CNAME` DNS record pointing `research` at `wisdomhill.github.io`.
2. Set the custom domain in the repository's Pages settings and enable
   *Enforce HTTPS*.
3. Create a file named `CNAME` in the project root containing the single line
   `research.wisdomhill.net`, and add it to `resources:` in `_quarto.yml` so
   that it survives each render.
4. Update the three places that carry the domain. `HANDOFF.md` lists them and
   gives the grep that finds them all:

   ```
   grep -rn "wisdomhill.github.io" _quarto.yml reports/*/_metadata.yml
   ```

   `site-url` generates every citation URL, `series-url` is the copy the PDF
   colophon prints, and each report's `citation.url` is its own canonical
   address.

**Do not create the `CNAME` file before the DNS record resolves.** Doing so
takes the site offline until it does.

PDFs embed their own URL and, unlike the site, cannot be redirected. Hold off
on distributing PDF files externally until the domain is settled.
