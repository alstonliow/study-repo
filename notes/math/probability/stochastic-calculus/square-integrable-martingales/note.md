---
title: "Square-Integrable Martingales as a Hilbert Space"
sources: [camiii-sc-2]
requires: [math/probability/continuous-time/continuous-time-martingales]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 2.3, in our own wording; proofs written out in steps. -->

The stochastic integral is built by extending a simple Riemann-sum definition by continuity, so the space of integrators must be complete.

::: {#def-m2-space .definition name="The spaces M² and M²_c"}

Let $\mathcal M^2$ be the càdlàg martingales $X$ with $\sup_tE[X_t^2]<\infty$, and $\mathcal M^2_c\subseteq\mathcal M^2$ those with continuous paths. By martingale convergence (@thm-continuous-martingale-convergence) $X_t\to X_\infty$ almost surely and in $L^2$, and
$$(X,Y)_{\mathcal M^2}=E[X_\infty Y_\infty],\qquad\lVert X\rVert_{\mathcal M^2}=E[X_\infty^2]^{1/2}.$$

:::

::: {#fig-square-integrable-martingales-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[box] (0,0) ellipse (3.6 and 1.5);
\draw[box] (0,-0.2) ellipse (2.2 and 0.9);
\draw[hl] (0,-0.3) ellipse (1.0 and 0.4);
\node[lab] at (0,1.1) {càdlàg martingales};
\node[lab] at (0,0.35) {$\mathcal M^2$};
\node[lab] at (0,-0.3) {$\mathcal M^2_c$};
\node[lab] at (6.3,0.3) {Hilbert space, $\lVert X\rVert=\lVert X_\infty\rVert_{L^2}$};
\end{tikzpicture}
\end{center}
```

Square-integrable martingales form a Hilbert space with the norm $\lVert X_\infty\rVert_{L^2}$; the continuous ones form a closed subspace.

:::

Since $X^2$ is a sub-martingale, $t\mapsto E[X_t^2]$ increases to $E[X_\infty^2]$.

::: {#thm-doob-l2-m2 .theorem name="Doob's inequality in M²"}

For $X\in\mathcal M^2$, $E\big[\sup_tX_t^2\big]\le4E[X_\infty^2]$.

:::

This is Doob's $L^2$ inequality (@lem-doob-lp-inequality) for cadlag martingales, passing to the limit over dyadic times as in @thm-continuous-martingale-convergence. It shows that controlling $X_\infty$ controls the whole path; in particular $\lVert X\rVert_{\mathcal M^2}=0$ implies $X=0$.

::: {#thm-m2-hilbert .theorem name="M² is a Hilbert space"}

$\mathcal M^2$ is a Hilbert space and $\mathcal M^2_c$ is a closed subspace.

:::

::: {.proof}

Let $(X^n)$ be Cauchy in $\mathcal M^2$; pass to a subsequence with $E[(X^n_\infty-X^{n-1}_\infty)^2]\le2^{-n}$.

1. By Cauchy–Schwarz and Doob,
$$E\Big[\sum_n\sup_t|X^n_t-X^{n-1}_t|\Big]\le\sum_nE\Big[\sup_t|X^n_t-X^{n-1}_t|^2\Big]^{1/2}\le2\sum_n2^{-n/2}<\infty.$$
So almost surely $\sum_n\sup_t|X^n_t-X^{n-1}_t|<\infty$, i.e. $(X^n(\omega,\cdot))$ is Cauchy in the sup-norm on càdlàg functions.

2. Let $X(\omega,\cdot)$ be the uniform limit on that event and $0$ elsewhere; it is càdlàg, and continuous if all $X^n$ are.

3. By Fatou and Doob, $E[\sup_t|X^n-X|^2]\le\liminf_mE[\sup_t|X^n-X^m|^2]\le\liminf_m4E[(X^n_\infty-X^m_\infty)^2]\to0$ as $n\to\infty$.

4. For $s<t$, $\lVert E[X_t\mid\mathcal F_s]-X_s\rVert_2\le\lVert X_t-X^n_t\rVert_2+\lVert X_s^n-X_s\rVert_2\le2E[\sup|X-X^n|^2]^{1/2}\to0$. The left side does not depend on $n$, so it vanishes: $X$ is a martingale in $\mathcal M^2$.

:::
