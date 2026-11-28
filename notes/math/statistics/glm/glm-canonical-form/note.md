---
title: "Canonical-Link GLMs and the Normal Equations"
sources: [camii-sm-11, camii-sm-12, camii-sm-14, camii-sms-3-q11, camii-sms-4-q2, camii-sms-4-q3, camii-sms-4-q8]
requires: [ai/machine-learning/generalized-linear-models, math/statistics/inference/exponential-family-inference]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Sections 4.1.2, 4.2, 4.3.1-4.3.2 and 4.5, and Example Sheets 3 (question 11) and 4 (questions 2, 3), in our own wording; proofs written out in steps. The definition of a GLM, link functions, the score and information for an arbitrary link, Fisher scoring and IRLS are already in ai/machine-learning/generalized-linear-models (from MIT 18.650) and are used here, not repeated. This note adds the exponential-family view of the canonical GLM, the normal equations and their consequences, and the role of the dispersion parameter. -->

A GLM has three components: an exponential (dispersion) family for $Y_i\mid X_i$, a linear predictor $\eta_i=X_i^{\mathsf T}\beta$, and a strictly increasing link $g$ with $g(\mu_i)=\eta_i$ (@def-link-function). The simplest case is the *canonical* one, where the natural parameter itself is the linear predictor: $\theta_i=X_i^{\mathsf T}\beta$ and the link $g=(b')^{-1}$ is the inverse of the mean function. With dispersion $\phi=1$ and the notation of @def-exponential-family ($a$ for the log partition function) it reads
$$Y_i\mid X_i\sim p(y;\eta_i)=b(y)e^{\eta_iy-a(\eta_i)},\qquad\eta_i=X_i^{\mathsf T}\beta,\qquad\mu_i=a'(\eta_i)=\mu(X_i^{\mathsf T}\beta).$$
The covariates are treated as fixed, and the $Y_i$ independent.

::: {#thm-canonical-glm-exponential-family .theorem name="The canonical GLM is a $p$-parameter exponential family"}

The joint density of $Y=(Y_1,\dots,Y_n)$ is
$$\prod_ib(y_i)\,\exp\Bigl\{\beta^{\mathsf T}\mathbb X^{\mathsf T}y-\sum_ia(X_i^{\mathsf T}\beta)\Bigr\}.$$
So the natural parameter is $\beta$, the sufficient statistic is $Z=\mathbb X^{\mathsf T}Y$ and the log partition function is $\psi(\beta)=\sum_ia(X_i^{\mathsf T}\beta)$. Consequently
$$E_\beta Z=\nabla\psi(\beta)=\mathbb X^{\mathsf T}\mu(\beta),\qquad\operatorname{Cov}_\beta Z=\nabla^2\psi(\beta)=\mathbb X^{\mathsf T}V(\beta)\mathbb X,$$
where $\mu(\beta)=(\mu_i)_i$ and $V(\beta)=\operatorname{diag}(a''(X_i^{\mathsf T}\beta))=\operatorname{diag}(\operatorname{Var}Y_i)$.

:::

::: {.proof}

1. Multiply the $n$ densities and use $\sum_i\eta_iy_i=\sum_i(X_i^{\mathsf T}\beta)y_i=\beta^{\mathsf T}\mathbb X^{\mathsf T}y$.

2. Differentiate $\psi$ by the chain rule: $\partial\psi/\partial\beta=\sum_ia'(X_i^{\mathsf T}\beta)X_i=\mathbb X^{\mathsf T}\mu(\beta)$ and $\nabla^2\psi=\sum_ia''(X_i^{\mathsf T}\beta)X_iX_i^{\mathsf T}=\mathbb X^{\mathsf T}V\mathbb X$.

3. For an exponential family the first two derivatives of the log partition function in the natural parameter are the mean and covariance of the sufficient statistic (@prp-exponential-family-moments).

:::

::: {#thm-glm-normal-equations .theorem name="Normal equations and information of a canonical GLM" related="thm-glm-score-information"}

The log-likelihood is $\ell(\beta)=\beta^{\mathsf T}\mathbb X^{\mathsf T}Y-\sum_ia(X_i^{\mathsf T}\beta)+\text{const}$, strictly concave if $\operatorname{rank}\mathbb X=p$. Its score is $U(\beta)=\mathbb X^{\mathsf T}\{Y-\mu(\beta)\}$, so the MLE satisfies the *normal equations*
$$\mathbb X^{\mathsf T}\{Y-\mu(\hat\beta)\}=0 .$$
The negative Hessian is non-random and equals the Fisher information $I(\beta)=\mathbb X^{\mathsf T}V(\beta)\mathbb X$, so Newton–Raphson and Fisher scoring coincide for the canonical link, and under regularity conditions $\hat\beta\approx N\bigl(\beta,I(\beta)^{-1}\bigr)$.

:::

::: {.proof}

1. Differentiating $\ell$ gives $U=\mathbb X^{\mathsf T}Y-\mathbb X^{\mathsf T}\mu(\beta)$, and $\nabla^2\ell=-\nabla^2\psi=-\mathbb X^{\mathsf T}V\mathbb X$ does not involve $Y$, hence equals its expectation.

2. $V$ has positive diagonal and $\mathbb X$ has full column rank, so $\mathbb X^{\mathsf T}V\mathbb X$ is positive definite and $\ell$ is strictly concave: the root of $U$ is the unique maximiser.

3. Asymptotic normality is the general maximum likelihood result with the information of step 1.

:::

For the normal family with identity link $a(\eta)=\eta^2/2$, $\mu(\beta)=\mathbb X\beta$, and the normal equations become $\mathbb X^{\mathsf T}(Y-\mathbb X\hat\beta)=0$ of least squares. In general $\hat\beta$ is the projection of $Y$ onto the $p$-dimensional curved manifold $\{\mu(\beta):\beta\in\mathbb R^p\}\subset\mathbb R^n$ in the sense that the residual $Y-\hat\mu$ is orthogonal to the columns of $\mathbb X$.

::: {#cor-glm-fitted-sum .corollary name="Fitted means preserve the total"}

If the canonical-link GLM has an intercept (a column of ones in $\mathbb X$), then $\sum_i\hat\mu_i=\sum_iY_i$.

:::

::: {.proof}

The normal equation of the constant column reads $\sum_i(Y_i-\hat\mu_i)=0$.

:::

::: {#exm-normal-one-step .example name="Fisher scoring converges in one step for the normal model" related="prp-glm-newton-step"}

For $Y_i\sim N(X_i^{\mathsf T}\beta,\sigma^2)$ the log-likelihood is quadratic in $\beta$ with Hessian $-\mathbb X^{\mathsf T}\mathbb X/\sigma^2$ independent of $\beta$. From any start $\beta^{(0)}$ one scoring step gives $\beta^{(0)}+(\mathbb X^{\mathsf T}\mathbb X)^{-1}\mathbb X^{\mathsf T}(Y-\mathbb X\beta^{(0)})=(\mathbb X^{\mathsf T}\mathbb X)^{-1}\mathbb X^{\mathsf T}Y$, the least squares estimate. It is the exact quadratic shape of the log-likelihood that makes one step enough.

:::

Now allow a general link and a dispersion parameter, as in @thm-glm-score-information: $\operatorname{Var}(Y_i)=\phi\,V(\mu_i)/w_i$ with known weights $w_i$.

::: {#prp-glm-dispersion-estimation .proposition name="The dispersion parameter does not affect $\hat\beta$"}

1. The score for $\beta$ is $\phi^{-1}\sum_iw_i\dfrac{(Y_i-\mu_i)X_i}{V(\mu_i)g'(\mu_i)}$, so the MLE $\hat\beta$ solves $\sum_iw_i(Y_i-\hat\mu_i)X_i/\{V(\hat\mu_i)g'(\hat\mu_i)\}=0$ whatever $\phi$ is; for the canonical link with $w_i=1$ this is the normal equation above.
2. The Fisher information for $(\beta,\phi)$ is block diagonal, with $I_{\beta\beta}=\phi^{-1}\mathbb X^{\mathsf T}W\mathbb X$, $W_i=w_i/\{V(\mu_i)g'(\mu_i)^2\}$. So $\hat\beta\approx N\bigl(\beta,\ \phi(\mathbb X^{\mathsf T}W\mathbb X)^{-1}\bigr)$.
3. If $\phi$ is unknown it is estimated by $\hat\phi=\dfrac1{n-p}\sum_iw_i\dfrac{(Y_i-\hat\mu_i)^2}{V(\hat\mu_i)}$, motivated by $E(Y_i-\mu_i)^2=\phi V(\mu_i)/w_i$ (for known $\phi$, $\hat\phi=\phi$).

:::

::: {.proof}

1. The score is the one of @thm-glm-score-information divided by $\phi$, and the factor $\phi^{-1}$ does not change its roots.

2. The mixed second derivative is $\partial^2\ell/\partial\beta\,\partial\phi=-\phi^{-2}\times(\text{score numerator})$, which is linear in $Y_i-\mu_i$ and has expectation $0$. So the information is block diagonal; $I_{\beta\beta}$ is the expected $-\nabla^2_\beta\ell$, which is $\phi^{-1}\mathbb X^{\mathsf T}W\mathbb X$ by @thm-glm-score-information.

3. Statement 3 is a definition; it generalises $\hat\sigma^2=\|Y-\mathbb X\hat\beta\|^2/(n-p)$ of the normal linear model.

:::

To construct a confidence interval for $\beta_j$ one replaces $\beta,\phi$ in the variance by $\hat\beta,\hat\phi$, giving $\hat\beta_j\pm z_{\alpha/2}\sqrt{\hat\phi\,[(\mathbb X^{\mathsf T}\hat W\mathbb X)^{-1}]_{jj}}$; with moderate $n$ the normal quantile may be replaced by $t_{n-p}(\alpha/2)$, as in the normal linear model.
