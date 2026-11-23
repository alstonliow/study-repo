---
title: "Gaussian Quadrature and Weight Functions"
sources: [mit18335-36]
requires: [math/numerical/quadrature/clenshaw-curtis-quadrature]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 36 (integration with weight functions, and Gaussian quadrature), in our own wording; proofs written out in steps; nodes and weights checked with numpy. -->

A rule with $n$ nodes and $n$ weights has $2n$ parameters, so one may hope to integrate all polynomials of degree $2n-1$ exactly. Gaussian quadrature achieves this by placing the nodes at the roots of an orthogonal polynomial. Allowing a *weight function* $w(x)$ in the integral lets the rule handle known singular or oscillatory factors exactly and integrate only the smooth part numerically.

::: {#def-orthogonal-polynomials .definition name="Orthogonal polynomials for a weight"}

Let $w>0$ be integrable on $(a,b)$ with all moments $\int x^kw\,dx$ finite, and $\langle f,g\rangle_w=\int_a^bf(x)g(x)w(x)\,dx$. Applying Gram–Schmidt to $1,x,x^2,\dots$ in this inner product gives *orthogonal polynomials* $\phi_0,\phi_1,\dots$ with $\deg\phi_k=k$ and $\langle\phi_j,\phi_k\rangle_w=0$ for $j\ne k$. Examples: Legendre polynomials ($w=1$ on $[-1,1]$), Chebyshev polynomials ($w=1/\sqrt{1-x^2}$, @prp-chebyshev-polynomial-properties), Laguerre ($w=e^{-x}$ on $[0,\infty)$), Hermite ($w=e^{-x^2}$ on $\mathbb R$).

:::

::: {#lem-orthogonal-polynomial-roots .lemma name="Roots of orthogonal polynomials"}

$\phi_n$ has $n$ distinct real roots, all in $(a,b)$.

:::

::: {.proof}

1. Let $r_1,\dots,r_j$ be the points of $(a,b)$ where $\phi_n$ changes sign, and $q(x)=\prod_i(x-r_i)$, so $\phi_nq$ does not change sign on $(a,b)$ and is not identically zero.

2. Then $\langle\phi_n,q\rangle_w\ne0$. But $\phi_n$ is orthogonal to all polynomials of degree $<n$, since these are combinations of $\phi_0,\dots,\phi_{n-1}$. Hence $\deg q=j\ge n$.

3. $\phi_n$ has degree $n$, so it has at most $n$ roots: $j=n$, and the roots are simple and lie in $(a,b)$.

:::

::: {#thm-gaussian-quadrature .theorem name="Gaussian quadrature"}

Let $x_1,\dots,x_n$ be the roots of $\phi_n$ and $w_k=\int_a^b\ell_k(x)w(x)\,dx$, where $\ell_k$ is the Lagrange polynomial with $\ell_k(x_j)=\delta_{jk}$. Then
$$\int_a^bp(x)w(x)\,dx=\sum_{k=1}^nw_kp(x_k)\qquad\text{for every polynomial }p\text{ of degree}\le2n-1,$$
no $n$-point rule is exact for all polynomials of degree $2n$, and all $w_k>0$.

:::

::: {.proof}

1. *Degree $\le n-1$.* $p=\sum_kp(x_k)\ell_k$ exactly, so integrating gives $\sum_kw_kp(x_k)$.

2. *Degree $\le2n-1$.* Divide: $p=q\phi_n+r$ with $\deg q,\deg r\le n-1$. Then $\int pw=\langle q,\phi_n\rangle_w+\int rw=\int rw$ by orthogonality, while $p(x_k)=r(x_k)$ because $\phi_n(x_k)=0$. Step 1 applied to $r$ finishes.

3. *Optimality.* For any nodes, $p=\prod_k(x-x_k)^2$ has degree $2n$, vanishes at every node, but has $\int pw>0$.

4. *Positivity.* $\ell_k^2$ has degree $2n-2$, so $0<\int\ell_k^2w=\sum_jw_j\ell_k(x_j)^2=w_k$.

:::

::: {#prp-golub-welsch .proposition name="Nodes and weights from an eigenvalue problem"}

The orthonormal polynomials satisfy a three-term recurrence $x\phi_k=\beta_{k+1}\phi_{k+1}+\alpha_k\phi_k+\beta_k\phi_{k-1}$. The Gauss nodes are the eigenvalues of the symmetric tridiagonal *Jacobi matrix* $J_n$ with diagonal $\alpha_0,\dots,\alpha_{n-1}$ and off-diagonal $\beta_1,\dots,\beta_{n-1}$, and $w_k=\bigl(\int w\bigr)\,v_{1k}^2$ where $\mathbf{v}_k$ is the corresponding unit eigenvector (Golub–Welsch).

:::

::: {.proof}

1. *Recurrence.* $x\phi_k$ has degree $k+1$ and $\langle x\phi_k,\phi_j\rangle_w=\langle\phi_k,x\phi_j\rangle_w=0$ for $j<k-1$ (since $x\phi_j$ has degree $<k$). So $x\phi_k$ involves only $\phi_{k+1},\phi_k,\phi_{k-1}$, and the symmetry of the inner product makes the coefficient of $\phi_{k-1}$ in $x\phi_k$ equal to that of $\phi_k$ in $x\phi_{k-1}$.

2. In vector form, with $\boldsymbol{\phi}(x)=(\phi_0(x),\dots,\phi_{n-1}(x))$, the recurrence reads $x\boldsymbol\phi(x)=J_n\boldsymbol\phi(x)+\beta_n\phi_n(x)\mathbf{e}_n$. At a root $x_k$ of $\phi_n$ this says $J_n\boldsymbol\phi(x_k)=x_k\boldsymbol\phi(x_k)$: $x_k$ is an eigenvalue with eigenvector $\boldsymbol\phi(x_k)$.

3. *Weights.* Exactness for $\phi_i\phi_j$ (degree $\le2n-2$) gives $\sum_kw_k\phi_i(x_k)\phi_j(x_k)=\delta_{ij}$, i.e. the matrix $P$ with columns $\sqrt{w_k}\boldsymbol\phi(x_k)$ is orthogonal. Its columns are the unit eigenvectors, and their first entries are $\sqrt{w_k}\phi_0=\sqrt{w_k}/\sqrt{\int w}$.

:::

Computing the eigenvalues of $J_n$ by the symmetric QR algorithm (@def-shifted-qr-algorithm) takes $O(n^2)$ operations, and faster $O(n)$ algorithms exist for large $n$.

::: {#exm-gauss-legendre-two-point .example name="Two-point Gauss–Legendre"}

For $w=1$ on $[-1,1]$, $\phi_2\propto3x^2-1$, so $x_{1,2}=\pm1/\sqrt3$ and by symmetry $w_1=w_2=1$. The rule $f(-1/\sqrt3)+f(1/\sqrt3)$ integrates $1,x,x^2,x^3$ exactly: for $x^2$ it gives $\tfrac13+\tfrac13=\tfrac23=\int_{-1}^1x^2dx$. The Jacobi matrix is $\begin{bmatrix}0&1/\sqrt3\\1/\sqrt3&0\end{bmatrix}$, with eigenvalues $\pm1/\sqrt3$ and eigenvectors $(1,\pm1)/\sqrt2$, so $w_k=2\cdot\tfrac12=1$, as @prp-golub-welsch predicts.

:::

::: {#fig-gaussian-quadrature-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.6cm, y=1.3cm]
\draw[->, faint] (-1.2,0) -- (1.25,0) node[lab, right] {$x$};
\draw[emph, domain=-1:1, samples=60] plot (\x,{1.5*\x*\x-0.5});
\node[tick, right] at (1,1) {$P_2=\tfrac12(3x^2-1)$};
\draw[faint, domain=-1:1, samples=60] plot (\x,{2.5*\x*\x*\x-1.5*\x});
\node[tick, right] at (1,-0.7) {$P_3$};
\foreach \x in {-0.5774,0.5774} {\fill[accent] (\x,0) circle (2.4pt);}
\foreach \x in {-0.7746,0,0.7746} {\draw[faint] (\x,-0.06) -- (\x,0.06);}
\node[tick, below] at (-0.5774,-0.05) {$-\tfrac1{\sqrt3}$}; \node[tick, below] at (0.5774,-0.05) {$\tfrac1{\sqrt3}$};
\node[tick, below] at (-1,0) {$-1$}; \node[tick, below] at (1,0) {$1$};
\end{tikzpicture}
\end{center}
```

The two-point Gauss–Legendre nodes (dots) are the roots of the Legendre polynomial $P_2$; the three-point nodes $0,\pm\sqrt{3/5}$ (ticks) are the roots of $P_3$ (thin), and they interlace.

:::

::: {#rmk-gaussian-quadrature-1 .remark name="Using weight functions"}

If $f(x)=g(x)w(x)$ with $w$ singular or oscillatory but known and $g$ smooth, a Gaussian rule for the weight $w$ integrates $g$ with the full spectral accuracy. For example $\int_{-1}^1g(x)/\sqrt{1-x^2}\,dx$ is computed by Gauss–Chebyshev quadrature, which has nodes $\cos\frac{(2k-1)\pi}{2n}$ and equal weights $\pi/n$; this is the midpoint rule in $\theta=\arccos x$ for a periodic integrand. Infinite intervals are handled by Gauss–Laguerre and Gauss–Hermite rules, or by a change of variables mapping them to a finite interval.

:::
