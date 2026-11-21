---
title: "Eigenvalue Perturbation and Interlacing"
sources: [mit18065-15, mit18065-16, mit18065-18]
requires: [math/linear-algebra/positive-definite/singular-value-decomposition]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lectures 15, 16 and 18 (video lectures and problem sets; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->

How do eigenvalues move when a matrix changes? For symmetric matrices the answer comes from one characterisation: each eigenvalue is a max–min of the Rayleigh quotient $R(\mathbf{x})=\mathbf{x}^{\mathsf T}S\mathbf{x}/\mathbf{x}^{\mathsf T}\mathbf{x}$. Throughout, a real symmetric $n\times n$ matrix $S$ has eigenvalues $\lambda_1(S)\ge\dots\ge\lambda_n(S)$ and orthonormal eigenvectors $\mathbf{q}_1,\dots,\mathbf{q}_n$ (@cor-real-symmetric-orthogonally-diagonalisable).

::: {#thm-courant-fischer .theorem name="Max–min principle (Courant–Fischer)"}

$$\lambda_i(S)=\max_{\dim Y=i}\ \min_{\mathbf{x}\in Y,\ \mathbf{x}\ne\mathbf{0}}\frac{\mathbf{x}^{\mathsf T}S\mathbf{x}}{\mathbf{x}^{\mathsf T}\mathbf{x}},$$
the maximum over subspaces $Y\subseteq\mathbb{R}^n$ of dimension $i$, attained by $Y=\operatorname{span}(\mathbf{q}_1,\dots,\mathbf{q}_i)$. In particular $\lambda_1=\max R(\mathbf{x})$ and $\lambda_n=\min R(\mathbf{x})$.

:::

::: {.proof}

1. Write $\mathbf{x}=\sum c_k\mathbf{q}_k$. Then $\mathbf{x}^{\mathsf T}\mathbf{x}=\sum c_k^2$ and $\mathbf{x}^{\mathsf T}S\mathbf{x}=\sum\lambda_kc_k^2$, so $R(\mathbf{x})$ is a weighted average of the $\lambda_k$ with weights $c_k^2$.

2. On $Y=\operatorname{span}(\mathbf{q}_1,\dots,\mathbf{q}_i)$ only $c_1,\dots,c_i$ are nonzero, so $R(\mathbf{x})\ge\lambda_i$, with equality at $\mathbf{q}_i$. Hence the max–min is at least $\lambda_i$.

3. Let $Y$ be any $i$-dimensional subspace and $Z=\operatorname{span}(\mathbf{q}_i,\dots,\mathbf{q}_n)$, of dimension $n-i+1$. Since $i+(n-i+1)>n$, $Y\cap Z$ contains some $\mathbf{x}\ne\mathbf{0}$.

4. That $\mathbf{x}$ has $c_1=\dots=c_{i-1}=0$, so $R(\mathbf{x})\le\lambda_i$. So the minimum over every $Y$ is at most $\lambda_i$.

:::

::: {#thm-weyl-inequality .theorem name="Weyl's inequality"}

For symmetric $S$ and $T$ and indices with $i+j-1\le n$,
$$\lambda_{i+j-1}(S+T)\le\lambda_i(S)+\lambda_j(T).$$
In particular $\lambda_i(S)+\lambda_n(T)\le\lambda_i(S+T)\le\lambda_i(S)+\lambda_1(T)$: adding a positive semidefinite $T$ cannot lower any eigenvalue.

:::

::: {.proof}

1. Let $W$ be spanned by the top $i+j-1$ eigenvectors of $S+T$, $V_1$ by the eigenvectors $i,\dots,n$ of $S$, and $V_2$ by the eigenvectors $j,\dots,n$ of $T$.

2. The dimensions add to $(i+j-1)+(n-i+1)+(n-j+1)=2n+1$, so the three subspaces share a vector $\mathbf{x}\ne\mathbf{0}$ (two intersections each lose at most $n$ dimensions).

3. As in step 1 of @thm-courant-fischer: on $W$, $R_{S+T}(\mathbf{x})\ge\lambda_{i+j-1}(S+T)$; on $V_1$, $R_S(\mathbf{x})\le\lambda_i(S)$; on $V_2$, $R_T(\mathbf{x})\le\lambda_j(T)$.

4. $R_{S+T}=R_S+R_T$, so $\lambda_{i+j-1}(S+T)\le\lambda_i(S)+\lambda_j(T)$.

5. For the lower bound apply the case $j=1$ to $S=(S+T)+(-T)$, using $\lambda_1(-T)=-\lambda_n(T)$.

:::

::: {#thm-rank-one-interlacing .theorem name="Interlacing for a rank one update"}

If $\mu_1\ge\dots\ge\mu_n$ are the eigenvalues of $S+\mathbf{u}\mathbf{u}^{\mathsf T}$, then
$$\mu_1\ge\lambda_1\ge\mu_2\ge\lambda_2\ge\dots\ge\mu_n\ge\lambda_n .$$

:::

::: {.proof}

1. $T=\mathbf{u}\mathbf{u}^{\mathsf T}$ is positive semidefinite with eigenvalues $\lVert\mathbf{u}\rVert^2,0,\dots,0$.

2. $\lambda_n(T)\ge0$, so @thm-weyl-inequality gives $\mu_i\ge\lambda_i$.

3. Weyl with $j=2$ gives $\mu_{i+1}\le\lambda_i+\lambda_2(T)=\lambda_i$.

:::

::: {#thm-cauchy-interlacing .theorem name="Cauchy interlacing"}

Let $B$ be $S$ with its last row and column removed, with eigenvalues $\beta_1\ge\dots\ge\beta_{n-1}$. Then
$$\lambda_1\ge\beta_1\ge\lambda_2\ge\beta_2\ge\dots\ge\beta_{n-1}\ge\lambda_n .$$

:::

::: {.proof}

1. Let $E=\{\mathbf{x}:x_n=0\}$. For $\mathbf{x}\in E$ with first $n-1$ components $\mathbf{y}$, $\mathbf{x}^{\mathsf T}S\mathbf{x}=\mathbf{y}^{\mathsf T}B\mathbf{y}$, so by @thm-courant-fischer $\beta_i$ is the max–min of $R_S$ over $i$-dimensional subspaces of $E$.

2. Subspaces of $E$ are among all subspaces of $\mathbb{R}^n$, so $\beta_i\le\lambda_i$.

3. $Y=\operatorname{span}(\mathbf{q}_1,\dots,\mathbf{q}_{i+1})\cap E$ has dimension at least $i$, and $R_S\ge\lambda_{i+1}$ on it. Any $i$-dimensional subspace of it shows $\beta_i\ge\lambda_{i+1}$.

:::

::: {#exm-rank-one-interlacing .example name="A rank one update of a diagonal matrix"}

$S=\operatorname{diag}(2,1)$ and $\mathbf{u}=(1,1)$ give $S+\mathbf{u}\mathbf{u}^{\mathsf T}=\begin{bmatrix}3&1\\1&2\end{bmatrix}$ with eigenvalues $(5\pm\sqrt5)/2\approx3.618,\ 1.382$. Indeed $3.618\ge2\ge1.382\ge1$. The trace rises by exactly $\lVert\mathbf{u}\rVert^2=2$.

:::

::: {#prp-derivative-of-inverse .proposition name="Derivative of an inverse"}

If $A(t)$ is invertible and differentiable, then
$$\frac{d A^{-1}}{dt}=-A^{-1}\frac{dA}{dt}A^{-1}.$$

:::

::: {.proof}

1. Differentiate $A(t)A^{-1}(t)=I$ by the product rule: $\dfrac{dA}{dt}A^{-1}+A\dfrac{dA^{-1}}{dt}=0$.

2. Multiply on the left by $A^{-1}$.

:::

::: {#thm-eigenvalue-derivative .theorem name="Derivative of an eigenvalue"}

Let $\lambda(t)$ be an eigenvalue of $A(t)$ with $A\mathbf{x}=\lambda\mathbf{x}$ and $\mathbf{y}^{\mathsf T}A=\lambda\mathbf{y}^{\mathsf T}$, normalised by $\mathbf{y}^{\mathsf T}\mathbf{x}=1$, all differentiable in $t$. Then
$$\frac{d\lambda}{dt}=\mathbf{y}^{\mathsf T}\frac{dA}{dt}\mathbf{x}.$$
For symmetric $A$ take $\mathbf{y}=\mathbf{x}$ with $\lVert\mathbf{x}\rVert=1$.

:::

::: {.proof}

1. $\lambda=\mathbf{y}^{\mathsf T}A\mathbf{x}$, because $\mathbf{y}^{\mathsf T}A\mathbf{x}=\lambda\mathbf{y}^{\mathsf T}\mathbf{x}=\lambda$.

2. Differentiate: $\lambda'=\mathbf{y}'^{\mathsf T}A\mathbf{x}+\mathbf{y}^{\mathsf T}A'\mathbf{x}+\mathbf{y}^{\mathsf T}A\mathbf{x}'$.

3. The outer terms are $\lambda\,\mathbf{y}'^{\mathsf T}\mathbf{x}+\lambda\,\mathbf{y}^{\mathsf T}\mathbf{x}'=\lambda\,(\mathbf{y}^{\mathsf T}\mathbf{x})'=0$.

:::

::: {#prp-singular-value-derivative .proposition name="Derivative of a singular value"}

If $\sigma(t)>0$ is a singular value of $A(t)$ with unit vectors $A\mathbf{v}=\sigma\mathbf{u}$, $A^{\mathsf T}\mathbf{u}=\sigma\mathbf{v}$, all differentiable, then
$$\frac{d\sigma}{dt}=\mathbf{u}^{\mathsf T}\frac{dA}{dt}\mathbf{v}.$$

:::

::: {.proof}

1. $\sigma=\mathbf{u}^{\mathsf T}A\mathbf{v}$. Differentiate: $\sigma'=\mathbf{u}'^{\mathsf T}A\mathbf{v}+\mathbf{u}^{\mathsf T}A'\mathbf{v}+\mathbf{u}^{\mathsf T}A\mathbf{v}'$.

2. $\mathbf{u}'^{\mathsf T}A\mathbf{v}=\sigma\,\mathbf{u}'^{\mathsf T}\mathbf{u}=0$ because $\mathbf{u}^{\mathsf T}\mathbf{u}=1$ gives $2\mathbf{u}^{\mathsf T}\mathbf{u}'=0$.

3. Likewise $\mathbf{u}^{\mathsf T}A\mathbf{v}'=\sigma\,\mathbf{v}^{\mathsf T}\mathbf{v}'=0$.

:::

::: {#rmk-eigenvalue-perturbation-and-interlacing-1 .remark name="When the derivative exists"}

A simple eigenvalue (or singular value) of a smoothly varying matrix varies smoothly, and so can its eigenvectors; the theorems above assume this. At a repeated eigenvalue the eigenvalue curves can cross or turn sharply, and $\lambda(t)$ may fail to be differentiable even for symmetric $A(t)$ when it is labelled by size.

:::
