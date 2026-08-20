-- Typst reads an apostrophe following a digit as a unit mark and renders it
-- as a prime: `Report 1's` becomes `Report 1’s` -> `Report 1′s`. Nothing in the
-- source can prevent this. Writing the curly U+2019 by hand does not work,
-- because pandoc's typst writer normalises it back to an ASCII apostrophe
-- before Typst ever sees it; zero-width and word-joiner characters do not
-- interrupt the rule either, and Typst's own `smartquote` cannot be
-- reconfigured for this case without turning every quote in the document
-- straight.
--
-- Emitting the apostrophe as raw typst is what works: the writer cannot
-- normalise it and Typst cannot reinterpret it. Only apostrophes preceded by
-- a digit are touched, so ordinary apostrophes and both kinds of quotation
-- mark keep their normal smart-quote treatment.
--
-- HTML never had the defect, so the filter is scoped to typst.
if FORMAT ~= "typst" then return {} end

function Str(el)
  if not el.text:find("%d’") then return nil end
  local out, i = {}, 1
  while true do
    local a, b = el.text:find("%d’", i)
    if not a then break end
    table.insert(out, pandoc.Str(el.text:sub(i, a)))
    table.insert(out, pandoc.RawInline("typst", "’"))
    i = b + 1
  end
  table.insert(out, pandoc.Str(el.text:sub(i)))
  return out
end
