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


def run(script: str, root: Path, *args: str, site: Path | None = None,
        private: bool = False) -> subprocess.CompletedProcess:
    env = dict(os.environ, STUDY_ROOT=str(root))
    env.pop("STUDY_PRIVATE", None)
    if private:
        env["STUDY_PRIVATE"] = "1"
    if site:
        env["STUDY_SITE"] = str(site)
    return subprocess.run([PY, str(BUILD / script), *args], env=env, capture_output=True, text=True)


def generate(root: Path, private: bool = False) -> Path:
    site = root / "site"
    site.mkdir(exist_ok=True)
    r = run("make_site.py", root, site=site, private=private)
    if r.returncode:
        raise AssertionError(r.stdout + r.stderr)
    return site


GENERATED = ["notes", "courses", "library", "library.qmd", "projects", "projects.qmd", "index.qmd",
             "_nav.yml", "site-data.json"]


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


class TestCoding(Repo):
    def test_page_has_editor_data_and_badge(self):
        page = (generate(self.root) / "notes/t/alpha/first.qmd").read_text()
        self.assertIn('data-item="prob-first-code" data-level="" data-kind="code" data-packages=""', page)
        self.assertIn('data-item="prob-first-01" data-level="medium" data-kind="written"', page)
        self.assertIn("[Code]{.code-badge}", page)
        self.assertIn("::: {.coding-starter}", page)
        self.assertIn("::: {.coding-tests}", page)
        self.assertIn("[DEMO 1.10 Basics exercises]{.problem-source}", page)   # a node id as source
        self.assertIn("{.solution-withheld}", page)

    def test_pdf_prints_starter_not_tests(self):
        r = run("make_pdf.py", self.root, "--markdown-only", "--name", "t")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        md = (self.root / "out/pdf/t.qmd").read_text()
        self.assertIn('def double(x):\n    """Return 2 * x."""\n    ...', md)
        self.assertNotIn("def test_zero", md)
        self.assertIn("return 2 * x", md[md.index("# Solutions"):])


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

    def code_md(self, text: str) -> None:
        (self.root / "notes/t/alpha/first/code.md").write_text(text, encoding="utf-8")

    def test_code_example_needs_origin(self):
        self.code_md('::: {#exm-first-code-1 .example}\n```{.python .runnable}\nprint(1)\n```\n:::\n')
        self.assertError("code example needs origin")

    def test_copied_code_needs_source(self):
        self.code_md('::: {#exm-first-code-1 .example origin="adapted"}\n```{.python}\nprint(1)\n```\n:::\n')
        self.assertError("origin=adapted needs a source key")

    def test_code_syntax_error(self):
        self.code_md('::: {#exm-first-code-1 .example origin="self"}\n```{.python}\nprint(1\n```\n:::\n')
        self.assertError("Python syntax error")

    def test_code_example_ok(self):
        self.code_md('::: {#exm-first-code-1 .example origin="self"}\n```{.python .runnable packages="numpy"}\nprint(1)\n```\n\n```text\n1\n```\n:::\n')
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)

    # coding exercises (SPEC §6.4) and withheld solutions (§6.2 item 6)
    EX = "notes/t/alpha/first/exercise.md"
    SOL = "notes/t/alpha/first/solution.md"

    def test_coding_solution_runs(self):
        r = self.check()
        self.assertIn("coding: 1 exercises, 1 solutions run against their tests", r.stdout)
        self.assertNotIn("prob-first-withheld", r.stdout)          # withheld: no warning

    def test_coding_wrong_solution(self):
        self.edit(self.SOL, "return 2 * x", "return x + 2")
        self.assertError("solution of 'prob-first-code' does not pass its tests: failed: test_zero")

    def test_coding_starter_must_fail(self):
        self.edit(self.EX, '"""Return 2 * x."""\n    ...', '"""Return 2 * x."""\n    return x * 2')
        self.assertError("the starter of 'prob-first-code' passes its tests")

    def test_coding_is_never_external(self):
        self.edit(self.EX, 'coding origin="adapted"', 'coding origin="external"')
        self.assertError("a coding exercise has origin self or adapted")

    def test_coding_needs_one_tests_fence(self):
        self.edit(self.EX, "{.python .tests}", "{.python}")
        self.assertError("needs exactly one {.python .tests} fence (found 0)")

    def test_coding_syntax_error(self):
        self.edit(self.SOL, "return 2 * x", "return 2 * (x")
        self.assertError("solution of 'prob-first-code': Python syntax error")

    def test_coding_packages_allowed_only(self):
        self.edit(self.EX, 'coding origin="adapted"', 'coding packages="torch" origin="adapted"')
        self.assertError("package 'torch' is not allowed")

    def test_coding_undeclared_import(self):
        self.edit(self.SOL, "    return 2 * x", "    import numpy\n    return 2 * x")
        self.assertError("solution of 'prob-first-code' imports numpy")

    # C coding exercises (SPEC §6.4 item 10): the Python fixture exercise turned into C
    def to_c(self, sol_body: str = "return 2 * x;") -> None:
        self.edit(self.EX, """```{.python .starter}
def double(x):
    \"\"\"Return 2 * x.\"\"\"
    ...
```

```{.python .tests}
def test_small():
    assert double(2) == 4


def test_zero():
    assert double(0) == 0
```""", """```{.c .starter}
int double_it(int x) { return 0; }
```

```{.c .tests}
void test_small(void) { assert(double_it(2) == 4); }
void test_zero(void) { assert(double_it(0) == 0); }
```""")
        self.edit(self.SOL, """```{.python}
def double(x):
    \"\"\"Return 2 * x.\"\"\"
    return 2 * x
```""", "```{.c}\nint double_it(int x) { %s }\n```" % sol_body)

    def test_c_solution_runs(self):
        self.to_c()
        r = self.check()
        self.assertIn("coding: 1 exercises, 1 solutions run against their tests", r.stdout)
        self.assertNotIn("prob-first-code", r.stdout)

    def test_c_wrong_solution(self):
        self.to_c("return x + 2;")
        self.assertError("solution of 'prob-first-code' does not pass its tests: failed: test_zero (assertion failed)")

    def test_c_crash_fails_one_test(self):
        self.to_c("if (x == 0) { volatile int *p = 0; *p = 1; } return 2 * x;")
        self.assertError("does not pass its tests: failed: test_zero (signal")

    def test_c_compile_error(self):
        self.to_c("return 2 * x")
        self.assertError("solution of 'prob-first-code' does not pass its tests: compile error")

    def test_c_header_not_allowed(self):
        self.to_c("return 2 * x; }\n#include <curl/curl.h>\nint unused(void) { return 0;")
        self.assertError("solution of 'prob-first-code' includes curl/curl.h")

    def test_c_mixed_languages(self):
        self.to_c()
        self.edit(self.EX, "{.c .tests}", "{.python .tests}")
        self.assertError("the .tests fence must be {.c .tests}")

    def test_c_page_is_marked(self):
        self.to_c()
        page = (generate(self.root) / "notes/t/alpha/first.qmd").read_text(encoding="utf-8")
        self.assertIn('data-lang="c"', page)
        self.assertIn("```c\nint double_it", page)

    def test_withheld_with_solution_is_an_error(self):
        self.edit(self.SOL, 'for="prob-first-code"', 'for="prob-first-withheld"')
        self.assertError("'prob-first-withheld' is solution=\"withheld\" and must have no solution")

    def test_heading_in_problem(self):
        self.edit("notes/t/alpha/first/exercise.md", "Statement two.",
                  "Statement two.\n\n# A heading")
        self.assertError("no headings inside problems or solutions")

    def test_comment_in_code_is_not_a_heading(self):
        self.edit("notes/t/alpha/first/exercise.md", "Statement two.",
                  "Statement two.\n\n```python\n# a comment\nx = 1\n```")
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_widget_for_unknown_figure(self):
        w = self.root / "site" / "_assets" / "widgets.html"
        w.parent.mkdir(parents=True, exist_ok=True)
        w.write_text('<script>\nconst WIDGETS = {\n  "fig-nothing-1": { title: "x" },\n};\n</script>\n')
        self.assertError("widget for unknown figure fig-nothing-1")

    def test_parts_of_a_field_together(self):
        self.edit("meta/taxonomy.yml", "  - title: Testing\n", "  - title: Testing\n    field: F\n")
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)
        with open(self.root / "meta/taxonomy.yml", "a", encoding="utf-8") as fh:
            fh.write("  - title: Mid\n    branches: []\n  - title: Extra\n    field: F\n    branches: []\n")
        self.assertError("field 'F': its parts must be listed together")

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

    def test_coursework_repo_must_be_https(self):
        self.edit("meta/courses/demo.yml", "status: draft", "status: draft\n"
                  "coursework_repo:\n  url: http://example.org/demo-hw")
        self.assertError("coursework_repo.url must be an https URL")

    def test_alias_clash(self):
        self.edit("notes/t/beta/third/note.md", "requires: [t/alpha/first]",
                  "requires: [t/alpha/first]\naliases: [t/alpha/first]")
        self.assertError("is the id of an existing note")


class TestReadmeStats(Repo):
    MARKERS = ("<!-- stats:start (generated by build/readme_stats.py; do not edit) -->\n"
               "<!-- stats:end -->\n")

    def test_generate_then_check(self):
        readme = self.root / "README.md"
        readme.write_text("# Fixture\n\n" + self.MARKERS + "\nEnd.\n", encoding="utf-8")
        self.assertEqual(run("readme_stats.py", self.root, "--check").returncode, 1)
        self.assertIn("statistics are out of date", self.check().stdout)
        r = run("readme_stats.py", self.root)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        text = readme.read_text(encoding="utf-8")
        self.assertIn("| **Total** |", text)
        self.assertTrue(text.startswith("# Fixture") and text.endswith("End.\n"))
        self.assertEqual(run("readme_stats.py", self.root, "--check").returncode, 0)
        self.assertNotIn("README.md", self.check().stdout)

    def test_no_markers(self):
        (self.root / "README.md").write_text("# Fixture\n", encoding="utf-8")
        self.assertEqual(run("readme_stats.py", self.root).returncode, 2)
        self.assertNotIn("README.md", self.check().stdout)


class TestSiteShards(unittest.TestCase):
    """build/site_shards.py on a fake generated site (no Quarto needed)."""
    PAGES = ["index.qmd", "map.qmd", "library.qmd", "library/res-a.qmd", "library/res-b.qmd",
             "courses/c1.qmd", "courses/c1/chapter-1.qmd", "courses/c2.qmd",
             "notes/math/discrete/sets/index.qmd", "notes/math/discrete/sets/subsets.qmd",
             "notes/math/algebra/groups/index.qmd", "notes/cs/algo/sorting/merge-sort.qmd"]

    def setUp(self):
        sys.path.insert(0, str(BUILD))
        import site_shards
        self.ss = site_shards
        self.tmp = Path(tempfile.mkdtemp(prefix="study-shards-"))
        self.site = self.tmp / "site"
        for page in self.PAGES:
            f = self.site / page
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text("---\ntitle: x\n---\n", encoding="utf-8")
        (self.site / "_assets").mkdir()
        (self.site / "_assets" / "ignored.qmd").write_text("", encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_units_do_not_overlap(self):
        units = self.ss.units(self.ss.pages(self.site))
        self.assertEqual(sorted(units), sorted(self.PAGES))
        self.assertEqual(units["courses/c1.qmd"], "courses/c1.qmd")      # beside courses/c1/
        self.assertEqual(units["courses/c1/chapter-1.qmd"], "courses/c1")
        self.assertEqual(units["library/res-a.qmd"], "library")
        self.assertEqual(units["notes/math/discrete/sets/subsets.qmd"], "notes/math/discrete")
        folders = {u for u in units.values() if not u.endswith(".qmd")}
        for u in set(units.values()):
            self.assertFalse(any(u.startswith(f + "/") for f in folders), u)
        for n in (1, 3, 5):
            shards = self.ss.plan(self.site, n)
            flat = [u for s in shards for u in s]
            self.assertEqual(sorted(flat), sorted(set(units.values())))

    def fake_render(self, n: int) -> list[Path]:
        """Each shard writes its own pages, a stub index.html, and its search/sitemap entries."""
        out = []
        for k, todo in enumerate(self.ss.plan(self.site, n)):
            d = self.tmp / f"shard{k}"
            mine = [p for p, u in self.ss.units(self.ss.pages(self.site)).items() if u in todo]
            for p in mine:
                f = d / (p[:-4] + ".html")
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text(f"page {p}", encoding="utf-8")
            if "index.qmd" not in mine:
                (d / "index.html").write_text("redirect stub", encoding="utf-8")
            (d / "site_libs").mkdir(parents=True, exist_ok=True)
            (d / "site_libs" / "lib.js").write_text("same", encoding="utf-8")
            entries = [{"objectID": p[:-4] + ".html", "href": p[:-4] + ".html", "title": p} for p in mine]
            (d / "search.json").write_text(json.dumps(entries), encoding="utf-8")
            urls = "".join(f"<url><loc>https://x/{p[:-4]}.html</loc></url>" for p in mine)
            (d / "sitemap.xml").write_text(
                f'<?xml version="1.0"?><urlset xmlns="{self.ss.SITEMAP_NS}">{urls}</urlset>', encoding="utf-8")
            out.append(d)
        return out

    def test_merge(self):
        shards = self.fake_render(3)
        merged = self.tmp / "merged"
        self.assertEqual(self.ss.merge(self.site, 3, merged, shards), 0)
        self.assertEqual((merged / "index.html").read_text(encoding="utf-8"), "page index.qmd")
        for p in self.PAGES:
            self.assertTrue((merged / (p[:-4] + ".html")).exists(), p)
        search = json.loads((merged / "search.json").read_text(encoding="utf-8"))
        self.assertEqual(len(search), len(self.PAGES))
        self.assertEqual((merged / "sitemap.xml").read_text(encoding="utf-8").count("<loc>"), len(self.PAGES))
        self.assertTrue((merged / "site_libs" / "lib.js").exists())

    def test_merge_missing_page_fails(self):
        shards = self.fake_render(2)
        for f in shards[0].rglob("*.html"):
            if f.name != "index.html":
                f.unlink()
                break
        self.assertEqual(self.ss.merge(self.site, 2, self.tmp / "merged", shards), 1)


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

    def test_move_note_with_flow_style_lists(self):
        # notes: [a, b] lists (the style of the real taxonomy.yml) are edited in place
        import re
        tax_path = self.root / "meta/taxonomy.yml"
        tax = re.sub(r"(        notes:)[^\n]*\n((?:          - .*\n)+)",
                     lambda m: m.group(1) + " [" + ", ".join(x.strip()[2:] for x in m.group(2).splitlines())
                     + "]   # topic order\n", tax_path.read_text())
        tax_path.write_text(tax)
        self.move("t/alpha/second", "t/beta/gadgets")
        tax = tax_path.read_text()
        self.assertIn("notes: [first]   # topic order\n", tax)
        self.assertIn("notes: [third, gadgets]   # topic order\n", tax)
        self.assertEqual(self.check().returncode, 0)

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


    def split_fields(self):
        """Put t/beta under a first field Zeta and t/alpha under a second field Alpha."""
        self.edit("meta/taxonomy.yml", "      - id: t/beta\n        title: Beta\n        desc: Second test branch\n"
                  "        notes:\n          - third\n", "")
        self.edit("meta/taxonomy.yml", "parts:\n  - title: Testing\n",
                  "parts:\n  - title: Later\n    field: Zeta\n    branches:\n"
                  "      - id: t/beta\n        title: Beta\n        desc: Second test branch\n"
                  "        notes:\n          - third\n  - title: Testing\n    field: Alpha\n")

    def test_course_field_is_majority_of_covered_notes(self):
        self.split_fields()
        data = json.loads((generate(self.root) / "site-data.json").read_text())
        self.assertEqual(data["fields"], ["Zeta", "Alpha"])
        self.assertEqual(data["courses"][0]["field"], "Alpha")     # first, second vs third

    def test_course_field_tie_goes_to_first_field(self):
        self.split_fields()
        self.edit("meta/courses/demo.yml", "covers: [t/alpha/second]", "covers: [t/alpha/first]")
        data = json.loads((generate(self.root) / "site-data.json").read_text())
        self.assertEqual(data["courses"][0]["field"], "Zeta")      # first vs third: tie

    def test_coursework_repo_link(self):
        self.edit("meta/courses/demo.yml", "status: draft", "status: draft\n"
                  "coursework_repo:\n  url: https://example.org/demo-hw")
        page = (generate(self.root) / "courses/demo.qmd").read_text()
        self.assertIn("Coursework code: [https://example.org/demo-hw]", page)

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



class TestRelations(Repo):
    """Acceptance tests for typed relationships, backlinks and placement (SPEC §17)."""

    THIRD = "notes/t/beta/third/note.md"

    def add_relations(self, yaml_lines: str, rel: str = THIRD) -> None:
        self.edit(rel, "status:", yaml_lines + "\nstatus:")

    def assertCheck(self, code: int, text: str = "") -> str:
        r = self.check()
        self.assertEqual(r.returncode, code, r.stdout)
        if text:
            self.assertIn(text, r.stdout)
        return r.stdout

    def test_uses_gives_forward_and_backlink(self):
        self.add_relations("relations:\n  uses: [t/alpha/second]")
        self.edit(self.THIRD, '{#prp-third .proposition name="Not covered"}',
                  '{#prp-third .proposition name="Not covered" uses="def-widget"}')
        self.assertCheck(0, "relationships: 4 typed")
        site = generate(self.root)
        third = (site / "notes/t/beta/third.qmd").read_text()
        self.assertIn("Uses: [1.2 Second note](/notes/t/alpha/second.qmd)", third)
        self.assertIn("(#prp-third) *uses* [Definition [1.1.1]", third)
        second = (site / "notes/t/alpha/second.qmd").read_text()
        self.assertIn("- This topic *used by* [2.1 Third note](/notes/t/beta/third.qmd)", second)
        first = (site / "notes/t/alpha/first.qmd").read_text()
        self.assertIn("(#def-widget) *used by* [Proposition [2.1.1]", first)

    def test_reference_is_a_backlink_not_uses(self):
        site = generate(self.root)
        first = (site / "notes/t/alpha/first.qmd").read_text()
        conn = first[first.index("## Connections"):]
        self.assertIn("**Referenced by**", conn)
        self.assertIn("- This topic ← [Definition [2.1.1]", conn)    # @sec-t-alpha-first in third
        self.assertNotIn("**Relationships**", conn)
        self.assertNotIn("used by", conn)

    def test_symmetric_relation_once_or_twice(self):
        self.add_relations("relations:\n  related: [t/alpha/first]")
        self.assertCheck(0)
        site = generate(self.root)
        self.assertIn("Related: [2.1 Third note]", (site / "notes/t/alpha/first.qmd").read_text())
        self.add_relations("relations:\n  related: [t/beta/third]", "notes/t/alpha/first/note.md")
        self.assertCheck(0, "related is symmetric; write it on one side only")

    def test_requires_cycle_is_an_error(self):
        self.edit("notes/t/alpha/first/note.md", "requires: []", "requires: [t/beta/third]")
        self.assertCheck(1, "requires leads back to itself (cycle)")

    def test_acyclic_type_cycle_is_an_error(self):
        self.add_relations("relations:\n  generalizes: [t/alpha/first]")
        self.add_relations("relations:\n  generalizes: [t/beta/third]", "notes/t/alpha/first/note.md")
        self.assertCheck(1, "generalizes has a cycle: t/alpha/first -> t/beta/third -> t/alpha/first")

    def test_uses_cycle_is_allowed(self):
        self.add_relations("relations:\n  uses: [t/alpha/first]")
        self.add_relations("relations:\n  uses: [t/beta/third]", "notes/t/alpha/first/note.md")
        self.assertCheck(0)

    def test_alias_as_target_is_an_error(self):
        self.edit(self.THIRD, "requires: [t/alpha/first]", "requires: [t/alpha/first]\naliases: [t/beta/old-third]")
        self.add_relations("relations:\n  uses: [t/beta/old-third]", "notes/t/alpha/second/note.md")
        self.assertCheck(1, "'t/beta/old-third' is an old id; use the current id 't/beta/third'")

    def test_alias_in_requires_and_reference_is_an_error(self):
        self.edit(self.THIRD, "requires: [t/alpha/first]", "requires: [t/alpha/first]\naliases: [t/beta/old-third]")
        self.edit("notes/t/alpha/second/note.md", "requires: [t/alpha/first]", "requires: [t/beta/old-third]")
        self.edit("notes/t/alpha/second/note.md", "Gadgets follow", "See @sec-t-beta-old-third. Gadgets follow")
        out = self.assertCheck(1, "requires 't/beta/old-third', an old id")
        self.assertIn("@sec-t-beta-old-third points to an old id; use @sec-t-beta-third", out)

    def test_unknown_type_end_and_target(self):
        self.add_relations("relations:\n  inspires: [t/alpha/first]")
        self.edit("notes/t/alpha/second/note.md", '{#thm-gadget .theorem name="Gadget theorem"}',
                  '{#thm-gadget .theorem name="Gadget theorem" requires="thm-widget" uses="thm-gadget idea-secret"}')
        out = self.assertCheck(1, "unknown relationship type 'inspires'")
        self.assertIn("requires is only from notes, not blocks ('thm-gadget')", out)
        self.assertIn("thm-gadget uses itself", out)
        self.assertIn("uses unknown id 'idea-secret'", out)

    def test_unknown_or_private_target_leaks_nothing(self):
        # A public build cannot see private entities: such a target is "missing" (SPEC §17.4.3).
        self.add_relations("relations:\n  related: [idea-secret]")
        self.assertCheck(1, "related unknown id 'idea-secret'")
        site = generate(self.root)
        for page in (site / "notes").rglob("*.qmd"):
            self.assertNotIn("idea-secret", page.read_text(), page)
        self.assertNotIn("idea-secret", (site / "site-data.json").read_text())

    def test_left_out_target_is_plain_text(self):
        md = run("make_pdf.py", self.root, "--markdown-only", "--name", "t", "--scope", "branch:t/beta")
        self.assertEqual(md.returncode, 0, md.stdout + md.stderr)
        text = (self.root / "out/pdf/t.qmd").read_text()
        self.assertIn("First note", text)
        self.assertNotIn("@sec-t-alpha-first", text)

    def test_note_covered_by_two_course_points_is_placed_at_the_first(self):
        self.edit("meta/courses/demo.yml", "        covers: [def-third]",
                  "        covers: [def-third]\n      - id: \"2.2\"\n        title: \"Again\"\n        covers: [t/alpha/first]")
        self.assertCheck(0)
        data = json.loads((generate(self.root) / "site-data.json").read_text())
        self.assertEqual(data["numbers"]["demo"]["t/alpha/first"], "1.1")
        self.assertEqual(data["numbers"]["demo"]["t/beta/third"], "2.1")

    def test_part_without_book(self):
        self.edit("meta/taxonomy.yml", "      - id: t/beta\n", "  - title: Loose\n    book: false\n    branches:\n      - id: t/beta\n")
        self.assertCheck(0)
        code = ("import model, numbering; r = model.Repo(); nb = numbering.build(r); "
                "f, t = r.notes['t/alpha/first'], r.notes['t/beta/third']; "
                "print(nb.section['t/beta/third']); print(nb.label('thm-widget', f, t)); print(nb.label('def-third', t, f))")
        out = subprocess.run([PY, "-c", code], cwd=BUILD, capture_output=True, text=True,
                             env=dict(os.environ, STUDY_ROOT=str(self.root)))
        self.assertEqual(out.stdout.split("\n")[:3], ["1.1", "Theorem 1.1.1 (Testing)", "Definition 1.1.1"], out.stderr)

    def test_book_flag_must_be_boolean(self):
        self.edit("meta/taxonomy.yml", "  - title: Testing\n", "  - title: Testing\n    book: maybe\n")
        self.assertCheck(1, "book must be true or false")



class TestResources(Repo):
    """Resources and legacy source keys (SPEC §17.12)."""

    RES = "resources/demo.yml"

    def py(self, code: str) -> list[str]:
        out = subprocess.run([PY, "-c", code], cwd=BUILD, capture_output=True, text=True,
                             env=dict(os.environ, STUDY_ROOT=str(self.root)))
        self.assertEqual(out.returncode, 0, out.stderr)
        return out.stdout.strip().split("\n")

    def resolve(self, *keys: str) -> list[str]:
        code = ("import model; r = model.Repo()\n"
                f"for k in {list(keys)!r}:\n"
                "    x = r.sources.resolve(k)\n"
                "    print(f'{x.resource} {x.edition} {x.node} {x.locator} {x.question}' if x else 'none')")
        return self.py(code)

    def test_locators_match_exactly(self):
        self.assertEqual(self.resolve("demo-1", "demo-1.1", "demo-1.10-q3", "demo-1.3"), [
            "res-demo 2026-01-01 res-demo-basics 1 None",
            "res-demo 2026-01-01 res-demo-widgets 1.1 None",
            "res-demo 2026-01-01 res-demo-basics-exercises 1.10 3",
            "none"])

    def test_nodes_in_entity_index_but_not_notes(self):
        out = self.py("import model; r = model.Repo(); e = r.entities['res-demo-widgets']; "
                      "print(e.type, e.holder, e.level, 'res-demo-widgets' in r.notes, r.resources['res-demo'].nodes['res-demo-widgets'].parent)")
        self.assertEqual(out, ["resource-node res-demo nodes False res-demo-basics"])

    def test_labels_unchanged(self):
        site = generate(self.root)
        first = (site / "notes/t/alpha/first.qmd").read_text()
        self.assertIn("DEMO 1.1 Q1", first)
        self.assertIn("Sources: `demo-1.1`", first)

    def test_unresolved_key_is_an_error(self):
        self.edit("notes/t/alpha/second/note.md", "sources: [demo-1.2]", "sources: [demo-1.3]")
        r = self.check()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("no node of res-demo is at 1.3 in edition 2026-01-01", r.stdout)

    def test_unknown_prefix_is_an_error(self):
        self.edit("notes/t/alpha/second/note.md", "sources: [demo-1.2]", "sources: [other-1.2]")
        r = self.check()
        self.assertIn("belongs to no resource", r.stdout)

    def test_locator_change_keeps_node_id(self):
        # a new edition renumbers 1.2 -> 1.5: only `at` changes; the node and old keys stay
        self.edit(self.RES, '    current: true\n', '    current: true\n  - id: "2027-01-01"\n')
        self.edit(self.RES, 'at: {"2026-01-01": "1.2"}', 'at: {"2026-01-01": "1.2", "2027-01-01": "1.5"}')
        self.assertEqual(self.check().returncode, 0)
        self.assertEqual(self.resolve("demo-1.2"), ["res-demo 2026-01-01 res-demo-gadgets 1.2 None"])
        out = self.py("import model; r = model.Repo(); print(r.resources['res-demo'].node_at('2027-01-01', '1.5').id)")
        self.assertEqual(out, ["res-demo-gadgets"])

    def test_duplicate_locator_and_node_id(self):
        self.edit(self.RES, 'at: {"2026-01-01": "1.2"}', 'at: {"2026-01-01": "1.1"}')
        r = self.check()
        self.assertIn("locator 1.1 of edition 2026-01-01 is also res-demo-widgets", r.stdout)
        self.edit(self.RES, "id: res-demo-gadgets", "id: res-demo-widgets")
        self.assertIn("node id 'res-demo-widgets' is used twice", self.check().stdout)

    def test_bad_ids_and_empty_fields(self):
        self.edit(self.RES, "id: res-demo-gadgets", "id: gadgets")
        self.edit(self.RES, "courses: [demo]", "courses: [demo]\nurl: ''")
        out = self.check().stdout
        self.assertIn("node id 'gadgets' must start with 'res-demo-'", out)
        self.assertIn("'url' is empty; leave it out instead", out)

    def test_resource_id_must_not_clash(self):
        self.edit("notes/t/beta/third/note.md", "#prp-third", "#res-demo-widgets")
        self.assertIn("'res-demo-widgets' is also the id of a note or block", self.check().stdout)



class TestLibrary(Repo):
    """covers, citations and the Library (SPEC §17.12.4–§17.12.7)."""

    RES = "resources/demo.yml"

    def cover(self, targets: str) -> None:
        self.edit(self.RES, '        at: {"2026-01-01": "1.1"}\n',
                  f'        at: {{"2026-01-01": "1.1"}}\n        covers: [{targets}]\n')

    def test_covers_shows_on_both_sides(self):
        self.cover("t/alpha/first, thm-gadget")
        self.assertEqual(self.check().returncode, 0)
        site = generate(self.root)
        lib = (site / "library/demo.qmd").read_text()
        self.assertIn("Covers: [1.1 First note](/notes/t/alpha/first.qmd), [Theorem [1.2.1]", lib)
        second = (site / "notes/t/alpha/second.qmd").read_text()
        self.assertIn("(#thm-gadget) *covered in* [DEMO 1.1 Widgets](/library/demo.qmd#res-demo-widgets)", second)
        first = (site / "notes/t/alpha/first.qmd").read_text()
        self.assertIn("- This topic *covered in* [DEMO 1.1 Widgets]", first)

    def test_citations_are_not_covers(self):
        site = generate(self.root)
        lib = (site / "library/demo.qmd").read_text()
        self.assertIn("Cited by: [1.1 First note](/notes/t/alpha/first.qmd), [Exercise [1.1.1]", lib)
        self.assertNotIn("Covers:", lib)
        self.assertNotIn("covered in", (site / "notes/t/alpha/first.qmd").read_text())

    def test_course_placement_is_not_covers(self):
        # the demo course covers t/alpha/first (placement): no relationship appears
        site = generate(self.root)
        self.assertNotIn("covered in", (site / "notes/t/alpha/first.qmd").read_text())

    def test_covers_ends_are_checked(self):
        self.edit("notes/t/beta/third/note.md", "status:", "relations:\n  covers: [t/alpha/first]\nstatus:")
        self.assertIn("covers is only from nodes and resources, not notes", self.check().stdout)  # written in resource files
        self.edit("notes/t/beta/third/note.md", "relations:\n  covers: [t/alpha/first]\n", "")
        self.cover("res-demo-gadgets")
        self.assertIn("covers is only to blocks and notes, not nodes ('res-demo-gadgets')", self.check().stdout)

    def test_root_covers_without_nodes_passes(self):
        (self.root / "resources/site.yml").write_text(
            "id: res-site\nkind: website\ntitle: A website\nurl: https://example.org\n"
            "covers: [t/beta/third]\n", encoding="utf-8")
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout)
        third = (generate(self.root) / "notes/t/beta/third.qmd").read_text()
        self.assertIn("- This topic *covered in* [A website](/library/site.qmd)", third)

    def test_root_covers_with_nodes_is_an_error(self):
        self.edit(self.RES, "courses: [demo]", "courses: [demo]\ncovers: [t/alpha/first]")
        r = self.check()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("res-demo has nodes, so covers goes on the node", r.stdout)

    def test_node_covers_with_nodes_passes(self):
        self.cover("t/alpha/first")
        self.assertEqual(self.check().returncode, 0)

    def test_covers_unknown_and_old_ids(self):
        self.edit("notes/t/beta/third/note.md", "requires: [t/alpha/first]", "requires: [t/alpha/first]\naliases: [t/beta/old]")
        self.cover("t/beta/old, def-nothing")
        out = self.check().stdout
        self.assertIn("covers 't/beta/old' is an old id; use the current id 't/beta/third'", out)
        self.assertIn("covers unknown id 'def-nothing'", out)

    def test_reference_to_a_node(self):
        self.edit("notes/t/beta/third/note.md", "Back to @sec-t-alpha-first.", "Back to @sec-t-alpha-first. Read @res-demo-gadgets.")
        self.assertEqual(self.check().returncode, 0)
        site = generate(self.root)
        third = (site / "notes/t/beta/third.qmd").read_text()
        self.assertIn("Read [DEMO 1.2 Gadgets](/library/demo.qmd#res-demo-gadgets)", third)
        lib = (site / "library/demo.qmd").read_text()
        self.assertIn("Referenced by: [Definition [2.1.1]", lib)
        r = run("make_pdf.py", self.root, "--markdown-only", "--name", "t")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("Read DEMO 1.2 Gadgets.", (self.root / "out/pdf/t.qmd").read_text())

    def test_broken_resource_reference(self):
        self.edit("notes/t/beta/third/note.md", "Back to @sec-t-alpha-first.", "See @res-demo-nothing.")
        self.assertIn("broken reference @res-demo-nothing", self.check().stdout)

    def test_library_lists_hierarchy_with_exact_locators(self):
        site = generate(self.root)
        lib = (site / "library/demo.qmd").read_text()
        self.assertIn("## 1 Basics {#res-demo-basics}", lib)
        self.assertIn("[1.10]{.node-loc} **Basics exercises**", lib)
        self.assertIn("[Demo course notes](/library/demo.qmd)", (site / "library.qmd").read_text())
        self.assertIn("library.qmd", (site / "_nav.yml").read_text())


def update_expected() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="study-test-"))
    try:
        root = tmp / "repo"
        shutil.copytree(FIXTURE, root)
        copy_generated(generate(root), EXPECTED)
        print(f"updated {EXPECTED.relative_to(HERE.parent)}; review the diff before committing")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)



class TestProjects(Repo):
    """Projects (SPEC §17.13): loader, checks, pages and the "Applied in" group."""

    PRJ = "projects/demo-tool/project.md"

    def assertCheck(self, text: str) -> str:
        r = self.check()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn(text, r.stdout)
        return r.stdout

    def test_loader(self):
        out = subprocess.run([PY, "-c", "import model; r = model.Repo(); p = r.projects['prj-demo-tool']; "
                              "print(p.kind, p.stage, p.started, r.entities[p.id].level, p.problems)"],
                             cwd=BUILD, capture_output=True, text=True, env=dict(os.environ, STUDY_ROOT=str(self.root)))
        self.assertEqual(out.stdout.strip(), "course active 2026-01-05 projects []", out.stderr)

    def test_private_store_is_never_read(self):
        priv = self.root / "private/projects/secret-work"
        priv.mkdir(parents=True)
        (priv / "project.md").write_text("---\nid: prj-secret-work\ntitle: Secret\n---\n")
        self.assertEqual(self.check().returncode, 0)
        site = generate(self.root)
        self.assertNotIn("secret", (site / "projects.qmd").read_text().lower())
        self.assertFalse((site / "projects/secret-work").exists())

    def test_bad_schema(self):
        self.edit(self.PRJ, "id: prj-demo-tool", "id: prj-other")
        self.edit(self.PRJ, "kind: course", "kind: homework")
        self.edit(self.PRJ, "stage: active", "stage: active\nowner: me")
        self.edit(self.PRJ, "commit: 0123abc", "commit: latest")
        self.edit(self.PRJ, "started: 2026-01-05", "started: 2026-01-05\nfinished: 2025-12-01")
        out = self.assertCheck("must match the folder name (prj-demo-tool)")
        for text in ("kind 'homework' not in course | personal", "unknown field 'owner'",
                     "commit 'latest' must be a commit sha", "finished 2025-12-01 is before started"):
            self.assertIn(text, out)

    def test_missing_fields(self):
        self.edit(self.PRJ, "status: draft\n", "")
        self.assertCheck("missing field 'status'")

    def test_unknown_course_and_assignment(self):
        self.edit(self.PRJ, "course: demo", "course: nosuch")
        self.edit(self.PRJ, "assignment: res-demo-widgets", "assignment: res-demo")
        out = self.assertCheck("course 'nosuch' is not a course")
        self.assertIn("assignment 'res-demo' must be a resource node, not a resource", out)

    def test_unknown_applies_target_and_wrong_end(self):
        self.edit(self.PRJ, "applies: [t/alpha/first, thm-gadget]", "applies: [t/alpha/nosuch, res-demo]\n  uses: [t/alpha/first]")
        out = self.assertCheck("applies unknown id 't/alpha/nosuch'")
        self.assertIn("applies is only to blocks and notes, not resources ('res-demo')", out)
        self.assertIn("uses is only from blocks and notes, not projects ('prj-demo-tool')", out)

    def test_notes_cannot_apply(self):
        self.edit("notes/t/alpha/second/note.md", '{#thm-gadget .theorem name="Gadget theorem"}',
                  '{#thm-gadget .theorem name="Gadget theorem" applies="thm-widget"}')
        self.assertCheck("applies is only from projects, not blocks ('thm-gadget')")

    def test_public_project_never_points_to_private(self):
        code = ("import model, relations; r = model.Repo(); r.entities['t/alpha/first'].visibility = 'private'; "
                "print([m for _, m in relations.Graph(r).check()])")
        out = subprocess.run([PY, "-c", code], cwd=BUILD, capture_output=True, text=True,
                             env=dict(os.environ, STUDY_ROOT=str(self.root)))
        self.assertIn("public prj-demo-tool applies private 't/alpha/first'", out.stdout, out.stderr)

    def test_broken_reference_in_write_up(self):
        self.edit(self.PRJ, "@thm-gadget", "@thm-nosuch")
        self.assertCheck("broken reference @thm-nosuch")

    def test_pages(self):
        site = generate(self.root)
        first = (site / "notes/t/alpha/first.qmd").read_text()
        self.assertIn("**Applied in**\n\n- This topic ← [Demo tool](/projects/demo-tool/index.qmd)", first)
        self.assertNotIn("*applied in*", first)                  # not mixed with "Used by"
        page = (site / "projects/demo-tool/index.qmd").read_text()
        self.assertIn("Assignment: [DEMO 1.1 Widgets](/library/demo.qmd#res-demo-widgets)", page)
        self.assertIn("Applies: [1.1 First note](/notes/t/alpha/first.qmd)", page)
        self.assertIn("A tool that puts [Theorem", page)
        self.assertIn("## Active\n\n- [Demo tool](/projects/demo-tool/index.qmd)", (site / "projects.qmd").read_text())
        self.assertIn("## Projects", (site / "courses/demo.qmd").read_text())


class TestYear(Repo):
    """The Year facet (SPEC §17.15.7): a problem's year comes from its source node,
    the nearest ancestor with one, or the resource."""

    def test_year_on_problem_groups(self):
        self.edit("resources/demo.yml", "status: draft\n", "status: draft\nyear: 2020\n")
        self.edit("resources/demo.yml", "title: Basics exercises\n", "title: Basics exercises\n        year: 2025-26\n")
        page = (generate(self.root) / "notes/t/alpha/first.qmd").read_text()
        self.assertIn('data-item="prob-first-01" data-level="medium" data-kind="written" '
                      'data-source="res-demo" data-source-label="Demo course notes" data-year="2020"', page)
        self.assertIn('data-source-label="Demo course notes" data-year="2025-26"', page)   # the coding exercise's node
        self.assertEqual(self.check().returncode, 0)

    def test_no_year_no_attribute(self):
        page = (generate(self.root) / "notes/t/alpha/first.qmd").read_text()
        self.assertNotIn("data-year", page)

    def test_bad_year(self):
        self.edit("resources/demo.yml", "status: draft\n", "status: draft\nyear: last year\n")
        r = self.check()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("year must be like 2024 or 2025-26", r.stdout)


PRIVATE_FILES = {
    "private/meta/taxonomy.yml": """parts:
  - title: Tutoring
    branches:
      - id: p/gamma
        title: Gamma
        desc: A private branch
        notes:
          - fourth
""",
    "private/notes/p/gamma/fourth/note.md": """---
title: Fourth note
sources: []
requires: [t/alpha/first]
status: draft
---

::: {#def-fourth .definition name="Private widget"}
Builds on @def-widget.
:::
""",
    "private/meta/courses/tut.yml": """id: tut
code: TUT1
name: "Tutoring course"
outline_from: "fixture"
status: draft
field: Tutoring
chapters:
  - num: 1
    title: "Only"
    points:
      - id: "1.1"
        title: "Private and public"
        covers: [t/alpha/first, p/gamma/fourth]
""",
    "private/resources/tbook.yml": """id: res-tbook
kind: book
title: Tutoring textbook
status: draft
courses: [tut]
editions:
  - id: "2024"
    current: true
nodes:
  - id: res-tbook-basics
    kind: chapter
    title: Basics
    at: {"2024": "1"}
    nodes:
      - id: res-tbook-widgets-ex
        kind: exercises
        title: Widget exercises
        at: {"2024": "1.1"}
      - id: res-tbook-review
        kind: review
        title: Review
        at: {"2024": "1.R"}
""",
    "private/meta/problem-types.yml": """- id: pt-count-widgets
  title: Count widgets
  title_zh: 数小部件
  note: t/alpha/first
""",
    "private/bank/tbook-widgets-ex/bank.md": """::: {.problem #prob-tb-1 origin="external" source="res-tbook-widgets-ex" practises="t/alpha/first" type="pt-count-widgets"}
How many widgets are there?
:::

::: {.problem #prob-tb-2 origin="external" source="res-tbook-widgets-ex" practises="p/gamma/fourth"}
Build a private widget.
:::
""",
    "private/bank/tbook-widgets-ex/solution.md": """::: {.solution for="prob-tb-1" status="draft"}
1. Count them.
:::
""",
    "private/bank/tbook-review/bank.md": """::: {.problem #prob-tb-r1 origin="external" source="res-tbook-review" practises="t/alpha/first"}
Review the widgets.
:::
""",
}


class TestPrivate(Repo):
    """The private store (SPEC §17.14): read only with STUDY_PRIVATE=1."""

    def setUp(self):
        super().setUp()
        for rel, text in PRIVATE_FILES.items():
            p = self.root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8")

    def private_check(self) -> subprocess.CompletedProcess:
        return run("check.py", self.root, private=True)

    def assertPrivateError(self, text: str):
        r = self.private_check()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn(text, r.stdout)

    def test_public_output_ignores_private_store(self):
        out = self.tmp / "out"
        copy_generated(generate(self.root), out)
        self.assertEqual(diff_dirs(EXPECTED, out), [], "a public build read private/")
        self.assertEqual(self.check().returncode, 0)

    def test_private_check_is_clean(self):
        r = self.private_check()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("private store: 1 notes, 1 courses, 1 resources", r.stdout)
        self.assertIn("question bank: 2 folders, 3 problems, 1 problem types", r.stdout)

    def test_private_site(self):
        site = generate(self.root, private=True)
        self.assertTrue((site / "notes/p/gamma/fourth.qmd").exists())
        data = json.loads((site / "site-data.json").read_text())
        self.assertIn({"id": "tut", "field": "Tutoring"},
                      [{"id": c["id"], "field": c["field"]} for c in data["courses"]])
        self.assertEqual(data["fields"][-1], "Tutoring")

    def test_missing_store_warns(self):
        shutil.rmtree(self.root / "private")
        r = self.private_check()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("private/ is missing", r.stdout)

    def test_public_reference_to_private(self):
        self.edit("notes/t/alpha/second/note.md", "@def-widget", "@def-fourth")
        self.assertPrivateError("public page references private 'def-fourth'")

    def test_public_requires_private(self):
        self.edit("notes/t/beta/third/note.md", "requires: [t/alpha/first]",
                  "requires: [t/alpha/first, p/gamma/fourth]")
        self.assertPrivateError("public note requires private 'p/gamma/fourth'")

    def test_public_course_covers_private(self):
        self.edit("meta/courses/demo.yml", "covers: [def-third]", "covers: [def-third, def-fourth]")
        self.assertPrivateError("public course points to private 'def-fourth'")

    def test_private_note_in_public_branch(self):
        (self.root / "private/notes/t/beta").mkdir(parents=True)
        (self.root / "private/notes/p/gamma/fourth").rename(self.root / "private/notes/t/beta/fifth")
        self.assertPrivateError("a private note must be in a branch of private/meta/taxonomy.yml")

    def test_private_id_clash(self):
        self.edit("private/notes/p/gamma/fourth/note.md", "#def-fourth", "#def-widget")
        self.assertPrivateError("duplicate id 'def-widget'")

    def test_bank_pages(self):
        site = generate(self.root, private=True)
        bank = (site / "courses/tut/bank-1.qmd").read_text()
        self.assertLess(bank.index("## Tutoring textbook 1.1 Widget exercises"), bank.index("## Tutoring textbook 1.R Review"))
        self.assertIn('data-ptype="pt-count-widgets" data-ptype-label="数小部件 (Count widgets)" data-set="exercises" '
                      'data-topics="t/alpha/first" data-topic-labels="1.1 First note"', bank)
        self.assertIn('data-set="review"', bank)
        self.assertIn("Draft solution", bank)
        self.assertIn("[Exercise 1]{.problem-title}", bank)
        first = (site / "notes/t/alpha/first.qmd").read_text()
        self.assertIn("题库: [TUT1 Ch 1: 2](/courses/tut/bank-1.qmd?topic=t/alpha/first)", first)
        self.assertNotIn("prob-tb-1", first)                 # never among a note's exercises
        self.assertNotIn("practised in", first)
        self.assertIn("[题库 (3) →](/courses/tut/bank-1.qmd)", (site / "courses/tut.qmd").read_text())

    def test_public_build_has_no_bank(self):
        site = generate(self.root)
        self.assertFalse((site / "courses/tut").exists())
        self.assertNotIn("题库", (site / "notes/t/alpha/first.qmd").read_text())

    def test_bank_problem_needs_practises(self):
        self.edit("private/bank/tbook-review/bank.md", ' practises="t/alpha/first"', "")
        self.assertPrivateError("a bank problem needs practises")

    def test_bank_unknown_type(self):
        self.edit("private/bank/tbook-review/bank.md", 'practises="t/alpha/first"',
                  'practises="t/alpha/first" type="pt-nothing"')
        self.assertPrivateError("unknown problem type 'pt-nothing'")

    def test_bank_type_note_not_practised(self):
        self.edit("private/bank/tbook-widgets-ex/bank.md", 'practises="p/gamma/fourth"',
                  'practises="p/gamma/fourth" type="pt-count-widgets"')
        self.assertPrivateError("type pt-count-widgets belongs to t/alpha/first, which is not in practises")

    def test_bank_folder_must_be_a_node(self):
        (self.root / "private/bank/tbook-review").rename(self.root / "private/bank/tbook-nothing")
        self.assertPrivateError("'res-tbook-nothing' is none")

    def test_bank_source_outside_folder_node(self):
        self.edit("private/bank/tbook-review/bank.md", 'source="res-tbook-review"', 'source="res-tbook-widgets-ex"')
        self.assertPrivateError("is not inside res-tbook-review")

    def test_bank_practises_unknown_note(self):
        self.edit("private/bank/tbook-review/bank.md", 'practises="t/alpha/first"', 'practises="t/alpha/gone"')
        self.assertPrivateError("practises unknown id 't/alpha/gone'")

    def test_problem_type_unknown_note(self):
        self.edit("private/meta/problem-types.yml", "note: t/alpha/first", "note: t/alpha/gone")
        self.assertPrivateError("pt-count-widgets: unknown note 't/alpha/gone'")

    def test_public_problem_with_type(self):
        self.edit("notes/t/alpha/first/exercise.md", 'source="demo-1.1-q2"', 'source="demo-1.1-q2" type="pt-count-widgets"')
        self.assertPrivateError("problem types are private")

    def test_course_field_must_be_text(self):
        self.edit("private/meta/courses/tut.yml", "field: Tutoring", "field: [Tutoring]")
        self.assertPrivateError("field must be a non-empty text")


if __name__ == "__main__":
    if "--update" in sys.argv:
        update_expected()
    else:
        unittest.main(verbosity=2)
