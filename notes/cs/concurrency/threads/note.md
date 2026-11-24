---
title: "Threads"
sources: [cmu15213-23, cmu15213-24, cmu15213lab-7]
requires: [cs/concurrency/concurrent-servers]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 23 "Concurrent Programming" (threads, Pthreads, a thread-based server) and Lecture 24 "Synchronization: Basics" (the memory model of threaded programs, shared variables), in our own wording; the code and the sharing example are our own. -->

A *thread* combines the two other approaches to concurrency (@sec-cs-concurrency-concurrent-servers): like processes, threads are scheduled by the kernel and identified by the kernel; like I/O multiplexing, they share one address space.

::: {#def-thread .definition name="Thread"}

A *thread* is a logical control flow running in the context of a process. Each thread has its own *thread context*: a thread ID, a stack, a stack pointer, a program counter, condition codes and general-purpose registers. All threads of a process share the rest of the process context: the code, the data, the heap, the shared libraries, and the open files (@def-descriptor-table). The first thread of a process is its *main thread*; the others are *peer threads*.

:::

::: {#fig-threads-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.55cm]
\begin{scope}
\node[lab] at (1.4,1.2) {process};
\foreach \i/\t in {0/{stack},1/{shared libraries},2/{heap},3/{data},4/{code}} { \draw[cell frame] (0,-\i) rectangle (2.8,-\i-0.9); \node[tick] at (1.4,-\i-0.45) {\t}; }
\draw[hl cell] (0,0) rectangle (2.8,-0.9); \node[tick] at (1.4,-0.45) {stack};
\draw[box] (0,-5.4) rectangle (2.8,-7.2); \node[tick] at (1.4,-5.9) {registers, PC, SP};
\node[tick] at (1.4,-6.6) {kernel context};
\end{scope}
\begin{scope}[xshift=5.2cm]
\node[lab] at (2.2,1.2) {process with two threads};
\draw[hl cell] (-0.6,0) rectangle (1.4,-0.9); \node[tick] at (0.4,-0.45) {stack 1};
\draw[hl cell] (3.0,0) rectangle (5.0,-0.9); \node[tick] at (4.0,-0.45) {stack 2};
\draw[box] (-0.6,-1.2) rectangle (1.4,-2.6); \node[tick] at (0.4,-1.6) {thread 1};\node[tick] at (0.4,-2.2) {regs, PC, SP};
\draw[box] (3.0,-1.2) rectangle (5.0,-2.6); \node[tick] at (4.0,-1.6) {thread 2};\node[tick] at (4.0,-2.2) {regs, PC, SP};
\path[tintB] (-0.6,-3.0) rectangle (5.0,-7.2);
\foreach \i/\t in {0/{shared libraries},1/{heap},2/{data},3/{code}} { \draw[cell frame] (-0.6,-3.0-\i) rectangle (5.0,-3.9-\i); \node[tick] at (2.2,-3.45-\i) {\t}; }
\node[tick] at (2.2,-7.6) {shared by both threads, with the open files and the kernel context};
\end{scope}
\end{tikzpicture}
\end{center}
```

A process seen as code and data plus one thread of control (left), and a process with two threads (right): each thread has its own stack and registers; everything else is shared

:::

::: {#prp-threads-vs-processes .proposition name="Threads and processes compared"}

Threads and processes have the same concurrency model (logical flows interleaved by the kernel) but differ in how they are organised and what they cost:

- the threads of a process form a *pool of peers*, not a tree: any thread can wait for or kill any other, and none is the parent of another;
- threads share code and data, so they communicate through memory; processes normally do not;
- creating and reaping a thread, and switching between two threads of one process, is cheaper than for processes, because no address space has to be copied or switched.

:::

::: {.proof}
1. A thread switch saves and restores only a thread context (registers, stack pointer, program counter); the page tables and the rest of the process context stay as they are, whereas a process switch (@def-context-switch) also changes the address space, which flushes the TLB (@def-tlb).

2. Creating a thread allocates a stack and a thread context; `fork` must duplicate the process's page tables and descriptor table, even with copy-on-write (@def-copy-on-write).

3. The peer structure is a property of the Pthreads interface (@def-pthreads): `pthread_join` and `pthread_cancel` take any thread ID in the process, unlike `waitpid`, which waits only for children.
:::

::: {#fig-threads-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}
\node[lab] at (0,0.7) {threads of one process};
\node[hl box] (m) at (0,0) {main};
\foreach \n/\a in {T1/90,T2/18,T3/-54,T4/-126,T5/162} { \node[box] (\n) at ({1.6*cos(\a)},{1.6*sin(\a)-1.6}) {\n}; }
\foreach \a/\b in {T1/T2,T2/T3,T3/T4,T4/T5,T5/T1,T1/T3,T2/T4,T3/T5,T4/T1,T5/T2} { \draw[faint] (\a) -- (\b); }
\draw[faint] (m) -- (T1);
\node[tick] at (0,-3.6) {a pool of peers};
\end{scope}
\begin{scope}[xshift=6cm]
\node[lab] at (0,0.7) {processes};
\node[hl box] (p0) at (0,0) {P0};
\node[box] (p1) at (-1.2,-1.2) {P1}; \node[box] (p2) at (1.2,-1.2) {P2};
\node[box] (p3) at (-1.8,-2.4) {P3}; \node[box] (p4) at (-0.6,-2.4) {P4};
\draw[->] (p0) -- (p1); \draw[->] (p0) -- (p2); \draw[->] (p1) -- (p3); \draw[->] (p1) -- (p4);
\node[tick] at (0,-3.6) {a tree of parents and children};
\end{scope}
\end{tikzpicture}
\end{center}
```

The threads of a process are peers; processes form a hierarchy rooted at the process that created them

:::

::: {#fig-threads-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm]
\draw[->] (0,-2.6) -- (11,-2.6) node[lab, right] {time};
\foreach \y/\n in {0/{thread A},-1/{thread B},-2/{thread C}} { \node[lab, anchor=east] at (-0.2,\y) {\n}; \draw[faint] (0,\y) -- (10.6,\y); }
\foreach \x/\y in {0/0,1.5/-1,3/0,4.5/-2,6/-1,7.5/0,9/-2} { \draw[emph, draw=primary] (\x,\y) -- (\x+1.5,\y); }
\draw[decorate, decoration={brace}] (3,0.3) -- (9,0.3) node[midway, above=2pt, tick] {A and B overlap in time: concurrent};
\end{tikzpicture}
\end{center}
```

Concurrent threads on one core: the kernel runs one thread at a time and switches between them; on several cores, the segments can also run at the same moment

:::

::: {#def-pthreads .definition name="The Pthreads interface"}

POSIX threads (Pthreads) is the standard C interface to threads:

- `pthread_create(&tid, NULL, f, arg)` creates a thread that runs `f(arg)`, where `f` has type `void *(*)(void *)`, and stores its ID in `tid`;
- a thread terminates when `f` returns, or when it calls `pthread_exit(ret)`; a call of `exit` by any thread terminates the whole process with all its threads;
- `pthread_join(tid, &ret)` blocks until thread `tid` terminates, reaps it, and stores its return value;
- `pthread_detach(tid)` makes a thread *detached*: it cannot be joined, and the system reaps it automatically when it terminates. By default threads are *joinable*, and a joinable thread that is never joined keeps its resources, like a zombie process (@def-reaping);
- `pthread_self()` returns the caller's own ID.

:::

::: {#exm-pthreads-hello .example name="Hello from a peer thread"}

```c
#include <pthread.h>
#include <stdio.h>

void *hello(void *arg) {                 /* thread routine */
    printf("hello from thread %ld\n", (long)arg);
    return NULL;
}

int main(void) {
    pthread_t tid;
    pthread_create(&tid, NULL, hello, (void *)1L);
    pthread_join(tid, NULL);             /* wait for the peer */
    return 0;                            /* exit: ends all threads */
}
```

Without the `pthread_join`, `main` might return, and so terminate the process, before the peer thread has printed anything.

:::

::: {#fig-threads-4}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.8cm]
\node[lab] at (0,0.6) {main thread}; \node[lab] at (4.5,0.6) {peer thread};
\draw[emph] (0,0.2) -- (0,-0.6);
\node[tick, anchor=east] at (-0.1,-0.6) {\texttt{pthread\_create}};
\draw[->, draw=accent] (0,-0.6) -- (4.5,-1.0);
\draw[emph] (0,-0.6) -- (0,-1.4); \node[tick, anchor=east] at (-0.1,-1.4) {\texttt{pthread\_join}};
\draw[faint, dashed] (0,-1.4) -- (0,-3.6); \node[tick, anchor=east] at (-0.1,-2.5) {waits};
\draw[emph, draw=accent] (4.5,-1.0) -- (4.5,-3.0);
\node[tick, anchor=west] at (4.6,-1.8) {\texttt{printf}};
\node[tick, anchor=west] at (4.6,-3.0) {\texttt{return NULL}: terminates};
\draw[->, dashed] (4.5,-3.0) -- (0,-3.6);
\draw[emph] (0,-3.6) -- (0,-4.4); \node[tick, anchor=east] at (-0.1,-4.4) {\texttt{return 0}: process ends};
\end{tikzpicture}
\end{center}
```

The execution of @exm-pthreads-hello: the main thread waits in `pthread_join` until the peer thread has terminated

:::

::: {#exm-thread-echo-server .example name="A thread-based echo server"}

```c
void *serve(void *vargp) {
    int connfd = *(int *)vargp;
    free(vargp);                          /* the main thread allocated it */
    pthread_detach(pthread_self());       /* nobody will join this thread */
    echo(connfd);
    close(connfd);
    return NULL;
}

int main(int argc, char **argv) {
    int listenfd = open_listenfd(argv[1]);
    for (;;) {
        int *connfdp = malloc(sizeof(int));   /* one int per client */
        *connfdp = accept(listenfd, NULL, NULL);
        pthread_t tid;
        pthread_create(&tid, NULL, serve, connfdp);
    }
}
```

Each connected descriptor is stored in its own heap block. Passing the address of a local variable `connfd` of `main` instead would be a *race* (@def-race): the main thread could accept the next client and overwrite `connfd` before the peer thread has read it, and two threads would then serve the same client. The peer thread runs detached, so it is reaped without a join, and it frees the block itself.

:::

::: {#fig-threads-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (c1) at (0,1.4) {client 1}; \node[box] (c2) at (0,-1.4) {client 2};
\node[hl box] (m) at (4.5,0) {main thread: \texttt{accept}};
\node[box] (t1) at (8.8,1.4) {peer 1: \texttt{echo}};
\node[box] (t2) at (8.8,-1.4) {peer 2: \texttt{echo}};
\draw[->, dashed] (c1) -- (m); \draw[->, dashed] (c2) -- (m);
\draw[->] (m) -- node[edge label, above] {create} (t1); \draw[->] (m) -- node[edge label, below] {create} (t2);
\draw[<->, emph, draw=accent] (c1) to[bend left=12] (t1); \draw[<->, emph, draw=accent] (c2) to[bend right=12] (t2);
\draw[regionB] (3.0,-2.2) rectangle (10.3,-2.8); \node[tick] at (6.65,-2.5) {one address space: globals and heap shared by all threads};
\end{tikzpicture}
\end{center}
```

Execution model of a thread-based server: the same structure as the process-based one (@fig-concurrent-servers-2), but all threads live in one address space

:::

::: {#def-shared-variable .definition name="Shared variable"}

In the memory model of threaded C programs, each variable has one or more *instances* in memory:

- a *global* variable (declared outside any function) has exactly one instance, which any thread can use;
- a *local automatic* variable (declared in a function without `static`) has one instance on the stack of each thread that runs the function;
- a *local static* variable has exactly one instance, like a global.

A variable is *shared* if and only if more than one thread references some instance of it. Stacks are not protected from other threads: a thread that obtains a pointer to another thread's stack can read and write it, which is how a local variable can become shared.

:::

::: {#exm-sharing-analysis .example name="Which variables are shared?"}

```c
char **names;                       /* global */

void *greet(void *vargp) {
    long id = (long)vargp;          /* local automatic */
    static int calls = 0;           /* local static */
    printf("[%ld] %s (%d)\n", id, names[id], ++calls);
    return NULL;
}

int main(void) {
    char *msgs[2] = {"hello", "world"};   /* local to main */
    names = msgs;
    pthread_t tid[2];
    for (long i = 0; i < 2; i++)
        pthread_create(&tid[i], NULL, greet, (void *)i);
    for (int i = 0; i < 2; i++)
        pthread_join(tid[i], NULL);
}
```

| variable instance | referenced by main | by peer 0 | by peer 1 | shared |
|---|---|---|---|---|
| `names` | yes | yes | yes | yes |
| `calls` | no | yes | yes | yes |
| `msgs` (on main's stack) | yes | yes | yes | yes |
| `i` (main's stack) | yes | no | no | no |
| `id` (peer 0's stack) | no | yes | no | no |
| `id` (peer 1's stack) | no | no | yes | no |

`msgs` is local to `main`, yet shared: the peers reach it through the global pointer `names`. The update `++calls` by two threads is unsynchronised, so it is a bug of the kind analysed in @sec-cs-concurrency-semaphores-and-mutual-exclusion.

:::

::: {#fig-threads-6}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.6cm]
\draw[cell frame] (0,0) rectangle (3,-1); \node[tick] at (1.5,-0.5) {main's stack: \texttt{msgs}, \texttt{i}};
\draw[cell frame] (0,-1.4) rectangle (3,-2.4); \node[tick] at (1.5,-1.9) {peer 0 stack: \texttt{id}};
\draw[cell frame] (0,-2.8) rectangle (3,-3.8); \node[tick] at (1.5,-3.3) {peer 1 stack: \texttt{id}};
\draw[hl cell] (0,-4.6) rectangle (3,-5.6); \node[tick] at (1.5,-5.1) {data: \texttt{names}, \texttt{calls}};
\node[box] (p0) at (6.5,-1.9) {peer 0}; \node[box] (p1) at (6.5,-3.3) {peer 1};
\draw[->] (p0) -- (3.0,-1.9); \draw[->] (p1) -- (3.0,-3.3);
\draw[->, draw=accent] (p0.south west) -- (3.0,-4.9); \draw[->, draw=accent] (p1.south west) -- (3.0,-5.3);
\draw[->, draw=accent, dashed] (p0.north west) -- (3.0,-0.4);
\draw[->, draw=accent, dashed] (p1.west) to[out=150, in=0] (3.0,-0.7);
\node[tick, anchor=west] at (7.4,-0.4) {dashed: through the pointer \texttt{names}};
\end{tikzpicture}
\end{center}
```

The instances of @exm-sharing-analysis: each peer uses its own `id`, but both reach the globals and, through `names`, the array `msgs` on the main thread's stack

:::
