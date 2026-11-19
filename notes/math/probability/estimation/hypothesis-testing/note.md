---
title: "Hypothesis Testing"
sources: [eecs126-9, eecs126hw-12, eecs126d-11]
requires: [math/probability/discrete/bayes-theorem, math/probability/continuous/normal-distribution]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Hypothesis Testing", Homework 12 and Discussion 11, in our own wording; proofs written out in steps. -->

We observe $Y$ and must decide which of two hypotheses produced it: $X=0$ ($H_0$, "no signal") or $X=1$ ($H_1$, "signal"). Under $H_x$, $Y$ has PMF or density $f(y\mid x)$.

::: {#def-map-mle .definition name="MAP and ML decisions"}

The *maximum a posteriori* (MAP) and *maximum likelihood* (ML) rules decide
$$\hat X_{\mathrm{MAP}}(y)=\arg\max_x\Pr(X=x)f(y\mid x),\qquad\hat X_{\mathrm{ML}}(y)=\arg\max_xf(y\mid x).$$

:::

::: {#thm-map-minimises-error .theorem name="MAP minimises the probability of error"}

When $X$ has a prior distribution, among all decision rules $g$ the MAP rule minimises $\Pr(g(Y)\ne X)$. ML is MAP for a uniform prior.

:::

::: {.proof}

1. Conditioning on $Y=y$, $\Pr(g(Y)=X\mid Y=y)=\Pr(X=g(y)\mid Y=y)$.

2. By Bayes' rule (@thm-bayes-theorem) $\Pr(X=x\mid Y=y)\propto\Pr(X=x)f(y\mid x)$, so for each $y$ the MAP choice maximises the conditional probability of being right.

3. Averaging over $Y$, MAP maximises $\Pr(g(Y)=X)$.

:::

Often there is no sensible prior, and the two errors have different costs (a missed alarm versus a false alarm). Then we fix the false-alarm probability and maximise the detection probability.

::: {#def-neyman-pearson-problem .definition name="Errors, likelihood ratio"}

For a randomised decision rule $\hat X$, the *probability of false alarm* is $\mathrm{PFA}=\Pr(\hat X=1\mid X=0)$ and the *probability of correct detection* is $\mathrm{PCD}=\Pr(\hat X=1\mid X=1)$. The *likelihood ratio* is $L(y)=f(y\mid1)/f(y\mid0)$.

:::

::: {#thm-neyman-pearson .theorem name="Neyman–Pearson lemma"}

Fix $\beta\in(0,1)$. Among all rules with $\mathrm{PFA}\le\beta$, $\mathrm{PCD}$ is maximised by the *likelihood ratio test*
$$\hat X=\begin{cases}1&L(Y)>\lambda,\\1\text{ with probability }\gamma&L(Y)=\lambda,\\0&L(Y)<\lambda,\end{cases}$$
with the threshold $\lambda\ge0$ and $\gamma\in[0,1]$ chosen so that $\mathrm{PFA}=\beta$.

:::

::: {.proof}

1. Write $\phi(y)\in[0,1]$ for the probability that the test decides $1$ on $y$, and $\psi(y)$ for that of any other rule with $\mathrm{PFA}\le\beta$. Then $\mathrm{PCD}=\int\phi f(\cdot\mid1)$ and $\mathrm{PFA}=\int\phi f(\cdot\mid0)$ (sums for PMFs).

2. Pointwise, $(\phi(y)-\psi(y))\bigl(f(y\mid1)-\lambda f(y\mid0)\bigr)\ge0$: where $f(y\mid1)>\lambda f(y\mid0)$, $\phi=1\ge\psi$; where it is smaller, $\phi=0\le\psi$.

3. Integrating, $\mathrm{PCD}_\phi-\mathrm{PCD}_\psi\ge\lambda(\mathrm{PFA}_\phi-\mathrm{PFA}_\psi)=\lambda(\beta-\mathrm{PFA}_\psi)\ge0$.

:::

The randomisation $\gamma$ is only needed when $L(Y)$ has an atom at the threshold (discrete observations). When $L$ is increasing in $y$, the test is simply "decide $1$ when $y$ exceeds a threshold".

::: {#exm-neyman-pearson-gaussian .example name="Gaussian mean"}

Under $H_0$, $Y\sim N(0,1)$; under $H_1$, $Y\sim N(1,1)$. Then $L(y)=e^{y-1/2}$ is increasing, so the test decides $1$ when $Y>t$. For $\mathrm{PFA}=0.05$, $t\approx1.645$, and $\mathrm{PCD}=\Pr(N(1,1)>1.645)\approx0.26$. With a uniform prior, MAP decides $1$ when $L(y)>1$, that is $y>\tfrac12$, with error probability $\Phi(-\tfrac12)\approx0.31$.

:::

::: {#rmk-hypothesis-testing-roc .remark name="The ROC curve"}

Plotting the best $\mathrm{PCD}$ against $\mathrm{PFA}=\beta$ for all $\beta$ gives the *receiver operating characteristic*. It is concave and increasing, from $(0,0)$ to $(1,1)$; the further it bends towards $(0,1)$, the easier the two hypotheses are to tell apart.

:::
