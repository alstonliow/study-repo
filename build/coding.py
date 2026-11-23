"""Running coding exercises (meta/SPEC.md §6.4 items 8 and 10): a program followed by
its tests, in a fresh CPython process (Python) or compiled with the local C compiler
and run with each test in its own child process (C), with a time limit.

check.py uses run() on the solution (must pass) and on the starter (must fail).
The code comes from build/model.py (the only parser of notes); nothing here
reads notes. The browser runs the same steps in Pyodide: site/_assets/runnable.html
holds a twin of HARNESS, so a change to one is made in both.
"""

from __future__ import annotations

import ast
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
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


def run(code: str, tests: str, timeout: int = TIMEOUT, lang: str = "python") -> Result:
    """Run code + tests in the exercise's language."""
    return run_c(code, tests, timeout) if lang == "c" else run_python(code, tests, timeout)


def run_python(code: str, tests: str, timeout: int = TIMEOUT) -> Result:
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


# ---------------------------------------------------------------- C (SPEC §6.4 item 10)
# Headers a C exercise may include: the C11 standard library and a fixed POSIX list.
C_HEADERS = {
    "assert.h", "complex.h", "ctype.h", "errno.h", "fenv.h", "float.h", "inttypes.h",
    "iso646.h", "limits.h", "locale.h", "math.h", "setjmp.h", "signal.h", "stdalign.h",
    "stdarg.h", "stdbool.h", "stddef.h", "stdint.h", "stdio.h", "stdlib.h", "stdnoreturn.h",
    "string.h", "time.h", "wchar.h", "wctype.h",
    "unistd.h", "fcntl.h", "pthread.h", "sys/types.h", "sys/wait.h", "sys/stat.h", "sys/mman.h",
}
# Included before the code, so tests can assert without their own includes.
C_PRELUDE = "".join(f"#include <{h}>\n" for h in (
    "assert.h", "limits.h", "stdbool.h", "stddef.h", "stdint.h", "stdio.h", "stdlib.h", "string.h"))
C_FLAGS = ["-std=c11", "-D_POSIX_C_SOURCE=200809L", "-O1", "-Wall", "-Wno-unused-function", "-pthread"]
C_TEST = re.compile(r"^[ \t]*(?:static[ \t]+)?void[ \t]+(test_\w+)[ \t]*\([ \t]*(?:void)?[ \t]*\)", re.M)
C_INCLUDE = re.compile(r'^[ \t]*#[ \t]*include[ \t]*([<"])([^>"\n]+)[>"]', re.M)
C_PER_TEST = 5                     # seconds per test (alarm in the child)

# The test driver, appended after the tests: one child process per test, so a
# crash or failed assert fails that test only. Prints one line per test:
# name <TAB> 1|0 <TAB> message.
C_MAIN = r"""
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>
static void (*const study_tests__[])(void) = { %(funcs)s };
static const char *const study_names__[] = { %(names)s };
int main(void) {
    for (unsigned i = 0; i < sizeof study_names__ / sizeof *study_names__; i++) {
        fflush(NULL);
        pid_t pid = fork();
        if (pid == 0) {
            alarm(%(limit)d);
            freopen("/dev/null", "w", stderr);
            study_tests__[i]();
            fflush(NULL);
            _exit(0);
        }
        int st = 0;
        waitpid(pid, &st, 0);
        if (WIFEXITED(st) && WEXITSTATUS(st) == 0) printf("\n@@%%s\t1\t\n", study_names__[i]);
        else if (WIFSIGNALED(st) && WTERMSIG(st) == SIGABRT) printf("\n@@%%s\t0\tassertion failed\n", study_names__[i]);
        else if (WIFSIGNALED(st) && WTERMSIG(st) == SIGALRM) printf("\n@@%%s\t0\ttime limit exceeded\n", study_names__[i]);
        else if (WIFSIGNALED(st)) printf("\n@@%%s\t0\tsignal %%d\n", study_names__[i], WTERMSIG(st));
        else printf("\n@@%%s\t0\texit status %%d\n", study_names__[i], WEXITSTATUS(st));
    }
    return 0;
}
"""


def c_compiler() -> str | None:
    return shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")


def c_tests(tests: str) -> list[str]:
    """Names of the test_* functions the tests define, in order."""
    return C_TEST.findall(tests)


def c_disallowed(code: str) -> set[str]:
    """Included headers outside C_HEADERS (a quoted include is never allowed)."""
    return {(h if q == "<" else f'"{h}"') for q, h in C_INCLUDE.findall(code)
            if q != "<" or h.strip() not in C_HEADERS}


def run_c(code: str, tests: str, timeout: int = TIMEOUT) -> Result:
    """Compile prelude + code + tests + driver with the local compiler and run it."""
    cc = c_compiler()
    if not cc:
        return Result(error="no C compiler (cc, gcc or clang) found")
    names = c_tests(tests)
    if not names:
        return Result(error="the tests define no test_* function (void test_name(void))")
    src = (C_PRELUDE + '#line 1 "code.c"\n' + code + '\n#line 1 "tests.c"\n' + tests + "\n"
           + C_MAIN % {"funcs": ", ".join(names), "names": ", ".join(json.dumps(n) for n in names),
                       "limit": C_PER_TEST})
    with tempfile.TemporaryDirectory(prefix="study-c-") as tmp:
        prog = Path(tmp) / "prog"
        (Path(tmp) / "prog.c").write_text(src, encoding="utf-8")
        try:
            p = subprocess.run([cc, *C_FLAGS, "prog.c", "-o", "prog", "-lm"], cwd=tmp,
                               capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return Result(error=f"compile time limit of {timeout} s exceeded")
        if p.returncode != 0:
            errs = [l for l in p.stderr.splitlines() if "error" in l] or p.stderr.splitlines() or ["no output"]
            return Result(error=f"compile error: {errs[0].strip()}")
        try:
            p = subprocess.run([str(prog)], cwd=tmp, capture_output=True, text=True,
                               timeout=timeout, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return Result(error=f"time limit of {timeout} s exceeded")
    out = [l[2:].split("\t", 2) for l in p.stdout.splitlines() if l.startswith("@@")]
    if len(out) != len(names):
        return Result(error=f"crashed: the test driver stopped (exit status {p.returncode})")
    return Result(tests=[(n, ok == "1", m) for n, ok, m in out])
