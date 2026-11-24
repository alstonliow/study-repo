---
title: "Semaphores and Mutual Exclusion"
sources: [cmu15213-24]
requires: [cs/concurrency/threads]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 24 "Synchronization: Basics" (an improperly synchronised counter, progress graphs, critical sections, semaphores, mutual exclusion), in our own wording; proofs written out in steps; the interleaving example is our own. -->

Shared variables are convenient, but threads that update them concurrently can produce wrong results that appear only under some schedules. This note shows why, gives a geometric way to reason about it, and introduces the classic tool that prevents it.

::: {#exm-bad-counter .example name="An improperly synchronised counter"}

```c
volatile long cnt = 0;                 /* global, shared */

void *count(void *vargp) {
    long n = *(long *)vargp;
    for (long i = 0; i < n; i++)
        cnt++;
    return NULL;
}
```

Two threads run `count` with $n=10^6$ each and the main thread then prints `cnt`. The result should be $2\,000\,000$, but runs print values such as $1\,083\,642$ or $1\,301\,958$, different each time. On one core the error appears rarely; on several cores almost always.

:::

::: {#def-counter-loop-steps .definition name="The five parts of the counter loop"}

The loop body compiles to code that, for the purpose of the analysis, consists of five parts:

- $H_i$, the *head*: loop test and increment of the local `i`;
- $L_i$: *load* `cnt` into a register (`movq cnt(%rip), %rdx`);
- $U_i$: *update* the register (`addq $1, %rdx`);
- $S_i$: *store* the register back to `cnt` (`movq %rdx, cnt(%rip)`);
- $T_i$, the *tail*: jump back to the head.

$H_i$ and $T_i$ touch only thread $i$'s registers and stack; $L_i$, $U_i$, $S_i$ manipulate the shared variable.

:::

::: {#exm-lost-update .example name="A lost update"}

Starting from `cnt` $=0$, each thread does one iteration, in the order below; `%rdx`$_i$ is thread $i$'s copy of the register.

| step | thread | instruction | `%rdx`$_1$ | `%rdx`$_2$ | `cnt` |
|---|---|---|---|---|---|
| 1 | 1 | $H_1$ | -- | -- | 0 |
| 2 | 1 | $L_1$ | 0 | -- | 0 |
| 3 | 1 | $U_1$ | 1 | -- | 0 |
| 4 | 2 | $H_2$ | 1 | -- | 0 |
| 5 | 2 | $L_2$ | 1 | 0 | 0 |
| 6 | 1 | $S_1$ | 1 | 0 | 1 |
| 7 | 1 | $T_1$ | 1 | 0 | 1 |
| 8 | 2 | $U_2$ | 1 | 1 | 1 |
| 9 | 2 | $S_2$ | 1 | 1 | 1 |
| 10 | 2 | $T_2$ | 1 | 1 | 1 |

Thread 2 loaded `cnt` before thread 1 stored its result, so thread 2 overwrites it with the same value: two increments, `cnt` $=1$. Any order in which one thread's $L$ falls between the other's $L$ and $S$ loses an update.

:::

::: {#def-progress-graph .definition name="Progress graph"}

For $n$ threads, a *progress graph* models their concurrent execution as a path in $n$-dimensional space. Axis $k$ is the sequence of instructions of thread $k$; a point $(I_1,\dots,I_n)$ is the state in which each thread $k$ has completed instruction $I_k$. An execution is a *trajectory*: a monotone path that moves one step along one axis at a time, since one instruction completes at a time. For a shared variable, the instructions $L$, $U$, $S$ of a thread form its *critical section*; the set of states in which two threads are both inside their critical sections is the *unsafe region*. A trajectory is *safe* if it avoids the unsafe region.

:::

::: {#fig-semaphores-and-mutual-exclusion-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.85]
\path[tintD] (1,1) rectangle (4,4); \node[tick] at (2.5,2.5) {unsafe region};
\foreach \i in {0,...,5} { \draw[gridline] (\i,0) -- (\i,5); \draw[gridline] (0,\i) -- (5,\i); }
\draw[->] (0,0) -- (5.6,0) node[lab, right] {thread 1};
\draw[->] (0,0) -- (0,5.6) node[lab, above] {thread 2};
\foreach \i/\n in {0/H,1/L,2/U,3/S,4/T} { \node[tick] at (\i+0.5,-0.3) {$\n_1$}; \node[tick] at (-0.35,\i+0.5) {$\n_2$}; }
\draw[decorate, decoration={brace, mirror}] (1,-0.6) -- (4,-0.6) node[midway, below=2pt, tick] {critical section of thread 1};
\draw[emph, draw=primary, ->] (0,0) -- (1,0) -- (4,0) -- (4,1) -- (5,1) -- (5,5);
\node[tick, text=primary, anchor=west] at (5.1,0.9) {safe};
\draw[emph, draw=accent, ->] (0,0) -- (0,1) -- (2,1) -- (2,2) -- (3,2) -- (3,5) -- (5,5);
\node[tick, text=accent, anchor=east] at (1.9,1.25) {unsafe};
\node[dot] at (5,5) {}; \node[tick, anchor=west] at (5.1,5.1) {both done};
\end{tikzpicture}
\end{center}
```

The progress graph of one iteration of the counter loop in two threads. The safe trajectory runs thread 1's critical section before thread 2's; the unsafe one enters the region where both are between their load and their store

:::

::: {#prp-safe-trajectory .proposition name="Safe trajectories give the right result"}

For the counter loop, an execution increments `cnt` correctly, by the total number of iterations, if and only if its trajectory never enters an unsafe region.

:::

::: {.proof}
1. Outside the critical sections a thread does not touch `cnt` or its register copy of it, so only the order of the $L$, $U$, $S$ steps matters.

2. If the trajectory avoids the unsafe region, whenever one thread is inside its critical section the other is not; so the two critical sections of each pair of iterations run one after the other, and each load reads the value stored by the previous store. Every iteration adds $1$.

3. If the trajectory enters the unsafe region, there is a state where both threads have executed their $L$ and neither its $S$ (the region's interior consists exactly of such states, up to the instruction of the boundary each has completed). Both loaded the same value $v$, and both store $v+1$: one increment is lost, as in @exm-lost-update.
:::

::: {#def-semaphore .definition name="Semaphore"}

A *semaphore* $s$ is a global variable with a nonnegative integer value, changed only by two operations, both executed *atomically* (indivisibly):

- $P(s)$: if $s>0$, decrement $s$ and return at once; if $s=0$, suspend the thread until $s$ becomes nonzero and another thread restarts it by a $V$, then decrement $s$ and return;
- $V(s)$: increment $s$; if some threads are blocked in $P$ waiting for $s$ to become nonzero, restart exactly one of them (which one is not specified).

These operations guarantee the *semaphore invariant*: a running program can never reach a state in which a properly initialised semaphore is negative. In POSIX, `sem_init`, `sem_wait` ($P$) and `sem_post` ($V$) implement them.

:::

::: {#def-mutex .definition name="Mutex"}

A semaphore whose value is always $0$ or $1$ is a *binary semaphore*. One used to protect shared variables is a *mutex* (for mutual exclusion): it is initialised to $1$, and each critical section is surrounded by $P(\textit{mutex})$, called *locking* the mutex, and $V(\textit{mutex})$, *unlocking* it. A thread that has locked a mutex and not yet unlocked it *holds* it. A semaphore used as a counter for a set of available resources is a *counting semaphore*. Pthreads also offers a dedicated mutex type, `pthread_mutex_t`, with `pthread_mutex_lock` and `pthread_mutex_unlock`.

:::

::: {#exm-good-counter .example name="The counter made correct"}

```c
volatile long cnt = 0;
sem_t mutex;                           /* sem_init(&mutex, 0, 1) in main */

void *count(void *vargp) {
    long n = *(long *)vargp;
    for (long i = 0; i < n; i++) {
        P(&mutex);                     /* sem_wait */
        cnt++;
        V(&mutex);                     /* sem_post */
    }
    return NULL;
}
```

Now every run prints $2\,000\,000$. The price is speed: each iteration performs two semaphore operations, which costs far more than the increment itself, and the threads now take turns; @sec-cs-concurrency-thread-level-parallelism shows how to avoid sharing in the inner loop.

:::

::: {#thm-mutex-forbidden-region .theorem name="A mutex forbids the unsafe region"}

If every thread surrounds its critical section for a shared variable with $P(\textit{mutex})$ and $V(\textit{mutex})$, where *mutex* is initialised to $1$, then no trajectory can enter the unsafe region: at most one thread is inside a critical section at any time.

:::

::: {.proof}
1. Let $h$ be the number of threads inside the region between their $P$ and $V$. Initially $h=0$ and $\textit{mutex}=1$.

2. Invariant: $\textit{mutex}+h=1$. A completed $P$ decrements *mutex* and increases $h$ by one; a $V$ increments *mutex* and decreases $h$ by one; other instructions change neither. So the sum stays $1$.

3. By the semaphore invariant, $\textit{mutex}\ge0$, so $h\le1$: two threads can never be inside their critical sections at once.

4. The states with $h=2$ form the *forbidden region*, where *mutex* would be $-1$. It contains the unsafe region, so every feasible trajectory is safe, and by @prp-safe-trajectory the counter is correct.
:::

::: {#fig-semaphores-and-mutual-exclusion-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.75]
\path[tintC] (1,1) rectangle (6,6);
\path[tintD] (2,2) rectangle (5,5); \node[tick] at (3.5,3.5) {unsafe};
\node[tick] at (3.5,5.5) {forbidden region};
\foreach \i in {0,...,7} { \draw[gridline] (\i,0) -- (\i,7); \draw[gridline] (0,\i) -- (7,\i); }
\draw[->] (0,0) -- (7.6,0) node[lab, right] {thread 1};
\draw[->] (0,0) -- (0,7.6) node[lab, above] {thread 2};
\foreach \i/\n in {0/H,1/P,2/L,3/U,4/S,5/V,6/T} { \node[tick] at (\i+0.5,-0.3) {$\n_1$}; \node[tick] at (-0.4,\i+0.5) {$\n_2$}; }
\draw[emph, draw=primary, ->] (0,0) -- (6,0) -- (6,1) -- (7,1) -- (7,7);
\draw[emph, draw=accent, ->] (0,0) -- (0,6) -- (1,6) -- (7,6) -- (7,7);
\node[tick, anchor=west] at (7.1,3.5) {every trajectory goes around};
\end{tikzpicture}
\end{center}
```

With $P$ and $V$ around the critical sections, the states where both threads would hold the mutex form a forbidden region that encloses the unsafe region

:::

::: {#fig-semaphores-and-mutual-exclusion-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm]
\node[lab, anchor=east] at (-0.2,1) {thread 1};
\node[lab, anchor=east] at (-0.2,0) {thread 2};
\node[lab, anchor=east] at (-0.2,-1) {\textit{mutex}};
\draw[faint] (0,1) -- (12,1); \draw[faint] (0,0) -- (12,0);
\draw[emph, draw=primary] (1,1) -- (5,1); \node[tick] at (1,1.3) {$P$}; \node[tick] at (5,1.3) {$V$};
\draw[emph, draw=accent] (5,0) -- (9,0); \node[tick] at (5,0.3) {$P$ returns}; \node[tick] at (9,0.3) {$V$};
\node[dot] at (2.5,0) {}; \node[tick] at (2.5,-0.3) {$P$: blocks};
\draw[dashed] (2.5,0) -- (5,0);
\draw[hl] (0,-0.75) -- (1,-0.75) -- (1,-1.25) -- (9,-1.25) -- (9,-0.75) -- (12,-0.75);
\node[tick] at (0.5,-0.55) {1}; \node[tick] at (3,-1.5) {0}; \node[tick] at (10.5,-0.55) {1};
\end{tikzpicture}
\end{center}
```

A mutex over time: thread 2's $P$ blocks while thread 1 holds the mutex; thread 1's $V$ wakes it, and the value goes straight from thread 1 to thread 2 without becoming $1$

:::

::: {#rmk-semaphores-and-mutual-exclusion-1 name="`volatile` is not synchronisation"}

`volatile` only forces the compiler to load and store `cnt` in memory on every iteration, instead of keeping it in a register for the whole loop. That is needed for the analysis above to apply, but it makes no increment atomic; mutual exclusion still requires a lock or an atomic instruction. On macOS the unnamed POSIX semaphores (`sem_init`) are not supported; a `pthread_mutex_t`, or a semaphore built from a mutex and a condition variable, serves instead.

:::
