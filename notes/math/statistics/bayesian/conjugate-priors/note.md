---
title: "Conjugate Priors: Beta and Normal"
sources: [mit1805-15]
requires: [math/statistics/bayesian/odds-and-prediction, math/probability/distributions/normal-distribution]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Classes 14 and 15, in our own wording; proofs written out in steps. -->

For most priors the posterior has no simple formula and the normalising integral must be computed numerically. For some likelihoods there is a family of priors that the update maps into itself; then updating only changes a few parameters.

::: {#def-conjugate-prior .definition name="Conjugate prior"}

A family $\mathcal F$ of distributions for a parameter $\theta$ is *conjugate* to a likelihood $p(x\mid\theta)$ if, for every prior in $\mathcal F$ and every observation $x$, the posterior is again in $\mathcal F$.

:::

::: {#lem-beta-integral .lemma name="Beta integral"}

For integers $a,b\ge0$,
$$\int_0^1\theta^a(1-\theta)^b\,d\theta=\frac{a!\,b!}{(a+b+1)!}.$$

:::

::: {.proof}

1. Write $I(a,b)$ for the integral. For $b=0$, $I(a,0)=\frac1{a+1}=\frac{a!\,0!}{(a+1)!}$.

2. For $b\ge1$, integrate by parts with $u=(1-\theta)^b$ and $dv=\theta^a\,d\theta$. The boundary term $\bigl[\frac{\theta^{a+1}}{a+1}(1-\theta)^b\bigr]_0^1$ vanishes, so
$$I(a,b)=\frac b{a+1}\,I(a+1,b-1).$$

3. Assume the formula for $b-1$ and every $a$ (induction on $b$). Then $I(a,b)=\frac b{a+1}\cdot\frac{(a+1)!\,(b-1)!}{(a+b+1)!}=\frac{a!\,b!}{(a+b+1)!}$.

:::

::: {#def-beta-distribution .definition name="Beta distribution"}

For $a,b>0$, the *beta distribution* $\operatorname{Beta}(a,b)$ has density
$$f(\theta)=c\,\theta^{a-1}(1-\theta)^{b-1}\qquad(0\le\theta\le1),$$
where $c$ makes the total integral $1$; for integer $a,b$, @lem-beta-integral gives $c=\dfrac{(a+b-1)!}{(a-1)!\,(b-1)!}$. Its mean is $\dfrac a{a+b}$ and, for $a,b>1$, its mode is $\dfrac{a-1}{a+b-2}$. $\operatorname{Beta}(1,1)$ is the uniform distribution on $[0,1]$.

:::

::: {#thm-beta-binomial-update .theorem name="Beta prior, binomial data"}

Let the prior for a success probability $\theta$ be $\operatorname{Beta}(a,b)$, and let the data be $k$ successes in $n$ independent Bernoulli$(\theta)$ trials. The posterior is
$$\operatorname{Beta}(a+k,\ b+n-k).$$

:::

::: {.proof}

1. The likelihood is $\binom nk\theta^k(1-\theta)^{n-k}$. It does not matter whether the order of the trials is recorded: that only changes the constant $\binom nk$.

2. Posterior $\propto$ likelihood $\times$ prior, so $f(\theta\mid k)\propto\theta^{k}(1-\theta)^{n-k}\cdot\theta^{a-1}(1-\theta)^{b-1}=\theta^{a+k-1}(1-\theta)^{b+n-k-1}$ on $[0,1]$.

3. A density proportional to $\theta^{a'-1}(1-\theta)^{b'-1}$ is $\operatorname{Beta}(a',b')$, because the constant is fixed by the total integral being $1$.

:::

Each success adds $1$ to $a$ and each failure adds $1$ to $b$, so $a-1$ and $b-1$ act like successes and failures seen before the experiment.

::: {#prp-beta-geometric-update .proposition name="Beta prior, geometric data"}

If the prior is $\operatorname{Beta}(a,b)$ and the data are that the first success came on trial $n$, the posterior is $\operatorname{Beta}(a+1,\ b+n-1)$.

:::

::: {.proof}

1. The likelihood of $n-1$ failures followed by a success is $(1-\theta)^{n-1}\theta$.

2. Multiplying by the prior gives $\theta^{a}(1-\theta)^{b+n-2}$, which is proportional to the $\operatorname{Beta}(a+1,b+n-1)$ density.

:::

::: {#exm-beta-coin .example name="Eight heads in ten tosses" related="exm-coin-bias-uniform-prior"}

With the flat prior $\operatorname{Beta}(1,1)$ and $8$ heads in $10$ tosses, the posterior is $\operatorname{Beta}(9,3)$: mean $9/12=0.75$, mode (the MAP estimate) $8/10=0.8$. By @prp-posterior-predictive the probability that the next toss is heads is the posterior mean of $\theta$, $0.75$.

:::

::: {#cor-rule-of-succession .corollary name="Laplace's rule of succession"}

With a uniform prior on $\theta$, after $k$ successes in $n$ trials the posterior predictive probability of a success on the next trial is $\dfrac{k+1}{n+2}$.

:::

::: {.proof}

1. By @thm-beta-binomial-update the posterior is $\operatorname{Beta}(k+1,n-k+1)$.

2. By @prp-posterior-predictive the predictive probability of a success is $\int_0^1\theta f(\theta\mid\text{data})\,d\theta$, the posterior mean, which is $\frac{k+1}{(k+1)+(n-k+1)}=\frac{k+1}{n+2}$.

:::

::: {#thm-normal-normal-update .theorem name="Normal prior, normal data" related="exm-normal-prior-normal-noise"}

Let the prior for $\theta$ be $N(\mu_{\mathrm{prior}},\sigma^2_{\mathrm{prior}})$, and let $x_1,\dots,x_n$ be independent $N(\theta,\sigma^2)$ observations with $\sigma$ known and mean $\bar x$. Put
$$a=\frac1{\sigma^2_{\mathrm{prior}}},\qquad b=\frac n{\sigma^2}.$$
The posterior is $N(\mu_{\mathrm{post}},\sigma^2_{\mathrm{post}})$ with
$$\mu_{\mathrm{post}}=\frac{a\,\mu_{\mathrm{prior}}+b\,\bar x}{a+b},\qquad\sigma^2_{\mathrm{post}}=\frac1{a+b}.$$

:::

::: {.proof}

1. The likelihood is proportional to $\exp\bigl(-\frac1{2\sigma^2}\sum_i(x_i-\theta)^2\bigr)$. Since $\sum_i(x_i-\theta)^2=\sum_i(x_i-\bar x)^2+n(\bar x-\theta)^2$ and the first sum does not involve $\theta$, the likelihood is proportional to $\exp\bigl(-\frac b2(\theta-\bar x)^2\bigr)$.

2. The prior is proportional to $\exp\bigl(-\frac a2(\theta-\mu_{\mathrm{prior}})^2\bigr)$. The posterior is proportional to the product, $\exp(-\frac12Q(\theta))$ with $Q(\theta)=a(\theta-\mu_{\mathrm{prior}})^2+b(\theta-\bar x)^2$.

3. Expand and complete the square: $Q(\theta)=(a+b)\theta^2-2(a\mu_{\mathrm{prior}}+b\bar x)\theta+\text{const}=(a+b)(\theta-\mu_{\mathrm{post}})^2+\text{const}$.

4. So the posterior density is proportional to $\exp\bigl(-\frac{(\theta-\mu_{\mathrm{post}})^2}{2/(a+b)}\bigr)$, the $N(\mu_{\mathrm{post}},1/(a+b))$ density.

:::

::: {#rmk-precision-weights .remark name="Precisions add"}

The reciprocal of a variance is called a *precision*. The posterior precision $a+b$ is the prior precision plus the precision of the data, and the posterior mean is the average of the prior mean and $\bar x$ weighted by their precisions. As $n$ grows, $b$ dominates: the posterior mean tends to $\bar x$ and the posterior variance to $0$.

:::

::: {#exm-normal-normal-one-point .example name="One measurement"}

Prior $N(4,4)$, one measurement $x=3$ with noise variance $\sigma^2=1$. Then $a=\frac14$, $b=1$, so $\mu_{\mathrm{post}}=\frac{1+3}{1.25}=3.2$ and $\sigma^2_{\mathrm{post}}=0.8$. The measurement is four times as precise as the prior, so the posterior mean sits four fifths of the way from $4$ to $3$.

:::
