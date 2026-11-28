::: {.problem #prob-camib-sts-3-q8 origin="external" source="camib-sts-3-q8"}
Consider the linear model $Y=X\beta+\varepsilon$ where $E\varepsilon=0$ and $\mathrm{Cov}(\varepsilon)=\sigma^2\Sigma$, for some unknown parameter $\sigma^2$ and known positive definite matrix $\Sigma$. Derive the form of the Generalised Least Squares estimator $\tilde\beta_{\mathrm{GLS}}$, defined by
$$\tilde\beta_{\mathrm{GLS}}=\operatorname*{argmin}_\beta\,(Y-X\beta)^{\mathsf T}\Sigma^{-1}(Y-X\beta).$$
State and prove a version of the Gauss–Markov theorem for $\tilde\beta_{\mathrm{GLS}}$.
:::

::: {.problem #prob-camii-sms-1-q7 origin="external" source="camii-sms-1-q7"}
Let $\Sigma$ be a known $n\times n$ positive definite matrix. Consider the following linear model
$$Y=X\beta+\varepsilon,\qquad\varepsilon\mid X\sim N(0,\sigma^2\Sigma),$$
where $\beta$ and $\sigma^2$ are unknown. Let $\hat\beta_\Sigma$ denote the maximum likelihood estimator of $\beta$.

(a) Write down the optimisation problem solved by $\hat\beta_\Sigma$ and an expression for $\hat\beta_\Sigma$, assuming $X^{\mathsf T}\Sigma^{-1}X$ is invertible.

(b) Show that $\hat\beta_\Sigma$ is the best linear unbiased estimator (BLUE) in this model.

(c) How does the optimisation problem and solution look like when $\Sigma$ is diagonal? Read the R documentation for `lm` and find out how you can solve this problem numerically.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::
