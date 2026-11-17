"""Prerequisite graphs as plain SVG (no external libraries).

Layered layout, top to bottom (or left to right): a note sits one layer after
its furthest prerequisite; the order inside a column is improved by a few barycentre sweeps.
Nodes are links with data-item="<note id>", so site/_assets/progress.html can colour
them by progress state. Used by make_site.py (branch pages, the global map and
chapter summaries).
"""

from __future__ import annotations

import html
import textwrap

NODE_W, NODE_H = 172, 46
COL_GAP, ROW_GAP = 64, 16
PAD = 12


def layout(nodes: list[str], edges: list[tuple[str, str]]) -> dict[str, tuple[int, int]]:
    """(column, row) for every node. edges are (prerequisite, dependent)."""
    preds = {n: [a for a, b in edges if b == n] for n in nodes}
    col: dict[str, int] = {}

    def depth(n: str, stack=()) -> int:
        if n in col:
            return col[n]
        if n in stack:                      # a cycle (check.py reports it); break it here
            return 0
        col[n] = 1 + max((depth(p, stack + (n,)) for p in preds[n]), default=-1)
        return col[n]

    for n in nodes:
        depth(n)
    columns: dict[int, list[str]] = {}
    for n in nodes:                         # keep the given (topic) order as the start
        columns.setdefault(col[n], []).append(n)
    row = {n: k for c in columns.values() for k, n in enumerate(c)}
    succs = {n: [b for a, b in edges if a == n] for n in nodes}
    for sweep in range(6):                  # barycentre ordering, alternating direction
        order = sorted(columns) if sweep % 2 == 0 else sorted(columns, reverse=True)
        for c in order:
            nbrs = preds if sweep % 2 == 0 else succs
            def key(n):
                ns = [row[m] for m in nbrs[n] if m in row]
                return (sum(ns) / len(ns)) if ns else row[n]
            columns[c].sort(key=key)
            for k, n in enumerate(columns[c]):
                row[n] = k
    return {n: (col[n], row[n]) for n in nodes}


def svg(nodes: list[str], edges: list[tuple[str, str]], label: dict[str, str], href: dict[str, str],
        faded: set[str] | frozenset[str] = frozenset(), css_class: str = "dep-graph", across: bool = False) -> str:
    """An SVG drawing of the graph. `faded` nodes (e.g. prerequisites from other
    branches) are drawn lighter."""
    if not nodes:
        return ""
    layer_pos = layout(nodes, edges)
    # across=True: layers are columns (left to right); otherwise layers are rows
    pos = layer_pos if across else {n: (r, c) for n, (c, r) in layer_pos.items()}
    col_gap, row_gap = (COL_GAP, ROW_GAP) if across else (ROW_GAP + 8, COL_GAP - 22)
    ncols = max(c for c, _ in pos.values()) + 1
    nrows = max(r for _, r in pos.values()) + 1
    width = PAD * 2 + ncols * NODE_W + (ncols - 1) * col_gap
    height = PAD * 2 + nrows * NODE_H + (nrows - 1) * row_gap

    def xy(n):
        c, r = pos[n]
        return PAD + c * (NODE_W + col_gap), PAD + r * (NODE_H + row_gap)

    out = [f'<svg class="{css_class}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
           f'width="{width}" height="{height}" role="img" aria-label="Prerequisite graph">']
    for a, b in edges:
        if a not in pos or b not in pos:
            continue
        x1, y1 = xy(a)
        x2, y2 = xy(b)
        cls = "dep-edge faded" if a in faded or b in faded else "dep-edge"
        if across:
            x1 += NODE_W
            y1 += NODE_H / 2
            y2 += NODE_H / 2
            m = (x1 + x2) / 2
            d = f"M{x1:.0f},{y1:.0f} C{m:.0f},{y1:.0f} {m:.0f},{y2:.0f} {x2 - 4:.0f},{y2:.0f}"
        else:
            x1 += NODE_W / 2
            x2 += NODE_W / 2
            y1 += NODE_H
            m = (y1 + y2) / 2
            d = f"M{x1:.0f},{y1:.0f} C{x1:.0f},{m:.0f} {x2:.0f},{m:.0f} {x2:.0f},{y2 - 4:.0f}"
        out.append(f'<path class="{cls}" d="{d}"/>')
    for n in nodes:
        x, y = xy(n)
        lines = textwrap.wrap(label[n], 24)[:2]
        if len(textwrap.wrap(label[n], 24)) > 2:
            lines[1] = lines[1][:22] + "…"
        cls = "dep-node faded" if n in faded else "dep-node"
        texts = "".join(
            f'<text x="{x + 10}" y="{y + (18 if len(lines) == 2 else 28) + 15 * k}">{html.escape(t)}</text>'
            for k, t in enumerate(lines))
        out.append(f'<a href="{html.escape(href[n])}" class="{cls}" data-item="{html.escape(n)}">'
                   f'<title>{html.escape(label[n])}</title>'
                   f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="4"/>{texts}</a>')
    out.append("</svg>")
    return "\n".join(out)
