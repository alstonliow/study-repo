---
title: "Process Control: fork, wait and execve"
sources: [cmu15213-14, cmu15213-15, cmu15213lab-5]
requires: [cs/exceptional-control-flow/processes]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 14 "Exceptional Control Flow: Exceptions and Processes", the shell part of Lecture 15 and the Shell Lab handout, in our own wording; proofs written out in steps. -->

::: {#def-fork .definition name="`fork`"}

`pid_t fork(void)` creates a new *child* process that is an almost exact copy of the calling *parent*: an identical but separate copy of the parent's address space (code, data, heap, stack, @def-copy-on-write) and of its open file descriptors. `fork` is called once but *returns twice*: in the child it returns $0$, in the parent it returns the child's process ID (PID). Parent and child then run concurrently, and their order is up to the scheduler.

:::

::: {#exm-fork-basic .example name="A first fork"}

```c
int main(void) {
    int x = 1;
    pid_t pid = fork();
    if (pid == 0) {                       /* child */
        printf("child : x=%d\n", ++x);
        exit(0);
    }
    printf("parent: x=%d\n", --x);        /* parent */
    exit(0);
}
```

prints `child : x=2` and `parent: x=0`, in either order. Each process changes its own copy of `x`; neither sees the other's update.

:::

::: {#def-process-graph .definition name="Process graph"}

The *process graph* of a program run is a directed graph whose vertices are the executions of statements, with an edge $a\to b$ if $a$ happens before $b$ in the same process, and an edge from each `fork` to the first statement of the child. Every possible order of the outputs is a *topological sort* of the graph (@thm-topological-sort), and every topological sort can occur.

:::

::: {#exm-fork-twice .example name="Two forks in a row"}

```c
printf("L0\n");
fork();
printf("L1\n");
fork();
printf("Bye\n");
```

prints `L0` once, `L1` twice and `Bye` four times: after the second `fork` there are four processes. `L0 L1 Bye Bye L1 Bye Bye` is a possible output; `L0 Bye L1 Bye L1 Bye Bye` is not, because the first `Bye` must follow an `L1` in the same process.

:::

::: {#fig-process-control-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.6cm, y=0.8cm]
\node[small vertex] (s) at (0,0) {}; \node[tick, above] at (0,0.2) {\texttt{L0}};
\node[small vertex, fill=accentLight, draw=accent] (f1) at (1,0) {};
\node[small vertex] (a) at (2,0) {}; \node[tick, above] at (2,0.2) {\texttt{L1}};
\node[small vertex, fill=accentLight, draw=accent] (f2) at (3,0) {};
\node[small vertex] (b) at (4,0) {}; \node[tick, above] at (4,0.2) {\texttt{Bye}};
\node[small vertex] (c) at (4,-1) {}; \node[tick, above] at (4,-0.8) {\texttt{Bye}};
\node[small vertex] (a2) at (2,-2) {}; \node[tick, above] at (2,-1.8) {\texttt{L1}};
\node[small vertex, fill=accentLight, draw=accent] (f3) at (3,-2) {};
\node[small vertex] (d) at (4,-2) {}; \node[tick, above] at (4,-1.8) {\texttt{Bye}};
\node[small vertex] (e) at (4,-3) {}; \node[tick, above] at (4,-2.8) {\texttt{Bye}};
\draw[->] (s) -- (f1); \draw[->] (f1) -- (a); \draw[->] (a) -- (f2); \draw[->] (f2) -- (b);
\draw[->] (f2) |- (c); \draw[->] (f1) |- (a2); \draw[->] (a2) -- (f3); \draw[->] (f3) -- (d); \draw[->] (f3) |- (e);
\node[tick] at (1,-0.45) {\texttt{fork}}; \node[tick] at (3,0.45) {\texttt{fork}}; \node[tick] at (3,-2.45) {\texttt{fork}};
\end{tikzpicture}
\end{center}
```

Process graph of @exm-fork-twice. Each fork (terracotta) starts a new horizontal line for the child; any topological sort of the vertices is a possible output

:::

::: {#def-reaping .definition name="Termination, zombies and reaping"}

A process terminates by returning from `main`, by calling `exit(status)`, or by receiving a signal whose default action is to terminate it. A terminated process is not removed at once: it stays a *zombie*, holding its exit status, until its parent *reaps* it with `wait` or `waitpid`. If a parent terminates first, its children are adopted by the `init` process (PID 1), which reaps them. A long-running parent such as a shell or server must reap its children, or zombies accumulate.

:::

::: {#def-waitpid .definition name="`waitpid`"}

`pid_t waitpid(pid_t pid, int *status, int options)` waits for a child to change state and returns its PID. `pid > 0` waits for that child, `pid == -1` for any child. With `options = 0` it blocks until a child terminates and reaps it; `WNOHANG` returns $0$ at once if no child has terminated; `WUNTRACED` also reports stopped children. If `status` is not `NULL`, the macros `WIFEXITED(status)`, `WEXITSTATUS(status)`, `WIFSIGNALED(status)`, `WTERMSIG(status)` and `WIFSTOPPED(status)` decode why the child changed state. With no children left, it returns $-1$ with `errno == ECHILD`. `wait(&status)` is `waitpid(-1, &status, 0)`.

:::

::: {#def-execve .definition name="`execve`"}

`int execve(const char *filename, char *const argv[], char *const envp[])` loads and runs the executable `filename` *in the current process*, replacing its code, data, heap and stack (@def-loading). The process keeps its PID and its open files. `argv` and `envp` are `NULL`-terminated arrays of strings, the arguments (by convention `argv[0]` is the program name) and the environment `"NAME=value"`. `execve` returns only if an error occurs: it is called once and, on success, never returns.

:::

::: {#fig-process-control-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.5cm]
\foreach \s [count=\i from 0] in {{null-terminated environment strings},{null-terminated argument strings},{\dots},{envp[n] = NULL},{envp[0]},{argv[argc] = NULL},{argv[0]},{\dots},{stack frame of \texttt{libc\_start\_main}},{future stack frame of \texttt{main}}} {
  \draw[cell frame] (0,-\i) rectangle (5,-\i-0.9); \node[tick] at (2.5,-\i-0.45) {\s};
}
\draw[hl cell] (0,-4) rectangle (5,-4.9); \node[tick] at (2.5,-4.45) {\texttt{envp[0]}};
\draw[hl cell] (0,-6) rectangle (5,-6.9); \node[tick] at (2.5,-6.45) {\texttt{argv[0]}};
\node[tick, anchor=west] at (5.2,-4.45) {\texttt{environ}, \texttt{envp}};
\node[tick, anchor=west] at (5.2,-6.45) {\texttt{argv}};
\node[tick, anchor=west] at (5.2,-0.45) {bottom of stack (high addresses)};
\node[tick, anchor=west] at (5.2,-9.45) {top of stack};
\end{tikzpicture}
\end{center}
```

The new stack after `execve`: the strings, the arrays of pointers to them, and then the first frames. `main(argc, argv, envp)` receives pointers to the arrays

:::

::: {#exm-tiny-shell .example name="The core of a shell"}

A shell repeats: read a command line, parse it into `argv`, and if it is not a built-in command, `fork` a child that calls `execve(argv[0], argv, environ)`. For a *foreground* job the parent then waits with `waitpid` for that child; for a *background* job (line ending in `&`) it continues at once, and must reap the child later, which needs the signals of @def-signal: the kernel sends `SIGCHLD` to the parent when a child terminates.

:::

::: {#prp-fork-count .proposition name="Counting processes"}

A program that calls `fork()` $n$ times in sequence (no `if`s, no exits in between) creates $2^n$ processes in total, including the original.

:::

::: {.proof}
1. Induction on $n$. With $n=0$ there is one process.

2. Before the $(n+1)$-st `fork`, by induction $2^n$ processes are running the same code. Each of them executes the `fork` once and so becomes two processes.

3. Hence $2\cdot2^n=2^{n+1}$ processes continue after it.
:::
