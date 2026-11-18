---
title: "Cramer's Rule, the Inverse and Volume"
sources: [mit1806-20]
requires: [math/linear-algebra/determinants/determinant-formulas]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 20, in our own wording; proofs written out in steps. -->

::: {#thm-inverse-by-cofactors .theorem name="Formula for the inverse"}

If $\det A\neq0$, then
$$A^{-1}=\frac1{\det A}\,C^{\mathsf T},$$
where $C=[C_{ij}]$ is the matrix of cofactors (@def-cofactor).

:::

::: {.proof}

1. Entry $(i,i)$ of $AC^{\mathsf T}$ is $\sum_ja_{ij}C_{ij}=\det A$, the cofactor expansion along row $i$ (@thm-cofactor-expansion).

2. For $i\neq k$, entry $(i,k)$ is $\sum_ja_{ij}C_{kj}$. This is the cofactor expansion along row $k$ of the matrix obtained from $A$ by replacing row $k$ with row $i$ (the cofactors $C_{kj}$ do not involve row $k$). That matrix has two equal rows, so the sum is $0$.

3. Hence $AC^{\mathsf T}=(\det A)\,I$; divide by $\det A$.

:::

For $2\times2$ this is the familiar $\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$.

::: {#thm-cramers-rule .theorem name="Cramer's rule"}

If $\det A\neq0$, the solution of $A\mathbf{x}=\mathbf{b}$ is
$$x_j=\frac{\det B_j}{\det A},$$
where $B_j$ is $A$ with column $j$ replaced by $\mathbf{b}$.

:::

::: {.proof}

1. Let $X_j$ be $I$ with column $j$ replaced by $\mathbf{x}$. Then $AX_j=B_j$, since column $j$ of $AX_j$ is $A\mathbf{x}=\mathbf{b}$ and the other columns are the columns of $A$.

2. Expanding $\det X_j$ along row $j$ (which has the single entry $x_j$ on the diagonal, after the other rows reduce to rows of $I$) gives $\det X_j=x_j$.

3. The product rule (@thm-product-rule-determinants) gives $\det A\cdot x_j=\det B_j$.

:::

Cramer's rule is elegant but costly: $n+1$ determinants instead of one elimination.

::: {#thm-determinant-volume .theorem name="Determinant as volume"}

$\lvert\det A\rvert$ is the volume of the box (parallelepiped) in $\mathbb{R}^n$ whose edges from the origin are the rows of $A$ (or the columns).

:::

::: {.proof}

1. The volume satisfies the three defining properties up to sign: the unit cube has volume $1$; exchanging rows does not change the box; scaling one edge by $t\ge0$ scales the volume by $t$.

2. Adding a multiple of one edge to another slides the box along that edge without changing its base or height, so the volume is unchanged. Together with step 1 this matches every step of elimination.

3. For an orthogonal matrix $Q$ the box is a rotated cube of volume $1$, and $\lvert\det Q\rvert=1$ because $\det Q^{\mathsf T}\det Q=\det I=1$ and $\det Q^{\mathsf T}=\det Q$. For a general $A$, eliminate to triangular form: each step preserves both volume and $\lvert\det\rvert$, and for a triangular (indeed diagonal after the upward steps) matrix both equal $\lvert a_{11}\cdots a_{nn}\rvert$.

:::

::: {#fig-cramers-rule-and-volume-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.200,0) -- (3.400,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.200) -- (0,2.600) node[lab, above] {$y$};
\fill[tintA] (0,0) -- (2.10,0.7) -- (2.8,2.10) -- (0.7,1.4) -- cycle;
\draw[emph] (0,0) -- (2.10,0.7) -- (2.8,2.10) -- (0.7,1.4) -- cycle;
\draw[->, hl] (0.000,0.000) -- (2.100,0.700);
\node[lab, right] at (2.100,0.700) {$(3,1)$};
\draw[->, hl] (0.000,0.000) -- (0.700,1.400);
\node[lab, left] at (0.700,1.400) {$(1,2)$};
\node[lab] at (1.4,1.05) {area $5$};
\end{tikzpicture}
\end{center}
```

The rows $(3,1)$ and $(1,2)$ span a parallelogram of area $\lvert\det\begin{bmatrix}3&1\\1&2\end{bmatrix}\rvert=5$.

:::

::: {#exm-triangle-area .example name="Area of a triangle"}

The triangle with corners $(x_1,y_1),(x_2,y_2),(x_3,y_3)$ is half of a parallelogram, so its area is
$$\frac12\left|\det\begin{bmatrix}x_1&y_1&1\\x_2&y_2&1\\x_3&y_3&1\end{bmatrix}\right|.$$
For corners $(0,0),(4,0),(1,3)$ this gives $\frac12\lvert4\cdot3-0\cdot1\rvert=6$.

:::
