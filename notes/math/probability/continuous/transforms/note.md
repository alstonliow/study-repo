---
title: "Moment Generating and Characteristic Functions"
sources: [eecs126hw-6, eecs126d-6]
requires: [math/probability/continuous/normal-distribution, math/probability/continuous/joint-distributions]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), Homework 6 and Discussion 6, in our own wording; proofs written out in steps. -->

A *transform* packs a whole distribution into one function. Sums of independent variables become products of transforms.

::: {#def-moment-generating-function .definition name="Moment generating function"}

The *moment generating function* (MGF) of a random variable $X$ is
$$M_X(s)=E\bigl[e^{sX}\bigr],$$
defined for those real $s$ where the expectation is finite. The *characteristic function* is
$$\varphi_X(t)=E\bigl[e^{itX}\bigr],\qquad t\in\mathbb{R},$$
which is defined for every $t$ since $|e^{itX}|=1$.

:::

::: {#fig-transforms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[xscale=1.6, yscale=0.8]
\draw[->] (-2.2,0) -- (1.4,0) node[lab, right] {$s$};
\draw[->] (0,-0.2) -- (0,4.6) node[lab, above] {$M_X(s)$};
\draw[faint, dashed] (1,0) -- (1,4.5); \node[tick, below] at (1,0) {$1$};
\draw[emph, primary] plot[domain=-2.1:0.77, samples=60] (\x,{1/(1-\x)});
\draw[accent] (-1,0) -- (0.9,1.9);
\node[hl dot] at (0,1) {};
\node[lab, left] at (-0.05,1.15) {$M_X(0)=1$};
\node[lab, below right] at (0.35,1.1) {slope $E[X]=1$};
\end{tikzpicture}
\end{center}
```

The moment generating function of $X\sim\operatorname{Exp}(1)$ is $M_X(s)=1/(1-s)$, finite only for $s<1$. Every MGF passes through $(0,1)$, and its slope there is $E[X]$.

:::

::: {#thm-transform-properties .theorem name="Properties of transforms"}

1. If $X$ and $Y$ are independent, $M_{X+Y}(s)=M_X(s)M_Y(s)$ and $\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)$.
2. $M_{aX+b}(s)=e^{bs}M_X(as)$.
3. If $M_X$ is finite on an interval around $0$, then $E[X^k]=M_X^{(k)}(0)$ for every $k\ge0$.
4. (Uniqueness) Two random variables with the same characteristic function have the same distribution; the same holds for MGFs that are finite on an interval around $0$.

:::

::: {.proof}

1. By independence $E[e^{s(X+Y)}]=E[e^{sX}e^{sY}]=E[e^{sX}]E[e^{sY}]$ (@thm-expectation-of-product); the same for $e^{it(X+Y)}$.

2. $E[e^{s(aX+b)}]=e^{bs}E[e^{(as)X}]$.

3. On the interval, $e^{sX}=\sum_ks^kX^k/k!$, and finiteness of $M_X$ at $\pm s_0$ dominates the series, so expectation and sum (and then differentiation at $0$) may be interchanged: $M_X(s)=\sum_kE[X^k]s^k/k!$, whose $k$-th derivative at $0$ is $E[X^k]$.

4. Uniqueness is the Fourier inversion theorem; we use it without proof.

:::

| distribution | $M_X(s)$ | $\varphi_X(t)$ |
|---|---|---|
| $\operatorname{Bernoulli}(p)$ | $1-p+pe^s$ | $1-p+pe^{it}$ |
| $\operatorname{Poisson}(\lambda)$ | $e^{\lambda(e^s-1)}$ | $e^{\lambda(e^{it}-1)}$ |
| $\operatorname{Exp}(\lambda)$ | $\frac{\lambda}{\lambda-s}$, $s<\lambda$ | $\frac{\lambda}{\lambda-it}$ |
| $N(\mu,\sigma^2)$ | $e^{\mu s+\sigma^2s^2/2}$ | $e^{i\mu t-\sigma^2t^2/2}$ |

::: {#exm-transform-poisson-sum .example name="Sums of Poissons"}

If $X\sim\operatorname{Poisson}(\lambda)$ and $Y\sim\operatorname{Poisson}(\mu)$ are independent, then $M_{X+Y}(s)=e^{\lambda(e^s-1)}e^{\mu(e^s-1)}=e^{(\lambda+\mu)(e^s-1)}$, so $X+Y\sim\operatorname{Poisson}(\lambda+\mu)$ by uniqueness. Differentiating, $M'(0)=\lambda+\mu$ and $M''(0)=(\lambda+\mu)+(\lambda+\mu)^2$, which give the mean and variance $\lambda+\mu$.

:::

::: {#rmk-transforms-1 .remark name="Why characteristic functions"}

The MGF of a heavy-tailed variable (Cauchy, for example) is infinite for every $s\neq0$, but its characteristic function always exists. Lévy's continuity theorem, $\varphi_{X_n}(t)\to\varphi_X(t)$ for all $t$ if and only if $X_n\to X$ in distribution (@def-convergence-in-distribution), is the standard route to the central limit theorem (@thm-central-limit-theorem).

:::
