---
title: "Poisson Regression"
sources: [camii-sm-17]
requires: [math/statistics/glm/glm-canonical-form, math/statistics/inference/deviance]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Sections 4.8.1 and 4.8.3, in our own wording; proofs written out in steps. The small numerical example is our own and checked by computation. The variance-stabilising transformation is in box-cox-transformation. -->

Count data $Y_i\in\{0,1,2,\dots\}$ are often modelled as Poisson. The rationale is the law of small numbers (@thm-poisson-as-a-limit-of): a total of many rare independent events is approximately Poisson. The Poisson law has $\operatorname{Var}Y=EY=\mu$ (@exm-natural-parametrisations); real counts are frequently overdispersed (@prp-clustered-binomial), which a dispersion parameter handles.

::: {#def-poisson-regression .definition name="Poisson regression"}

*Poisson regression* is the GLM with independent $Y_i\sim\mathrm{Poisson}(\mu_i)$ and the canonical *log link*,
$$\log\mu_i=X_i^{\mathsf T}\beta,\qquad\text{i.e.}\quad\mu_i=\prod_{j=1}^p\bigl(e^{\beta_j}\bigr)^{X_{ij}} .$$
Hence $e^{\beta_j}$ is the multiplicative change of the mean per unit increase of the $j$th regressor. The natural parameter is $\theta=\log\mu$ and the cumulant function is $a(\theta)=e^\theta$. Other links, such as the identity or the square root, are possible but not canonical.

:::

By @thm-glm-normal-equations the MLE solves $\mathbb X^{\mathsf T}\{Y-\exp(\mathbb X\hat\beta)\}=0$ (found by Fisher scoring), and with an intercept $\sum\hat\mu_i=\sum Y_i$ (@cor-glm-fitted-sum). The deviance (@exm-deviance-formulas) is
$$D^{(n)}(Y,\hat\mu)=2\sum_i\Bigl(Y_i\log\frac{Y_i}{\hat\mu_i}-Y_i+\hat\mu_i\Bigr),$$
with the convention $0\log0=0$.

::: {#prp-poisson-deviance-pearson .proposition name="Deviance and Pearson's statistic agree for large means"}

Let the model include an intercept and let $\delta_i=Y_i-\hat\mu_i$ satisfy $|\delta_i|\ll\hat\mu_i$. Then
$$D^{(n)}(Y,\hat\mu)\approx\sum_i\frac{(Y_i-\hat\mu_i)^2}{\hat\mu_i}=\chi^2_{\mathrm{Pearson}}=\sum_iR_{P,i}^2 .$$
If the model is correct and $\min_i\mu_i\to\infty$, this statistic is asymptotically $\chi^2_{n-p}$ (*small-dispersion asymptotics*; $n$ does not need to grow).

:::

::: {.proof}

1. By @cor-glm-fitted-sum, $\sum_i\delta_i=0$, so $D=2\sum_iY_i\log(Y_i/\hat\mu_i)$.

2. Write $Y_i=\hat\mu_i+\delta_i$: $D=2\sum_i(\hat\mu_i+\delta_i)\log(1+\delta_i/\hat\mu_i)$.

3. Use $\log(1+x)\approx x-x^2/2$: $(\hat\mu_i+\delta_i)\bigl(\delta_i/\hat\mu_i-\delta_i^2/(2\hat\mu_i^2)\bigr)\approx\delta_i+\delta_i^2/(2\hat\mu_i)$, up to terms of order $\delta_i^3/\hat\mu_i^2$.

4. Summing and using $\sum\delta_i=0$ gives $D\approx\sum_i\delta_i^2/\hat\mu_i$.

:::

::: {#exm-poisson-two-groups .example name="Two groups of counts"}

For the counts $(3,5,4)$ and $(9,7,8)$ with a group indicator (@exm-poisson-analysis-of-deviance), the fitted means are $4$ and $8$ and $e^{\hat\beta_1}=8/4=2$: the second group has twice the mean. The residual deviance is $0.756$ and Pearson's statistic $\sum(Y_i-\hat\mu_i)^2/\hat\mu_i=(1+1)/4\cdot1+(1+1)/8\cdot1=0.75$, close as the proposition predicts (here $\delta_i=\pm1$ against $\hat\mu_i\ge4$).

:::
