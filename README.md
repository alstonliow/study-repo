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
- Sources (courses, textbooks) are metadata, not folders. Course membership
  comes from source keys and `meta/courses.yml`.

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
  it empty and add a TODO comment. Only `fit1058-` keys appear in the course
  filter.
- `level="easy|medium|hard"` and `tags="a,b"` are optional.

### A knowledge point

1. Create a folder under an existing branch (see `meta/taxonomy.md`), with a
   lowercase hyphenated name, e.g. `notes/math/discrete/counting/stars-and-bars/`.
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

3. Optionally add `example.md`, `exercise.md` and `solution.md`.
4. Refer to blocks with `@thm-xxx` and to knowledge points with
   `@sec-` plus the id with `/` replaced by `-`.
5. Keep it to about 30–150 lines. Split above 200 lines.

The website numbers pages automatically. Within a branch, pages are ordered by
their first source key.

### Before committing

```bash
make check   # must report 0 errors; warnings are open TODOs
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
4. Put the project URL and the **anon** key in `site/progress.html`. Never use
   the `service_role` key.
5. After signing in once, turn off "Allow new users to sign up" so that no one
   else can create an account.

## Repository layout

| Path | Contents |
|---|---|
| `notes/` | The notes (one folder per knowledge point) |
| `meta/` | Specification, taxonomy, notation, course registry |
| `build/` | Scripts: checks, website generator, one-off LaTeX migration |
| `site/` | Quarto website configuration; generated pages are not committed |
| `legacy/` | Original LaTeX notes, kept until migration review is finished |
| `.github/workflows/` | Builds and publishes the website on every push to `main` |

## Building

Requirements: Python 3 with PyYAML, [Quarto](https://quarto.org), a TeX
distribution (`pdflatex`) and `pdftocairo` (Poppler) for the diagrams.

```bash
make check     # validate notes (ids, references, YAML, problem/solution pairs)
make site      # generate and render the website into site/_site/
make preview   # live local preview
```

## Sources and copyright

- Problems marked `origin="external"` in `exercise.md` are copied from their
  sources (for example the FIT1058 Course Notes) for study purposes. **Their
  statements remain the copyright of their original authors and publishers**;
  each problem records its source in the `source` attribute.
- These problems are not covered by this repository's licence. They will be
  removed or replaced by citations on request from the copyright holder.
- Assignments, quizzes, exams, lecture slides and textbook files are never
  included.

## Licence

- **Notes and other original written content** (everything not listed below,
  excluding third-party problem statements): [CC BY-NC-SA 4.0](LICENSE).
- **Code** (`build/`, `site/`, `Makefile`, `.github/`): [MIT](LICENSE-CODE).

© 2026 alstonliow
