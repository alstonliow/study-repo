---
title: "Selection in Linear Time: Median of Medians"
sources: [mit6046-2, mit6046r-1]
requires: [cs/sorting/selection, cs/algorithms/divide-and-conquer]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 2 and Recitation 1, in our own wording; proofs written out in steps. Split from cs/algorithms/divide-and-conquer on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

A deterministic divide-and-conquer algorithm for selection (@def-select) in $O(n)$ worst-case time.

::: {#def-median-of-medians .definition name="Median of medians"}

`select(S, i)`:

1. split $S$ into groups of $5$ and find the median of each group;
2. recursively find the median $x$ of these $\lceil n/5\rceil$ medians;
3. partition $S$ into $B=\{y<x\}$ and $C=\{y>x\}$, and let $k=|B|+1$ be the rank of $x$;
4. if $i=k$ return $x$; if $i<k$ return `select(B, i)`; otherwise return `select(C, i-k)`.

:::

```{=latex}
\begin{algorithm}
\caption{Median of medians: select$(S,i)$}
\begin{algorithmic}
\INPUT A set $S$ of $n$ distinct numbers, a rank $1\le i\le n$
\OUTPUT The element of rank $i$ in $S$
\IF{$n\le5$}
    \RETURN the element of rank $i$, by sorting
\ENDIF
\STATE split $S$ into groups of $5$; $M\gets$ the medians of the groups
\STATE $x\gets$ select$(M,\lceil|M|/2\rceil)$ \COMMENT{the median of the medians}
\STATE $B\gets\{y\in S:y<x\}$; $C\gets\{y\in S:y>x\}$; $k\gets|B|+1$
\IF{$i=k$}
    \RETURN $x$
\ELSIF{$i<k$}
    \RETURN select$(B,i)$
\ENDIF
\RETURN select$(C,i-k)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-divide-and-conquer-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0.0) rectangle (0.6,0.5);
\node[lab, lbl bold] at (0.3,0.25) {5};
\draw[cell frame] (0.0,-0.62) rectangle (0.6,-0.12);
\node[lab, lbl bold] at (0.3,-0.37) {8};
\draw[cell frame] (0.0,-1.24) rectangle (0.6,-0.74);
\node[lab, lbl bold] at (0.3,-0.99) {12};
\draw[cell frame] (0.0,-1.86) rectangle (0.6,-1.36);
\node[lab] at (0.3,-1.61) {28};
\draw[cell frame] (0.0,-2.48) rectangle (0.6,-1.98);
\node[lab] at (0.3,-2.23) {65};
\draw[cell frame] (0.75,0.0) rectangle (1.35,0.5);
\node[lab, lbl bold] at (1.05,0.25) {7};
\draw[cell frame] (0.75,-0.62) rectangle (1.35,-0.12);
\node[lab, lbl bold] at (1.05,-0.37) {20};
\draw[cell frame] (0.75,-1.24) rectangle (1.35,-0.74);
\node[lab, lbl bold] at (1.05,-0.99) {42};
\draw[cell frame] (0.75,-1.86) rectangle (1.35,-1.36);
\node[lab] at (1.05,-1.61) {51};
\draw[cell frame] (0.75,-2.48) rectangle (1.35,-1.98);
\node[lab] at (1.05,-2.23) {84};
\draw[cell frame] (1.5,0.0) rectangle (2.1,0.5);
\node[lab, lbl bold] at (1.8,0.25) {10};
\draw[cell frame] (1.5,-0.62) rectangle (2.1,-0.12);
\node[lab, lbl bold] at (1.8,-0.37) {13};
\draw[hl cell] (1.5,-1.24) rectangle (2.1,-0.74);
\node[lab] at (1.8,-0.99) {47};
\draw[cell frame] (1.5,-1.86) rectangle (2.1,-1.36);
\node[lab, lbl bold] at (1.8,-1.61) {69};
\draw[cell frame] (1.5,-2.48) rectangle (2.1,-1.98);
\node[lab, lbl bold] at (1.8,-2.23) {75};
\draw[cell frame] (2.25,0.0) rectangle (2.85,0.5);
\node[lab] at (2.55,0.25) {9};
\draw[cell frame] (2.25,-0.62) rectangle (2.85,-0.12);
\node[lab] at (2.55,-0.37) {31};
\draw[cell frame] (2.25,-1.24) rectangle (2.85,-0.74);
\node[lab, lbl bold] at (2.55,-0.99) {54};
\draw[cell frame] (2.25,-1.86) rectangle (2.85,-1.36);
\node[lab, lbl bold] at (2.55,-1.61) {56};
\draw[cell frame] (2.25,-2.48) rectangle (2.85,-1.98);
\node[lab, lbl bold] at (2.55,-2.23) {85};
\draw[cell frame] (3.0,0.0) rectangle (3.6,0.5);
\node[lab] at (3.3,0.25) {16};
\draw[cell frame] (3.0,-0.62) rectangle (3.6,-0.12);
\node[lab] at (3.3,-0.37) {55};
\draw[cell frame] (3.0,-1.24) rectangle (3.6,-0.74);
\node[lab, lbl bold] at (3.3,-0.99) {71};
\draw[cell frame] (3.0,-1.86) rectangle (3.6,-1.36);
\node[lab, lbl bold] at (3.3,-1.61) {73};
\draw[cell frame] (3.0,-2.48) rectangle (3.6,-1.98);
\node[lab, lbl bold] at (3.3,-2.23) {89};
\node[lab,tick, anchor=west] at (3.9,0.25) {groups of $5$, each sorted;};
\node[lab,tick, anchor=west] at (3.9,-0.25) {columns sorted by median;};
\node[lab,tick, anchor=west] at (3.9,-0.75) {$x=47$ is the median of medians:};
\node[lab,tick, anchor=west] at (3.9,-1.25) {bold items are $\le x$ (top left)};
\node[lab,tick, anchor=west] at (3.9,-1.75) {or $\ge x$ (bottom right)};
\end{tikzpicture}
\end{center}
```

Median of medians on $25$ numbers. Each column is a group of $5$ in increasing order, and the columns are ordered by their medians. Everything above and to the left of $x$ is at most $x$, and everything below and to the right is at least $x$: about $\frac3{10}$ of the items on each side, so the recursion discards at least that many.

:::

::: {#thm-median-of-medians .theorem name="Selection in linear time"}

The median-of-medians algorithm runs in $O(n)$ time.

:::

::: {.proof}

1. Half of the $\lceil n/5\rceil$ groups have a median at least $x$, and in each such group (except possibly $x$'s own and a last incomplete one) at least $3$ elements are at least $x$. So at least $3\bigl(\frac12\lceil n/5\rceil-2\bigr)\ge\frac{3n}{10}-6$ elements are at least $x$, and symmetrically at least $\frac{3n}{10}-6$ are at most $x$.

2. Hence each of $B$ and $C$ has at most $\frac{7n}{10}+6$ elements, and $T(n)\le T(\lceil n/5\rceil)+T(\frac{7n}{10}+6)+O(n)$.

3. Guess $T(n)\le cn$. The right side is at most $c(\frac n5+1)+c(\frac{7n}{10}+6)+an=cn-\bigl(\frac{cn}{10}-7c-an\bigr)$, which is at most $cn$ for $c\ge20a$ and $n\ge140$; smaller $n$ are handled by a large enough $c$. So $T(n)=O(n)$. The key fact is $\frac15+\frac7{10}<1$.

:::
