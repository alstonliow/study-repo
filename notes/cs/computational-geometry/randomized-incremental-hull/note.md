---
title: "Convex Hulls in Higher Dimensions: Randomized Incremental Construction"
sources: [mit6854-22]
requires: [cs/computational-geometry/seidel-lp, cs/computational-geometry/graham-scan]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 22 (Section 2), in our own wording; the example is our own (checked by computation); proofs written out in steps. -->

In the plane a convex hull is a cyclic list of vertices, found in $O(n\log n)$ (@def-graham-scan). In $\mathbb R^d$ the hull of $n$ points can have $\Theta(n^{\lfloor d/2\rfloor})$ facets (the *upper bound theorem*), so any algorithm that lists them needs that much time. Seidel's randomized incremental algorithm runs in expected $O(n^2+n^{\lfloor d/2\rfloor})$, which is optimal for $d\ge4$ and simpler than the optimal $O(n\log n+n^{\lfloor d/2\rfloor})$ algorithms of Clarkson–Shor (randomized) and Chazelle (deterministic).

## What is computed

Assume *general position*: no $d+1$ of the points lie on a hyperplane (perturb otherwise). Then every facet of the hull $P$ is a $(d-1)$-simplex spanned by $d$ of the points, and $P$ is a *simplicial* polytope. A *ridge* is a $(d-2)$-face; each ridge lies in exactly two facets (@def-polyhedron-face).

::: {#def-facet-graph .definition name="Facet graph"}

The *facet graph* $\mathcal F(P)$ has a node for every facet of $P$ and an edge for every ridge, joining the two facets that contain it. The algorithm outputs $\mathcal F(P)$, each facet with its $d$ vertices and outward normal.

:::

::: {#def-visible-facet .definition name="Visible facet, horizon ridge"}

A facet $F$ of $P$ is *visible* from a point $x$ if the hyperplane of $F$ separates $x$ from $P$, and *obscured* otherwise. A ridge is a *horizon ridge* if exactly one of its two facets is visible.

:::

::: {#prp-hull-update .proposition name="Adding a point"}

Let $P'=\operatorname{conv}(P\cup\{x\})$ with $x\notin P$. The facets of $P'$ are the obscured facets of $P$ together with the cones $\operatorname{conv}(R\cup\{x\})$ over the horizon ridges $R$. In particular the visible facets form a connected subgraph of $\mathcal F(P)$, bounded by the horizon ridges.

:::

::: {.proof}

1. An obscured facet's hyperplane has $P$ and $x$ on the same side, so it still supports $P'$ and the facet remains a facet.

2. A visible facet's hyperplane has $x$ strictly outside, so $x$ lies beyond it and the facet is not on the boundary of $P'$.

3. For a horizon ridge $R$, between a visible facet $F_1$ and an obscured facet $F_2$, rotate the hyperplane of $F_2$ about $R$ towards $F_1$ until it passes through $x$; this hyperplane supports $P'$ and meets it exactly in $\operatorname{conv}(R\cup\{x\})$. Every new facet contains $x$ and a ridge of $P$ on its boundary, and that ridge must be a horizon ridge.

4. The set of points $y$ seen from $x$ through visible facets is a topological disk on the boundary of $P$ (the part of the boundary illuminated by a light at $x$), so the visible facets are connected.

:::

::: {#fig-randomized-incremental-hull-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[emph] (0,0)--(2,-0.5);
\draw[hl] (2,-0.5)--(3.2,0.6);
\draw[hl] (3.2,0.6)--(2.6,2);
\draw[emph] (2.6,2)--(0.8,2.2);
\draw[emph] (0.8,2.2)--(-0.4,1.2);
\draw[emph] (-0.4,1.2)--(0,0);
\node[dot] at (0,0) {};
\node[dot] at (2,-0.5) {};
\node[dot] at (3.2,0.6) {};
\node[dot] at (2.6,2) {};
\node[dot] at (0.8,2.2) {};
\node[dot] at (-0.4,1.2) {};
\node[hl dot] at (4.4, 1.6) {};
\node[lab, right] at (4.4, 1.6) {$x_i$};
\draw[faint, dashed] (2,-0.5)--(4.4,1.6)--(2.6,2);
\end{tikzpicture}
\end{center}
```

The update in the plane, where facets are edges and ridges are vertices: the edges visible from $x_i$ (highlighted) are deleted, and the two horizon vertices are joined to $x_i$ (dashed) to form the new facets.

:::

## The algorithm

::: {#def-randomized-incremental-hull .definition name="Randomized incremental hull (Seidel)"}

Put the points in random order $x_1,\dots,x_n$ and let $P_i=\operatorname{conv}\{x_1,\dots,x_i\}$. $P_{d+1}$ is a simplex, whose facet graph is complete on $d+1$ nodes. For $i=d+2,\dots,n$:

1. find one facet of $P_{i-1}$ visible from $x_i$, or decide that $x_i\in P_{i-1}$ and skip it; this is a linear program in $d+1$ unknowns (a hyperplane through $x_i$ with all $x_j$, $j<i$, on one side), solved by @def-seidel-lp in $O(d!\,i)$ expected time;
2. by depth-first search from it in $\mathcal F(P_{i-1})$, find all visible facets and the horizon ridges, and delete the visible facets;
3. create a new facet $\operatorname{conv}(R\cup\{x_i\})$ for every horizon ridge $R$, adjacent across $R$ to the obscured facet;
4. join the new facets to each other: each has $d-1$ new ridges containing $x_i$; sort all of them (as sorted lists of point indices, by radix sort) and pair up equal ones.

:::

```{=latex}
\begin{algorithm}
\caption{Randomized incremental convex hull in $\mathbb R^d$}
\begin{algorithmic}
\INPUT points $x_1,\dots,x_n\in\mathbb R^d$ in general position
\OUTPUT the facet graph of $\operatorname{conv}\{x_1,\dots,x_n\}$
\STATE randomly permute the points
\STATE $\mathcal F\gets$ facet graph of the simplex on $x_1,\dots,x_{d+1}$
\FOR{$i=d+2$ \TO $n$}
\STATE find a facet visible from $x_i$ by linear programming; if none, \textbf{continue}
\STATE DFS from it: collect visible facets $V$ and horizon ridges $H$
\STATE delete $V$ from $\mathcal F$
\FORALL{$R\in H$}
\STATE add facet $\operatorname{conv}(R\cup\{x_i\})$, adjacent across $R$ to the obscured facet of $R$
\ENDFOR
\STATE match the new ridges through $x_i$ by radix sort
\ENDFOR
\RETURN $\mathcal F$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-randomized-incremental-hull .theorem name="Running time"}

Let $N_i$ be the number of facets created at step $i$. The expected running time is $O\big(\sum_i(i+\mathbb E[N_i])\big)$ for fixed $d$, and
$$\mathbb E[N_i]\le\frac di\,O\big(i^{\lfloor d/2\rfloor}\big).$$
Summed over $i$ this gives $O(n^2+n^{\lfloor d/2\rfloor})$.

:::

::: {.proof}

1. *Cost of a step.* Step 1 costs $O(i)$ for fixed $d$. Steps 2–4 cost $O(N_i)$ plus the number of deleted facets; a facet is deleted at most once, so deletions are paid for by creations.

2. *Backward analysis.* The facets created at step $i$ are exactly the facets of $P_i$ that contain $x_i$. Fix the set $\{x_1,\dots,x_i\}$; then $x_i$ is a uniformly random one of its $i$ points. Each facet of $P_i$ has $d$ vertices, so it contains $x_i$ with probability $d/i$.

3. $P_i$ has $O(i^{\lfloor d/2\rfloor})$ facets by the upper bound theorem, so $\mathbb E[N_i]\le\frac di\,O(i^{\lfloor d/2\rfloor})$.

4. Adding over $i$ gives the bound; the details are an exercise.

:::

::: {#exm-randomized-incremental-hull .example name="Adding a point to a tetrahedron"}

In $\mathbb R^3$ take the tetrahedron on $(0,0,0)$, $(1,0,0)$, $(0,1,0)$, $(0,0,1)$ and add $x=(1,1,1)$. Only the facet on the plane $x_1+x_2+x_3=1$ is visible from $x$; its three edges are the horizon ridges. Deleting it and adding the three triangles joining $x$ to these edges gives a hull with $3+3=6$ facets, each new facet adjacent to one old facet and to the two other new ones.

:::

::: {#rmk-randomized-incremental-hull-1 .remark name="Dimensions two and three"}

For $d=2,3$ the $O(n^2)$ term comes from step 1. Keeping, for every point not yet inserted, a pointer to one facet it sees (a *conflict list*) replaces the linear programs and gives the optimal expected $O(n\log n)$ (Clarkson–Shor).

:::
