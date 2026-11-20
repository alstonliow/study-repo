---
title: "Confidence Intervals"
sources: [mit1805-22, mit1805-23]
requires: [math/statistics/frequentist/chi-square-and-f-tests, math/probability/estimation/classical-estimation]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Classes 22 and 23, in our own wording; proofs written out in steps. -->

A confidence interval (@def-confidence-interval) is an interval computed from the data that contains the true parameter for a fixed fraction of all possible data sets. For normal data the standardized statistics of the previous notes give exact intervals; for other data the central limit theorem gives approximate ones.

::: {#thm-normal-confidence-intervals .theorem name="Confidence intervals for normal data"}

Let $x_1,\dots,x_n$ be independent $N(\mu,\sigma^2)$ data and $0<\alpha<1$. Write $z_{\alpha/2}$, $t_{n-1,\alpha/2}$ for the upper critical values of $N(0,1)$ and $t_{n-1}$, and $c_{\alpha/2}$, $c_{1-\alpha/2}$ for those of $\chi^2_{n-1}$ (so $\Pr(\chi^2_{n-1}\ge c_\beta)=\beta$). Each of the following is a $1-\alpha$ confidence interval:

1. for $\mu$, $\sigma$ known (*z-interval*): $\Bigl[\bar x-z_{\alpha/2}\dfrac\sigma{\sqrt n},\ \bar x+z_{\alpha/2}\dfrac\sigma{\sqrt n}\Bigr]$;
2. for $\mu$, $\sigma$ unknown (*t-interval*): $\Bigl[\bar x-t_{n-1,\alpha/2}\dfrac s{\sqrt n},\ \bar x+t_{n-1,\alpha/2}\dfrac s{\sqrt n}\Bigr]$;
3. for $\sigma^2$ (*chi-square interval*): $\Bigl[\dfrac{(n-1)s^2}{c_{\alpha/2}},\ \dfrac{(n-1)s^2}{c_{1-\alpha/2}}\Bigr]$.

:::

::: {.proof}

1. *t-interval.* By @thm-normal-sample-theory, $T=(\bar X-\mu)/(S/\sqrt n)\sim t_{n-1}$ whatever $\mu$ and $\sigma$ are, and $t_{n-1}$ is symmetric, so $\Pr(-t_{n-1,\alpha/2}\le T\le t_{n-1,\alpha/2})=1-\alpha$.

2. *Pivot.* The inequality $-t_{n-1,\alpha/2}\le(\bar X-\mu)/(S/\sqrt n)\le t_{n-1,\alpha/2}$ is equivalent, after multiplying by $S/\sqrt n>0$ and rearranging, to $\bar X-t_{n-1,\alpha/2}S/\sqrt n\le\mu\le\bar X+t_{n-1,\alpha/2}S/\sqrt n$. So this random interval contains $\mu$ with probability $1-\alpha$.

3. *z-interval.* The same two steps with $Z=(\bar X-\mu)/(\sigma/\sqrt n)\sim N(0,1)$.

4. *Chi-square interval.* $V=(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$, so $\Pr(c_{1-\alpha/2}\le V\le c_{\alpha/2})=1-\alpha$. Taking reciprocals and multiplying by $(n-1)S^2$, the inequality is equivalent to $(n-1)S^2/c_{\alpha/2}\le\sigma^2\le(n-1)S^2/c_{1-\alpha/2}$.

:::

A statistic such as $T$ whose distribution does not depend on the unknown parameters is called a *pivot*; every interval above comes from solving a pivot's probability statement for the parameter.

::: {#exm-t-interval .example name="Intervals from five measurements"}

For the data of @exm-one-sample-t-test ($\bar x=3$, $s^2=0.185$, $n=5$), $t_{4,0.025}\approx2.776$ gives the $95\%$ t-interval $3\pm0.534=[2.47,\ 3.53]$ for $\mu$. With $c_{0.975}\approx0.484$ and $c_{0.025}\approx11.14$ for $\chi^2_4$, the $95\%$ interval for $\sigma^2$ is $[0.066,\ 1.53]$: five points say little about a variance.

:::

::: {#thm-interval-test-duality .theorem name="Confidence intervals and tests"}

Suppose that for every $\theta_0$ there is a test of $H_0:\theta=\theta_0$ at level $\alpha$. The set of $\theta_0$ that the observed data do *not* reject is a $1-\alpha$ confidence set for $\theta$.

:::

::: {.proof}

1. Let $C(x)=\{\theta_0: x\notin R_{\theta_0}\}$, where $R_{\theta_0}$ is the rejection region of the test of $\theta_0$.

2. If the true value is $\theta$, then $\theta\in C(X)$ exactly when $X\notin R_\theta$.

3. The test of $\theta$ has level $\alpha$, so $\Pr_\theta(X\in R_\theta)\le\alpha$ and $\Pr_\theta(\theta\in C(X))\ge1-\alpha$, for every $\theta$.

:::

For example, the $95\%$ t-interval $[2.47,3.53]$ above contains $2.5$, matching the fact that the t-test of @exm-one-sample-t-test did not reject $\mu=2.5$.

::: {#prp-conservative-proportion-interval .proposition name="Conservative interval for a proportion"}

Let $x_1,\dots,x_n$ be independent Bernoulli$(\theta)$ and $\bar x$ the sample proportion. For large $n$,
$$\Bigl[\bar x-\frac{z_{\alpha/2}}{2\sqrt n},\ \bar x+\frac{z_{\alpha/2}}{2\sqrt n}\Bigr]$$
is approximately a confidence interval with confidence level at least $1-\alpha$. For $\alpha=0.05$ it is roughly $\bar x\pm1/\sqrt n$.

:::

::: {.proof}

1. Each $x_i$ has variance $\theta(1-\theta)=\frac14-(\theta-\frac12)^2\le\frac14$, so $\sigma=\sqrt{\theta(1-\theta)}\le\frac12$.

2. By the central limit theorem (@thm-central-limit-theorem), $\bar X$ is approximately $N(\theta,\sigma^2/n)$, so $\bar X\pm z_{\alpha/2}\sigma/\sqrt n$ is an approximate $1-\alpha$ interval.

3. Replacing $\sigma$ by its upper bound $\frac12$ can only widen the interval, so it contains $\theta$ at least as often. Finally $z_{0.025}/2\approx0.98\approx1$.

:::

A poll of $1000$ people therefore has a margin of error of about $1/\sqrt{1000}\approx3\%$, which is the figure newspapers usually quote.

::: {#rmk-large-sample-interval .remark name="Large-sample intervals"}

For any independent data with finite variance and large $n$, $\bar x\pm z_{\alpha/2}\,s/\sqrt n$ is an approximate $1-\alpha$ interval for the mean: the central limit theorem makes $\bar X$ nearly normal and $s$ is close to $\sigma$. The t-interval is then almost the same, since $t_{n-1}$ is close to $N(0,1)$.

:::

::: {#rmk-confidence-misreading .remark name="Reading a confidence interval" related="def-probability-interval"}

Once the data are in, a computed interval such as $[2.47,3.53]$ either contains $\mu$ or does not; "$95\%$" describes the procedure, not this interval. A Bayesian probability interval does assign probability $0.95$ to the parameter lying in the computed interval, but only relative to a prior. For normal data with known $\sigma$ and a flat prior on $\mu$, the posterior is $N(\bar x,\sigma^2/n)$ and its symmetric probability interval coincides numerically with the z-interval, which is why they are often confused.

:::
