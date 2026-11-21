---
title: "Distance Matrices and the Procrustes Problem"
sources: [mit18065-33, mit18065-34]
requires: [math/linear-algebra/matrix-methods/matrix-norms]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lectures 33 and 34 (video lectures and problem sets; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->

Two problems about point clouds. From the distances alone, can we recover the points? (Yes, up to a rigid motion, when a Gram matrix is positive semidefinite.) Given two clouds with matched points, which rotation brings one closest to the other? (The orthogonal factor from an SVD.)

::: {#thm-points-from-distances .theorem name="Points from their distances"}

Let $d_{ij}\ge0$ be given for $i,j=1,\dots,N$, with $d_{ii}=0$ and $d_{ij}=d_{ji}$. Define the $N\times N$ matrix
$$G_{ij}=\tfrac12\big(d_{1i}^2+d_{1j}^2-d_{ij}^2\big).$$
There are points $\mathbf{x}_1,\dots,\mathbf{x}_N\in\mathbb{R}^k$ with $\lVert\mathbf{x}_i-\mathbf{x}_j\rVert=d_{ij}$ for all $i,j$ if and only if $G$ is positive semidefinite with rank at most $k$. Then $G$ is the Gram matrix $G_{ij}=\mathbf{x}_i^{\mathsf T}\mathbf{x}_j$ of the points placed with $\mathbf{x}_1=\mathbf{0}$, and the points are unique up to a rotation or reflection.

:::

::: {.proof}

1. Suppose the points exist; translate so that $\mathbf{x}_1=\mathbf{0}$. Then $\lVert\mathbf{x}_i\rVert^2=d_{1i}^2$, and expanding $d_{ij}^2=\lVert\mathbf{x}_i\rVert^2+\lVert\mathbf{x}_j\rVert^2-2\mathbf{x}_i^{\mathsf T}\mathbf{x}_j$ gives $\mathbf{x}_i^{\mathsf T}\mathbf{x}_j=G_{ij}$.

2. So $G=X^{\mathsf T}X$ where the columns of the $k\times N$ matrix $X$ are the points; such a matrix is positive semidefinite with rank at most $k$.

3. Conversely, if $G$ is positive semidefinite of rank $r\le k$, write $G=Q\Lambda Q^{\mathsf T}$ and let $Y=\Lambda_r^{1/2}Q_r^{\mathsf T}$ ($r\times N$, using the $r$ positive eigenvalues). Then $G=Y^{\mathsf T}Y$; pad the columns $\mathbf{y}_i$ with zeros to lie in $\mathbb{R}^k$.

4. Check the distances: $\lVert\mathbf{y}_i-\mathbf{y}_j\rVert^2=G_{ii}+G_{jj}-2G_{ij}=d_{1i}^2+d_{1j}^2-(d_{1i}^2+d_{1j}^2-d_{ij}^2)=d_{ij}^2$, using $G_{ii}=d_{1i}^2$.

5. If $X^{\mathsf T}X=Y^{\mathsf T}Y$, the map $\mathbf{y}_i\mapsto\mathbf{x}_i$ preserves all inner products, so it extends to an orthogonal map on the span of the $\mathbf{y}_i$.

:::

::: {#exm-points-from-distances .example name="A triangle and a non-triangle"}

Three points at mutual distance $1$: $G=\begin{bmatrix}0&0&0\\0&1&\frac12\\0&\frac12&1\end{bmatrix}$ has eigenvalues $0,\frac12,\frac32$, so rank $2$: an equilateral triangle in the plane, e.g. $\mathbf{x}_2=(1,0)$, $\mathbf{x}_3=(\frac12,\frac{\sqrt3}2)$.

With $d_{12}=d_{23}=1$ and $d_{13}=3$ the triangle inequality fails, and indeed the lower $2\times2$ block of $G$ is $\begin{bmatrix}1&4.5\\4.5&9\end{bmatrix}$ with determinant $-11.25<0$, so $G$ is not positive semidefinite.

:::

::: {#thm-orthogonal-procrustes .theorem name="Orthogonal Procrustes problem"}

Let $X$ and $Y$ be $N\times d$ matrices (row $i$ of each is the $i$-th point of a cloud in $\mathbb{R}^d$). Write the SVD $Y^{\mathsf T}X=U\Sigma V^{\mathsf T}$. Among orthogonal $d\times d$ matrices $Q$,
$$Q=UV^{\mathsf T}\quad\text{minimises}\quad\lVert X-YQ\rVert_F .$$

:::

::: {.proof}

1. $\lVert X-YQ\rVert_F^2=\operatorname{tr}\big((X-YQ)^{\mathsf T}(X-YQ)\big)=\lVert X\rVert_F^2+\lVert YQ\rVert_F^2-2\operatorname{tr}(Q^{\mathsf T}Y^{\mathsf T}X)$, and $\lVert YQ\rVert_F=\lVert Y\rVert_F$ (@thm-matrix-norms-singular-values). So we maximise $\operatorname{tr}(Q^{\mathsf T}Y^{\mathsf T}X)$.

2. $\operatorname{tr}(Q^{\mathsf T}U\Sigma V^{\mathsf T})=\operatorname{tr}(V^{\mathsf T}Q^{\mathsf T}U\,\Sigma)=\operatorname{tr}(Z\Sigma)$ with $Z=V^{\mathsf T}Q^{\mathsf T}U$, which is orthogonal.

3. $\operatorname{tr}(Z\Sigma)=\sum_iz_{ii}\sigma_i\le\sum_i\sigma_i$, because each entry of an orthogonal matrix has $\lvert z_{ii}\rvert\le1$ (its columns are unit vectors).

4. Equality holds for $Z=I$, that is $Q^{\mathsf T}=VU^{\mathsf T}$, or $Q=UV^{\mathsf T}$.

:::

::: {#rmk-distance-matrices-and-procrustes-1 .remark name="Uses"}

Recovering points from distances is *multidimensional scaling*; with noisy distances one keeps the top $k$ eigenvalues of $G$ (@thm-eckart-young-frobenius) to get the best $k$-dimensional picture. Procrustes aligns two such pictures, or two shapes, scans or word embeddings, before they are compared; centring both clouds first also removes the translation.

:::
