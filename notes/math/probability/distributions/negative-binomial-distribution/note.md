---
title: "Negative Binomial Distribution"
sources: [camib-st-1]
requires: [math/probability/distributions/geometric-distribution, math/probability/distributions/binomial-distribution]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 1 (review of important distributions), in our own wording; proofs written out in steps. The R convention (failures before the $k$-th success) is mentioned only as a remark. -->

The geometric distribution counts the trials up to the first success. Waiting for the $k$-th success instead gives the negative binomial distribution.

::: {#def-negative-binomial .definition name="Negative binomial distribution"}

In independent Bernoulli trials with success probability $p\in(0,1)$ let $X$ be the number of the trial on which the $k$-th success occurs. Then $X$ has the *negative binomial distribution* $\mathrm{NegBin}(k,p)$,
$$
P(X=x)=\binom{x-1}{k-1}(1-p)^{x-k}p^{k},\qquad x=k,k+1,\dots .
$$
For $k=1$ this is the geometric distribution (@def-geometric-distribution).

:::

::: {.proof}

The $k$-th success is on trial $x$ exactly when trial $x$ is a success and exactly $k-1$ of the first $x-1$ trials are successes. These two events are independent; the second has probability $\binom{x-1}{k-1}p^{k-1}(1-p)^{x-k}$ (@def-binomial-distribution), and multiplying by $p$ gives the formula.

:::

::: {#fig-negative-binomial-distribution-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.32cm,y=30cm]
\draw[->, muted] (9,0) -- (31.5,0) node[lab, right] {$x$};
\draw[->, muted] (9,0) -- (9,0.105);
\foreach \x in {10,15,20,25,30} \node[tick, below] at (\x,0) {$\x$};
\foreach \y in {0.05,0.10} \node[tick, left] at (9,\y) {$\y$};
\foreach \x/\v in {10/0.0010,11/0.0049,12/0.0134,13/0.0269,14/0.0436,15/0.0611,16/0.0764,17/0.0873,18/0.0927,19/0.0927,20/0.0881,21/0.0801,22/0.0701,23/0.0593,24/0.0487,25/0.0390,26/0.0304,27/0.0233,28/0.0175,29/0.0129,30/0.0093}
  \fill[primary] (\x-0.35,0) rectangle (\x+0.35,\v);
\draw[hl] (20,0) -- (20,0.1);
\node[lab, above] at (20,0.1) {mean $20$};
\end{tikzpicture}
\end{center}
```

The probability mass function of $\mathrm{NegBin}(10,\tfrac12)$: the number of tosses of a fair coin needed to get ten heads.

:::

::: {#thm-negative-binomial-moments .theorem name="Negative binomial as a sum of geometric waits"}

If $G_1,\dots,G_k$ are independent geometric variables with parameter $p$ (numbers of trials), then $G_1+\dots+G_k\sim\mathrm{NegBin}(k,p)$. Consequently
$$
E(X)=\frac kp,\qquad \mathrm{Var}(X)=\frac{k(1-p)}{p^2}.
$$

:::

::: {.proof}

1. Let $G_1$ be the number of trials up to the first success, $G_2$ the number of further trials up to the second, and so on. By independence of the trials after each success, $G_1,\dots,G_k$ are independent geometric variables with parameter $p$, and their sum is the number of the trial of the $k$-th success.

2. A geometric variable has mean $1/p$ and variance $(1-p)/p^2$. Means add, and variances add for independent variables.

:::

::: {#exm-negative-binomial-coin .example name="Ten heads"}

The number of fair-coin tosses needed to see $10$ heads is $\mathrm{NegBin}(10,\tfrac12)$, with mean $10/(1/2)=20$ and variance $10\cdot\tfrac12/\tfrac14=20$. The probability that exactly $20$ tosses are needed is $\binom{19}{9}2^{-20}\approx0.088$.

:::

::: {#rmk-negative-binomial-convention .remark name="Two conventions"}

Some texts, and the statistics package R, call $Y=X-k$ (the number of *failures* before the $k$-th success) negative binomial. Its support is $\{0,1,2,\dots\}$ and its mean is $k(1-p)/p$. Always check which of the two variables is meant.

:::
