---
title: Taxonomy
version: 0.1
status: draft
---

# Taxonomy v0.1

Topic skeleton for `notes/`. Only the top two levels and the branches are fixed
here. Leaf folders (knowledge points) are created when content is added
(`meta/SPEC.md` §2).

Changes to this file need the owner's approval. During the SPEC freeze, record
wanted changes in `meta/ideas.md`.

## 1. Top two levels

| Path | Status | Notes |
|---|---|---|
| `math/discrete` | active (first batch) | FIT1058 scope |
| `math/probability` | active (first batch) | 1058note chapter 9 only, for now |
| `cs/algorithms` | active | CS70 Note 4 (stable matching) |
| `cs/theory` | active | CS70 Note 12 (computability) |

Other fields (programming, calculus, linear algebra, analysis,
optimisation) are added in later batches.

## 2. Branches

### `math/discrete`

| Branch | Content |
|---|---|
| `sets` | Sets, subsets, power set, set operations, Cartesian product, partitions |
| `functions` | Functions, injections/surjections/bijections, inverses, composition |
| `relations` | Binary relations and their properties, equivalence relations |
| `proof` | Theorems and proofs, proof techniques, induction |
| `logic/propositional` | Truth values, connectives, laws, normal forms |
| `logic/predicate` | Predicates, quantifiers |
| `sequences` | Sequences, recurrences, limits, big-O, sums and series |
| `number-theory` | Divisibility, gcd, modular arithmetic, totient, Diffie–Hellman |
| `counting` | Addition/multiplication principles, inclusion–exclusion, selection |
| `graph` | Graphs, walks, connectivity, trees, planarity |

### `math/probability`

| Branch | Content |
|---|---|
| `discrete` | Sample spaces, events, conditional probability, random variables, expectation and variance, discrete distributions, concentration, applications |
| `continuous` | (planned, CS70 Note 20) Continuous random variables, exponential and normal distributions, central limit theorem |
| `markov-chains` | (planned, CS70 Note 21) Finite Markov chains |

The discrete notes moved from `math/probability/<note>` to
`math/probability/discrete/<note>` on 2026-11-17 (old ids kept as aliases).

### `cs`

Added 2026-11-17 as the part "Computer Science" (CS70 Notes 4 and 12).

| Branch | Content |
|---|---|
| `algorithms` | Design and analysis of algorithms; for now stable matching |
| `theory` | Computability: self-reference, the halting problem, reductions, incompleteness |

## 3. Mapping from 1058note chapters

Source: `FIT1058_course/notes/chapters/`. Leaf names are decided per chapter during
migration (P3/P7), not here.

| 1058note chapter | Target |
|---|---|
| 01 Sets | `math/discrete/sets` |
| 02 Functions, from "Definitions" to "Counting functions" | `math/discrete/functions` |
| 02 Functions, from "Binary relations" to "Counting relations" | `math/discrete/relations` |
| 03 Proofs | `math/discrete/proof` |
| 04 Propositional Logic | `math/discrete/logic/propositional` |
| 05 Predicate Logic | `math/discrete/logic/predicate` |
| 06 Sequences & Series | `math/discrete/sequences` |
| 07 Number Theory | `math/discrete/number-theory` |
| 08 Counting & Combinatorics | `math/discrete/counting` |
| 09 Probability | `math/probability/discrete` |
| 10 Graph Theory | `math/discrete/graph` |
| 11 Notation summary | `meta/notation.md` (not a knowledge point) |

The exercises volume (`FIT1058_course/exercises/chapters/`) follows the same
mapping. Its chapters 09–10 (probability 1–2) map to `math/probability/discrete`, and
11–12 (graph theory 1–2) map to `math/discrete/graph`.
