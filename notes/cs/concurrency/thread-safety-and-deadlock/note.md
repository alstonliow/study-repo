---
title: "Thread Safety, Races and Deadlock"
sources: [cmu15213-25]
requires: [cs/concurrency/semaphores-and-mutual-exclusion]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 25 "Synchronization: Advanced" (thread safety and its four classes, reentrant functions, races, deadlock in progress graphs), in our own wording; proofs written out in steps; the code is our own. -->

A function used by several threads must give correct results when the threads call it concurrently. This note classifies the ways functions fail to, and two further synchronisation errors: races and deadlock.

::: {#def-thread-safe .definition name="Thread-safe function"}

A function is *thread-safe* if it always produces correct results when called repeatedly from multiple concurrent threads. Thread-unsafe functions fall into four (overlapping) classes:

1. functions that do not protect shared variables, such as an unsynchronised counter (@exm-bad-counter); fix: protect the variables with a mutex, at the cost of slower calls;
2. functions that keep state across invocations, such as a pseudo-random number generator whose next result depends on a static seed; fix: rewrite the function so the caller passes the state in;
3. functions that return a pointer to a static variable, such as `ctime` or `gethostbyname`, whose result a second thread may overwrite before the first has used it; fixes: rewrite the function so the caller passes the memory for the result, or *lock-and-copy*: wrap the unsafe function in a function that locks a mutex, calls it, copies the result to private memory, and unlocks;
4. functions that call thread-unsafe functions, unless they make the call safe (for example by locking around it).

:::

::: {#exm-rand-unsafe .example name="A random number generator, unsafe and safe"}

```c
static unsigned int next = 1;                 /* state across calls: class 2 */

int my_rand(void) {
    next = next * 1103515245 + 12345;
    return (unsigned int)(next / 65536) % 32768;
}

int my_rand_r(unsigned int *state) {          /* caller keeps the state */
    *state = *state * 1103515245 + 12345;
    return (unsigned int)(*state / 65536) % 32768;
}
```

With `my_rand`, the sequence one thread sees depends on how the other threads' calls interleave with its own, and concurrent updates of `next` can be lost. With `my_rand_r`, each thread passes its own state variable and always gets the same sequence for the same seed, whatever the other threads do.

:::

::: {#def-reentrant-function .definition name="Reentrant function"}

A function is *reentrant* if it accesses no shared variables when it is called by multiple threads. Reentrant functions are a proper subclass of thread-safe functions: they need no synchronisation at all. A function is *explicitly reentrant* if all its arguments are passed by value and all the data it uses is in local automatic variables; it is *implicitly reentrant* if some arguments are pointers, and it is reentrant only when the callers pass pointers to non-shared data, as with `my_rand_r` in @exm-rand-unsafe. Reentrancy also makes a function safe to call from a signal handler (@def-async-signal-safe).

:::

::: {#fig-thread-safety-and-deadlock-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0) rectangle (9,4.0); \node[lab, anchor=north west] at (0.1,3.95) {all functions};
\draw[regionC] (0.4,0.3) rectangle (5.6,3.2); \node[lab, anchor=north west] at (0.5,3.15) {thread-safe};
\draw[hl box] (0.8,0.6) rectangle (3.4,2.2); \node[lab] at (2.1,1.6) {reentrant}; \node[tick] at (2.1,1.1) {\texttt{my\_rand\_r}, \texttt{strlen}};
\node[tick] at (4.5,1.4) {locked counter};
\node[tick] at (4.5,1.0) {lock-and-copy};
\node[tick] at (7.3,2.4) {thread-unsafe:};
\node[tick] at (7.3,1.9) {\texttt{my\_rand}, \texttt{ctime},};
\node[tick] at (7.3,1.5) {\texttt{gethostbyname},};
\node[tick] at (7.3,1.1) {unlocked counter};
\end{tikzpicture}
\end{center}
```

Reentrant functions form a subset of the thread-safe functions, which form a subset of all functions

:::

::: {#rmk-thread-safety-and-deadlock-1 name="The C library"}

Most standard C functions, such as `malloc`, `free`, `printf` and `scanf`, are thread-safe (internally locked). The few exceptions have reentrant versions with the suffix `_r`: `rand_r`, `strtok_r`, `ctime_r`, `asctime_r`, `localtime_r`. The network functions `gethostbyname` and `gethostbyaddr` are obsolete and unsafe; `getaddrinfo` and `getnameinfo` (@def-getaddrinfo) are thread-safe.

:::

::: {#def-race .definition name="Race"}

A *race* occurs when the correctness of a program depends on one thread reaching a point $x$ in its control flow before another thread reaches a point $y$. Races arise when a programmer assumes that threads follow some particular trajectory through the execution state space, while the scheduler may choose any feasible trajectory.

:::

::: {#exm-race-loop-index .example name="Passing the loop index by address"}

```c
void *show(void *vargp) {
    int myid = *(int *)vargp;              /* read i through the pointer */
    printf("Hello from thread %d\n", myid);
    return NULL;
}

int main(void) {
    pthread_t tid[4];
    for (int i = 0; i < 4; i++)
        pthread_create(&tid[i], NULL, show, &i);   /* race on i */
    for (int i = 0; i < 4; i++)
        pthread_join(tid[i], NULL);
}
```

The program is correct only if each peer reads `i` before the main thread increments it. If the scheduler delays a peer, the peer reads a later value: two threads may print the same number and some number may be missing, and after the loop `i` may even be $4$. In experiments the error is rare on one core and frequent on a multicore machine. The fix gives each thread its own copy: pass the value itself, `(void *)(long)i`, or a pointer to a separately allocated block (@exm-thread-echo-server).

:::

::: {#fig-thread-safety-and-deadlock-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.8cm]
\node[lab] at (0,0.6) {main thread}; \node[lab] at (5,0.6) {peer thread 0};
\draw[faint] (0,0.2) -- (0,-4.6); \draw[faint] (5,0.2) -- (5,-4.6);
\node[tick, anchor=east] at (-0.1,0) {\texttt{i = 0}};
\draw[->] (0,-0.5) -- node[edge label, above] {create with \texttt{\&i}} (5,-0.9);
\node[tick, anchor=east] at (-0.1,-1.6) {\texttt{i++}: \texttt{i = 1}};
\node[dot] at (0,-1.6) {};
\draw[->, draw=accent, dashed] (5,-2.6) -- node[edge label, above] {reads \texttt{*vargp}} (0.1,-1.7);
\node[tick, anchor=west] at (5.1,-2.6) {\texttt{myid = 1}, not 0};
\draw[cell frame] (1.6,-4.0) rectangle (3.4,-3.4); \node[tick] at (2.5,-3.7) {\texttt{i} on main's stack};
\end{tikzpicture}
\end{center}
```

The race of @exm-race-loop-index: the peer reads `i` through the pointer only after the main thread has incremented it

:::

::: {#def-deadlock .definition name="Deadlock"}

A collection of threads is *deadlocked* when each is blocked waiting for a condition that will never become true, because only another thread of the collection could make it true. With mutexes, the typical case is two threads that each hold one mutex and wait in $P$ for the mutex the other holds. In a progress graph, the forbidden regions of two mutexes (@thm-mutex-forbidden-region) overlap so as to form a *deadlock region*: a set of states from which every trajectory leads into a corner it cannot leave.

:::

::: {#exm-deadlock-two-mutexes .example name="Two threads, two mutexes"}

Thread 1 runs $P(s)$, $P(t)$, $V(s)$, $V(t)$ and thread 2 runs $P(t)$, $P(s)$, $V(s)$, $V(t)$, with $s=t=1$ initially. If thread 1 completes $P(s)$ and thread 2 then completes $P(t)$, thread 1 blocks in $P(t)$ and thread 2 in $P(s)$, forever. Other schedules finish normally, which is what makes deadlock hard to find: the program may run correctly thousands of times.

:::

::: {#fig-thread-safety-and-deadlock-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\path[tintB] (2,1) rectangle (6,6); \node[tick] at (4.6,5.4) {forbidden for $t$};
\path[tintC] (1,2) rectangle (4,4); \node[tick] at (2.5,3.0) {forbidden for $s$};
\path[tintD] (1,1) rectangle (2,2); \node[tick, anchor=north east] at (1,1) {deadlock region};
\draw[->] (0,0) -- (6.8,0) node[lab, right] {thread 1};
\draw[->] (0,0) -- (0,6.8) node[lab, above] {thread 2};
\foreach \x/\n in {1/{$P(s)$},2/{$P(t)$},4/{$V(s)$},6/{$V(t)$}} { \draw (\x,-0.08) -- (\x,0.08); \node[tick] at (\x,-0.35) {\n}; }
\foreach \y/\n in {1/{$P(t)$},2/{$P(s)$},4/{$V(s)$},6/{$V(t)$}} { \draw (-0.08,\y) -- (0.08,\y); \node[tick, anchor=east] at (-0.1,\y) {\n}; }
\draw[emph, draw=accent, ->] (0,0) -- (1.0,0) -- (1.0,1.0) -- (1.6,1.0) -- (1.6,1.6);
\node[dot] at (1.6,1.6) {}; \node[tick, anchor=west] at (1.7,1.75) {stuck};
\draw[emph, draw=primary, ->] (0,0) -- (0,0.6) -- (0.6,0.6) -- (0.6,6.8);
\node[tick, text=primary, anchor=west] at (0.65,6.5) {safe: thread 2 first};
\end{tikzpicture}
\end{center}
```

Deadlock in a progress graph: once a trajectory enters the small region where thread 1 holds $s$ and thread 2 holds $t$, every move leads into a forbidden region, so no thread can proceed

:::

::: {#thm-mutex-lock-ordering .theorem name="Mutex lock ordering rule"}

Given a total ordering of all mutexes, a program is deadlock-free if each thread acquires its mutexes in that order and releases them in reverse order.

:::

::: {.proof}
1. Suppose some threads are deadlocked on mutexes. Each blocked thread $T_i$ waits in $P$ for a mutex $m_i$ held by another thread of the collection, $T_{i+1}$ say.

2. Following "waits for a mutex held by" from any thread, we must eventually revisit a thread, since there are finitely many: there is a cycle $T_1\to T_2\to\dots\to T_k\to T_1$.

3. $T_{i+1}$ holds $m_i$ and is itself waiting for $m_{i+1}$. Because $T_{i+1}$ acquires its mutexes in the given order and it already holds $m_i$, the mutex it is waiting for comes later: $m_i<m_{i+1}$.

4. Around the cycle this gives $m_1<m_2<\dots<m_k<m_1$, a contradiction. So no deadlock can occur.
:::

::: {#fig-thread-safety-and-deadlock-4}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\path[tintC] (1,1) rectangle (4,4);
\path[tintB] (2,2) rectangle (6,6);
\node[tick] at (1.9,1.5) {forbidden for $s$};
\node[tick] at (4.9,5.4) {forbidden for $t$};
\draw[->] (0,0) -- (6.8,0) node[lab, right] {thread 1};
\draw[->] (0,0) -- (0,6.8) node[lab, above] {thread 2};
\foreach \x/\n in {1/{$P(s)$},2/{$P(t)$},4/{$V(s)$},6/{$V(t)$}} { \draw (\x,-0.08) -- (\x,0.08); \node[tick] at (\x,-0.35) {\n}; }
\foreach \y/\n in {1/{$P(s)$},2/{$P(t)$},4/{$V(s)$},6/{$V(t)$}} { \draw (-0.08,\y) -- (0.08,\y); \node[tick, anchor=east] at (-0.1,\y) {\n}; }
\draw[emph, draw=accent, ->] (0,0) -- (0.6,0) -- (0.6,0.6) -- (6.8,0.6) -- (6.8,6.8);
\draw[emph, draw=primary, ->] (0,0) -- (0,6.8) -- (6.8,6.8);
\end{tikzpicture}
\end{center}
```

The same threads with both acquiring $s$ before $t$: the forbidden regions nest instead of forming a trap, and every trajectory can go around them

:::
