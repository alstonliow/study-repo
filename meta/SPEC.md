---
title: Repository Specification
version: 0.1
status: draft
---

# Repository Specification v0.1

This file is the normative specification for notes in this repository.
It is consolidated from `meta/PLAN.md` §5–§6. Where they differ, this file wins
once approved.

- **v0.1**: drafted in P1, before the pilot.
- **v0.2**: revised once after the P3 pilot, then frozen (see §8).

## 1. Scope

- Notes cover topics under `notes/`, organised by knowledge topic only.
- Sources (units, books, open courses) are never directories. They appear only
  as YAML metadata (`sources`, `source`) and in generated `sources/` mappings.
- First batch: discrete mathematics within FIT1058 scope, plus the probability
  chapter of 1058note (see `meta/taxonomy.md`).

## 2. ids and naming

1. A knowledge point is a folder under `notes/`.
2. Its `id` equals its path without the `notes/` prefix, for example
   `math/discrete/logic/propositional/truth-values`. The id is not stored
   separately.
3. Folder names are lowercase English words joined by hyphens.
4. Paths are at most 3–4 levels below the field (for example below
   `math/discrete/`).
5. `meta/taxonomy.md` fixes the top two levels and the branches. Leaf folders are
   created only when content is added. No empty directories in advance.
6. ids are not renamed without the owner's approval. When a knowledge point is split, the
   original id stays as an overview so existing references do not break.

## 3. Folder contents

| File | Required | Content |
|---|---|---|
| `note.md` | yes | Definitions, theorems, proofs, remarks |
| `example.md` | no | Worked examples |
| `exercise.md` | no | `problem` blocks (§6) |
| `solution.md` | no | `solution` blocks paired with problems by id (§6) |

Examples and exercises are not knowledge points of their own. They live in the
`example.md` / `exercise.md` of the point they belong to.

## 4. YAML header (`note.md`)

```yaml
---
title: Truth Values
sources: [fit1058-w4, rosen-1.1]
requires: [math/discrete/logic/propositional/statements]
status: draft        # draft | done
---
```

| Field | Required | Values |
|---|---|---|
| `title` | yes | English title |
| `sources` | yes | List of source keys; may be empty if unknown (with a TODO comment) |
| `requires` | yes | List of ids; may be empty |
| `status` | yes | `draft` or `done`. Mechanical migration always sets `draft` |

Source keys are never invented. If a source is unknown, leave it out and add a
`<!-- TODO: source -->` comment.

Knowledge points carry no difficulty field. Difficulty belongs to individual
problems and examples (`level`, §5 and §6.1).

## 5. Block types

Content blocks are Pandoc fenced divs (`:::`).

Allowed classes: `definition`, `theorem`, `proposition`, `lemma`, `corollary`,
`claim`, `proof`, `example`, `remark`, `problem`, `solution`.

1. Blocks that are numbered or referenced carry a Quarto id with a prefix:
   `def-`, `thm-`, `prp-`, `lem-`, `cor-`, `exm-`, `prob-`.
2. `proof`, `remark` and `claim` blocks normally carry no id.
3. Which course a piece of content belongs to comes from its source keys
   (`sources`, `source`) and `meta/courses.yml`, not from block markup.
4. A block title goes in a `name` attribute: `{#thm-sum-rule .theorem name="Sum rule"}`.
   Use single quotes around the value if the title contains `"`.
5. 1058note `note` environments become `remark` blocks.
6. Examples stay inside `note.md` in the author's order; `example.md` is for
   additional worked examples.
7. Drawings (TikZ, circuitikz, picture, algorithm) are kept as raw LaTeX
   blocks (```` ```{=latex} ````). The website build compiles them to SVG.
8. `example` blocks may carry `level="easy|medium|hard"`, filled in by the owner
   only.

```markdown
::: {#def-tautology .definition}
A compound proposition is a *tautology* if
$$ p \equiv \mathrm{T} $$
for every assignment of truth values.
:::

::: {.proof}
1. First step.

2. Second step.
:::
```

## 6. Problems and solutions

### 6.1 `exercise.md`

```markdown
::: {.problem #prob-induction-03 origin="external" source="fit1058-tut6-q3" level="medium" tags="induction,divisibility"}
...full problem statement...
:::
```

| Attribute | Required | Rule |
|---|---|---|
| id (`#prob-...`) | yes | Unique across the repository |
| `origin` | yes | `self` (written by the owner) or `external` (textbook, unit, open course) |
| `source` | yes | Source key. If unknown: empty value plus a TODO comment; never guessed |
| `level` | no | `easy`, `medium` or `hard`, filled in by the owner only; omitted if unknown |
| `tags` | no | Comma-separated, lowercase, hyphenated |

1. Problem statements are copied verbatim. They are never paraphrased,
   shortened or "improved".
2. `origin="external"` must be accurate, so that external statements can be
   replaced by citations in bulk if a takedown is ever needed.

### 6.2 `solution.md`

```markdown
::: {.solution for="prob-induction-03"}
1. ...

2. ...
:::
```

1. Every `solution` has a `for` attribute naming an existing problem id.
2. A solution lives in the `solution.md` of the same folder as its problem.
3. Problems without a solution yet are allowed; `make check` reports them as
   warnings.
4. Source keys for course-note exercises: `fit1058-cn-<exercise section>-q<n>`,
   e.g. `fit1058-cn-8.10-q5`. Note sources: `fit1058-cn-<section>`.

## 7. Writing conventions

1. Notes are in English.
2. Main formulas in definitions and theorems use display maths, not inline.
3. Proofs are stepwise: numbered steps or separate paragraphs, never one dense
   block.
4. Cross-references use labels only (compiled to `\label`/`\ref`/`\eqref`).
   Never plain text such as "§1.6" or "Theorem X".
   - Blocks: `@thm-sum-rule`. Quarto supplies the word "Theorem".
   - Knowledge points: `@sec-` plus the id with `/` replaced by `-`, e.g.
     `@sec-math-discrete-counting-derangements`. The build gives each note this
     section label.
   - Problem statements are verbatim and may keep the source's plain-text
     references (e.g. "§8.9").
5. Symbols follow `meta/notation.md`. Notation differences between sources are
   recorded in the `sources/` mappings.
6. Heading levels are not hard-coded in notes. The build derives
   `\section`/`\subsection` from directory depth.
7. Mechanical migration means convert and tag only. The author's wording is not
   rewritten.

## 8. Granularity

1. One knowledge point ≈ one `\subsection` of 1058note. `note.md` is about
   30–150 lines.
2. Split only above about 200 lines.
3. Isolated definitions under about 10 lines merge into a neighbour.
4. Criterion: the smallest concept cluster that is referenced on its own
   elsewhere gets its own folder.
5. Start coarse. Splitting is easier than merging.

## 9. Freeze

After the P3 pilot this SPEC is revised once and frozen as v0.2. While the
first 20 knowledge points are migrated, structure is not changed; wanted changes
go into `meta/ideas.md` and are applied in one batch afterwards.

## 10. Excluded content

Never in the repository: assignments, quizzes, exams, original lecture slides,
original course-note or textbook text, textbook PDFs, anything from `raw/`,
build artefacts (`*.aux`, `*.log`, PDFs, `out/`, `_site/`).

## 11. Checks (`make check`)

`build/check.py` must report:

1. Duplicate ids.
2. Broken cross-references.
3. Missing required YAML fields (§4).
4. `problem` blocks missing `origin` or `source` (§6.1).
5. Problems without solutions and solutions without problems.
6. `requires` entries pointing to non-existent ids.
7. Files that must not be committed: anything under `raw/`, PDFs, `.aux` and
   similar artefacts.

## 12. Open questions (verify in P3)

1. Whether Quarto id prefixes and custom `.problem`/`.solution` blocks render and
   keep cross-references on both the website and the PDF.
2. Which id prefixes to use for `example`, `remark`, `problem` (currently
   `prob-` in examples above).
