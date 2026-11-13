---
title: "The coupon collector's problem"
sources: [fit1058-cn-10.11]
requires: [math/discrete/sequences/sums-and-series]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: The coupon collector's problem. -->

::: {#thm-coupon-collector .theorem name="Coupon collector"}

There are $n$ types of coupon, and each draw gives a type chosen uniformly at random, independently. Let $T$ be the number of draws needed to collect all $n$ types. Then
$$E[T] = n H_n = n\left(1+\frac12+\cdots+\frac1n\right).$$

:::

::: {.proof}

Let $T_i$ be the number of draws taken to go from $i-1$ to $i$ distinct types, so $T=\sum_{i=1}^n T_i$. When $i-1$ types have been collected, each draw is new with probability $\frac{n-i+1}{n}$, so $T_i$ is geometric with this $p$, and $E[T_i]=\frac{n}{n-i+1}$. By linearity,
$$E[T] = \sum_{i=1}^n \frac{n}{n-i+1} = n\sum_{j=1}^n\frac1j = nH_n,$$
substituting $j=n-i+1$.

:::

::: {#exm-coupon-collector-1 .example}

To see all six faces of a die takes on average $6H_6=6\bigl(1+\frac12+\frac13+\frac14+\frac15+\frac16\bigr)=14.7$ throws.

:::

::: {.remark name="The last few are expensive"}

Since $H_n\approx\ln n$ (@sec-math-discrete-sequences-sums-and-series), collecting all $n$ types takes about $n\ln n$ draws, not about $n$. The early types come quickly; the last one alone takes $n$ draws on average.

:::
