---
title: "Choosing Priors and Probability Intervals"
sources: [mit1805-16]
requires: [math/statistics/bayesian/conjugate-priors]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Class 16, in our own wording; proofs written out in steps. -->

A posterior depends on the prior. This note collects what can be said about choosing one, and how a posterior is summarised by an interval.

::: {#rmk-choosing-priors .remark name="Flat and informed priors"}

A *flat* prior gives every hypothesis the same weight; an *informed* prior uses earlier data or expert judgement. With little data the two can give very different posteriors; with much data the likelihood dominates and they agree. For example, after $80$ heads in $100$ tosses the flat prior $\operatorname{Beta}(1,1)$ gives the posterior $\operatorname{Beta}(81,21)$ with mean $0.794$, while the prior $\operatorname{Beta}(10,10)$, centred on a fair coin, gives $\operatorname{Beta}(90,30)$ with mean $0.75$ (@thm-beta-binomial-update). When the choice of prior matters, it is good practice to report the posterior for several reasonable priors.

:::

::: {#prp-zero-prior .proposition name="A zero prior stays zero"}

If $\Pr(H)=0$, then $\Pr(H\mid D)=0$ for all data $D$ with $\Pr(D)>0$. Likewise, a prior density that vanishes on an interval gives a posterior density that vanishes there.

:::

::: {.proof}

1. The Bayes numerator is $\Pr(D\mid H)\Pr(H)=0$.

2. The posterior is the Bayes numerator divided by $\Pr(D)>0$, so it is $0$. The density case is the same computation pointwise.

:::

So a prior should not rule out anything that is actually possible: no amount of data can bring it back. A prior that does is called *rigid*.

::: {#def-probability-interval .definition name="Probability (credible) interval" related="def-confidence-interval"}

Let $\theta$ have a (prior or posterior) distribution and let $0<p<1$. An interval $[a,b]$ with
$$\Pr(a\le\theta\le b)=p$$
is a *$p$-probability interval* (or *credible interval*) for $\theta$. If $q_s$ denotes the $s$-quantile of $\theta$ (@def-quantile), the *symmetric* $p$-probability interval is
$$\bigl[q_{(1-p)/2},\ q_{(1+p)/2}\bigr].$$

:::

Probability intervals are not unique; among all of them the shortest is the one whose endpoints have equal density, and it contains the region where the density is highest. Unlike a confidence interval, a probability interval makes a probability statement about $\theta$ itself.

::: {#exm-probability-intervals .example name="Two posteriors summarised"}

1. The posterior $N(3.2,0.8)$ of @exm-normal-normal-one-point has the symmetric $0.95$-probability interval $3.2\pm1.96\sqrt{0.8}\approx[1.45,\ 4.95]$.

2. The posterior $\operatorname{Beta}(9,3)$ of @exm-beta-coin has the symmetric $0.9$-probability interval $[q_{0.05},q_{0.95}]\approx[0.53,\ 0.92]$ (quantiles computed numerically).

:::

::: {#exm-prior-from-quantiles .example name="A prior from a belief about quantiles"}

Someone believes a coin's bias $\theta$ is equally likely to be above or below $0.5$, and that it lies in $[0.4,0.6]$ with probability $\frac12$. A symmetric prior $\operatorname{Beta}(a,a)$ has median $0.5$; numerically, $\Pr(0.4\le\theta\le0.6)$ is $0.467$ for $a=5$, $0.507$ for $a=6$ and $0.542$ for $a=7$, so $\operatorname{Beta}(6,6)$ matches the stated belief well. Choosing a prior by matching a few quantiles is a simple way to turn a judgement into a distribution.

:::
