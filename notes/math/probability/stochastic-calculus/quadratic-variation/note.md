---
title: "Quadratic Variation, Covariation and Semi-Martingales"
sources: [camiii-sc-2]
requires: [math/probability/stochastic-calculus/local-martingales, math/probability/stochastic-calculus/square-integrable-martingales]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Sections 2.4–2.6, in our own wording; proofs written out in steps where given. -->

Brownian motion and continuous local martingales oscillate so wildly that second-order terms survive in the limit.

::: {#def-ucp .definition name="Uniform convergence on compacts in probability"}

$X^n\to X$ *u.c.p.* if $\Pr\big(\sup_{s\le t}|X^n_s-X_s|>\varepsilon\big)\to0$ for all $t>0$, $\varepsilon>0$.

:::

::: {#thm-quadratic-variation .theorem name="Existence of the quadratic variation"}

Let $M$ be a continuous local martingale with $M_0=0$. There is a unique (up to indistinguishability) continuous adapted increasing process $\langle M\rangle$ with $\langle M\rangle_0=0$ such that $M^2-\langle M\rangle$ is a continuous local martingale. Moreover
$$\langle M\rangle_t=\lim_{n\to\infty}\langle M\rangle^{(n)}_t\ \text{ u.c.p.},\qquad\langle M\rangle^{(n)}_t=\sum_{i=1}^{\lceil2^nt\rceil}\big(M_{i2^{-n}\wedge t}-M_{(i-1)2^{-n}\wedge t}\big)^2.$$
$\langle M\rangle$ is the *quadratic variation* of $M$.

:::

::: {.proof}

*Uniqueness.* If $A,\tilde A$ both qualify, then $A-\tilde A=(M^2-\tilde A)-(M^2-A)$ is a continuous local martingale of finite variation starting at $0$, hence $0$ by @thm-fv-local-martingale-zero.

*Existence* (proof omitted here; the lecture notes carry it out in three steps). For bounded $M$ one shows that $X^n_t=\sum_iM_{(i-1)2^{-n}}(M_{i2^{-n}\wedge t}-M_{(i-1)2^{-n}\wedge t})$ is Cauchy in $\mathcal M^2_c$, using $M^2_{k2^{-n}}=\langle M\rangle^{(n)}_{k2^{-n}}+2X^n_{k2^{-n}}$ and Doob's inequality (@thm-m2-hilbert); the limit gives $\langle M\rangle=M^2-2X$. A general continuous local martingale is localised by the stopping times $S_n$ of @prp-localising-by-hitting-times.

:::

<!-- TODO: write out the existence proof (bounded case via Hilbert space completeness, then localisation); only uniqueness is proved here. -->

::: {#exm-brownian-quadratic-variation .example name="Brownian motion"}

For a standard Brownian motion, $B_t^2-t$ is a martingale (@prp-brownian-martingales), so $\langle B\rangle_t=t$. In contrast $\sum_i|B_{i2^{-n}}-B_{(i-1)2^{-n}}|\to\infty$: the path has infinite variation but finite quadratic variation.

:::

::: {#fig-quadratic-variation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (6,0);
\draw[emph] (0,0) -- (0.3,0.35) -- (0.6,0.1) -- (0.9,0.55) -- (1.2,0.3) -- (1.5,0.9) -- (1.8,0.6) -- (2.1,0.85) -- (2.4,0.4) -- (2.7,0.7) -- (3.0,0.2);
\node[tick] at (3.0,-0.3) {$t$};
\node[lab] at (4.8,0.9) {$\sum_i\lvert\Delta_iB\rvert\to\infty$};
\node[lab, text=accent] at (4.8,0.2) {$\sum_i(\Delta_iB)^2\to t$};
\end{tikzpicture}
\end{center}
```

Along finer and finer partitions of $[0,t]$ the sum of absolute increments of Brownian motion diverges, while the sum of squared increments converges to $t$.

:::

::: {#def-covariation .definition name="Covariation"}

For continuous local martingales $M,N$ define $\langle M,N\rangle=\tfrac14\big(\langle M+N\rangle-\langle M-N\rangle\big)$.

:::

::: {#prp-covariation-properties .proposition name="Properties of the bracket"}

1. $\langle M,N\rangle$ is the unique finite variation process (null at $0$) such that $MN-\langle M,N\rangle$ is a continuous local martingale.

2. $(M,N)\mapsto\langle M,N\rangle$ is bilinear and symmetric.

3. $\langle M,N\rangle^{(n)}_t=\sum_i(M_{i2^{-n}\wedge t}-M_{(i-1)2^{-n}\wedge t})(N_{i2^{-n}\wedge t}-N_{(i-1)2^{-n}\wedge t})\to\langle M,N\rangle_t$ u.c.p.

For $M,N\in\mathcal M^2_c$ the value at $\infty$ is the inner product: $E[\langle M,N\rangle_\infty]=E[M_\infty N_\infty]$.

:::

::: {#thm-kunita-watanabe .theorem name="Kunita–Watanabe inequality"}

For continuous local martingales $M,N$ and previsible $H,K$, almost surely
$$\int_0^\infty|H_s||K_s|\,|d\langle M,N\rangle_s|\le\Big(\int_0^\infty H_s^2\,d\langle M\rangle_s\Big)^{1/2}\Big(\int_0^\infty K_s^2\,d\langle N\rangle_s\Big)^{1/2}.$$

:::

This is the Cauchy–Schwarz inequality for the positive semi-definite bilinear form $\langle\cdot,\cdot\rangle$, extended from simple $H,K$ by approximation (proof omitted).

::: {#def-semimartingale .definition name="Semi-martingale and its quadratic variation"}

A continuous adapted process $X$ is a *continuous semi-martingale* if $X=X_0+M+A$ with $X_0\in\mathcal F_0$, $M$ a continuous local martingale with $M_0=0$ and $A$ a continuous finite variation process with $A_0=0$. This decomposition is unique up to indistinguishability (@thm-fv-local-martingale-zero). For $X=X_0+M+A$ and $X'=X'_0+M'+A'$ put $\langle X\rangle=\langle M\rangle$ and $\langle X,X'\rangle=\langle M,M'\rangle$.

:::

This is consistent because a continuous finite variation process has zero quadratic variation, so $\langle X,Y\rangle^{(n)}\to\langle X,Y\rangle$ u.c.p. for semi-martingales as well.
