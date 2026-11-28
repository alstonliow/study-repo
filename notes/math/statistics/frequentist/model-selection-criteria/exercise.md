::: {.problem #prob-camii-sms-2-q4 origin="external" source="camii-sms-2-q4"}
Show that the AIC in a normal linear model is
$$n\{1+\log(2\pi\hat\sigma^2_{\mathrm{MLE}})\}+2(p+1),$$
where $\hat\sigma^2_{\mathrm{MLE}}=\|(I-H)Y\|^2/n$ is the maximum likelihood estimator of $\sigma^2$. When the noise variance $\sigma^2$ is known, re-derive the AIC and show that it is equivalent to Mallow's $C_p$.

*Note (these notes):* Here $H$ is the hat matrix, called $P$ in the notation of the sheet. Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::
