---
title: "Principal Component Analysis as a Statistical Method"
sources: [mit18650-9]
requires: [math/linear-algebra/matrix-methods/low-rank-approximation, math/probability/random-variables/covariance-and-correlation]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 9 (covariance and empirical covariance matrices, the centring projector, directions of maximal spread, the PCA procedure and the choice of k, PCA for covariance estimation), in our own wording. The proofs and the numerical example are our own. The singular value view of PCA is in the low-rank approximation note; merge with def-principal-components (owner approved 2026-11-21): both kept, def-pca-procedure points to it for the principal directions. -->

Principal component analysis reduces $d$-dimensional data to $k<d$ dimensions while keeping as much of their spread as possible. The linear algebra note (@sec-math-linear-algebra-matrix-methods-low-rank-approximation) describes it through the singular value decomposition and closest subspaces; here the starting point is the covariance matrix, and the principal directions are the directions in which the data vary most.

::: {#def-covariance-matrix .definition name="Covariance matrix, empirical covariance matrix" related="def-covariance"}

Let $X=(X^{(1)},\dots,X^{(d)})^{\mathsf T}$ be a random vector with $E\|X\|^2<\infty$. Its *covariance matrix* is the $d\times d$ matrix $\Sigma$ with entries $\Sigma_{jk}=\operatorname{Cov}(X^{(j)},X^{(k)})$:
$$\Sigma=E\bigl[(X-E[X])(X-E[X])^{\mathsf T}\bigr]=E[XX^{\mathsf T}]-E[X]E[X]^{\mathsf T}.$$
For observations $X_1,\dots,X_n\in\mathbb{R}^d$ with mean $\bar X=\frac1n\sum_iX_i$, the *empirical covariance matrix* is
$$S=\frac1n\sum_{i=1}^n(X_i-\bar X)(X_i-\bar X)^{\mathsf T}=\frac1n\sum_{i=1}^nX_iX_i^{\mathsf T}-\bar X\bar X^{\mathsf T}.$$

:::

Stack the observations as the rows of $\mathbb X\in\mathbb{R}^{n\times d}$. Then $\bar X=\frac1n\mathbb X^{\mathsf T}\mathbf 1$ with $\mathbf 1\in\mathbb{R}^n$ the all-ones vector, and
$$S=\frac1n\mathbb X^{\mathsf T}H\mathbb X,\qquad H=I_n-\frac1n\mathbf 1\mathbf 1^{\mathsf T}.$$
$H$ is symmetric with $H^2=H$: it is the orthogonal projection onto the vectors with zero sum, and $H\mathbb X$ is the data matrix with each column centred.

::: {#prp-directional-variance .proposition name="Variance in a direction"}

For $u\in\mathbb{R}^d$:

1. $u^{\mathsf T}\Sigma u=\mathrm{Var}(u^{\mathsf T}X)$, and $u^{\mathsf T}Su$ is the empirical variance $\frac1n\sum_i(u^{\mathsf T}X_i-u^{\mathsf T}\bar X)^2$ of the projected data $u^{\mathsf T}X_1,\dots,u^{\mathsf T}X_n$;
2. hence $\Sigma$ and $S$ are symmetric positive semidefinite;
3. $u^{\mathsf T}Su=0$ if and only if all $X_i$ lie in the affine hyperplane $\{x:u^{\mathsf T}x=u^{\mathsf T}\bar X\}$, and $u^{\mathsf T}\Sigma u=0$ if and only if $X$ lies in such a hyperplane with probability $1$.

:::

::: {.proof}

1. $u^{\mathsf T}(X-E[X])(X-E[X])^{\mathsf T}u=\bigl(u^{\mathsf T}X-E[u^{\mathsf T}X]\bigr)^2$; taking expectations gives $\mathrm{Var}(u^{\mathsf T}X)$. The same computation with the empirical average in place of $E$ gives the statement for $S$.

2. Symmetry is clear from the definitions, and variances are non-negative.

3. An empirical variance is zero exactly when all the values are equal to their mean, and a variance is zero exactly when the variable equals its mean with probability $1$.

:::

So $u^{\mathsf T}Su$, for a unit vector $u$, measures how spread out the data are along $u$. By the spectral theorem (@cor-real-symmetric-orthogonally-diagonalisable) $S=PDP^{\mathsf T}$ with $P=(v_1,\dots,v_d)$ orthogonal and $D=\operatorname{diag}(\lambda_1,\dots,\lambda_d)$, $\lambda_1\ge\dots\ge\lambda_d\ge0$. The coordinates $P^{\mathsf T}X_i$ have empirical covariance $P^{\mathsf T}SP=D$: they are uncorrelated, with empirical variances $\lambda_1,\dots,\lambda_d$.

::: {#thm-pca-maximal-variance .theorem name="Principal directions maximise the variance"}

With $S=PDP^{\mathsf T}$ as above,

$$
v_1\in\operatorname*{argmax}_{\|u\|=1}u^{\mathsf T}Su,\qquad v_k\in\operatorname*{argmax}_{\substack{\|u\|=1\\ u\perp v_1,\dots,v_{k-1}}}u^{\mathsf T}Su\quad(k=2,\dots,d),
$$

and the maximal values are $\lambda_1,\dots,\lambda_d$. So the $k$ orthogonal directions of greatest spread are the eigenvectors of the $k$ largest eigenvalues of $S$.

:::

::: {.proof}

1. Write a unit vector $u$ in the eigenbasis, $u=\sum_jc_jv_j$ with $c=P^{\mathsf T}u$ and $\sum_jc_j^2=1$. Then $u^{\mathsf T}Su=c^{\mathsf T}Dc=\sum_j\lambda_jc_j^2$.

2. This is a weighted average of the $\lambda_j$ with weights $c_j^2$, so it is at most $\lambda_1$, with equality for $u=v_1$ ($c=e_1$).

3. If $u\perp v_1,\dots,v_{k-1}$, then $c_1=\dots=c_{k-1}=0$, and the average $\sum_{j\ge k}\lambda_jc_j^2$ is at most $\lambda_k$, with equality for $u=v_k$.

:::

::: {#def-pca-procedure .definition name="PCA procedure" related="def-principal-components"}

Given $X_1,\dots,X_n\in\mathbb{R}^d$ and a target dimension $k<d$: compute the empirical covariance $S$, its eigendecomposition $S=PDP^{\mathsf T}$ with decreasing eigenvalues (the principal directions of @def-principal-components, there computed from the singular value decomposition of the centred data), set $P_k=(v_1,\dots,v_k)\in\mathbb{R}^{d\times k}$, and output the *principal component scores*
$$Y_i=P_k^{\mathsf T}(X_i-\bar X)\in\mathbb{R}^k,\qquad i=1,\dots,n .$$
The ratio $(\lambda_1+\dots+\lambda_k)/(\lambda_1+\dots+\lambda_d)$ is the fraction of the *total variance* $\operatorname{tr}S$ *explained* by the first $k$ components.

:::

```{=latex}
\begin{algorithm}
\caption{Principal component analysis}
\begin{algorithmic}
\INPUT data $X_1,\dots,X_n\in\mathbb{R}^d$; a fraction $\tau\in(0,1)$ of variance to keep
\STATE $\bar X\gets\frac1n\sum_iX_i$; \quad $S\gets\frac1n\sum_i(X_i-\bar X)(X_i-\bar X)^{\mathsf T}$
\STATE compute $S=PDP^{\mathsf T}$ with $\lambda_1\ge\dots\ge\lambda_d$ and $P=(v_1,\dots,v_d)$
\STATE $k\gets$ the smallest $k$ with $(\lambda_1+\dots+\lambda_k)/\operatorname{tr}S\ge\tau$
\STATE $P_k\gets(v_1,\dots,v_k)$
\STATE \textbf{return} $Y_i=P_k^{\mathsf T}(X_i-\bar X)$ for $i=1,\dots,n$
\end{algorithmic}
\end{algorithm}
```

The procedure leaves $k$ to the user. Besides a threshold on the explained variance, two common rules are to look for an "elbow" in the plot of $\lambda_1,\lambda_2,\dots$ against their index (the *scree plot*), and, for visualisation, simply to take $k=2$ or $3$.

::: {#exm-pca-five-points .example name="Five points in the plane"}

The points $(1,2),(2,3),(3,3),(4,5),(5,7)$ have mean $(3,4)$ and empirical covariance
$$S=\begin{pmatrix}2&2.4\\2.4&3.2\end{pmatrix}.$$
Its eigenvalues are $2.6\pm\sqrt{0.36+5.76}$, that is $\lambda_1\approx5.074$ and $\lambda_2\approx0.126$, and the first principal direction is $v_1\approx(0.615,0.788)$. One component explains $5.074/5.2\approx97.6\%$ of the total variance, and the one-dimensional scores $v_1^{\mathsf T}(X_i-\bar X)$ are $-2.81,-1.40,-0.79,1.40,3.60$.

:::

::: {#fig-principal-component-analysis-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (3.90,0) node[lab, right] {$x_1$};
\draw[->] (0,0) -- (0,5.10) node[lab, above] {$x_2$};
\draw (0.600,0) -- (0.600,-0.07) node[lab, tick, below] {1};
\draw (1.800,0) -- (1.800,-0.07) node[lab, tick, below] {3};
\draw (3.000,0) -- (3.000,-0.07) node[lab, tick, below] {5};
\draw (0,1.200) -- (-0.07,1.200) node[lab, tick, left] {2};
\draw (0,2.400) -- (-0.07,2.400) node[lab, tick, left] {4};
\draw (0,3.600) -- (-0.07,3.600) node[lab, tick, left] {6};
\draw[emph, primary] (0.249,0.414) -- (3.425,4.481) node[lab, anchor=south west] {$v_1$};
\draw[faint] (0.600,1.200) -- (0.763,1.072);
\node[dot] at (0.600,1.200) {};
\node[hl dot] at (0.763,1.072) {};
\draw[faint] (1.200,1.800) -- (1.282,1.736);
\node[dot] at (1.200,1.800) {};
\node[hl dot] at (1.282,1.736) {};
\draw[faint] (1.800,1.800) -- (1.509,2.027);
\node[dot] at (1.800,1.800) {};
\node[hl dot] at (1.509,2.027) {};
\draw[faint] (2.400,3.000) -- (2.318,3.064);
\node[dot] at (2.400,3.000) {};
\node[hl dot] at (2.318,3.064) {};
\draw[faint] (3.000,4.200) -- (3.128,4.100);
\node[dot] at (3.000,4.200) {};
\node[hl dot] at (3.128,4.100) {};
\node[hollow dot] at (1.800,2.400) {};
\node[lab, anchor=north west] at (1.880,2.350) {$\bar X$};
\end{tikzpicture}
\end{center}
```

The five points (black), their mean $\bar X=(3,4)$ (hollow) and the first principal direction $v_1\approx(0.615,0.788)$ through it. The highlighted dots are the projections $\bar X+(v_1^{\mathsf T}(X_i-\bar X))v_1$; the short perpendicular segments carry only $2.4\%$ of the total variance.

:::

::: {#rmk-pca-estimation .remark name="PCA in estimation"}

PCA is used as a descriptive tool even for data that are not a random sample. In statistics it also serves estimation. For independent $X_i$ with covariance $\Sigma$, $S$ is a consistent estimator of $\Sigma$ when $n$ is large compared with $d$. If $\Sigma$ is known to have (nearly) low rank, the truncated matrix $P_kD_kP_k^{\mathsf T}$, keeping only the $k$ largest eigenvalues, is a better estimator than $S$ itself. When $n$ is small compared with $d$, as with gene expression data, $S$ is a poor estimator, and variants that force the principal directions to be sparse (*sparse PCA*) are used.

:::
