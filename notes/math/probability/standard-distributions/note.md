---
title: "Standard Distributions"
sources: [fit1058-cn-10.7, fit1058-cn-10.8, fit1058-cn-10.9, fit1058-cn-10.10]
requires: [math/discrete/counting/combinations, math/discrete/sequences/sums-and-series]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Uniform distribution; Binomial distribution; Poisson distribution; Geometric distribution. -->

## Uniform distribution

::: {#def-discrete-uniform-distribution .definition name="Discrete uniform distribution"}

$X\sim\mathrm{Unif}(a,b)$ means $X$ takes each integer value in $[a,b]$ with the same probability $1/(b-a+1)$.

:::

::: {#exm-standard-distributions-1 .example}

A fair coin with Tails $=0$ and Heads $=1$ is $\mathrm{Unif}(0,1)$; a fair die is $\mathrm{Unif}(1,6)$. The uniform distribution is also used to model ignorance: with no other information, the age of an adult learner driver might be modelled as $\mathrm{Unif}(18,21)$.

:::

::: {#prp-standard-distributions-1 .proposition}

If $X\sim\mathrm{Unif}(1,n)$, then $E[X] = \dfrac{n+1}{2}$ and $\mathrm{Var}(X) = \dfrac{n^2-1}{12}$.

:::

::: {.proof}

$E[X]=\frac1n\sum_{k=1}^n k = \frac{n+1}2$ (@sec-math-discrete-sequences-sums-and-series). Also $E[X^2]=\frac1n\sum_{k=1}^n k^2=\frac{(n+1)(2n+1)}6$, so $\mathrm{Var}(X)=\frac{(n+1)(2n+1)}6-\frac{(n+1)^2}4=\frac{n^2-1}{12}$.

:::

## Binomial distribution

::: {#def-bernoulli-trial .definition name="Bernoulli trial"}

A *Bernoulli trial* is a random experiment with two outcomes, “success” with probability $p$ and “failure” with probability $1-p$.

:::

::: {#def-binomial-distribution .definition name="Binomial distribution"}

$X\sim\mathrm{Bin}(n,p)$ is the number of successes in $n$ independent Bernoulli trials, each with success probability $p$:
$$\Pr(X=k) = \binom{n}{k}p^k(1-p)^{n-k}, \qquad k=0,1,\dots,n.$$

:::

::: {.remark name="Where the formula comes from"}

$\binom nk$ counts the ways to choose which $k$ of the $n$ trials succeed (@sec-math-discrete-counting-combinations), and each such outcome has probability $p^k(1-p)^{n-k}$ by independence.

:::

::: {#exm-standard-distributions-1-2 .example}

For $n=10$, $p=0.3$:  $\Pr(X=6)=\binom{10}6(0.3)^6(0.7)^4=210\cdot0.000729\cdot0.2401\approx0.037$.

:::

::: {#prp-standard-distributions-1-2 .proposition}

If $X\sim\mathrm{Bin}(n,p)$, then $E[X] = np$ and $\mathrm{Var}(X) = np(1-p)$.

:::

::: {.proof}

Let $X_i=1$ if trial $i$ succeeds and $0$ otherwise, so $X=\sum_i X_i$. Each $E[X_i]=p$, so $E[X]=np$ by linearity. Also $\mathrm{Var}(X_i)=E[X_i^2]-E[X_i]^2=p-p^2=p(1-p)$, and the $X_i$ are independent, so $\mathrm{Var}(X)=np(1-p)$ by the variance of an independent sum.

:::

## Poisson distribution

::: {#def-poisson-distribution .definition name="Poisson distribution"}

$X\sim\mathrm{Poisson}(\mu)$, for a parameter $\mu>0$, means
$$\Pr(X=k) = \frac{e^{-\mu}\mu^k}{k!}, \qquad k=0,1,2,\dots$$

:::

::: {.remark name="When it applies"}

The Poisson distribution counts events that happen independently at random times, at a steady average rate, during a fixed time interval: phone calls to a call centre, visits to a website, coins tossed into a busker’s cap, alpha particles emitted by radioactive material. The parameter $\mu$ is the average number of events in the interval.

:::

::: {#exm-standard-distributions-1-3 .example}

For $\mu=3$:  $\Pr(X\le2)=e^{-3}\bigl(1+3+\tfrac92\bigr)\approx0.0498+0.1494+0.2240\approx0.423$.

:::

::: {#prp-standard-distributions-1-3 .proposition}

If $X\sim\mathrm{Poisson}(\mu)$, then $E[X]=\mu$ and $\mathrm{Var}(X)=\mu$.

:::

::: {#thm-poisson-as-a-limit-of .theorem name="Poisson as a limit of binomial"}

Fix $\mu>0$. As $n\to\infty$ with $p=\mu/n$,
$$\binom{n}{k}p^k(1-p)^{n-k} \to \frac{e^{-\mu}\mu^k}{k!}.$$

:::

::: {.proof}

Write the left side as $\dfrac{\mu^k}{k!}\cdot\dfrac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\Bigl(1-\dfrac\mu n\Bigr)^{n-k}$. As $n\to\infty$, the middle factor tends to $1$ (it is a product of $k$ factors, each tending to $1$), and the last tends to $e^{-\mu}$ (using $(1+x/n)^n\to e^x$).

:::

::: {.remark name="Approximating the binomial"}

So $\mathrm{Bin}(n,p)$ with $n$ large, $p$ small and $np$ moderate is well approximated by $\mathrm{Poisson}(np)$: think of many trials, each with a small chance of a rare event.

:::

## Geometric distribution

::: {#def-geometric-distribution .definition name="Geometric distribution"}

$X\sim\mathrm{Geom}(p)$ is the number of independent Bernoulli trials, each with success probability $p$, up to and including the first success:
$$\Pr(X=k) = (1-p)^{k-1}p, \qquad k=1,2,3,\dots$$

:::

::: {.remark name="Two conventions"}

Some books instead count the failures *before* the first success, which is $X-1$. Check which one is meant.

:::

::: {#exm-standard-distributions-1-4 .example}

For $p=0.3$:  $\Pr(X=6)=(0.7)^5\cdot0.3\approx0.050$.

:::

::: {#prp-standard-distributions-1-4 .proposition}

If $X\sim\mathrm{Geom}(p)$, then $E[X] = \dfrac1p$ and $\mathrm{Var}(X)=\dfrac{1-p}{p^2}$.

:::

::: {.proof name="Proof of the expectation"}

$E[X] = p\sum_{k\ge1} k(1-p)^{k-1}$. Differentiating the geometric series $\sum_{k\ge0}x^k=\frac1{1-x}$ (@sec-math-discrete-sequences-sums-and-series) gives $\sum_{k\ge1}kx^{k-1}=\frac1{(1-x)^2}$; with $x=1-p$ this is $1/p^2$, so $E[X]=p\cdot\frac1{p^2}=\frac1p$.

:::

::: {.remark name="Memoryless property"}

Given that the first $t$ trials have all failed, the number of further trials needed is again $\mathrm{Geom}(p)$: past failures do not make success “due”. Examples include the number of loop iterations until a random stopping condition holds, the number of time intervals until a component fails, and the number of balls a cricket batter faces.

:::
