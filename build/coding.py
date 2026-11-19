"""Running coding exercises (meta/SPEC.md §6.4 item 8): a program followed by its
tests, in a fresh CPython process with a time limit.

check.py uses run() on the solution (must pass) and on the starter (must fail).
The code comes from build/model.py (the only parser of notes); nothing here
reads notes. The browser runs the same steps in Pyodide: site/_assets/runnable.html
holds a twin of HARNESS, so a change to one is made in both.
"""

from __future__ import annotations

import ast
import json
import subprocess
import sys
from dataclasses import dataclass, field

TIMEOUT = 10                       # seconds per run
ALLOWED_PACKAGES = {"numpy"}       # beyond the standard library (Pyodide has it too)

# Runs `code`, then `tests`, in one namespace. Top-level statements of the tests
# count as one test, "(top level)"; then every test_* function the tests define is
# called in order. Prints one JSON list of [name, passed, message].
HARNESS = r'''
import json, sys
src = json.load(sys.stdin)
ns = {"__name__": "__exercise__"}
out = []
def fail(e):
    return f"{type(e).__name__}: {e}" if str(e) else type(e).__name__
try:
    exec(compile(src["code"], "<code>", "exec"), ns)
except BaseException as e:
    out.append(["(your code)", False, fail(e)])
else:
    before = set(ns)
    try:
        exec(compile(src["tests"], "<tests>", "exec"), ns)
        top = None
    except BaseException as e:
        top = fail(e)
    tests = [v for k, v in ns.items() if k.startswith("test_") and callable(v)
             and getattr(getattr(v, "__code__", None), "co_filename", "") == "<tests>"]
    if top is not None or not tests:
        out.append(["(top level)", top is None, top or ""])
    for t in tests:
        try:
            t()
            out.append([t.__name__, True, ""])
        except BaseException as e:
            out.append([t.__name__, False, fail(e)])
print(json.dumps(out))
'''


@dataclass
class Result:
    tests: list[tuple[str, bool, str]] = field(default_factory=list)
    error: str = ""                # the run itself failed (timeout, crash)

    @property
    def passed(self) -> bool:
        return not self.error and bool(self.tests) and all(ok for _, ok, _ in self.tests)

    def summary(self) -> str:
        if self.error:
            return self.error
        bad = [f"{n} ({m})" if m else n for n, ok, m in self.tests if not ok]
        return "failed: " + "; ".join(bad) if bad else "all tests pass"


def run(code: str, tests: str, timeout: int = TIMEOUT) -> Result:
    """Run code + tests in a fresh, isolated CPython process (-I: no site
    packages from the user, no current directory on the path)."""
    try:
        p = subprocess.run([sys.executable, "-I", "-c", HARNESS], input=json.dumps({"code": code, "tests": tests}),
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return Result(error=f"time limit of {timeout} s exceeded")
    lines = p.stdout.strip().splitlines()
    try:
        return Result(tests=[(str(n), bool(ok), str(m)) for n, ok, m in json.loads(lines[-1])])
    except (IndexError, ValueError):
        return Result(error=f"crashed: {(p.stderr.strip().splitlines() or ['no output'])[-1]}")


def imports(code: str) -> set[str]:
    """Top-level module names imported by code (raises SyntaxError)."""
    names: set[str] = set()
    for node in ast.walk(ast.parse(code)):
        if isinstance(node, ast.Import):
            names |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            names.add(node.module.split(".")[0])
    return names


def disallowed(code: str, packages: list[str]) -> set[str]:
    """Imported modules that are neither standard library nor a declared, allowed package."""
    return {m for m in imports(code) if m not in sys.stdlib_module_names
            and not (m in ALLOWED_PACKAGES and m in packages)}
