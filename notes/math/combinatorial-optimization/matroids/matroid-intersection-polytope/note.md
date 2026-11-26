---
title: "The Matroid Intersection Polytope"
sources: [mit18433-6]
requires: [math/combinatorial-optimization/matroids/matroid-intersection, math/combinatorial-optimization/matroids/matroid-polytope, math/combinatorial-optimization/polyhedra/total-unimodularity]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on matroid intersection (Section 6.3), in our own wording; example our own (checked by computation); proofs written out in steps. -->

The convex hull of the common independent sets of two matroids is as simple as it could be: the intersection of the two matroid polytopes. This gives a min-max relation for weighted matroid intersection, which generalises the assignment problem (@sec-math-combinatorial-optimization-matching-hungarian-method).

::: {#thm-matroid-intersection-polytope .theorem name="Matroid intersection polytope (Edmonds)"}

For matroids $M_1$, $M_2$ on $E$ with rank functions $r_1$, $r_2$,
$$\operatorname{conv}\{\chi_S:S\in\mathcal I_1\cap\mathcal I_2\}=\{x\in\mathbb R^E:\ x(S)\le r_1(S),\ x(S)\le r_2(S)\ \text{for all } S\subseteq E,\ \ x\ge0\}.$$

:::

The overall constraint matrix is not totally unimodular, but at each vertex only a TU subsystem matters.

::: {.proof}

1. Call the right side $P$. It contains each $\chi_S$ with $S\in\mathcal I_1\cap\mathcal I_2$, and it is bounded, so by @thm-minkowski-polytope it suffices to show every vertex $x^*$ of $P$ is such a $\chi_S$.

2. Let $\mathcal F_i=\{S:x^*(S)=r_i(S)\}$ and $E_0=\{e:x^*_e=0\}$. By @thm-vertex-unique-solution, $x^*$ is the unique solution of $x(S)=r_1(S)$ ($S\in\mathcal F_1$), $x(S)=r_2(S)$ ($S\in\mathcal F_2$), $x_e=0$ ($e\in E_0$).

3. For $i=1,2$ the equations of $\mathcal F_i$ define a face of the matroid polytope $P_i$ of $M_i$, so by @thm-matroid-face-chain they can be replaced by those of a chain $\mathcal C_i\subseteq\mathcal F_i$ with the same span (the proof there only used that $\mathcal F_i$ is closed under union and intersection, @lem-tight-sets-lattice). So $x^*$ is the unique solution of $Ax=b$, where after deleting the variables of $E_0$ the rows of $A$ are the incidence vectors of the sets in $\mathcal C_1\cup\mathcal C_2$.

4. *$A$ is TU*, by Ghouila-Houri (@thm-ghouila-houri). Given a set of rows, i.e. subchains $\mathcal C_1'\subseteq\mathcal C_1$ and $\mathcal C_2'\subseteq\mathcal C_2$, list $\mathcal C_1'$ from the largest set down and put its sets alternately into $R_1,R_2,R_1,\dots$; list $\mathcal C_2'$ the same way starting with $R_2$. An element lies in a top segment of each chain, so its column sum is in $\{0,1\}$ from $\mathcal C_1'$ and in $\{0,-1\}$ from $\mathcal C_2'$, in total in $\{-1,0,1\}$.

5. As $b$ is integral, @thm-tu-integral-polyhedron (in the form for a square invertible TU system, Cramer's rule) makes $x^*$ integral. With $0\le x^*_e\le r_1(\{e\})\le1$, $x^*=\chi_S$, and $|S|=x^*(S)\le r_i(S)$ gives $S\in\mathcal I_1\cap\mathcal I_2$.

:::

::: {#exm-matroid-intersection-polytope-bipartite .example name="Bipartite matchings again"}

For the two partition matroids of a bipartite graph (@exm-matroid-intersection-examples), the rank inequalities reduce to $x(\delta(v))\le1$ for each vertex together with $x\ge0$: for $M_A$, $r_A(S)$ is the number of $A$-vertices met by $S$, and $x(S)\le r_A(S)$ follows by adding $x(\delta(v)\cap S)\le1$ over those vertices. So the theorem says that the matching polytope of a bipartite graph is $\{x\ge0:x(\delta(v))\le1\ \text{for all } v\}$, as also follows from @thm-bipartite-incidence-tu. For the path $1$–$2$–$3$ this polytope in $\mathbb R^2$ (edges $12$, $23$) is the triangle $x_{12}+x_{23}\le1$, $x\ge0$, with vertices $\varnothing$, $\{12\}$, $\{23\}$.

:::

::: {#fig-matroid-intersection-polytope-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) rectangle (1.8,1.8);
\fill[tintA] (0,0) -- (1.8,0) -- (0,1.8) -- cycle; \draw[emph] (0,0) -- (1.8,0) -- (0,1.8) -- cycle;
\draw[->, faint] (0,0) -- (2.3,0) node[lab, right] {$x_{12}$}; \draw[->, faint] (0,0) -- (0,2.3) node[lab, above] {$x_{23}$};
\node[lab, below left] at (0,0) {$\varnothing$}; \node[lab, below] at (1.8,0) {$\{12\}$}; \node[lab, left] at (0,1.8) {$\{23\}$};
\node[lab] at (2.0,2.0) {$\{12,23\}$};
\end{tikzpicture}
\end{center}
```

The matching polytope of the path $1$–$2$–$3$: the degree constraint at vertex $2$, $x_{12}+x_{23}\le1$, cuts the unit square to the triangle with vertices $\varnothing$, $\{12\}$, $\{23\}$; the corner $\{12,23\}$ is not a matching.

:::

::: {#rmk-matroid-intersection-polytope-1 .remark name="Weighted matroid intersection"}

By LP duality the theorem gives, for every weight $c$, $\max\{c(S):S\in\mathcal I_1\cap\mathcal I_2\}=\min\{\sum_S r_1(S)y^1_S+\sum_S r_2(S)y^2_S\}$ over nonnegative $y^1,y^2$ with $\sum_{S\ni e}(y^1_S+y^2_S)\ge c(e)$. Primal–dual algorithms for weighted matroid intersection exist; the minimum cost arborescence algorithm (@sec-math-combinatorial-optimization-matroids-arborescences) is a special case solved directly.

:::
