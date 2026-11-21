---
title: "Low-Rank Approximation and PCA"
sources: [mit18065-7, mit18065-17, mit1806-29]
requires: [math/linear-algebra/matrix-methods/matrix-norms, math/linear-algebra/matrix-methods/eigenvalue-perturbation-and-interlacing]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lectures 7 and 17 (video lectures and problem sets; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->
<!-- Merged 2026-11-21 (owner): thm-eckart-young-spectral also replaces the Eckart–Young statement (without proof) that the SVD note made in a remark, from MIT 18.06SC Lecture 29; statement and proof are the 18.065 version. -->

Cutting the SVD after $k$ terms,
$$A_k=\sigma_1\mathbf{u}_1\mathbf{v}_1^{\mathsf T}+\dots+\sigma_k\mathbf{u}_k\mathbf{v}_k^{\mathsf T},$$
gives the best rank $k$ approximation to $A$ in the spectral and Frobenius norms. Applied to a centred data matrix, this is principal component analysis. $A$ is $m\times n$ with SVD $A=U\Sigma V^{\mathsf T}$ (@thm-svd), $\sigma_i=0$ for $i>r$.

::: {#lem-singular-values-after-rank-k .lemma name="Removing rank k lowers singular values by at most k places"}

If $\operatorname{rank}B\le k$, then $\sigma_i(A-B)\ge\sigma_{i+k}(A)$ for every $i$.

:::

::: {.proof}

1. By @thm-courant-fischer applied to $M^{\mathsf T}M$, $\sigma_i(M)^2=\max_{\dim Y=i}\min_{\mathbf{x}\in Y\setminus\{\mathbf{0}\}}\lVert M\mathbf{x}\rVert^2/\lVert\mathbf{x}\rVert^2$.

2. Let $Y=\operatorname{span}(\mathbf{v}_1,\dots,\mathbf{v}_{i+k})$. There $\lVert A\mathbf{x}\rVert\ge\sigma_{i+k}\lVert\mathbf{x}\rVert$.

3. $N(B)$ has dimension at least $n-k$, so $Y\cap N(B)$ has dimension at least $i$.

4. For $\mathbf{x}$ in $Y\cap N(B)$, $(A-B)\mathbf{x}=A\mathbf{x}$, so $\lVert(A-B)\mathbf{x}\rVert\ge\sigma_{i+k}(A)\lVert\mathbf{x}\rVert$. An $i$-dimensional subspace of $Y\cap N(B)$ in step 1 gives $\sigma_i(A-B)\ge\sigma_{i+k}(A)$.

:::

::: {#thm-eckart-young-spectral .theorem name="Eckart–Young in the spectral norm"}

For every $B$ of rank at most $k$,
$$\lVert A-B\rVert_2\ge\lVert A-A_k\rVert_2=\sigma_{k+1}.$$

:::

::: {.proof}

1. $A-A_k=\sum_{i>k}\sigma_i\mathbf{u}_i\mathbf{v}_i^{\mathsf T}$ has largest singular value $\sigma_{k+1}$, so $\lVert A-A_k\rVert_2=\sigma_{k+1}$ (@thm-matrix-norms-singular-values).

2. @lem-singular-values-after-rank-k with $i=1$ gives $\lVert A-B\rVert_2=\sigma_1(A-B)\ge\sigma_{k+1}$.

:::

::: {#thm-eckart-young-frobenius .theorem name="Eckart–Young in the Frobenius norm"}

For every $B$ of rank at most $k$,
$$\lVert A-B\rVert_F^2\ge\lVert A-A_k\rVert_F^2=\sigma_{k+1}^2+\dots+\sigma_r^2 .$$

:::

::: {.proof}

1. $\lVert A-A_k\rVert_F^2$ is the sum of squares of the singular values $\sigma_{k+1},\dots,\sigma_r$ of $A-A_k$.

2. By @lem-singular-values-after-rank-k, $\lVert A-B\rVert_F^2=\sum_i\sigma_i(A-B)^2\ge\sum_{i\ge1}\sigma_{i+k}(A)^2$, which is the same sum.

:::

::: {#exm-eckart-young .example name="Best rank one approximation"}

$A=\begin{bmatrix}3&0\\4&5\end{bmatrix}$ has $\sigma_1=3\sqrt5$, $\mathbf{u}_1=(1,3)/\sqrt{10}$, $\mathbf{v}_1=(1,1)/\sqrt2$ (@exm-svd-two-by-two). So
$$A_1=\sigma_1\mathbf{u}_1\mathbf{v}_1^{\mathsf T}=\begin{bmatrix}1.5&1.5\\4.5&4.5\end{bmatrix},\qquad \lVert A-A_1\rVert_2=\lVert A-A_1\rVert_F=\sigma_2=\sqrt5 .$$

:::

::: {#def-principal-components .definition name="Principal components"}

Let the columns of the $m\times N$ matrix $X$ be $N$ samples of $m$ variables, each row centred to mean zero. The *sample covariance matrix* is
$$S=\frac{1}{N-1}XX^{\mathsf T}.$$
If $X=U\Sigma V^{\mathsf T}$, the *principal directions* are $\mathbf{u}_1,\mathbf{u}_2,\dots$, and the variance of the data along $\mathbf{u}_i$ is $\sigma_i^2/(N-1)$, the $i$-th eigenvalue of $S$.

:::

::: {#thm-pca-best-subspace .theorem name="PCA finds the closest subspace"}

Among all $k$-dimensional subspaces of $\mathbb{R}^m$, $\operatorname{span}(\mathbf{u}_1,\dots,\mathbf{u}_k)$ minimises the sum of squared distances from the $N$ data points (columns of $X$) to the subspace. The minimum is $\sigma_{k+1}^2+\dots+\sigma_r^2$.

:::

::: {.proof}

1. Let $P$ project onto a $k$-dimensional subspace. The squared distances add to $\lVert X-PX\rVert_F^2$, and $PX$ has rank at most $k$.

2. By @thm-eckart-young-frobenius, $\lVert X-PX\rVert_F^2\ge\sigma_{k+1}^2+\dots+\sigma_r^2$.

3. For $P=U_kU_k^{\mathsf T}$ (first $k$ columns of $U$), $PX=X_k$, which attains the bound.

:::

::: {#exm-pca-small-data .example name="Four points in the plane"}

The centred points $(2,1),(-1,0),(0,-1),(-1,0)$ give $XX^{\mathsf T}=\begin{bmatrix}6&2\\2&2\end{bmatrix}$ and $S=XX^{\mathsf T}/3$ with eigenvalues $(4\pm2\sqrt2)/3\approx2.276,\ 0.391$. The first principal direction is $\mathbf{u}_1=(\cos\frac{\pi}{8},\sin\frac{\pi}{8})$, since $\tan\frac{\pi}{8}=\sqrt2-1$ solves $(6-\lambda_1)x+2y=0$. It carries $2.276/2.667\approx85\%$ of the total variance $\operatorname{tr}S$.

:::

::: {#fig-low-rank-approximation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.2,0) -- (2.7,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.6) -- (0,1.7) node[lab, above] {$y$};
\draw[hl] (-2.03,-0.84) -- (2.40,0.99) node[lab, right] {$\mathbf{u}_1$};
\draw[faint, dashed] (-1,0) -- (-0.85,-0.35);
\fill (-1,0) circle (2pt);
\draw[faint, dashed] (0,-1) -- (-0.35,-0.15);
\fill (0,-1) circle (2pt);
\draw[faint, dashed] (2,1) -- (2.06,0.85);
\fill (2,1) circle (2pt);
\node[lab, below left] at (-1,0) {$\times2$};
\end{tikzpicture}
\end{center}
```

The four centred points (one repeated) and the first principal direction $\mathbf{u}_1$ at angle $\pi/8$. PCA minimises the sum of squared perpendicular distances (dashed); here it is $\sigma_2^2\approx1.17$.

:::

::: {#rmk-low-rank-approximation-1 .remark name="PCA is not least squares"}

Least squares (@def-least-squares-solution) measures vertical errors in the last variable only; PCA measures perpendicular distances and treats all variables alike. The two best-fit lines differ in general. PCA also depends on the units: rescaling one variable changes the principal directions, so variables are often standardised first.

:::

::: {#def-sylvester-equation .definition name="Sylvester equation"}

For square $A$ ($m\times m$), $B$ ($n\times n$) and $C$ ($m\times n$), the *Sylvester equation* for the unknown $m\times n$ matrix $X$ is
$$AX-XB=C .$$

:::

::: {#prp-sylvester-equation-unique .proposition name="Unique solution when the spectra are disjoint"}

If $A=P\Lambda P^{-1}$ and $B=QMQ^{-1}$ are diagonalisable and no eigenvalue $\lambda_i$ of $A$ equals an eigenvalue $\mu_j$ of $B$, then $AX-XB=C$ has exactly one solution.

:::

::: {.proof}

1. Set $Y=P^{-1}XQ$ and $D=P^{-1}CQ$. Multiplying the equation by $P^{-1}$ on the left and $Q$ on the right gives $\Lambda Y-YM=D$.

2. Entry $(i,j)$ of this reads $(\lambda_i-\mu_j)y_{ij}=d_{ij}$.

3. Every $\lambda_i-\mu_j\ne0$, so $y_{ij}=d_{ij}/(\lambda_i-\mu_j)$ is forced, and $X=PYQ^{-1}$ is the unique solution.

:::

::: {#rmk-low-rank-approximation-2 .remark name="Why many matrices are nearly low rank"}

When $C$ has low rank and the eigenvalues of $A$ and $B$ lie in well-separated sets, the solution $X$ of a Sylvester equation has singular values that decrease geometrically, so $X$ is close to a low-rank matrix by @thm-eckart-young-spectral. Hilbert, Cauchy and Vandermonde matrices satisfy such equations with $\operatorname{rank}C=1$, which explains their tiny trailing singular values and their huge condition numbers (@exm-condition-number-hilbert).

:::
