# Study repo: rules for Claude Code

Public study-notes repo. Notes are Markdown + YAML, built with Quarto and Pandoc Lua filters.
Read meta/PLAN.md and meta/SPEC.md before any task.

## Hard rules
- NEVER run git add, commit, push, reset, checkout, restore, stash, or config. The owner does all git operations.
- At the end of every task, list the changed files and propose ONE commit message (prefix: feat, migrate, fix, build, docs, chore). Do not commit.
- NEVER read, write, or reference raw/. Never add assignments, quizzes, exams, lecture slides, or textbook text.
- Do not invent taxonomy nodes, rename ids, or change YAML fields without asking.
- Never put git write commands in scripts or the Makefile.

## Content rules
- Notes are in English.
- Copy problem statements verbatim. Never paraphrase or shorten them.
- Never fabricate sources. If a source is unknown, leave `source` empty and add a TODO comment.
- Mechanical migration means convert and tag only. Do not rewrite or improve the author's wording. Set `status: draft`.
- Every `problem` block needs `origin` and `source`. Each solution is paired by id in solution.md.
- Proofs: numbered steps, separate paragraphs, no dense blocks.
- Display math for definitions and theorems. Cross-references use labels, never plain text like "Section 1.6".
- Follow meta/notation.md for symbols.

## Structure
- One knowledge point per folder under notes/: note.md, example.md, exercise.md, solution.md (only note.md is required).
- id equals the path without the notes/ prefix. Folder names are lowercase English with hyphens.
- Granularity: about one subsection, 30-150 lines. Split above 200 lines, merge below 10.

## Workflow
- One task per session. Keep changes small and reviewable.
- Run `make check` before reporting a task done.
- If a request conflicts with these rules or SPEC, stop and ask.
