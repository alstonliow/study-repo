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

Other fields (algorithms, programming, calculus, linear algebra, analysis,
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

No branches yet. Knowledge points from 1058note chapter 9 sit directly under
`math/probability/` until the P3 pilot shows whether branches are needed.

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
| 09 Probability | `math/probability` |
| 10 Graph Theory | `math/discrete/graph` |
| 11 Notation summary | `meta/notation.md` (not a knowledge point) |

The exercises volume (`FIT1058_course/exercises/chapters/`) follows the same
mapping. Its chapters 09–10 (probability 1–2) map to `math/probability`, and
11–12 (graph theory 1–2) map to `math/discrete/graph`.
