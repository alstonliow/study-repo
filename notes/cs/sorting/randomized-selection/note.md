---
title: "Randomized Selection"
sources: [mit6046-6, mit6046r-4]
requires: [cs/sorting/selection, cs/sorting/quicksort]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 6 and Recitation 4, in our own wording; proofs written out in steps. Split from cs/algorithms/randomized-algorithms on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

A Las Vegas algorithm (@sec-cs-algorithms-randomized-algorithms) for selection (@def-select): partition as in quicksort (@def-quicksort), but recurse into one side only.

::: {#def-randomized-select .definition name="Randomized select"}

`rselect(S, i)`: choose a random pivot $x$, partition into $L$ and $G$, let $k=|L|+1$; return $x$ if $i=k$, `rselect(L, i)` if $i<k$, and `rselect(G, i-k)` otherwise.

:::

```{=latex}
\begin{algorithm}
\caption{rselect$(S,i)$}
\begin{algorithmic}
\INPUT A set $S$ of distinct numbers, a rank $1\le i\le|S|$
\OUTPUT The element of rank $i$ in $S$
\STATE $x\gets$ an element of $S$ chosen uniformly at random
\STATE $L\gets\{y\in S:y<x\}$; $G\gets\{y\in S:y>x\}$; $k\gets|L|+1$
\IF{$i=k$}
    \RETURN $x$
\ELSIF{$i<k$}
    \RETURN rselect$(L,i)$
\ENDIF
\RETURN rselect$(G,i-k)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-randomized-algorithms-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$6$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$9$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$4$};
\draw[hl cell] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$7$};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$1$};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$8$};
\draw[cell frame] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$3$};
\draw[cell frame] (4.400,0.000) rectangle (4.950,0.550);
\node[lab] at (4.675,0.275) {$5$};
\node[lab,tick,anchor=west] at (5.25,0.28) {$i=5$, pivot $7$, $k=7$: recurse on $L$};
\draw[cell frame] (0.000,-0.900) rectangle (0.550,-0.350);
\node[lab] at (0.275,-0.625) {$6$};
\draw[hl cell] (0.550,-0.900) rectangle (1.100,-0.350);
\node[lab] at (0.825,-0.625) {$2$};
\draw[cell frame] (1.100,-0.900) rectangle (1.650,-0.350);
\node[lab] at (1.375,-0.625) {$4$};
\draw[cell frame] (1.650,-0.900) rectangle (2.200,-0.350);
\node[lab] at (1.925,-0.625) {$1$};
\draw[cell frame] (2.200,-0.900) rectangle (2.750,-0.350);
\node[lab] at (2.475,-0.625) {$3$};
\draw[cell frame] (2.750,-0.900) rectangle (3.300,-0.350);
\node[lab] at (3.025,-0.625) {$5$};
\node[lab,tick,anchor=west] at (5.25,-0.62) {$i=5$, pivot $2$, $k=2$: recurse on $G$ with $i=3$};
\draw[cell frame] (0.000,-1.800) rectangle (0.550,-1.250);
\node[lab] at (0.275,-1.525) {$6$};
\draw[cell frame] (0.550,-1.800) rectangle (1.100,-1.250);
\node[lab] at (0.825,-1.525) {$4$};
\draw[cell frame] (1.100,-1.800) rectangle (1.650,-1.250);
\node[lab] at (1.375,-1.525) {$3$};
\draw[hl cell] (1.650,-1.800) rectangle (2.200,-1.250);
\node[lab] at (1.925,-1.525) {$5$};
\node[lab,tick,anchor=west] at (5.25,-1.52) {$i=3$, pivot $5$, $k=3$: return $x$};
\end{tikzpicture}
\end{center}
```

One run of `rselect` for the median (rank $5$) of the items of @fig-randomized-algorithms-1, with random pivots $7$, $2$ and $5$ (highlighted). Each call partitions around the pivot and recurses into one side only; the third pivot has rank $k=i$ in its call, so the answer is $5$. Unlike quicksort, only one side is ever processed.

:::

::: {#thm-randomized-select .theorem name="Randomized select is linear in expectation"}

`rselect` runs in $O(n)$ expected time.

:::

::: {.proof}

1. Call the pivot *good* if both $L$ and $G$ have at most $\frac34$ of the items; at least half of the items are good pivots (all ranks in the middle half), so a pivot is good with probability at least $\frac12$.

2. Group the recursive calls into *phases*: phase $j$ consists of the calls made while the current size is in $\bigl((\frac34)^{j+1}n,(\frac34)^jn\bigr]$. A phase ends at the latest after its first good pivot, so the expected number of calls in a phase is at most $2$ (a geometric random variable), each costing $O((\frac34)^jn)$.

3. The expected total is $O\bigl(\sum_j2(\frac34)^jn\bigr)=O(n)$.

:::
