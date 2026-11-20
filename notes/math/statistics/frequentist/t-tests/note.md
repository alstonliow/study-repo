---
title: "Sample Variance and t-Tests"
sources: [mit1805-19, mit1805-22]
requires: [math/statistics/frequentist/significance-testing, math/probability/estimation/jointly-gaussian]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Classes 19 and 22, in our own wording; proofs written out in steps. -->

The z-test (@def-z-test) needs the true standard deviation $\sigma$. In practice $\sigma$ is unknown and is estimated from the same data; the extra randomness changes the null distribution from normal to Student's $t$.

::: {#def-sample-mean-variance .definition name="Sample mean, sample variance" related="exm-ml-normal"}

For data $x_1,\dots,x_n$ ($n\ge2$), the *sample mean* and *sample variance* are
$$\bar x=\frac1n\sum_{i=1}^nx_i,\qquad s^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2 .$$
Dividing by $n-1$ makes $s^2$ an unbiased estimator of the variance (@exm-ml-normal).

:::

::: {#def-chi-square-distribution .definition name="Chi-square distribution"}

If $Z_1,\dots,Z_m$ are independent standard normal, the distribution of $Z_1^2+\dots+Z_m^2$ is the *chi-square distribution with $m$ degrees of freedom*, $\chi^2_m$. It has mean $m$ and variance $2m$.

:::

::: {#def-t-distribution .definition name="Student's t distribution"}

If $Z\sim N(0,1)$ and $V\sim\chi^2_m$ are independent, the distribution of
$$T=\frac Z{\sqrt{V/m}}$$
is the *$t$ distribution with $m$ degrees of freedom*, $t_m$. It is symmetric about $0$, has heavier tails than $N(0,1)$, and tends to $N(0,1)$ as $m\to\infty$ (because $V/m\to1$ by the law of large numbers). Its critical values are written $t_{m,\alpha}=q_{1-\alpha}$.

:::

::: {#thm-normal-sample-theory .theorem name="Sampling from a normal distribution"}

Let $X_1,\dots,X_n$ be independent $N(\mu,\sigma^2)$, with sample mean $\bar X$ and sample variance $S^2$. Then

1. $\bar X\sim N(\mu,\sigma^2/n)$;
2. $\bar X$ and $S^2$ are independent;
3. $\dfrac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$;
4. $\dfrac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1}$.

:::

::: {.proof}

1. Standardize: $Z_i=(X_i-\mu)/\sigma$ are independent $N(0,1)$, so $Z=(Z_1,\dots,Z_n)$ is jointly Gaussian with covariance $I$. Then $\bar X=\mu+\sigma\bar Z$ and $(n-1)S^2/\sigma^2=\sum_i(Z_i-\bar Z)^2$.

2. Choose an orthogonal $n\times n$ matrix $Q$ whose first row is $(1/\sqrt n,\dots,1/\sqrt n)$ (complete this unit vector to an orthonormal basis). By @thm-jointly-gaussian-properties (item 2), $W=QZ\sim N(0,QQ^{\mathsf T})=N(0,I)$, so by item 4 of that theorem $W_1,\dots,W_n$ are independent $N(0,1)$.

3. $W_1=\frac1{\sqrt n}\sum_iZ_i=\sqrt n\,\bar Z$, so $\bar Z=W_1/\sqrt n\sim N(0,1/n)$ and $\bar X\sim N(\mu,\sigma^2/n)$. This is item 1.

4. Orthogonal matrices preserve length, so $\sum_iW_i^2=\sum_iZ_i^2$. Hence
$$\sum_{i=2}^nW_i^2=\sum_iZ_i^2-n\bar Z^2=\sum_i(Z_i-\bar Z)^2=\frac{(n-1)S^2}{\sigma^2}.$$
This is a sum of $n-1$ independent squared standard normals, so it is $\chi^2_{n-1}$ (item 3), and it depends only on $W_2,\dots,W_n$, which are independent of $W_1$; so $S^2$ is independent of $\bar X$ (item 2).

5. Finally $\dfrac{\bar X-\mu}{S/\sqrt n}=\dfrac{\sqrt n\,\bar Z}{\sqrt{(n-1)S^2/\sigma^2\,/\,(n-1)}}=\dfrac{W_1}{\sqrt{V/(n-1)}}$ with $V=\sum_{i\ge2}W_i^2$, which is $t_{n-1}$ by @def-t-distribution (item 4).

:::

::: {#def-one-sample-t-test .definition name="One-sample t-test"}

Let $x_1,\dots,x_n$ be independent $N(\mu,\sigma^2)$ data with $\mu$ and $\sigma$ unknown, and $H_0:\mu=\mu_0$. The *studentized mean*
$$t=\frac{\bar x-\mu_0}{s/\sqrt n}$$
has null distribution $t_{n-1}$ by @thm-normal-sample-theory. The two-sided test at level $\alpha$ rejects when $|t|\ge t_{n-1,\alpha/2}$.

:::

::: {#exm-one-sample-t-test .example name="A one-sample t-test"}

Five measurements $2.4,3.1,2.9,3.6,3.0$ have $\bar x=3.0$ and $s^2=0.185$. For $H_0:\mu=2.5$, $t=\frac{0.5}{\sqrt{0.185/5}}\approx2.60$. The critical value is $t_{4,0.025}\approx2.78$, so at level $0.05$ we do not reject $H_0$ (two-sided p-value $\approx0.060$). A z-test using $\sigma=\sqrt{0.185}$ as if it were known would have rejected: estimating $\sigma$ costs evidence.

:::

::: {#def-two-sample-t-test .definition name="Two-sample t-test, equal variances"}

Let $x_1,\dots,x_n$ be $N(\mu_x,\sigma^2)$ and $y_1,\dots,y_m$ be $N(\mu_y,\sigma^2)$, all independent, with the same unknown $\sigma$, and $H_0:\mu_x=\mu_y$. With the *pooled variance*
$$s_p^2=\frac{(n-1)s_x^2+(m-1)s_y^2}{n+m-2}\Bigl(\frac1n+\frac1m\Bigr),$$
the statistic $t=(\bar x-\bar y)/s_p$ has null distribution $t_{n+m-2}$.

:::

::: {#exm-two-sample-t-test .example name="Two groups"}

Groups $12,15,11,14,13$ and $10,12,9,11,13,11$ have means $13$ and $11$ and sample variances $2.5$ and $2$. Then $s_p^2=\frac{4\cdot2.5+5\cdot2}{9}\bigl(\frac15+\frac16\bigr)\approx0.815$ and $t=2/0.903\approx2.22$, just below $t_{9,0.025}\approx2.26$: not significant at level $0.05$ (p $\approx0.054$).

:::

::: {#rmk-t-test-variants .remark name="Other t-tests"}

If the two variances may differ, the statistic $(\bar x-\bar y)/\sqrt{s_x^2/n+s_y^2/m}$ is approximately $t$ with a data-dependent number of degrees of freedom (Welch's test). For *paired* data $(x_i,y_i)$, such as measurements on the same subject before and after a treatment, one applies the one-sample test to the differences $x_i-y_i$.

:::
