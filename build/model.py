"""The repository model: the single parser of notes, blocks, the taxonomy and
course files (meta/SPEC.md §11, §13).

check.py and make_site.py both build on `load()`. Nothing else parses notes.
Read-only: never writes files and never runs git.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"
META = ROOT / "meta"

NOTE_FILES = ("note.md", "example.md", "exercise.md", "solution.md")
XREF_PREFIXES = ("def", "thm", "prp", "lem", "cor", "exm", "prob", "fig")   # numbered, @-referenceable
ID_PREFIXES = XREF_PREFIXES + ("rmk", "clm")                                  # every block id (SPEC §5)
KEY_PREFIXES = {"def", "thm", "prp", "lem", "cor"}                            # listed on branch pages
PREFIX_OF_CLASS = {"definition": "def", "theorem": "thm", "proposition": "prp", "lemma": "lem",
                   "corollary": "cor", "example": "exm", "problem": "prob", "remark": "rmk",
                   "claim": "clm"}

OPEN = re.compile(r"^(:{3,})\s*\{(.*)\}\s*$")
CLOSE = re.compile(r"^(:{3,})\s*$")
REF = re.compile(r"(?<![\w@])@((?:def|thm|prp|lem|cor|exm|prob|fig|rmk|clm|rem|sec)-[A-Za-z0-9-]*[A-Za-z0-9])")
RAW = re.compile(r"^([ \t]*)```\{=latex\}\n(.*?)\n[ \t]*```", re.S | re.M)
COMMENT = re.compile(r"<!--.*?-->", re.S)
MATH = re.compile(r"\$\$.*?\$\$|(?<![\\$])\$[^$\n]+?\$", re.S)   # display and inline maths


# ---------------------------------------------------------------- text utilities
def split_front(text: str) -> tuple[dict, str]:
    """(front matter, rest). Raises yaml.YAMLError on invalid YAML."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def strip_comments(text: str) -> str:
    """Remove HTML comments (and the newline after each), as the website shows them."""
    return re.sub(r"<!--.*?-->\n?", "", text, flags=re.S)


def mask_comments(text: str) -> str:
    """Remove HTML comments but keep line numbers (for messages with file:line)."""
    return COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def attrs_of(s: str) -> dict:
    """Pandoc attribute string -> {"id", "classes", key: value, ...}."""
    out = {"classes": re.findall(r"(?:^|\s)\.([\w-]+)", s)}
    kv = dict(re.findall(r'([\w-]+)="([^"]*)"', s))
    kv.update(dict(re.findall(r"([\w-]+)='([^']*)'", s)))
    no_kv = re.sub(r'[\w-]+=("[^"]*"|\'[^\']*\')', "", s)
    out["classes"] = re.findall(r"(?:^|\s)\.([\w-]+)", no_kv)
    idm = re.search(r"(?:^|\s)#([\w-]+)", no_kv)
    out["id"] = idm.group(1) if idm else None
    out.update(kv)
    return out


def top_level_divs(text: str):
    """Yield (attrs, body) for top-level fenced divs, in order."""
    for d in divs_in(text):
        if d.depth == 0:
            yield d.attrs, d.body


def divs_in(text: str, file: str = "") -> list["Div"]:
    """All fenced divs (nested ones too), in document order, with 1-based lines."""
    lines = text.splitlines()
    out: list[Div] = []
    stack: list[Div] = []
    for i, line in enumerate(lines):
        m = OPEN.match(line)
        if m:
            d = Div(file=file, line=i + 1, attrs=attrs_of(m.group(2)), depth=len(stack))
            out.append(d)
            stack.append(d)
        elif CLOSE.match(line) and stack:
            d = stack.pop()
            d.body = "\n".join(lines[d.line:i])
            d.end = i + 1
    return out


def fence_for(body: str) -> str:
    longest = max((len(m.group(1)) for m in re.finditer(r"^(:{3,})", body, re.M)), default=2)
    return ":" * max(3, longest + 1)


def sort_key(sources: list) -> tuple:
    """Numeric position from the first source key with numbers (topic order in a branch)."""
    for s in sources or []:
        nums = re.findall(r"\d+", str(s))
        if nums:
            return tuple(int(n) for n in nums)
    return (999,)


# ---------------------------------------------------------------- model
@dataclass
class Div:
    file: str
    line: int
    attrs: dict
    depth: int
    body: str = ""
    end: int = 0

    @property
    def id(self) -> str | None:
        return self.attrs.get("id")

    @property
    def classes(self) -> list[str]:
        return self.attrs["classes"]

    @property
    def name(self) -> str:
        return self.attrs.get("name", "")

    def has(self, cls: str) -> bool:
        return cls in self.attrs["classes"]


@dataclass
class SourceFile:
    name: str
    path: Path
    raw: str
    text: str = ""      # comments removed (website form)
    masked: str = ""    # comments removed, line numbers kept
    divs: list[Div] = field(default_factory=list)   # from `masked`, with real line numbers

    def __post_init__(self):
        self.text = strip_comments(self.raw)
        self.masked = mask_comments(self.raw)
        self.divs = divs_in(self.masked, self.name)


class Note:
    """One knowledge point (a folder under notes/)."""

    def __init__(self, folder: Path):
        self.folder = folder
        self.id = str(folder.relative_to(NOTES))
        self.files: dict[str, SourceFile] = {}
        for name in NOTE_FILES:
            p = folder / name
            if p.exists():
                self.files[name] = SourceFile(name, p, p.read_text(encoding="utf-8"))
        self.front_error: str | None = None
        self.front: dict = {}
        note = self.files.get("note.md")
        body = ""
        if note:
            if not re.match(r"^---\n(.*?)\n---\n", note.raw, re.S):
                self.front_error = "missing YAML front matter"
                body = note.raw
            else:
                try:
                    self.front, body = split_front(note.raw)
                except yaml.YAMLError as exc:
                    self.front_error = f"invalid YAML ({exc})"
                    body = re.sub(r"^---\n.*?\n---\n", "", note.raw, count=1, flags=re.S)
        self.title = self.front.get("title", self.id.rsplit("/", 1)[-1])
        self.body = strip_comments(body)
        self.examples = self.files["example.md"].text if "example.md" in self.files else ""
        self.exercises = self.files["exercise.md"].text if "exercise.md" in self.files else ""
        self.solutions = self.files["solution.md"].text if "solution.md" in self.files else ""

        # labelled blocks of the page (note, examples, exercises): id -> name
        self.blocks: dict[str, str] = {}
        self.key_items: list[str] = []
        for text in (self.body, self.examples, self.exercises):
            for line in text.splitlines():
                m = OPEN.match(line)
                if m:
                    a = attrs_of(m.group(2))
                    if a["id"]:
                        self.blocks[a["id"]] = a.get("name", "")
                        if a["id"].split("-", 1)[0] in KEY_PREFIXES and a.get("name"):
                            self.key_items.append(a["name"])
        self.problems = [Div("exercise.md", 0, a, 0, b) for a, b in top_level_divs(self.exercises)
                         if "problem" in a["classes"]]
        self.problem_sources = [p.attrs.get("source", "") for p in self.problems]
        self.solution_divs = [Div("solution.md", 0, a, 0, b) for a, b in top_level_divs(self.solutions)
                              if "solution" in a["classes"]]
        self.num = ""   # display number, set by the site build

    @property
    def has_note(self) -> bool:
        return "note.md" in self.files

    @property
    def branch(self) -> str:
        return self.id.rsplit("/", 1)[0]

    @property
    def sec_label(self) -> str:
        return "sec-" + self.id.replace("/", "-")

    @property
    def display_title(self) -> str:
        return f"{self.num} {self.title}" if self.num else self.title

    def units(self) -> list[tuple[str | None, Div]]:
        """Top-level blocks of the page body (note.md, then example.md) with the
        id that decides their scope: their own id, or for a proof the block
        just before it (SPEC §13.1)."""
        out = []
        for name in ("note.md", "example.md"):
            if name not in self.files:
                continue
            last = None
            for d in self.files[name].divs:
                if d.depth:
                    continue
                if d.has("proof") and not d.has("remark"):
                    out.append((last, d))
                else:
                    last = d.id
                    out.append((d.id, d))
        return out


@dataclass
class Point:
    id: str
    title: str
    chapter: int
    covers: list[str]


class Course:
    """A course file meta/courses/<id>.yml (SPEC §13)."""

    def __init__(self, path: Path):
        self.path = path
        d = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        self.id = d.get("id", path.stem)
        self.code = d.get("code", self.id.upper())
        self.name = d.get("name") or ""
        self.institution = d.get("institution", "")
        self.source_prefix = d.get("source_prefix", "")
        self.outline_from = d.get("outline_from", "")
        self.status = d.get("status", "draft")
        self.exclude = [str(x) for x in d.get("exclude") or []]
        self.chapters = []     # [{"num", "title", "points": [Point]}]
        for ch in d.get("chapters") or []:
            pts = [Point(str(p["id"]), p.get("title", ""), ch.get("num"), [str(c) for c in p.get("covers") or []])
                   for p in ch.get("points") or []]
            self.chapters.append({"num": ch.get("num"), "title": ch.get("title", ""), "points": pts})
        self.problems: list[tuple[str, str]] = []   # (level, message) found while resolving
        # resolved by Repo.resolve_courses()
        self.whole: set[str] = set()       # notes covered as a whole
        self.parts: set[str] = set()       # blocks covered one by one
        self.excluded: set[str] = set(self.exclude)
        self.order: list[tuple[str, Point]] = []   # notes in course order, with their first point

    @property
    def points(self) -> list[Point]:
        return [p for ch in self.chapters for p in ch["points"]]

    def chapter_of(self, nid: str) -> dict | None:
        for n, p in self.order:
            if n == nid:
                return next(ch for ch in self.chapters if ch["num"] == p.chapter)
        return None


class Repo:
    def __init__(self, root: Path = ROOT):
        self.root = root
        self.errors: list[str] = []
        folders = sorted({p.parent for p in NOTES.rglob("*.md")}) if NOTES.exists() else []
        self.all_notes = [Note(f) for f in folders]            # includes folders without note.md
        self.notes = {n.id: n for n in self.all_notes if n.has_note}
        self.owner = {bid: n.id for n in self.notes.values() for bid in n.blocks}
        tax = yaml.safe_load((META / "taxonomy.yml").read_text(encoding="utf-8")) or {}
        self.parts = [(p["title"], [(b["id"], b["title"]) for b in p["branches"]]) for p in tax.get("parts", [])]
        self.branch_desc = {b["id"]: b.get("desc", "") for p in tax.get("parts", []) for b in p["branches"]}
        cdir = META / "courses"
        self.courses = [Course(p) for p in sorted(cdir.glob("*.yml"))] if cdir.exists() else []
        self.resolve_courses()

    # ------------------------------------------------------------ scope (SPEC §13)
    def resolve_courses(self) -> None:
        for c in self.courses:
            seen_points = set()
            for p in c.points:
                if p.id in seen_points:
                    c.problems.append(("error", f"duplicate point id '{p.id}'"))
                seen_points.add(p.id)
                if not p.covers:
                    c.problems.append(("warning", f"point {p.id} covers nothing"))
                for ref in p.covers:
                    if ref in self.notes:
                        nid = ref
                        c.whole.add(ref)
                    elif ref in self.owner:
                        nid = self.owner[ref]
                        c.parts.add(ref)
                    else:
                        c.problems.append(("error", f"point {p.id}: unknown note or block '{ref}'"))
                        continue
                    if nid not in (n for n, _ in c.order):
                        c.order.append((nid, p))
            for b in c.exclude:
                if b not in self.owner:
                    c.problems.append(("error", f"exclude: unknown block '{b}'"))
                elif self.owner[b] not in c.whole:
                    c.problems.append(("warning", f"exclude: '{b}' is not inside a covered note"))

    def in_scope(self, c: Course, nid: str, bid: str | None = None) -> bool:
        """Is block `bid` of note `nid` (or the note itself, bid=None) in course c?"""
        if bid is None:
            return nid in c.whole or any(self.owner.get(b) == nid for b in c.parts)
        if bid in c.excluded:
            return False
        return nid in c.whole or bid in c.parts

    def note_courses(self, n: "Note") -> list[str]:
        return [c.id for c in self.courses if self.in_scope(c, n.id)]

    def block_courses(self, n: "Note", bid: str | None) -> list[str]:
        """Courses whose scope includes this block. A block without an id
        (prose, a proof with nothing before it) follows its note."""
        return [c.id for c in self.courses
                if (self.in_scope(c, n.id) if bid is None else self.in_scope(c, n.id, bid))]

    def branch_members(self, bid: str) -> list[Note]:
        """Notes of a branch in topic order."""
        return sorted((n for n in self.notes.values() if n.branch == bid),
                      key=lambda n: (sort_key(n.front.get("sources")), n.id))


def load() -> Repo:
    return Repo()
