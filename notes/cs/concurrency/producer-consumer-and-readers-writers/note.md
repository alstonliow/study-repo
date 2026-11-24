---
title: "Producer-Consumer and Readers-Writers"
sources: [cmu15213-25, cmu15213lab-7]
requires: [cs/concurrency/semaphores-and-mutual-exclusion]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 25 "Synchronization: Advanced" (scheduling shared resources with semaphores, the producer-consumer and readers-writers problems, a prethreaded server) and the Proxy Lab handout (parts II and III: concurrency and a shared cache), in our own wording; the code is our own. -->

Besides mutual exclusion (@def-mutex), semaphores *schedule* access to shared resources: a thread waits for a condition, such as "the buffer has an item", and another thread signals it when the condition becomes true. Two classic patterns cover most uses.

::: {#def-producer-consumer .definition name="Producer-consumer problem"}

*Producer* threads and *consumer* threads share a *bounded buffer* of $n$ slots. A producer generates items and inserts them into the buffer; a consumer removes items and uses them. Insertions and removals must be mutually exclusive, a producer must wait while the buffer is full, and a consumer must wait while it is empty. Examples are a multimedia player (one thread decodes frames, another displays them), a graphical interface (one thread detects events, another handles them), and a prethreaded server (@def-prethreaded-server).

:::

::: {#fig-producer-consumer-and-readers-writers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (p) at (0,0) {producer threads};
\node[box] (c) at (9,0) {consumer threads};
\foreach \i in {0,...,5} { \draw[cell frame] (2.8+\i*0.6,-0.3) rectangle (3.4+\i*0.6,0.3); }
\foreach \i in {1,2,3} { \draw[hl cell] (2.8+\i*0.6,-0.3) rectangle (3.4+\i*0.6,0.3); }
\draw[->, emph] (p) -- node[edge label, above] {insert} (2.75,0);
\draw[->, emph] (6.45,0) -- node[edge label, above] {remove} (c);
\node[tick] at (4.6,-0.65) {bounded buffer, $n=6$ slots, 3 items};
\end{tikzpicture}
\end{center}
```

The producer-consumer pattern: the buffer decouples the speed of producers from that of consumers

:::

::: {#def-sbuf .definition name="Bounded buffer with three semaphores"}

A bounded buffer of $n$ items is a circular array `buf[0..n)` with two indices, `front` and `rear` (the next item is at `buf[front % n]`, the next free slot at `buf[rear % n]`), and three semaphores:

- `mutex`, initially $1$, protects the array and the indices;
- `slots`, initially $n$, counts the empty slots;
- `items`, initially $0$, counts the items.

To insert $x$: $P(\texttt{slots})$, $P(\texttt{mutex})$, store $x$ at `buf[rear++ % n]`, $V(\texttt{mutex})$, $V(\texttt{items})$. To remove: $P(\texttt{items})$, $P(\texttt{mutex})$, take `buf[front++ % n]`, $V(\texttt{mutex})$, $V(\texttt{slots})$.

:::

::: {#prp-sbuf-correct .proposition name="The bounded buffer is correct"}

With the operations of @def-sbuf, a producer never overwrites an item that has not been removed, and a consumer never removes from an empty buffer.

:::

::: {.proof}
1. Let $k=\texttt{rear}-\texttt{front}$ be the number of items stored. Each insertion is preceded by a completed $P(\texttt{slots})$ and each removal followed by a $V(\texttt{slots})$, so $\texttt{slots}\le n-k$ at all times; as $\texttt{slots}\ge0$ (semaphore invariant), an insertion that has passed $P(\texttt{slots})$ finds $k<n$ when it stores, hence a free slot.

2. Symmetrically, each removal is preceded by a completed $P(\texttt{items})$ and each insertion followed by $V(\texttt{items})$, so $\texttt{items}\le k$, and a removal that has passed $P(\texttt{items})$ finds $k>0$.

3. The array and indices are changed only between $P(\texttt{mutex})$ and $V(\texttt{mutex})$, so by @thm-mutex-forbidden-region no two insertions or removals interleave; with $0\le k\le n$ the positions `rear % n` and `front % n` never collide in a harmful way.
:::

::: {#fig-producer-consumer-and-readers-writers-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {0,...,7} { \draw[cell frame] ({\i*45}:1.2) -- ({\i*45}:2.0) arc ({\i*45}:{\i*45+45}:2.0) -- ({\i*45+45}:1.2) arc ({\i*45+45}:{\i*45}:1.2); }
\foreach \i in {2,3,4} { \draw[hl cell] ({\i*45}:1.2) -- ({\i*45}:2.0) arc ({\i*45}:{\i*45+45}:2.0) -- ({\i*45+45}:1.2) arc ({\i*45+45}:{\i*45}:1.2); }
\foreach \i in {0,...,7} { \node[tick] at ({\i*45+22.5}:1.6) {\i}; }
\draw[->, draw=accent, emph] ({90+0}:3.0) -- (90:2.05); \node[tick, anchor=south] at (90:3.0) {\texttt{front}: next item};
\draw[->, draw=primary, emph] (225:3.0) -- (225:2.05); \node[tick, anchor=north east] at (225:3.0) {\texttt{rear}: next free slot};
\node[tick, anchor=west] at (3.0,0.6) {\texttt{mutex} $=1$};
\node[tick, anchor=west] at (3.0,0.0) {\texttt{items} $=3$};
\node[tick, anchor=west] at (3.0,-0.6) {\texttt{slots} $=5$};
\end{tikzpicture}
\end{center}
```

A circular bounded buffer of $8$ slots holding $3$ items; the two counting semaphores record the items and the free slots

:::

::: {#def-readers-writers .definition name="Readers-writers problem"}

Threads share an object, such as a cache or a database. *Readers* only read it, *writers* modify it. A writer needs exclusive access, but any number of readers may access the object at the same time. In the *first readers-writers problem* (readers favoured), no reader waits unless a writer already holds the object; in the *second* (writers favoured), once a writer is waiting, no new reader may start. Either solution can *starve* a thread: in the first, a steady stream of readers can keep a writer waiting forever.

:::

::: {#exm-readers-first .example name="A readers-favoured solution"}

```c
int readcnt = 0;           /* number of readers inside; protected by mutex */
sem_t mutex, w;            /* both initialised to 1 */

void reader(void) {
    P(&mutex);
    if (++readcnt == 1)    /* first reader in locks out the writers */
        P(&w);
    V(&mutex);
    /* ... read the object ... */
    P(&mutex);
    if (--readcnt == 0)    /* last reader out lets the writers in */
        V(&w);
    V(&mutex);
}

void writer(void) {
    P(&w);
    /* ... write the object ... */
    V(&w);
}
```

The semaphore `w` is held either by one writer or by the whole group of readers present. Pthreads packages this pattern as `pthread_rwlock_t`, with `pthread_rwlock_rdlock`, `pthread_rwlock_wrlock` and `pthread_rwlock_unlock`.

:::

::: {#fig-producer-consumer-and-readers-writers-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.85cm]
\draw[->] (0,-0.6) -- (12,-0.6) node[lab, right] {time};
\draw[box] (0,1.8) rectangle (2,2.3); \node[tick] at (1,2.05) {writer};
\draw[hl box] (2.2,1.2) rectangle (6.5,1.7); \node[tick] at (4.3,1.45) {reader 1};
\draw[hl box] (3.0,0.6) rectangle (8.0,1.1); \node[tick] at (5.5,0.85) {reader 2};
\draw[hl box] (5.0,0.0) rectangle (9.5,0.5); \node[tick] at (7.2,0.25) {reader 3};
\draw[box] (9.7,1.8) rectangle (11.7,2.3); \node[tick] at (10.7,2.05) {writer};
\draw[dashed, draw=accent] (3.5,2.05) -- (9.7,2.05); \node[tick, text=accent] at (6.6,2.35) {second writer waits for the last reader};
\node[dot] at (3.5,2.05) {};
\end{tikzpicture}
\end{center}
```

Readers favoured: overlapping readers share the object while the arriving writer waits; if new readers kept arriving, the writer would starve

:::

::: {#def-prethreaded-server .definition name="Prethreaded concurrent server"}

Creating a thread per client costs a thread creation per connection. A *prethreaded* server instead creates a fixed pool of *worker threads* at start-up. The main thread is a producer: it accepts connections and inserts the connected descriptors into a bounded buffer (@def-sbuf). Each worker is a consumer: it repeatedly removes a descriptor, serves that client, and closes the descriptor.

:::

::: {#fig-producer-consumer-and-readers-writers-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (cl) at (-1.2,0) {clients};
\node[hl box] (m) at (1.8,0) {main thread};
\foreach \i in {0,...,4} { \draw[cell frame] (3.4+\i*0.5,-0.25) rectangle (3.9+\i*0.5,0.25); }
\draw[hl cell] (3.4,-0.25) rectangle (3.9,0.25); \draw[hl cell] (3.9,-0.25) rectangle (4.4,0.25);
\node[tick] at (4.65,-0.55) {buffer of \texttt{connfd}s};
\foreach \i/\y in {1/1.4,2/0,3/-1.4} { \node[box] (w\i) at (7.6,\y) {worker \i}; \draw[->] (5.95,0) -- (w\i.west); }
\draw[->] (cl) -- node[edge label, above] {\texttt{accept}} (m);
\draw[->] (m) -- node[edge label, above] {insert} (3.35,0);
\draw[<->, draw=accent] (cl.north) to[out=60, in=170] node[edge label, above] {service} (w1.west);
\end{tikzpicture}
\end{center}
```

A prethreaded server: the main thread produces connected descriptors, a fixed pool of worker threads consumes them

:::

::: {#rmk-producer-consumer-and-readers-writers-1 name="Condition variables"}

Pthreads offers a second scheduling tool: a *condition variable* `pthread_cond_t`, always used with a mutex. `pthread_cond_wait(&c, &m)` atomically releases `m` and blocks; when woken it locks `m` again before returning. `pthread_cond_signal(&c)` wakes one waiter, `pthread_cond_broadcast(&c)` all of them. Since a woken thread may find the condition false again, the wait sits in a loop: `while (buffer is full) pthread_cond_wait(&notfull, &m);`. A bounded buffer built this way needs one mutex and two condition variables instead of three semaphores (@prob-bounded-buffer-code).

:::
