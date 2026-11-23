::: {.solution for="prob-reap-children-code" status="draft"}
```{.c}
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>

int reap_sum(int n) {
    int sum = 0, status;
    for (int i = 1; i <= n; i++)
        if (fork() == 0)
            _exit(i);                       /* child i: terminate at once */
    while (waitpid(-1, &status, 0) > 0)     /* parent: reap until none is left */
        if (WIFEXITED(status))
            sum += WEXITSTATUS(status);
    return sum;
}

int run_and_classify(void (*job)(void)) {
    int status;
    pid_t pid = fork();
    if (pid == 0) {
        job();
        exit(0);
    }
    if (waitpid(pid, &status, 0) < 0)
        return -1000;                       /* should not happen */
    if (WIFEXITED(status))
        return WEXITSTATUS(status);
    return -WTERMSIG(status);
}
```

1. `fork` returns $0$ in the child, which terminates at once with status $i$. `_exit` is used rather than `exit` so that the child does not flush a copy of the parent's `stdio` buffers a second time.
2. The parent does not know in which order the children terminate, so it calls `waitpid(-1, …)` until it returns $-1$ (with `errno` $=$ `ECHILD`): then every child has been reaped and no zombie remains (@def-reaping).
3. `WIFEXITED` and `WEXITSTATUS` extract the status passed to `_exit`; only its low 8 bits survive, which is enough for $i\le255$.
4. In `run_and_classify`, the parent waits for that specific child. A child killed by a signal (by `raise(SIGKILL)`, or `abort`, which raises `SIGABRT`) has `WIFSIGNALED` true and `WTERMSIG` gives the signal number.
:::
