---
title: "Locality of Reference"
sources: [cmu15213-11, cmu15213r-7]
requires: [cs/machine-level/arrays-and-structs]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 11 "The Memory Hierarchy" and Recitation 7, in our own wording. -->

::: {#def-locality .definition name="Temporal and spatial locality"}

A program has *temporal locality* if a location it referenced recently is likely to be referenced again soon, and *spatial locality* if, after referencing a location, it is likely to reference nearby locations soon. Both apply to data and to instructions.

:::

::: {#exm-sum-locality .example name="Locality of a summing loop"}

```c
int sum = 0;
for (int i = 0; i < n; i++)
    sum += a[i];
return sum;
```

- Data: `sum` is referenced in every iteration (temporal); `a[0], a[1], …` are referenced in order of their addresses (spatial).
- Instructions: the loop body runs again and again (temporal) and its instructions are executed in sequence (spatial).

:::

::: {#def-stride-pattern .definition name="Stride-$k$ reference pattern"}

A sequence of references to the elements of an array has *stride* $k$ if successive references are $k$ elements apart. Stride $1$ (*sequential* access) has the best spatial locality; spatial locality decreases as the stride grows.

:::

::: {#exm-row-column-order .example name="Row-major versus column-major traversal"}

```c
int sum_rows(int a[M][N]) {          int sum_cols(int a[M][N]) {
    int sum = 0;                         int sum = 0;
    for (int i = 0; i < M; i++)          for (int j = 0; j < N; j++)
        for (int j = 0; j < N; j++)          for (int i = 0; i < M; i++)
            sum += a[i][j];                      sum += a[i][j];
    return sum;                          return sum;
}                                    }
```

Both compute the same sum. C stores `a` row by row (@def-array-layout), so `sum_rows` visits addresses with stride $1$ while `sum_cols` jumps $N$ elements between consecutive references. For large arrays `sum_cols` is several times slower.

:::

::: {#fig-locality-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r in {0,1,2} { \foreach \c in {0,...,3} { \draw[cell frame] (\c*0.7,-\r*0.6) rectangle (\c*0.7+0.7,-\r*0.6+0.55); } }
\draw[->, draw=primary, emph] (0.2,0.27) -- (2.6,0.27);
\draw[->, draw=primary, emph] (0.2,-0.33) -- (2.6,-0.33);
\draw[->, draw=primary, emph] (0.2,-0.93) -- (2.6,-0.93);
\node[lab] at (1.4,1.0) {\texttt{sum\_rows}: stride 1};
\foreach \r in {0,1,2} { \foreach \c in {0,...,3} { \draw[cell frame] (4.5+\c*0.7,-\r*0.6) rectangle (4.5+\c*0.7+0.7,-\r*0.6+0.55); } }
\foreach \c in {0,...,3} { \draw[->, draw=accent, emph] (4.85+\c*0.7,0.45) -- (4.85+\c*0.7,-1.05); }
\node[lab] at (5.9,1.0) {\texttt{sum\_cols}: stride $N$};
\foreach \k in {0,...,11} { \pgfmathtruncatemacro{\r}{\k/4} \pgfmathtruncatemacro{\c}{mod(\k,4)} \draw[cell frame] (\k*0.62,-2.4) rectangle (\k*0.62+0.62,-1.95); \node[tick] at (\k*0.62+0.31,-2.18) {\r,\c}; }
\node[tick, anchor=west] at (7.5,-2.18) {memory order};
\draw[->, draw=accent] (0.31,-2.5) to[bend right=25] (4*0.62+0.31,-2.5);
\draw[->, draw=accent] (4*0.62+0.31,-2.5) to[bend right=25] (8*0.62+0.31,-2.5);
\end{tikzpicture}
\end{center}
```

The same $3\times4$ array traversed row by row (consecutive addresses) and column by column (jumps of $N=4$ elements in memory)

:::

::: {#rmk-locality-1 name="Locality as a habit"}

Two rules of thumb give good locality: reuse a variable many times once it has been brought in (temporal), and walk through arrays in the order they are stored (spatial). The cache notes that follow quantify both, for example in the miss rates of the loop orders of matrix multiplication (@exm-matmul-loop-orders).

:::
