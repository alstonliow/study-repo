# Study Notes

Personal study notes, organised by topic rather than by course or textbook.

**Website:** <https://alstonliow.github.io/study-repo/>

The first batch covers discrete mathematics (the scope of Monash FIT1058) and
discrete probability. Other areas (algorithms, calculus, linear algebra, …) will
be added over time.

This is a personal project. It is **not affiliated with or endorsed by Monash
University** or any other institution, and it is not official course material.

## How the notes are organised

- Each knowledge point is one folder under `notes/`, e.g.
  `notes/math/discrete/counting/derangements/`:
  - `note.md` – definitions, theorems, proofs, examples
  - `exercise.md` – problems
  - `solution.md` – solutions, paired with problems by id
- Notes are Markdown with YAML front matter and Pandoc fenced divs
  (`::: {#thm-… .theorem}`).
- Sources (courses, textbooks) are metadata, not folders. `sources`/`source`
  only record where content came from.
- Which course needs which content is defined in one file per course,
  `meta/courses/<id>.yml`: the course outline, and for each outline point the
  notes (or single blocks) it covers. Blocks outside a course's scope are folded
  on the website when that course is selected in the course filter.

The full conventions are in [`meta/SPEC.md`](meta/SPEC.md). The topic tree is in
[`meta/taxonomy.md`](meta/taxonomy.md) and the notation in
[`meta/notation.md`](meta/notation.md).

## Adding content

### A solution

Every problem already has a stub in the `solution.md` of its folder:

```markdown
::: {.solution for="prob-proofs-11"}
<!-- TODO: solution -->
:::
```

Replace the TODO line with the solution. Write proofs as numbered steps. Empty
stubs are not shown on the website, and `make check` lists them as warnings.

### A problem

Add it to the folder's `exercise.md`, and add a matching stub to `solution.md`:

```markdown
::: {.problem #prob-proofs-20 origin="self" source=""}
<!-- TODO: source -->
Problem statement, copied verbatim.
:::
```

- The id is unique across the repository. Continue the folder's numbering.
- `origin` is `self` (written by me) or `external` (from a textbook or course).
- `source` is a source key, e.g. `fit1058-cn-8.10-q5`. If it is unknown, leave
  it empty and add a TODO comment. It records provenance only; the problem is
  in a course's scope when its note is (see "A course" below).
- `level="easy|medium|hard"` and `tags="a,b"` are optional.

### A knowledge point

1. Create a folder under an existing branch (see `meta/taxonomy.md`), with a
   lowercase hyphenated name, e.g. `notes/math/discrete/counting/stars-and-bars/`,
   and add the folder name to that branch's `notes:` list in
   `meta/taxonomy.yml`, at the place where it should appear.
2. Write `note.md`:

   ```markdown
   ---
   title: Stars and Bars
   sources: [fit1058-cn-8.6]                         # [] plus a TODO if unknown
   requires: [math/discrete/counting/combinations]   # ids, may be empty
   status: draft
   ---

   ::: {#def-xxx .definition name="..."}
   ...
   :::

   ::: {#thm-xxx .theorem name="..."}
   ...
   :::

   ::: {.proof}
   1. ...

   2. ...
   :::
   ```

   Every block except a proof needs an id: `def-`, `thm-`, `prp-`, `lem-`,
   `cor-`, `exm-`, `fig-`, and `rmk-` for remarks (`rmk-<folder>-<n>`),
   `clm-` for claims. Ids never change once given. A proof belongs to the
   block before it.

3. Optionally add `example.md`, `exercise.md` and `solution.md`.
4. Refer to blocks with `@thm-xxx` and to knowledge points with
   `@sec-` plus the id with `/` replaced by `-`.
5. Keep it to about 30–150 lines. Split above 200 lines.

### A figure

Draw with TikZ in a ```` ```{=latex} ```` block, using only the shared styles
and colours (`graph`, `hl`, `lbl`, `bold`, `box`, `primary`, `accentLight`, …
listed in `meta/SPEC.md` §5). Do not write raw colours (`defc!30`), line
widths, font sizes or node sizes; `make check` warns if you do, and changing
a style in `build/make_site.py` restyles every figure. To give it a number and a caption, wrap it in a `fig-` div
with the caption as the last paragraph, then refer to it as `@fig-trees-1`:

````markdown
::: {#fig-trees-1}

```{=latex}
\begin{tikzpicture}[dotgraph]
  \node (a) at (0,0) {}; \node (b) at (1,0) {};
  \draw (a) -- (b);
\end{tikzpicture}
```

A tree

:::
````

The website numbers pages automatically. Within a branch, pages are ordered by
their first source key.

### Visualising a course

Static figures first (website and PDF), then interactive widgets (website only).

1. **Choose.** In each note pick 1–3 places where seeing the process helps
   most: key steps of an algorithm, how a data structure changes, a DP table.
2. **Simulate.** Run the algorithm in a short script on the note's own example
   and record the state after each step, so every number in a figure is computed,
   not typed by hand.
3. **Generate.** Turn the states into TikZ with the shared styles only, as a
   `fig-<folder>-<n>` div with a one-sentence caption (see "A figure"); round
   coordinates to two decimals.
4. **Preview and place.** Compile each figure on its own (the preamble is in
   `build/tikz.py`), fix overlaps, then insert it after the block it illustrates.
5. **Widgets.** For figures that read better step by step, register a widget in
   `site/_assets/widgets.html` under the figure's id: a function from the inputs
   to a list of frames (picture plus one sentence). Reuse the existing drawing
   helpers (cells, trees, graphs, tables); let the reader enter their own input
   where it makes sense. Every widget needs its static figure (`meta/SPEC.md` §5).
6. **Verify.** Run `make check` (it also reports widgets attached to unknown
   figures), `make test` and `make site`; look at a few PDF pages; in the browser,
   step every widget to the end and try a bad input and the Example button.

### A course

Add `meta/courses/<id>.yml` (format in `meta/SPEC.md` §13; see
`meta/courses/fit1058.yml`). List the course's chapters and outline points, and
for each point the note ids (or single block ids) it covers. Put blocks inside a
covered note that the course does not need under `exclude`. Keep
`status: draft` until the mapping has been reviewed. A new note that a course
needs must be added to that course's file; `make check` lists notes drawn from a
course's material that its file does not cover.

### Moving or renaming notes

Never move note folders by hand. Use

```bash
python3 build/move_note.py math/discrete/counting/stars-and-bars math/discrete/counting/multisets
```

It works for a single note or a whole folder (`math/discrete/graph`), updates
every reference, `requires`, the course files and `meta/taxonomy.yml`, and
records the old id under `aliases`, so old links redirect and progress marks
follow. Add `--dry-run` to see what it would change.

### Prerequisites, summaries and PDFs

- `requires` in a note's YAML lists its **direct** prerequisites only (see
  `meta/SPEC.md` §4); the website draws every prerequisite graph from it, and
  `make check` rejects cycles.
- Other relationships (`uses`, `generalizes`, `equivalent`, `related`; the
  list is `meta/relations.yml`) are written once, at their source: in a note's
  YAML as `relations: {uses: [<note id>]}`, or on a block as
  `::: {#thm-x .theorem uses="def-a def-b"}`. Never write the reverse ("used
  by"): each page's **Connections** section shows both directions, plus every
  `@` reference from other pages ("Referenced by"). See `meta/SPEC.md` §17.
- Resources (books, course notes) are YAML files in `resources/` (SPEC §17.12).
  To record that a section teaches a topic, add `covers: [<note or block id>]`
  to that node in the resource file (a resource without chapters or sections
  puts `covers` at its top level). Only add real teaching coverage ("to study
  B, read A"), not mentions. Cite a section in text with `@res-<node id>`. The
  website's **Library** shows each resource's sections with what they cover
  and what cites them.
- Synthesis problems for a branch go in `notes/<branch>/review/exercise.md` and
  `solution.md`; they appear at the end of the branch's summary page.
- Summary pages (one per branch, one per course chapter) are generated.
- PDFs: on the website, **Export** lets you tick what to print and save it as a
  PDF from the browser, or copy the options for a LaTeX PDF built on GitHub
  (Actions → Build PDF → Run workflow). Locally:

  ```bash
  make pdf                                   # the common versions, into out/pdf/
  python3 build/make_pdf.py --help           # every option
  python3 build/make_pdf.py --scope course:fit1058 --extra omit --solutions separate --layout document --style plain
  ```

### Before committing

```bash
make check   # must report 0 errors; warnings are open TODOs
make test    # only needed after changing build/ or site/ scripts
make pdf     # optional: PDFs (CI builds them too)
make site    # optional local preview
```

## Progress tracking

Every knowledge point and exercise on the website has a mark:
**New → Learned → Reviewing → Mastered** (click to advance, shift-click to go
back). Branch pages and the home page show the totals.

Marks are saved in the browser. To sync them across devices, sign in with
GitHub (link at the bottom of the sidebar). Sync uses Supabase:

1. Create a Supabase project. In the SQL Editor, run
   [`build/supabase-schema.sql`](build/supabase-schema.sql).
2. Create a GitHub OAuth app with the callback URL
   `https://<project>.supabase.co/auth/v1/callback`, and enter its client id and
   secret under Authentication → Sign In / Providers → GitHub.
3. Under Authentication → URL Configuration, set the Site URL to the website
   and add `http://localhost:4321/**` to the redirect URLs.
4. Put the project URL and the **anon** key in `site/_assets/progress.html`. Never use
   the `service_role` key.
5. After signing in once, turn off "Allow new users to sign up" so that no one
   else can create an account.

## Repository layout

| Path | Contents |
|---|---|
| `notes/` | The notes: one folder per knowledge point, `<field>/<area>/<branch>/<note>/` with `note.md` and optional `example.md`, `exercise.md`, `solution.md` |
| `meta/` | Specification (`SPEC.md`), taxonomy (`taxonomy.yml`, the list of parts, branches and notes; `taxonomy.md`, its rules and history), notation, course files (`courses/`), relationship types (`relations.yml`), numbering formats (`numbering.yml`), parked ideas (`ideas.md`) |
| `resources/` | One YAML file per resource (book, course notes, ...): its chapters and sections as nodes, editions, and the format of its source keys (`meta/SPEC.md` §17.12) |
| `build/` | `model.py` (the one parser), registries (`kinds.py`, `sources.py`), `outline.py` and `numbering.py`, `refs.py`, `filters.py`, `transforms.py`; site (`make_site.py`, `web.py`, `summaries.py`, `graphs.py`, `tikz.py`), PDF (`make_pdf.py`, `book.py`), shared figure styles (`figures.tex`), checks (`check.py`), `move_note.py` |
| `site/` | Quarto website: `_quarto.yml` and `_assets/` (themes, styles, page scripts, Lua filter, favicon) are hand-written; everything else there is generated and not committed |
| `tests/` | Tests of the build scripts on a small fixture (`make test`) |
| `.github/workflows/` | Builds and publishes the website and the PDFs on every push to `main` |

Local only, never committed: `raw/` (reference material: course notes and solutions, one folder per course), `out/` (built PDFs), `private/` (the private store).

## Building

Requirements: Python 3 with PyYAML, [Quarto](https://quarto.org), a TeX
distribution (`pdflatex`) and `pdftocairo` (Poppler) for the diagrams.

```bash
make check     # validate notes (ids, references, YAML, problem/solution pairs)
make site      # generate and render the website into site/_site/
make preview   # live local preview
make test      # type checks and tests of the build scripts
make pdf       # PDFs into out/pdf/
make clean-site  # remove the generated website files
```

## Sources and copyright

- Problems marked `origin="external"` in `exercise.md` are copied from their
  sources (for example the FIT1058 Course Notes) for study purposes. **Their
  statements remain the copyright of their original authors and publishers**;
  each problem records its source in the `source` attribute.
- These problems are not covered by this repository's licence. They will be
  removed or replaced by citations on request from the copyright holder.
- Homework problems may appear as exercises in the same way (statement copied,
  source recorded); their official solutions are never copied, and every
  solution here is our own.
- Quizzes, exams, lecture slides and textbook files are never included.

## Licence

- **Notes and other original written content** (everything not listed below,
  excluding third-party problem statements): [CC BY-NC-SA 4.0](LICENSE).
- **Code** (`build/`, `site/`, `Makefile`, `.github/`): [MIT](LICENSE-CODE).

© 2026 alstonliow
