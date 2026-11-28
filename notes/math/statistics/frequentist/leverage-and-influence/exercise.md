::: {.problem #prob-camii-sms-2-q5 origin="external" source="camii-sms-2-q5"}
In the normal linear model, show that $\operatorname{Var}(Y_i-X_i^{\mathsf T}\hat\beta\mid X)=\sigma^2(1-P_{ii})$. Hint: Write the residual $Y_i-X_i^{\mathsf T}\hat\beta$ as a linear transformation of $Y$.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::

::: {.problem #prob-camii-sms-2-q6 origin="external" source="camii-sms-2-q6"}
Suppose the design matrix $X$ consists of just a single variable and a column of 1's representing an intercept term (as the first column). Show that the leverage, $P_{ii}$, of the $i$th observation satisfies
$$P_{ii}=\frac1n+\frac{(X_{i2}-\bar X_2)^2}{\sum_{k=1}^n(X_{k2}-\bar X_2)^2},$$
where $\bar X_2:=\frac1n\sum_{k=1}^nX_{k2}$. Describe what kind of observations may have a large leverage. Hint: Why can we assume that the $i$th component of the second column is $X_{i2}-\bar X_2$ rather than $X_{i2}$?

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::

::: {.problem #prob-camii-sms-2-q11 origin="external" source="camii-sms-2-q11"}
(a) Let $A$ be a $p\times p$ non-singular matrix and let $b\in\mathbb R^p$. Prove that if $v^{\mathsf T}A^{-1}u\neq-1$, then $A+uv^{\mathsf T}$ is invertible with inverse given by the Sherman–Morrison formula
$$(A+uv^{\mathsf T})^{-1}=A^{-1}-\frac{A^{-1}uv^{\mathsf T}A^{-1}}{1+v^{\mathsf T}A^{-1}u}.$$

(b) Consider the normal linear model $Y=X\beta+\varepsilon$. Let $X_i^{\mathsf T}$ denote the $i$th row of $X$. Further, let $X_{(-i)}$ denote the $(n-1)\times p$ matrix obtained by deleting the $i$th row of $X$, and suppose that this matrix has full column rank and that the leverage score of the $i$th observation, $P_{ii}$, is less than 1. Let $\hat\beta_{(-i)}$ be the OLS estimator of $\beta$ when the $i$th observation has been removed. Prove that the difference
$$\operatorname{Var}(\hat\beta_{(-i)})-\operatorname{Var}(\hat\beta)$$
is positive semi-definite. Hint: Use $X^{\mathsf T}X=\sum_{i=1}^nX_iX_i^{\mathsf T}$ and $P_{ii}=X_i^{\mathsf T}(X^{\mathsf T}X)^{-1}X_i$.

(c) Show that
$$\hat\beta-\hat\beta_{(-i)}=\frac1{1-P_{ii}}(X^{\mathsf T}X)^{-1}X_i(Y_i-X_i^{\mathsf T}\hat\beta),\tag{1}$$
and use this to deduce the identity
$$\hat\mu_i=P_{ii}Y_i+(1-P_{ii})\hat\mu_{(-i)},\tag{2}$$
where $\hat\mu_i=X_i^{\mathsf T}\hat\beta$ and $\hat\mu_{(-i)}=X_i^{\mathsf T}\hat\beta_{(-i)}$.

(d) Show that Cook's distance $D_i$ of the observation $(Y_i,X_i)$ can be expressed as
$$D_i:=\frac{\|X(\hat\beta-\hat\beta_{(-i)})\|^2}{p\hat\sigma^2}=\frac1p\frac{P_{ii}}{1-P_{ii}}\hat\eta_i^2,$$
where $\hat\eta_i=(Y_i-X_i^{\mathsf T}\hat\beta)/(\hat\sigma\sqrt{1-P_{ii}})$ is the $i$th studentised fitted residual.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::

::: {.problem #prob-camii-sms-2-q12 origin="external" source="camii-sms-2-q12"}
(a) (Continuation) The externally studentised residual of the $i$th observation may be defined as
$$\tilde\eta_i:=\frac{\hat\varepsilon_i}{\hat\sigma_{(-i)}\sqrt{1-P_{ii}}},$$
where $\hat\sigma_{(-i)}$ is the equivalent of $\hat\sigma$ but calculated omitting the $i$th observation, so
$$\hat\sigma^2_{(-i)}=\frac1{n-p-1}\|Y_{(-i)}-X_{(-i)}\hat\beta_{(-i)}\|^2,$$
where $Y_{(-i)}$ is the response $Y$ without the $i$th component. Show that $\tilde\eta_i\sim t_{n-p-1}$ in the normal linear model, that is, if $\varepsilon\mid X\sim N(0,\sigma^2I)$. Hint: Use (2). How can we construct a hypothesis test based on $\tilde\eta_i$ to test whether the $i$th observation is an outlier?

*Note (these notes):* Part (b) of the sheet question, which applies this test to the `mammals` data in R, is omitted. Equation (2) is the identity $\hat\mu_i=P_{ii}Y_i+(1-P_{ii})\hat\mu_{(-i)}$ of question 11; $\hat\varepsilon_i=Y_i-\hat\mu_i$. Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::
