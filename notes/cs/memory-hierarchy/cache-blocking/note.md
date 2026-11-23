---
title: "Blocking for Temporal Locality"
sources: [cmu15213-12, cmu15213r-7, cmu15213lab-4]
requires: [cs/memory-hierarchy/cache-performance]
relations:
  related: [math/numerical/direct-solvers/caches-and-blocking]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 12 "Cache Memories", Recitation 7 (blocked matrix multiplication and transpose) and the Cache Lab handout (part B), in our own wording; the miss counts are proved in steps. The ideal-cache treatment of blocked matrix algorithms is in math/numerical/direct-solvers/caches-and-blocking. -->

Reordering loops (@exm-matmul-loop-orders) improves spatial locality. Matrix multiplication also has a great deal of potential temporal locality, since it reads $3n^2$ numbers but performs $2n^3$ operations, so every element is used about $n$ times. *Blocking* turns that potential into actual cache hits.

::: {#def-blocking .definition name="Blocking (tiling)"}

*Blocking* splits a large array computation into sub-computations on small $b\times b$ sub-arrays (*blocks* or *tiles*) chosen so that the tiles in use at the same time fit in the cache together; each tile is then used many times while it is cached.

:::

::: {#def-blocked-matmul .definition name="Blocked matrix multiplication"}

For $n\times n$ matrices with $b\mid n$, write $A$, $B$, $C$ as $(n/b)\times(n/b)$ grids of $b\times b$ blocks. Then $C_{IJ}=\sum_K A_{IK}B_{KJ}$, and the blocked algorithm is

```c
for (i = 0; i < n; i += b)
    for (j = 0; j < n; j += b)
        for (k = 0; k < n; k += b)
            /* C[i..i+b)[j..j+b) += A[i..i+b)[k..k+b) * B[k..k+b)[j..j+b) */
            for (i1 = i; i1 < i + b; i1++)
                for (j1 = j; j1 < j + b; j1++)
                    for (k1 = k; k1 < k + b; k1++)
                        c[i1*n + j1] += a[i1*n + k1] * b[k1*n + j1];
```

:::

::: {#thm-blocked-matmul-cache-misses .theorem name="Misses of plain and blocked matrix multiplication" related="thm-blocked-matmul-misses"}

Let a cache block hold $8$ doubles, let the cache size $C$ (in doubles) satisfy $C\ll n$, and count misses on $A$ and $B$ only.

1. The `ijk` triple loop incurs about $\tfrac98n^3$ misses.
2. The blocked algorithm with $3b^2<C$ incurs about $\tfrac{n^3}{4b}$ misses.

:::

::: {.proof}
1. *Plain.* Computing one element of $C$ scans a row of $A$ ($n/8$ misses, $8$ elements per block) and a column of $B$ ($n$ misses, one per element, @exm-matmul-loop-orders). Because $C\ll n$, nothing of the previous row or column survives to be reused, so each of the $n^2$ elements of $C$ costs $\tfrac98n$ misses: $\tfrac98n^3$ in total.

2. *One block product.* With $3b^2<C$, the three $b\times b$ blocks in use fit in the cache together. Loading a block of $A$ or $B$ costs $b^2/8$ misses (each of its $b$ rows covers $b/8$ cache blocks), and after that every access to it hits.

3. *One block of $C$.* Computing $C_{IJ}$ multiplies $n/b$ pairs of blocks $A_{IK}$, $B_{KJ}$, each pair loaded once: $2\cdot\tfrac nb\cdot\tfrac{b^2}8=\tfrac{nb}4$ misses.

4. *All of $C$.* There are $(n/b)^2$ blocks of $C$, so the total is $\tfrac{nb}{4}\cdot\tfrac{n^2}{b^2}=\tfrac{n^3}{4b}$.

5. The ratio of the two counts is $\tfrac98n^3\big/\tfrac{n^3}{4b}=4.5\,b$, so the largest $b$ with $3b^2<C$ is the best choice.
:::

::: {#fig-cache-blocking-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.75]
\foreach \x/\n in {0/C,3.0/A,6.0/B} {
  \draw[cell frame] (\x,0) rectangle (\x+2.4,2.4);
  \foreach \k in {0.6,1.2,1.8} { \draw[gridline] (\x+\k,0) -- (\x+\k,2.4); \draw[gridline] (\x,\k) -- (\x+2.4,\k); }
  \node[lab] at (\x+1.2,2.75) {$\n$};
}
\node[lab] at (2.7,1.2) {$=$}; \node[lab] at (5.7,1.2) {$\times$};
\draw[hl cell] (0.6,1.2) rectangle (1.2,1.8);
\path[tintB] (3.0,1.2) rectangle (5.4,1.8); \draw[hl cell] (4.2,1.2) rectangle (4.8,1.8);
\path[tintB] (6.6,0) rectangle (7.2,2.4); \draw[hl cell] (6.6,0.0) rectangle (7.2,0.6);
\node[tick] at (0.9,-0.4) {$C_{IJ}$};
\node[tick] at (4.2,-0.4) {row $I$ of $A$};
\node[tick] at (7.2,-0.4) {column $J$ of $B$};
\end{tikzpicture}
\end{center}
```

Blocked multiplication: block $C_{IJ}$ accumulates the products of the blocks of row $I$ of $A$ and column $J$ of $B$; the three blocks currently in use (shaded) fit in the cache together

:::

::: {#exm-blocked-transpose .example name="Blocked transpose"}

Transposing an $n\times n$ matrix, `B[j][i] = A[i][j]`, reads $A$ along rows and writes $B$ along columns. In a direct-mapped cache of $1$ KiB with $32$-byte blocks ($8$ `int`s per block, $32$ sets), take $n=32$ and place $B$ $4096$ bytes after $A$, so that `A[i][j]` and `B[i][j]` map to the same set. Counting misses by simulation:

| method | misses |
|---|---|
| row by row | $1180$ |
| $4\times4$ blocks | $484$ |
| $8\times8$ blocks | $340$ |

With $8\times8$ blocks, the eight rows of a block of $B$ that are written stay in eight different sets while the block is processed, so each cache block of $B$ is loaded once per tile instead of once per element. Most of the remaining misses come from the diagonal blocks, where $A$ and $B$ use the same sets and evict each other.

:::

::: {#fig-cache-blocking-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.42]
\foreach \m/\x in {A/0,B/9} {
  \draw[cell frame] (\x,0) rectangle (\x+8,8);
  \foreach \k in {2,4,6} { \draw[gridline] (\x+\k,0) -- (\x+\k,8); \draw[gridline] (\x,\k) -- (\x+8,\k); }
  \node[lab] at (\x+4,8.6) {$\m$};
}
\draw[hl cell] (2,4) rectangle (4,6);
\foreach \r in {0,...,3} { \draw[->, draw=accent] (2.1,5.75-\r*0.5) -- (3.9,5.75-\r*0.5); }
\draw[hl cell] (13,2) rectangle (15,4);
\foreach \c in {0,...,3} { \draw[->, draw=accent] (13.25+\c*0.5,3.9) -- (13.25+\c*0.5,2.1); }
\draw[map] (4.1,5) to[out=-10,in=190] (12.9,3);
\node[tick] at (8.5,-0.8) {tile $(I,J)$ of $A$ becomes tile $(J,I)$ of $B$};
\end{tikzpicture}
\end{center}
```

Blocked transpose: a tile of $A$ read along its rows is written as a tile of $B$ down its columns; both tiles stay in the cache while the tile is processed

:::

::: {#rmk-cache-blocking-1 name="Choosing the block size"}

The block must be large enough that each cache block brought in is fully used, and small enough that the working tiles fit in the cache without conflicting. The right choice depends on the cache size, the associativity, the block size and the matrix dimensions; for awkward dimensions (such as $64\times64$ in the small direct-mapped cache above, where rows four apart collide) different shapes or a different order inside the tile are needed. Measuring a few candidates is usually quicker than predicting.

:::
