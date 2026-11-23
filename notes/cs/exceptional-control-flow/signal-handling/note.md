---
title: "Writing Safe Signal Handlers"
sources: [cmu15213-15, cmu15213lab-5]
requires: [cs/exceptional-control-flow/signals]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 15 "Exceptional Control Flow: Signals and Nonlocal Jumps" and the Shell Lab handout, in our own wording. -->

A handler runs concurrently with the main program and with other handlers, and it may interrupt the main program in the middle of anything. Handlers are therefore among the hardest code to get right. This note collects the rules.

::: {#def-async-signal-safe .definition name="Async-signal-safe function"}

A function is *async-signal-safe* if it can be called from a handler without corrupting the interrupted program: either it is *reentrant* (it touches only local data, @def-reentrant-function) or it cannot be interrupted by a signal. POSIX lists the safe functions; they include `_exit`, `write`, `wait`, `waitpid`, `sleep` and `kill`. `printf`, `sprintf`, `malloc` and `exit` are *not* safe: they use global state (a buffer, the heap) that the interrupted code may be in the middle of changing.

:::

::: {#def-signal-handler-guidelines .definition name="Guidelines for handlers"}

1. Keep handlers as simple as possible, for example: set a global flag and return.
2. Call only async-signal-safe functions in a handler.
3. Save `errno` on entry and restore it on exit, since safe functions such as `waitpid` may change it.
4. Protect accesses to data shared with the main program by blocking all signals around them.
5. Declare shared globals `volatile`, so the compiler reloads them from memory each time instead of caching them in a register.
6. Declare flags `volatile sig_atomic_t`, a type whose reads and writes are single, uninterruptible operations.

:::

::: {#exm-sigchld-reaping-bug .example name="Counting children with a SIGCHLD handler"}

A parent forks five children that exit at once, and its handler reaps one child per `SIGCHLD`:

```c
void child_handler(int sig) {          /* wrong */
    int olderrno = errno;
    if (wait(NULL) > 0) ccount--;
    errno = olderrno;
}
```

The program may hang with `ccount` stuck above $0$: while the handler runs, further `SIGCHLD` signals arrive, but at most one stays pending (@prp-signals-not-queued), so some terminations never cause a handler call. The fix is to reap *all* terminated children each time, `while (wait(NULL) > 0) ccount--;`, because a signal only means "at least one event happened".

:::

::: {#fig-signal-handling-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm]
\draw[->] (0,0) -- (8,0) node[lab, right] {time}; \node[tick, anchor=east] at (0.9,0.95) {child exits:};
\foreach \x/\l in {1/1,1.6/2,2.2/3,2.8/4,3.4/5} { \node[hl dot] at (\x,0.6) {}; \node[tick] at (\x,0.95) {\l}; }
\draw[emph, draw=primary] (1.1,-0.4) -- (2.0,-0.4); \node[tick] at (1.55,-0.75) {run 1};
\draw[emph, draw=primary] (2.1,-0.4) -- (3.0,-0.4); \node[tick] at (2.55,-0.75) {run 2};
\node[tick, align=left, anchor=west] at (4,-0.9) {signals 3--5 arrive while bit 17 is already\\pending: only two handler runs, three children\\left unreaped by the wrong handler};
\end{tikzpicture}
\end{center}
```

Five `SIGCHLD` signals but only two handler runs: a signal that arrives while one of its type is pending is lost

:::

::: {#def-sigprocmask .definition name="Blocking signals explicitly"}

`sigprocmask(how, &set, &oldset)` changes the blocked set: `SIG_BLOCK` adds the signals in `set`, `SIG_UNBLOCK` removes them, `SIG_SETMASK` replaces the blocked set by `set`; the previous blocked set is stored in `oldset`. Sets are built with `sigemptyset`, `sigfillset`, `sigaddset` and `sigdelset`. The kernel also blocks a signal's own type while its handler runs.

:::

::: {#exm-fork-race .example name="A race between the parent and its child"}

A shell adds each new child to a job list after `fork`, and its `SIGCHLD` handler deletes reaped children from the list. If the child exits before the parent runs `addjob`, the handler may run first and try to delete a job that is not there yet; then `addjob` adds a job that never disappears. The fix blocks `SIGCHLD` before `fork`, adds the job, and only then unblocks it:

```c
sigprocmask(SIG_BLOCK, &mask_chld, &prev);   /* block SIGCHLD */
if ((pid = fork()) == 0) {
    sigprocmask(SIG_SETMASK, &prev, NULL);   /* child: unblock */
    execve(argv[0], argv, environ);
}
addjob(pid);                                 /* handler cannot run yet */
sigprocmask(SIG_SETMASK, &prev, NULL);       /* now it may */
```

The child inherits the blocked set, so it must unblock before `execve`.

:::

::: {#def-sigsuspend .definition name="Waiting for a signal: `sigsuspend`"}

`sigsuspend(&mask)` atomically replaces the blocked set by `mask` and suspends the process until a signal is received; after the handler returns, it restores the previous blocked set and returns. It is equivalent to `sigprocmask(SIG_SETMASK, &mask, &prev); pause(); sigprocmask(SIG_SETMASK, &prev, NULL);` without the gap between the first two calls, in which a signal could arrive and leave `pause` waiting forever.

:::

::: {#exm-wait-for-foreground .example name="Waiting for a foreground job"}

```c
sigprocmask(SIG_BLOCK, &mask_chld, &prev);
/* ... fork the child, record fg_pid = 0 ... */
while (!fg_pid)               /* the SIGCHLD handler sets fg_pid */
    sigsuspend(&prev);        /* wait with SIGCHLD unblocked */
sigprocmask(SIG_SETMASK, &prev, NULL);
```

A busy loop `while (!fg_pid) ;` wastes the processor; `while (!fg_pid) pause();` can miss the signal if it arrives between the test and `pause`; `sleep(1)` in the loop is slow. `sigsuspend` is correct and efficient.

:::

::: {#def-nonlocal-jump .definition name="Nonlocal jumps"}

`setjmp(env)` saves the current calling environment (the stack pointer, the program counter and callee-saved registers) in `env` and returns $0$. A later `longjmp(env, v)` restores that environment, so the earlier `setjmp` *returns again*, this time with value $v\ne0$. This jumps out of any number of nested calls at once, for example to handle an error found deep in a computation. The function that called `setjmp` must not have returned before the `longjmp`. In handlers, `sigsetjmp`/`siglongjmp` also restore the blocked set; they let a Ctrl-C handler restart a program at its prompt.

:::

::: {#fig-signal-handling-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \f/\y in {main/2.4,foo/1.6,bar/0.8,bletch/0.0} { \draw[cell frame] (0,\y) rectangle (2.2,\y+0.6); \node[lab] at (1.1,\y+0.3) {\texttt{\f}}; }
\draw[hl cell] (0,2.4) rectangle (2.2,3.0); \node[lab] at (1.1,2.7) {\texttt{main}: \texttt{setjmp}};
\draw[->, draw=accent, emph] (2.3,0.3) to[out=0,in=0, looseness=1.2] node[edge label, midway] {\texttt{longjmp(buf, 1)}} (2.3,2.7);
\node[tick, anchor=east] at (-0.1,0.3) {error found here};
\end{tikzpicture}
\end{center}
```

`longjmp` returns directly to the `setjmp` in `main`, discarding the frames of `foo`, `bar` and `bletch`

:::
