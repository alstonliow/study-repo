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

::: {#fig-distance-matrices-and-procrustes-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[ink] (0,0) circle[pt] node[below left, lab] {$\mathbf x_1=\mathbf 0$};
\fill[ink] (3,0) circle[pt] node[below right, lab] {$\mathbf x_i$}; \fill[ink] (1.2,2) circle[pt] node[above, lab] {$\mathbf x_j$};
\draw[emph, primary] (0,0) -- node[below, lab, note] {$d_{1i}$} (3,0); \draw[emph, primary] (0,0) -- node[left, lab, note] {$d_{1j}$} (1.2,2); \draw[emph, accent] (3,0) -- node[above right, lab, note] {$d_{ij}$} (1.2,2);
\node[lab, note, anchor=west, align=left] at (3.8,1.0) {law of cosines:\\$\mathbf x_i\cdot\mathbf x_j=\tfrac12\big(d_{1i}^2+d_{1j}^2-d_{ij}^2\big)$\\fills the Gram matrix $G$};
\end{tikzpicture}
\end{center}
```

From distances to dot products: placing $\mathbf x_1$ at the origin, each dot product $\mathbf x_i\cdot\mathbf x_j$ is fixed by three distances. Factoring $G=X^{\mathsf T}X$ then recovers the points up to a rotation.

:::

::: {#exm-points-from-distances .example name="A triangle and a non-triangle"}

Three points at mutual distance $1$: $G=\begin{bmatrix}0&0&0\\0&1&\frac12\\0&\frac12&1\end{bmatrix}$ has eigenvalues $0,\frac12,\frac32$, so rank $2$: an equilateral triangle in the plane, e.g. $\mathbf{x}_2=(1,0)$, $\mathbf{x}_3=(\frac12,\frac{\sqrt3}2)$.

With $d_{12}=d_{23}=1$ and $d_{13}=3$ the triangle inequality fails, and indeed the lower $2\times2$ block of $G$ is $\begin{bmatrix}1&4.5\\4.5&9\end{bmatrix}$ with determinant $-11.25<0$, so $G$ is not positive semidefinite.

:::

::: {#fig-distance-matrices-and-procrustes-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2,0) -- (1,1.732) -- cycle; \draw[emph, primary] (0,0) -- (2,0) -- (1,1.732) -- cycle;
\fill[ink] (0,0) circle[pt] node[below, lab, tick] {$\mathbf x_1$}; \fill[ink] (2,0) circle[pt] node[below, lab, tick] {$\mathbf x_2$}; \fill[ink] (1,1.732) circle[pt] node[above, lab, tick] {$\mathbf x_3$};
\node[lab, note] at (1,-0.6) {$1,1,1$: realisable};
\begin{scope}[shift={(3.6,0)}]
\draw[emph, primary] (0,0) -- (2,0); \draw[emph, primary] (2,0) -- (2.6,0.8);
\draw[emph, accent, dashed] (0,0) -- (6,0);
\fill[ink] (0,0) circle[pt] node[below, lab, tick] {$\mathbf x_1$}; \fill[ink] (2,0) circle[pt] node[below, lab, tick] {$\mathbf x_2$};
\node[lab, note, accent] at (4.5,0.3) {need $3$, at most $1+1=2$}; \node[lab, note] at (3,-0.6) {$1,1,3$: no points exist};
\end{scope}
\end{tikzpicture}
\end{center}
```

The two cases of @exm-points-from-distances (drawn at scale $2$). Equal distances give an equilateral triangle and a positive semidefinite $G$ of rank $2$; distances $1,1,3$ break the triangle inequality and $G$ has a negative eigenvalue.

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

::: {#fig-distance-matrices-and-procrustes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0.00,0.00) -- (1.40,0.20) -- (0.50,1.10) -- cycle;
\node[dot] at (0.00,0.00) {}; \node[lab, tick, below right] at (0.00,0.00) {$1$};
\node[dot] at (1.40,0.20) {}; \node[lab, tick, below right] at (1.40,0.20) {$2$};
\node[dot] at (0.50,1.10) {}; \node[lab, tick, below right] at (0.50,1.10) {$3$};
\draw[faint] (4.00,0.00) -- (4.29,1.38) -- (3.14,0.85) -- cycle;
\node[hl dot] at (4.00,0.00) {}; \node[lab, tick, below right] at (4.00,0.00) {$1$};
\node[hl dot] at (4.29,1.38) {}; \node[lab, tick, below right] at (4.29,1.38) {$2$};
\node[hl dot] at (3.14,0.85) {}; \node[lab, tick, below right] at (3.14,0.85) {$3$};
\node[lab, below] at (0.7,-0.3) {cloud $X$}; \node[lab, below] at (3.7,-0.3) {cloud $Y$};
\draw[map] (3.0,1.4) to[bend right=30] node[lab, above] {$Q$} (1.4,1.4);
\end{tikzpicture}
\end{center}
```

Two labelled point clouds that differ by a rotation. Procrustes finds the orthogonal $Q$ that best turns $Y$ onto $X$ point by point; with noise the fit is not exact and $Q=UV^{\mathsf T}$ minimises the total squared error.

:::

::: {#rmk-distance-matrices-and-procrustes-1 .remark name="Uses"}

Recovering points from distances is *multidimensional scaling*; with noisy distances one keeps the top $k$ eigenvalues of $G$ (@thm-eckart-young-frobenius) to get the best $k$-dimensional picture. Procrustes aligns two such pictures, or two shapes, scans or word embeddings, before they are compared; centring both clouds first also removes the translation.

:::
