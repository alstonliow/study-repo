---
title: "Null Hypothesis Significance Testing"
sources: [mit1805-17, mit1805-18, mit1805-20]
requires: [math/probability/estimation/hypothesis-testing, math/probability/continuous/central-limit-theorem, math/statistics/bayesian/credible-intervals]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Classes 17, 18 and 20, in our own wording; proofs written out in steps. -->

Frequentist statistics assigns probabilities only to repeatable random events, never to hypotheses. A significance test therefore does not compute how probable a hypothesis is; it asks whether the data would be surprising if a default hypothesis were true. The Neyman–Pearson setting of @def-neyman-pearson-problem is the special case with two simple hypotheses.

::: {#def-significance-test .definition name="Significance test"}

A *significance test* consists of

1. a *null hypothesis* $H_0$, the default assumption, and an *alternative hypothesis* $H_A$;
2. a *test statistic* $X$, computed from the data;
3. the *null distribution*: the distribution of $X$ when $H_0$ is true;
4. a *rejection region* $R$: if the observed value $x$ lies in $R$ we *reject* $H_0$ in favour of $H_A$; otherwise we *do not reject* $H_0$.

A hypothesis is *simple* if it fixes the distribution of the data completely, and *composite* otherwise ($\theta>0.5$, say).

:::

::: {#def-significance-power .definition name="Errors, significance level, power"}

A *type I error* is rejecting $H_0$ when it is true; a *type II error* is not rejecting $H_0$ when $H_A$ is true. The *significance level* of the test is
$$\alpha=\Pr(X\in R\mid H_0)$$
(for composite $H_0$, the largest such probability), and for a simple alternative its *power* is
$$\Pr(X\in R\mid H_A)=1-\Pr(\text{type II error}).$$

:::

A test is designed by fixing $\alpha$ (often $0.05$ or $0.01$) and choosing $R$ in the tails of the null distribution, on the side or sides where values are more likely under $H_A$. A *one-sided* region has the form $X\ge c$ or $X\le c$; a *two-sided* region has the form $X\le c_1$ or $X\ge c_2$. The boundary values are the *critical values*.

::: {#exm-binomial-test .example name="Testing a coin"}

A coin is tossed $10$ times and $X$ is the number of heads. Take $H_0:\theta=0.5$, $H_A:\theta=0.7$ and the rejection region $R=\{0,1,2,8,9,10\}$. Then
$$\alpha=\Pr(X\in R\mid\theta=0.5)=\frac{2(1+10+45)}{1024}\approx0.109,\qquad\text{power}=\Pr(X\in R\mid\theta=0.7)\approx0.384 .$$
Shrinking $R$ to $\{0,1,9,10\}$ lowers $\alpha$ to $0.021$ but also lowers the power to $0.149$: with only ten tosses no test separates the two hypotheses well.

:::

::: {#def-p-value .definition name="p-value"}

The *p-value* of an observed statistic $x$ is the probability, under $H_0$, of a value of $X$ at least as extreme as $x$, where "extreme" means "further into the rejection side". For a right-sided test $p=\Pr(X\ge x\mid H_0)$; for a two-sided test with a symmetric null distribution about $m$, $p=\Pr(|X-m|\ge|x-m|\mid H_0)$.

:::

::: {#prp-p-value-rule .proposition name="Rejecting by p-value"}

For a right-sided test whose rejection region at level $\alpha$ is $\{X\ge c\}$ with $\Pr(X\ge c\mid H_0)=\alpha$ and a continuous null distribution, $H_0$ is rejected if and only if $p\le\alpha$.

:::

::: {.proof}

1. The function $g(t)=\Pr(X\ge t\mid H_0)$ is continuous and non-increasing, and strictly decreasing where the null density is positive.

2. If $x\ge c$ then $p=g(x)\le g(c)=\alpha$.

3. If $x<c$ and $x$ lies in the range of $X$, then $p=g(x)>g(c)=\alpha$ by strict decrease. So $p\le\alpha$ exactly when $x$ is in the rejection region. The left-sided and two-sided cases are the same argument.

:::

::: {#def-z-test .definition name="z-test"}

Let $x_1,\dots,x_n$ be independent $N(\mu,\sigma^2)$ data with $\sigma$ *known*, and $H_0:\mu=\mu_0$. The test statistic is the *standardized mean*
$$z=\frac{\bar x-\mu_0}{\sigma/\sqrt n},$$
whose null distribution is $N(0,1)$. The two-sided test at level $\alpha$ rejects when $|z|\ge z_{\alpha/2}$, where $z_{\alpha/2}=q_{1-\alpha/2}$ is the standard normal critical value ($1.96$ for $\alpha=0.05$).

:::

::: {#exm-z-test .example name="A z-test"}

Scores are $N(\mu,15^2)$ and $H_0:\mu=100$. Nine people score a mean of $\bar x=112$. Then $z=\frac{12}{15/3}=2.4$, and the two-sided p-value is $2(1-\Phi(2.4))\approx0.016$. We reject $H_0$ at level $0.05$ but not at level $0.01$.

:::

::: {#rmk-p-value-meaning .remark name="What a p-value is not"}

A p-value is computed assuming $H_0$; it is not $\Pr(H_0\mid\text{data})$, and a large p-value is not evidence that $H_0$ is true. "Not rejecting" only means the data are consistent with $H_0$. Running many tests at level $0.05$ makes some false rejections almost certain, and selecting the significant ones afterwards hides this.

:::

::: {#rmk-bayes-versus-frequentist .remark name="Bayesian and frequentist inference compared" related="def-bayesian-update-table"}

Both schools use the likelihood $p(\text{data}\mid\theta)$. The Bayesian also needs a prior and in return can state probabilities of hypotheses; the frequentist avoids priors but can only state how the procedure behaves over repetitions, for every $\theta$. One visible difference is the *stopping rule*. Suppose $9$ heads and $3$ tails are seen and $H_0:\theta=0.5$ is tested against $\theta>0.5$. If the plan was to toss $12$ times, the one-sided p-value is $\Pr(X\ge9)=299/4096\approx0.073$; if the plan was to toss until the third tails, it is the probability of at least $9$ heads before the third tails, $\approx0.033$. The likelihoods are both proportional to $\theta^9(1-\theta)^3$, so any Bayesian posterior is the same in the two cases; the p-values are not, because they depend on outcomes that did not happen.

:::
