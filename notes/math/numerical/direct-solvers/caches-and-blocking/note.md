---
title: "Caches and Blocked Matrix Algorithms"
sources: [mit18335-11, mit18335-12]
requires: [math/numerical/direct-solvers/cholesky-factorization]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 11 and 12 (matrix operations, caches and blocking; cache-oblivious algorithms and spatial locality) and the ideal-cache handout, in our own wording. The ideal-cache model and the recursive multiplication bound are the existing blocks def-external-memory-model and prp-co-matrix; this note adds the numerical-linear-algebra side. -->

Flop counts no longer predict running time: a modern processor can do dozens of flops in the time it takes to fetch one number from main memory. Dense linear algebra is fast in practice only because its algorithms are reorganised so that each number brought into the cache is used many times.

::: {#rmk-caches-and-blocking-1 .remark name="The ideal-cache model in this note"}

We use the ideal-cache model of @def-external-memory-model, writing $Z$ for the cache size in words and $L$ for the line (block) size (the $M$ and $B$ of that definition), and count *cache misses* $Q$, the number of lines moved. We assume a *tall cache*, $Z\ge L^2$, and that an $n\times n$ matrix is stored by columns.

:::

::: {#prp-naive-matmul-misses .proposition name="Cache misses of the triple loop"}

Computing $C=AB$ for $n\times n$ matrices by the loop "for $i$, for $j$: $c_{ij}=\sum_ka_{ik}b_{kj}$" with $3n^2>Z$ incurs $Q=\Theta(n^3)$ misses in the worst case, and $\Theta(n^3/L)$ even with the best loop order.

:::

::: {.proof}

1. For fixed $(i,j)$ the inner loop reads row $i$ of $A$, whose entries are $n$ words apart in column-major storage, so each $a_{ik}$ is in a different line: $n$ misses unless the row is still cached.

2. The $n$ lines holding row $i$ of $A$ are reused for every $j$, but between two uses of a fixed entry the loop also sweeps a column of $B$ and the rest of the row, and over all $j$ it reads all of $B$. When the $nL$ words of those lines plus the columns of $B$ exceed $Z$, an LRU cache has evicted them, so in the worst case each of the $n^2$ inner loops costs $\Theta(n)$ misses, $\Theta(n^3)$ in total.

3. Reordering the loops so that the innermost index runs down columns makes every access sequential and gets $L$ useful words per miss, which gives $\Theta(n^3/L)$, but no better: each of the $\Theta(n^3)$ multiply–adds touches an entry that, for large $n$, was last used $\Theta(n^2)\gg Z$ accesses earlier.

:::

::: {#thm-blocked-matmul-misses .theorem name="Blocked matrix multiplication" related="prp-co-matrix"}

Split $A$, $B$, $C$ into $b\times b$ blocks with $3b^2\le Z$ and compute $C_{IJ}=\sum_KA_{IK}B_{KJ}$ one block product at a time. Then
$$Q=\Theta\Bigl(\frac{n^3}{L\sqrt Z}\Bigr)$$
for $b=\Theta(\sqrt Z)$ (and $n^2>Z$). This is optimal: every way of performing the $n^3$ multiply–adds of the standard algorithm needs $\Omega(n^3/(L\sqrt Z))$ misses (Hong and Kung).

:::

::: {.proof}

1. There are $(n/b)^3$ block products $A_{IK}B_{KJ}$. Each needs the three blocks in cache, which fit since $3b^2\le Z$; loading them costs $O(b^2/L+b)$ misses (a $b\times b$ block in column-major storage is $b$ contiguous pieces of length $b$).

2. Inside the cache the block product does $b^3$ multiply–adds with no further misses.

3. Total: $(n/b)^3\cdot O(b^2/L)=O(n^3/(bL))$ for $b\ge L$, which is $O(n^3/(L\sqrt Z))$ with $b\approx\sqrt{Z/3}$. Under the tall-cache assumption $b\ge L$ holds.

4. *Lower bound (sketch).* Split the computation into phases during which $Z$ new words are loaded. In a phase at most $2Z$ entries of $A$ and $B$ and $2Z$ of $C$ are available, and by a geometric inequality (Loomis–Whitney) at most $O(Z^{3/2})$ of the products $a_{ik}b_{kj}$ can be formed from them. So there are at least $n^3/O(Z^{3/2})$ phases, each costing $Z/L$ misses: $\Omega(n^3/(L\sqrt Z))$.

:::

The recursive, cache-oblivious version (@prp-co-matrix) reaches the same bound without knowing $Z$: the recursion eventually produces blocks that fit in every level of cache at once.

::: {#fig-caches-and-blocking-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.32]
\foreach \s/\lab in {0/C,10/A,20/B} {\draw[faint] (\s,0) rectangle (\s+8,8); \foreach \t in {2,4,6} {\draw[faint] (\s+\t,0) -- (\s+\t,8); \draw[faint] (\s,\t) -- (\s+8,\t);} \node[lab] at (\s+4,9) {$\lab$};}
\fill[accentLight, draw=accent] (2,4) rectangle (4,6);
\fill[tintA] (10,4) rectangle (18,6); \fill[accentLight, draw=accent] (14,4) rectangle (16,6);
\fill[tintA] (22,0) rectangle (24,8); \fill[accentLight, draw=accent] (22,2) rectangle (24,4);
\node[lab] at (9,4) {$=$}; \node[lab] at (19,4) {$\times$};
\node[note] at (3,-1) {$C_{IJ}$}; \node[note] at (15,-1) {$A_{IK}$}; \node[note] at (23,-1) {$B_{KJ}$};
\end{tikzpicture}
\end{center}
```

Blocked multiplication: block $C_{IJ}$ accumulates the products of the block row $I$ of $A$ (tinted) with the block column $J$ of $B$. At any moment only three $b\times b$ blocks (shaded) need to be in cache, and each word loaded is used in $b$ multiply–adds.

:::

::: {#def-blas-levels .definition name="BLAS levels and arithmetic intensity"}

The *Basic Linear Algebra Subprograms* are grouped by the data they touch:

1. *Level 1*, vector–vector ($\mathbf{y}\gets\alpha\mathbf{x}+\mathbf{y}$, dot products): $O(n)$ flops on $O(n)$ data;

2. *Level 2*, matrix–vector ($\mathbf{y}\gets A\mathbf{x}+\mathbf{y}$, rank-one updates, triangular solves): $O(n^2)$ flops on $O(n^2)$ data;

3. *Level 3*, matrix–matrix ($C\gets AB+C$, triangular solves with many right sides): $O(n^3)$ flops on $O(n^2)$ data.

The *arithmetic intensity* (flops per word moved from memory) is $O(1)$ for levels 1 and 2 but can be $O(\sqrt Z)$ for level 3 by @thm-blocked-matmul-misses. Only level 3 can run near the processor's peak speed.

:::

::: {#rmk-caches-and-blocking-2 .remark name="Blocked factorizations"}

LU, Cholesky and QR as written element by element (@def-partial-pivoting, @def-cholesky-factorization, @def-householder-qr) are sequences of level 2 operations: each step is a rank-one update of the trailing matrix. *Blocked* versions factor a panel of $b$ columns with the unblocked algorithm and then update the trailing matrix with one matrix–matrix product (for QR, several reflectors are combined into $I-VTV^{\mathsf H}$ with $V$ of size $m\times b$ and $T$ triangular, the "compact WY" form). For $b\ll n$ almost all flops are then level 3. Libraries such as LAPACK are organised this way on top of an optimised BLAS, and in timing experiments a tuned matrix multiplication runs ten to a hundred times faster than the straightforward triple loop on the same machine, with identical flop counts.

:::

::: {#fig-caches-and-blocking-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=0.62cm]
\draw[box] (-0.7,-0.42) rectangle (0.7,0.42); \node[lbl] at (0,0) {registers}; \node[note, anchor=west] at (2.7,0) {$\sim$1 cycle};
\draw[box] (-1.2,-1.42) rectangle (1.2,-0.58); \node[lbl] at (0,-1) {L1 cache}; \node[note, anchor=west] at (2.7,-1) {$\sim$4 cycles};
\draw[box] (-1.7,-2.42) rectangle (1.7,-1.58); \node[lbl] at (0,-2) {L2 and L3 caches}; \node[note, anchor=west] at (2.7,-2) {10--40 cycles};
\draw[box] (-2.3,-3.42) rectangle (2.3,-2.58); \node[lbl] at (0,-3) {main memory}; \node[note, anchor=west] at (2.7,-3) {$\sim$200 cycles};
\draw[->, faint] (-2.8,0.3) -- (-2.8,-3.3) node[note, below] {larger, slower};
\end{tikzpicture}
\end{center}
```

The memory hierarchy, with typical access latencies. Each level is larger and slower than the one above; blocking keeps the working set of an inner loop in the fast levels.

:::
