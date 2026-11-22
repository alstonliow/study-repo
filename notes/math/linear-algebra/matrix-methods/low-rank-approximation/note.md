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

::: {#fig-low-rank-approximation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, muted] (0,0) -- (4.2,0) node[right, lab, tick] {$i$}; \draw[->, muted] (0,0) -- (0,2.8) node[above, lab, tick] {$\sigma_i$};
\draw[bar] (0.15,0) rectangle (0.50,2.50); \node[lab, tick] at (0.32,-0.2) {1};
\draw[bar] (0.75,0) rectangle (1.10,1.60); \node[lab, tick] at (0.92,-0.2) {2};
\draw[cell, fill=accentLight] (1.35,0) rectangle (1.70,0.70); \node[lab, tick] at (1.52,-0.2) {3};
\draw[cell, fill=accentLight] (1.95,0) rectangle (2.30,0.40); \node[lab, tick] at (2.12,-0.2) {4};
\draw[cell, fill=accentLight] (2.55,0) rectangle (2.90,0.20); \node[lab, tick] at (2.72,-0.2) {5};
\draw[cell, fill=accentLight] (3.15,0) rectangle (3.50,0.10); \node[lab, tick] at (3.32,-0.2) {6};
\draw[faint, dashed] (1.3,0) -- (1.3,2.6) node[above, lab, note] {keep $k=2$};
\node[lab, note, anchor=west, align=left] at (4.4,1.3) {$\lVert A-A_k\rVert_2=\sigma_{k+1}$\\$\lVert A-A_k\rVert_F=\sqrt{\sigma_{k+1}^2+\dots+\sigma_r^2}$};
\end{tikzpicture}
\end{center}
```

Eckart–Young with made-up singular values: the best rank $k$ approximation keeps the $k$ largest terms $\sigma_i\mathbf u_i\mathbf v_i^{\mathsf T}$ of the SVD (blue). The error is measured by the discarded singular values (red).

:::

::: {#exm-eckart-young .example name="Best rank one approximation"}

$A=\begin{bmatrix}3&0\\4&5\end{bmatrix}$ has $\sigma_1=3\sqrt5$, $\mathbf{u}_1=(1,3)/\sqrt{10}$, $\mathbf{v}_1=(1,1)/\sqrt2$ (@exm-svd-two-by-two). So
$$A_1=\sigma_1\mathbf{u}_1\mathbf{v}_1^{\mathsf T}=\begin{bmatrix}1.5&1.5\\4.5&4.5\end{bmatrix},\qquad \lVert A-A_1\rVert_2=\lVert A-A_1\rVert_F=\sigma_2=\sqrt5 .$$

:::

::: {#fig-low-rank-approximation-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$3$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$0$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$4$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$5$};
\node[lab, note] at (0.550,-0.350) {$A$};
\node[lab] at (1.35,0.55) {$\approx$};
\draw[cell, fill=primaryLight] (1.700,0.550) rectangle (2.250,1.100);
\node[lab] at (1.975,0.825) {$1.5$};
\draw[cell, fill=primaryLight] (2.250,0.550) rectangle (2.800,1.100);
\node[lab] at (2.525,0.825) {$1.5$};
\draw[cell, fill=primaryLight] (1.700,0.000) rectangle (2.250,0.550);
\node[lab] at (1.975,0.275) {$4.5$};
\draw[cell, fill=primaryLight] (2.250,0.000) rectangle (2.800,0.550);
\node[lab] at (2.525,0.275) {$4.5$};
\node[lab, note] at (2.250,-0.350) {$A_1=\sigma_1\mathbf u_1\mathbf v_1^{\mathsf T}$};
\node[lab, note, anchor=west, align=left] at (3.2,0.55) {rank one: column $(1,3)$ times row $(1.5,1.5)$\\error $\lVert A-A_1\rVert_2=\sigma_2=\sqrt5$};
\end{tikzpicture}
\end{center}
```

@exm-eckart-young: the best rank one approximation of $A$ has equal columns, both multiples of $\mathbf u_1$; no matrix of rank one is closer in the spectral or the Frobenius norm.

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

::: {#fig-low-rank-approximation-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[emph, primary] (-1.7,-1.0) -- (1.7,1.0);
\draw[accent] (-1.4,-0.9) -- (-1.400,-0.824); \fill[ink] (-1.4,-0.9) circle[pt];
\draw[accent] (-0.6,0.2) -- (-0.600,-0.353); \fill[ink] (-0.6,0.2) circle[pt];
\draw[accent] (0.3,-0.1) -- (0.300,0.176); \fill[ink] (0.3,-0.1) circle[pt];
\draw[accent] (0.8,0.9) -- (0.800,0.471); \fill[ink] (0.8,0.9) circle[pt];
\draw[accent] (1.2,0.4) -- (1.200,0.706); \fill[ink] (1.2,0.4) circle[pt];
\node[lab, note] at (0,-1.5) {least squares: vertical errors};
\end{scope}
\begin{scope}[shift={(4.2,0)}]
\draw[emph, primary] (-1.7,-1.0) -- (1.7,1.0);
\draw[accent] (-1.4,-0.9) -- (-1.433,-0.843); \fill[ink] (-1.4,-0.9) circle[pt];
\draw[accent] (-0.6,0.2) -- (-0.358,-0.211); \fill[ink] (-0.6,0.2) circle[pt];
\draw[accent] (0.3,-0.1) -- (0.179,0.105); \fill[ink] (0.3,-0.1) circle[pt];
\draw[accent] (0.8,0.9) -- (0.988,0.581); \fill[ink] (0.8,0.9) circle[pt];
\draw[accent] (1.2,0.4) -- (1.066,0.627); \fill[ink] (1.2,0.4) circle[pt];
\node[lab, note] at (0,-1.5) {PCA: perpendicular distances};
\end{scope}
\end{tikzpicture}
\end{center}
```

The same line measured in the two ways compared in the remark above. Least squares treats one coordinate as the output and measures errors in it; PCA treats the coordinates alike and measures distances to the line. The minimisers are different lines in general.

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
