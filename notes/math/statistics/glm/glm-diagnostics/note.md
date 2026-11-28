---
title: "Diagnostics and Model Selection for GLMs"
sources: [camii-sm-15]
requires: [math/statistics/glm/glm-canonical-form, math/statistics/inference/deviance, math/statistics/frequentist/model-selection-criteria]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 4.6, in our own wording. The key identity (Pearson residuals as least squares residuals) is written out in steps; the variance statement is the approximation of the source and is not proved. The Poisson example is our own and checked by computation (an IRLS fit). -->

Iteratively reweighted least squares (@prp-irls) shows that the final step of fitting a GLM is a weighted linear regression. This lets the diagnostics of @sec-math-statistics-frequentist-leverage-and-influence be carried over.

Let $\hat\mu_i,\hat W_i$ denote the fitted mean and weight at the MLE, with $W_i=w_i/\{\phi V(\mu_i)g'(\mu_i)^2\}$ as in @thm-glm-score-information, and let $\hat Z_i=X_i^{\mathsf T}\hat\beta+g'(\hat\mu_i)(Y_i-\hat\mu_i)$ be the *adjusted response* of the last IRLS step.

::: {#def-adjusted-hat-matrix .definition name="Adjusted hat matrix and leverage"}

The *adjusted hat matrix* of the fit is
$$H=\hat W^{1/2}\mathbb X(\mathbb X^{\mathsf T}\hat W\mathbb X)^{-1}\mathbb X^{\mathsf T}\hat W^{1/2},$$
the orthogonal projection onto the column space of $\hat W^{1/2}\mathbb X$ (the hat matrix of the weighted regression of $\hat Z$ on $\mathbb X$). The *leverage* of observation $i$ is $H_{ii}$; the $H_{ii}$ sum to $p$.

:::

::: {#prp-pearson-residual-wls .proposition name="Pearson residuals are weighted least squares residuals"}

The Pearson residual $R_{P,i}=\dfrac{Y_i-\hat\mu_i}{\sqrt{\hat\phi V(\hat\mu_i)/w_i}}$ satisfies
$$R_P=(I-H)\,\hat\phi^{-1/2}\hat W^{1/2}\hat Z\quad(\text{with }\hat\phi\text{ absorbed in }\hat W\text{ if one prefers}).$$

:::

::: {.proof}

1. At the maximum likelihood estimate $\hat\beta$ is the weighted least squares fit of $\hat Z$ on $\mathbb X$ with weights $\hat W$ (@prp-irls), so $\hat W^{1/2}(\hat Z-\mathbb X\hat\beta)=(I-H)\hat W^{1/2}\hat Z$.

2. By definition $\hat Z-\mathbb X\hat\beta=g'(\hat\mu)(Y-\hat\mu)$ componentwise, and $\hat W_i^{1/2}g'(\hat\mu_i)=\sqrt{w_i/\{\phi V(\hat\mu_i)\}}$, so the $i$th component of the left side is $(Y_i-\hat\mu_i)\sqrt{w_i/(\phi V(\hat\mu_i))}=R_{P,i}$.

:::

So $\hat W^{1/2}\hat Z$, $\hat W^{1/2}\hat\eta$ and $R_P$ behave like the response, fitted values and residuals of a linear model, and approximately $\operatorname{Var}(Y-\hat\mu)\approx\phi\hat V^{1/2}(I-H)\hat V^{1/2}$ with $\hat V=\operatorname{diag}(V(\hat\mu_i)/w_i)$: as for least squares, residuals at high-leverage points are shrunk. This motivates the following definitions.

::: {#def-glm-residuals .definition name="GLM residuals and Cook's distance"}

With $\hat\phi$ the dispersion estimate (equal to $\phi$ when known) and $D(y,\mu)$ the deviance of @def-deviance:

1. Pearson residual $R_{P,i}=(Y_i-\hat\mu_i)/\sqrt{\hat\phi V(\hat\mu_i)/w_i}$.
2. Deviance residual $R_{D,i}=\operatorname{sign}(Y_i-\hat\mu_i)\sqrt{w_i\,D(Y_i,\hat\mu_i)/\hat\phi}$.
3. Standardised versions $\tilde R_{P,i}=R_{P,i}/\sqrt{1-H_{ii}}$ and $\tilde R_{D,i}=R_{D,i}/\sqrt{1-H_{ii}}$.
4. Cook's distance $D_i=\dfrac1p\dfrac{H_{ii}}{1-H_{ii}}\tilde R_{P,i}^2$, the analogue of @prp-cooks-distance-formula.

The deviance residual is usually closer to normal than the Pearson residual (@def-deviance-residual); the sum of the squared deviance residuals is the residual deviance.

:::

*Model selection.* Mallows' $C_p$ relies on squared error and is not available. Leave-one-out cross-validation uses the deviance in place of the squared error, $\mathrm{CV}=\sum_iD(Y_i,\hat\mu_{-i})$, with $\hat\mu_{-i}$ the fitted value of observation $i$ from the fit without it. AIC and BIC (@def-aic-bic) are applied unchanged to the GLM log-likelihood, with $\dim\Theta$ the number of regression coefficients (plus one for $\phi$ if estimated). Best subset, forward and backward stepwise selection (@def-subset-algorithms) and penalisation carry over by replacing the residual sum of squares with the deviance.

::: {#exm-glm-diagnostics-poisson .example name="Residuals of a Poisson regression"}

Fit $\log\mu_i=\beta_0+\beta_1x_i$ to $x=(0,1,2,3,4)$ and counts $y=(2,1,6,5,14)$. Fisher scoring gives $\hat\beta=(0.290,0.566)$ and

| $i$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $\hat\mu_i$ | 1.34 | 2.35 | 4.15 | 7.30 | 12.86 |
| $H_{ii}$ | 0.36 | 0.33 | 0.26 | 0.26 | 0.79 |
| $R_{P,i}$ | 0.57 | $-0.88$ | 0.91 | $-0.85$ | 0.32 |
| $R_{D,i}$ | 0.53 | $-1.00$ | 0.85 | $-0.90$ | 0.31 |
| $D_i$ | 0.145 | 0.284 | 0.192 | 0.173 | 0.941 |

The leverages sum to $p=2$. Observation 5 has the largest leverage, $0.79$, although its residuals are small: the fit is forced through it, and its Cook's distance is by far the largest. The fitted means sum to $28=\sum y_i$ (@cor-glm-fitted-sum), and the residual deviance is $2.92$, close to Pearson's $\chi^2=2.76$.

:::
