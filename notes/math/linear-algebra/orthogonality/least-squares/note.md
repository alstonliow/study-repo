---
title: "Least Squares Approximation"
sources: [mit1806-16]
requires: [math/linear-algebra/orthogonality/projections]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 16, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

An overdetermined system $A\mathbf{x}=\mathbf{b}$ (more equations than unknowns) usually has no solution: $\mathbf{b}$ is not in $C(A)$. The best we can do is to make the error small.

::: {#def-least-squares-solution .definition name="Least squares solution"}

A *least squares solution* of $A\mathbf{x}=\mathbf{b}$ is a vector $\hat{\mathbf{x}}$ that minimises
$$\lVert A\mathbf{x}-\mathbf{b}\rVert^2=\sum_i\big((A\mathbf{x})_i-b_i\big)^2.$$

:::

::: {#thm-least-squares-normal-equations .theorem name="Least squares solves the normal equations"}

$\hat{\mathbf{x}}$ is a least squares solution if and only if $A^{\mathsf T}A\hat{\mathbf{x}}=A^{\mathsf T}\mathbf{b}$. If the columns of $A$ are independent it is unique, and $A\hat{\mathbf{x}}$ is the projection of $\mathbf{b}$ onto $C(A)$.

:::

::: {.proof}

1. $A\mathbf{x}$ ranges over $C(A)$, so minimising $\lVert A\mathbf{x}-\mathbf{b}\rVert$ means finding the point of $C(A)$ closest to $\mathbf{b}$.

2. For independent columns this is @thm-projection-onto-subspace.

3. In general, step 2 of that proof shows that any $\hat{\mathbf{x}}$ with $A^{\mathsf T}(\mathbf{b}-A\hat{\mathbf{x}})=\mathbf{0}$ is a minimiser; conversely at a minimiser the error must be orthogonal to $C(A)$, or moving along a column direction would reduce it.

:::

::: {#exm-least-squares-line .example name="Fitting a straight line"}

Fit $b=C+Dt$ to the points $(t,b)=(0,1),(1,3),(2,4),(3,4)$. The four equations $C+Dt_i=b_i$ are
$$A=\begin{bmatrix}1&0\\1&1\\1&2\\1&3\end{bmatrix},\qquad \mathbf{b}=\begin{bmatrix}1\\3\\4\\4\end{bmatrix},\qquad
A^{\mathsf T}A=\begin{bmatrix}4&6\\6&14\end{bmatrix},\qquad A^{\mathsf T}\mathbf{b}=\begin{bmatrix}12\\23\end{bmatrix}.$$
The normal equations give $\hat C=\frac32$, $\hat D=1$: the best line is $b=\frac32+t$. Its values at the four points are $\mathbf{p}=(\frac32,\frac52,\frac72,\frac92)$ and the errors are $\mathbf{e}=\mathbf{b}-\mathbf{p}=(-\frac12,\frac12,\frac12,-\frac12)$. As predicted, $\mathbf{e}$ is perpendicular to both columns of $A$: its entries sum to $0$, and $\sum_i t_ie_i=0+\frac12+1-\frac32=0$.

:::

::: {#fig-least-squares-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.300,0) -- (3.600,0) node[lab, right] {$t$};
\draw[->, faint] (0,-0.200) -- (0,3.000) node[lab, above] {$b$};
\draw[hl] (-0.200,0.780) -- (3.400,2.940) node[lab, right] {$b=\frac32+t$};
\draw[dashed] (0.000,0.900) -- (0.000,0.600);
\node[dot] at (0.000,0.600) {};
\node[lab, tick, left] at (-0.050,0.750) {$e=-\tfrac12$};
\node[lab, tick, below] at (0.000,0) {0};
\draw[dashed] (1.000,1.500) -- (1.000,1.800);
\node[dot] at (1.000,1.800) {};
\node[lab, tick, left] at (0.950,1.650) {$e=\tfrac12$};
\node[lab, tick, below] at (1.000,0) {1};
\draw[dashed] (2.000,2.100) -- (2.000,2.400);
\node[dot] at (2.000,2.400) {};
\node[lab, tick, left] at (1.950,2.250) {$e=\tfrac12$};
\node[lab, tick, below] at (2.000,0) {2};
\draw[dashed] (3.000,2.700) -- (3.000,2.400);
\node[dot] at (3.000,2.400) {};
\node[lab, tick, left] at (2.950,2.550) {$e=-\tfrac12$};
\node[lab, tick, below] at (3.000,0) {3};
\end{tikzpicture}
\end{center}
```

The best line $b=\frac32+t$ and the vertical errors $e_i=b_i-p_i$, which sum to zero and are orthogonal to $(0,1,2,3)$.

:::

::: {#rmk-least-squares-1 .remark name="Calculus gives the same equations"}

Setting the partial derivatives of $E(C,D)=\sum_i(C+Dt_i-b_i)^2$ to zero gives $\sum_i(C+Dt_i-b_i)=0$ and $\sum_it_i(C+Dt_i-b_i)=0$, which are the two normal equations. Fitting a parabola $C+Dt+Et^2$ adds a column $t_i^2$ to $A$; the method is unchanged.

:::
