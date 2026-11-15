"""Drawings: raw LaTeX (TikZ, circuitikz, ...) compiled to SVG for the website,
cached by content hash. Uses the shared styles in build/figures.tex."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

FIGURES = (Path(__file__).resolve().parent / "figures.tex").read_text(encoding="utf-8")
TIKZ_PREAMBLE = ("\\documentclass[varwidth=16cm,border=4pt]{standalone}\n"
                 "\\usepackage[utf8]{inputenc}\n" + FIGURES)


def compile_svg(code: str, tikz_dir: Path) -> str | None:
    code = re.sub(r"\\begin\{algorithm\}(\[[^\]]*\])?", r"\\begin{algorithm}[H]", code)
    src = TIKZ_PREAMBLE + "\\begin{document}\n" + code + "\n\\end{document}\n"
    key = hashlib.sha1(src.encode()).hexdigest()[:16]
    out = tikz_dir / f"{key}.svg"
    if out.exists():
        return out.name
    with tempfile.TemporaryDirectory() as tmp:
        tex = Path(tmp) / "fig.tex"
        tex.write_text(src, encoding="utf-8")
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "fig.tex"],
                           cwd=tmp, capture_output=True, text=True)
        pdf = Path(tmp) / "fig.pdf"
        if r.returncode != 0 or not pdf.exists():
            err = [l for l in r.stdout.splitlines() if l.startswith("!")][:2]
            print(f"  tikz compile failed ({key}): {' '.join(err)}", file=sys.stderr)
            return None
        r = subprocess.run(["pdftocairo", "-svg", str(pdf), str(out)], capture_output=True, text=True)
        if r.returncode != 0:
            print(f"  pdftocairo failed ({key}): {r.stderr.strip()}", file=sys.stderr)
            return None
    return out.name



FIG_SCALE = 1.3  # figures are drawn at 10pt; scale up to sit with the larger body text



def svg_width(name: str, tikz_dir: Path) -> int:
    """Display width in px for a compiled SVG: its natural size times FIG_SCALE."""
    head = (tikz_dir / name).read_text(encoding="utf-8")[:600]
    m = re.search(r'width="([\d.]+)(pt|px)?"', head)
    w = float(m.group(1)) * (4 / 3 if (m.group(2) or "pt") == "pt" else 1) if m else 400
    return round(w * FIG_SCALE)



def is_algorithm(code: str) -> bool:
    """Raw LaTeX blocks in algorithmic syntax, rendered as HTML instead of SVG."""
    return "\\begin{algorithmic}" in code
