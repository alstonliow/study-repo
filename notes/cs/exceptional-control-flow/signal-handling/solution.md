::: {.solution for="prob-sigchld-reaper-code" status="draft"}
```{.c}
#include <errno.h>
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>

static volatile sig_atomic_t reaped;

static void chld_handler(int sig) {
    int olderrno = errno;
    (void) sig;
    while (waitpid(-1, NULL, WNOHANG) > 0)   /* reap every terminated child */
        reaped++;
    errno = olderrno;
}

int reap_with_handler(int n) {
    struct sigaction sa, old;
    sigset_t mask, prev;
    sa.sa_handler = chld_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART;
    sigaction(SIGCHLD, &sa, &old);

    sigemptyset(&mask);
    sigaddset(&mask, SIGCHLD);
    sigprocmask(SIG_BLOCK, &mask, &prev);    /* no handler runs until we wait */
    reaped = 0;
    for (int i = 0; i < n; i++)
        if (fork() == 0)
            _exit(0);
    while (reaped < n)
        sigsuspend(&prev);                   /* unblock SIGCHLD and sleep, atomically */
    sigprocmask(SIG_SETMASK, &prev, NULL);
    sigaction(SIGCHLD, &old, NULL);
    return reaped;
}
```

1. The handler reaps in a loop with `WNOHANG` until no terminated child is left. A single `SIGCHLD` may stand for many terminations, since signals of one type are not queued (@prp-signals-not-queued), so reaping one child per signal would leave some unreaped.
2. `waitpid` is async-signal-safe but may change `errno`, so the handler saves and restores it; the counter is a `volatile sig_atomic_t`, so the main loop rereads it from memory and every update is atomic.
3. `SIGCHLD` is blocked before the children are forked. Without that, every child could terminate, and the handler could run, between the test `reaped < n` and the moment the parent goes to sleep, and the parent would sleep forever.
4. `sigsuspend(&prev)` unblocks `SIGCHLD` and sleeps in one atomic step; when a handler has run it returns with `SIGCHLD` blocked again, and the loop tests the counter. When all $n$ children are reaped, the old mask and the old action are restored.
:::
