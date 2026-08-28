-- Typst mis-sets an apostrophe that touches a digit, in both directions.
--
-- Following a digit it is read as a unit mark and rendered as a prime:
-- `Report 1’s` becomes `Report 1′s`. Preceding one it is read as an opening
-- quotation mark, so a year elision comes out reversed: `Cloud Next ’26`
-- becomes `Cloud Next ‘26`, and `’000 accelerators` becomes `‘000`.
--
-- Nothing in the source can prevent either. Writing the curly U+2019 by hand
-- does not work, because pandoc's typst writer normalises it back to an ASCII
-- apostrophe before Typst ever sees it; zero-width and word-joiner characters
-- do not interrupt the rules either, and Typst's own `smartquote` cannot be
-- reconfigured for these cases without turning every quote in the document
-- straight.
--
-- Emitting the apostrophe as raw typst is what works: the writer cannot
-- normalise it and Typst cannot reinterpret it. Only apostrophes adjacent to a
-- digit are touched, so ordinary apostrophes and both kinds of quotation mark
-- keep their normal smart-quote treatment.
--
-- HTML never had either defect, so the filter is scoped to typst.
if FORMAT ~= "typst" then return {} end

local APOS = "’"

function Str(el)
  local t = el.text
  if not (t:find("%d" .. APOS) or t:find(APOS .. "%d")) then return nil end

  local out, last, i = {}, 1, 1
  while true do
    local a, b = t:find(APOS, i, true)
    if not a then break end
    -- Adjacent on either side is enough: `’26` sits between a space and a
    -- digit, `1’s` between a digit and a letter.
    if t:sub(a - 1, a - 1):match("^%d$") or t:sub(b + 1, b + 1):match("^%d$") then
      if a > last then table.insert(out, pandoc.Str(t:sub(last, a - 1))) end
      table.insert(out, pandoc.RawInline("typst", APOS))
      last = b + 1
    end
    i = b + 1
  end
  if last <= #t then table.insert(out, pandoc.Str(t:sub(last))) end
  return out
end
