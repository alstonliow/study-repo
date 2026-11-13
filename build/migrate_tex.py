#!/usr/bin/env python3
"""One-off mechanical migration of 1058note (legacy/1058note) into notes/.

Convert and tag only: wording is not changed. Environments become fenced divs,
labels become Quarto ids, \\ref becomes @-references, TikZ and other drawings
are kept as raw LaTeX blocks. Pandoc does the inline LaTeX -> Markdown work.

Usage: python3 build/migrate_tex.py            (writes notes/)
       python3 build/migrate_tex.py --dry-run  (prints the plan only)

Read-only with respect to legacy/. Never runs git.
"""

from __future__ import annotations

import re
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGACY = ROOT / "legacy" / "1058note"
NOTES = ROOT / "notes"
D = "math/discrete"
P = "math/probability"

# ---------------------------------------------------------------------------
# Mapping: subsection title -> knowledge-point folder (id), per chapter.
# Folder titles are given in FOLDER_TITLES; otherwise the first subsection title.
# ---------------------------------------------------------------------------
CHAPTERS: dict[str, dict[str, str]] = {
    "01-sets": {
        "Sets and elements": f"{D}/sets/sets-and-elements",
        "Specifying sets": f"{D}/sets/sets-and-elements",
        "Cardinality": f"{D}/sets/cardinality-and-standard-sets",
        "Sets of numbers": f"{D}/sets/cardinality-and-standard-sets",
        "Sets of strings": f"{D}/sets/cardinality-and-standard-sets",
        "Subsets and supersets": f"{D}/sets/subsets",
        "Minimal, minimum, maximal, maximum": f"{D}/sets/subsets",
        "Counting all subsets": f"{D}/sets/power-set",
        "The power set of a set": f"{D}/sets/power-set",
        "Counting subsets by size using binomial coefficients": f"{D}/sets/power-set",
        "Complement and set difference": f"{D}/sets/set-operations",
        "Union and intersection": f"{D}/sets/set-operations",
        "Symmetric difference": f"{D}/sets/symmetric-difference",
        "Cartesian product": f"{D}/sets/cartesian-product",
        "Partitions": f"{D}/sets/partitions",
    },
    "02-functions": {
        "Definitions": f"{D}/functions/definitions",
        "Notation": f"{D}/functions/definitions",
        "Some special functions": f"{D}/functions/special-functions",
        "Functions with multiple arguments and values": f"{D}/functions/special-functions",
        "Restrictions": f"{D}/functions/special-functions",
        "Injections, surjections, bijections": f"{D}/functions/injections-surjections-bijections",
        "Inverse functions": f"{D}/functions/inverse-functions",
        "Composition": f"{D}/functions/composition",
        "Cryptosystems": f"{D}/functions/cryptosystems",
        "Loose composition": f"{D}/functions/composition",
        "Counting functions": f"{D}/functions/counting",
        "Binary relations": f"{D}/relations/binary-relations",
        "Properties of binary relations": f"{D}/relations/properties",
        "Combining binary relations": f"{D}/relations/combining",
        "Equivalence relations": f"{D}/relations/equivalence-relations",
        "Relations": f"{D}/relations/counting",
        "Counting relations": f"{D}/relations/counting",
    },
    "03-proofs": {
        "Theorems and proofs": f"{D}/proof/theorems-and-proofs",
        "Logical deduction": f"{D}/proof/theorems-and-proofs",
        "Proofs of existential and universal statements": f"{D}/proof/finding-proofs",
        "Finding proofs": f"{D}/proof/finding-proofs",
        "Types of proofs": f"{D}/proof/finding-proofs",
        "Proof by symbolic manipulation": f"{D}/proof/techniques",
        "Proof by construction": f"{D}/proof/techniques",
        "Proof by cases": f"{D}/proof/techniques",
        "Proof by contradiction": f"{D}/proof/contradiction",
        "Proof by mathematical induction": f"{D}/proof/induction",
        "Induction: more examples": f"{D}/proof/induction-examples",
        "Induction: extended example": f"{D}/proof/induction-extended-example",
    },
    "04-propositional-logic": {
        "Truth values": f"{D}/logic/propositional/propositions",
        "Boolean variables": f"{D}/logic/propositional/propositions",
        "Propositions": f"{D}/logic/propositional/propositions",
        "Logical operations": f"{D}/logic/propositional/propositions",
        "Negation": f"{D}/logic/propositional/connectives",
        "Conjunction": f"{D}/logic/propositional/connectives",
        "Disjunction": f"{D}/logic/propositional/connectives",
        "De Morgan's Laws": f"{D}/logic/propositional/de-morgans-laws",
        "Implication": f"{D}/logic/propositional/implication-and-equivalence",
        "Equivalence": f"{D}/logic/propositional/implication-and-equivalence",
        "Exclusive-or": f"{D}/logic/propositional/implication-and-equivalence",
        "Tautologies and logical equivalence": f"{D}/logic/propositional/tautologies",
        "History": f"{D}/logic/propositional/tautologies",
        "Distributive Laws": f"{D}/logic/propositional/laws-of-boolean-algebra",
        "Laws of Boolean algebra": f"{D}/logic/propositional/laws-of-boolean-algebra",
        "Disjunctive Normal Form": f"{D}/logic/propositional/normal-forms",
        "Conjunctive Normal Form": f"{D}/logic/propositional/normal-forms",
        "Representing logical statements": f"{D}/logic/propositional/representing-statements",
        "Statements about how many variables are true": f"{D}/logic/propositional/representing-statements",
        "Universal sets of operations": f"{D}/logic/propositional/universal-sets-of-operations",
    },
    "05-predicate-logic": {
        "Relations, predicates, and truth-valued functions": f"{D}/logic/predicate/predicates",
        "Variables and constants": f"{D}/logic/predicate/predicates",
        "Predicates and variables": f"{D}/logic/predicate/predicates",
        "Arguments of predicates": f"{D}/logic/predicate/predicates",
        "Building logical expressions with predicates": f"{D}/logic/predicate/quantifiers",
        "Existential quantifier": f"{D}/logic/predicate/quantifiers",
        "Restricting existentially quantified variables": f"{D}/logic/predicate/quantifiers",
        "Universal quantifier": f"{D}/logic/predicate/quantifiers",
        "Restricting universally quantified variables": f"{D}/logic/predicate/quantifiers",
        "Multiple quantifiers": f"{D}/logic/predicate/multiple-quantifiers",
        "Predicate logic expressions": f"{D}/logic/predicate/multiple-quantifiers",
        "Doing logic with quantifiers": f"{D}/logic/predicate/logic-with-quantifiers",
        "Duality between quantifiers": f"{D}/logic/predicate/logic-with-quantifiers",
        "Some examples": f"{D}/logic/predicate/logic-with-quantifiers",
        "Summary of rules for logic with quantifiers": f"{D}/logic/predicate/logic-with-quantifiers",
    },
    "06-sequences-series": {
        "Definitions and notation": f"{D}/sequences/basic-sequences",
        "Recursive definitions of sequences": f"{D}/sequences/basic-sequences",
        "Arithmetic sequences": f"{D}/sequences/basic-sequences",
        "Geometric sequences": f"{D}/sequences/basic-sequences",
        "Harmonic sequences": f"{D}/sequences/basic-sequences",
        "From recursive definitions to formulas": f"{D}/sequences/solving-recurrences",
        "The Fibonacci sequence": f"{D}/sequences/fibonacci",
        "Limits of infinite sequences": f"{D}/sequences/limits",
        "Big-O notation": f"{D}/sequences/big-o",
        "Sums and summation": f"{D}/sequences/sums-and-series",
        "Finite series": f"{D}/sequences/sums-and-series",
        "Finite arithmetic series": f"{D}/sequences/sums-and-series",
        "Finite geometric series": f"{D}/sequences/sums-and-series",
        "Infinite geometric series": f"{D}/sequences/sums-and-series",
        "Harmonic numbers": f"{D}/sequences/sums-and-series",
    },
    "07-number-theory": {
        "Multiples and divisors": f"{D}/number-theory/divisibility-and-primes",
        "Prime numbers": f"{D}/number-theory/divisibility-and-primes",
        "Remainders and the mod operation": f"{D}/number-theory/remainders-and-parity",
        "Parity": f"{D}/number-theory/remainders-and-parity",
        "The greatest common divisor": f"{D}/number-theory/gcd-and-euclidean-algorithm",
        "The Euclidean algorithm": f"{D}/number-theory/gcd-and-euclidean-algorithm",
        "The gcd and integer linear combinations": f"{D}/number-theory/extended-euclidean-algorithm",
        "The extended Euclidean algorithm": f"{D}/number-theory/extended-euclidean-algorithm",
        "Coprimality": f"{D}/number-theory/coprimality",
        "Modular arithmetic": f"{D}/number-theory/modular-arithmetic",
        "Modular inverses": f"{D}/number-theory/modular-arithmetic",
        "The Euler totient function": f"{D}/number-theory/euler-totient",
        "Fast exponentiation": f"{D}/number-theory/modular-exponentiation",
        "Modular exponentiation": f"{D}/number-theory/modular-exponentiation",
        "Primitive roots": f"{D}/number-theory/primitive-roots",
        "One-way functions": f"{D}/number-theory/diffie-hellman",
        "Modular exponentiation with fixed base": f"{D}/number-theory/diffie-hellman",
        "Diffie--Hellman key agreement": f"{D}/number-theory/diffie-hellman",
    },
    "09-probability": {
        "The nature of randomness": f"{P}/sample-spaces",
        "Probability": f"{P}/sample-spaces",
        "Choice of sample space": f"{P}/sample-spaces",
        "Mutually exclusive events": f"{P}/events",
        "Operations on events": f"{P}/events",
        "Inclusion-Exclusion for probabilities": f"{P}/events",
        "Independent events": f"{P}/conditional-probability",
        "Conditional probability": f"{P}/conditional-probability",
        "Bayes' Theorem": f"{P}/bayes-theorem",
        "Random variables": f"{P}/random-variables",
        "Probability distributions": f"{P}/random-variables",
        "Expectation": f"{P}/expectation-and-variance",
        "Median": f"{P}/expectation-and-variance",
        "Mode": f"{P}/expectation-and-variance",
        "Variance": f"{P}/expectation-and-variance",
        "Uniform distribution": f"{P}/standard-distributions",
        "Binomial distribution": f"{P}/standard-distributions",
        "Poisson distribution": f"{P}/standard-distributions",
        "Geometric distribution": f"{P}/standard-distributions",
        "The coupon collector's problem": f"{P}/coupon-collector",
    },
    "10-graph-theory": {
        "Basic definitions": f"{D}/graph/basic-definitions",
        "Types of graphs": f"{D}/graph/basic-definitions",
        "Subgraphs": f"{D}/graph/basic-definitions",
        "Some special graphs": f"{D}/graph/special-graphs",
        "Degree": f"{D}/graph/degree",
        "Representing graphs": f"{D}/graph/representing-graphs",
        "Graphs and relations": f"{D}/graph/representing-graphs",
        "Walks, paths and cycles": f"{D}/graph/walks-paths-cycles",
        "Connectivity": f"{D}/graph/connectivity",
        "Bipartite graphs": f"{D}/graph/bipartite-graphs",
        "Euler tours and Hamiltonian cycles": f"{D}/graph/euler-and-hamilton",
        "Trees": f"{D}/graph/trees",
        "Properties of trees": f"{D}/graph/trees",
        "Forests": f"{D}/graph/forests-and-spanning-trees",
        "Spanning trees": f"{D}/graph/forests-and-spanning-trees",
        "Planarity": f"{D}/graph/planarity",
        "Games on graphs": f"{D}/graph/games-on-graphs",
    },
}

FOLDER_TITLES = {
    f"{D}/sets/sets-and-elements": "Sets and Elements",
    f"{D}/sets/cardinality-and-standard-sets": "Cardinality and Standard Sets",
    f"{D}/sets/subsets": "Subsets",
    f"{D}/sets/power-set": "The Power Set",
    f"{D}/sets/set-operations": "Complement, Difference, Union and Intersection",
    f"{D}/functions/definitions": "Functions: Definitions and Notation",
    f"{D}/functions/special-functions": "Special Functions and Restrictions",
    f"{D}/functions/composition": "Composition",
    f"{D}/relations/counting": "Relations and Counting Relations",
    f"{D}/proof/theorems-and-proofs": "Theorems, Proofs and Logical Deduction",
    f"{D}/proof/finding-proofs": "Finding Proofs",
    f"{D}/proof/techniques": "Proof by Manipulation, Construction and Cases",
    f"{D}/logic/propositional/propositions": "Truth Values and Propositions",
    f"{D}/logic/propositional/connectives": "Negation, Conjunction and Disjunction",
    f"{D}/logic/propositional/implication-and-equivalence": "Implication, Equivalence and Exclusive-or",
    f"{D}/logic/propositional/tautologies": "Tautologies and Logical Equivalence",
    f"{D}/logic/propositional/laws-of-boolean-algebra": "Laws of Boolean Algebra",
    f"{D}/logic/propositional/normal-forms": "Normal Forms",
    f"{D}/logic/propositional/representing-statements": "Representing Logical Statements",
    f"{D}/logic/predicate/predicates": "Predicates",
    f"{D}/logic/predicate/quantifiers": "Quantifiers",
    f"{D}/logic/predicate/multiple-quantifiers": "Multiple Quantifiers",
    f"{D}/logic/predicate/logic-with-quantifiers": "Doing Logic with Quantifiers",
    f"{D}/sequences/basic-sequences": "Sequences: Definitions and Basic Types",
    f"{D}/sequences/sums-and-series": "Sums and Series",
    f"{D}/number-theory/divisibility-and-primes": "Divisibility and Primes",
    f"{D}/number-theory/remainders-and-parity": "Remainders and Parity",
    f"{D}/number-theory/gcd-and-euclidean-algorithm": "The GCD and the Euclidean Algorithm",
    f"{D}/number-theory/extended-euclidean-algorithm": "The Extended Euclidean Algorithm",
    f"{D}/number-theory/modular-arithmetic": "Modular Arithmetic and Inverses",
    f"{D}/number-theory/modular-exponentiation": "Modular Exponentiation",
    f"{D}/number-theory/diffie-hellman": "One-Way Functions and Diffie–Hellman",
    f"{P}/sample-spaces": "Probability and Sample Spaces",
    f"{P}/events": "Events",
    f"{P}/conditional-probability": "Independence and Conditional Probability",
    f"{P}/random-variables": "Random Variables and Distributions",
    f"{P}/expectation-and-variance": "Expectation, Median, Mode and Variance",
    f"{P}/standard-distributions": "Standard Distributions",
    f"{D}/graph/basic-definitions": "Graphs: Basic Definitions",
    f"{D}/graph/representing-graphs": "Representing Graphs",
    f"{D}/graph/trees": "Trees",
    f"{D}/graph/forests-and-spanning-trees": "Forests and Spanning Trees",
}

# Exercises: file -> (problem-id prefix, CN exercise section, {number: folder}).
def _ex(prefix, cn, mapping):
    out = {}
    for folder, nums in mapping.items():
        for n in nums:
            out[n] = folder
    return prefix, cn, out

S, F, R, PR = f"{D}/sets", f"{D}/functions", f"{D}/relations", f"{D}/proof"
LP, LQ, SQ, NT, G = (f"{D}/logic/propositional", f"{D}/logic/predicate",
                     f"{D}/sequences", f"{D}/number-theory", f"{D}/graph")
EXERCISES = {
    "01-sets": _ex("sets", "1.16", {
        f"{S}/set-operations": [1, 3, 6, 9, 10, 11, 12, 13, 14, 21],
        f"{S}/sets-and-elements": [2],
        f"{S}/power-set": [4, 5, 7, 8],
        f"{S}/symmetric-difference": [15, 16, 17, 18],
        f"{S}/cartesian-product": [19],
        f"{S}/partitions": [20, 22]}),
    "02-functions": _ex("functions", "2.19", {
        f"{F}/special-functions": [1, 2, 3],
        f"{F}/injections-surjections-bijections": [4, 7, 8, 12],
        f"{F}/definitions": [5, 6],
        f"{F}/counting": [9, 10, 11],
        f"{F}/composition": [13, 14],
        f"{F}/cryptosystems": [15],
        f"{F}/inverse-functions": [16],
        f"{R}/properties": [17, 20],
        f"{R}/combining": [18, 19],
        f"{R}/equivalence-relations": [21, 22],
        f"{R}/counting": [23, 24]}),
    "03-proofs": _ex("proofs", "3.15", {
        f"{PR}/techniques": [1],
        f"{PR}/finding-proofs": [2, 4, 5, 12, 15],
        f"{PR}/theorems-and-proofs": [3],
        f"{PR}/induction": [6, 7, 8, 9, 13],
        f"{PR}/induction-examples": [10, 11],
        f"{PR}/contradiction": [14]}),
    "04-propositional-logic": _ex("propositional", "4.21", {
        f"{LP}/propositions": [1, 2],
        f"{LP}/de-morgans-laws": [3],
        f"{LP}/laws-of-boolean-algebra": [4, 5, 7, 8, 13],
        f"{LP}/implication-and-equivalence": [6, 9, 11, 12],
        f"{LP}/tautologies": [10],
        f"{LP}/normal-forms": [14, 17, 20],
        f"{LP}/representing-statements": [15, 16, 21],
        f"{LP}/universal-sets-of-operations": [18, 19, 22, 23, 24]}),
    "05-predicate-logic": _ex("predicate", "5.16", {
        f"{LQ}/predicates": [1, 7, 8],
        f"{LQ}/quantifiers": [2],
        f"{LQ}/multiple-quantifiers": [3, 4, 5, 6, 9, 10, 11, 12, 13],
        f"{LQ}/logic-with-quantifiers": [14]}),
    "06-sequences-series": _ex("sequences", "6.16", {
        f"{SQ}/basic-sequences": [1],
        f"{SQ}/solving-recurrences": [2, 3, 4, 5, 6],
        f"{SQ}/fibonacci": [7],
        f"{SQ}/limits": [8, 9, 10],
        f"{SQ}/big-o": [11, 12],
        f"{SQ}/sums-and-series": [13, 14, 15]}),
    "07-number-theory": _ex("number-theory", "7.19", {
        f"{NT}/divisibility-and-primes": [1, 2, 5, 9],
        f"{NT}/modular-arithmetic": [3, 8, 10, 11, 15],
        f"{NT}/remainders-and-parity": [4, 6, 7],
        f"{NT}/gcd-and-euclidean-algorithm": [12],
        f"{NT}/extended-euclidean-algorithm": [13],
        f"{NT}/euler-totient": [14],
        f"{NT}/modular-exponentiation": [16],
        f"{NT}/primitive-roots": [17],
        f"{NT}/diffie-hellman": [18, 19, 20, 21]}),
    "09-probability-1": _ex("probability-1", "9.10", {
        f"{P}/sample-spaces": [1, 2, 3, 4, 5, 6, 7],
        f"{P}/events": [8, 9, 12],
        f"{P}/conditional-probability": [10, 11, 13, 14, 15],
        f"{P}/bayes-theorem": [16, 17, 18]}),
    "10-probability-2": _ex("probability-2", "10.12", {
        f"{P}/random-variables": [1, 2, 3],
        f"{P}/standard-distributions": [4, 7, 8, 9, 10],
        f"{P}/expectation-and-variance": [5, 6],
        f"{P}/coupon-collector": [11]}),
    "11-graph-theory-1": _ex("graph-1", "11.12", {
        f"{G}/basic-definitions": [1],
        f"{G}/representing-graphs": [2],
        f"{G}/degree": [3, 4],
        f"{G}/walks-paths-cycles": [5, 6, 7],
        f"{G}/bipartite-graphs": [8],
        f"{G}/euler-and-hamilton": [9, 10, 11, 12]}),
    "12-graph-theory-2": _ex("graph-2", "12.7", {
        f"{G}/trees": [1, 2, 3, 4, 5, 6],
        f"{G}/forests-and-spanning-trees": [7, 8],
        f"{G}/planarity": [9, 10, 11, 12],
        f"{G}/degree": [13]}),
}

# Chapter 8 was migrated by hand in the pilot; map its labels to existing ids.
C8 = f"{D}/counting"
PILOT_LABELS = {
    "sec:8-1": ("sec", f"{C8}/sum-and-product-rules"),
    "sec:8-2": ("sec", f"{C8}/sum-and-product-rules"),
    "sec:8-3": ("sec", f"{C8}/inclusion-exclusion"),
    "sec:8-4": ("sec", f"{C8}/derangements"),
    "sec:8-5": ("sec", f"{C8}/selection"),
    "sec:8-6": ("sec", f"{C8}/selection"),
    "sec:8-7": ("sec", f"{C8}/selection"),
    "sec:8-8": ("sec", f"{C8}/combinations"),
    "sec:8-9": ("sec", f"{C8}/stars-and-bars"),
    "thm:bijectionrule": ("blk", "thm-bijection-rule"),
    "thm:derangecount": ("blk", "thm-derangement-count"),
    "thm:derangerec": ("blk", "prp-derangement-recurrence"),
    "thm:divisionrule": ("blk", "thm-division-rule"),
    "thm:altsum": ("blk", "cor-alternating-sum"),
    "thm:hockeystick": ("blk", "prp-hockey-stick"),
}

# ---------------------------------------------------------------------------
ENV_CLASS = {
    "definition": ("definition", "def"), "theorem": ("theorem", "thm"),
    "proposition": ("proposition", "prp"), "lemma": ("lemma", "lem"),
    "corollary": ("corollary", "cor"), "example": ("example", "exm"),
    "claim": ("claim", None), "note": ("remark", None), "remark": ("remark", None),
    "proof": ("proof", None),
}
RAW_ENVS = ["tikzpicture", "circuitikz", "picture", "tikzcd", "algorithm"]
MACROS = r"""
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\I}{\mathcal{I}}
\newcommand{\power}[1]{\mathcal{P}(#1)}
\newcommand{\Collatz}{\operatorname{Collatz}}
\newcommand{\dom}{\operatorname{dom}}
\newcommand{\lcmop}{\operatorname{lcm}}
"""
PANDOC_TO = "markdown-smart-simple_tables-multiline_tables-grid_tables-header_attributes-auto_identifiers"


def sec_label(nid: str) -> str:
    return "sec-" + nid.replace("/", "-")


def slug(s: str) -> str:
    s = re.sub(r"\$[^$]*\$", "", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return "-".join(s.split("-")[:5])


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


def balanced(text: str, i: int, open_ch: str, close_ch: str) -> int:
    """text[i] == open_ch; return index just past the matching close."""
    depth = 0
    for j in range(i, len(text)):
        c = text[j]
        if c == "\\":
            continue
        if c == open_ch and (j == 0 or text[j - 1] != "\\"):
            depth += 1
        elif c == close_ch and text[j - 1] != "\\":
            depth -= 1
            if depth == 0:
                return j + 1
    raise ValueError("unbalanced")


class Converter:
    def __init__(self) -> None:
        self.used_ids: set[str] = set()
        self.labels: dict[str, tuple[str, str]] = dict(PILOT_LABELS)
        for kind, v in PILOT_LABELS.values():
            if kind == "blk":
                self.used_ids.add(v)
        self.unresolved: list[str] = []
        self.ranges: list[str] = []
        # ids already used by the hand-migrated pilot chapter
        for md in (NOTES / "math/discrete/counting").rglob("*.md"):
            self.used_ids |= set(re.findall(r"\{#([A-Za-z][\w-]*)", md.read_text(encoding="utf-8")))

    def unique(self, base: str) -> str:
        cand, n = base, 2
        while cand in self.used_ids:
            cand = f"{base}-{n}"
            n += 1
        self.used_ids.add(cand)
        return cand

    # -- tokenise LaTeX so Pandoc leaves structure alone -------------------
    def tokenise(self, tex: str, folder: str, store: dict) -> str:
        opens, raws, refs = store["opens"], store["raws"], store["refs"]

        # raw drawings (outermost), including a wrapping center env
        for env in RAW_ENVS:
            pat = re.compile(r"(\\begin\{center\}\s*)?\\begin\{%s\}.*?\\end\{%s\}(\s*\\end\{center\})?" % (env, env), re.S)
            def raw_sub(m):
                body = m.group(0)
                raws.append(body)
                return f"\n\nZZRAW{len(raws) - 1}ZZ\n\n"
            tex = pat.sub(raw_sub, tex)

        # enumerate labels
        tex = re.sub(r"\\begin\{enumerate\}\[label=\(\\alph\*\)(?:,start=(\d+))?\]",
                     lambda m: r"\begin{enumerate}[(a)]" + (r"\setcounter{enumi}{%d}" % (int(m.group(1)) - 1) if m.group(1) else ""), tex)
        tex = tex.replace(r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[(i)]")
        tex = tex.replace(r"\begin{enumerate}[label=\arabic*.]", r"\begin{enumerate}[1.]")
        tex = re.sub(r"\\item\[([^\]]*)\]", lambda m: "\\item " + m.group(1) + " ", tex)
        tex = re.sub(r"\\begin\{align\*\}", r"\\[\\begin{aligned}", tex)
        tex = re.sub(r"\\end\{align\*\}", r"\\end{aligned}\\]", tex)
        for cmd in ["bigskip", "medskip", "smallskip", "noindent", "newpage", "FloatBarrier", "qedhere"]:
            tex = re.sub(r"\\%s\b\s*" % cmd, "", tex)
        tex = re.sub(r"\\begin\{center\}|\\end\{center\}", "", tex)

        # references
        def ref_sub(m):
            refs.append(m.group("label"))
            return f"ZZREF{len(refs) - 1}ZZ"
        # "\S\ref{sec:4-16}-4.17" ranges: keep the first ref, drop the plain-text end
        def range_sub(m):
            self.ranges.append(f"{folder}: {m.group(0)}")
            return m.group(1)
        tex = re.sub(r"(\\S\\ref\{[^}]+\})-\d+\.\d+", range_sub, tex)
        word = r"(?:Theorem|Theorems|Lemma|Corollary|Proposition|Definition|Example|Claim|Section|Sections)"
        tex = re.sub(r"(?:%s~?\s*)?\\S\s*~?\\ref\{(?P<label>[^}]+)\}" % word, ref_sub, tex)
        tex = re.sub(r"%s~\\(?:eq)?ref\{(?P<label>[^}]+)\}" % word, ref_sub, tex)
        tex = re.sub(r"\\(?:eq)?ref\{(?P<label>[^}]+)\}", ref_sub, tex)

        # theorem-like environments
        env_re = re.compile(r"\\begin\{(%s)\}" % "|".join(ENV_CLASS))
        out, i = [], 0
        while True:
            m = env_re.search(tex, i)
            if not m:
                out.append(tex[i:])
                break
            out.append(tex[i:m.start()])
            env = m.group(1)
            j = m.end()
            title = ""
            k = j
            while k < len(tex) and tex[k] in " \t":
                k += 1
            if k < len(tex) and tex[k] == "[":
                end = balanced(tex, k, "[", "]")
                title = tex[k + 1:end - 1].strip()
                j = end
            lm = re.match(r"\s*\\label\{([^}]+)\}", tex[j:])
            label = None
            if lm:
                label = lm.group(1)
                j += lm.end()
            opens.append({"env": env, "title": title, "label": label, "folder": folder})
            out.append(f"\n\nZZOPEN{len(opens) - 1}ZZ\n\n")
            i = j
        tex = "".join(out)
        tex = re.sub(r"\\end\{(%s)\}" % "|".join(ENV_CLASS), "\n\nZZCLOSEZZ\n\n", tex)

        # remaining labels (sections, equations) -> remember, drop
        def lab_sub(m):
            store["loose_labels"].append(m.group(1))
            return ""
        tex = re.sub(r"\\label\{([^}]+)\}", lab_sub, tex)
        return tex

    def assign_ids(self, store: dict, folder: str) -> None:
        leaf = folder.rsplit("/", 1)[-1]
        counters: dict[str, int] = {}
        for o in store["opens"]:
            cls, prefix = ENV_CLASS[o["env"]]
            o["cls"] = cls
            o["id"] = None
            if prefix is None:
                if o["label"]:
                    self.labels[o["label"]] = ("text", "")
                continue
            if o["label"]:
                base = prefix + "-" + re.sub(r"[^a-z0-9]+", "-", o["label"].split(":", 1)[-1].lower()).strip("-")
            elif o["title"] and slug(o["title"]):
                base = prefix + "-" + slug(o["title"])
            else:
                counters[prefix] = counters.get(prefix, 0) + 1
                base = f"{prefix}-{leaf}-{counters[prefix]}"
            o["id"] = self.unique(base)
            if o["label"]:
                self.labels[o["label"]] = ("blk", o["id"])

    def pandoc(self, tex: str) -> str:
        res = subprocess.run(["pandoc", "-f", "latex", "-t", PANDOC_TO, "--wrap=preserve"],
                             input=MACROS + tex, capture_output=True, text=True)
        if res.returncode != 0:
            raise RuntimeError(res.stderr)
        return res.stdout

    @staticmethod
    def title_attr(title: str) -> str:
        t = title.replace("``", "\u201c").replace("''", "\u201d").replace("---", "\u2014").replace("--", "\u2013")
        t = re.sub(r"\\emph\{([^}]*)\}", r"*\1*", t)
        t = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", t)
        t = t.replace("\\&", "&").replace("~", " ")
        for name, rep in [("N", r"\mathbb{N}"), ("Z", r"\mathbb{Z}"), ("R", r"\mathbb{R}"), ("Q", r"\mathbb{Q}")]:
            t = re.sub(r"\\%s(?![a-zA-Z])" % name, lambda _m, r=rep: r, t)
        t = re.sub(r"\\dom(?![a-zA-Z])", r"\\operatorname{dom}", t)
        if '"' in t:
            return f"name='{t}'" if "'" not in t else 'name="%s"' % t.replace('"', "\u201d")
        return f'name="{t}"'

    def detokenise(self, md: str, store: dict) -> str:
        opens = store["opens"]
        # structure: compute nesting heights for fence lengths
        stack, height = [], {}
        for t in re.finditer(r"ZZOPEN(\d+)ZZ|ZZCLOSEZZ", md):
            if t.group(1) is not None:
                stack.append(int(t.group(1)))
                height.setdefault(int(t.group(1)), 0)
            else:
                n = stack.pop()
                if stack:
                    height[stack[-1]] = max(height.get(stack[-1], 0), height[n] + 1)
        assert not stack, "unbalanced environments"
        close_stack = []

        def open_sub(m):
            n = int(m.group(1))
            o = opens[n]
            fence = ":" * (3 + height.get(n, 0))
            close_stack.append(fence)
            parts = []
            if o["id"]:
                parts.append("#" + o["id"])
            parts.append("." + o["cls"])
            if o["title"]:
                parts.append(self.title_attr(o["title"]))
            return f"{fence} {{{' '.join(parts)}}}"

        def any_sub(m):
            if m.group(1) is not None:
                return open_sub(m)
            return close_stack.pop()
        md = re.sub(r"ZZOPEN(\d+)ZZ|ZZCLOSEZZ", any_sub, md)
        md = re.sub(r"ZZRAW(\d+)ZZ", lambda m: "```{=latex}\n" + store["raws"][int(m.group(1))].strip() + "\n```", md)
        return md

    def resolve_refs(self, md: str, store: dict, folder: str, requires: set) -> str:
        def sub(m):
            label = store["refs"][int(m.group(1))]
            target = self.labels.get(label)
            if target is None:
                self.unresolved.append(f"{folder}: {label}")
                return f"@sec-legacy-{re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')}"
            kind, val = target
            if kind == "sec":
                if val != folder:
                    requires.add(val)
                return "@" + sec_label(val)
            if kind == "blk":
                owner = self.block_owner.get(val)
                if owner and owner != folder:
                    requires.add(owner)
                return "@" + val
            self.unresolved.append(f"{folder}: {label} (unnumbered)")
            return "@sec-legacy-" + re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
        return re.sub(r"ZZREF(\d+)ZZ", sub, md)

    @staticmethod
    def tidy(md: str) -> str:
        md = re.sub(r"\n<!-- -->\n", "\n", md)
        md = re.sub(r"\n{3,}", "\n\n", md)
        return md.strip() + "\n"


def split_subsections(tex: str):
    """Yield (title, cn_ref, body) per \\subsection."""
    parts = re.split(r"\\subsection\*?\{", tex)
    for part in parts[1:]:
        close = balanced("{" + part, 0, "{", "}") - 1  # index of '}' in "{"+part
        title = part[:close - 1]
        body = part[close:]
        cn = re.search(r"%\s*CN\s+([\d.]+)", body)
        yield title, (cn.group(1) if cn else None), body


def main(dry: bool) -> int:
    conv = Converter()
    conv.block_owner = {}
    pilot_owner = {
        "thm-bijection-rule": f"{C8}/sum-and-product-rules",
        "thm-derangement-count": f"{C8}/derangements",
        "prp-derangement-recurrence": f"{C8}/derangements",
        "thm-division-rule": f"{C8}/combinations",
        "cor-alternating-sum": f"{C8}/combinations",
        "prp-hockey-stick": f"{C8}/combinations",
    }
    conv.block_owner.update(pilot_owner)

    # Pass 1: tokenise all chapters, collect labels and ids.
    folders: "OrderedDict[str, dict]" = OrderedDict()
    pending = []  # (folder, subsection title, store, tokenised tex)
    for chap, mapping in CHAPTERS.items():
        raw = (LEGACY / "notes" / "chapters" / f"{chap}.tex").read_text(encoding="utf-8")
        for title, cn, body in split_subsections(raw):
            if title not in mapping:
                raise SystemExit(f"unmapped subsection in {chap}: {title!r}")
            folder = mapping[title]
            f = folders.setdefault(folder, {"subs": [], "sources": [], "chapter": chap})
            if cn:
                f["sources"].append(f"fit1058-cn-{cn}")
            store = {"opens": [], "raws": [], "refs": [], "loose_labels": []}
            tex = conv.tokenise(strip_comments(body), folder, store)
            conv.assign_ids(store, folder)
            for o in store["opens"]:
                if o["id"]:
                    conv.block_owner[o["id"]] = folder
            for lbl in store["loose_labels"]:
                if lbl.startswith("sec:"):
                    conv.labels[lbl] = ("sec", folder)
                else:
                    conv.labels.setdefault(lbl, ("text", ""))
            pending.append((folder, title, store, tex))
            f["subs"].append(title)

    # Exercises pass 1
    ex_items = []  # (folder, pid, source, problem_tex, solution_tex, store_p, store_s)
    for fname, (prefix, cn, mapping) in EXERCISES.items():
        raw = strip_comments((LEGACY / "exercises" / "chapters" / f"{fname}.tex").read_text(encoding="utf-8"))
        pat = re.compile(r"\\begin\{exercise\}(?:\[[^\]]*\])?\{(\d+)\}(.*?)\\end\{exercise\}"
                         r"(?P<after>.*?)(?=\\begin\{exercise\}|\Z)", re.S)
        seen = set()
        for m in pat.finditer(raw):
            n = int(m.group(1))
            after = re.sub(r"\\(?:begin|end)\{solbox\}(?:\[[^\]]*\])?", "", m.group("after"))
            after = re.sub(r"\\begin\{solution\}(?:\[([^\]]*)\])?",
                           lambda s: f"\n\n\\textbf{{{s.group(1)}}}\n\n" if s.group(1) else "\n\n", after)
            after = after.replace("\\end{solution}", "\n\n")
            only_labels = re.sub(r"\\textbf\{\([a-z]+\)\}", "", after).strip()
            sol_tex = after if only_labels else None
            seen.add(n)
            if n not in mapping:
                raise SystemExit(f"unmapped exercise {fname} #{n}")
            folder = mapping[n]
            if folder not in folders and not (NOTES / folder).exists():
                raise SystemExit(f"exercise {fname} #{n} -> unknown folder {folder}")
            pid = f"prob-{prefix}-{n:02d}"
            sp = {"opens": [], "raws": [], "refs": [], "loose_labels": []}
            ptex = conv.tokenise(m.group(2), folder, sp)
            conv.assign_ids(sp, folder)
            ss, stex = None, None
            if sol_tex is not None:
                ss = {"opens": [], "raws": [], "refs": [], "loose_labels": []}
                stex = conv.tokenise(sol_tex, folder, ss)
                conv.assign_ids(ss, folder)
            ex_items.append((folder, pid, f"fit1058-cn-{cn}-q{n}", ptex, stex, sp, ss))
        missing = set(mapping) - seen
        if missing:
            raise SystemExit(f"{fname}: exercises not found: {sorted(missing)}")
        if raw.count("\\begin{exercise}") != len(seen):
            raise SystemExit(f"{fname}: some exercises not parsed")

    if dry:
        for folder, f in folders.items():
            print(folder, "<-", f["subs"])
        print(len(ex_items), "exercises")
        return 0

    # Pass 2: convert and write notes.
    bodies: "OrderedDict[str, list]" = OrderedDict()
    requires: dict[str, set] = {}
    for folder, title, store, tex in pending:
        md = conv.pandoc(tex)
        md = conv.detokenise(md, store)
        md = conv.resolve_refs(md, store, folder, requires.setdefault(folder, set()))
        bodies.setdefault(folder, []).append((title, md))

    for folder, parts in bodies.items():
        f = folders[folder]
        multi = len(parts) > 1
        title = FOLDER_TITLES.get(folder, parts[0][0].replace("--", "–"))
        chunks = []
        for sub_title, md in parts:
            md = Converter.tidy(md)
            if multi:
                chunks.append(f"## {sub_title.replace('--', '–')}\n\n{md}")
            else:
                chunks.append(md)
        sources = list(dict.fromkeys(f["sources"]))
        req = sorted(r for r in requires.get(folder, set()) if r != folder)
        yaml_title = title.replace('"', '\\"')
        front = (
            "---\n"
            f'title: "{yaml_title}"\n'
            f"sources: [{', '.join(sources)}]\n"
            f"requires: [{', '.join(req)}]\n"
            "level: core\n"
            "status: draft\n"
            "---\n\n"
            f"<!-- Migrated from 1058note notes/chapters/{f['chapter']}.tex: {'; '.join(s.replace('--', '–') for s in f['subs'])}. -->\n\n"
        )
        out = NOTES / folder / "note.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(front + "\n".join(chunks), encoding="utf-8")

    # Pass 2: exercises and solutions.
    ex_by_folder: "OrderedDict[str, list]" = OrderedDict()
    sol_by_folder: "OrderedDict[str, list]" = OrderedDict()
    src_files: dict[str, set] = {}
    for folder, pid, source, ptex, stex, sp, ss in ex_items:
        pm = conv.resolve_refs(conv.detokenise(conv.pandoc(ptex), sp), sp, folder, set())
        ex_by_folder.setdefault(folder, []).append(
            f'::: {{.problem #{pid} origin="external" source="{source}"}}\n{Converter.tidy(pm).strip()}\n:::\n')
        if stex is not None:
            sm = conv.resolve_refs(conv.detokenise(conv.pandoc(stex), ss), ss, folder, set())
            sol_by_folder.setdefault(folder, []).append(
                f'::: {{.solution for="{pid}"}}\n{Converter.tidy(sm).strip()}\n:::\n')
        src_files.setdefault(folder, set()).add(pid.rsplit("-", 1)[0])

    header = "<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->\n\n"
    for folder, items in ex_by_folder.items():
        path = NOTES / folder / "exercise.md"
        path.write_text(header + "\n".join(items), encoding="utf-8")
    for folder, items in sol_by_folder.items():
        path = NOTES / folder / "solution.md"
        path.write_text("<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->\n\n" + "\n".join(items), encoding="utf-8")

    # Fix legacy refs left in the hand-migrated pilot chapter.
    for md in (NOTES / C8).rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        def fix(m):
            label = "sec:" + m.group(1)
            t = conv.labels.get(label)
            if t and t[0] == "sec":
                return "@" + sec_label(t[1])
            return m.group(0)
        new = re.sub(r"@sec-legacy-(\d+-\d+)", fix, text)
        if new != text:
            md.write_text(new, encoding="utf-8")

    print(f"wrote {len(bodies)} notes, {len(ex_items)} problems, "
          f"{sum(len(v) for v in sol_by_folder.values())} solutions")
    if conv.ranges:
        print("section ranges reduced to their first reference:")
        for r in conv.ranges:
            print("  ", r)
    if conv.unresolved:
        print("unresolved references:")
        for u in conv.unresolved:
            print("  ", u)
    return 0


if __name__ == "__main__":
    sys.exit(main("--dry-run" in sys.argv))
