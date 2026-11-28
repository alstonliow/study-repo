::: {.problem #prob-camib-sts-3-q7 origin="external" source="camib-sts-3-q7"}
Consider the one-way analysis of variance (ANOVA) model
$$Y_{ij}=\mu_i+\varepsilon_{ij},\qquad i=1,\dots,I,\ j=1,\dots,n_i,$$
where $(\varepsilon_{ij})\overset{\text{iid}}{\sim}N(0,\sigma^2)$. Derive from first principles explicit expressions for the MLEs $\hat\mu_1,\dots,\hat\mu_I$ and $\hat\sigma^2$. Show that we can obtain the same expressions if we regard the ANOVA model as a special case of the general linear regression model $Y=X\beta+\varepsilon$ and specialise the formulae $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$ and $\hat\sigma^2=n^{-1}\|Y-X\hat\beta\|^2$.
:::

::: {.problem #prob-camib-sts-3-q10 origin="external" source="camib-sts-3-q10"}
Consider the one-way ANOVA model of Question 7. Letting $\bar Y_i=n_i^{-1}\sum_{j=1}^{n_i}Y_{ij}$ and $\bar Y=n^{-1}\sum_{i=1}^I\sum_{j=1}^{n_i}Y_{ij}$ with $n=n_1+\dots+n_I$, show from first principles that the size $\alpha$ likelihood ratio test of equality of means rejects $H_0$ if
$$\frac{\frac1{I-1}\sum_{i=1}^In_i(\bar Y_i-\bar Y)^2}{\frac1{n-I}\sum_{i=1}^I\sum_{j=1}^{n_i}(Y_{ij}-\bar Y_i)^2}>k$$
where $F(k)=1-\alpha$ and $F$ is the distribution function of the $F_{I-1,n-I}$ distribution; i.e. if 'the ratio of the between groups sum of squares to the within groups sum of squares is large'.
:::

::: {.problem #prob-camii-sms-1-q1 origin="external" source="camii-sms-1-q1"}
Show that
$$\|(P-P_0)Y\|^2=\|(I-P_0)Y\|^2-\|(I-P)Y\|^2=\|PY\|^2-\|P_0Y\|^2.$$

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::

::: {.problem #prob-camii-sms-1-q2 origin="external" source="camii-sms-1-q2"}
Consider a random variable $T$ that follows the $F$-distribution with $d_1$ and $d_2$ degrees of freedom.

(a) When $d_1=1$, show that the distribution of $T$ is the same as the square of a random variable that follows the $t$-distribution of $d_2$ degrees of freedom.

(b) What can you say about the distribution of $T$ when $d_2\to\infty$? Use R to verify your conclusion. You may find some of these functions useful: `df`/`pf`, `dchisq`/`pchisq`, `hist`/`ecdf`/`qqplot`.
:::

::: {.problem #prob-camii-sms-1-q4 origin="external" source="camii-sms-1-q4"}
In the normal linear model, show that the likelihood ratio statistic for testing $H_0:\beta_1=0$ versus $H_1:\beta_1\neq0$ can be written as a monotonically increasing function of $\|(I-P_0)Y\|^2/\|(I-P)Y\|^2$.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$. Here $\beta=(\beta_0,\beta_1)$ is partitioned like $X=(X_0\ X_1)$.
:::

::: {.problem #prob-camii-sms-1-q12 origin="external" source="camii-sms-1-q12"}
This question is about understanding what can happen to the $F$-test when the linearity assumption does not hold. Consider the model in question 8 and let us assume $\epsilon$ follows the multivariate normal distribution. Define $\beta\in\mathbb R^p$ by $X\beta=P\mu$, so $Y=X\beta+(I-P)\mu+\varepsilon$, and partition $\beta=(\beta_0^{\mathsf T},\beta_1^{\mathsf T})^{\mathsf T}$ as before. Suppose we try to test the hypothesis $H_0:\beta_1=0$ against the alternative $H_1:\beta_1\neq0$ by rejecting the null hypothesis when
$$F:=\frac{\frac1{p-p_0}\|(P-P_0)Y\|^2}{\frac1{n-p}\|(I-P)Y\|^2}>F_{p-p_0,n-p}(\alpha).$$
We will show that the size of this test (the probability of rejecting $H_0$ when it is in fact true) is at most $\alpha$.

(a) Show that the numerator and denominator of $F$ are independent (no matter which hypothesis is true).

(b) What is the distribution of $\|(P-P_0)Y\|^2$ under the null hypothesis (i.e. when $Y=X_0\beta_0+(I-P)\mu+\varepsilon$)?

(c) By considering the eigendecomposition of $I-P$, show that $\|(I-P)Y\|^2$ has the same distribution as
$$Z_1^2+\dots+Z_{n-p}^2,$$
where the $Z_i$ are independent and $Z_i\sim N(\lambda_i,\sigma^2)$ for some $\lambda_i$ such that $\sum_{i=1}^{n-p}\lambda_i^2=\|(I-P)\mu\|^2$.

(d) For any two real-valued random variables $A$ and $B$, let us write $A\preceq B$ to mean $\mathbb P(A>x)\le\mathbb P(B>x)$ for all $x\in(-\infty,\infty)$ (we say $A$ is stochastically less than $B$). Now prove that if $A_1,\dots,A_m$ and $B_1,\dots,B_m$ are all independent real-valued random variables and $A_1\preceq B_1,\dots,A_m\preceq B_m$, then $A_1+\dots+A_m\preceq B_1+\dots+B_m$. Hint: Use induction on $m$ and recall that for real-valued random variables $U_1$ and $U_2$, the tower property of conditional expectation gives us that $\mathbb P(U_1+U_2>x)=\mathbb E\{\mathbb P(U_1>x-U_2\mid U_2)\}:=\mathbb E\{\mathbb E(\mathbf 1_{\{U_1>x-U_2\}}\mid U_2)\}$.

(e) Let $Z\sim\sigma^2\chi^2_{n-p}$. Show that $Z\preceq\|(I-P)Y\|^2$. Conclude that the size of the test mentioned at the beginning of this question is at most $\alpha$.

*Note (these notes):* In this question $\mu\in\mathbb R^n$ is the non-random mean vector of question 8 of sheet 1 (so $Y=\mu+\varepsilon$ with $\mathbb E\varepsilon=0$, $\operatorname{Var}\varepsilon=\sigma^2I$); Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::
