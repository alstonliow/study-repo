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
| Mathematics | Single Variable Calculus | `math/calculus/single-variable/*` (sequences and limits, differentiation, applications of differentiation, the definite integral, techniques of integration, applications of integration, improper integrals and series) |
| Mathematics | Linear Algebra | `math/linear-algebra/*` (systems, vector spaces, orthogonality, determinants, eigenvalues, positive definite matrices and SVD) |
| Mathematics | Multivariable Calculus | `math/calculus/multivariable/*` (vectors and curves in space, partial differentiation, multiple integrals, line integrals and Green's theorem, vector calculus in space) |
| Mathematics | Probability and Statistics | `math/probability/*` |
| Computer Science | Algorithms | `cs/algorithms`, `cs/data-structures`, `cs/graph-algorithms`, `cs/dynamic-programming`, `cs/algorithm-design`, `cs/models-of-computation` |
| Computer Science | Theory of Computation | `cs/theory` (Computability and Complexity) |
| Computer Science | Cryptography | `cs/cryptography` |
| Artificial Intelligence | Artificial Intelligence | `ai/machine-learning`, `ai/deep-learning`, `ai/search`, `ai/reinforcement-learning`, `ai/games`, `ai/bayesian-networks` (one part for now, split into parts when more AI courses arrive; owner decision, 2026-11-18) |

### Planned structure

Three fields, each split into parts. Folders are created only when content arrives,
and knowledge goes where its content belongs, whichever course brings it (graph
theory stays in `math/discrete/graph` whether FIT1058, 6.042J or CS154 uses it).

| Field | Parts (in topic order) | Folders |
|---|---|---|
| Mathematics | Discrete Mathematics; Single Variable Calculus; Linear Algebra; Multivariable Calculus; Probability and Statistics; later Numerical Analysis, Optimization, Information Theory | `math/discrete`, `math/calculus/single-variable`, `math/calculus/multivariable`, `math/linear-algebra`, `math/probability`, `math/statistics`, … |
| Computer Science | Algorithms; Theory of Computation; Cryptography; later Systems (architecture, operating systems, databases, distributed systems) | `cs/*` |
| Artificial Intelligence | later: Foundations (search and planning, probabilistic models), Machine Learning, Deep Learning, Reinforcement Learning, Vision, Language | `ai/*` |

Single Variable Calculus, Linear Algebra and Multivariable Calculus come before Probability and Statistics because
continuous probability and statistics build on them; Multivariable Calculus comes after Linear Algebra because it
uses its vectors, matrices and determinants (owner decision, 2026-11-18). Knowledge parts of research
methods (experimental design, statistical evaluation) go into statistics or machine
learning; reading, reproducing and writing are practice, recorded privately, not
a field. Course order for the next additions: 6.041 with 18.05 (18.01, 18.06 and 18.02 done).

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
| MIT 18.01 lecture notes (Fall 2006), Lectures 1–37, and Supplementary Notes sections G, C, MVT, PI, FT, F, AV, INT and E (exercises) | `math/calculus/single-variable/*` (new part and seven branches) |
| MIT 18.02 lecture notes (Fall 2007), Lectures 1–33, and Supplementary Notes D, M, K, TA, LS, SD, N, P, I, CV, G, V1–V6, V8–V15 and E (exercises) | `math/calculus/multivariable/*` (new part and five branches); vectors, matrices and determinants from `math/linear-algebra/systems` and `determinants` |
| MIT 6.042J textbook (MCS 2015), Chapters 1–21 | mostly existing branches; new notes in `proof` (well ordering, state machines, structural induction), `relations` (partial orders), `graph` (directed graphs, isomorphism, colouring, communication networks), `sequences` (approximating sums), `counting` (generating functions), `probability/discrete` (conditional expectation, Chernoff bounds) |
| Stanford CS221 lecture code (commit 3ac2452), Lectures 1–20 | `ai/machine-learning` (seven notes), `ai/deep-learning` (five), `ai/search` (four), `ai/reinforcement-learning` (nine), `ai/games` (five), `ai/bayesian-networks` (six); logic gaps in `math/discrete/logic` (models and entailment, inference rules, first-order inference) |
| Stanford CS221 homework (Autumn 2026), HW 1–7, written parts | 15 exercises with draft solutions in `ai/*` notes and `math/discrete/logic/propositional/inference-rules`; programming parts reserved for coursework projects |
| UC Berkeley CS188 lecture slides (Fall 2025), Lectures 2–24 (1, 25, 26 omitted) | new branches `ai/constraint-satisfaction` (five notes), `ai/decision-theory` (three), `ai/temporal-models` (two); new notes in `ai/search`, `ai/reinforcement-learning` (two), `ai/bayesian-networks` (three), `ai/machine-learning` (three), `ai/deep-learning` (two); blocks added to A*, game trees, TD learning, conditional independence |
| UC Berkeley CS188 homework (Fall 2025) HW 1–10 and discussions 1, 2, 4, 7, 11 | 13 homework and 5 discussion exercises with draft solutions; exam-prep worksheets and exam-style discussion problems not used; projects 1–5 as coursework projects |
| UC Berkeley EECS126 supplementary notes (Fall 2021), 12 notes | new branches `math/probability/random-processes` (two notes), `math/probability/information-theory` (three), `math/probability/estimation` (four); new notes in `math/probability/continuous` (three), `math/probability/markov-chains` (two), `math/probability/discrete` (random graphs), `ai/temporal-models` (Viterbi); Hoeffding added to Chernoff bounds |
| UC Berkeley EECS126 homework (Fall 2021) HW 1–14 and discussions 2, 4–9, 11, 13 | 63 homework (figures redrawn in TikZ) and 11 discussion exercises with draft solutions; midterm redos and repeated problems skipped; labs 1–9 as coursework projects |

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
  the Fall 2006 problem sets, Part II (37 problems), and the 153 Supplementary Notes exercises that Part I assigns.
- 2026-11-18: Calculus split into two parts, Single Variable Calculus (`math/calculus/single-variable/*`, the 18.01
  notes; old ids kept as aliases) and Multivariable Calculus (`math/calculus/multivariable/*`,
  planned, created when 18.02 arrives).
- 2026-11-18: `math/discrete/sequences/limits`, `sums-and-series` and `approximating-sums` moved to Single Variable
  Calculus as `limits/limits-of-sequences`, `limits/sums-and-series` and `series/approximating-sums` (old ids kept as
  aliases); `big-o` now requires `basic-sequences` instead of the sequence-limits note, which it did not use.
- 2026-11-18: MIT 18.02 (Multivariable Calculus) added as a course; new part Multivariable Calculus (field Mathematics,
  after Linear Algebra, owner decision) with five branches and 29 notes; homework from the Fall 2007 problem sets,
  Part B (36 problems), and the 184 Supplementary Notes exercises assigned in Part A or Part B.
- 2026-11-18: Stanford CS221 round 1: `ai/search` filled from Lectures 6–7 (search problems, exhaustive search and
  dynamic programming, best-of-n and beam search, uniform cost search, A* and relaxations); four notes, five figures, one widget.
- 2026-11-18: Stanford CS221 round 2: `ai/deep-learning` tensors and einsum from Lecture 1; two notes, three figures, NumPy/einops code.
- 2026-11-18: Stanford CS221 round 3: `ai/machine-learning` from Lectures 2–3 (supervised learning, linear regression, gradient descent and SGD with the descent lemma, linear classification, logistic regression, softmax and cross entropy, text representation); seven notes, six figures.
- 2026-11-18: Stanford CS221 round 4: `ai/deep-learning` from Lectures 4–5 (computation graphs and backpropagation, neural networks, training deep networks); three notes, four figures.
- 2026-11-18: Stanford CS221 round 5: `ai/reinforcement-learning` from Lectures 8–12 and 14 (MDPs, policy evaluation, value iteration with a widget, model-based RL, Monte Carlo/SARSA/Q-learning, function approximation, policy gradient, improving policy gradient, TD learning); nine notes.
- 2026-11-18: Stanford CS221 round 6: `ai/games` from Lectures 13 and 15 (game trees, expectimax and minimax, alpha-beta pruning, evaluation functions, simultaneous zero-sum games, Nash equilibria); five notes, value-iteration and alpha-beta widgets.
- 2026-11-18: Stanford CS221 round 7: `ai/bayesian-networks` from Lectures 16–18 (Bayesian networks and exact inference, rejection sampling, Gibbs sampling with a widget, conditional independence, parameter learning, EM); six notes.
- 2026-11-18: Stanford CS221 round 8: logic gaps from Lectures 19–20 added to `math/discrete/logic` (models, entailment and satisfiability; modus ponens, definite clauses and resolution; first-order models, unification and modus ponens); three notes. All 20 technical lectures now covered.
- 2026-11-19: Stanford CS221 homework: written parts of HW 1–7 added as 15 exercises (one per handout problem, parts kept together); programming, run-and-report and ethics parts left out (SPEC §17.13.1 item 4).
- 2026-11-19: UC Berkeley CS188 (Fall 2025): three new branches (constraint satisfaction, decision theory, temporal models) and 17 new notes; HW 1–10 (13 exercises, figures redrawn in TikZ) and five discussion problems; projects `prj-cs188-*`; 17 figures; widgets for n-queens backtracking and the forward algorithm.
- 2026-11-19: UC Berkeley EECS126 (Fall 2021): three new branches (random processes, information theory, estimation and detection) and 16 new notes; HW 1–14 (63 exercises, figures redrawn in TikZ) and 11 discussion problems; labs `prj-eecs126-*`; figures for Huffman, Viterbi and Kalman.
