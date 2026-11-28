---
title: "Stochastic Differential Equations: Solutions and Uniqueness"
sources: [camiii-sc-4]
requires: [math/probability/stochastic-calculus/levy-and-dubins-schwarz]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 4.1, in our own wording; proofs written out in steps where given. -->

The noisy equation $\dot x=F(x)+\eta$ is now interpreted as $dX_t=F(X_t)\,dt+dB_t$, i.e. $X_t-X_0=\int_0^tF(X_s)\,ds+B_t$.

::: {#def-sde .definition name="Stochastic differential equation, weak and strong solutions"}

Let $b:\mathbb R_+\times\mathbb R^d\to\mathbb R^d$ and $\sigma:\mathbb R_+\times\mathbb R^d\to\mathbb R^{d\times m}$ be locally bounded and measurable. A *solution* of the equation $\mathcal E(\sigma,b)$,
$$dX_t=b(t,X_t)\,dt+\sigma(t,X_t)\,dB_t,$$
consists of a filtered probability space with the usual conditions, an $m$-dimensional $(\mathcal F_t)$-Brownian motion $B$ with $B_0=0$, and a continuous adapted process $X$ in $\mathbb R^d$ with
$$X_t=X_0+\int_0^t\sigma(s,X_s)\,dB_s+\int_0^tb(s,X_s)\,ds .$$
If $X_0=x$ it is a (*weak*) solution of $\mathcal E_x(\sigma,b)$; it is a *strong* solution if $X$ is adapted to the canonical filtration of $B$.

:::

::: {#def-sde-uniqueness .definition name="Uniqueness in law and pathwise uniqueness"}

For $\mathcal E(\sigma,b)$ there is *uniqueness in law* if, for each $x$, all solutions of $\mathcal E_x(\sigma,b)$ have the same law. There is *pathwise uniqueness* if for a fixed filtered space and Brownian motion $B$, any two solutions with the same starting point are indistinguishable.

:::

::: {#exm-tanaka .example name="Tanaka's equation: uniqueness in law without pathwise uniqueness"}

Consider $dX_t=\operatorname{sgn}(X_t)\,dB_t$, $X_0=x$, with $\operatorname{sgn}(y)=1$ for $y>0$ and $-1$ for $y\le0$. It has a weak solution, unique in law, but pathwise uniqueness fails.

1. *Existence.* Let $X$ be a Brownian motion started at $x$ and $B_t=\int_0^t\operatorname{sgn}(X_s)\,dX_s$ (the integrand $\operatorname{sgn}(X_s)$ is only progressively measurable; for a continuous integrator it agrees $\Pr\otimes d\langle X\rangle$-almost everywhere with a previsible process, which is all the integral needs). Then $B$ is a continuous local martingale with $\langle B\rangle_t=\int_0^t\operatorname{sgn}(X_s)^2d\langle X\rangle_s=t$, so $B$ is a Brownian motion by Lévy's characterisation (@thm-levy-characterisation), and $\int_0^t\operatorname{sgn}(X_s)\,dB_s=\int_0^t\operatorname{sgn}^2(X_s)dX_s=X_t-x$.

2. *Uniqueness in law.* Any solution is a continuous local martingale with $\langle X\rangle_t=t$, hence a Brownian motion by Lévy.

3. *No pathwise uniqueness.* If $x=0$ and $X$ is a solution driven by $B$, then $-X$ also solves the equation with the same $B$: $-X_t=\int\operatorname{sgn}(X_s)\,dB_s$ and $\operatorname{sgn}(X_s)=-\operatorname{sgn}(-X_s)+2\mathbf 1_{\{X_s=0\}}$, and $\int\mathbf 1_{\{X_s=0\}}dB_s$ is a continuous local martingale with quadratic variation $\int\mathbf 1_{\{X_s=0\}}ds=0$.

:::

::: {#thm-yamada-watanabe .theorem name="Yamada–Watanabe"}

If weak existence and pathwise uniqueness hold for $\mathcal E(\sigma,b)$, then uniqueness in law holds, and for every filtered space and Brownian motion $B$ and every $x$ there is a unique strong solution.

:::

*Proof omitted* (the lecture notes do not prove it either, since it is not needed below).

::: {#def-lipschitz-coefficients .definition name="Lipschitz coefficients"}

$b$ and $\sigma$ are *Lipschitz in $x$* if there is $K>0$ with $|b(t,x)-b(t,y)|\le K|x-y|$ and $|\sigma(t,x)-\sigma(t,y)|\le K|x-y|$ for all $t,x,y$.

:::

::: {#thm-sde-lipschitz .theorem name="Existence and uniqueness under Lipschitz conditions"}

If $b,\sigma$ are Lipschitz in $x$, then pathwise uniqueness holds for $\mathcal E(\sigma,b)$, and for every filtered space satisfying the usual conditions, every $(\mathcal F_t)$-Brownian motion $B$ and every $x$ there is a unique strong solution of $\mathcal E_x(\sigma,b)$.

:::

::: {.proof}

*Pathwise uniqueness* (with $m=d=1$ for notation). Let $X,X'$ be solutions with $X_0=X_0'$, fix $T$ and $n$, and put $S=\inf\{t:|X_t|\ge n\text{ or }|X'_t|\ge n\}$.

1. For $t\le T$, using $(a+b)^2\le2a^2+2b^2$ and the Itô isometry, the Cauchy–Schwarz inequality for the drift integral, and the Lipschitz bound,
$$E\big[(X_{t\wedge S}-X'_{t\wedge S})^2\big]\le2K^2(1+T)\int_0^tE\big[(X_{s\wedge S}-X'_{s\wedge S})^2\big]\,ds .$$

2. The function $h(t)=E[(X_{t\wedge S}-X'_{t\wedge S})^2]$ is bounded on $[0,T]$ (the processes are stopped inside $[-n,n]$), so Gronwall's lemma gives $h\equiv0$.

3. Let $n\to\infty$: $X_t=X_t'$ a.s. for each $t$, and by continuity the processes are indistinguishable.

*Existence* (proof omitted here) is by Picard iteration, $X^{k+1}_t=x+\int_0^t\sigma(s,X^k_s)\,dB_s+\int_0^tb(s,X^k_s)\,ds$, which converges in the same way as for ordinary differential equations, with Doob's inequality controlling the stochastic integrals; the limit is adapted to the filtration of $B$.

:::

<!-- TODO: write out the Picard iteration (existence) part of the proof; only pathwise uniqueness is proved here. -->

::: {#fig-sde-existence-and-uniqueness-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (6,0);
\node[small vertex] at (0,0) {};
\draw[emph] (0,0) -- (1,0.3) -- (2,-0.2) -- (3,0.4) -- (4,0.8) -- (5,0.5) -- (6,1.0);
\draw[hl] (0,0) -- (1,-0.3) -- (2,0.2) -- (3,-0.4) -- (4,-0.8) -- (5,-0.5) -- (6,-1.0);
\node[lab] at (7.2,1.0) {$X$};
\node[lab] at (7.2,-1.0) {$-X$};
\node[tick] at (3,-1.6) {Tanaka: both solve $dX=\mathrm{sgn}(X)\,dB$ for the same $B$};
\end{tikzpicture}
\end{center}
```

For the Tanaka equation started at $0$, a solution and its reflection are two different solutions driven by the same Brownian motion, so pathwise uniqueness fails although the law is unique.

:::
