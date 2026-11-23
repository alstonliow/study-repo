---
title: "Cache Performance and Cache-Friendly Code"
sources: [cmu15213-12, cmu15213r-7]
requires: [cs/memory-hierarchy/cache-organization]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 12 "Cache Memories" and Recitation 7, in our own wording; the miss counts are worked out step by step. -->

::: {#def-cache-metrics .definition name="Miss rate, hit time, miss penalty"}

The *miss rate* is the fraction of references that miss; the *hit rate* is $1$ minus it. The *hit time* is the time to deliver a word that is in the cache, including set selection and tag comparison. The *miss penalty* is the extra time a miss costs to fetch the block from the next level. The *average access time* is
$$T_{\text{avg}}=\text{hit time}+\text{miss rate}\times\text{miss penalty}.$$

:::

::: {#exm-hit-rate-matters .example name="97% versus 99% hits"}

With a hit time of $1$ cycle and a miss penalty of $100$ cycles, a hit rate of $97\%$ gives $1+0.03\cdot100=4$ cycles per access, while $99\%$ gives $1+0.01\cdot100=2$ cycles: two percentage points of hit rate halve the average time. This is why miss *rate*, not hit rate, is the number to watch.

:::

::: {#def-memory-mountain .definition name="Memory mountain"}

The *read throughput* of a loop that reads $n$ bytes with a fixed stride, repeatedly, is the number of megabytes read per second. Plotted against the size of the data (temporal locality) and the stride (spatial locality), it forms the *memory mountain* of a machine: high ridges where the data fits in L1, L2 or L3, a low plateau where it lives in main memory, and slopes that fall as the stride grows, until every access touches a new block.

:::

::: {#fig-cache-performance-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm, y=0.45cm]
\draw[->] (0,0) -- (8.6,0) node[lab, right] {working-set size};
\draw[->] (0,0) -- (0,8.6) node[lab, above] {read throughput};
\foreach \x/\l in {1/16K,2.5/128K,4.5/2M,6.5/32M} { \draw (\x,-0.15) -- (\x,0.15); \node[tick] at (\x,-0.6) {\l}; }
\draw[emph, draw=primary] (0.3,8) -- (1.6,8) -- (2.0,5.6) -- (2.9,5.6) -- (3.3,3.8) -- (5.0,3.8) -- (5.6,1.2) -- (8.2,1.2);
\draw[emph, draw=accent] (0.3,5.5) -- (1.6,5.5) -- (2.0,3.4) -- (2.9,3.4) -- (3.3,2.0) -- (5.0,2.0) -- (5.6,0.5) -- (8.2,0.5);
\node[tick] at (0.95,8.5) {L1}; \node[tick] at (2.45,6.1) {L2}; \node[tick] at (4.15,4.3) {L3}; \node[tick] at (6.9,1.7) {main memory};
\node[tick, anchor=west, text=primary] at (5.7,6.5) {stride 1};
\node[tick, anchor=west, text=accent] at (5.7,5.6) {stride 8};
\end{tikzpicture}
\end{center}
```

A slice through a memory mountain (schematic): throughput falls in steps as the working set outgrows each cache level, and a larger stride lowers every step

:::

::: {#exm-matmul-loop-orders .example name="Loop orders of matrix multiplication"}

Multiply $n\times n$ matrices of `double`s, $C=AB$, with $n$ large, 32-byte blocks ($4$ doubles per block), and a cache too small to hold a row between uses. The three loops `i`, `j`, `k` can be nested in six orders, which fall into three classes by what the innermost loop touches:

| inner loop over | orders | per inner iteration | misses for $A$ | $B$ | $C$ | total |
|---|---|---|---|---|---|---|
| `k` | `ijk`, `jik` | row of $A$, column of $B$ | $0.25$ | $1$ | $0$ | $1.25$ |
| `i` | `jki`, `kji` | column of $A$, column of $C$ | $1$ | $0$ | $1$ | $2$ |
| `j` | `kij`, `ikj` | row of $B$, row of $C$ | $0$ | $0.25$ | $0.25$ | $0.5$ |

1. A row is scanned with stride $1$: one miss per block of $4$ elements, so $0.25$ misses per iteration.
2. A column is scanned with stride $n$: every element is in a different block, so $1$ miss per iteration.
3. An element that stays fixed in the inner loop (such as `C[i][j]` in the `ijk` order, kept in a register) costs nothing.

All six orders do $n^3$ multiply-adds, but the `kij` order has a quarter of the misses of the `jki` order, and on large matrices it runs many times faster.

:::

::: {#fig-cache-performance-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\newcommand{\mat}[3]{\draw[cell frame] (#1,#2) rectangle (#1+1.6,#2+1.6); \node[tick] at (#1+0.8,#2+1.85) {#3};}
\mat{0}{0}{$C$} \mat{2.2}{0}{$A$} \mat{4.4}{0}{$B$}
\node[lab] at (1.9,0.8) {$=$}; \node[lab] at (4.1,0.8) {$\times$};
\draw[hl] (2.2,1.0) -- (3.8,1.0); \draw[->, draw=accent] (2.3,0.75) -- (3.7,0.75);
\draw[hl] (5.4,0) -- (5.4,1.6); \draw[->, draw=accent] (5.65,1.5) -- (5.65,0.1);
\node[dot] at (1.0,1.0) {};
\node[tick] at (2.7,-0.6) {\texttt{ijk}: row of $A$ (stride 1), column of $B$ (stride $n$)};
\end{tikzpicture}
\end{center}
```

In the `ijk` order the innermost loop walks along a row of $A$ but down a column of $B$; each step down the column touches a new cache block

:::

::: {#rmk-cache-performance-1 name="Rules for cache-friendly code"}

Make the common case, the inner loops, cache friendly: keep repeated references to a variable in a register or local (temporal locality), and access arrays with stride $1$ in the order they are stored (spatial locality). Measure, because associativity, block size and prefetching make real behaviour differ from the simple counts above; hardware *prefetchers* detect stride-$1$ scans and fetch blocks before they are requested, which makes sequential access even more favourable than the counts suggest.

:::
