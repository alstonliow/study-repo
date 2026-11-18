---
title: Taxonomy
version: 0.2
status: draft
---

# Taxonomy v0.2

How `notes/` is organised by topic. The list of parts, branches and notes lives
in one place only: [`taxonomy.yml`](taxonomy.yml) (titles, descriptions and the
topic order used by the website and the PDFs). This file holds the rules and the
history; it does not repeat the branch list.

Changes need the owner's approval. Ideas for later go into `meta/ideas.md`.

## 1. Rules

1. A note id is its path under `notes/`: `<field>/<area>/<branch>/<note>`, for
   example `math/discrete/sets/power-set` (`meta/SPEC.md` §2).
2. Fields are the top folders (`math`, `cs`). A field is split into areas
   (`math/discrete`, `math/probability`) or directly into branches
   (`cs/algorithms`); branches may have sub-branches (`math/discrete/logic/predicate`).
3. Every branch is listed in `taxonomy.yml` under a part, with its notes in topic
   order; each part names its field (`field:`), which groups the parts on the website. `make check` fails on a note
   that is not listed.
4. Topic order is prerequisite order: a note never requires a later one.
5. A new branch goes at the end of its part unless the owner decides otherwise, so
   that existing chapter numbers do not change.
6. Notes are moved or renamed only with `build/move_note.py`; the old id stays as
   an alias.

## 2. Fields and parts

The website shows three levels above the notes: field, part, branch. Folders and
ids are not affected by this grouping.

| Field | Part in `taxonomy.yml` | Branches (folders) |
|---|---|---|
| Mathematics | Discrete Mathematics | `math/discrete/*` |
| Mathematics | Calculus | `math/calculus/*` (functions and limits, differentiation, applications of differentiation, the definite integral, techniques of integration, applications of integration, improper integrals and series) |
| Mathematics | Linear Algebra | `math/linear-algebra/*` (systems, vector spaces, orthogonality, determinants, eigenvalues, positive definite matrices and SVD) |
| Mathematics | Probability and Statistics | `math/probability/*` |
| Computer Science | Algorithms | `cs/algorithms`, `cs/data-structures`, `cs/graph-algorithms`, `cs/dynamic-programming`, `cs/algorithm-design`, `cs/models-of-computation` |
| Computer Science | Theory of Computation | `cs/theory` (Computability and Complexity) |
| Computer Science | Cryptography | `cs/cryptography` |

### Planned structure

Three fields, each split into parts. Folders are created only when content arrives,
and knowledge goes where its content belongs, whichever course brings it (graph
theory stays in `math/discrete/graph` whether FIT1058, 6.042J or CS154 uses it).

| Field | Parts (in topic order) | Folders |
|---|---|---|
| Mathematics | Discrete Mathematics; Calculus; Linear Algebra; Probability and Statistics; later Numerical Analysis, Optimization, Information Theory | `math/discrete`, `math/calculus`, `math/linear-algebra`, `math/probability`, `math/statistics`, … |
| Computer Science | Algorithms; Theory of Computation; Cryptography; later Systems (architecture, operating systems, databases, distributed systems) | `cs/*` |
| Artificial Intelligence | later: Foundations (search and planning, probabilistic models), Machine Learning, Deep Learning, Reinforcement Learning, Vision, Language | `ai/*` |

Calculus and Linear Algebra come before Probability and Statistics because
continuous probability and statistics build on them. Knowledge parts of research
methods (experimental design, statistical evaluation) go into statistics or machine
learning; reading, reproducing and writing are practice, recorded privately, not
a field. Course order for the next additions: 18.02, 6.041 with 18.05 (18.01 and 18.06 done).

## 3. Where the sources went

| Source | Target |
|---|---|
| FIT1058 course notes, chapters 1–8 and 10 | `math/discrete/*` (functions and relations both come from chapter 2) |
| FIT1058 course notes, chapter 9 | `math/probability/discrete` |
| CS70 Notes 1–3, 5–7, 10, 11 | the matching `math/discrete` branches |
| CS70 Notes 8–9 | `math/discrete/polynomials` |
| CS70 Note 4 | `cs/algorithms` |
| CS70 Note 12 | `cs/theory` |
| CS70 Notes 13–19 | `math/probability/discrete` |
| CS70 Note 20 | `math/probability/continuous` |
| CS70 Note 21 | `math/probability/markov-chains` |
| MIT 6.006 lecture and recitation notes (Spring 2020) | `cs/data-structures`, `cs/graph-algorithms`, `cs/dynamic-programming` (new branches); `cs/algorithms` (model of computation), `cs/theory` (complexity classes); the general master theorem in `math/discrete/sequences/solving-recurrences` |
| MIT 6.046 lecture and recitation notes (Spring 2015) | `cs/algorithm-design`, `cs/models-of-computation`, `cs/cryptography` (new branches); further notes in `cs/data-structures`, `cs/graph-algorithms`, `cs/dynamic-programming` and `cs/theory`; a matrix-multiplication section in `all-pairs-shortest-paths` |
| MIT 18.06SC lecture summaries (Fall 2011), Lectures 1–33 | `math/linear-algebra/*` (new part and six branches); the linear-algebra side of Markov matrices, the Fourier matrix and incidence matrices, linked to the existing notes |
| MIT 18.01 lecture notes (Fall 2006), Lectures 1–37, and Supplementary Notes sections G, C, MVT, PI, FT, F, AV, INT | `math/calculus/*` (new part and seven branches); infinite series linked to `math/discrete/sequences` (sums and series, approximating sums) |
| MIT 6.042J textbook (MCS 2015), Chapters 1–21 | mostly existing branches; new notes in `proof` (well ordering, state machines, structural induction), `relations` (partial orders), `graph` (directed graphs, isomorphism, colouring, communication networks), `sequences` (approximating sums), `counting` (generating functions), `probability/discrete` (conditional expectation, Chernoff bounds) |

Section-level placement is recorded in the resource files (`resources/`) and the
course files (`meta/courses/`), not here.

## 4. History

- 2026-11-13: first skeleton, `math/discrete` and `math/probability` (FIT1058).
- 2026-11-16: `math/probability/standard-distributions` split into one note per distribution.
- 2026-11-17: probability split into sub-branches; the discrete notes moved from
  `math/probability/<note>` to `math/probability/discrete/<note>` (aliases kept).
- 2026-11-17: new branches `math/discrete/polynomials`, `math/probability/continuous`,
  `math/probability/markov-chains`, and the part Computer Science (`cs/algorithms`,
  `cs/theory`), all from CS70.
- 2026-11-17: `covariance-and-correlation` and `composition` split;
  `standard-distributions` moved to the end of `math/probability/continuous` as an
  overview of all distributions.
- 2026-11-17: MIT 6.042J (Mathematics for Computer Science) added as a course; 13 new notes placed in existing branches.
- 2026-11-17: MIT 6.006 (Introduction to Algorithms) added as a course; new branches `cs/data-structures`,
  `cs/graph-algorithms` and `cs/dynamic-programming` at the end of the part Computer Science; 21 new notes.
- 2026-11-18: MIT 6.046 (Design and Analysis of Algorithms) added as a course; new branches
  `cs/algorithm-design`, `cs/models-of-computation` and `cs/cryptography`; 23 new notes.
- 2026-11-18: a field level (Mathematics, Computer Science) above the parts; the part
  Computer Science split into Algorithms and Theory of Computation; the branch `cs/theory` is
  shown as Computability and Complexity. No id changed.
- 2026-11-18: Cryptography made its own part under Computer Science (it was a branch of Theory of
  Computation). No id changed.
- 2026-11-18: planned structure of three fields recorded; the part Probability renamed
  Probability and Statistics.
- 2026-11-18: MIT 18.06 (Linear Algebra) added as a course; new part Linear Algebra (field Mathematics,
  between Discrete Mathematics and Probability and Statistics) with six branches and 34 notes; homework from
  the Spring 2010 problem sets (128 problems).
- 2026-11-18: MIT 18.01 (Single Variable Calculus) added as a course; new part Calculus (field Mathematics,
  between Discrete Mathematics and Linear Algebra, owner decision) with seven branches and 33 notes; homework from
  the Fall 2006 problem sets, Part II (37 problems).
