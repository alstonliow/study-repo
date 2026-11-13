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
