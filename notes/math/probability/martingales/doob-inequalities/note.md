---
title: "Doob's Maximal Inequalities"
sources: [camiii-ap-2]
requires: [math/probability/martingales/martingales-and-stopping-times, math/analysis/measure-theory/product-measures]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 2.3, in our own wording; proofs written out in steps. -->

Markov's inequality bounds $\Pr(|X|\ge\lambda)$ by $E|X|/\lambda$. For a martingale the same bound controls the whole running maximum, and with a factor $p/(p-1)$ the $L^p$ norm of the maximum. Write $X^*_n=\sup_{k\le n}|X_k|$.

::: {#lem-doob-maximal-inequality .lemma name="Doob's maximal inequality"}

Let $(X_n)$ be a non-negative sub-martingale or a martingale. For $\lambda\ge0$,

$$
\lambda\Pr(X^*_n\ge\lambda)\le E\big[|X_n|\mathbf 1_{\{X^*_n\ge\lambda\}}\big]\le E|X_n| .
$$

:::

::: {.proof}

1. If $X$ is a martingale then $|X|$ is a non-negative sub-martingale (Jensen), so assume $X\ge0$ is a sub-martingale. Let $T=\inf\{k:X_k\ge\lambda\}$, a stopping time; $\{T\le n\}=\{X^*_n\ge\lambda\}$.

2. By optional stopping (@thm-optional-stopping-discrete) for the bounded times $T\wedge n\le n$, $E[X_n]\ge E[X_{T\wedge n}]=E[X_T\mathbf 1_{\{T\le n\}}]+E[X_n\mathbf 1_{\{T>n\}}]$.

3. On $\{T\le n\}$ we have $X_T\ge\lambda$, so $E[X_n]\ge\lambda\Pr(T\le n)+E[X_n\mathbf 1_{\{T>n\}}]$. Subtract: $\lambda\Pr(X^*_n\ge\lambda)\le E[X_n\mathbf 1_{\{T\le n\}}]$.

:::

::: {#fig-doob-inequalities-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (7.2,0) node[lab, right] {$k$};
\draw[faint] (0,2) -- (7,2);
\node[tick, left] at (0,2) {$\lambda$};
\draw[emph] (0,0.4) -- (1,0.9) -- (2,0.6) -- (3,1.4) -- (4,2.3) -- (5,1.5) -- (6,1.1) -- (7,1.6);
\draw[hl] (4,0) -- (4,2.3);
\node[tick] at (4,-0.3) {$T$};
\node[lab, text=accent] at (3.0,2.9) {$X^*_n\ge\lambda$ iff the path reaches $\lambda$ by time $n$};
\end{tikzpicture}
\end{center}
```

The first time $T$ the path reaches $\lambda$ splits the event $\{X^*_n\ge\lambda\}$ by where the path is stopped; the proof compares $E[X_n]$ with the value $\ge\lambda$ collected at $T$.

:::

::: {#lem-doob-lp-inequality .lemma name="Doob's $L^p$ inequality"}

For a martingale or non-negative sub-martingale and $p>1$,

$$
\|X^*_n\|_p\le\frac{p}{p-1}\,\|X_n\|_p .
$$

:::

::: {.proof}

1. Fix $k>0$. Since $x^p=\int_0^xp\,s^{p-1}ds$, Fubini (@thm-fubini) gives $\|X^*_n\wedge k\|_p^p=\int_0^kp\,x^{p-1}\Pr(X^*_n\ge x)\,dx$.

2. By the maximal inequality, this is at most $\int_0^kp\,x^{p-2}E[|X_n|\mathbf 1_{\{X^*_n\ge x\}}]\,dx$, and Fubini again turns it into $E\big[|X_n|\int_0^{X^*_n\wedge k}p\,x^{p-2}dx\big]=\frac p{p-1}E\big[|X_n|(X^*_n\wedge k)^{p-1}\big]$.

3. By Hölder with exponents $p$ and $q=p/(p-1)$, this is at most $\frac p{p-1}\|X_n\|_p\,\|X^*_n\wedge k\|_p^{p-1}$.

4. Divide by $\|X^*_n\wedge k\|_p^{p-1}$ (if nonzero) and let $k\to\infty$ with monotone convergence.

:::

::: {#rmk-doob-inequalities-1 .remark name="Why the factor"}

Letting $n\to\infty$, a martingale bounded in $L^p$ has $\|X^*\|_p\le\frac p{p-1}\sup_n\|X_n\|_p<\infty$ (monotone convergence): the whole path is dominated by one $L^p$ variable. This is the domination used for $L^p$ convergence in @sec-math-probability-martingales-lp-and-l1-martingale-convergence. The case $p=1$ fails: the maximal inequality only gives a weak-type bound.

:::
