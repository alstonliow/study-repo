"""PDF content assembly: which chapters, notes, blocks and exercises go into a
PDF, in which order and with which numbers (meta/SPEC.md §15). make_pdf.py
turns the options into a Book and renders Book.markdown() with LaTeX."""

from __future__ import annotations

import re

import filters
import kinds
import numbering
import outline
import refs
import transforms
from model import OPEN, REF, divs_in, fence_for
from summaries import statements

TYPES = tuple(g for g, _ in kinds.GROUPS)


# ---------------------------------------------------------------- content
class Book:
    """Assembles one document from the model according to the options."""

    def __init__(self, repo, o):
        self.repo, self.o = repo, o
        self.levels = {x.strip() for x in o.level.split(",") if x.strip()}
        self.course = None
        cid = o.scope.split(":", 1)[1] if o.scope.startswith("course:") else o.course
        if cid:
            self.course = next((c for c in repo.courses if c.id == cid), None)
            if not self.course:
                raise SystemExit(f"unknown course '{cid}'")
        if o.extra == "omit" and not self.course:
            raise SystemExit("--extra omit needs a course (--scope course:<id> or --course <id>)")
        self.branch_num = repo.number_notes()
        self.include = {x.strip() for x in o.include.split(",") if x.strip()}
        self.filter = filters.Filter(repo, frozenset(self.include), frozenset(self.levels),
                                     self.course, o.extra == "omit")
        bad = self.filter.unknown
        if bad:
            raise SystemExit(f"--include: unknown {', '.join(sorted(bad))}; use {','.join(TYPES)}")
        self.outline = None
        self.chapters = self.select(self.plan())
        self.numbering = numbering.build(repo, self.outline)    # topic or course numbers
        self.printed: set[str] = set()      # labels present in the document
        self.solutions_end: list[str] = []
        self.solutions_only: list[str] = []

    # which notes, grouped into chapters: [(title, [notes], [review folders])]
    def plan(self):
        """Chapters to print: [(title, notes, review folders)], from an outline."""
        r, o = self.repo, self.o
        if o.scope == "book" or o.scope.startswith("branch:"):
            self.outline = outline.topic(r)
            chapters = self.outline.chapters
            if o.scope.startswith("branch:"):
                b = o.scope.split(":", 1)[1]
                chapters = [ch for ch in chapters if ch.key == b]
                if not chapters:
                    raise SystemExit(f"unknown branch '{b}'")
            return [(ch.label, ch.notes, ch.reviews) for ch in chapters]
        if o.scope.startswith("course:"):
            co = outline.course(r, self.course, only_in_scope=self.o.extra == "omit")
            self.outline = co
            co.apply()                       # course numbering, as on the website when filtered
            return [(ch.label, ch.notes, ch.reviews) for ch in co.chapters]
        raise SystemExit(f"--scope must be book, branch:<id> or course:<id>, not '{o.scope}'")

    def select(self, chapters):
        """Apply --branches, --chapters and --notes."""
        o = self.o
        if o.branches:
            want = {x.strip() for x in o.branches.split(",") if x.strip()}
            chapters = [ch for ch in chapters
                        if ch[1] and (ch[1][0].branch in want or ch[1][0].branch.rsplit("/", 1)[-1] in want)]
        if o.chapters:
            want = {x.strip() for x in o.chapters.split(",") if x.strip()}
            chapters = [ch for ch in chapters if ch[0].split(" ", 1)[0] in want]
        if o.notes:
            want = {x.strip() for x in o.notes.split(",") if x.strip()}
            unknown = want - set(self.repo.notes)
            if unknown:
                raise SystemExit(f"--notes: unknown {', '.join(sorted(unknown))}")
            chapters = [(t, [n for n in ns if n.id in want], rv) for t, ns, rv in chapters]
            chapters = [ch for ch in chapters if ch[1]]
        if not chapters:
            raise SystemExit("nothing selected")
        return chapters

    def keep(self, note, bid) -> bool:
        return self.filter.in_scope(note, bid)

    def keep_problem(self, note, pid, level) -> bool:
        return self.filter.problem(note, pid, level)

    # ---- pieces
    def note_body(self, note) -> str:
        """note.md (+ example.md, code.md) without out-of-scope blocks, headings demoted."""
        parts = []
        for k, text in enumerate((note.body, note.examples, note.code)):
            text = text.strip()
            if not text:
                continue
            lines = text.split("\n")
            drop = []
            last = None
            for d in divs_in(text):
                if d.depth:
                    continue
                is_proof = d.has("proof") and not d.has("remark")
                owner = last if is_proof else d.id
                if not is_proof:
                    last = d.id
                kind = "proof" if is_proof else kinds.group(d.id)
                owner_kind = kinds.group(owner)
                if (owner and not self.keep(note, owner)) or (kind and not self.filter.shows(kind)) \
                        or (is_proof and owner_kind and not self.filter.shows(owner_kind)):
                    drop.append((d.line - 1, d.end - 1))
            for a, b in reversed(drop):
                del lines[a:b + 1]
            text = "\n".join(lines)
            text = re.sub(r"(?m)^(#{2,5}) ", r"#\1 ", text)   # ## -> ###
            if k:                                        # example.md, code.md
                if not self.filter.shows("example"):
                    continue
                text = ("### Examples\n\n", "### Code\n\n")[k - 1] + text
            parts.append(text)
        body = "\n\n".join(parts)
        for d in divs_in(body):
            if d.id:
                self.printed.add(d.id)
        return body

    no_headings = staticmethod(transforms.no_headings)

    def problems(self, note, heading: str) -> str:
        sols = {d.attrs.get("for"): d for d in note.solution_divs}
        out = []
        for k, p in enumerate(note.problems, 1):
            pid, lv = p.id, p.attrs.get("level", "")
            if not self.keep_problem(note, pid, lv):
                continue
            word = self.numbering.exercise_word(note)              # Exercise, or Review for synthesis
            num = self.numbering.exercise(note, pid, on_page=True)  # 1, 2, 3 (or 8.1 for a review)
            full = self.numbering.label(pid, note)                   # Exercise 8.1.3 / Review 8.1
            src = p.attrs.get("source", "")
            label = self.repo.sources.label(src) if src else ""
            # textbook layout: "Exercise n" on the left, source and level small on the right
            side = " · ".join(x for x in (label, lv) if x)
            head = (f"\\exercisehead{{{word}}}{{{num}}}{{{transforms.tex_escape(side)}}}")
            stmt = (f"[]{{#{pid}}}\n```{{=latex}}\n{head}\n```\n\n"
                    f"{self.no_headings(p.body.strip())}\n")
            self.printed.add(pid)
            out.append(stmt)
            sol = sols.get(pid)
            if sol is None or not sol.body.strip() or self.o.solutions == "none":
                continue
            draft = " (draft)" if sol.attrs.get("status") == "draft" else ""
            text = f"*Solution{draft}.*\n\n{self.no_headings(sol.body.strip())}\n"
            if self.o.solutions == "inline":
                out.append(text)
            elif self.o.solutions == "end":
                self.solutions_end.append(f"**{full}.**\n\n{text}")
            else:
                self.solutions_only.append(f"**{full}.**\n\n{p.body.strip()}\n\n{text}")
        return "\n\n".join(out)

    def statements_of(self, note) -> str:
        out = []
        want = lambda bid: self.filter.block(note, bid)
        for d in statements(note, want):
            f = fence_for(d.body)
            attrs = "{" + f"#{d.id} ." + d.classes[0] + (f' name="{d.name}"' if d.name else "") + "}"
            out.append(f"{f} {attrs}\n{d.body.strip()}\n{f}")
            self.printed.add(d.id)
        return "\n\n".join(out)

    # ---- document
    def markdown(self) -> str:
        o = self.o
        lines = []
        for title, notes, reviews in self.chapters:
            lines += [f"# {title}", ""]
            if o.only == "summaries":
                lines += ["## Definitions and results", ""]
                for n in notes:
                    st = self.statements_of(n)
                    if st:
                        lines += [f"### {n.display_title}", "", st, ""]
                ex = [(n, self.problems(n, n.display_title) if self.filter.shows("exercise") else "") for n in notes]
                if any(p for _, p in ex):
                    lines += ["## Exercises", ""]
                    for n, p in ex:
                        if p:
                            lines += [f"### {n.display_title}", "", p, ""]
            else:
                for n in notes:
                    self.printed.add(n.sec_label)
                    lines += [f"## {n.display_title} {{#{n.sec_label}}}", ""]
                    if o.only == "all":
                        lines += [self.note_body(n), ""]
                    probs = self.problems(n, n.display_title) if self.filter.shows("exercise") else ""
                    if probs:
                        lines += (["### Exercises", ""] if o.only == "all" else []) + [probs, ""]
            syn = [self.problems(rv, f"{title}, synthesis") for rv in reviews] if self.filter.shows("synthesis") else []
            syn = [s for s in syn if s]
            if syn:
                lines += ["## Synthesis problems", ""] + syn + [""]
        if self.solutions_end:
            lines += ["# Solutions", ""] + self.solutions_end
        return self.finish("\n".join(lines))

    def finish(self, md: str) -> str:
        """Boxes, numbered titles and captions (numbering.py), and references."""
        md = transforms.drop_plain_ids(md)
        if self.o.style == "color":
            md = boxed(md)
        md = transforms.title_blocks(md, self.block_title, lambda bid: f"[]{{#{bid}}}")
        md = italic_results(md)
        md = transforms.caption_figures(md, self.figure_label, lambda bid: f"[]{{#{bid}}}",
                                        opening="\n\n```{=latex}\n\\begin{center}\\small\n```\n",
                                        suffix="\n\n```{=latex}\n\\end{center}\n```")
        md = transforms.brace_scripts(md)
        resolver = refs.Resolver(self.repo)
        nb = self.numbering

        def ref(m):
            r = m.group(1)
            rl = resolver.resource_label(r)
            if rl:                                   # resources are not printed: plain text
                return rl
            t = resolver.find(r)
            if t is None:
                return kinds.word(r)
            if t.is_note:
                text = resolver.describe(t)
                return f"[{text}](#{r})" if r in self.printed else text
            numbered = bool(nb.block(r)) or (t.kind is not None and t.kind.prefix == "prob")
            text = nb.label(r, t.note, here[0]) if numbered else resolver.describe(t)
            return f"[{text}](#{r})" if r in self.printed else text

        def plain(m):                                # inside a block's title: no links in LaTeX arguments
            out = ref(m)
            return re.sub(r"^\[(.*)\]\(#[^)]*\)$", r"\1", out)
        here: list = [None]                          # the note being read, for cross-book labels
        out = []
        for line in md.split("\n"):
            sec = re.match(r"^## .*\{#(sec-[\w-]+)\}\s*$", line)
            if sec:
                t0 = resolver.find(sec.group(1))
                here[0] = t0.note if t0 else None
            out.append(REF.sub(plain, line) if OPEN.match(line) else REF.sub(ref, line))
        return "\n".join(out)

    def block_title(self, d) -> str:
        """LaTeX title of a numbered block: 'Theorem 8.1.2 (Name).'"""
        k = kinds.of(d.id)
        num = self.numbering.block(d.id)
        word = k.word if k else ""
        name = f" ({d.name})" if d.name else ""
        return (f"`\\textcolor{{thmheadc}}{{\\upshape `{{=latex}}**{word}{' ' + num if num else ''}**"
                f"{name}.`}}`{{=latex}}")

    def figure_label(self, d) -> str:
        num = self.numbering.block(d.id)
        return f"**Figure {num}:** " if num else ""


def italic_results(md: str) -> str:
    """Theorems, propositions, lemmas and corollaries in italics, as in LaTeX's
    plain theorem style. Line count is unchanged."""
    lines = md.split("\n")
    results = {k.cls for k in kinds.KINDS if k.group == "result"}
    for d in reversed(divs_in(md)):
        if not results & set(d.classes):
            continue
        i, j = d.line - 1, d.end - 1
        lines[i] += "\n\n```{=latex}\n\\begingroup\\itshape\n```\n"
        lines[j] = "\n```{=latex}\n\\endgroup\n```\n\n" + lines[j]
    return "\n".join(lines)


def boxed(md: str) -> str:
    """Wrap each top-level definition, result and example (with the proof that
    follows it) in a coloured box, like the website."""
    lines = md.split("\n")
    units: list[list] = []
    for d in divs_in(md):
        if d.depth:
            continue
        if d.has("proof") and not d.has("remark") and units and units[-1][2] == d.line - 2:
            units[-1][2] = d.end - 1
            continue
        k = kinds.of(d.id)
        if k and k.colour:
            units.append([k.colour, d.line - 1, d.end - 1])
    for color, a, b in reversed(units):
        lines[b + 1:b + 1] = ["", "```{=latex}", "\\end{stbox}", "```"]
        lines[a:a] = ["```{=latex}", f"\\begin{{stbox}}{{{color}}}", "```", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------- render
