---
title: "Quicksort"
sources: [mit6046-6, mit6046r-4]
requires: [cs/sorting/comparison-sorting, cs/algorithms/randomized-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 6 and Recitation 4, in our own wording; proofs written out in steps. Split from cs/algorithms/randomized-algorithms on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

::: {#def-quicksort .definition name="Quicksort"}

*Quicksort* of an array of distinct items: if it has at most one item, stop. Otherwise choose a *pivot* $x$, partition the other items into $L=\{y<x\}$ and $G=\{y>x\}$ in $O(n)$ time, and sort $L$ and $G$ recursively. In *randomized quicksort* the pivot is chosen uniformly at random among the current items.

:::

```{=latex}
\begin{algorithm}
\caption{Randomized quicksort}
\begin{algorithmic}
\INPUT An array $S$ of distinct items
\OUTPUT $S$ sorted
\IF{$|S|\le1$}
    \RETURN $S$
\ENDIF
\STATE $x\gets$ an item of $S$ chosen uniformly at random
\STATE $L\gets\{y\in S:y<x\}$; $G\gets\{y\in S:y>x\}$
\RETURN quicksort$(L)$, then $x$, then quicksort$(G)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-randomized-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (q0) at (5.50,0.00) {6 2 9 \textbf{4} 7 1 8 3 5};
\node[box] (q1) at (2.75,-0.95) {\textbf{2} 1 3};
\node[box] (q2) at (1.38,-1.90) {1};
\draw (q1) -- (q2);
\node[box] (q3) at (4.12,-1.90) {3};
\draw (q1) -- (q3);
\draw (q0) -- (q1);
\node[box] (q4) at (8.25,-0.95) {6 9 \textbf{7} 8 5};
\node[box] (q5) at (6.88,-1.90) {\textbf{6} 5};
\node[box] (q6) at (6.19,-2.85) {5};
\draw (q5) -- (q6);
\draw (q4) -- (q5);
\node[box] (q7) at (9.62,-1.90) {9 \textbf{8}};
\node[box] (q8) at (10.31,-2.85) {9};
\draw (q7) -- (q8);
\draw (q4) -- (q7);
\draw (q0) -- (q4);
\end{tikzpicture}
\end{center}
```

One run of randomized quicksort on $6,2,9,4,7,1,8,3,5$; the pivot of each call is in bold. Two items are compared only if one of them is a pivot while both are in the same call: $1$ and $9$ are never compared, because the pivot $4$ separates them first.

:::

With a fixed pivot rule (such as the first item), a sorted input gives $T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$. Choosing the median as pivot (@thm-median-of-medians) gives $\Theta(n\log n)$ in the worst case but with large constants. A random pivot is simple and fast in expectation, for every input.

::: {#thm-randomized-quicksort .theorem name="Randomized quicksort"}

Randomized quicksort makes at most $2n\ln n$ comparisons in expectation on any input of $n$ distinct items. So it runs in $O(n\log n)$ expected time.

:::

::: {.proof}

1. Let $z_1<\dots<z_n$ be the items in sorted order and $X_{ij}$ the indicator that $z_i$ and $z_j$ are ever compared ($i<j$). Two items are compared only when one of them is the pivot, and never again afterwards, so the number of comparisons is $X=\sum_{i<j}X_{ij}$.

2. Consider the items $Z_{ij}=\{z_i,\dots,z_j\}$. They stay together in one subarray until the first time a pivot is chosen from $Z_{ij}$. If that pivot is $z_i$ or $z_j$, they are compared; if it is strictly between, they are separated and never compared.

3. Each item of $Z_{ij}$ is equally likely to be that first pivot, so $\Pr(X_{ij}=1)=\frac2{j-i+1}$.

4. By linearity (@thm-linearity-of-expectation),
   $$E[X]=\sum_{i<j}\frac2{j-i+1}\le\sum_{i=1}^n\sum_{k=2}^{n}\frac2k<2nH_n\le2n(1+\ln n),$$
   using @cor-harmonic-bounds. (A slightly more careful count gives at most $2n\ln n$.)

:::
