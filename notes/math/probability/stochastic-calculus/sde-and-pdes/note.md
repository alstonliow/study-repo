---
title: "SDEs and PDEs: Dirichlet–Poisson, Cauchy Problem and Feynman–Kac"
sources: [camiii-sc-4]
requires: [math/probability/stochastic-calculus/sde-existence-and-uniqueness, math/probability/brownian-motion/harmonic-functions-and-dirichlet-problem]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 4.3, in our own wording; proofs written out in steps. -->

Brownian motion solves the Dirichlet problem for the Laplacian (@thm-harmonic-martingale). Diffusions solve it for general elliptic operators.

::: {#def-generator .definition name="The generator of an SDE"}

For the time-independent equation $dX_t=b(X_t)\,dt+\sigma(X_t)\,dB_t$ with $b,\sigma$ measurable and locally bounded, put $a=\sigma\sigma^{\mathsf T}$ and
$$L=\frac12\sum_{i,j}a_{ij}\,\partial_i\partial_j+\sum_ib_i\,\partial_i .$$

:::

For $b=0$ and $\sigma=\sqrt2I$, $L=\Delta$.

::: {#prp-generator-martingale .proposition name="Martingales from the generator"}

If $X$ solves $\mathcal E_x(\sigma,b)$ and $f$ is $C^1$ in time and $C^2$ in space, then
$$M^f_t=f(t,X_t)-f(0,X_0)-\int_0^t\Big(\frac\partial{\partial s}+L\Big)f(s,X_s)\,ds$$
is a continuous local martingale.

:::

This is Itô's formula (@thm-ito-formula): $d\langle X^i,X^j\rangle=a_{ij}\,dt$, and the remaining terms are stochastic integrals against $dB$.

::: {#def-dirichlet-poisson .definition name="The Dirichlet–Poisson problem"}

Let $U\subseteq\mathbb R^d$ be non-empty, bounded and open, $f\in C_b(U)$ and $g\in C_b(\partial U)$. Find $u\in C^2(U)\cap C(\bar U)$ with $-Lu=f$ in $U$ and $u=g$ on $\partial U$. The case $f=0$ is the *Dirichlet problem*, the case $g=0$ the *Poisson problem*. The matrix $a$ is *uniformly elliptic* if $\xi^{\mathsf T}a(x)\xi\ge c|\xi|^2$ for some $c>0$ and all $\xi,x$.

:::

::: {#thm-dirichlet-poisson-representation .theorem name="Probabilistic representation of the Dirichlet–Poisson problem"}

Let $\sigma,b$ be bounded measurable with $\sigma\sigma^{\mathsf T}$ uniformly elliptic, let $u$ solve the Dirichlet–Poisson problem, let $X$ solve $\mathcal E_x(\sigma,b)$ and $T_U=\inf\{t\ge0:X_t\notin U\}$. Then $E[T_U]<\infty$ and
$$u(x)=E_x\Big[g(X_{T_U})+\int_0^{T_U}f(X_s)\,ds\Big].$$
In particular the solution is unique.

:::

(Existence of a solution for regular $U$ and Hölder coefficients is a classical PDE theorem that the lecture notes quote without proof.)

::: {.proof}

1. *Localise.* Let $U_n=\{y\in U:\operatorname{dist}(y,\partial U)>1/n\}$, $T_n=\inf\{t:X_t\notin U_n\}$, and $u_n\in C_b^2(\mathbb R^d)$ equal to $u$ on $U_n$. By @prp-generator-martingale, $u_n(X_{t\wedge T_n})-u_n(x)-\int_0^{t\wedge T_n}Lu_n(X_s)ds$ is a bounded local martingale, hence a martingale. For $n$ large, taking expectations and using $-Lu=f$ on $U_n$,
$$u(x)=E\Big[u(X_{t\wedge T_n})+\int_0^{t\wedge T_n}f(X_s)\,ds\Big].$$

2. *$E[T_U]<\infty$.* This does not depend on $f,g$, so take $f=1$, $g=0$ with solution $v$ (bounded, by the existence theorem). The same identity gives $E[t\wedge T_n]=v(x)-E[v(X_{t\wedge T_n})]\le2\lVert v\rVert_\infty$. Letting $n,t\to\infty$ by monotone convergence, $E[T_U]\le2\lVert v\rVert_\infty<\infty$.

3. *Pass to the limit.* $t\wedge T_n\to T_U$, $|f|\le\lVert f\rVert_\infty$ with $E[T_U]<\infty$, so dominated convergence handles the integral; $u$ is continuous on $\bar U$ and $X_{T_U}\in\partial U$ where $u=g$, so $E[u(X_{t\wedge T_n})]\to E[g(X_{T_U})]$.

:::

::: {#def-cauchy-problem .definition name="The Cauchy problem"}

For $f\in C_b^2(\mathbb R^d)$ find $u:\mathbb R_+\times\mathbb R^d\to\mathbb R$, $C^1$ in time and $C^2$ in space, with $\partial_tu=Lu$ on $\mathbb R_+\times\mathbb R^d$ and $u(0,\cdot)=f$.

:::

::: {#thm-cauchy-representation .theorem name="Probabilistic representation of the Cauchy problem"}

Let $u$ be a bounded solution of the Cauchy problem and $X$ a solution of $\mathcal E_x(\sigma,b)$. Then for $0\le s\le t$, $E_x[f(X_t)\mid\mathcal F_s]=u(t-s,X_s)$. In particular $u(t,x)=E_x[f(X_t)]$, and $X$ is a continuous Markov process.

:::

::: {.proof}

1. Fix $t$ and let $g(s,y)=u(t-s,y)$. Then $(\partial_s+L)g(s,y)=-\partial_tu(t-s,y)+Lu(t-s,y)=0$.

2. By @prp-generator-martingale $g(s,X_s)-g(0,X_0)$ is a local martingale, and it is a martingale because $u$ is bounded (this uses the boundedness of the derivatives that enter the integrals, assumed for the solution).

3. Thus $u(t-s,X_s)=g(s,X_s)=E[g(t,X_t)\mid\mathcal F_s]=E[u(0,X_t)\mid\mathcal F_s]=E[f(X_t)\mid\mathcal F_s]$.

:::

::: {#thm-feynman-kac .theorem name="Feynman–Kac formula"}

Let $f\in C_b^2(\mathbb R^d)$, $V\in C_b(\mathbb R^d)$ and let $u$ be a bounded solution with bounded derivatives of $\partial_tu=Lu+Vu$, $u(0,\cdot)=f$. For $X$ solving $\mathcal E_x(\sigma,b)$,
$$u(t,x)=E_x\Big[f(X_t)\exp\Big(\int_0^tV(X_s)\,ds\Big)\Big].$$

:::

::: {.proof}

1. Fix $t$ and set $g(s,y)=u(t-s,y)$ and $A_s=\exp\big(\int_0^sV(X_r)dr\big)$, a continuous finite variation process with $dA_s=V(X_s)A_s\,ds$.

2. By integration by parts, $d\big(g(s,X_s)A_s\big)=A_s\,dg(s,X_s)+g(s,X_s)V(X_s)A_s\,ds$, and by Itô's formula $dg(s,X_s)=(\partial_s+L)g\,ds+dN_s$ with $N$ a local martingale. Since $(\partial_s+L)g=-\partial_tu+Lu=-Vu$ at $(t-s,\cdot)$, the $ds$-terms cancel.

3. So $g(s,X_s)A_s$ is a local martingale, bounded on $[0,t]$ (as $u$ and $V$ are bounded), hence a martingale. Equating expectations at $s=0$ and $s=t$: $u(t,x)=E[g(0,X_0)A_0]=E[g(t,X_t)A_t]=E[f(X_t)A_t]$.

:::

When $L$ is the Laplacian, $\partial_tu=\Delta u+Vu$ is the Schrödinger equation in imaginary time, which motivated Feynman's path-integral view.

::: {#fig-sde-and-pdes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[box] (0,0) .. controls (0.3,2.2) and (3.4,2.6) .. (4.0,1.2) .. controls (4.5,-0.4) and (1.2,-0.7) .. (0,0);
\node[lab] at (2.1,-1.1) {$U$};
\node[small vertex] at (1.4,0.9) {};
\node[tick] at (1.2,0.6) {$x$};
\draw[emph] (1.4,0.9) -- (1.9,1.2) -- (2.3,0.8) -- (2.8,1.3) -- (3.3,1.7) -- (3.7,2.0);
\node[small vertex] at (3.7,2.0) {};
\node[tick] at (4.4,2.2) {$X_{T_U}$};
\node[lab, text=accent] at (7.3,1.3) {$u(x)=E_x\big[g(X_{T_U})\big]$};
\node[lab] at (7.3,0.7) {($f=0$)};
\end{tikzpicture}
\end{center}
```

A path of the diffusion started at $x$ runs until it first leaves $U$; the solution of the Dirichlet problem is the average of the boundary data at the exit point.

:::
