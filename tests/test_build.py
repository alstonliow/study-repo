"""Tests for the build scripts, run on a small fixture repository (tests/fixture).

    make test                                   # run all tests
    python3 tests/test_build.py --update        # accept new site output as expected

The site test compares the generated pages with tests/expected/. When a change to
the output is intended, run with --update and review the diff of tests/expected/
before committing it. Nothing here touches notes/ or meta/ of the real repository.
"""

from __future__ import annotations

import filecmp
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD = HERE.parent / "build"
FIXTURE = HERE / "fixture"
EXPECTED = HERE / "expected"
PY = sys.executable


def run(script: str, root: Path, *args: str, site: Path | None = None) -> subprocess.CompletedProcess:
    env = dict(os.environ, STUDY_ROOT=str(root))
    if site:
        env["STUDY_SITE"] = str(site)
    return subprocess.run([PY, str(BUILD / script), *args], env=env, capture_output=True, text=True)


def generate(root: Path) -> Path:
    site = root / "site"
    site.mkdir(exist_ok=True)
    r = run("make_site.py", root, site=site)
    if r.returncode:
        raise AssertionError(r.stdout + r.stderr)
    return site


GENERATED = ["notes", "courses", "index.qmd", "_nav.yml", "site-data.json"]


def copy_generated(site: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    for name in GENERATED:
        src = site / name
        if src.is_dir():
            shutil.copytree(src, dest / name)
        elif src.exists():
            shutil.copy2(src, dest / name)


def diff_dirs(a: Path, b: Path) -> list[str]:
    out = []
    cmp = filecmp.dircmp(a, b)
    out += [f"only in expected: {x}" for x in cmp.left_only]
    out += [f"only in output: {x}" for x in cmp.right_only]
    for f in cmp.common_files:
        if (a / f).read_bytes() != (b / f).read_bytes():
            out.append(f"differs: {f}")
    for d in cmp.common_dirs:
        out += [f"{d}/{x}" for x in diff_dirs(a / d, b / d)]
    return out


class Repo(unittest.TestCase):
    """Each test works on a fresh copy of the fixture."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="study-test-"))
        self.root = self.tmp / "repo"
        shutil.copytree(FIXTURE, self.root)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def edit(self, rel: str, old: str, new: str) -> None:
        p = self.root / rel
        text = p.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture changed? '{old}' not in {rel}")
        p.write_text(text.replace(old, new, 1), encoding="utf-8")

    def check(self) -> subprocess.CompletedProcess:
        return run("check.py", self.root)


class TestSite(Repo):
    def test_output_matches_expected(self):
        out = self.tmp / "out"
        copy_generated(generate(self.root), out)
        problems = diff_dirs(EXPECTED, out) if EXPECTED.exists() else ["tests/expected/ is missing"]
        self.assertEqual(problems, [], "generated site differs from tests/expected/ "
                                       "(run: python3 tests/test_build.py --update, then review)")

    def test_scope_wrapping(self):
        site = generate(self.root)
        second = (site / "notes/t/alpha/second.qmd").read_text()
        self.assertIn('.scope-block data-courses="" data-kind="rmk"', second)
        third = (site / "notes/t/beta/third.qmd").read_text()
        self.assertIn('data-courses="" data-kind="prp"', third)      # only def-third is covered
        data = json.loads((site / "site-data.json").read_text())
        self.assertEqual(data["pages"]["notes/t/beta/third.html"], ["demo"])


class TestCheck(Repo):
    def test_fixture_is_clean(self):
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)

    def assertError(self, text: str):
        r = self.check()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn(text, r.stdout)

    def test_duplicate_id(self):
        self.edit("notes/t/beta/third/note.md", "#prp-third", "#thm-widget")
        self.assertError("duplicate id 'thm-widget'")

    def test_broken_reference(self):
        self.edit("notes/t/alpha/second/note.md", "@def-widget", "@def-nothing")
        self.assertError("broken reference @def-nothing")

    def test_reference_inside_maths(self):
        self.edit("notes/t/alpha/first/note.md", "$$ w = 1. $$", "$$ w = 1 \\text{ @thm-gadget} $$")
        self.assertError("inside maths cannot be a link")

    def test_missing_yaml_field(self):
        self.edit("notes/t/beta/third/note.md", "status: done\n", "")
        self.assertError("missing YAML field 'status'")

    def test_problem_without_origin(self):
        self.edit("notes/t/alpha/first/exercise.md", 'origin="self" ', "")
        self.assertError("problem missing origin")

    def test_block_without_id(self):
        self.edit("notes/t/alpha/first/note.md", "#rmk-first-1 ", "")
        r = self.check()
        self.assertIn("block(s) without an id", r.stdout)

    def test_note_missing_from_taxonomy(self):
        self.edit("meta/taxonomy.yml", "          - third\n", "")
        self.assertError("not listed under its branch")

    def test_course_unknown_id(self):
        self.edit("meta/courses/demo.yml", "covers: [def-third]", "covers: [def-gone]")
        self.assertError("unknown note or block 'def-gone'")

    def test_alias_clash(self):
        self.edit("notes/t/beta/third/note.md", "requires: [t/alpha/first]",
                  "requires: [t/alpha/first]\naliases: [t/alpha/first]")
        self.assertError("is the id of an existing note")


class TestMove(Repo):
    def move(self, old: str, new: str) -> subprocess.CompletedProcess:
        r = run("move_note.py", self.root, old, new)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r

    def test_move_note_to_other_branch(self):
        self.move("t/alpha/second", "t/beta/gadgets")
        self.assertFalse((self.root / "notes/t/alpha/second").exists())
        note = (self.root / "notes/t/beta/gadgets/note.md").read_text()
        self.assertIn("aliases: [t/alpha/second]", note)
        first = (self.root / "notes/t/alpha/first/note.md").read_text()
        self.assertIn("@sec-t-beta-gadgets", first)
        self.assertNotIn("@sec-t-alpha-second", first)
        tax = (self.root / "meta/taxonomy.yml").read_text()
        self.assertIn("          - third\n          - gadgets\n", tax)
        self.assertIn("covers: [t/beta/gadgets]", (self.root / "meta/courses/demo.yml").read_text())
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)
        site = generate(self.root)
        page = (site / "notes/t/beta/gadgets.qmd").read_text()
        self.assertIn("/notes/t/alpha/second.html", page)            # redirect from the old address
        data = json.loads((site / "site-data.json").read_text())
        self.assertEqual(data["aliases"], {"t/alpha/second": "t/beta/gadgets"})

    def test_move_whole_branch(self):
        self.move("t/alpha", "t/gamma")
        self.assertTrue((self.root / "notes/t/gamma/first/note.md").exists())
        self.assertIn("- id: t/gamma", (self.root / "meta/taxonomy.yml").read_text())
        third = (self.root / "notes/t/beta/third/note.md").read_text()
        self.assertIn("requires: [t/gamma/first]", third)
        self.assertIn("@sec-t-gamma-first", third)
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_move_twice_keeps_both_aliases(self):
        self.move("t/beta/third", "t/beta/third-a")
        self.move("t/beta/third-a", "t/beta/third-b")
        note = (self.root / "notes/t/beta/third-b/note.md").read_text()
        self.assertIn("aliases: [t/beta/third, t/beta/third-a]", note)
        self.assertEqual(note.count("aliases:"), 1)
        self.assertEqual(self.check().returncode, 0)

    def test_dry_run_changes_nothing(self):
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        r = run("move_note.py", self.root, "t/alpha/first", "t/beta/first", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stdout)
        after = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_refuses_existing_target(self):
        r = run("move_note.py", self.root, "t/alpha/first", "t/beta/third")
        self.assertEqual(r.returncode, 1)
        self.assertIn("already exists", r.stdout)


class TestRequires(Repo):
    def test_cycle_is_an_error(self):
        self.edit("notes/t/alpha/first/note.md", "requires: []", "requires: [t/beta/third]")
        r = self.check()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("leads back to itself (cycle)", r.stdout)

    def test_later_prerequisite_warns(self):
        self.edit("notes/t/alpha/second/note.md", "requires: [t/alpha/first]", "requires: [t/beta/third]")
        r = self.check()
        self.assertIn("comes later in topic order", r.stdout)

    def test_redundant_prerequisite_warns(self):
        self.edit("notes/t/beta/third/note.md", "requires: [t/alpha/first]",
                  "requires: [t/alpha/first, t/alpha/second]")
        r = self.check()
        self.assertIn("already implied by another one", r.stdout)


class TestPages(Repo):
    def test_graphs_and_leads_to(self):
        site = generate(self.root)
        first = (site / "notes/t/alpha/first.qmd").read_text()
        self.assertIn("Leads to:", first)
        branch = (site / "notes/t/alpha/index.qmd").read_text()
        self.assertIn('class="dep-node"', branch)
        self.assertIn('data-item="t/alpha/second"', (site / "map.qmd").read_text())

    def test_branch_summary(self):
        site = generate(self.root)
        page = (site / "notes/t/alpha/summary.qmd").read_text()
        self.assertIn('data-kind="def" data-item="t/alpha/first"', page)
        self.assertIn("Widget theorem", page)
        self.assertNotIn("Trivial.", page)                         # statements only, no proofs
        self.assertIn('data-item="prob-first-01" data-level="medium"', page)
        self.assertIn("## Synthesis problems", page)
        self.assertIn(".problem-group .synthesis", page)
        nav = (site / "_nav.yml").read_text()
        self.assertIn("notes/t/alpha/summary.qmd", nav)

    def test_course_chapter_summary_keeps_scope(self):
        site = generate(self.root)
        ch2 = (site / "courses/demo/chapter-2.qmd").read_text()
        self.assertIn("Third", ch2)                                # def-third is covered
        self.assertNotIn("Not covered", ch2)                       # prp-third is not
        data = json.loads((site / "site-data.json").read_text())
        self.assertEqual(data["order"]["demo"][0]["summary"], "courses/demo/chapter-1.html")


class TestPdf(Repo):
    def assemble(self, *args) -> str:
        r = run("make_pdf.py", self.root, "--markdown-only", "--name", "t", *args)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return (self.root / "out/pdf/t.qmd").read_text()

    def test_book_has_everything_and_solutions_at_end(self):
        md = self.assemble()
        self.assertIn("## 1.1 First note {#sec-t-alpha-first}", md)
        self.assertIn("Every widget is a widget.", md)
        self.assertIn("## Synthesis problems", md)
        self.assertLess(md.index("Show that a widget"), md.index("# Solutions"))
        self.assertIn("\\begin{stbox}{defc}", md)                 # colour style by default

    def test_course_omit_extra(self):
        md = self.assemble("--scope", "course:demo", "--extra", "omit")
        self.assertNotIn("Beyond the course", md)                  # excluded remark
        self.assertNotIn("Not covered", md)                        # block outside the course
        self.assertIn("Third", md)

    def test_solutions_options(self):
        self.assertIn("*Solution (draft).*", self.assemble("--solutions", "inline"))
        self.assertNotIn("Solution", self.assemble("--solutions", "none"))
        self.assemble("--solutions", "separate")
        self.assertIn("Use both theorems.", (self.root / "out/pdf/t-solutions.qmd").read_text())

    def test_level_and_only(self):
        md = self.assemble("--only", "exercises", "--level", "hard", "--solutions", "none")
        self.assertIn("Combine", md)                               # the hard synthesis problem
        self.assertNotIn("Show that a widget", md)                 # a medium problem
        self.assertNotIn("Every widget is a widget.", md)          # no notes text
        md = self.assemble("--only", "summaries", "--solutions", "none")
        self.assertIn("## Definitions and results", md)
        self.assertNotIn("Trivial.", md)

    def test_plain_style_and_missing_references(self):
        md = self.assemble("--scope", "branch:t/beta", "--style", "plain")
        self.assertNotIn("stbox", md)
        self.assertIn("First note", md)                            # @sec- to a note not printed -> text
        self.assertNotIn("@sec-t-alpha-first", md)


class TestSelection(Repo):
    def assemble(self, *args) -> str:
        r = run("make_pdf.py", self.root, "--markdown-only", "--name", "t", *args)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return (self.root / "out/pdf/t.qmd").read_text()

    def test_branches_notes_and_types(self):
        md = self.assemble("--branches", "alpha", "--notes", "t/alpha/second", "--include", "result,exercise")
        self.assertIn("Second note", md)
        self.assertNotIn("First note {#", md)
        self.assertIn("Gadget theorem", md)
        self.assertNotIn("Use @thm-widget", md)              # proofs left out
        self.assertNotIn("Beyond the course", md)            # remarks left out

    def test_exercise_numbers_start_at_one(self):
        md = self.assemble("--only", "exercises", "--solutions", "none")
        self.assertIn("\\exercisehead{Exercise}{1}", md)
        self.assertIn("\\exercisehead{Exercise}{2}", md)
        self.assertIn("\\exercisehead{Review}{1.1}", md)

    def test_unknown_note_is_refused(self):
        r = run("make_pdf.py", self.root, "--markdown-only", "--notes", "t/nope")
        self.assertNotEqual(r.returncode, 0)

    def test_export_page_data(self):
        site = generate(self.root)
        self.assertTrue((site / "export.qmd").exists())
        data = json.loads((site / "site-data.json").read_text())
        self.assertEqual(data["titles"]["t/alpha/first"], "1.1 First note")
        self.assertEqual(data["reviews"], ["t/alpha"])
        page = (site / "notes/t/alpha/first.qmd").read_text()
        self.assertIn("[Exercise 1]", page)
        self.assertIn("[Exercise 2]", page)


class TestNumbering(Repo):
    def test_blocks_numbered_per_kind_on_the_page(self):
        site = generate(self.root)
        first = (site / "notes/t/alpha/first.qmd").read_text()
        self.assertIn('Definition [1.1.1]{.num data-note="t/alpha/first"} (Widget)', first)
        self.assertIn('Theorem [1.1.1]{.num data-note="t/alpha/first"} (Widget theorem)', first)
        self.assertIn('Example [1.1.1]{.num', first)
        self.assertNotIn("#thm-widget .theorem", first)      # no Quarto numbering
        self.assertIn('<span id="thm-widget" class="anchor"></span>', first)

    def test_references_use_numbers(self):
        site = generate(self.root)
        second = (site / "notes/t/alpha/second.qmd").read_text()
        self.assertIn('[Definition [1.1.1]{.num data-note="t/alpha/first"}](/notes/t/alpha/first.qmd#def-widget)', second)

    def test_course_numbers_in_site_data(self):
        site = generate(self.root)
        data = json.loads((site / "site-data.json").read_text())
        self.assertEqual(data["numbers"]["topic"]["t/beta/third"], "2.1")
        self.assertEqual(data["numbers"]["demo"]["t/beta/third"], "2.1")
        self.assertIn("kinds", data)

    def test_review_numbers(self):
        site = generate(self.root)
        page = (site / "notes/t/alpha/summary.qmd").read_text()
        self.assertIn("[Review 1.1]{.problem-title}", page)
        self.assertIn("from 1.1 First note", page)

    def test_pdf_titles_and_solution_labels(self):
        r = run("make_pdf.py", self.root, "--markdown-only", "--name", "t")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        md = (self.root / "out/pdf/t.qmd").read_text()
        self.assertIn("**Theorem 1.1.1**", md)
        self.assertIn("**Exercise 1.1.1.**", md)              # solutions at the end use full numbers
        self.assertIn("**Review 1.1.**", md)

    def test_cross_book_label(self):
        code = ("import model, numbering; r = model.Repo(); nb = numbering.build(r); "
                "nb.book['t/beta/third'] = 'Other Book'; "
                "print(nb.label('thm-widget', r.notes['t/alpha/first'], r.notes['t/beta/third']))")
        out = subprocess.run([PY, "-c", code], cwd=BUILD, capture_output=True, text=True,
                             env=dict(os.environ, STUDY_ROOT=str(self.root)))
        self.assertEqual(out.stdout.strip(), "Theorem 1.1.1 (Testing)", out.stderr)


def update_expected() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="study-test-"))
    try:
        root = tmp / "repo"
        shutil.copytree(FIXTURE, root)
        copy_generated(generate(root), EXPECTED)
        print(f"updated {EXPECTED.relative_to(HERE.parent)}; review the diff before committing")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    if "--update" in sys.argv:
        update_expected()
    else:
        unittest.main(verbosity=2)
