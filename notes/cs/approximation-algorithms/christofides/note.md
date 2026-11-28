---
title: "Christofides' Algorithm for the Metric TSP"
sources: [mit6854-16]
requires: [cs/approximation-algorithms/approximation-algorithms, cs/graph-algorithms/eulerian-circuits]
aliases: [cs/algorithm-topics/christofides]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 16 (Section 2), in our own wording; the example is our own (checked by brute force over all tours); proof written out in steps. -->

In the *metric* travelling salesman problem the costs on a complete graph are symmetric and satisfy the triangle inequality $c(u,w)\le c(u,v)+c(v,w)$, and we want a cheapest tour (a cycle through every vertex once). Doubling a minimum spanning tree gives a $2$-approximation (@thm-metric-tsp-2-approx). Christofides (1976) replaces the doubling by a matching and gets $\tfrac32$. The analysis compares with the unknown optimum directly, without a relaxation.

::: {#def-christofides .definition name="Christofides' algorithm"}

1. Find a minimum spanning tree $T$ (@def-kruskal).
2. Let $O$ be the set of vertices of odd degree in $T$; find a minimum-cost perfect matching $M$ on $O$ in the complete graph on $O$.
3. $T\cup M$ (as a multigraph) has all degrees even and is connected; find an Euler tour of it (@sec-cs-graph-algorithms-eulerian-circuits).
4. *Shortcut:* visit the vertices in the order of their first appearance on the Euler tour.

:::

```{=latex}
\begin{algorithm}
\caption{Christofides' algorithm}
\begin{algorithmic}
\INPUT complete graph with metric costs $c$
\OUTPUT a tour of cost at most $\tfrac32$ times the optimum
\STATE $T\gets$ minimum spanning tree
\STATE $O\gets$ vertices of odd degree in $T$
\STATE $M\gets$ minimum-cost perfect matching on $O$
\STATE $W\gets$ Euler tour of the multigraph $T\cup M$
\RETURN the vertices in the order of their first visit on $W$
\end{algorithmic}
\end{algorithm}
```

$O$ has even size (the degrees of a graph add up to an even number), so the perfect matching exists. A minimum-cost perfect matching in a general graph can be found in polynomial time, by Edmonds' algorithm (@sec-math-combinatorial-optimization-matching-blossom-algorithm gives the unweighted version) or by the ellipsoid method over the perfect matching polytope.

::: {#thm-christofides .theorem name="Christofides"}

For metric costs, the tour returned costs at most $\tfrac32\,\mathrm{OPT}$.

:::

::: {.proof}

1. *Tree.* Deleting an edge from an optimal tour gives a spanning tree, so $c(T)\le\mathrm{OPT}$.

2. *Matching.* Shortcut an optimal tour to visit only the vertices of $O$, in the same cyclic order; by the triangle inequality the resulting cycle costs at most $\mathrm{OPT}$. It has $|O|$ edges, $|O|$ even, so its edges split alternately into two perfect matchings on $O$, and the cheaper has cost at most $\mathrm{OPT}/2$. Hence $c(M)\le\mathrm{OPT}/2$.

3. *Euler tour.* Every vertex of $T\cup M$ has even degree (odd vertices of $T$ get one matching edge), and the multigraph is connected, so an Euler tour exists; it costs $c(T)+c(M)\le\tfrac32\mathrm{OPT}$.

4. *Shortcutting.* Each skipped stretch $u,\dots,w$ is replaced by the edge $uw$, which costs no more by the triangle inequality. So the final tour costs at most $\tfrac32\mathrm{OPT}$.

:::

::: {#exm-christofides .example name="Six points on a line and a square"}

Take the points $a=(0,0)$, $b=(2,0)$, $c=(4,0)$, $d=(4,2)$, $e=(2,2)$, $f=(0,2)$ with Euclidean distances (the boundary of a $4\times2$ rectangle with midpoints on the long sides). A minimum spanning tree is the path $a\,b\,c\,d\,e\,f$ of cost $10$; its odd vertices are $a$ and $f$, matched by the edge $af$ of cost $2$. The Euler tour of $T\cup M$ is the cycle $a\,b\,c\,d\,e\,f\,a$ itself, of cost $12$, which is optimal here (the perimeter).

:::

::: {#fig-christofides-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\node[small vertex] (ca) at (0.00,0.00) {$a$};
\node[small vertex] (cb) at (1.60,0.00) {$b$};
\node[small vertex] (cc) at (3.20,0.00) {$c$};
\node[small vertex] (cd) at (3.20,1.60) {$d$};
\node[small vertex] (ce) at (1.60,1.60) {$e$};
\node[small vertex] (cf) at (0.00,1.60) {$f$};
\draw[emph] (ca)--(cb);
\draw[emph] (cb)--(cc);
\draw[emph] (cc)--(cd);
\draw[emph] (cd)--(ce);
\draw[emph] (ce)--(cf);
\draw[hl] (ca)--(cf);
\draw[faint, dashed] (cb)--(ce);
\end{tikzpicture}
\end{center}
```

The minimum spanning tree (thick) has odd vertices $a$ and $f$; adding the matching edge $af$ (highlighted) makes every degree even, and the Euler tour is the optimal tour around the rectangle. The dashed edge $be$ is another tree edge of the same length.

:::

::: {#rmk-christofides-1 .remark name="Tightness and later progress"}

The factor $\tfrac32$ is tight for the algorithm: there are instances where it returns a tour of cost close to $\tfrac32\mathrm{OPT}$. Metric TSP is MAX-SNP-hard even with all distances $1$ or $2$, and approximating it within some constant above $1$ is NP-hard. For decades $\tfrac32$ was the best known guarantee; in 2020 Karlin, Klein and Oveis Gharan improved it by a tiny constant. For Euclidean distances there is a PTAS (Arora, Mitchell).

:::
