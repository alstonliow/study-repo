> **Note.** English translation of `meta/PLAN.zh.md` (the original). If they differ, the Chinese original wins.
> The root `CLAUDE.md` supersedes the sample CLAUDE.md shown in §5.2.
> Git operations are done by the owner in GitHub Desktop; the CLI steps in §5.3 map to its Changes/Commit view.

# Study Repository Full Plan v2

Consolidates all earlier discussions and every decision you made, and adds how to work with Claude Code.

## 0. Decisions Made

| Item | Decision |
|---|---|
| Organisation | By knowledge topic only; sources (Monash/MIT/UCB/textbooks) are metadata and mappings only |
| Note format | Markdown + YAML header, one folder per knowledge point |
| Language | All English (`id`, titles, body, tags) |
| Toolchain | Quarto (website and PDF from one source), Lua filters for custom blocks |
| Outputs | PDF generated from selection/manifest, public website, practice-paper PDF |
| Visibility | Fully public (GitHub Pages) |
| Exercises | Public repo holds full problem statements; solutions in a separate `solution.md` |
| 1058 tutorial/workshop | Statements and solutions may be public (CN agreed; you are non-commercial) |
| Assignments, quizzes, exams | Never enter the repo |
| Licence | Notes CC BY-NC-SA 4.0; script code separately MIT |
| First batch scope | Discrete maths, FIT1058 course scope only |
| Migration approach | Pilot one chapter first, then decide |
| Time | 3–8 hours per week |
| Git | Claude Code never commits; all done manually by you |

## 1. Repository Structure

```
study-repo/
├── CLAUDE.md                 # Project rules for Claude Code (you write first)
├── .claude/settings.json     # Permission guardrails (you write first)
├── README.md                 # Includes source statement and copyright notice
├── LICENSE                   # CC BY-NC-SA 4.0 (content)
├── LICENSE-CODE              # MIT (scripts under build/)
├── _quarto.yml
├── Makefile
├── .gitignore
├── meta/
│   ├── SPEC.md               # Spec (dirs/id/YAML/block types/granularity); rarely changed once frozen
│   ├── taxonomy.md           # Topic skeleton
│   ├── notation.md           # Notation standard
│   ├── PROVENANCE.md         # External material sources and CN consent statement
│   └── preamble.tex          # Reuses 1058note styling
├── notes/
│   └── math/discrete/<branch>/<topic>/
│       ├── note.md
│       ├── example.md
│       ├── exercise.md
│       └── solution.md
├── sources/                  # Source → note mapping
│   └── monash/fit1058.md
├── views/                    # Note export lists (manifests)
├── papers/                   # Practice-paper specs
├── build/
│   ├── filters/              # Lua filters
│   ├── check.py              # Check script
│   ├── make_note.py          # Concatenate per manifest and render PDF
│   └── make_paper.py         # Practice-paper generation
├── code/                     # Course projects, LeetCode
├── legacy/                   # Old .tex notes; emptied once migrated
├── raw/                      # Copyrighted material, assignments/exams (gitignored)
└── out/                      # Generated PDFs (gitignored)
```

`out/` is not committed, so practice papers compiled from external problem statements are not placed directly in the public repo.

## 2. SPEC Core Rules

**2.1 Paths and ids**: `id` equals the path (minus `notes/`), e.g. `math/discrete/logic/propositional/truth-values`; not maintained separately. Directory names are lowercase English with hyphens, at most 3–4 levels.

**2.2 YAML header** (every `note.md`):

```yaml
---
title: Truth Values
sources: [fit1058-w4, rosen-1.1]
requires: [math/discrete/logic/propositional/statements]
level: core          # core | extra (first batch does not use extra)
status: draft        # draft | done
---
```

**2.3 Block types**: `definition`, `theorem`, `lemma`, `corollary`, `proof`, `example`, `remark`, `problem`, `solution`, `extra`. Numbered blocks that get referenced use Quarto id prefixes (`def-`, `thm-`, `lem-`, etc.). P3 must verify these custom blocks render correctly on both the website and PDF.

**2.4 Problem attributes** (`exercise.md`; full statement copied verbatim, not rewritten):

```markdown
::: {.problem #prob-induction-03 origin="external" source="fit1058-tut6-q3" difficulty="2" tags="induction,divisibility"}
……full statement……
:::
```

In `solution.md`, pair by the same id:

```markdown
::: {.solution for="prob-induction-03"}
1. ……

2. ……
:::
```

`origin` is `self` or `external`. To take external problems down later, a script batch-replaces `external` statements with citations.

**2.5 Writing conventions**: proofs in steps (numbered list); important formulas in display blocks; cross-references via labels, never "§1.6"; notation follows `notation.md`.

**2.6 Knowledge-point granularity**: roughly one `\subsection` of 1058note; `note.md` 30–150 lines; split only above 200 lines, merge into a neighbour below 10. Start coarse; when splitting later, keep the original id as an overview.

**2.7 SPEC freeze rule**: revise once after the P3 pilot and freeze as v0.2. Do not change structure while migrating the first 20 knowledge points; record desired changes in `meta/ideas.md` and apply them in one batch afterwards.

## 3. Build and Outputs

All three outputs share the same md files and the same Lua filters:

| Output | Entry | Process |
|---|---|---|
| Note PDF | `views/xxx.yml` (hand-written manifest; v1 has no selection UI) | `make_note.py` generates `\section` levels from directory depth, concatenates into a temporary `.qmd`, `quarto render` to PDF, using `meta/preamble.tex` |
| Practice-paper PDF | `papers/xxx.yml` | `make_paper.py` scans `problem` blocks in `exercise.md`, filters by path/difficulty/tags/origin; options include whether to attach `solution.md` |
| Website | `quarto render` | Sidebar generated by script from the directory tree; GitHub Actions publishes to Pages |

Manifest example:

```yaml
title: FIT1058 Review
include:
  - path: math/discrete/logic/propositional
    files: [note, example]
  - path: math/discrete/proof/induction
    files: [note, example, exercise]
options: {include_extra: true, order: manifest}
```

Practice-paper spec example:

```yaml
title: Induction Practice
select: {path: math/discrete/proof/induction, difficulty: [1, 2], tags: [divisibility]}
options: {count: 10, solutions: false}
```

`check.py` checks: duplicate ids, broken references, missing YAML, `problem` missing `source`/`origin`, missing problem–solution pairing, `requires` pointing to non-existent nodes, accidental inclusion of `raw/` content.

## 4. Compliance and Licensing

- **CN consent**: keep the original record (email or message screenshot, in a private location) and confirm two points: whether it covers a public website, and whether it covers both statements and solutions. `PROVENANCE.md` contains only a one-sentence summary, no screenshots.
- **README statement**: copyright of third-party problems belongs to the original authors, quoted for study only; CC BY-NC-SA covers only the author's own content.
- **Textbook problems (Rosen, Stewart)**: you have accepted the risk; the `origin="external"` attribute ensures batch takedown is always possible.
- **Never in the repo**: assignments, quizzes, exams, original lecture slides, textbook PDFs.
- **Claude Code constraints**: see next section, written into CLAUDE.md.

## 5. Working with Claude Code

### 5.1 Division of Labour

| You | Claude Code |
|---|---|
| Review SPEC, decide granularity and taxonomy | Draft SPEC/taxonomy, build skeleton |
| Review every converted note item by item (against the original PDF) | Pandoc conversion, splitting, adding YAML and block markup |
| All `git add` / `git commit` / `git push` | Write Lua filters, build scripts, check.py, CI config |
| Settings on the GitHub website (Pages, repo visibility) | Read-only checks (`git status`, `git diff`, `find`) |

### 5.2 Guardrails First, Then Start Claude Code

Before the first launch, you write these two files by hand.

`.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(git status *)",
      "Bash(git diff *)",
      "Bash(git log *)"
    ],
    "deny": [
      "Bash(git add *)",
      "Bash(git commit *)",
      "Bash(git push *)",
      "Bash(git * commit *)",
      "Bash(git * push *)",
      "Bash(git reset *)",
      "Bash(git rebase *)",
      "Bash(git merge *)",
      "Bash(git checkout *)",
      "Bash(git restore *)",
      "Bash(git clean *)",
      "Bash(git stash *)",
      "Bash(git config *)",
      "Read(./raw/**)"
    ]
  }
}
```

Per the official permissions documentation: rules are evaluated in the order deny, ask, allow, and the first match wins; permissions are enforced by Claude Code, whereas instructions in CLAUDE.md only influence Claude's tendencies and do not change what it is allowed to do. So "no commits" must rely on deny rules; CLAUDE.md is only a supplement. Bash rules support wildcards in the middle of a command, e.g. `git * main`; the `git * commit *` above blocks variants like `git -C . commit`.

After launch, confirm the rules are active with `/permissions`. Two more points:

- Do not put `git commit` in the Makefile or scripts, because calls inside scripts are outside the Bash rules' view.
- You may also put the same deny rules in user-level `~/.claude/settings.json` to guard against other projects missing them.

`CLAUDE.md` (English, short):

```markdown
# Study repo — rules for Claude Code

## Hard rules
- NEVER run git add/commit/push/reset/checkout/restore/stash. The owner does all git operations.
- At the end of every task: list changed files and propose ONE commit message (conventional prefix: feat/migrate/fix/build/docs/chore). Do not commit.
- NEVER read, write or reference anything in raw/. Never add assignments, quizzes, exams, slides or textbook text.
- Follow meta/SPEC.md. Do not invent new taxonomy nodes, rename ids, or change YAML fields without asking.

## Content rules
- Notes are in English. Problem statements are copied verbatim; never paraphrase.
- Never fabricate sources. If a source is unknown, leave `source` empty and add a TODO comment.
- Mechanical migration = convert and tag only. Do not rewrite or "improve" the author's wording. Set `status: draft`.
- Proofs: numbered steps, separated paragraphs. Cross-references via labels, not plain-text section numbers.

## Workflow
- One task per session. Keep changes small and reviewable.
- Run `make check` before reporting a task done.
```

### 5.3 Your Commit Flow (once per task)

```bash
git status
git diff --stat
git diff                      # review every change; check note content against the original PDF
make check
git add <specific paths>      # not git add -A, to avoid pulling in raw/ or PDFs
git commit -m "migrate(discrete): logic/propositional truth-values"
# after a batch of tasks
git push
```

| Prefix | Use |
|---|---|
| `migrate` | Old notes moved into notes/ |
| `feat` | New notes or features |
| `build` | Filters, scripts, CI |
| `docs` | SPEC, README, taxonomy |
| `fix` | Fix errors in notes or scripts |
| `chore` | Skeleton, ignore, config |

Commit granularity: one knowledge point or one chapter per commit; one kind of change per commit. Optional: set up your own `.git/hooks/pre-commit` (triggered by your own commits) that rejects staged content containing `raw/`, `*.pdf`, `.env`.

### 5.4 Prompt Template for Each Session

```
Task: <one sentence>
Context: read CLAUDE.md and meta/SPEC.md first.
Input: <file or directory>
Output: <files to produce>
Constraints: no rewriting of wording; verbatim problem statements; do not touch git.
Done when: make check passes; list changed files and propose a commit message.
```

## 6. Phased Plan

Estimated at 3–8 hours per week; each phase has a timebox, and when it expires you move on whether or not it is perfect.

| Phase | Content | You | Claude Code | Acceptance | Timebox |
|---|---|---|---|---|---|
| **P0 Inventory** | Go through `Monash`, `discrete_mathematic`, `Algorithm`, `Advanced_math`, `UECnote` one by one; sort into "own source files / copyrighted & assignments/exams / build artefacts"; find the CN consent record; send me the 1058note TOC | Classify, find record | Optional: read-only scan, produce list, check for nested `.git` | A classification list | 2 hours |
| **P1 Skeleton & SPEC** | Create repo; hand-write `.claude/settings.json` and `CLAUDE.md`; have Claude Code draft SPEC v0.1, taxonomy, notation, directories, `.gitignore`, README, licences | Review SPEC, decide top two taxonomy levels | Draft files | SPEC v0.1 approved by you | Week 1 |
| **P2 Move-in** | `cp` old files into `legacy/` and `code/`, keep original folders; before committing check `git status` has no PDFs or `raw/` | Move, first commit | None | A clean first commit | End of week 1, 1–2 hours |
| **P3 Pilot** | Pick one chapter of 1058note (a smaller one suggested), Pandoc to md, split into 3–5 knowledge points per SPEC, add YAML, block markup, problem attributes, solutions | Line-by-line review against the original PDF | Convert, split, mark up | Pilot chapter passes `check.py`; **decision point**: if mechanical conversion needs few changes, migrate all remaining chapters mechanically, otherwise switch to rewriting; revise SPEC to v0.2 and freeze | Week 2, 4–6 hours |
| **P4 PDF build v1** | Extract preamble from 1058note; write Lua filters; `make_note.py` renders from a hand-written manifest | Compare old and new PDFs side by side | Write code | Pilot chapter PDF layout close to the old one; environments, numbering, references work (page-for-page match not required) | Weeks 3–4, capped at 2 weeks |
| **P5 Practice papers** | `make_paper.py` selects problems by filter, optionally with solutions | Accept output | Write code | One practice-paper PDF generated from the pilot chapter | Week 5 |
| **P6 Website** | `_quarto.yml`, sidebar script, GitHub Actions, Pages | Enable Pages on GitHub, check public content | Write config and scripts | Live site reachable, maths and references correct, no `raw/` content | Week 6 |
| **P7 Bulk migration** | In 1058 chapter order, one loop per chapter: convert → review → `check.py` → commit → delete the matching part of `legacy/` | Review, commit | Convert | `legacy/` empty, all chapters in `notes/` | Ongoing, 1–2 chapters per week |
| **P8 Source index** | Script generates `sources/monash/fit1058.md` in reverse from YAML `sources` | Spot-check | Write script | Index consistent with notes | After P7 is half done |
| **Later** | Selection UI (after 30+ knowledge points); second batch: Rosen extensions (using `level: extra`), MIT 6.042, calculus | | | | TBD |

**First batch done when**: all 1058 chapters are in `notes/`, `make check` passes, the website is published, and at least 3 practice papers can be generated.

## 7. Daily Workflow

1. When learning or reviewing a knowledge point, open `taxonomy.md` to find its place; add it first if missing
2. Create the knowledge-point folder and write `note.md` (Claude Code may draft; you rewrite in your own words)
3. Put examples, exercises and solutions in their files
4. `make check` → commit yourself following §5.3
5. When you need review material, write a manifest, or write a papers spec to produce a practice paper
6. After each batch of commits, `git push`; the website updates automatically

## 8. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Assignments, exam questions or slides leak into the public repo | `raw/` in `.gitignore` and `Read` deny; only `git add <specific paths>`; optional pre-commit hook |
| Claude Code commits on its own | Hard block via deny rules; check with `/permissions` after launch; scripts contain no git write operations |
| Claude Code rewrites statements or fabricates sources | Explicitly forbidden in CLAUDE.md; you check `source` and statements against originals |
| External problems must be taken down | `origin="external"` + batch replacement script; `out/` not committed |
| Perfectionist procrastination | Timeboxes; P4 only requires "close"; SPEC freeze; migrate mechanically first, polish later |
| Quarto's custom-block support insufficient | Verify in P3 first; fall back on Lua filters if needed, without affecting the md itself |
| Repeated taxonomy changes | At most 3–4 directory levels; record desired changes in `meta/ideas.md` and adjust in one batch |

## 9. Next Steps

1. Send me the TOC page (chapter list) of 1058note's `main.pdf`; I will draft the discrete-maths part of `taxonomy.md` and SPEC v0.1
2. Confirm the scope of CN's consent (whether it covers a public website, statements and solutions)
3. On day one, do P0 first, then hand-write `.claude/settings.json` and `CLAUDE.md`, and only then start Claude Code

This plan can be saved as `meta/PLAN.md` so every Claude Code session can reference it.
