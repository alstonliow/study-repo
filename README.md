# Study Notes

Study notes in mathematics, computer science and artificial intelligence,
organised by topic rather than by course or textbook.

**Website:** <https://alstonliow.github.io/study-repo/>

This is a personal project. It is **not affiliated with or endorsed by any
university** whose courses it follows, and it is not official course material.

## Contents

| Field | Parts |
|---|---|
| Mathematics | Discrete Mathematics · Single Variable Calculus · Multivariable Calculus · Linear Algebra · Real Analysis · Probability · Statistics · Convex Optimization · Numerical Analysis |
| Computer Science | Algorithms · Theory of Computation · Cryptography |
| Artificial Intelligence | Machine Learning · Deep Learning · Search and Constraint Satisfaction · Reinforcement Learning and Games · Probabilistic Reasoning |

The topic tree is [`meta/taxonomy.yml`](meta/taxonomy.yml). Courses mapped onto
it so far:

- **MIT:** 6.006, 6.041, 6.042J, 6.046, 18.01, 18.02, 18.05, 18.06, 18.065,
  18.335J, 18.404J, 18.650
- **Stanford:** CS221, CS229, CS231n, EE364A
- **UC Berkeley:** CS70, CS188, EECS126
- **Cambridge:** IA Analysis I, IB Analysis and Topology, IB Linear Algebra,
  II Probability and Measure
- **Monash:** FIT1058

## Design

- **One knowledge point, one place.** Each topic is a single folder under
  `notes/`, written once. When several sources cover the same definition or
  theorem, the notes keep one version, the best of them, and record every
  source.
- **Courses are views.** A course is a file in `meta/courses/` that lists, for
  each point of its outline, the notes or single blocks it covers. Selecting a
  course on the website folds everything outside its scope.
- **Stable ids, generated numbers.** Every definition, theorem, example and
  problem has a permanent id. Numbers are derived from the outline being read,
  so the same theorem can sit in several outlines without renumbering anything.
- **Relationships written once.** Prerequisites and relations such as `uses` or
  `generalizes` are recorded at their source; reverse links, prerequisite graphs
  and summary pages are generated.
- **Own words.** Explanations and solutions are written here. Problem statements
  from courses are quoted verbatim with their source; official solutions are
  never copied.

## Using the website

- **Read by topic** from the sidebar, or **by course** with the course filter.
- Each page has **Connections**: prerequisites, related results, and every page
  that refers to it.
- Figures, many with **interactive step-by-step widgets**; some exercises are
  **runnable code** with tests.
- **Library** lists the books and lecture notes behind the notes and what each
  section covers.
- **Export** builds a PDF of any selection: a branch, a course, with or without
  solutions.
- **Progress marks** (New → Learned → Reviewing → Mastered) on every note and
  exercise, saved in the browser and optionally synced.

## Building

Requires Python 3 with PyYAML, [Quarto](https://quarto.org), a TeX distribution
and Poppler (`pdftocairo`).

```bash
make check    # validate notes, references and course files
make preview  # live local preview of the website
make pdf      # PDFs into out/pdf/
```

How the repository is laid out and how to add notes, problems, figures and
courses: [`meta/CONTRIBUTING.md`](meta/CONTRIBUTING.md). Full specification:
[`meta/SPEC.md`](meta/SPEC.md).

## Sources and copyright

- Problems marked `origin="external"` are copied from their sources for study
  purposes. **Their statements remain the copyright of their original authors
  and publishers**; each records its source in the `source` attribute. They are
  not covered by this repository's licence and will be removed or replaced by
  citations on request from the copyright holder.
- Official solutions are never copied; every solution here is our own.
- Quizzes, exams, lecture slides and textbook files are never included.
- Code excerpts from permissively licensed resources are listed in
  [`NOTICES.md`](NOTICES.md).

## Licence

- **Notes and other original written content** (everything not listed below,
  excluding third-party problem statements): [CC BY-NC-SA 4.0](LICENSE).
- **Code** (`build/`, `site/`, `Makefile`, `.github/`): [MIT](LICENSE-CODE).

© 2026 alstonliow
