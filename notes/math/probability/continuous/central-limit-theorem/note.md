---
title: "Central Limit Theorem"
sources: [cs70-20.5]
requires: [math/probability/continuous/normal-distribution, math/probability/discrete/concentration-inequalities]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 20 (cs70-20.5), in our own wording. The example is our own, checked by an exact computation. -->

The law of large numbers (@thm-law-of-large-numbers) says that the average $\frac{S_n}n$ of $n$ i.i.d. observations concentrates at the mean $\mu$. The central limit theorem says more: for large $n$ the *shape* of its distribution is close to the normal distribution $N\bigl(\mu,\frac{\sigma^2}n\bigr)$, whatever the distribution of a single observation. The mean and variance are known already (@prp-sample-mean); the new point is the normal shape. To get a limit that does not depend on $n$, standardize:
$$\frac{S_n/n-\mu}{\sigma/\sqrt n}=\frac{S_n-n\mu}{\sigma\sqrt n},$$
which has mean $0$ and variance $1$ for every $n$.

::: {#thm-central-limit-theorem .theorem name="Central limit theorem"}

Let $X_1,X_2,\dots$ be i.i.d. random variables with finite mean $\mu$ and finite variance $\sigma^2>0$, and let $S_n=X_1+\dots+X_n$. Then for every constant $c$,
$$\Pr\Bigl(\frac{S_n-n\mu}{\sigma\sqrt n}\le c\Bigr)\to\frac1{\sqrt{2\pi}}\int_{-\infty}^c e^{-x^2/2}\,dx\qquad\text{as }n\to\infty.$$

:::

::: {#rmk-central-limit-theorem-meaning}

1. We do not prove the theorem here; the usual proofs use characteristic or moment generating functions.

2. Every trace of the original distribution disappears except $\mu$ and $\sigma^2$. The standard deviation of the average is $\sigma/\sqrt n$, so its bell curve becomes a spike at $\mu$ at the rate $1/\sqrt n$.

3. This is why the normal distribution models aggregate data so well, such as measurement errors or the heights in a population: each value is a sum of many small, roughly independent effects.

4. In practice one replaces $\frac{S_n-n\mu}{\sigma\sqrt n}$ by a standard normal variable for moderately large $n$. The theorem gives no error bound; for one, see the Berry–Esseen theorem.

:::

::: {#exm-clt-dice .example name="Sum of a hundred dice"}

Roll $100$ fair dice and let $S$ be the total. One die has mean $\frac72$ and variance $\frac{35}{12}$ (@prp-standard-distributions-1), so $S$ has mean $350$ and standard deviation $\sqrt{100\cdot\frac{35}{12}}\approx17.08$. Then
$$\Pr(S\ge380)=\Pr\Bigl(\frac{S-350}{17.08}\ge1.757\Bigr)\approx1-\Phi(1.757)\approx0.039,$$
where $\Phi$ is the standard normal c.d.f. The exact value, from the distribution of $S$, is $0.0420$. Using $379.5$ in place of $380$ (a *continuity correction*, since $S$ takes integer values) gives $0.0421$.

:::
