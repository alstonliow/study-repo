---
title: "Norms of Vectors and Matrices"
sources: [mit18065-8, mit18065-10, mit18065-11]
requires: [math/linear-algebra/positive-definite/singular-value-decomposition]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lectures 8, 10 and 11 (video lectures and problem sets; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->

A norm measures the size of a vector or a matrix. For matrices the useful norms are all read off from the singular values, and the ratio of the largest to the smallest singular value measures how sensitive $A\mathbf{x}=\mathbf{b}$ is to errors.

::: {#def-vector-p-norms .definition name="The ℓ¹, ℓ² and ℓ^∞ norms" related="def-norm"}

For $\mathbf{v}=(v_1,\dots,v_n)\in\mathbb{R}^n$,
$$\lVert\mathbf{v}\rVert_1=\sum_{i}\lvert v_i\rvert,\qquad \lVert\mathbf{v}\rVert_2=\Big(\sum_i v_i^2\Big)^{1/2},\qquad \lVert\mathbf{v}\rVert_\infty=\max_i\lvert v_i\rvert.$$
Each satisfies $\lVert\mathbf{v}\rVert\ge0$ with equality only for $\mathbf{v}=\mathbf{0}$, $\lVert c\mathbf{v}\rVert=\lvert c\rvert\,\lVert\mathbf{v}\rVert$, and the triangle inequality $\lVert\mathbf{v}+\mathbf{w}\rVert\le\lVert\mathbf{v}\rVert+\lVert\mathbf{w}\rVert$. Without a subscript, $\lVert\mathbf{v}\rVert=\lVert\mathbf{v}\rVert_2$.

:::

::: {#prp-vector-norm-comparisons .proposition name="Comparing the three norms"}

For every $\mathbf{v}\in\mathbb{R}^n$,
$$\lVert\mathbf{v}\rVert_\infty\le\lVert\mathbf{v}\rVert_2\le\lVert\mathbf{v}\rVert_1\le\sqrt n\,\lVert\mathbf{v}\rVert_2\le n\,\lVert\mathbf{v}\rVert_\infty .$$

:::

::: {.proof}

1. $\lVert\mathbf{v}\rVert_\infty^2=\max_i v_i^2\le\sum_i v_i^2=\lVert\mathbf{v}\rVert_2^2$.

2. $\lVert\mathbf{v}\rVert_1^2=\sum_{i,j}\lvert v_i\rvert\lvert v_j\rvert\ge\sum_i v_i^2=\lVert\mathbf{v}\rVert_2^2$, since the cross terms are nonnegative.

3. By Cauchy–Schwarz with the all-ones vector, $\sum_i\lvert v_i\rvert\cdot1\le\sqrt n\,\lVert\mathbf{v}\rVert_2$.

4. $\lVert\mathbf{v}\rVert_2^2=\sum_i v_i^2\le n\max_i v_i^2$, so $\sqrt n\,\lVert\mathbf{v}\rVert_2\le n\lVert\mathbf{v}\rVert_\infty$.

:::

::: {#fig-matrix-norms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.6,0) -- (1.8,0) node[lab, right] {$v_1$};
\draw[->, faint] (0,-1.5) -- (0,1.7) node[lab, above] {$v_2$};
\draw[faint] (-1,-1) rectangle (1,1);
\draw[emph] (0,0) circle (1);
\draw[hl] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
\node[lab] at (1.25,1.15) {$\ell^\infty$};
\node[lab] at (-0.86,0.86) {$\ell^2$};
\node[lab] at (0.25,0.38) {$\ell^1$};
\end{tikzpicture}
\end{center}
```

Unit balls in $\mathbb{R}^2$: the $\ell^1$ diamond lies inside the $\ell^2$ disc, which lies inside the $\ell^\infty$ square, matching $\lVert\mathbf{v}\rVert_\infty\le\lVert\mathbf{v}\rVert_2\le\lVert\mathbf{v}\rVert_1$.

:::

::: {#def-matrix-norms .definition name="Spectral, Frobenius and nuclear norms"}

For a real $m\times n$ matrix $A$,
$$\lVert A\rVert_2=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert A\mathbf{x}\rVert_2}{\lVert\mathbf{x}\rVert_2},\qquad \lVert A\rVert_F=\Big(\sum_{i,j}a_{ij}^2\Big)^{1/2},\qquad \lVert A\rVert_*=\sigma_1+\dots+\sigma_r .$$

:::

::: {#thm-matrix-norms-singular-values .theorem name="Matrix norms from singular values"}

If $A$ has singular values $\sigma_1\ge\dots\ge\sigma_r>0$, then
$$\lVert A\rVert_2=\sigma_1,\qquad \lVert A\rVert_F^2=\sigma_1^2+\dots+\sigma_r^2,\qquad \lVert A\rVert_*=\sigma_1+\dots+\sigma_r .$$
All three are unchanged when $A$ is multiplied on either side by an orthogonal matrix.

:::

::: {.proof}

1. Write $A=U\Sigma V^{\mathsf T}$ (@thm-svd). Orthogonal matrices preserve lengths (@prp-orthonormal-columns-preserve-length), so with $\mathbf{y}=V^{\mathsf T}\mathbf{x}$ we get $\lVert A\mathbf{x}\rVert=\lVert\Sigma\mathbf{y}\rVert$ and $\lVert\mathbf{x}\rVert=\lVert\mathbf{y}\rVert$.

2. $\lVert\Sigma\mathbf{y}\rVert^2=\sum_i\sigma_i^2y_i^2\le\sigma_1^2\lVert\mathbf{y}\rVert^2$, with equality for $\mathbf{y}=\mathbf{e}_1$. So $\lVert A\rVert_2=\sigma_1$.

3. $\lVert A\rVert_F^2=\operatorname{tr}(A^{\mathsf T}A)$, and $A^{\mathsf T}A=V\Sigma^{\mathsf T}\Sigma V^{\mathsf T}$ has the same trace as $\Sigma^{\mathsf T}\Sigma$, which is $\sum\sigma_i^2$.

4. If $Q_1,Q_2$ are orthogonal, $Q_1AQ_2=(Q_1U)\Sigma(Q_2^{\mathsf T}V)^{\mathsf T}$ is an SVD with the same $\Sigma$, so every norm defined by the $\sigma$'s is unchanged.

:::

::: {#prp-frobenius-submultiplicative .proposition name="Norms of products"}

$$\lVert AB\rVert_2\le\lVert A\rVert_2\lVert B\rVert_2,\qquad \lVert AB\rVert_F\le\lVert A\rVert_F\lVert B\rVert_F .$$

:::

::: {.proof}

1. $\lVert AB\mathbf{x}\rVert\le\lVert A\rVert_2\lVert B\mathbf{x}\rVert\le\lVert A\rVert_2\lVert B\rVert_2\lVert\mathbf{x}\rVert$ for every $\mathbf{x}$.

2. Let $\mathbf{r}_i^{\mathsf T}$ be the rows of $A$ and $\mathbf{b}_j$ the columns of $B$. By Cauchy–Schwarz, $(AB)_{ij}^2=(\mathbf{r}_i^{\mathsf T}\mathbf{b}_j)^2\le\lVert\mathbf{r}_i\rVert^2\lVert\mathbf{b}_j\rVert^2$.

3. Summing over all $i$ and $j$: $\lVert AB\rVert_F^2\le\big(\sum_i\lVert\mathbf{r}_i\rVert^2\big)\big(\sum_j\lVert\mathbf{b}_j\rVert^2\big)=\lVert A\rVert_F^2\lVert B\rVert_F^2$.

:::

::: {#rmk-matrix-norms-1 .remark name="Unit balls"}

The unit ball $\{\mathbf{v}:\lVert\mathbf{v}\rVert\le1\}$ in $\mathbb{R}^2$ is a diamond for $\ell^1$, a disc for $\ell^2$ and a square for $\ell^\infty$. Each is convex, by the triangle inequality. For $0<p<1$ the formula $(\sum\lvert v_i\rvert^p)^{1/p}$ gives a non-convex "ball" and fails the triangle inequality, so it is not a norm. Minimising $\lVert\mathbf{x}\rVert_1$ subject to $A\mathbf{x}=\mathbf{b}$ tends to give sparse solutions, because the diamond first touches the plane $A\mathbf{x}=\mathbf{b}$ at a corner; minimising $\lVert\mathbf{x}\rVert_2$ gives $A^{+}\mathbf{b}$ (@thm-pseudoinverse-properties).

:::

::: {#def-condition-number .definition name="Condition number"}

For an invertible $n\times n$ matrix $A$,
$$\kappa(A)=\lVert A\rVert_2\,\lVert A^{-1}\rVert_2=\frac{\sigma_1}{\sigma_n}\ \ge1 .$$

:::

::: {#thm-condition-number-error .theorem name="Relative error is at most κ times larger"}

If $A\mathbf{x}=\mathbf{b}$ and $A(\mathbf{x}+\delta\mathbf{x})=\mathbf{b}+\delta\mathbf{b}$ with $\mathbf{b}\ne\mathbf{0}$, then
$$\frac{\lVert\delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(A)\,\frac{\lVert\delta\mathbf{b}\rVert}{\lVert\mathbf{b}\rVert}.$$

:::

::: {.proof}

1. Subtracting, $A\,\delta\mathbf{x}=\delta\mathbf{b}$, so $\lVert\delta\mathbf{x}\rVert=\lVert A^{-1}\delta\mathbf{b}\rVert\le\lVert A^{-1}\rVert_2\lVert\delta\mathbf{b}\rVert$.

2. From $\mathbf{b}=A\mathbf{x}$, $\lVert\mathbf{b}\rVert\le\lVert A\rVert_2\lVert\mathbf{x}\rVert$, so $1/\lVert\mathbf{x}\rVert\le\lVert A\rVert_2/\lVert\mathbf{b}\rVert$.

3. Multiply the two inequalities.

4. Equality holds when $\mathbf{x}$ is along $\mathbf{v}_1$ and $\delta\mathbf{b}$ along $\mathbf{u}_n$, so the bound cannot be improved.

:::

::: {#exm-condition-number-hilbert .example name="Small and large condition numbers"}

$A=\begin{bmatrix}3&0\\4&5\end{bmatrix}$ has $\sigma_1=3\sqrt5$, $\sigma_2=\sqrt5$ (@exm-svd-two-by-two). So $\lVert A\rVert_2=3\sqrt5$, $\lVert A\rVert_F=\sqrt{50}$, $\lVert A\rVert_*=4\sqrt5$ and $\kappa(A)=3$.

The $3\times3$ Hilbert matrix $H_{ij}=1/(i+j-1)$ is symmetric positive definite with $\kappa(H)\approx524$; for $n=10$ it is about $1.6\times10^{13}$, so in double precision almost every digit of the solution of $H\mathbf{x}=\mathbf{b}$ can be lost. Orthogonal matrices have $\kappa(Q)=1$, which is why computations with $Q$ are safe.

:::
