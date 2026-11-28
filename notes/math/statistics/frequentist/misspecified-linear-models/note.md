---
title: "Heteroscedasticity, Misspecification and Omitted Variables"
sources: [camii-sm-3, camii-sms-1-q11]
requires: [math/statistics/frequentist/multiple-linear-regression, math/statistics/inference/slutsky-and-delta-method]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 2.4 (sandwich variance, the linear working model, omitted-variable bias), in our own wording; proofs written out in steps. Generalised least squares is already in multiple-linear-regression and gauss-markov and is not repeated. The numerical example is our own and checked by computation. -->

The exact theory of the Gaussian linear model needs three assumptions: the conditional mean is linear, the noise is independent of the covariates, and the noise is normal. This note drops them one at a time and asks what ordinary least squares still estimates, and how its variance must then be estimated.

::: {#thm-sandwich-variance .theorem name="Heteroscedasticity-robust (sandwich) variance" related="thm-gauss-markov"}

Let $(X_i,\varepsilon_i)$, $i=1,\dots,n$, be iid with $Y_i=X_i^{\mathsf T}\beta+\varepsilon_i$, $E[\varepsilon_i\mid X_i]=0$ and $\operatorname{Var}(\varepsilon_i\mid X_i)=\sigma^2(X_i)$ (possibly non-constant: *heteroscedastic* noise). Put $\Sigma_X=E[X_iX_i^{\mathsf T}]$ (invertible) and $\Omega=E[\sigma^2(X_i)X_iX_i^{\mathsf T}]$ (finite). Then the least squares estimator satisfies
$$\sqrt n(\hat\beta-\beta)\xrightarrow{d}N\bigl(0,\ \Sigma_X^{-1}\Omega\,\Sigma_X^{-1}\bigr).$$
With residuals $e_i=Y_i-X_i^{\mathsf T}\hat\beta$ and $\hat\Sigma_X=\frac1n\sum_iX_iX_i^{\mathsf T}$, $\hat\Omega=\frac1n\sum_ie_i^2X_iX_i^{\mathsf T}$, the matrix $\hat\Sigma_X^{-1}\hat\Omega\hat\Sigma_X^{-1}$ is a consistent estimator of the limiting covariance, so the sandwich form gives asymptotic confidence intervals for the coefficients without assuming constant variance.

:::

::: {.proof}

1. Since $Y=\mathbb X\beta+\boldsymbol\varepsilon$, we have $\sqrt n(\hat\beta-\beta)=\sqrt n(\mathbb X^{\mathsf T}\mathbb X)^{-1}\mathbb X^{\mathsf T}\boldsymbol\varepsilon=\bigl(\tfrac1n\sum_iX_iX_i^{\mathsf T}\bigr)^{-1}\bigl(\tfrac1{\sqrt n}\sum_iX_i\varepsilon_i\bigr)$.

2. By the weak law of large numbers, $\frac1n\sum_iX_iX_i^{\mathsf T}\to\Sigma_X$ in probability.

3. The vectors $X_i\varepsilon_i$ are iid with mean $E[X_iE[\varepsilon_i\mid X_i]]=0$ and covariance $E[\varepsilon_i^2X_iX_i^{\mathsf T}]=E[\sigma^2(X_i)X_iX_i^{\mathsf T}]=\Omega$. By the multivariate central limit theorem (@thm-multivariate-clt), $\frac1{\sqrt n}\sum_iX_i\varepsilon_i\xrightarrow{d}N(0,\Omega)$.

4. Slutsky's theorem (@thm-slutsky) combines steps 2 and 3: the product converges in distribution to $\Sigma_X^{-1}N(0,\Omega)=N(0,\Sigma_X^{-1}\Omega\Sigma_X^{-1})$.

5. For the estimator, $e_i=\varepsilon_i-X_i^{\mathsf T}(\hat\beta-\beta)$ with $\hat\beta-\beta\to0$ in probability; replacing $\varepsilon_i$ by $e_i$ changes $\hat\Omega$ by a term that vanishes in probability under moment conditions, so $\hat\Omega\to\Omega$ by the law of large numbers. Continuity of matrix inversion finishes the proof.

:::

When the noise is homoscedastic, $\Omega=\sigma^2\Sigma_X$ and the limit reduces to $N(0,\sigma^2\Sigma_X^{-1})$, which is the exact covariance $\sigma^2(\mathbb X^{\mathsf T}\mathbb X)^{-1}$ of @thm-gaussian-linear-model rescaled by $n$. The sandwich form $\Sigma_X^{-1}\Omega\Sigma_X^{-1}$ is typical of maximum likelihood under a misspecified model.

Next the linear form itself is questioned. A *linear working model* is the fit $\mu=\mathbb X\beta$ when the truth may be nonlinear.

::: {#prp-best-linear-projection .proposition name="What least squares estimates when the model is wrong" related="prp-regression-characterisation"}

Let $(X_i,\varepsilon_i)$ be iid with $Y_i=g(X_i)+\varepsilon_i$, where $\varepsilon_i$ is independent of $X_i$, $E[\varepsilon_i]=0$, and $E[g(X_i)^2]<\infty$, $\Sigma_X$ invertible. Then $\hat\beta\to\beta_{\mathrm{OLS}}$ in probability, where
$$\beta_{\mathrm{OLS}}=\operatorname*{argmin}_{\beta}E\bigl[(g(X_i)-X_i^{\mathsf T}\beta)^2\bigr]=\Sigma_X^{-1}E[X_ig(X_i)].$$
So $X^{\mathsf T}\beta_{\mathrm{OLS}}$ is the population least squares projection of $g(X)$ onto the linear functions of $X$. It depends on the distribution of $X_i$, not only on $g$.

:::

::: {.proof}

1. $\hat\beta=\bigl(\frac1n\sum X_iX_i^{\mathsf T}\bigr)^{-1}\frac1n\sum X_iY_i\to\Sigma_X^{-1}E[X_iY_i]$ by the law of large numbers and continuity of inversion.

2. $E[X_iY_i]=E[X_ig(X_i)]+E[X_i]E[\varepsilon_i]=E[X_ig(X_i)]$ by independence and $E[\varepsilon_i]=0$.

3. Expanding the square, $E[(Y_i-X_i^{\mathsf T}\beta)^2]=E[(g(X_i)-X_i^{\mathsf T}\beta)^2]+2E[(g(X_i)-X_i^{\mathsf T}\beta)\varepsilon_i]+E[\varepsilon_i^2]$. The cross term is $0$ by independence and the last term does not depend on $\beta$, so the minimiser is the same as that of $E[(g(X_i)-X_i^{\mathsf T}\beta)^2]$. Setting its gradient to $0$ gives $\Sigma_X\beta=E[X_ig(X_i)]$.

:::

::: {#exm-misspecified-quadratic .example name="A quadratic truth and a linear fit"}

Let $g(x)=x^2+x$ and $X\sim N(m,1)$. With an intercept, the population regression slope is $\operatorname{Cov}(X,g(X))/\operatorname{Var}(X)$. For the normal law $\operatorname{Cov}(X,X^2)=E[X^3]-E[X]E[X^2]=(m^3+3m)-m(m^2+1)=2m$ and $\operatorname{Cov}(X,X)=1$, so the slope is $2m+1$.

1. For $m=-1$ the slope is $-1$: the line slopes down although $g$ is increasing on the right half-line.

2. For $m=1$ the slope is $3$.

So the "true" coefficient of the working model changes sign with where the covariates happen to lie (@fig-misspecified-linear-models-1).

:::

::: {#fig-misspecified-linear-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.1cm,y=0.22cm]
\draw[->, muted] (-4.2,0) -- (4.2,0) node[lab, right] {$x$};
\draw[->, muted] (0,-1) -- (0,17);
\draw[emph, primary, domain=-3.2:3.2, samples=60] plot (\x,{\x*\x+\x});
\draw[hl, domain=-3:0.6] plot (\x,{-1*\x+0});
\draw[hl, domain=0.4:3.2] plot (\x,{3*\x});
\node[lab] at (-2.6,10.5) {slope $-1$, $m=-1$};
\node[lab] at (2.4,16) {slope $3$, $m=1$};
\node[lab, below] at (1.2,-1.2) {$g(x)=x^2+x$};
\end{tikzpicture}
\end{center}
```

The same curve $g(x)=x^2+x$ is fitted by a line twice: when the covariates are centred at $-1$ the best line slopes down, when they are centred at $1$ it slopes up. Both best lines pass through the origin: $E[g(X)]-(2m+1)m=0$ for $m=\pm1$.

:::

The estimand also depends on the loss: the least absolute deviation estimator $\operatorname{argmin}\sum|Y_i-X_i^{\mathsf T}\beta|$ generally converges to a different limit than $\beta_{\mathrm{OLS}}$ unless $g$ is linear.

A different misspecification is leaving out a covariate.

::: {#prp-omitted-variable-bias .proposition name="Omitted-variable bias" related="prp-best-linear-projection"}

Let $Y=X^{\mathsf T}\beta^*+Z^{\mathsf T}\gamma^*+\varepsilon^*$ with $E[\varepsilon^*\mid X,Z]=0$, and let $\Delta=E[XX^{\mathsf T}]^{-1}E[XZ^{\mathsf T}]$ be the matrix of population coefficients of the regression of $Z$ on $X$. Regressing $Y$ on $X$ alone estimates
$$\beta=\beta^*+\Delta\gamma^*.$$
In particular $\beta=\beta^*$ if $\gamma^*=0$, or if $\Delta=0$, which holds when $E[XZ^{\mathsf T}]=0$ (for instance independent covariates, one of them centred).

:::

::: {.proof}

1. The population coefficient of the short regression is $\beta=E[XX^{\mathsf T}]^{-1}E[XY]$.

2. Substituting $Y$, $E[XY]=E[XX^{\mathsf T}]\beta^*+E[XZ^{\mathsf T}]\gamma^*+E[X\varepsilon^*]$ and $E[X\varepsilon^*]=0$.

3. Multiplying by $E[XX^{\mathsf T}]^{-1}$ gives $\beta=\beta^*+\Delta\gamma^*$.

:::

An extreme form of this bias is *Simpson's paradox* (@exm-simpsons-paradox): a covariate that is associated both with the response and with the retained regressor reverses the sign of the retained coefficient. A regression coefficient measures conditional association and need not be a causal effect.
