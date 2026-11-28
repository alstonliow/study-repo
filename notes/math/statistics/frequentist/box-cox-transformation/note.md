---
title: "Box–Cox and Variance-Stabilising Transformations"
sources: [camii-sm-11, camii-sm-17]
requires: [math/statistics/frequentist/regression-inference, math/statistics/inference/slutsky-and-delta-method]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Sections 4.1.1 (Box-Cox transformation) and 4.8.2 (variance stabilising transform), in our own wording. The numerical check for the Poisson case is our own. -->

When the response is positive and skewed, one cheap remedy is to model a transformation of it with the ordinary normal linear model. Generalised linear models (@sec-ai-machine-learning-generalized-linear-models) are the more flexible alternative, because they model the mean of $Y$ on its own scale.

::: {#def-box-cox .definition name="Box–Cox transformation"}

For a positive response $Y$ and a parameter $\lambda\in\mathbb R$, the *Box–Cox transformation* is
$$Y^{(\lambda)}=\begin{cases}(Y^\lambda-1)/\lambda,&\lambda\ne0,\\ \log Y,&\lambda=0.\end{cases}$$
One then fits the normal linear model $Y_i^{(\lambda)}=X_i^{\mathsf T}\beta+\varepsilon_i$. The index $\lambda$ can be chosen by maximum likelihood jointly with $\beta$, or by looking at a normal quantile plot of the residuals.

:::

The case $\lambda=0$ is the limit of the first line, since $(y^\lambda-1)/\lambda\to\log y$ as $\lambda\to0$. A single parameter is asked to achieve three things at once: normal noise, linearity in the regressors, and constant variance. In practice the three goals often cannot all be met.

::: {#prp-variance-stabilising .proposition name="Variance-stabilising transformation"}

Let $Y$ have mean $\mu$ and variance $v(\mu)$. If $g'(\mu)=1/\sqrt{v(\mu)}$, then $\operatorname{Var}(g(Y))\approx1$ for $\mu$ large enough that the delta method applies. For a Poisson response $v(\mu)=\mu$ and $g(y)=2\sqrt y$.

:::

::: {.proof}

1. By the delta method (@thm-delta-method), $\operatorname{Var}(g(Y))\approx g'(\mu)^2\operatorname{Var}(Y)=g'(\mu)^2v(\mu)$.

2. This equals $1$ exactly when $g'(\mu)=v(\mu)^{-1/2}$.

3. For $v(\mu)=\mu$, $g'(\mu)=\mu^{-1/2}$, which integrates to $g(\mu)=2\sqrt\mu$.

:::

The approximation is accurate only for moderately large means: for $Y\sim\mathrm{Poisson}(20)$ the exact variance of $2\sqrt Y$ is $1.02$, but for mean $5$ it is $1.14$.

Fitting $E[2\sqrt Y\mid X]=X^{\mathsf T}\beta$ models the mean of the transformed response, which is a different model from the square-root *link* $E[Y\mid X]=(X^{\mathsf T}\beta)^2$ in a Poisson GLM. The drawback of transforming is that the transformed scale is rarely the scale of interest.
