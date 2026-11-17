---
title: "Approximation Algorithms"
sources: [mit6046-17, mit6046r-9]
requires: [cs/theory/np-complete-reductions]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 17 and Recitation 9, in our own wording; proofs written out in steps. -->

When an optimisation problem is NP-hard, we may settle for a solution that is provably close to optimal, found in polynomial time.

::: {#def-approximation-ratio .definition name="Approximation ratio, PTAS"}

An algorithm for an optimisation problem has *approximation ratio* $\rho(n)\ge1$ if on every input of size $n$ its solution's cost $C$ and the optimal cost $C^*$ satisfy $\max\{C/C^*,\,C^*/C\}\le\rho(n)$. A *polynomial-time approximation scheme* (PTAS) takes an extra parameter $\varepsilon>0$ and has ratio $1+\varepsilon$, running in time polynomial in $n$ for each fixed $\varepsilon$; it is *fully polynomial* (FPTAS) if the time is polynomial in $n$ and $1/\varepsilon$.

:::

## Vertex cover

::: {#thm-vertex-cover-2-approx .theorem name="A 2-approximation for vertex cover"}

Repeatedly pick any remaining edge $\{u,v\}$, put *both* $u$ and $v$ into the cover, and delete every edge touching $u$ or $v$. The result is a vertex cover at most twice the minimum size, found in $O(|V|+|E|)$ time.

:::

::: {.proof}

1. Every edge is deleted only when one of its ends enters the cover, so the result is a cover.

2. The picked edges share no endpoints (their endpoints were deleted with them), so they form a matching $M$, and the cover has $2|M|$ vertices.

3. Any vertex cover contains an end of each edge of $M$, and these ends are distinct, so $C^*\ge|M|$. Hence $C=2|M|\le2C^*$.

:::

::: {#fig-approximation-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight, draw=accent] (a) at (0,1) {$a$};
\node[small vertex, fill=accentLight, draw=accent] (b) at (1.5,1) {$b$};
\node[small vertex, fill=accentLight, draw=accent] (c) at (3,1) {$c$};
\node[small vertex, fill=accentLight, draw=accent] (d) at (0,-0.3) {$d$};
\node[small vertex, fill=accentLight, draw=accent] (e) at (1.5,-0.3) {$e$};
\node[small vertex, fill=accentLight, draw=accent] (f) at (3,-0.3) {$f$};
\draw[hl] (a) -- (b);
\draw[] (b) -- (c);
\draw[] (a) -- (d);
\draw[] (b) -- (e);
\draw[hl] (c) -- (f);
\draw[hl] (d) -- (e);
\draw[] (e) -- (f);
\end{tikzpicture}
\end{center}
```

The $2$-approximation for vertex cover: the highlighted edges were picked (a matching), and both ends of each joined the cover, 6 vertices in all. Any cover needs one end of each picked edge, so at least 3; the smallest cover here, $\{b,d,f\}$, has $3$.

:::

Greedily taking a vertex of largest degree sounds better but has ratio $\Theta(\log n)$ on some graphs.

## Set cover

::: {#thm-set-cover-greedy .theorem name="Greedy set cover"}

Given sets $S_1,\dots,S_m$ whose union is a set $X$ of $n$ elements, repeatedly choose a set covering the most still-uncovered elements. If an optimal cover uses $t$ sets, the greedy cover uses at most $t\lceil\ln n\rceil+1$; so the ratio is $O(\ln n)$.

:::

::: {.proof}

1. Let $X_k$ be the uncovered elements after $k$ greedy steps, $X_0=X$. The $t$ optimal sets cover $X_k$, so one of them covers at least $|X_k|/t$ of its elements, and greedy covers at least that many: $|X_{k+1}|\le(1-\frac1t)|X_k|$.

2. Hence $|X_k|\le(1-\frac1t)^kn\le e^{-k/t}n$, using $1-y\le e^{-y}$.

3. For $k=t\lceil\ln n\rceil$ this is at most $1$, so at most one more step is needed.

:::

## Travelling salesman with the triangle inequality

::: {#thm-metric-tsp-2-approx .theorem name="TSP via spanning trees"}

On a complete graph whose costs satisfy the triangle inequality $c(u,w)\le c(u,v)+c(v,w)$, the following tour costs at most twice the optimum: find a minimum spanning tree $T$, walk around it (depth-first, visiting every edge twice), and visit the vertices in the order of their first appearance on this walk.

:::

::: {.proof}

1. Deleting one edge of an optimal tour leaves a spanning tree, so $c(T)\le C^*$.

2. The full walk around $T$ costs $2c(T)$.

3. Skipping repeated vertices replaces a part of the walk by a direct edge, which by the triangle inequality is no more expensive. So the tour costs at most $2c(T)\le2C^*$.

:::

(Christofides' algorithm improves the ratio to $\frac32$ by adding a minimum matching on the odd-degree vertices of $T$.)

## Partition: an approximation scheme

::: {#prp-partition-ptas .proposition name="A PTAS for partition"}

To split numbers $s_1\ge s_2\ge\dots\ge s_n$ into two parts minimising the larger part sum, fix $m$: find the best split of the $m$ largest numbers by trying all $2^m$ splits, then add the remaining numbers one at a time, each to the currently smaller part. With $m=\lceil2/\varepsilon\rceil-1$ the ratio is at most $1+\varepsilon$, in time $O(2^{2/\varepsilon}+n\log n)$.

:::

::: {.proof}

1. Let $L=\frac12\sum_is_i$, so $C^*\ge L$. If the larger part never receives a greedy number after the first phase, its sum is optimal for the $m$ largest numbers, hence at most $C^*$.

2. Otherwise let $s_k$ ($k>m$) be the last number added to the larger part. Before that the part was the smaller one, so its sum was at most $L$, and $C\le L+s_k$.

3. The $m+1$ numbers $s_1,\dots,s_m,s_k$ are all at least $s_k$, so $2L\ge(m+1)s_k$, that is $s_k\le\frac{2L}{m+1}$.

4. Then $\frac C{C^*}\le\frac{L+s_k}L\le1+\frac2{m+1}$. With $m+1=\lceil2/\varepsilon\rceil$ this is at most $1+\varepsilon$.

:::
