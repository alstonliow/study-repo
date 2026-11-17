-- Keep the delimiter style of ordered lists in HTML.
-- Pandoc's HTML writer emits <ol type="a"> for "(a)", "a)" and "a." alike;
-- wrap "(a)" and "a)" lists in a div whose classes name the delimiter and the
-- numbering style, so styles.css can draw the markers.
local STYLE = {
  LowerAlpha = "lower-alpha", UpperAlpha = "upper-alpha",
  LowerRoman = "lower-roman", UpperRoman = "upper-roman",
  Decimal = "decimal", DefaultStyle = "decimal", Example = "decimal",
}

function OrderedList(el)
  local delim = el.listAttributes.delimiter
  local cls
  if delim == "TwoParens" then
    cls = "list-two-parens"
  elseif delim == "OneParen" then
    cls = "list-one-paren"
  else
    return nil
  end
  local style = STYLE[el.listAttributes.style] or "decimal"
  return pandoc.Div({ el }, pandoc.Attr("", { cls, "list-" .. style }))
end
