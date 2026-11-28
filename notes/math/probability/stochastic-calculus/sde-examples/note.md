---
title: "Examples of SDEs: Ornstein–Uhlenbeck, Dyson, Geometric and Bessel"
sources: [camiii-sc-4]
requires: [math/probability/stochastic-calculus/sde-existence-and-uniqueness]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 4.2, in our own wording; proofs written out in steps. -->

::: {#def-ornstein-uhlenbeck .definition name="Ornstein–Uhlenbeck process"}

For $\lambda>0$ the *Ornstein–Uhlenbeck process* solves $dX_t=-\lambda X_t\,dt+dB_t$.

:::

The coefficients are Lipschitz, so a unique strong solution exists (@thm-sde-lipschitz); here it can be written down.

::: {#prp-ou-solution .proposition name="Explicit solution and covariance"}

The solution is $X_t=e^{-\lambda t}X_0+\int_0^te^{-\lambda(t-s)}\,dB_s$. If $X_0=x$ is deterministic, $X$ is a Gaussian process with
$$E[X_t]=e^{-\lambda t}x,\qquad\operatorname{cov}(X_t,X_s)=\frac1{2\lambda}\big(e^{-\lambda|t-s|}-e^{-\lambda(t+s)}\big),$$
and in particular $X_t\sim N\big(e^{-\lambda t}x,\frac{1-e^{-2\lambda t}}{2\lambda}\big)\to N(0,\frac1{2\lambda})$. If $X_0\sim N(0,\frac1{2\lambda})$ is independent of $B$, then $X$ is a centred stationary Gaussian process with $\operatorname{cov}(X_t,X_s)=\frac1{2\lambda}e^{-\lambda|t-s|}$.

:::

::: {.proof}

1. By Itô's formula (integration by parts) $d(e^{\lambda t}X_t)=e^{\lambda t}dX_t+\lambda e^{\lambda t}X_t\,dt=e^{\lambda t}dB_t$, which integrates to the formula.

2. The integrand $e^{-\lambda(t-s)}$ is deterministic, so the integral is a Wiener integral and $(X_{t_1},\dots,X_{t_n})$ is jointly Gaussian (@prp-gaussian-isometry).

3. By the Itô isometry, for $s\le t$,
$$\operatorname{cov}(X_t,X_s)=E\Big[\int_0^te^{-\lambda(t-u)}dB_u\int_0^se^{-\lambda(s-u)}dB_u\Big]=e^{-\lambda(t+s)}\int_0^se^{2\lambda u}du=\frac{e^{-\lambda(t-s)}-e^{-\lambda(t+s)}}{2\lambda}.$$

4. If $X_0\sim N(0,\frac1{2\lambda})$ then $\operatorname{var}(e^{-\lambda t}X_0)=\frac{e^{-2\lambda t}}{2\lambda}$ adds to the above and cancels the term $e^{-\lambda(t+s)}/2\lambda$, leaving $\frac1{2\lambda}e^{-\lambda|t-s|}$.

:::

::: {#fig-sde-examples-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (6.5,0);
\draw[hl, dashed] (0,1.2) -- (6.5,1.2);
\draw[hl, dashed] (0,-1.2) -- (6.5,-1.2);
\draw[hl] plot[domain=0:6.3,samples=30] (\x,{2.0*exp(-0.8*\x)});
\draw[emph] (0,2.0) -- (0.6,1.5) -- (1.2,0.9) -- (1.8,0.9) -- (2.4,0.1) -- (3.0,0.5) -- (3.6,-0.2) -- (4.2,0.4) -- (4.8,0.9) -- (5.4,0.3) -- (6.0,-0.4);
\node[lab] at (7.8,1.2) {$\pm\tfrac1{\sqrt{2\lambda}}$};
\node[lab] at (7.4,2.0) {mean $e^{-\lambda t}x$};
\end{tikzpicture}
\end{center}
```

An Ornstein–Uhlenbeck path started at $x$ is pulled towards $0$ along its mean $e^{-\lambda t}x$ and then fluctuates in a stationary band of width of order $1/\sqrt{2\lambda}$.

:::

::: {#def-gaussian-orthogonal-ensemble .definition name="Gaussian orthogonal ensemble"}

Let $\mathcal H_N$ be the space of real symmetric $N\times N$ matrices with the inner product $N\operatorname{Tr}(HK)$ and orthonormal basis $H^1,\dots,H^{\dim\mathcal H_N}$. The *Gaussian orthogonal ensemble* $\mathrm{GOE}_N$ is the law of $H=\sum_nX_nH^n$ with $X_n$ i.i.d. standard normal.

:::

::: {#thm-dyson-brownian-motion .theorem name="Dyson Brownian motion"}

Replace each $X_n$ by an independent Ornstein–Uhlenbeck process with $\lambda=\frac12$ (this leaves $\mathrm{GOE}_N$ invariant). Then the ordered eigenvalues $\lambda^1_t\le\dots\le\lambda^N_t$ of the matrix process satisfy
$$d\lambda^i_t=\Big(-\frac{\lambda^i_t}2+\frac1N\sum_{j\ne i}\frac1{\lambda^i_t-\lambda^j_t}\Big)dt+\sqrt{\frac2{N\beta}}\,dB^i_t,\qquad\beta=1 .$$

:::

*Proof omitted.* It follows from Itô's formula and the formulas for the derivatives of eigenvalues of a symmetric matrix. Hermitian matrices give $\beta=2$ and symplectic ones $\beta=4$.

::: {#exm-geometric-brownian-motion .example name="Geometric Brownian motion"}

For $\sigma>0$ and $r\in\mathbb R$, the solution of $dX_t=\sigma X_t\,dB_t+rX_t\,dt$ is
$$X_t=X_0\exp\Big(\sigma B_t+\big(r-\tfrac{\sigma^2}2\big)t\Big).$$
Indeed, Itô's formula for $\log X_t$ gives $d\log X_t=\sigma\,dB_t+r\,dt-\tfrac12\sigma^2dt$, since $d\langle X\rangle=\sigma^2X^2dt$.

:::

::: {#exm-bessel-process .example name="The Bessel process"}

For a $d$-dimensional Brownian motion $B$, $X_t=|B_t|$ satisfies, up to the first time it hits $0$,
$$dX_t=\frac{d-1}{2X_t}\,dt+d\beta_t$$
for a one-dimensional Brownian motion $\beta$. The drift $\frac{d-1}{2X}$ pushes the process away from $0$ more strongly as $d$ grows, matching the recurrence–transience dichotomy (@thm-brownian-recurrence).

:::
