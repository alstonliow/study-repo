---
title: "Positive Definite Matrices and Minima"
sources: [mit1806-25, mit1806-27]
requires: [math/linear-algebra/eigenvalues/symmetric-matrices]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 25 (second half) and Lecture 27, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-positive-definite .definition name="Positive definite matrix"}

A real symmetric matrix $S$ is *positive definite* if
$$\mathbf{x}^{\mathsf T}S\mathbf{x}>0\qquad\text{for every }\mathbf{x}\neq\mathbf{0}.$$
It is *positive semidefinite* if $\mathbf{x}^{\mathsf T}S\mathbf{x}\ge0$ for every $\mathbf{x}$.

:::

The number $\mathbf{x}^{\mathsf T}S\mathbf{x}=\sum_{i,j}s_{ij}x_ix_j$ is a *quadratic form*. For $S=\begin{bmatrix}a&b\\b&c\end{bmatrix}$ it is $ax^2+2bxy+cy^2$.

::: {#thm-positive-definite-tests .theorem name="Tests for positive definiteness"}

For a real symmetric $n\times n$ matrix $S$ the following are equivalent:

1. $\mathbf{x}^{\mathsf T}S\mathbf{x}>0$ for all $\mathbf{x}\neq\mathbf{0}$;
2. all eigenvalues of $S$ are positive;
3. all $n$ pivots of $S$ are positive (elimination without row exchanges);
4. all upper-left determinants $\det S_1,\dots,\det S_n$ are positive, where $S_k$ is the upper-left $k\times k$ submatrix;
5. $S=A^{\mathsf T}A$ for some matrix $A$ with independent columns.

:::

::: {.proof}

1. **(1)⇔(2).** By the spectral theorem (@thm-spectral-theorem), with $\mathbf{y}=Q^{\mathsf T}\mathbf{x}$, $\mathbf{x}^{\mathsf T}S\mathbf{x}=\mathbf{y}^{\mathsf T}\Lambda\mathbf{y}=\sum\lambda_iy_i^2$. As $\mathbf{x}$ runs over nonzero vectors, so does $\mathbf{y}$. The sum is always positive iff every $\lambda_i>0$ (take $\mathbf{y}=\mathbf{e}_i$ for the converse).

2. **(1)⇒(4).** Each $S_k$ is positive definite (use vectors $\mathbf{x}$ whose last $n-k$ entries are $0$), so by (2) its eigenvalues are positive and $\det S_k$, their product (@thm-trace-determinant-eigenvalues), is positive.

3. **(4)⇒(3).** Elimination on $S$ restricted to the first $k$ rows and columns is elimination on $S_k$, so $\det S_k=d_1\cdots d_k$ (@cor-determinant-pivots) as long as the pivots are nonzero. Hence $d_k=\det S_k/\det S_{k-1}>0$ for every $k$, which also shows that no zero pivot appears.

4. **(3)⇒(1).** $S=LDL^{\mathsf T}$ (@prp-symmetric-ldlt), so $\mathbf{x}^{\mathsf T}S\mathbf{x}=\mathbf{z}^{\mathsf T}D\mathbf{z}=\sum d_iz_i^2$ with $\mathbf{z}=L^{\mathsf T}\mathbf{x}\neq\mathbf{0}$ ($L^{\mathsf T}$ is invertible). This is positive.

5. **(5)⇒(1).** $\mathbf{x}^{\mathsf T}A^{\mathsf T}A\mathbf{x}=\lVert A\mathbf{x}\rVert^2>0$, because $A\mathbf{x}\ne\mathbf{0}$ for $\mathbf{x}\neq\mathbf{0}$ when the columns are independent.

6. **(3)⇒(5).** Take $A=\sqrt D\,L^{\mathsf T}$, which is invertible: $A^{\mathsf T}A=L\sqrt D\sqrt DL^{\mathsf T}=S$.

:::

::: {#exm-positive-definite-threshold .example name="Where definiteness stops"}

$S=\begin{bmatrix}2&4\\4&c\end{bmatrix}$ has $\det S_1=2$ and $\det S_2=2c-16$. It is positive definite exactly when $c>8$. At $c=8$ it is semidefinite: $\mathbf{x}^{\mathsf T}S\mathbf{x}=2x^2+8xy+8y^2=2(x+2y)^2$, which vanishes along $x=-2y$. For $c<8$ the form takes negative values, e.g. at $(2,-1)$ it equals $8-16+c=c-8$.

:::

::: {#exm-second-difference-positive-definite .example name="The second difference matrix"}

$S=\begin{bmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{bmatrix}$ has upper-left determinants $2,3,4$ and pivots $2,\frac32,\frac43$, all positive. Its eigenvalues are $2-\sqrt2$, $2$, $2+\sqrt2$. Completing squares,
$$\mathbf{x}^{\mathsf T}S\mathbf{x}=2\big(x_1-\tfrac12x_2\big)^2+\tfrac32\big(x_2-\tfrac23x_3\big)^2+\tfrac43x_3^2,$$
with the pivots as coefficients and the multipliers inside the squares.

:::

<!-- Merged 2026-11-20 (owner): the block thm-second-derivative-test was removed in favour of thm-second-derivative-test-several in math/analysis/differentiation/second-derivatives; its use of the smallest eigenvalue is kept there as an alternative in step 1. -->

**Minima.** If $f:\mathbb{R}^n\to\mathbb{R}$ is twice continuously differentiable, $\nabla f(\mathbf{x}_0)=\mathbf{0}$ and the matrix of second derivatives $H=\big[\partial^2f/\partial x_i\partial x_j(\mathbf{x}_0)\big]$ is positive definite, then $f$ has a strict local minimum at $\mathbf{x}_0$ (@thm-second-derivative-test-several). The reason: by Taylor's theorem $f(\mathbf{x}_0+\mathbf{h})-f(\mathbf{x}_0)=\frac12\mathbf{h}^{\mathsf T}H\mathbf{h}+o(\lVert\mathbf{h}\rVert^2)$, and $\mathbf{h}^{\mathsf T}H\mathbf{h}\ge\lambda_{\min}\lVert\mathbf{h}\rVert^2$ with $\lambda_{\min}>0$.

::: {#rmk-positive-definite-matrices-1 .remark name="Ellipses"}

For positive definite $S$, the set $\mathbf{x}^{\mathsf T}S\mathbf{x}=1$ is an ellipse (ellipsoid). Its axes point along the eigenvectors and have half-lengths $1/\sqrt{\lambda_i}$: in the coordinates $\mathbf{y}=Q^{\mathsf T}\mathbf{x}$ the equation is $\sum\lambda_iy_i^2=1$.

:::
