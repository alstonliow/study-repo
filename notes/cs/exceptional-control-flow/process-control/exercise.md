::: {#prob-reap-children-code .problem .coding origin="adapted" source="res-cmu-15213-labs-shell-lab" tags="processes,fork,waitpid"}
Write `reap_sum(n)`: create $n\ge0$ child processes with `fork`, where child $i$ ($1\le i\le n$) immediately terminates with exit status $i$ (@def-fork). The parent reaps *every* child with `waitpid` (@def-waitpid), decodes the exit statuses with the status macros, and returns their sum. No zombies may be left behind.

Then write `run_and_classify(job)`: run the function `job` in a child process, which calls `exit(0)` if `job` returns; the parent waits for the child and returns its exit status if it terminated normally, or minus the number of the signal that terminated it.

```{.c .starter}
int reap_sum(int n) {
    return 0;
}

int run_and_classify(void (*job)(void)) {
    return 0;
}
```

```{.c .tests}
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>
#include <errno.h>

static void no_children_left(void) {
    errno = 0;
    assert(waitpid(-1, NULL, WNOHANG) == -1 && errno == ECHILD);
}

void test_reap_sum(void) {
    assert(reap_sum(0) == 0);
    assert(reap_sum(1) == 1);
    assert(reap_sum(5) == 15);
    assert(reap_sum(20) == 210);
    no_children_left();
}

static void job_ok(void) { }
static void job_exit3(void) { exit(3); }
static void job_kill(void) { raise(SIGKILL); }
static void job_abort(void) { abort(); }

void test_classify(void) {
    assert(run_and_classify(job_ok) == 0);
    assert(run_and_classify(job_exit3) == 3);
    assert(run_and_classify(job_kill) == -SIGKILL);
    assert(run_and_classify(job_abort) == -SIGABRT);
    no_children_left();
}
```
:::
