::: {.problem #prob-camib-sts-3-q11 origin="external" source="camib-sts-3-q11"}
In the standard linear model $Y=X\beta+\varepsilon$ with $\varepsilon\sim N_n(0,\sigma^2I)$ and MLE $\hat\beta$, determine the distribution of the quadratic form $(\hat\beta-\beta)^{\mathsf T}X^{\mathsf T}X(\hat\beta-\beta)$. (Hint: Consider $(X^{\mathsf T}X)^{1/2}(\hat\beta-\beta)$, where the square root is a matrix square root.) Use the $F$-distribution to find a $(1-\alpha)$-level confidence set for $\beta$, i.e. a random set $C(Y)$ such that $P_{\beta,\sigma^2}(\beta\in C(Y))=1-\alpha$ for all $\beta,\sigma^2$. What is the shape of this confidence set?

*Note (these notes):* The sheet writes the coverage event as $b\in C(Y)$; $\beta\in C(Y)$ is meant.
:::

::: {.problem #prob-camii-sms-1-q5 origin="external" source="camii-sms-1-q5"}
Let the cuboid $C$ be defined $C:=\prod_{j=1}^pC_j(\alpha/p)$, where
$$C_j(\alpha)=\Bigl[\hat\beta_j-\sqrt{\hat\sigma^2(X^{\mathsf T}X)^{-1}_{jj}}\,t_{n-p}(\alpha/2),\ \hat\beta_j+\sqrt{\hat\sigma^2(X^{\mathsf T}X)^{-1}_{jj}}\,t_{n-p}(\alpha/2)\Bigr].$$
Assuming the normal linear model, show that $\mathbb P(\beta\in C)\ge1-\alpha$.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::
