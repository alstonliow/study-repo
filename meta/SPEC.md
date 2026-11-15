---
title: Repository Specification
version: 0.2
status: draft
---

# Repository Specification v0.2

This file is the normative specification for notes in this repository.
It is consolidated from `meta/PLAN.md` §5–§6. Where they differ, this file wins
once approved.

- **v0.1**: drafted in P1, before the pilot.
- **v0.2** (2026-11-15): provenance and course scope separated (§1, §13); every
  block except proofs carries an id (§5); one shared parser (`build/model.py`);
  branches in `meta/taxonomy.yml`. Frozen (see §9).

## 1. Scope

- Notes cover topics under `notes/`, organised by knowledge topic only.
- Sources (units, books, open courses) are never directories. They appear only
  as YAML metadata (`sources`, `source`) and in generated `sources/` mappings.
- **Provenance and scope are different things.** `sources` / `source` record
  where content came from (attribution, copyright). Which course *requires* a
  piece of content is recorded only in the course files `meta/courses/<id>.yml`
  (§13). A course never changes a note, and a source key never puts content in
  a course.
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
5. `meta/taxonomy.md` fixes the top two levels and the branches;
   `meta/taxonomy.yml` is the machine-readable list of parts and branches (order,
   display title, one-line description) and, for each branch, the order of its
   notes (`notes:`, folder names). Every note is listed there; topic order on
   the website comes only from this list, never from source keys. The two files
   are changed together. Leaf folders are created only when content is added. No empty
   directories in advance.
6. ids are not renamed without the owner's approval. When a knowledge point is split, the
   original id stays as an overview so existing references do not break.
7. **Moving** a knowledge point or a folder of them is done only with
   `build/move_note.py OLD NEW`. It rewrites `@sec-` references, `requires`,
   course files and `meta/taxonomy.yml`, and adds the old id to the note's
   `aliases` (§4). The website keeps a redirect page at every old address, and
   progress marks saved under an old id move to the new one. An alias is never
   reused as the id of another note. Block ids never change when a note moves.

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
| `requires` | yes | Direct prerequisites (ids); may be empty. See below |
| `status` | yes | `draft` or `done`. Mechanical migration always sets `draft` |
| `aliases` | no | Old ids of this note, added by `build/move_note.py`; never edited by hand |

`requires` lists only the **direct** prerequisites: what a reader must already
know to read this note. No cycles; nothing already implied by another entry; no
note that comes later in topic order. `make check` reports a cycle as an error
and the other two as warnings. The website draws the prerequisite graphs (each
page's "Prerequisites / Leads to", each branch page, and the global Map) from
this field alone.

Source keys are never invented. If a source is unknown, leave it out and add a
`<!-- TODO: source -->` comment.

Knowledge points carry no difficulty field. Difficulty belongs to individual
problems and examples (`level`, §5 and §6.1).

## 5. Block types

Content blocks are Pandoc fenced divs (`:::`).

Allowed classes: `definition`, `theorem`, `proposition`, `lemma`, `corollary`,
`claim`, `proof`, `example`, `remark`, `problem`, `solution`.

1. Every block in `note.md`, `example.md` and `exercise.md` carries a stable id
   with a prefix: `def-`, `thm-`, `prp-`, `lem-`, `cor-`, `exm-`, `prob-`,
   `fig-` (numbered, can be cross-referenced with `@`), and `rmk-` (remark),
   `clm-` (claim). `rmk-`/`clm-` ids are not numbered and are not used in
   `@`-references; they exist so that courses and progress tracking can name
   the block (§13). Ids are never renamed or reused.
2. `proof` blocks carry no id. A proof belongs to the block just before it.
   Blocks inside `solution.md` belong to their solution and need no id.
3. Blocks carry no course markup. Course scope is defined in
   `meta/courses/<id>.yml` (§13).
4. A block title goes in a `name` attribute: `{#thm-sum-rule .theorem name="Sum rule"}`.
   Use single quotes around the value if the title contains `"`.
5. 1058note `note` environments become `remark` blocks.
6. Examples stay inside `note.md` in the author's order; `example.md` is for
   additional worked examples.
7. Drawings (TikZ, circuitikz, picture) are kept as raw LaTeX blocks
   (```` ```{=latex} ````). The website build compiles them to SVG.
   Algorithms are raw LaTeX blocks too, written in `algorithmic` syntax:
   `\begin{algorithm}`, `\caption{...}`, `\begin{algorithmic}`, then `\INPUT`,
   `\OUTPUT`, `\STATE`, `\IF{..}`/`\ELSIF{..}`/`\ELSE`/`\ENDIF`,
   `\WHILE{..}`/`\ENDWHILE`, `\FOR{..}`/`\ENDFOR`, `\RETURN`, `\COMMENT{..}`.
   The website renders them as text with pseudocode.js (`site/pseudocode.html`);
   they are not compiled to SVG. A PDF build must define `\INPUT` and `\OUTPUT`.
   **Figures with a caption** are a div with a `fig-` id holding the drawing,
   then the caption as the last paragraph. They are numbered per page
   ("Figure 1") and referenced as `@fig-...`, also from other notes. Ids are
   `fig-<folder name>-<n>`, e.g. `fig-trees-2`; when two folders share a
   name, put the parent folder first, e.g. `fig-relations-counting-1`. A drawing without a caption
   needs no div.

   ````markdown
   ::: {#fig-trees-1}

   ```{=latex}
   \begin{tikzpicture}[dotgraph] ... \end{tikzpicture}
   ```

   A tree

   :::
   ````

   **Shared drawing styles.** Figures never hard-code colours, line widths,
   font sizes or node sizes; they use only the names defined in the preamble
   in `build/make_site.py`, so the look of every figure is changed in one
   place. Coordinates and scales (`x=0.6cm`, `scale=0.8`) are layout and stay
   in the figure. `make check` warns about raw values.
   - Colours (roles): `primary` (blue), `accent` (red-brown, for emphasis),
     `secondary` (green), `muted` (grey), `ink` (near-black). Fixed tints:
     `primarySoft`, `primaryLight`, `primaryMid`, `primaryStrong`,
     `accentSoft`, `accentLight`, `secondarySoft`, `neutral` (cell grey),
     `rule` (light lines).
   - Text: `lbl` (labels), `tick` (axis ticks, small notes), `note`,
     `heading`, `big`, `lbl bold`, `heading bold`.
   - Lines: `emph`, `bold`, `hl` (highlighted edge), `faint`, `gridline`.
   - Graphs: `graph` (all nodes labelled vertices), `dotgraph` (all nodes
     dots), `vertex`, `small vertex`, `dot`, `hl dot`, `hollow dot`, `pt`
     (radius for `circle[pt]`).
   - Areas: `regionA`/`regionB`/`regionC`, `tintA`–`tintD` and
     `overlapA`/`overlapB` (translucent fills), `shade`.
   - Cells, bars, boxes: `cell`, `cell frame`, `hl cell`, `bar`, `box`,
     `hl box`, `ball`, `hl ball`.
   - Labels and maps: `lab`, `edge label`, `set` (an oval for a domain or
     codomain), `map` (an arrow between elements).

   The website shows figures at 1.3 times their natural size.
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
   warnings. An empty stub (only a `<!-- TODO: solution -->` comment) counts as
   no solution.
4. `status="draft"` marks a solution that the owner has not reviewed yet (for
   example one written by Claude). The website labels it "Draft solution".
   The owner removes the attribute after review.
5. Source keys for course-note exercises: `fit1058-cn-<exercise section>-q<n>`,
   e.g. `fit1058-cn-8.10-q5`. Note sources: `fit1058-cn-<section>`.

### 6.3 Synthesis problems (`review/`)

Problems that combine several knowledge points of a branch live in
`notes/<branch>/review/exercise.md` (and `solution.md`), with the same rules as
§6.1–6.2. A review folder holds nothing else and is not a knowledge point: it is
not listed in `meta/taxonomy.yml`. Its problems belong to a course when some
note of the branch does, unless the course excludes them.

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

v0.2 is frozen. Wanted structural changes go into `meta/ideas.md` and are
applied in one batch, with the owner's approval, as v0.3.

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
8. Blocks without an id (§5), and `@`-references to `rmk-`/`clm-` ids.
9. Notes missing from `meta/taxonomy.yml`, or listed there but absent (§2.5);
   aliases that clash with a note id or with each other (§2.7).
10. Course files (§13): unknown note or block ids in `covers`/`exclude`, duplicate
   point ids, points that cover nothing (warning), and notes whose `sources`
   name a course that does not cover them (warning: provenance without scope).

All checks run on the model built by `build/model.py`, the single parser of
notes, blocks and course files. `make test` runs the build scripts on a small
fixture repository (`tests/fixture`) and compares the generated pages with
`tests/expected`; CI runs it before `make check`. Any change to the build
scripts keeps `make test` passing; an intended change of output is accepted
with `python3 tests/test_build.py --update` and reviewed in the diff. `build/make_site.py` uses the same model; no
other script parses notes on its own.

## 12. Open questions

None. (Cross-references in the PDF build were verified in November 2026.)

## 13. Courses and scope

One file per course: `meta/courses/<id>.yml`. It lists the course outline and,
for each outline point, which content the course requires.

```yaml
id: fit1058
code: FIT1058
name: ""                    # full name; filled in by the owner, never guessed
institution: Monash University
source_prefix: fit1058-     # provenance keys from this course's own material
outline_from: "FIT1058 Course Notes (16 June 2026), table of contents"
status: draft               # draft | confirmed (owner reviewed the mapping)
exclude: [exm-x, rmk-y]     # blocks inside covered notes that are out of scope
chapters:
  - num: 1
    title: Sets
    points:
      - id: "1.6"
        title: Subsets and supersets
        covers: [math/discrete/sets/subsets]   # note ids and/or block ids
```

1. **Scope is block-level.** A block is in a course's scope when its note is
   covered (by note id) and the block is not in `exclude`, or when the block
   itself is covered (by block id). A proof follows the block before it; a
   solution follows its problem. Prose outside blocks follows its note.
2. **Outline points** use the course's own numbering and short titles, written
   by the owner or Claude, never copied text. Order of chapters and points is
   the course order, used for course pages and the course filter.
3. **What is in scope:** everything that appears in the course's own material
   (for FIT1058, the Course Notes), including sections that material marks as
   optional or beyond the curriculum. Everything else is out of scope ("extra"):
   the owner's "(extra)" material, and any other block whose content the course
   material does not have. This is decided by checking the content against the
   course material, not by labels or source keys. There is no `extra` tag; out of
   scope simply means listed under `exclude` (or not covered).
4. **Mappings are drafted, then confirmed.** Claude may draft a course file from
   an outline; `status: draft` until the owner has reviewed it.
5. On the website, the course filter shows the selected courses' notes in
   course order, and folds blocks outside their scope into a one-line
   "Beyond <code>" summary that can be opened. Progress marks are shared across
   courses.

## 14. Chapter summaries

Generated by `build/summaries.py`, never written by hand. One page per branch
(`notes/<branch>/summary`), and one per chapter of each course
(`courses/<id>/chapter-<n>`), which lists only content in the course's scope. A
page shows the prerequisite graph, the statements of definitions and results
(no proofs, each linking to its note), all exercises, then the synthesis
problems (§6.3). A filter bar selects by content type, level and progress
state, and hides or expands solutions; printing the page prints what is shown.

## 15. PDF export

`build/make_pdf.py` builds PDFs from the same model with Quarto and XeLaTeX.
Options: scope (book, branch, course), solutions (inline, end, separate,
none), extra content (include, omit; needs a course), content (all, summaries,
exercises), exercise levels, paper (A4, Letter), layout (book, document),
margins, and style (color = the website's look; plain = black and white).
`make pdf` builds the common versions (presets in `make_pdf.py`), which CI
publishes on the website's PDF page; any other combination is built locally.
Figures use `build/figures.tex`, shared with the website. References to content
that a PDF leaves out are printed as plain text.
