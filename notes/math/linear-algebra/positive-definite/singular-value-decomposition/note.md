---
title: "Singular Value Decomposition"
sources: [mit1806-29]
requires: [math/linear-algebra/positive-definite/positive-definite-matrices]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 29, in our own wording; proofs written out in steps. Example numbers checked with numpy. -->

Diagonalization $A=S\Lambda S^{-1}$ needs a square matrix with enough eigenvectors, and $S$ is usually not orthogonal. The SVD works for every matrix and uses orthonormal bases on both sides.

::: {#thm-svd .theorem name="Singular value decomposition"}

Every real $m\times n$ matrix $A$ of rank $r$ can be written as
$$A=U\Sigma V^{\mathsf T}=\sigma_1\mathbf{u}_1\mathbf{v}_1^{\mathsf T}+\dots+\sigma_r\mathbf{u}_r\mathbf{v}_r^{\mathsf T},$$
where $U$ ($m\times m$) and $V$ ($n\times n$) are orthogonal, and $\Sigma$ ($m\times n$) has the *singular values* $\sigma_1\ge\dots\ge\sigma_r>0$ on its diagonal and zeros elsewhere. Then
$$A\mathbf{v}_i=\sigma_i\mathbf{u}_i\quad(i\le r),\qquad A\mathbf{v}_i=\mathbf{0}\quad(i>r).$$

:::

::: {.proof}

1. $A^{\mathsf T}A$ is symmetric and positive semidefinite ($\mathbf{x}^{\mathsf T}A^{\mathsf T}A\mathbf{x}=\lVert A\mathbf{x}\rVert^2\ge0$), so by @cor-real-symmetric-orthogonally-diagonalisable it has orthonormal eigenvectors $\mathbf{v}_1,\dots,\mathbf{v}_n$ with eigenvalues $\lambda_i\ge0$, ordered decreasingly. It has rank $r$ (@thm-ata-invertible), so exactly $r$ of them are positive. Set $\sigma_i=\sqrt{\lambda_i}$.

2. For $i\le r$ let $\mathbf{u}_i=A\mathbf{v}_i/\sigma_i$. These are orthonormal: $\mathbf{u}_i^{\mathsf T}\mathbf{u}_j=\mathbf{v}_i^{\mathsf T}A^{\mathsf T}A\mathbf{v}_j/(\sigma_i\sigma_j)=\lambda_j\mathbf{v}_i^{\mathsf T}\mathbf{v}_j/(\sigma_i\sigma_j)$, which is $1$ for $i=j$ and $0$ otherwise.

3. For $i>r$, $\lVert A\mathbf{v}_i\rVert^2=\lambda_i=0$, so $A\mathbf{v}_i=\mathbf{0}$.

4. Extend $\mathbf{u}_1,\dots,\mathbf{u}_r$ to an orthonormal basis of $\mathbb{R}^m$. Then $AV=U\Sigma$ column by column, and $A=U\Sigma V^{\mathsf T}$ because $V^{-1}=V^{\mathsf T}$.

:::

::: {#cor-svd-four-subspaces .corollary name="The SVD and the four subspaces"}

$\mathbf{v}_1,\dots,\mathbf{v}_r$ is an orthonormal basis of the row space $C(A^{\mathsf T})$ and $\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ of $N(A)$; $\mathbf{u}_1,\dots,\mathbf{u}_r$ is an orthonormal basis of $C(A)$ and $\mathbf{u}_{r+1},\dots,\mathbf{u}_m$ of $N(A^{\mathsf T})$. Moreover $AA^{\mathsf T}\mathbf{u}_i=\sigma_i^2\mathbf{u}_i$.

:::

::: {.proof}

1. $\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ are $n-r$ orthonormal vectors in $N(A)$, a space of dimension $n-r$, so they are a basis. The other $\mathbf{v}$'s are orthogonal to them, so they lie in $N(A)^{\perp}=C(A^{\mathsf T})$ (@thm-fundamental-theorem-orthogonality), and there are $r=\dim C(A^{\mathsf T})$ of them.

2. $\mathbf{u}_i=A\mathbf{v}_i/\sigma_i\in C(A)$ for $i\le r$, and $\dim C(A)=r$. The remaining $\mathbf{u}$'s are orthogonal to $C(A)$, so they lie in $N(A^{\mathsf T})$, of dimension $m-r$.

3. $AA^{\mathsf T}\mathbf{u}_i=AA^{\mathsf T}A\mathbf{v}_i/\sigma_i=A(\sigma_i^2\mathbf{v}_i)/\sigma_i=\sigma_i^2\mathbf{u}_i$.

:::

::: {#exm-svd-two-by-two .example name="SVD of a 2 by 2 matrix"}

For $A=\begin{bmatrix}3&0\\4&5\end{bmatrix}$: $A^{\mathsf T}A=\begin{bmatrix}25&20\\20&25\end{bmatrix}$ has eigenvalues $45$ and $5$ with $\mathbf{v}_1=\frac1{\sqrt2}(1,1)$, $\mathbf{v}_2=\frac1{\sqrt2}(-1,1)$. So $\sigma_1=3\sqrt5$ and $\sigma_2=\sqrt5$, and
$$\mathbf{u}_1=\frac{A\mathbf{v}_1}{\sigma_1}=\frac1{\sqrt{10}}(1,3),\qquad \mathbf{u}_2=\frac{A\mathbf{v}_2}{\sigma_2}=\frac1{\sqrt{10}}(-3,1).$$
Check: $\sigma_1\sigma_2=15=\lvert\det A\rvert$.

:::

::: {#fig-singular-value-decomposition-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,0) circle (0.9);
\draw[->, hl] (0.000,0.000) -- (-0.636,-0.636);
\node[lab, above right] at (-0.636,-0.636) {$\mathbf v_1$};
\draw[->, hl] (0.000,0.000) -- (-0.636,0.636);
\node[lab, above left] at (-0.636,0.636) {$\mathbf v_2$};
\node[lab] at (0,-1.3) {unit circle};
\draw[->] (1.4,0) -- node[lab, above] {$A$} (2.4,0);
\draw[emph] (5.060,0.880) -- (5.057,0.973) -- (5.050,1.058) -- (5.038,1.135) -- (5.020,1.203) -- (4.998,1.262) -- (4.972,1.312) -- (4.941,1.352) -- (4.906,1.381) -- (4.867,1.400) -- (4.824,1.408) -- (4.779,1.406) -- (4.730,1.393) -- (4.679,1.369) -- (4.626,1.335) -- (4.571,1.290) -- (4.515,1.236) -- (4.458,1.173) -- (4.400,1.100) -- (4.342,1.019) -- (4.285,0.930) -- (4.229,0.835) -- (4.174,0.733) -- (4.121,0.625) -- (4.070,0.513) -- (4.021,0.396) -- (3.976,0.277) -- (3.933,0.156) -- (3.894,0.033) -- (3.859,-0.090) -- (3.828,-0.212) -- (3.802,-0.333) -- (3.780,-0.451) -- (3.762,-0.565) -- (3.750,-0.676) -- (3.743,-0.781) -- (3.740,-0.880) -- (3.743,-0.973) -- (3.750,-1.058) -- (3.762,-1.135) -- (3.780,-1.203) -- (3.802,-1.262) -- (3.828,-1.312) -- (3.859,-1.352) -- (3.894,-1.381) -- (3.933,-1.400) -- (3.976,-1.408) -- (4.021,-1.406) -- (4.070,-1.393) -- (4.121,-1.369) -- (4.174,-1.335) -- (4.229,-1.290) -- (4.285,-1.236) -- (4.342,-1.173) -- (4.400,-1.100) -- (4.458,-1.019) -- (4.515,-0.930) -- (4.571,-0.835) -- (4.626,-0.733) -- (4.679,-0.625) -- (4.730,-0.513) -- (4.779,-0.396) -- (4.824,-0.277) -- (4.867,-0.156) -- (4.906,-0.033) -- (4.941,0.090) -- (4.972,0.212) -- (4.998,0.333) -- (5.020,0.451) -- (5.038,0.565) -- (5.050,0.676) -- (5.057,0.781) -- (5.060,0.880) -- cycle;
\draw[->, hl] (4.400,0.000) -- (4.867,1.400);
\node[lab, right] at (4.867,1.400) {$\sigma_1\mathbf u_1$};
\draw[->, hl] (4.400,0.000) -- (3.933,0.156);
\node[lab, left] at (3.933,0.156) {$\sigma_2\mathbf u_2$};
\end{tikzpicture}
\end{center}
```

$A$ maps the unit circle to an ellipse; the orthonormal $\mathbf v_i$ go to the half-axes $\sigma_i\mathbf u_i$, with $\sigma_1=3\sqrt5$, $\sigma_2=\sqrt5$.

:::

::: {#rmk-singular-value-decomposition-1 .remark name="Geometry of the SVD"}

$A=U\Sigma V^{\mathsf T}$ says: rotate (by $V^{\mathsf T}$), stretch along the axes (by $\Sigma$), rotate again (by $U$). The unit circle goes to an ellipse with half-axes $\sigma_i\mathbf{u}_i$. Keeping only the first $k$ terms $\sigma_1\mathbf{u}_1\mathbf{v}_1^{\mathsf T}+\dots+\sigma_k\mathbf{u}_k\mathbf{v}_k^{\mathsf T}$ gives the best rank-$k$ approximation of $A$ (@thm-eckart-young-spectral); this is how images are compressed (@sec-math-linear-algebra-positive-definite-change-of-basis).

<!-- Merged 2026-11-21 (owner): the Eckart–Young statement this remark used to make without proof now lives only in thm-eckart-young-spectral (low-rank-approximation note); the geometric picture stays here. -->

:::
