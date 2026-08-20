
#let article(
  title: none,
  subtitle: none,
  series: none,
  series-label: none,
  headingfont: none,
  titlecolor: none,
  subtitlecolor: "2F4B8F",
  bylinecolor: "3C4A57",
  serieslabelcolor: "6E7B87",
  rulecolor: "C8D0D8",
  cover-title-size: 22pt,
  cover-title-weight: "bold",
  cover-subtitle-size: 14pt,
  cover-subtitle-weight: "semibold",
  cover-series-size: 9pt,
  cover-byline-size: 10pt,
  cover-gap-title-subtitle: 1.2em,
  cover-gap-subtitle-series: 1em,
  cover-gap-series-byline: 0.75em,
  cover-gap-byline-rule: 1em,
  cover-gap-rule-toc: 2em,
  heading1-size: 15pt,
  heading2-size: 12pt,
  heading3-size: 11pt,
  heading1-color: "2F4B8F",
  heading1-gap-after: 0.5em,
  colophon-size: 8.5pt,
  colophon-color: "6E7B87",
  colophon-gap-before: 1.5em,
  colophon-leading: 0.55em,
  title-text: none,
  series-title: none,
  series-url: none,
  report-number: none,
  license-text: none,
  copyright-holder: none,
  copyright-year: none,
  heading2-gap-after: 0.3em,
  toc-title-size: 13pt,
  toc-gap-after-title: 0.9em,
  toc-level1-size: 10.5pt,
  toc-level2-size: 9pt,
  authors: none,
  keywords: (),
  date: none,
  abstract-title: none,
  abstract: none,
  thanks: none,
  cols: 1,
  lang: "en",
  region: "US",
  font: none,
  fontsize: 11pt,
  title-size: 1.5em,
  subtitle-size: 1.25em,
  heading-family: none,
  heading-weight: "bold",
  heading-style: "normal",
  heading-color: black,
  heading-line-height: 0.65em,
  mathfont: none,
  codefont: none,
  linestretch: 1,
  sectionnumbering: none,
  linkcolor: none,
  citecolor: none,
  filecolor: none,
  toc: false,
  toc_title: none,
  toc_depth: none,
  toc_indent: 1.5em,
  doc,
) = {
  // Set document metadata for PDF accessibility
  set document(title: title, keywords: keywords)
  set document(
    author: authors.map(author => content-to-string(author.name)).join(", ", last: " & "),
  ) if authors != none and authors != ()
  set par(
    justify: true,
    leading: linestretch * 0.65em
  )
  set text(lang: lang,
           region: region,
           size: fontsize)
  set text(font: font) if font != none
  show math.equation: set text(font: mathfont) if mathfont != none
  show raw: set text(font: codefont) if codefont != none

  set heading(numbering: sectionnumbering)
  show heading: set text(font: headingfont, weight: "semibold") if headingfont != none
  show heading.where(level: 1): set text(size: heading1-size, fill: rgb(heading1-color))
  show heading.where(level: 2): set text(size: heading2-size)
  show heading.where(level: 3): set text(size: heading3-size)
  show heading.where(level: 1): it => { it; v(heading1-gap-after) }
  show heading.where(level: 2): it => { it; v(heading2-gap-after) }

  show link: set text(fill: rgb(content-to-string(linkcolor))) if linkcolor != none
  show ref: set text(fill: rgb(content-to-string(citecolor))) if citecolor != none
  show link: this => {
    if filecolor != none and type(this.dest) == label {
      text(this, fill: rgb(content-to-string(filecolor)))
    } else {
      text(this)
    }
   }

  let has-title-block = title != none or (authors != none and authors != ()) or date != none or abstract != none
  if has-title-block {
    place(
      top,
      float: true,
      scope: "parent",
      clearance: 4mm,
      block(below: 1em, width: 100%)[

        #if title != none {
          block(inset: (top: 0em, bottom: 0em), width: 100%)[
            #set par(leading: 0.5em, spacing: 0em)
            #set text(font: heading-family) if heading-family != none
            #set align(left)

            #text(size: cover-title-size, weight: cover-title-weight,
                  fill: if titlecolor != none { rgb(titlecolor) } else { black })[
              #title #if thanks != none {
                footnote(thanks, numbering: "*")
                counter(footnote).update(n => n - 1)
              }
            ]
            #(if subtitle != none {
              parbreak()
              v(cover-gap-title-subtitle)
              text(size: cover-subtitle-size, weight: cover-subtitle-weight,
                   fill: rgb(subtitlecolor))[#subtitle]
            })
          ]
        }

        #let byline = if authors != none and authors != () {
          authors.map(author => author.name).join(", ")
        } else { none }

        #block(inset: 0em, width: 100%)[
          #set text(font: headingfont) if headingfont != none
          #set align(left)

          #v(cover-gap-subtitle-series)
          // `series-label` is a series-wide display string from _quarto.yml and
          // is present on every document; `series` is citation.container-title
          // and only exists where a report supplies one. Guarding on `series`
          // alone silently dropped the eyebrow from any document without a
          // _metadata.yml — the Prologue among them.
          #if series-label != none or series != none {
            text(size: cover-series-size, weight: "medium",
                 tracking: 0.06em, fill: rgb(serieslabelcolor))[
              #upper(if series-label != none { series-label } else { series })
            ]
          }
          #if byline != none or date != none {
            parbreak()
            v(cover-gap-series-byline, weak: true)
            text(size: cover-byline-size, weight: "regular",
                 fill: rgb(bylinecolor))[
              #if byline != none [#byline]
              #if byline != none and date != none [#h(1.2em)]
              #if date != none [#date]
            ]
          }
          #v(cover-gap-byline-rule)
          #line(length: 100%, stroke: 0.6pt + rgb(rulecolor))
        ]

        #if abstract != none {
          block(inset: 2em)[
          #text(weight: "semibold")[#abstract-title] #h(1em) #abstract
          ]
        }
      ]
    )
  }

  if toc {
    block(above: cover-gap-rule-toc, below: 2em)[
    #set text(font: headingfont) if headingfont != none
    #text(size: toc-title-size, weight: "semibold")[
      #if toc_title == none { "Table of contents" } else { toc_title }
    ]
    #v(toc-gap-after-title)
    #show outline.entry.where(level: 1): set text(size: toc-level1-size, weight: "medium")
    #show outline.entry.where(level: 2): set text(size: toc-level2-size, weight: "regular")
    #outline(
      title: none,
      depth: toc_depth,
      indent: toc_indent
    );
    ]
    pagebreak(weak: true)
  }

  doc

  // Closing colophon. The web pages carry Quarto's own licence and citation
  // apparatus; the PDF travels on its own and had neither. Every value is
  // inherited, so reports 2-14 and the Epilogue acquire this without declaring
  // anything: the report number comes from `citation.number`, which the
  // Prologue does not have, and its absence is what selects the shorter form.
  //
  // No rule is drawn here. Each chapter closes with one (TYPOGRAPHY.md, 3),
  // so the last chapter's rule already separates the body from this block.
  if series-title != none {
    v(colophon-gap-before)
    block(width: 100%)[
      #set text(size: colophon-size, fill: rgb(colophon-color))
      #set text(font: headingfont) if headingfont != none
      #set par(justify: false, leading: colophon-leading)
      #set align(left)

      #series-title#if report-number != none [ · Report #report-number]\
      © #copyright-year #copyright-holder. Licensed under #license-text.\
      Quotation and summary are freely permitted with attribution.

      #let byline = if authors != none and authors != () {
        authors.map(author => author.name).join(", ")
      } else { none }
      // `title-text` rather than `title`: a title beginning "1. " is parsed
      // as an enum item when inserted as markup, which drops the number and
      // breaks the citation onto three lines.
      #let cited = if title-text != none { title-text } else { content-to-string(title) }
      Cite as: #byline. #copyright-year. “#cited.”\
      In #series-title#if report-number != none [, No. #report-number]. #copyright-holder.\
      // Pandoc escapes "//" as "/\/" when writing Typst, which survives
      // into a quoted string; the URL has to be unescaped before use.
      #if series-url != none {
        let u = series-url.replace("\\", "")
        link(u)[#u]
      }
    ]
  }
}

#set table(
  inset: 6pt,
  stroke: none
)
