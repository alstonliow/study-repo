---
title: "Thread-Level Parallelism"
sources: [cmu15213-26]
requires: [cs/concurrency/semaphores-and-mutual-exclusion, cs/machine-level/instruction-level-parallelism]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 26 "Thread-Level Parallelism" (multicore processors, parallel summation, speedup and efficiency, Amdahl's law, parallel quicksort, memory consistency), in our own wording; proofs written out in steps; the numbers are our own computations. -->

On a single core, threads make a program concurrent but not faster: the kernel interleaves them. On a multicore processor the threads of one program can run at the same moment on different cores, and a well-written program runs faster. *Parallel* programs are concurrent programs running on multiple processors.

::: {#def-multicore .definition name="Multicore processor and hyperthreading"}

A *multicore processor* puts several CPUs (*cores*) on one chip. Each core has its own registers, L1 and L2 caches; all cores share the L3 cache and main memory (@exm-core-i7-caches). *Hyperthreading* (simultaneous multithreading) lets one core run two threads at once: the core keeps two copies of the registers and program counter and issues instructions from both threads to its shared functional units (@def-superscalar-pipelined), which fills slots one thread alone would leave idle.

:::

::: {#fig-thread-level-parallelism-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {0,...,3} {
  \draw[regionA] (\i*2.4,0) rectangle (\i*2.4+2.1,2.6); \node[lab] at (\i*2.4+1.05,2.35) {core \i};
  \draw[box] (\i*2.4+0.2,1.6) rectangle (\i*2.4+1.9,2.05); \node[tick] at (\i*2.4+1.05,1.82) {registers};
  \draw[box] (\i*2.4+0.2,0.95) rectangle (\i*2.4+1.0,1.4); \node[tick] at (\i*2.4+0.6,1.17) {L1-d};
  \draw[box] (\i*2.4+1.1,0.95) rectangle (\i*2.4+1.9,1.4); \node[tick] at (\i*2.4+1.5,1.17) {L1-i};
  \draw[box] (\i*2.4+0.2,0.2) rectangle (\i*2.4+1.9,0.7); \node[tick] at (\i*2.4+1.05,0.45) {L2 unified};
}
\draw[hl box] (0,-1.0) rectangle (9.3,-0.4); \node[tick] at (4.65,-0.7) {L3 unified cache, shared by all cores};
\draw[regionC] (0,-2.2) rectangle (9.3,-1.6); \node[tick] at (4.65,-1.9) {main memory};
\foreach \i in {0,...,3} { \draw (\i*2.4+1.05,0) -- (\i*2.4+1.05,-0.4); }
\draw (4.65,-1.0) -- (4.65,-1.6);
\node[tick] at (4.65,-2.5) {one processor chip, except main memory};
\end{tikzpicture}
\end{center}
```

A quad-core processor: private registers and L1, L2 caches per core, a shared L3 cache, and one main memory

:::

::: {#exm-parallel-sum .example name="Summing in parallel, three ways"}

Compute $\sum_{i=0}^{n-1}i$ with $t$ threads, thread $k$ summing the block of $n/t$ consecutive values starting at $k\cdot n/t$.

1. *psum-mutex*: every thread adds each value to one global `sum`, inside a mutex (@def-mutex). Correct, but every addition costs a lock and an unlock, and the threads serialise on the mutex: with more threads the program becomes *slower*, often by orders of magnitude, than the sequential loop.
2. *psum-array*: each thread adds into its own element `psum[k]` of a global array, and the main thread adds the $t$ partial sums after joining the threads. No synchronisation is needed, since no two threads touch the same element, and the program speeds up with $t$.
3. *psum-local*: each thread accumulates in a local variable (a register) and stores it into `psum[k]` once at the end. This removes a memory load and store per iteration, and avoids the cache line holding `psum` bouncing between cores, so it is faster again.

The lesson: synchronisation is expensive, so a parallel program should share as little as possible in its inner loops.

:::

::: {#fig-thread-level-parallelism-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.7cm]
\draw[cell frame] (0,0) rectangle (16,0.6);
\foreach \k/\tn in {0/tintA,1/tintB,2/tintC,3/tintD} {
  \path[\tn] (\k*4,0) rectangle (\k*4+4,0.6);
  \node[tick] at (\k*4+2,0.3) {thread \k};
}
\foreach \i in {0,4,8,12,16} { \draw (\i,0) -- (\i,0.6); }
\node[tick, anchor=east] at (-0.2,0.3) {$0,\dots,n-1$};
\foreach \k in {0,...,3} { \draw[->] (\k*4+2,-0.05) -- (\k*4+2,-0.75); \draw[hl cell] (\k*4+1.2,-1.35) rectangle (\k*4+2.8,-0.8); \node[tick] at (\k*4+2,-1.07) {\texttt{psum[\k]}}; }
\draw[->] (8,-1.4) -- (8,-2.0); \node[box] at (8,-2.35) {main thread adds the 4 partial sums};
\end{tikzpicture}
\end{center}
```

psum-array and psum-local: each thread sums its own block into its own slot; only the final combination is sequential

:::

::: {#def-speedup .definition name="Speedup and efficiency"}

Let $T_p$ be the running time of a program on $p$ cores. The *speedup* is
$$S_p=\frac{T_1}{T_p}.$$
It is the *absolute speedup* when $T_1$ is the time of the best sequential program, and the *relative speedup* when $T_1$ is the time of the parallel program run on one core. The *efficiency* $E_p=S_p/p$, often given in percent, measures the fraction of the cores' time spent on useful work rather than on overhead; ideally $S_p=p$ and $E_p=1$.

:::

::: {#thm-amdahl-law .theorem name="Amdahl's law"}

Suppose a fraction $\alpha$ of a program's sequential running time $T$ can be sped up by a factor $k$, and the rest cannot. Then the new running time and the overall speedup are
$$T_{\text{new}}=(1-\alpha)T+\frac{\alpha T}{k},\qquad S=\frac{T}{T_{\text{new}}}=\frac{1}{(1-\alpha)+\alpha/k}.$$
In particular, however large $k$ is,
$$S<\frac{1}{1-\alpha}.$$

:::

::: {.proof}
1. The part that is not sped up still takes $(1-\alpha)T$; the other part took $\alpha T$ and now takes $\alpha T/k$. Adding gives $T_{\text{new}}$.

2. Dividing $T$ by $T_{\text{new}}$ and cancelling $T$ gives $S=1/\big((1-\alpha)+\alpha/k\big)$.

3. For $\alpha<1$ and every $k\ge1$, $\alpha/k>0$, so the denominator exceeds $1-\alpha$ and $S<1/(1-\alpha)$. As $k\to\infty$ the bound is approached: $S\to1/(1-\alpha)$.
:::

::: {#exm-amdahl-numbers .example name="Amdahl's law with numbers"}

If $90\%$ of a program parallelises perfectly ($\alpha=0.9$, $k=p$ cores):

| cores $p$ | 2 | 4 | 8 | 16 | $\infty$ |
|---|---|---|---|---|---|
| speedup $S_p$ | 1.82 | 3.08 | 4.71 | 6.40 | 10 |
| efficiency $E_p$ | 0.91 | 0.77 | 0.59 | 0.40 | 0 |

With $\alpha=0.95$, $8$ cores give $5.93$ and $16$ give $9.14$. The sequential $10\%$ or $5\%$ dominates as soon as the parallel part has become short, which is why the hot sequential steps must be parallelised too. The same law limits single-thread optimisation (@sec-cs-machine-level-code-optimization): speeding up a part that takes $\alpha$ of the time cannot gain more than a factor $1/(1-\alpha)$.

:::

::: {#fig-thread-level-parallelism-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.42cm, y=0.35cm]
\draw[->] (0,0) -- (17,0) node[lab, right] {cores $p$};
\draw[->] (0,0) -- (0,17) node[lab, above] {speedup};
\foreach \v in {4,8,12,16} { \draw (\v,-0.2) -- (\v,0.2); \node[tick] at (\v,-0.8) {\v}; \draw (-0.2,\v) -- (0.2,\v); \node[tick, anchor=east] at (-0.3,\v) {\v}; }
\draw[faint, dashed] (1,1) -- (16,16); \node[tick, anchor=west] at (13.5,15.5) {ideal $S_p=p$};
\draw[emph, draw=primary, domain=1:16, samples=40] plot (\x, {1/(0.05+0.95/\x)});
\draw[emph, draw=accent, domain=1:16, samples=40] plot (\x, {1/(0.1+0.9/\x)});
\draw[faint] (0,10) -- (16.5,10); \node[tick, anchor=west] at (16.6,10) {limit $10$};
\node[tick, text=primary, anchor=west] at (16.2,9.1) {$\alpha=0.95$};
\node[tick, text=accent, anchor=west] at (16.2,6.4) {$\alpha=0.9$};
\end{tikzpicture}
\end{center}
```

Amdahl's law: the speedup approaches $1/(1-\alpha)$ and stays far below the ideal line, the more so the larger the sequential fraction

:::

::: {#exm-parallel-quicksort .example name="Parallel quicksort"}

Quicksort (@def-quicksort) partitions the array around a pivot and then sorts the two parts independently, so the recursive calls can run in parallel. A *task* sorts a range: if the range has fewer than some threshold of elements it sorts it sequentially; otherwise it partitions the range and creates two new tasks, which run as separate threads (or are handed to a pool of worker threads, @def-prethreaded-server). The program waits until all tasks are done.

The speedup is limited by Amdahl's law: the first partition step, over the whole array, runs on one core, the two partitions of the second level on two cores, and so on; the top levels are a sequential fraction of the work. Parallelising the partition step itself helps in principle but is hard to make efficient. The threshold also matters: too small and the overhead of creating tasks dominates; too large and there are too few tasks to keep all cores busy.

:::

::: {#fig-thread-level-parallelism-4}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm, y=0.8cm]
\draw[hl cell] (0,0) rectangle (16,0.5); \node[tick] at (8,0.25) {partition (1 core)};
\draw[cell frame] (0,-1) rectangle (7,-0.5); \node[tick] at (3.5,-0.75) {partition};
\draw[cell frame] (7.4,-1) rectangle (16,-0.5); \node[tick] at (11.7,-0.75) {partition};
\foreach \a/\b in {0/3,3.3/7,7.4/11,11.4/16} { \path[tintA] (\a,-2) rectangle (\b,-1.5); \draw[cell frame] (\a,-2) rectangle (\b,-1.5); }
\node[tick] at (8,-2.4) {below the threshold: each part sorted sequentially by its own task};
\draw[->] (8,0) -- (3.5,-0.5); \draw[->] (8,0) -- (11.7,-0.5);
\foreach \x/\t in {3.5/1.5,3.5/5.15,11.7/9.2,11.7/13.7} { \draw[->] (\x,-1) -- (\t,-1.5); }
\node[tick, anchor=west] at (16.4,0.25) {1 task};
\node[tick, anchor=west] at (16.4,-0.75) {2 tasks in parallel};
\node[tick, anchor=west] at (16.4,-1.75) {4 tasks in parallel};
\end{tikzpicture}
\end{center}
```

Parallel quicksort: each level of partitioning creates twice as many tasks; the top level is sequential

:::

::: {#def-sequential-consistency .definition name="Sequential consistency"}

A *memory consistency model* says which values reads may return when threads on different cores access shared memory. Under *sequential consistency*, every execution behaves as if the operations of all threads were interleaved into one sequence that keeps each thread's own program order, every read returning the value of the most recent write before it in that sequence. Caches must then keep all copies of a location consistent: with a *snoopy* protocol, each cache line is marked exclusive, shared or invalid, and a core that writes a shared line invalidates the copies in the other cores' caches.

:::

::: {#exm-consistency-outcomes .example name="Which outputs are possible?"}

With `int a = 1, b = 100;` shared, thread 1 runs `a = 2; print(b);` and thread 2 runs `b = 200; print(a);`. Under sequential consistency the possible outputs (thread 1's value of `b`, thread 2's value of `a`) are $(100,2)$, $(200,2)$ and $(200,1)$. The output $(100,1)$ is impossible: it needs thread 1's read of `b` before thread 2's write of `b`, and thread 2's read of `a` before thread 1's write of `a`, which together with the program orders gives the cycle $W_a<R_b<W_b<R_a<W_a$. Real x86 processors buffer stores, so they can in fact produce $(100,1)$; code that depends on such orderings needs memory fences or atomic operations, which mutexes contain.

:::

::: {#fig-thread-level-parallelism-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (wa) at (0,1.2) {$W_a$: \texttt{a = 2}};
\node[box] (rb) at (0,0) {$R_b$: \texttt{print(b)}};
\node[box] (wb) at (5,1.2) {$W_b$: \texttt{b = 200}};
\node[box] (ra) at (5,0) {$R_a$: \texttt{print(a)}};
\draw[->, emph] (wa) -- node[edge label, left] {program order} (rb);
\draw[->, emph] (wb) -- node[edge label, right] {program order} (ra);
\draw[->, draw=accent, dashed] (rb) -- (wb);
\draw[->, draw=accent, dashed] (ra) -- (wa);
\node[tick] at (2.5,-1.0) {a cycle: no single interleaving gives $(100,1)$};
\end{tikzpicture}
\end{center}
```

Why the output $(100,1)$ violates sequential consistency: besides the two program orders (solid), reading $b=100$ needs $R_b$ before $W_b$ and reading $a=1$ needs $R_a$ before $W_a$ (dashed); the four constraints form a cycle

:::
