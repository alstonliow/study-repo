---
title: "Faces of Polyhedra"
sources: [mit18433-3]
requires: [math/combinatorial-optimization/polyhedra/lp-duality]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on polyhedral theory and linear programming (Section 3.3, faces, facets and minimal descriptions), in our own wording; example our own (checked by computation); proofs written out in steps. The theorems on redundant inequalities are stated without proof, as in the course. -->

Throughout, $P=\{x\in\mathbb R^n:Ax\le b\}$ with rows $a_i^{\mathsf T}x\le b_i$, $i=1,\dots,m$.

::: {#def-affine-independence-dimension .definition name="Affine independence, dimension"}

Points $a^{(1)},\dots,a^{(k)}\in\mathbb R^n$ are *affinely independent* if
$$\sum_i\lambda_ia^{(i)}=0\ \text{and}\ \sum_i\lambda_i=0\quad\Longrightarrow\quad\lambda_i=0\ \text{for all }i,$$
equivalently, if the vectors $(a^{(i)},1)\in\mathbb R^{n+1}$ are linearly independent. The *dimension* $\dim P$ of a polyhedron is the largest number of affinely independent points in $P$, minus one; it is the dimension of its affine hull (@def-affine-set). So $\dim\varnothing=-1$, a point has dimension $0$, and $P$ is *full-dimensional* if $\dim P=n$.

:::

::: {#def-polyhedron-face .definition name="Valid inequality, face, vertex, edge, facet"}

An inequality $\alpha^{\mathsf T}x\le\beta$ is *valid* for $P$ if every $x\in P$ satisfies it. A *face* of $P$ is a set
$$F=\{x\in P:\alpha^{\mathsf T}x=\beta\}$$
for some valid inequality. The empty set and $P$ itself (from $0^{\mathsf T}x\le0$) are the *trivial* faces. Faces of dimension $0$ are *vertices* (or *extreme points*), of dimension $1$ *edges*, and of dimension $\dim P-1$ *facets*.

:::

Every face is itself a polyhedron. To check that an inequality is valid for $\operatorname{conv}(S)$ it suffices to check it on the points of $S$, since the set of points satisfying it is convex; this is why faces are convenient for convex hulls of combinatorial objects.

::: {#thm-faces-tight-rows .theorem name="Faces are obtained by making rows tight"}

Every non-empty face of $P$ has the form
$$F_I=\{x: a_i^{\mathsf T}x=b_i\ (i\in I),\ a_i^{\mathsf T}x\le b_i\ (i\notin I)\}$$
for some $I\subseteq\{1,\dots,m\}$. Hence $P$ has at most $2^m$ non-empty faces.

:::

::: {.proof}

1. Let $F$ be the non-empty face of the valid inequality $\alpha^{\mathsf T}x\le\beta$. Then $F$ is the set of optimal solutions of the LP $\max\{\alpha^{\mathsf T}x:x\in P\}$, whose optimum value is $\beta$.

2. This LP is feasible and bounded, so by strong duality (@thm-lp-strong-duality) its dual has an optimal solution $y^*$.

3. By complementary slackness (@thm-lp-complementary-slackness), a point $x\in P$ is optimal exactly when $a_i^{\mathsf T}x=b_i$ for all $i\in I=\{i:y^*_i>0\}$. So $F=F_I$.

4. There are $2^m$ choices of $I$.

:::

Conversely each non-empty $F_I$ is a face: it is the face of the valid inequality $\sum_{i\in I}a_i^{\mathsf T}x\le\sum_{i\in I}b_i$.

::: {#exm-faces-of-square .example name="The faces of a square"}

The square $P=\{x\in\mathbb R^2:0\le x_1\le1,\ 0\le x_2\le1\}$ has $4$ rows. Its non-empty faces are $P$ itself ($I=\varnothing$), $4$ edges (one row tight), $4$ vertices (two rows on different coordinates tight); sets $I$ containing both $x_1\ge0$ and $x_1\le1$ give the empty set. With the empty face there are $1+4+4+1=10$ faces, fewer than $2^4=16$.

:::

::: {#fig-faces-of-polyhedra-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (1.60,0.00) -- (1.60,1.60) -- (2.30,2.10) -- (2.30,0.50) -- cycle;
\draw[faint] (0.00,0.00) -- (0.70,0.50);
\draw[faint] (0.00,0.00) -- (0.00,1.60);
\draw[faint] (0.00,0.00) -- (1.60,0.00);
\draw[faint] (0.70,0.50) -- (0.70,2.10);
\draw[faint] (0.70,0.50) -- (2.30,0.50);
\draw[faint] (0.00,1.60) -- (0.70,2.10);
\draw[faint] (0.00,1.60) -- (1.60,1.60);
\draw[faint] (0.70,2.10) -- (2.30,2.10);
\draw[faint] (1.60,0.00) -- (2.30,0.50);
\draw[faint] (1.60,0.00) -- (1.60,1.60);
\draw[faint] (2.30,0.50) -- (2.30,2.10);
\draw[faint] (1.60,1.60) -- (2.30,2.10);
\draw[hl] (0.00,1.60) -- (0.70,2.10);
\node[hl dot] at (0.00,0.00) {};
\node[lab, below left] at (0.00,0.00) {vertex $x=0$};
\node[lab, above left] at (0.35,1.85) {edge $x_1=0,\ x_2=1$};
\node[lab, right] at (2.40,0.30) {facet $x_1=1$};
\end{tikzpicture}
\end{center}
```

Faces of the unit cube: a facet (one row tight), an edge (two rows tight) and a vertex (three rows tight). Exercise 3-4 counts all $28$ faces.

:::

::: {#cor-maximal-faces-are-facets .corollary name="Maximal faces are facets"}

The inclusion-wise maximal non-trivial faces of a non-empty polyhedron are its facets.

:::

The proof is an exercise.

For descriptions, only facets matter. Let $I^=$ be the set of rows with $a_i^{\mathsf T}x=b_i$ for all $x\in P$ (the *implicit equalities*), and $I^<$ the others. A row is *redundant* if deleting it does not change $P$.

::: {#thm-facets-describe-polyhedra .theorem name="Facets are necessary and sufficient"}

1. If $i\in I^<$ and the face $\{x\in P:a_i^{\mathsf T}x=b_i\}$ is not a facet, then row $i$ is redundant.
2. If $F$ is a facet of $P$, then some $i\in I^<$ has $\{x\in P:a_i^{\mathsf T}x=b_i\}=F$.

So a minimal description of $P$ consists of a set of linearly independent implicit equalities and exactly one inequality for each facet.

:::

::: {#rmk-faces-of-polyhedra-1 .remark name="Counting faces"}

The bound $2^m$ is attained by some polyhedra, such as the nonnegative orthant $\{x\in\mathbb R^n:x\ge0\}$ (exercise). For polytopes much better bounds are known (the upper bound theorem), but they are not needed here.

:::
