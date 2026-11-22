---
title: "Cramer's Rule, the Inverse and Volume"
sources: [mit1806-20]
requires: [math/linear-algebra/determinants/determinant-formulas]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 20, in our own wording; proofs written out in steps. -->

<!-- Merged 2026-11-20 (owner): the block thm-inverse-by-cofactors was removed in favour of thm-adjugate (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Formula for the inverse.** If $\det A\neq0$, then
$$A^{-1}=\frac1{\det A}\,C^{\mathsf T},$$
where $C=[C_{ij}]$ is the matrix of cofactors (@def-cofactor): row $i$ of $A$ times the cofactors of row $i$ is $\det A$, and times the cofactors of another row it is the determinant of a matrix with two equal rows, $0$. $C^{\mathsf T}$ is the adjugate; see @thm-adjugate.

For $2\times2$ this is the familiar $\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$.

::: {#thm-cramers-rule .theorem name="Cramer's rule"}

If $\det A\neq0$, the solution of $A\mathbf{x}=\mathbf{b}$ is
$$x_j=\frac{\det B_j}{\det A},$$
where $B_j$ is $A$ with column $j$ replaced by $\mathbf{b}$.

:::

::: {.proof}

1. Let $X_j$ be $I$ with column $j$ replaced by $\mathbf{x}$. Then $AX_j=B_j$, since column $j$ of $AX_j$ is $A\mathbf{x}=\mathbf{b}$ and the other columns are the columns of $A$.

2. Expanding $\det X_j$ along row $j$ (which has the single entry $x_j$ on the diagonal, after the other rows reduce to rows of $I$) gives $\det X_j=x_j$.

3. The product rule (@thm-determinant-multiplicative) gives $\det A\cdot x_j=\det B_j$.

:::

::: {#fig-cramers-rule-and-volume-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.5]
\draw[->, muted] (-0.3,0) -- (6.4,0); \draw[->, muted] (0,-0.3) -- (0,8.6);
\fill[tintA] (0.000,0.000) -- (2.000,1.000) -- (3.000,4.000) -- (1.000,3.000) -- cycle;
\draw[primary] (0,0) -- (2,1) -- (3,4) -- (1,3) -- cycle;
\fill[tintB] (0.000,0.000) -- (5.000,5.000) -- (6.000,8.000) -- (1.000,3.000) -- cycle;
\draw[accent, faint] (0,0) -- (5,5) -- (6,8) -- (1,3) -- cycle;
\draw[->, emph, primary] (0,0) -- (2,1) node[below right, lab] {$\mathbf a_1$};
\draw[->, emph, secondary] (0,0) -- (1,3) node[left, lab] {$\mathbf a_2$};
\draw[->, emph, accent] (0,0) -- (5,5) node[right, lab] {$\mathbf b=2\mathbf a_1+\mathbf a_2$};
\node[lab, note, primary, anchor=west] at (6.5,3.0) {area of $\mathbf a_1,\mathbf a_2$: $\det A=5$}; \node[lab, note, accent, anchor=west] at (6.5,1.8) {area of $\mathbf b,\mathbf a_2$: $\det B_1=10$};
\end{tikzpicture}
\end{center}
```

Cramer's rule as areas, for $A=\begin{bmatrix}2&1\\1&3\end{bmatrix}$ and $\mathbf b=(5,5)$. Replacing column $\mathbf a_1$ by $\mathbf b=x_1\mathbf a_1+x_2\mathbf a_2$ multiplies the area by $x_1$, since the $x_2\mathbf a_2$ part only shears along the other side. So $x_1=\det B_1/\det A=10/5=2$.

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

::: {#fig-cramers-rule-and-volume-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-0.3,0) -- (4.6,0); \draw[->, muted] (0,-0.3) -- (0,3.4);
\fill[tintD] (0.000,0.000) -- (4.000,0.000) -- (5.000,3.000) -- (1.000,3.000) -- cycle;
\draw[faint, dashed] (4,0) -- (5,3) -- (1,3);
\fill[tintB] (0.000,0.000) -- (4.000,0.000) -- (1.000,3.000) -- cycle;
\draw[accent, emph] (0,0) -- (4,0) -- (1,3) -- cycle;
\node[lab, tick, below] at (4,0) {$(4,0)$}; \node[lab, tick, above] at (1,3) {$(1,3)$};
\node[lab, note, accent] at (1.7,1.0) {area $6$}; \node[lab, note, muted] at (3.6,2.3) {parallelogram: $12$};
\end{scope}
\end{tikzpicture}
\end{center}
```

@exm-triangle-area: the triangle with corners $(0,0),(4,0),(1,3)$ is half of the parallelogram on the edges $(4,0)$ and $(1,3)$, whose area is $\lvert4\cdot3-0\cdot1\rvert=12$.

:::
