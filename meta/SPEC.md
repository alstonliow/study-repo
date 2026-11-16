---
title: Repository Specification
version: 0.3
status: draft
---

# Repository Specification v0.3

This file is the normative specification for this repository: the notes, and
the domain model (§17) that all content follows.
It is consolidated from `meta/PLAN.md` §5–§6. Where they differ, this file wins
once approved.

- **v0.1**: drafted in P1, before the pilot.
- **v0.2** (2026-11-15): provenance and course scope separated (§1, §13); every
  block except proofs carries an id (§5); one shared parser (`build/model.py`);
  branches in `meta/taxonomy.yml`. Frozen (see §9).
- **v0.3** (2026-11-16): the domain model (§17): entities, identity,
  references, typed relationships, backlinks, outlines and placement with an
  optional book level, numbering context, and public/private visibility. The
  repository becomes a personal knowledge system whose public part is the
  study notes. Implemented in phases (§17.10).

## 1. Scope

- The repository is a personal knowledge system built from entities (§17). Its
  public part is the study notes described in §2–§16. Its private part holds
  personal content, kept behind the privacy boundary (§17.9). New entity types
  are added one at a time, each specified here before it is built.
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
   are changed together. A part with `book: false` only groups the navigation:
   it is not a book (§16.1, §17.7). Leaf folders are created only when content is added. No empty
   directories in advance.
6. ids are not renamed without the owner's approval. When a knowledge point is split, the
   original id stays as an overview so existing references do not break.
7. **Moving** a knowledge point or a folder of them is done only with
   `build/move_note.py OLD NEW`. It rewrites `@sec-` references, `requires`,
   course files and `meta/taxonomy.yml`, and adds the old id to the note's
   `aliases` (§4). The website keeps a redirect page at every old address, and
   progress marks saved under an old id move to the new one. An alias is never
   reused as the id of another note. Block ids never change when a note moves.
8. ids name things; they never encode numbers, courses or books (§17.3). Block
   ids are unique across the whole repository, public and private.

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
`claim`, `proof`, `example`, `remark`, `problem`, `solution`. The registry of
kinds (prefix, word, numbering, colour) is `build/kinds.py` (§16.7).

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
   - Blocks: `@thm-sum-rule`. The build writes the label with its number,
     "Theorem 8.1.2" (§16), as a link.
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

v0.2 is frozen. v0.3 adds the domain model (§17), approved by the owner on
2026-11-16; it is frozen once its phase 2 is built. Further structural changes
go into `meta/ideas.md` and are applied in one batch, with the owner's
approval.

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
11. Relationships (§17.5.8), and old ids (aliases) used in `requires`,
   `relations` or `@sec-` references (§17.3.3).

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
for each outline point, which content the course requires. In terms of the
domain model (§17.7), a course is an outline, and `covers` gives placements:
the same notes and blocks are placed in the course without being copied or
changed.

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
Selection: branches, course chapters, single knowledge points, and block types
(definitions, results, proofs, examples, remarks, figures, exercises, synthesis
problems); table of contents on or off. Exercises are numbered 1, 2, 3, ... per
knowledge point, everywhere, with their source beside the number.
`make pdf` builds the common versions (presets in `make_pdf.py`), which CI
publishes on the website's PDF page.

The website's **Export** page offers the same choices as checkboxes. It
assembles the chosen content in the browser (also filtering by progress
marks) and prints it with "Save as PDF"; it also writes the matching
`make_pdf.py` options, which the owner can run on GitHub
(`.github/workflows/pdf.yml`, "Build PDF") to get a LaTeX PDF of any
combination.
Figures use `build/figures.tex`, shared with the website. References to content
that a PDF leaves out are printed as plain text.

## 16. Numbering

Numbers are derived from the **numbering context** (§17.8): an entity, its
placement, and the **outline** in use (`build/outline.py`). Outlines are the
topic outline from `meta/taxonomy.yml` (books = parts → chapters = branches →
notes), and one outline per course from `meta/courses/<id>.yml`.
`build/numbering.py` turns an outline and `meta/numbering.yml` into every
number; nothing else computes numbers, and Quarto's or LaTeX's own theorem
numbering is not used. Numbers are never stored in content and never used as
references.

1. **Books and other collections.** A book is an optional level of an outline
   (§17.7). Where an outline has books, each book has its own numbers; fields
   (math, cs) only group the navigation. A reference into another collection
   (another book or course) adds that collection's title after the number:
   Theorem 11.8.1 (Discrete Mathematics). Chapters outside any book (parts
   with `book: false`) share one sequence of chapter numbers and add no book
   name; a reference from them into a book adds the book's title.
2. **Notes**: chapter.k (8.1). Headings inside a note are not numbered.
3. **Blocks**: the note's number and a counter per kind: Definition 8.1.1,
   Definition 8.1.2, Example 8.1.1, Theorem 8.1.1. Numbered kinds are listed in
   `numbering.yml` (definitions, theorems, propositions, lemmas, corollaries,
   examples, figures); remarks and claims are not numbered.
4. **Exercises**: 1, 2, 3 on their note's page; Exercise 8.1.3 anywhere else
   (references, PDF solutions). On summary pages and the Export page they keep
   1, 2, 3 and note the topic they come from, their source and level.
5. **Synthesis problems** (`review/`): Review 8.1, 8.2 (chapter.k).
6. **Courses.** With the course filter on, the website shows the course's
   numbers (Theorem 7.1.2): every number is marked with its note and switched
   from the maps in `site-data.json`. Course PDFs use course numbers.
7. **Kinds of block** are defined once in `build/kinds.py` (prefix, class,
   word, group, numbered, cross-referenced, colour); the page scripts read the
   same table from `site-data.json`.

## 17. Domain model

This section is the architecture of the whole repository: a personal knowledge
system whose public part is the study notes and whose private part holds
personal content. It defines concepts. It does not require code for entity
types that do not exist yet; implementation goes in phases (§17.10).

### 17.1 Principles

1. **Entity-centred.** Everything stored is an entity with a stable id. Books,
   courses and chapters organise entities; they are not levels every entity
   must pass through.
2. **Identity, position and number are separate.** An id never contains a
   number, a course or a book. Moving an entity or renumbering an outline
   never breaks a reference.
3. **One canonical record, many derived views.** Each fact is written once;
   numbers, backlinks, graphs, summaries, `site-data.json` and PDFs are
   generated from it at build time and never edited by hand.
4. **References and relationships point to ids**, never to numbers or titles.
5. **Shared core, own schemas.** Entity types share only id, title, status and
   visibility; every other field belongs to one type's schema.
6. **No speculative abstraction.** Code is generalised only when at least two
   entity types need the same thing.

### 17.2 Entities and entity types

1. An **entity** is an object with a stable id that can be referenced. There
   are two levels:
   - **file-level** entities: a knowledge point (note) today; resources,
     ideas, projects and others later;
   - **block-level** entities: definitions, theorems, examples, problems,
     figures, remarks and claims inside a file (§5). A block belongs to its
     file.
2. An **entity type** is defined once in a registry: name, where it is stored,
   how its id is formed, its schema (YAML fields), whether it is numbered and
   whether it can be placed in outlines. Block types are defined in
   `build/kinds.py` (§16.7). File-level types today: note (§2–§4) and review
   folder (§6.3). Planned: resource first, then others; each new type gets its
   own subsection here, with its schema, before any code (§17.10).
3. Core fields of every file-level type: `id` (for notes, derived from the
   path), `title`, `status`, and visibility (derived from where it is stored,
   §17.9).
4. **Not entities:** proofs (they belong to the block before them and have a
   local anchor only), solutions (paired with a problem by `for`, §6),
   headings and prose outside blocks.

### 17.3 Identity

1. ids are stable and never reused.
2. A note's id is its path (§2.2). The path is a namespace, not a position:
   numbering and placement never read it. The note's place in the topic
   outline comes from `meta/taxonomy.yml`.
3. A **rename** (move, §2.7) gives the entity a new id and keeps the old one as
   an alias. Aliases are a **permanent compatibility layer for addresses
   outside the repository**: web addresses (redirect pages), progress marks,
   and links from elsewhere. Inside the repository, references and
   relationships always use the current id; `build/move_note.py` rewrites
   them, and `make check` reports an alias used as a target.
   - Aliases are flat: every alias of an entity points directly to its
     current id. Moving again keeps the earlier aliases and adds one more, so
     there are no chains and no cycles.
   - An alias is never the id of an existing entity and never the alias of
     two entities (check error). It is never reused.
   - Block ids never change, so blocks have no aliases.
   - Aliases are never deleted.
4. Block ids are unique across all files, entity types and visibilities.
5. **Entity index.** `build/model.py` builds one index of all entities
   (id → type, file, title, visibility, aliases), which the resolver, checks,
   backlinks and pages use. It is a thin index over the per-type classes, not a
   universal entity class.
6. **Known cost of path ids.** Because a note's id is its path, a move changes
   its id. If moves become frequent, notes can later get an opaque `id` field,
   with their current paths kept as aliases. That migration only touches the
   front matter and the index, because references already go through ids and
   aliases. It is recorded here, not planned.

### 17.4 References

1. A **reference** is a link in content to an id: `@<block id>`, or
   `@sec-<note id>` for a note (§7). It is never a number or a title.
2. Resolving a reference: id or alias → entity → presentation in the current
   numbering context (§17.8).
3. Three cases of a target that cannot be shown are kept apart:

   | Case | Example | Result |
   |---|---|---|
   | **Missing**: no entity has this id | a typo, a deleted block | check error |
   | **Left out**: the target exists but this build does not include it | a PDF selection, a course filter | plain text, no link (the target is public, so its label may be shown) |
   | **Not visible**: the target is private and the build is public | a public note pointing to a private idea | not allowed (§17.9); a public build cannot see the private store, so there it is reported as missing, and nothing about the target appears |

4. References and relationships (§17.5) are separate records with separate
   meanings. A reference says only "this text points there"; it never implies
   `uses` or any other type. They share id resolution (§17.3) and the backlink
   index (§17.6).

### 17.5 Relationships

1. A **relationship** is a record (source id, type, target id) with optional
   metadata (for example a note or a date). The model stores the full record.
   Files use a short syntax, and a longer form is reserved for metadata.
2. A relationship is written **once, at its source**, in one of two syntaxes
   that mean the same thing:
   - file-level, in the YAML header:

     ```yaml
     relations:
       uses: [math/discrete/number-theory/gcd]
       generalizes: [math/discrete/counting/sum-rule]
     ```

     `requires` stays a top-level field (§4); it is the relationship type
     `requires`.
   - block-level, as a div attribute named after the type, with
     space-separated ids:

     ```markdown
     ::: {#thm-euclidean .theorem uses="def-gcd def-divides"}
     ```

   Reserved for later, only when needed: a list item in `relations` may be a
   mapping `{to: <id>, note: "..."}` instead of a bare id.
3. **Types** are defined in `meta/relations.yml`: name, inverse display name,
   symmetric or not, acyclic or not, and which entity types may be source and
   target. Initial types:

   | Type | Shown at the target as | Symmetric | Acyclic | Between |
   |---|---|---|---|---|
   | `requires` | required by | no | yes | notes |
   | `uses` | used by | no | no | notes, blocks |
   | `generalizes` | specializes | no | yes | notes, blocks |
   | `equivalent` | equivalent | yes | no | notes, blocks |
   | `related` | related | yes | no | notes, blocks |

4. **Inverse names are display names, not stored relationships.** "Used by"
   is never written; it is derived. A symmetric relationship is stored once,
   on either side; writing it on both sides is a check warning.
5. **Cycles** are checked only for acyclic types, over that type's whole graph
   across all notes and blocks. Cycles in other types, and cycles that mix
   types, are allowed.
6. The `requires` rules in §4 still hold: direct prerequisites only, nothing
   already implied, nothing later in topic order.
7. **Not relationships:** references (§17.4), the pairing of problems and
   solutions, a block belonging to its file, and placement in outlines.
8. `make check` reports unknown types, unknown target ids, types used between
   entity types the registry does not allow, cycles in acyclic types (errors),
   and duplicate symmetric pairs (warnings).

### 17.6 Backlinks

1. Backlinks are derived data: canonical references and relationships →
   backlink index → rendered backlinks. They are never written by hand;
   removing a relationship removes its backlink at the next build.
2. Two groups are kept apart:
   - **References**: "Referenced by", from `@` links;
   - **Relationships**: grouped by inverse name: Required by, Used by,
     Specializes, Equivalent, Related.
3. A note page ends with its backlinks, in a **Connections** section: those to the note, then those to each
   of its blocks (for example "Theorem 8.1.2 ← used by Example 8.3.1"). Labels
   use the current numbering context.
4. Relationships written in YAML or div attributes do not appear in the text,
   so the source's page also lists them forward ("Uses", "Generalizes", ...),
   next to the existing "Prerequisites / Leads to". Both directions come from
   the same records.

### 17.7 Outlines, collections and placement

1. A **collection** is a named group of entities. Only one kind exists so far:
   the **outline**, an ordered tree. Other kinds (unordered, filtered,
   hand-picked) are added only when needed.
2. An outline's levels and their names are set by the outline's own
   configuration. Current outlines: the topic outline (`meta/taxonomy.yml`:
   book → chapter → note) and course outlines (`meta/courses/<id>.yml`:
   chapter → point → notes and blocks). A **book is an optional level** that an
   outline may have; an entity never needs a book.
3. A **placement** is the position of one entity in one outline, and it gives
   the entity its number there. An entity may be placed in many outlines, but
   has **exactly one numbered placement in each**. This is a deliberate design
   limit, so that an entity never has two numbers in one numbering context.
   - In the topic outline, each note is listed once in `meta/taxonomy.yml`
     (check error otherwise).
   - In a course outline, several points may cover the same note (for
     example a note spanning points 1.3–1.5). Coverage decides scope (§13).
     Only the **first** point that covers the note places it: the note is
     numbered and shown there, and later points link to it.
   - Showing an entity in another place of the same outline is done with a
     reference or, later, a collection view, never with a second placement.
4. Every note has a placement in the topic outline (§2.5); other entity types
   say in their schema whether they need one.
5. Entities exist independently of their placements. Removing an entity from
   an outline never changes the entity.

### 17.8 Numbering context

1. A number is computed from the entity, its placement and the outline in use
   (the **context**), with the formats in `meta/numbering.yml`. The rules are
   in §16.
2. An outline may be unnumbered; its entities are then shown by title.
3. A reference shows the target's number in the current context. A target in
   another collection (another book, another course) shows that collection's
   number with the collection's name after it (§16.1). A target with no
   placement in any numbered outline is shown by its title.

### 17.9 Visibility and the privacy boundary

1. Every entity is **public** or **private**. Private: personal content, that
   is ideas, projects, goals, decisions, logs, personal reading records, and
   anything else the owner marks private. Public: the study notes, problems
   and solutions, as now.
2. Visibility follows from where an entity is stored, never from a field that
   could be forgotten. Public entities are stored in this repository. Private
   entities are stored outside its public history. The first implementation
   is a private Git repository mounted at `private/`, added in the Resources
   phase. The rules below do not depend on that mechanism.
3. Rules:
   1. A public entity never references or relates to a private one (check
      error), because its title would leak. Private entities may point to
      public ones. A private build reports this case by name. A public build
      sees only "missing" (§17.4). Writing a private id in a public file
      already reveals that the id exists, and git history keeps it, so the
      owner runs the private `make check` before committing. Private ids
      follow the same id rules and must not clash with public ids; only a
      private build can check this.
   2. A **public build** (CI, the public website, published PDFs) never reads
      the private store. Its output is the same whether or not the private
      store is present.
   3. A **private build** runs locally, reads both, and is never published.
      If the private store is missing it warns and builds the public part.
   4. Private content never appears in any public file: pages,
      `site-data.json`, search index, graphs, redirects, summaries or PDFs.
   5. Private content is never copied into the public tree.
4. Progress marks are personal records already kept outside the repository
   (Supabase); they stay there.
5. §10 and the `raw/` rules apply to all content. Excluded material is not
   allowed in the private store either.

### 17.10 Phases

1. **Specification**: this section (v0.3).
2. **Notes** (built 2026-11-16): entity index (`Repo.entities`), backlinks and
   typed relationships (`build/relations.py`, `meta/relations.yml`), and an
   optional book level (`book: false` on a part in `meta/taxonomy.yml`). No
   note file changed; the output is unchanged except for the new Connections
   sections.
3. **Resources**: the first new entity type, with its schema written here
   first, and the private store. This phase must keep three concepts apart:
   - **Resource**: the logical work you keep, read or watch (one book across
     its editions);
   - **Source locator**: a place in one edition (chapter, section, page, URL);
     edition maps stay in `meta/sources.yml` (§16);
   - **Citation**: a note's pointer to a source locator (today the `sources`
     and `source` fields).

   This phase also decides how `meta/sources.yml` entries relate to Resource
   entities.
4. **Further types** (ideas, projects, and others), one per round. Shared code
   is generalised only when two types need it.

### 17.11 Compatibility with v0.2

| v0.2 | v0.3 |
|---|---|
| Note id = path | Kept; the path is a namespace, not a position (§17.3) |
| "ids are never renamed" | A move is a new id plus an alias; aliases keep outside addresses working, and in-repo references use the current id (§2.7, §17.3) |
| A course may cover a note from several points; it was placed at the first, without a written rule | One numbered placement per outline: the first covering point (§17.7) |
| Topic outline is always book → chapter → note | The book level is optional (§16.1, §17.7) |
| Only `requires` between notes | `requires` plus typed relationships (§17.5) |
| No backlinks | Derived backlinks (§17.6) |
| Public repository only | Public and private entities, with a privacy boundary (§17.9) |
