---
title: "Non-Informative Priors and Bayes Estimators"
sources: [mit18650-8]
requires: [math/statistics/inference/fisher-information, math/statistics/bayesian/credible-intervals]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 8 (posterior via Bayes' formula, improper priors, Jeffreys prior and its invariance, Bayesian confidence regions, the Bayes estimator as a frequentist tool), in our own wording. The invariance proof and the numerical example are our own; the rest of Bayesian updating is in the Bayesian statistics branch. -->

Bayesian updating (@sec-math-statistics-bayesian-bayesian-updating) treats the parameter as random, with a prior that expresses belief before the data. Two questions remain once Fisher information is available: what prior to use when one has no belief, and how Bayesian answers behave as frequentist estimators.

Recall the setting (@def-bayesian-model): a prior density $\pi$ on $\Theta$, and, given $\theta$, data $X_1,\dots,X_n$ with joint density $p_n(x_1,\dots,x_n\mid\theta)$. The posterior is
$$\pi(\theta\mid X_1,\dots,X_n)=\frac{\pi(\theta)\,p_n(X_1,\dots,X_n\mid\theta)}{\int_\Theta\pi(t)\,p_n(X_1,\dots,X_n\mid t)\,dt}\ \propto\ \pi(\theta)\,p_n(X_1,\dots,X_n\mid\theta).$$

::: {#def-improper-prior .definition name="Improper prior"}

An *improper prior* on $\Theta$ is a measurable function $\pi\ge0$ with $\int_\Theta\pi=\infty$. It is not a probability density, but if $\int_\Theta\pi(t)\,p_n(X_1,\dots,X_n\mid t)\,dt<\infty$ the formula above still defines a proper posterior density.

:::

::: {#exm-flat-prior-normal-mean .example name="A flat prior on a normal mean"}

Let $\pi(\theta)=1$ on $\mathbb{R}$, an improper prior, and given $\theta$ let the $X_i$ be independent $N(\theta,1)$. Then
$$\pi(\theta\mid X)\propto\exp\Bigl(-\frac12\sum_{i=1}^n(X_i-\theta)^2\Bigr)\propto\exp\Bigl(-\frac n2(\theta-\bar X_n)^2\Bigr),$$
using $\sum_i(X_i-\theta)^2=\sum_i(X_i-\bar X_n)^2+n(\theta-\bar X_n)^2$. The posterior is $N(\bar X_n,1/n)$, a proper distribution: the limit of the normal–normal update (@thm-normal-normal-update) as the prior variance tends to infinity.

:::

A flat prior is not "uninformative" in any absolute sense: flat in $p$ is not flat in $\log\frac p{1-p}$ or in $p^2$. Jeffreys proposed a prior that does not depend on how the model is parametrised.

::: {#def-jeffreys-prior .definition name="Jeffreys prior"}

For a model with Fisher information $I(\theta)$ (@def-fisher-information), the *Jeffreys prior* is

$$
\pi_J(\theta)\propto\sqrt{\det I(\theta)} ,
$$

proper or improper according to whether the right side is integrable over $\Theta$.

:::

::: {#exm-jeffreys-priors .example name="Two Jeffreys priors"}

1. *Bernoulli.* $I(p)=1/(p(1-p))$ (@exm-fisher-information-bernoulli), so $\pi_J(p)\propto p^{-1/2}(1-p)^{-1/2}$, the proper prior $\operatorname{Beta}(1/2,1/2)$ (@def-beta-distribution). It puts more weight near $0$ and $1$ than the uniform prior.
2. *Normal mean, known variance $1$.* $\ell(\theta)=-\frac12(X-\theta)^2+\text{const}$, so $I(\theta)=1$ and $\pi_J$ is the flat improper prior of @exm-flat-prior-normal-mean.

:::

::: {#prp-jeffreys-invariance .proposition name="Jeffreys prior does not depend on the parametrisation"}

Let $\eta=\varphi(\theta)$ with $\varphi$ a continuously differentiable bijection with non-vanishing derivative ($d=1$), and let $\tilde I(\eta)$ be the Fisher information of the same model written in terms of $\eta$. If $\theta$ has density proportional to $\sqrt{I(\theta)}$, then $\eta$ has density proportional to $\sqrt{\tilde I(\eta)}$.

:::

::: {.proof}

1. Write $\theta=\varphi^{-1}(\eta)$. The log-likelihood in the new parameter is $\tilde\ell(\eta)=\ell(\varphi^{-1}(\eta))$, so by the chain rule $\tilde\ell'(\eta)=\ell'(\theta)\,\dfrac{d\theta}{d\eta}$.

2. Hence $\tilde I(\eta)=\mathrm{Var}(\tilde\ell'(\eta))=I(\theta)\Bigl(\dfrac{d\theta}{d\eta}\Bigr)^2$ and $\sqrt{\tilde I(\eta)}=\sqrt{I(\theta)}\,\Bigl|\dfrac{d\theta}{d\eta}\Bigr|$.

3. By the change-of-variables formula for densities (@thm-derived-density-monotone), if $\theta$ has density $\pi(\theta)$ then $\eta$ has density $\pi(\varphi^{-1}(\eta))\,|d\theta/d\eta|$. With $\pi\propto\sqrt I$ this is $\sqrt{I(\theta)}\,|d\theta/d\eta|=\sqrt{\tilde I(\eta)}$, by step 2. (For an improper prior the same computation applies to the unnormalised function.)

:::

::: {#def-bayesian-confidence-region .definition name="Bayesian confidence region" related="def-probability-interval"}

For $\alpha\in(0,1)$, a *Bayesian confidence region* (credible region) of level $1-\alpha$ is a set $R$, depending on the data, with
$$\Pr\bigl(\theta\in R\mid X_1,\dots,X_n\bigr)=1-\alpha$$
under the posterior. It depends on the prior. It is a different object from a confidence interval (@def-confidence-interval): there the probability is over repeated samples with $\theta$ fixed, here it is over $\theta$ with the sample fixed.

:::

The posterior can also be used purely as a device for constructing estimators, judged afterwards by frequentist criteria; the prior is then a tuning choice, not a belief.

::: {#def-bayes-estimator .definition name="Bayes estimator" related="def-map-lms-estimates"}

For a prior $\pi$ (proper or improper with a proper posterior), the *Bayes estimator* is the posterior mean

$$
\hat\theta^{(\pi)}=\int_\Theta\theta\,\pi(\theta\mid X_1,\dots,X_n)\,d\theta .
$$

It minimises the posterior expected squared error (it is the LMS estimate of @def-map-lms-estimates).

:::

::: {#exm-bayes-estimator-bernoulli .example name="Bayes estimators for a proportion"}

With prior $\operatorname{Beta}(a,a)$ and $S$ successes in $n$ trials, the posterior is $\operatorname{Beta}(a+S,a+n-S)$ (@thm-beta-binomial-update), so
$$\hat p^{(\pi)}=\frac{a+S}{2a+n}=\frac{a/n+\bar X_n}{2a/n+1}.$$
For $S=14$ in $n=20$ trials: the MLE is $0.700$; the uniform prior ($a=1$) gives $15/22\approx0.682$; the Jeffreys prior ($a=1/2$) gives $14.5/21\approx0.690$, with equal-tailed $95\%$ credible interval $[0.483,\,0.864]$ from $\operatorname{Beta}(14.5,6.5)$. The plug-in confidence interval of @prp-three-asymptotic-intervals is $[0.499,\,0.901]$, of similar length but not the same.

As $n\to\infty$ with $a$ fixed, $\hat p^{(\pi)}-\bar X_n=\dfrac{a(1-2\bar X_n)}{2a+n}=O(1/n)$, so $\sqrt n(\hat p^{(\pi)}-\bar X_n)\to0$ and, by Slutsky's theorem, $\hat p^{(\pi)}$ is consistent and asymptotically normal with the same asymptotic variance $p(1-p)$ as the MLE, whatever $a$ is.

:::

::: {#rmk-bernstein-von-mises .remark name="The prior washes out"}

The last observation is general. For a smooth model satisfying the conditions of @thm-mle-asymptotic-normality and any prior with a continuous positive density near $\theta^*$, the posterior is asymptotically $N\bigl(\hat\theta_n,\ I(\theta^*)^{-1}/n\bigr)$ (the *Bernstein–von Mises theorem*, not proved here). Consequently Bayes estimators are consistent and asymptotically normal with the MLE's asymptotic variance, and Bayesian credible intervals are asymptotically confidence intervals of the same level. With little data, the prior matters; with much data, it does not.

:::
