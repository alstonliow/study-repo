::: {#prob-sigchld-reaper-code .problem .coding origin="adapted" source="res-cmu-15213-labs-shell-lab" tags="signals,sigchld,sigsuspend"}
Write `reap_with_handler(n)`, which installs a `SIGCHLD` handler, forks $n\ge1$ children that each terminate at once, and waits until the handler has reaped all of them; it returns the number of children the handler reaped (which must be $n$) and leaves no zombies. Follow the rules of this note: the handler must cope with lost signals (@exm-sigchld-reaping-bug), save and restore `errno`, and share its counter through a `volatile sig_atomic_t`; the main program must wait with `sigsuspend` (@def-sigsuspend), never with a busy loop or `pause` alone. Restore the default action for `SIGCHLD` before returning.

```{.c .starter}
int reap_with_handler(int n) {
    return 0;
}
```

```{.c .tests}
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>
#include <errno.h>

void test_one_child(void) { assert(reap_with_handler(1) == 1); }

void test_many_children(void) {
    assert(reap_with_handler(10) == 10);
    assert(reap_with_handler(60) == 60);
}

void test_no_zombies(void) {
    reap_with_handler(30);
    errno = 0;
    assert(waitpid(-1, NULL, WNOHANG) == -1 && errno == ECHILD);
}
```
:::
