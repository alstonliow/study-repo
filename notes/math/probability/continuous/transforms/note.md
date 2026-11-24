---
title: "Moment Generating and Characteristic Functions"
sources: [eecs126hw-6, eecs126d-6]
requires: [math/probability/continuous/normal-distribution, math/probability/continuous/joint-distributions]
relations:
  related: [math/probability/measure-theoretic/weak-convergence]
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

::: {#fig-transforms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.6,0) node[lab, right] {$k$};
\path[bar] (0.12,0) rectangle (0.24,0.947);
\path[bar] (0.67,0) rectangle (0.79,1.895);
\path[bar] (1.22,0) rectangle (1.34,1.895);
\path[bar] (1.77,0) rectangle (1.89,1.263);
\path[bar] (2.32,0) rectangle (2.44,0.632);
\path[bar] (2.87,0) rectangle (2.99,0.253);
\path[bar] (3.42,0) rectangle (3.54,0.084);
\path[bar] (3.97,0) rectangle (4.09,0.024);
\path[bar] (4.52,0) rectangle (4.64,0.006);
\path[bar] (5.07,0) rectangle (5.19,0.001);
\path[bar] (5.62,0) rectangle (5.74,0.000);
\path[bar] (6.17,0) rectangle (6.29,0.000);
\path[bar] (6.72,0) rectangle (6.84,0.000);
\path[cell frame] (0.24,0) rectangle (0.36,0.349);
\path[cell frame] (0.79,0) rectangle (0.91,1.046);
\path[cell frame] (1.34,0) rectangle (1.46,1.568);
\path[cell frame] (1.89,0) rectangle (2.01,1.568);
\path[cell frame] (2.44,0) rectangle (2.56,1.176);
\path[cell frame] (2.99,0) rectangle (3.11,0.706);
\path[cell frame] (3.54,0) rectangle (3.66,0.353);
\path[cell frame] (4.09,0) rectangle (4.21,0.151);
\path[cell frame] (4.64,0) rectangle (4.76,0.057);
\path[cell frame] (5.19,0) rectangle (5.31,0.019);
\path[cell frame] (5.74,0) rectangle (5.86,0.006);
\path[cell frame] (6.29,0) rectangle (6.41,0.002);
\path[cell frame] (6.84,0) rectangle (6.96,0.000);
\path[hl cell] (0.36,0) rectangle (0.48,0.047);
\path[hl cell] (0.91,0) rectangle (1.03,0.236);
\path[hl cell] (1.46,0) rectangle (1.58,0.590);
\path[hl cell] (2.01,0) rectangle (2.13,0.983);
\path[hl cell] (2.56,0) rectangle (2.68,1.228);
\path[hl cell] (3.11,0) rectangle (3.23,1.228);
\path[hl cell] (3.66,0) rectangle (3.78,1.024);
\path[hl cell] (4.21,0) rectangle (4.33,0.731);
\path[hl cell] (4.76,0) rectangle (4.88,0.457);
\path[hl cell] (5.31,0) rectangle (5.43,0.254);
\path[hl cell] (5.86,0) rectangle (5.98,0.127);
\path[hl cell] (6.41,0) rectangle (6.53,0.058);
\path[hl cell] (6.96,0) rectangle (7.08,0.024);
\draw (0.3,0) -- (0.3,-0.08) node[tick, below] {$0$};
\draw (1.40,0) -- (1.40,-0.08) node[tick, below] {$2$};
\draw (2.5,0) -- (2.5,-0.08) node[tick, below] {$4$};
\draw (3.6,0) -- (3.6,-0.08) node[tick, below] {$6$};
\draw (4.7,0) -- (4.7,-0.08) node[tick, below] {$8$};
\draw (5.8,0) -- (5.8,-0.08) node[tick, below] {$10$};
\draw (6.9,0) -- (6.9,-0.08) node[tick, below] {$12$};
\path[bar] (5,2.1) rectangle (5.2,2.25);
\node[tick, right] at (5.2,2.17) {$\mu=2$};
\path[cell frame] (5,1.8) rectangle (5.2,1.95);
\node[tick, right] at (5.2,1.87) {$\mu=3$};
\path[hl cell] (5,1.5) rectangle (5.2,1.65);
\node[tick, right] at (5.2,1.57) {sum, $\mu=5$};
\end{tikzpicture}
\end{center}
```

Transforms multiply under independent sums: $e^{2(e^s-1)}e^{3(e^s-1)}=e^{5(e^s-1)}$, so the sum of independent Poisson variables with means $2$ and $3$ is Poisson with mean $5$

:::

::: {#rmk-transforms-1 .remark name="Why characteristic functions"}

The MGF of a heavy-tailed variable (Cauchy, for example) is infinite for every $s\neq0$, but its characteristic function always exists. Lévy's continuity theorem, $\varphi_{X_n}(t)\to\varphi_X(t)$ for all $t$ if and only if $X_n\to X$ in distribution (@def-convergence-in-distribution), is the standard route to the central limit theorem (@thm-central-limit-theorem).

:::
