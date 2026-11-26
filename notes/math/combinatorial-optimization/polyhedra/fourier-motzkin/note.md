---
title: "Projection and Fourier–Motzkin Elimination"
sources: [mit18433-3]
requires: [math/optimization/convex-sets/examples-of-convex-sets]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on polyhedral theory and linear programming (Section 3, opening part), in our own wording; example our own (checked by computation); proofs written out in steps. Halfspaces, polyhedra and the hulls are already defined in @def-hyperplane-halfspace, @def-polyhedron, @def-affine-set, @def-convex-combination and @def-convex-cone; here a polyhedron is always written $P=\{x\in\mathbb R^n:Ax\le b\}$ (an equality is two inequalities). -->

Eliminating one variable from a system of linear inequalities gives again a system of linear inequalities. This simple fact shows that projections of polyhedra are polyhedra, that the convex hull of finitely many points is a polyhedron, and (in @sec-math-combinatorial-optimization-polyhedra-farkas-lemma) that an infeasible system always has a short certificate.

::: {#def-coordinate-projection .definition name="Coordinate projection"}

For a polyhedron $P\subseteq\mathbb R^n$ and an index $k$, the *projection* of $P$ along $x_k$ is
$$P_k=\{(x_1,\dots,x_{k-1},x_{k+1},\dots,x_n): x\in P\text{ for some value of }x_k\}\subseteq\mathbb R^{n-1}.$$
Projecting repeatedly eliminates any set of coordinates.

:::

::: {#def-fourier-motzkin .definition name="Fourier–Motzkin elimination"}

Let $P=\{x:Ax\le b\}$ with rows $a_i^{\mathsf T}x\le b_i$, and split the rows by the sign of the coefficient of $x_k$:
$$S_+=\{i:a_{ik}>0\},\qquad S_-=\{i:a_{ik}<0\},\qquad S_0=\{i:a_{ik}=0\}.$$
The *eliminated system* consists of

1. every row $i\in S_0$ (it does not involve $x_k$), and
2. for every pair $i\in S_+$, $l\in S_-$, the combination $(-a_{lk})\,(a_i^{\mathsf T}x\le b_i)+a_{ik}\,(a_l^{\mathsf T}x\le b_l)$, in which the coefficient of $x_k$ is $0$:
$$\sum_{j\ne k}(a_{ik}a_{lj}-a_{lk}a_{ij})\,x_j\le a_{ik}b_l-a_{lk}b_i .$$

Each new inequality is a nonnegative combination of the old ones.

:::

::: {#thm-fourier-motzkin .theorem name="Projections of polyhedra are polyhedra"}

The projection $P_k$ is exactly the set of solutions of the eliminated system. In particular $P_k$ is a polyhedron.

:::

::: {.proof}

1. *Every point of $P_k$ satisfies the system.* If $x\in P$, then $x$ satisfies every row of $S_0$ and every nonnegative combination of rows; these do not involve $x_k$, so the projected point satisfies them.

2. *Every solution lifts.* Let $y=(x_j)_{j\ne k}$ satisfy the eliminated system. Divide row $i$ by $|a_{ik}|$ when $a_{ik}\ne0$. A row $i\in S_+$ becomes an upper bound $x_k\le U_i(y)$ and a row $l\in S_-$ a lower bound $x_k\ge L_l(y)$, where $U_i$ and $L_l$ are affine functions of $y$.

3. The combination of rows $i$ and $l$ in the eliminated system is, after division by the positive number $a_{ik}(-a_{lk})$, exactly $L_l(y)\le U_i(y)$. So every lower bound is at most every upper bound.

4. Hence $\max_l L_l(y)\le\min_i U_i(y)$ (an empty maximum is $-\infty$, an empty minimum $+\infty$), and any $x_k$ between them satisfies all rows of $S_+\cup S_-$. The rows of $S_0$ hold by assumption, so $(y,x_k)\in P$.

:::

::: {#exm-fourier-motzkin-triangle .example name="Projecting a triangle"}

Let $P=\{x\in\mathbb R^2: -x_1\le0,\ -x_2\le0,\ x_1+x_2\le2\}$, the triangle with corners $(0,0)$, $(2,0)$, $(0,2)$. To eliminate $x_2$: $S_+=\{3\}$, $S_-=\{2\}$, $S_0=\{1\}$. Adding rows $2$ and $3$ gives $x_1\le2$, and row $1$ is kept, so $P_2=\{x_1:0\le x_1\le2\}$, the shadow of the triangle on the $x_1$-axis.

:::

::: {#fig-fourier-motzkin-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (3,0) -- (0,3) -- cycle;
\draw[emph] (0,0) -- (3,0) -- (0,3) -- cycle;
\draw[->, faint] (-0.3,0) -- (3.6,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-1.1) -- (0,3.4) node[lab, above] {$x_2$};
\draw[hl] (0,-0.7) -- (3,-0.7);
\draw[faint, dashed] (0,0) -- (0,-0.7); \draw[faint, dashed] (3,0) -- (3,-0.7);
\node[lab] at (1.5,-1.05) {$P_2=[0,2]$};
\node[lab] at (0.9,0.9) {$P$};
\node[lab, left] at (0,3) {$2$}; \node[lab, below right] at (3,0) {$2$};
\end{tikzpicture}
\end{center}
```

Eliminating $x_2$ from the triangle $P$ (shaded) gives its shadow $P_2=\{x_1:0\le x_1\le2\}$ on the $x_1$-axis: the bound $x_1\le2$ is the sum of the rows $-x_2\le0$ and $x_1+x_2\le2$.

:::

::: {#cor-polytope-hull-is-polyhedron .corollary name="The convex hull of finitely many points is a bounded polyhedron"}

For points $a^{(1)},\dots,a^{(m)}\in\mathbb R^n$, the set $\operatorname{conv}\{a^{(1)},\dots,a^{(m)}\}$ is a bounded polyhedron.

:::

::: {.proof}

1. The hull is the projection onto the $x$-coordinates of the polyhedron in the variables $(x,\lambda)$ given by $x-\sum_k\lambda_ka^{(k)}=0$, $\sum_k\lambda_k=1$, $\lambda\ge0$.

2. Eliminating $\lambda_1,\dots,\lambda_m$ one at a time (@thm-fourier-motzkin) leaves a system of inequalities in $x$ alone, so the hull is a polyhedron.

3. It is bounded: for $x=\sum_k\lambda_ka^{(k)}$ in the hull, $\lVert x\rVert\le\sum_k\lambda_k\lVert a^{(k)}\rVert\le\max_k\lVert a^{(k)}\rVert$.

:::

The converse, that every bounded polyhedron is the convex hull of finitely many points, is @thm-minkowski-polytope. So the two usual definitions of a *polytope* (a bounded polyhedron, @def-polyhedron, and the convex hull of a finite set) agree.

::: {#rmk-fourier-motzkin-1 .remark name="Cost of elimination"}

One elimination step can replace $|S_+|+|S_-|$ rows by $|S_+|\cdot|S_-|$ rows, so eliminating many variables may blow up the system exponentially. The method is a tool for proofs, not an efficient algorithm.

:::
