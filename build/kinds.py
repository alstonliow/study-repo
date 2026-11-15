"""The block-kind registry: every kind of block in one table (meta/SPEC.md §5).

Everything that needs to know about kinds of blocks reads it from here: the
model, checks, the website, summaries, PDFs and (through site-data.json) the
page scripts. Adding a kind of block means adding one row.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Kind:
    prefix: str            # id prefix: def-, thm-, ...
    cls: str               # Pandoc class in the notes: .definition, .theorem, ...
    word: str              # display word: Definition, Theorem, ...
    group: str             # filter group: def, result, example, remark, figure, exercise
    numbered: bool         # gets a number (Definition 8.1.1)
    xref: bool             # may be cited with @
    summary: bool          # listed (statement only) on chapter summaries
    colour: str = ""       # colour role in figures.tex / styles.css (defc, thmc, exc)


KINDS: tuple[Kind, ...] = (
    Kind("def", "definition", "Definition", "def", True, True, True, "defc"),
    Kind("thm", "theorem", "Theorem", "result", True, True, True, "thmc"),
    Kind("prp", "proposition", "Proposition", "result", True, True, True, "thmc"),
    Kind("lem", "lemma", "Lemma", "result", True, True, True, "thmc"),
    Kind("cor", "corollary", "Corollary", "result", True, True, True, "thmc"),
    Kind("exm", "example", "Example", "example", True, True, False, "exc"),
    Kind("fig", "", "Figure", "figure", True, True, False),
    Kind("rmk", "remark", "Remark", "remark", False, False, False),
    Kind("clm", "claim", "Claim", "remark", False, False, False),
    Kind("prob", "problem", "Exercise", "exercise", True, True, False),
)

BY_PREFIX = {k.prefix: k for k in KINDS}
BY_CLASS = {k.cls: k for k in KINDS if k.cls}

# groups a reader can switch on and off (summaries, PDF, Export page), in order
GROUPS: tuple[tuple[str, str], ...] = (
    ("def", "Definitions"), ("result", "Theorems, propositions, lemmas"), ("proof", "Proofs"),
    ("example", "Examples"), ("remark", "Remarks"), ("figure", "Figures"),
    ("exercise", "Exercises"), ("synthesis", "Synthesis problems"))

ID_PREFIXES = tuple(k.prefix for k in KINDS)
XREF_PREFIXES = tuple(k.prefix for k in KINDS if k.xref)
SUMMARY_PREFIXES = tuple(k.prefix for k in KINDS if k.summary)
RESULT_PREFIXES = tuple(k.prefix for k in KINDS if k.group == "result")
NO_ID_CLASSES = {"proof", "solution"}          # never carry an id (SPEC §5.2)


def of(block_id: str | None) -> Kind | None:
    """The kind of a block from its id, or None."""
    return BY_PREFIX.get((block_id or "").split("-", 1)[0])


def word(block_id: str | None) -> str:
    k = of(block_id)
    return k.word if k else ""


def group(block_id: str | None) -> str | None:
    k = of(block_id)
    return k.group if k else None


def as_data() -> dict:
    """The registry for the page scripts (site-data.json)."""
    return {"kinds": [{"prefix": k.prefix, "class": k.cls, "word": k.word, "group": k.group}
                      for k in KINDS],
            "groups": [list(g) for g in GROUPS]}
