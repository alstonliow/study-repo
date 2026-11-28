---
title: "Maximum Cut: Local Search, Random Cuts and the Goemans–Williamson Algorithm"
sources: [mit6854-18, mit6854-19]
requires: [cs/approximation-algorithms/lp-rounding-and-primal-dual, math/optimization/convex-problems/semidefinite-programs]
aliases: [cs/algorithm-topics/max-cut]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 18 and Lecture 19 (Sections 1-3), in our own wording; the constant 0.87856 and the 5-cycle values were checked numerically; proofs written out in steps. One note for the problem and its approximation algorithms (tiny algorithms plus the main one, SPEC §8.6). -->

Given a graph $G=(V,E)$ with weights $w\ge0$, the *maximum cut* problem asks for $S\subseteq V$ maximising $w(\delta(S))$, the weight of the edges with one end in $S$. Minimum cut is polynomial (@prp-global-cut-by-flows), but maximum cut is NP-hard. Four ideas give successively better guarantees.

## Ratio one half

::: {#prp-max-cut-local-search .proposition name="Local search"}

Call $S$ *locally optimal* if moving one vertex to the other side does not increase the cut. Then $w(\delta(S))\ge\tfrac12w(E)\ge\tfrac12\mathrm{OPT}$.

:::

::: {.proof}

1. For a vertex $i$, let $C_i$ be its edges in the cut and $A_i$ its other edges. Moving $i$ changes the cut by $w(A_i)-w(C_i)\le0$, so $w(C_i)\ge w(A_i)$.

2. Summing over $i$ counts every edge twice: $2w(\delta(S))\ge2\big(w(E)-w(\delta(S))\big)$, so $w(\delta(S))\ge\tfrac12w(E)$.

:::

The bound is tight for this neighbourhood: on a cycle of length divisible by $4$, placing the vertices in the pattern $S,S,\bar S,\bar S,\dots$ cuts every other edge, and no single move helps, although the whole cycle can be cut. Local search may also take exponentially many steps; maximum cut with this neighbourhood is PLS-complete.

::: {#prp-max-cut-random .proposition name="Random cut and its derandomisation"}

Putting each vertex in $S$ independently with probability $\tfrac12$ gives $\mathbb E\,w(\delta(S))=\tfrac12w(E)$. Deciding the vertices one by one, each on the side that maximises the conditional expectation, gives deterministically a cut of weight at least $\tfrac12w(E)$; this is the greedy rule "put $v_i$ opposite to the heavier part of its edges to $v_1,\dots,v_{i-1}$".

:::

::: {.proof}

1. An edge is cut with probability $\tfrac12$; add over the edges (linearity of expectation).

2. $\mathbb E[X]=\tfrac12\mathbb E[X\mid v_i\in S]+\tfrac12\mathbb E[X\mid v_i\notin S]$ (conditioned on the earlier choices), so one of the two choices does not lower the conditional expectation. After all $n$ choices the expectation is the weight of a fixed cut.

3. Given the earlier choices, the only edges whose status depends on $v_i$ and is not yet random go to $v_1,\dots,v_{i-1}$; the rest are cut with probability $\tfrac12$ either way. So the better choice is the greedy one.

:::

A linear programming relaxation does not help: with variables $x_e$ and the *cycle inequalities* (a cut meets every cycle in an even number of edges) the LP can be solved in polynomial time and is exact on planar graphs, but on some graphs its value is almost twice the optimum.

## The semidefinite relaxation

With $y_i=\pm1$ for the side of $i$, an edge $ij$ is cut exactly when $y_iy_j=-1$, so
$$\mathrm{OPT}=\max\Big\{\sum_{ij\in E}w_{ij}\frac{1-y_iy_j}2:y\in\{\pm1\}^V\Big\}=\max\Big\{\tfrac14\,y^{\mathsf T}Ly:y\in\{\pm1\}^V\Big\},$$
$L$ being the weighted Laplacian. Replace each $y_i$ by a unit vector $v_i\in\mathbb R^n$:
$$\mathrm{SDP}=\max\Big\{\sum_{ij\in E}w_{ij}\frac{1-v_i^{\mathsf T}v_j}2:\lVert v_i\rVert=1\Big\}=\max\Big\{\tfrac14L\bullet Y:Y_{ii}=1,\ Y\succeq0\Big\},$$
the second form with $Y_{ij}=v_i^{\mathsf T}v_j$ (a positive semidefinite $Y$ is a Gram matrix). Taking all $v_i$ equal to $\pm e_1$ shows $\mathrm{SDP}\ge\mathrm{OPT}$. Both the program and its dual are strictly feasible, so it can be solved to any accuracy (@def-primal-dual-ipm). Restricting the dual to a multiple of the identity shows $\mathrm{SDP}\le\tfrac n4\lambda_{\max}(L)$, the older eigenvalue bound.

::: {#def-goemans-williamson .definition name="Goemans–Williamson rounding"}

Solve the semidefinite program to get unit vectors $v_i$. Pick a uniformly random unit vector $r$ (normalise a vector of independent standard Gaussians) and return $S=\{i:r^{\mathsf T}v_i\ge0\}$: the vertices on one side of a random hyperplane through the origin.

:::

```{=latex}
\begin{algorithm}
\caption{Goemans--Williamson maximum cut}
\begin{algorithmic}
\INPUT graph $G=(V,E)$, weights $w\ge0$
\OUTPUT a cut $S$ with $\mathbb E\,w(\delta(S))\ge0.878\,\mathrm{OPT}$
\STATE solve $\max\{\tfrac14L\bullet Y:Y_{ii}=1,\,Y\succeq0\}$
\STATE factor $Y=V^{\mathsf T}V$; let $v_i$ be the columns of $V$
\STATE draw $r$ with independent standard normal coordinates
\RETURN $S=\{i:r^{\mathsf T}v_i\ge0\}$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-goemans-williamson .theorem name="Goemans–Williamson"}

The cut satisfies $\mathbb E\,w(\delta(S))\ge\gamma\,\mathrm{SDP}\ge\gamma\,\mathrm{OPT}$, where
$$\gamma=\min_{-1\le x<1}\frac{2\arccos x}{\pi(1-x)}\approx0.87856.$$

:::

::: {.proof}

1. *Probability that an edge is cut.* $v_i$ and $v_j$ are separated when $r^{\mathsf T}v_i$ and $r^{\mathsf T}v_j$ have opposite signs. These depend only on the projection $p$ of $r$ onto the plane spanned by $v_i,v_j$, and $p/\lVert p\rVert$ is uniform on the unit circle of that plane (the Gaussian distribution is rotation invariant). The line orthogonal to $p$ separates $v_i$ from $v_j$ with probability $\theta_{ij}/\pi$, where $\theta_{ij}=\arccos(v_i^{\mathsf T}v_j)$ is the angle between them.

2. By linearity, $\mathbb E\,w(\delta(S))=\sum_{ij}w_{ij}\arccos(v_i^{\mathsf T}v_j)/\pi$.

3. Term by term, with $x=v_i^{\mathsf T}v_j$, $\arccos(x)/\pi\ge\gamma\,(1-x)/2$ by the definition of $\gamma$ (for $x=1$ both sides are $0$). Since $w_{ij}\ge0$, $\mathbb E\,w(\delta(S))\ge\gamma\sum w_{ij}(1-v_i^{\mathsf T}v_j)/2=\gamma\,\mathrm{SDP}$.

:::

::: {#exm-goemans-williamson-c5 .example name="The 5-cycle"}

For the unweighted cycle on five vertices, $\mathrm{OPT}=4$ (an odd cycle cannot be fully cut). The optimal vectors lie in a plane, consecutive ones at angle $4\pi/5$, so $\mathrm{SDP}=5\cdot\frac{1-\cos(4\pi/5)}2\approx4.523$. Every edge is cut with probability $\tfrac45$, so the expected cut is exactly $4=\mathrm{OPT}$, and $\mathrm{OPT}/\mathrm{SDP}\approx0.884$.

:::

::: {#fig-max-cut-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) circle (1.4);
\draw[->, hl] (0,0)--(1.400,0.000);
\node[lab] at (1.700,0.000) {$v_1$};
\draw[->, emph] (0,0)--(-1.133,0.823);
\node[lab] at (-1.375,0.999) {$v_2$};
\draw[->, hl] (0,0)--(0.433,-1.331);
\node[lab] at (0.525,-1.617) {$v_3$};
\draw[->, hl] (0,0)--(0.433,1.331);
\node[lab] at (0.525,1.617) {$v_4$};
\draw[->, emph] (0,0)--(-1.133,-0.823);
\node[lab] at (-1.375,-0.999) {$v_5$};
\draw[gridline, dashed] (0.591,-1.911)--(-0.591,1.911);
\draw[->, emph] (0,0)--(0.764,0.236) node[lab, right] {$r$};
\end{tikzpicture}
\end{center}
```

Optimal vectors for the $5$-cycle: $v_{k+1}$ at angle $4\pi k/5$, consecutive ones $144^\circ$ apart. The hyperplane orthogonal to the random $r$ (dashed) puts the highlighted vectors in $S$; each edge is cut with probability $\tfrac45$.

:::

::: {#rmk-max-cut-1 .remark name="Hardness"}

The ratio $\gamma$ is tight for the relaxation: there are graphs with $\mathrm{OPT}/\mathrm{SDP}$ arbitrarily close to $\gamma$. Approximating maximum cut within $16/17+\varepsilon$ is NP-hard (Håstad), and within $\gamma+\varepsilon$ is hard under the Unique Games Conjecture (Khot, Kindler, Mossel, O'Donnell). The rounding can be derandomised.

:::
