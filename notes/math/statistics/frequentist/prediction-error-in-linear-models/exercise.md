::: {.problem #prob-camii-sms-1-q8 origin="external" source="camii-sms-1-q8"}
Consider the model $Y=\mu+\varepsilon$ where $\mathbb E(\varepsilon)=0$ and $\operatorname{Var}(\varepsilon)=\sigma^2I$ and $\mu\in\mathbb R^n$ is a non-random vector. Suppose we have performed least squares of $Y$ on a fixed design matrix $X\in\mathbb R^{n\times p}$, so the fitted values are $\hat\mu=PY$. Show that if $Y^*=\mu+\varepsilon^*$ where $\varepsilon^*$ is an independent and identically distributed copy of $\varepsilon$, then
$$\frac1n\mathbb E(\|\hat\mu-Y^*\|^2)=\sigma^2+\frac1n\|(I-P)\mu\|^2+\frac{\sigma^2p}n.$$
Compare this to the bias-variance tradeoff in the lectures and identify the "bias$^2$" and "variance" terms.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::

::: {.problem #prob-camii-sms-2-q3 origin="external" source="camii-sms-2-q3"}
Suppose $Y\sim N(\mu,\sigma^2I)$ where $\mu\in\mathbb R^n$ is unknown. Consider any linear estimator of the form $\hat\mu=MY$ where $M=M(X)\in\mathbb R^{n\times n}$ can depend on $X$. Show that
$$C_M=\|Y-\hat\mu\|^2+2\sigma^2\cdot\operatorname{trace}(M)$$
is, conditional on $X$, an unbiased estimator of the mean squared prediction error
$$\mathbb E(\|Y^*-\hat\mu\|^2\mid X)$$
where $Y^*=\mu+\epsilon^*$, $\epsilon^*\sim N(0,\sigma^2I)$ is independent of $Y$. Explain why this reduces to Mallow's $C_p$ when $\hat\mu=X\hat\beta=PY$.
:::
