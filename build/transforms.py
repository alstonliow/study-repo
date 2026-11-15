"""Markdown transformations shared by the website and PDF builds.

Each function takes Markdown and returns Markdown. The website applies its
steps in make_site.transform(), PDFs in make_pdf.Book.finish(); both pick
from this list, so a fix here reaches every output.
"""

from __future__ import annotations

import re

from model import OPEN, attrs_of, divs_in, fence_for


def level_badge(level) -> str:
    return f" [{level}]{{.level-badge .level-{level}}}" if level in ("easy", "medium", "hard") else ""


def add_example_levels(text: str) -> str:
    """Put a level badge at the start of example blocks that have `level`."""
    def sub(m):
        a = attrs_of(m.group(2))
        if "example" in a["classes"] and a.get("level"):
            return m.group(0) + "\n" + level_badge(a["level"]).strip()
        return m.group(0)
    return re.sub(r"^(:{3,})\s*\{(.*)\}\s*$", sub, text, flags=re.M)


def fix_claims(text: str) -> str:
    def sub(m):
        a = attrs_of(m.group(2))
        if "claim" not in a["classes"]:
            return m.group(0)
        name = a.get("name")
        head = f"**Claim** ({name})." if name else "**Claim.**"
        return f"{m.group(1)} {{.claim}}\n{head}"
    return re.sub(r"^(:{3,})\s*\{(.*)\}\s*$", sub, text, flags=re.M)


def wrap_plain_ids(text: str) -> str:
    """Quarto treats an id on a remark/claim as a cross-reference target and
    fails on the unnumbered rmk-/clm- prefixes (SPEC §5.1). Move such ids to a
    plain wrapper div, which keeps the anchor in the page."""
    lines = text.split("\n")
    for d in reversed(divs_in(text)):
        if not d.id or d.id.split("-", 1)[0] not in ("rmk", "clm"):
            continue
        i, j = d.line - 1, d.end - 1
        m = OPEN.match(lines[i])
        assert m, lines[i]
        attrs = re.sub(r"(?:^|\s)#" + re.escape(d.id) + r"(?=\s|$)", "", m.group(2), count=1).strip()
        ind0 = lines[i][:len(lines[i]) - len(lines[i].lstrip(" \t"))]
        lines[i] = f"{ind0}{m.group(1)} {{{attrs}}}"
        inner = "\n".join(lines[i:j + 1])
        f = fence_for(inner)
        ind = ind0
        lines[i:j + 1] = [f"{ind}{f} {{#{d.id} .block}}"] + lines[i:j + 1] + [f"{ind}{f}"]
    return "\n".join(lines)


def drop_plain_ids(text: str) -> str:
    """Quarto rejects ids on remarks/claims (rmk-, clm-); drop them for the PDF."""
    return re.sub(r"^(:{3,}\s*\{)#(?:rmk|clm)-[\w-]+\s*", r"\1", text, flags=re.M)


def no_headings(text: str) -> str:
    """Headings inside a problem or solution would become chapters in a PDF;
    show them as bold paragraphs (check.py also rejects them)."""
    return re.sub(r"^([ \t]*)#{1,6} (.+)$", r"\1**\2**", text, flags=re.M)


def brace_scripts(md: str) -> str:
    """LaTeX (unlike MathJax) needs braces for a command as sub/superscript: x_\\mathbb{Z}."""
    return re.sub(r"([_^])\\((?:math[a-z]+|text[a-z]*|operatorname|bm))\{([^{}]*)\}", r"\1{\\\2{\3}}", md)


def tex_escape(t: str) -> str:
    return re.sub(r"([\\&%$#_{}~^])", lambda m: {"\\": r"\textbackslash{}", "~": r"\textasciitilde{}",
                                                  "^": r"\textasciicircum{}"}.get(m.group(1), "\\" + m.group(1)), t)


# ---------------------------------------------------------------- numbered blocks
# Lines that cannot carry a title in front of them (they open a list, display
# maths, a div, a raw block, a table or a heading).
_NO_INLINE_TITLE = re.compile(r"^(\$\$|[-*+] |\d+[.)] |:::|```|\||<|\\\[|#|\[\]\{)")


def title_blocks(text: str, title_of, anchor) -> str:
    """Give numbered blocks their own title instead of Quarto's/LaTeX's numbering.

    For every block with a numbered kind (kinds.Kind.numbered, except exercises
    and figures), title_of(div) returns the title Markdown (or None to leave the
    block alone) and anchor(id) the markup that keeps its id as a link target.
    The id and name are removed from the div, so no other numbering applies.
    Line count is unchanged, so nested blocks keep their positions."""
    import kinds
    lines = text.split("\n")
    for d in reversed(divs_in(text)):
        k = kinds.of(d.id)
        if not d.id or k is None or not k.numbered or k.prefix in ("prob", "fig"):
            continue
        title = title_of(d)
        if title is None:
            continue
        i, j = d.line - 1, d.end - 1
        m = OPEN.match(lines[i])
        assert m, lines[i]
        attrs = re.sub(r"(?:^|\s)#" + re.escape(d.id) + r"(?=\s|$)", "", m.group(2), count=1)
        attrs = re.sub(r'\s*name=("[^"]*"|\'[^\']*\')', "", attrs).strip()
        ind = lines[i][:len(lines[i]) - len(lines[i].lstrip(" \t"))]
        lines[i] = f"{ind}{m.group(1)} {{{attrs}}}"
        head = anchor(d.id) + title
        p = next((x for x in range(i + 1, j) if lines[x].strip()), None)
        if p is not None and not _NO_INLINE_TITLE.match(lines[p].lstrip()):
            lines[p] = lines[p][:len(lines[p]) - len(lines[p].lstrip())] + head + " " + lines[p].lstrip()
        elif p is not None:
            lines[p] = ind + head + "\n\n" + lines[p]
        else:
            lines[i] += "\n" + ind + head
    return "\n".join(lines)


def caption_figures(text: str, label_of, anchor, cls: str = "st-figure", suffix: str = "",
                    opening: str = "") -> str:
    """Figures (fig- divs): drop Quarto's numbering; put label_of(div) in front of
    the caption (the div's last paragraph) and keep the id with anchor(id)."""
    lines = text.split("\n")
    for d in reversed(divs_in(text)):
        if not d.id or not d.id.startswith("fig-"):
            continue
        i, j = d.line - 1, d.end - 1
        m = OPEN.match(lines[i])
        assert m, lines[i]
        attrs = re.sub(r"(?:^|\s)#" + re.escape(d.id) + r"(?=\s|$)", "", m.group(2), count=1).strip()
        lines[i] = f"{m.group(1)} {{.{cls}{' ' + attrs if attrs else ''}}}" + opening
        last = next((x for x in range(j - 1, i, -1) if lines[x].strip()), None)
        if last is None or lines[last].strip().startswith(("```", ":::")):
            lines[i] += "\n" + anchor(d.id)
            continue
        first = last
        while first - 1 > i and lines[first - 1].strip() and not lines[first - 1].strip().startswith(("```", ":::")):
            first -= 1
        lines[first] = anchor(d.id) + label_of(d) + lines[first]
        lines[last] += suffix
    return "\n".join(lines)
