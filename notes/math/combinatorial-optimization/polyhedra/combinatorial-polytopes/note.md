---
title: "Polytopes of Combinatorial Objects"
sources: [mit18433-3]
requires: [math/combinatorial-optimization/polyhedra/vertices-of-polyhedra]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on polyhedral theory and linear programming (Section 3.4, polyhedral combinatorics and the permutahedron), in our own wording; example our own (checked by computation); proofs written out in steps. -->

*Polyhedral combinatorics* studies the convex hull of a finite set $X\subseteq\mathbb R^n$ of combinatorial objects, for example the incidence vectors of the matchings or spanning trees of a graph. A description $\operatorname{conv}(X)=\{x:Ax\le b\}$ turns the combinatorial problem $\max\{c^{\mathsf T}x:x\in X\}$ into a linear program, because a linear function attains its maximum over a polytope at a vertex (@cor-minimal-faces-are-vertices), and every vertex of $\operatorname{conv}(X)$ lies in $X$. For problems that are hard to optimise (such as stable sets in general graphs) no usable description is expected to exist.

For a proposed $P=\{x:Ax\le b\}$, the inclusion $\operatorname{conv}(X)\subseteq P$ only needs every point of $X$ to satisfy every row. The reverse inclusion is the real work.

::: {#rmk-three-proof-techniques .remark name="Three ways to prove $P\subseteq\operatorname{conv}(X)$"}

1. *Algorithmic (duality).* For every cost $c$,
$$\max_{x\in X}c^{\mathsf T}x=\max_{x\in\operatorname{conv}(X)}c^{\mathsf T}x\le\max_{x\in P}c^{\mathsf T}x=\min\{b^{\mathsf T}y:A^{\mathsf T}y=c,\ y\ge0\}$$
by strong duality (@thm-strong-duality). Exhibit, for each $c$, a point $x\in X$ and a dual feasible $y$ with $c^{\mathsf T}x=b^{\mathsf T}y$; then equality holds throughout for every $c$, which forces $P=\operatorname{conv}(X)$ (a point of $P$ outside $\operatorname{conv}(X)$ would be separated from it by some $c$). The Hungarian method (@sec-math-combinatorial-optimization-matching-hungarian-method) is an example.

2. *Vertices.* Show that $P$ is bounded and that each vertex of $P$ lies in $X$. Then $P=\operatorname{conv}(\text{vertices})\subseteq\operatorname{conv}(X)$ by @thm-minkowski-polytope. Total unimodularity (@sec-math-combinatorial-optimization-polyhedra-total-unimodularity) is the main tool.

3. *Facets.* Write $P=\{x:Ax\le b,\ Cx=d\}$. First show that no equality is missing: $\dim\operatorname{conv}(X)=\dim P$, by exhibiting $\dim P+1$ affinely independent points of $X$. Then show that no facet is missing: for each $\alpha$ not in the row space of $C$, every maximiser of $\alpha^{\mathsf T}x$ over $X$ satisfies some row $a_i^{\mathsf T}x\le b_i$ of $P$ with equality, where that row is not tight on all of $P$. Then every facet of $\operatorname{conv}(X)$ is contained in a face defined by a row of $P$, and by @thm-facets-describe-polyhedra the rows of $P$ already cut out $\operatorname{conv}(X)$.

:::

The facet method is often the shortest. Here is a clean example.

::: {#thm-permutahedron .theorem name="The permutahedron"}

Let $X=\{(\sigma(1),\dots,\sigma(n)):\sigma\text{ a permutation of }\{1,\dots,n\}\}\subseteq\mathbb R^n$. Then
$$\operatorname{conv}(X)=\Big\{x\in\mathbb R^n:\ \sum_{i=1}^nx_i=\binom{n+1}2,\quad\sum_{i\in S}x_i\ge\binom{|S|+1}2\ \text{ for all } S\subsetneq\{1,\dots,n\}\Big\}.$$

:::

::: {.proof}

1. *$X\subseteq P$.* The entries of a permutation sum to $1+\dots+n=\binom{n+1}2$, and any $|S|$ of them are distinct positive integers, so their sum is at least $1+\dots+|S|=\binom{|S|+1}2$.

2. *No equality is missing.* Let $\pi_1$ be the identity and, for $k=2,\dots,n$, let $\pi_k$ swap the values $1$ and $k$. Then $\pi_k-\pi_1=(k-1)(e_k-e_1)$, and the vectors $e_k-e_1$ ($k=2,\dots,n$) are linearly independent. So $\pi_1,\dots,\pi_n$ are $n$ affinely independent points of $X$, and $\dim\operatorname{conv}(X)\ge n-1$. Since $P$ lies in a hyperplane, $\dim P\le n-1$.

3. *No facet is missing.* Let $\alpha^{\mathsf T}x\le\beta$ define a non-trivial face of $\operatorname{conv}(X)$, with $\beta=\max_{x\in X}\alpha^{\mathsf T}x$, and let $S=\{i:\alpha_i=\min_j\alpha_j\}$. If $S$ were all indices, $\alpha$ would be a multiple of $\mathbf 1$ and $\alpha^{\mathsf T}x$ constant on $X$, giving a trivial face; so $S\ne\{1,\dots,n\}$.

4. A permutation maximising $\alpha^{\mathsf T}x$ must give the $|S|$ smallest values $1,\dots,|S|$ to the positions of $S$: if some $i\in S$ had a larger value than some $j\notin S$ (where $\alpha_j>\alpha_i$), swapping the two values would raise $\alpha^{\mathsf T}x$ by $(\alpha_j-\alpha_i)(x_i-x_j)>0$.

5. So every maximiser satisfies $\sum_{i\in S}x_i=\binom{|S|+1}2$, a row of $P$ that is not tight on all of $X$ (put the value $n$ in $S$). By the facet method (the third technique above), $P=\operatorname{conv}(X)$.

:::

::: {#exm-permutahedron-three .example name="The permutahedron for $n=3$"}

For $n=3$ the six permutations of $(1,2,3)$ lie in the plane $x_1+x_2+x_3=6$ and form a regular hexagon. The six inequalities with $|S|=1$ or $|S|=2$ ($x_i\ge1$ and $x_i+x_j\ge3$) give its six edges; for instance $x_1\ge1$ is tight at $(1,2,3)$ and $(1,3,2)$.

:::

::: {#fig-combinatorial-polytopes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (-0.78,-1.35) -- (0.78,-1.35) -- (1.56,0.00) -- (0.78,1.35) -- (-0.78,1.35) -- (-1.56,0.00) -- cycle;
\draw[emph] (-0.78,-1.35) -- (0.78,-1.35) -- (1.56,0.00) -- (0.78,1.35) -- (-0.78,1.35) -- (-1.56,0.00) -- cycle;
\fill (-0.78,-1.35) circle (1.5pt);
\node[lab] at (-1.03,-1.78) {$123$};
\fill (-1.56,0.00) circle (1.5pt);
\node[lab] at (-2.05,0.00) {$132$};
\fill (0.78,-1.35) circle (1.5pt);
\node[lab] at (1.03,-1.78) {$213$};
\fill (-0.78,1.35) circle (1.5pt);
\node[lab] at (-1.03,1.78) {$231$};
\fill (1.56,0.00) circle (1.5pt);
\node[lab] at (2.05,0.00) {$312$};
\fill (0.78,1.35) circle (1.5pt);
\node[lab] at (1.03,1.78) {$321$};
\draw[hl] (-0.78,-1.35) -- (-1.56,0.00);
\node[lab] at (-0.72,-0.42) {$x_1\ge1$};
\end{tikzpicture}
\end{center}
```

The permutahedron for $n=3$, drawn in the plane $x_1+x_2+x_3=6$: a hexagon whose vertices are the six permutations (written $\sigma(1)\sigma(2)\sigma(3)$). The highlighted edge is the facet $x_1\ge1$.

:::
