---
title: "The Poisson Trick for Multinomial Data"
sources: [camii-sm-17, camii-sms-4-q10]
requires: [math/statistics/glm/poisson-regression, math/probability/distributions/multinomial-distribution]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 4.8.4, in our own wording; proofs written out in steps. -->

The multinomial distribution is not a minimal exponential family and its counts are not independent. Writing it with a baseline category breaks the symmetry between categories (@exm-natural-parametrisations). The Poisson trick replaces it by independent Poisson counts.

::: {#thm-poisson-trick .theorem name="Poisson counts conditional on their total"}

Let $Y_1,\dots,Y_L$ be independent with $Y_l\sim\mathrm{Poisson}(\mu_l)$ and put $Y_+=\sum_lY_l$, $\mu_+=\sum_l\mu_l$, $\pi_l=\mu_l/\mu_+$. Then
$$Y_+\sim\mathrm{Poisson}(\mu_+)\quad\text{and}\quad(Y_1,\dots,Y_L)\mid Y_+\sim\mathrm{Multinomial}(Y_+;\pi_1,\dots,\pi_L).$$

:::

::: {.proof}

1. $Y_+\sim\mathrm{Poisson}(\mu_+)$ is the additivity of independent Poisson variables (@thm-sum-of-poissons).

2. For $y_1+\dots+y_L=m$, $P(Y=y\mid Y_+=m)=\dfrac{\prod_le^{-\mu_l}\mu_l^{y_l}/y_l!}{e^{-\mu_+}\mu_+^m/m!}=\dfrac{m!}{\prod_ly_l!}\prod_l\Bigl(\dfrac{\mu_l}{\mu_+}\Bigr)^{y_l}$, the multinomial probability.

:::

::: {#thm-poisson-trick-likelihood .theorem name="Fitting a multinomial model with a Poisson log-linear model"}

Let $Y_l\sim\mathrm{Poisson}(\mu_l)$ independently with $\log\mu_l=\alpha+X_l^{\mathsf T}\beta$ and an intercept $\alpha$ distinct from $\beta$. Then $\pi_l=e^{X_l^{\mathsf T}\beta}/\sum_ke^{X_k^{\mathsf T}\beta}$ does not depend on $\alpha$, and the Poisson likelihood factorises as
$$L_{\mathrm{P}}(\mu_+,\beta)=L_{\mathrm M}(\beta)\,f(Y_+;\mu_+),$$
with $L_{\mathrm M}(\beta)$ the multinomial likelihood for $(Y\mid Y_+)$ with probabilities $\pi_l(\beta)$. Hence the MLE $\hat\beta$ of the Poisson model also maximises the multinomial likelihood, $\hat\mu_+=Y_+$, the Fisher information is block diagonal in $(\mu_+,\beta)$, and the deviances of the two models coincide.

:::

::: {.proof}

1. $\mu_l=e^\alpha e^{X_l^{\mathsf T}\beta}$ and $\mu_+=e^\alpha\sum_ke^{X_k^{\mathsf T}\beta}$, so $\pi_l=\mu_l/\mu_+$ is free of $\alpha$.

2. The joint probability is $P(Y)=P(Y\mid Y_+)P(Y_+)$, which by @thm-poisson-trick is the stated factorisation. Given $\beta$, $\mu_+$ is a bijective function of $\alpha$, so $(\mu_+,\beta)$ is a reparametrisation of $(\alpha,\beta)$ in which the two factors have separate parameters.

3. Therefore the likelihood is maximised by maximising each factor: $f(Y_+;\mu_+)$ is maximal at $\hat\mu_+=Y_+$ and $L_{\mathrm M}$ at the multinomial MLE of $\beta$. The log-likelihood is a sum of the two parts, so the information matrix is block diagonal.

4. At $\hat\mu_+=Y_+$ the two fitted multinomial and Poisson means agree, $\hat\mu_l=Y_+\pi_l(\hat\beta)$, so the saturated and fitted models give the same deviance in both.

:::

::: {#exm-poisson-trick-logistic .example name="Two categories give logistic regression"}

For $L=2$ the conditional law of $Y_1$ given $Y_+$ is $\mathrm{Binomial}(Y_+,\pi_1)$ with $\log\frac{\pi_1}{1-\pi_1}=\log\mu_1-\log\mu_2=(X_1-X_2)^{\mathsf T}\beta$: the Poisson log-linear model with an intercept contains the logistic regression with covariate $X_1-X_2$.

:::
