---
title: "Inference in the Linear Model"
sources: [mit18650-7, camii-sms-1-q3, camii-sms-1-q9]
requires: [math/statistics/frequentist/multiple-linear-regression]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 7 (significance tests for one coefficient and for groups of coefficients, Bonferroni's test, the F test of a linear hypothesis, lack of identifiability, subset selection with AIC/BIC and the Lasso), in our own wording. The proofs, the continuation of the six-point example and the remark on why the Lasso is convex are our own. -->

In the Gaussian linear model (@thm-gaussian-linear-model) the estimator $\hat\beta$ and the variance estimate $\hat\sigma^2$ have exact, independent distributions. This turns questions such as "does the $j$th variable matter?" into exact tests. Throughout, $\mathbf Y=\mathbb X\beta+\boldsymbol\varepsilon$ with deterministic $\mathbb X\in\mathbb{R}^{n\times p}$ of rank $p<n$ and $\boldsymbol\varepsilon\sim N_n(0,\sigma^2I_n)$; $q_\alpha(\cdot)$ denotes the $(1-\alpha)$-quantile of a distribution.

::: {#thm-coefficient-t-test .theorem name="t-test for one coefficient"}

Let $\gamma_j>0$ be the $j$th diagonal entry of $(\mathbb X^{\mathsf T}\mathbb X)^{-1}$. Then

$$
\frac{\hat\beta_j-\beta_j}{\hat\sigma\sqrt{\gamma_j}}\sim t_{n-p} .
$$

Hence, to test $H_0:\beta_j=0$ against $H_1:\beta_j\ne0$, the test $\delta_\alpha^{(j)}=\mathbf 1\{|T^{(j)}|>q_{\alpha/2}(t_{n-p})\}$ with $T^{(j)}=\hat\beta_j/(\hat\sigma\sqrt{\gamma_j})$ has level exactly $\alpha$, for every $n$.

:::

::: {.proof}

1. By @thm-gaussian-linear-model, $\hat\beta_j\sim N(\beta_j,\sigma^2\gamma_j)$, so $Z=(\hat\beta_j-\beta_j)/(\sigma\sqrt{\gamma_j})\sim N(0,1)$.

2. By the same theorem $V=(n-p)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p}$, independent of $\hat\beta$ and hence of $Z$.

3. The ratio in the statement equals $Z/\sqrt{V/(n-p)}$, which is $t_{n-p}$ by @def-t-distribution.

4. Under $H_0$, $T^{(j)}$ is this ratio, and $\Pr(|T^{(j)}|>q_{\alpha/2}(t_{n-p}))=\alpha$ by symmetry of the $t$ distribution.

:::

::: {#exm-six-points-tests .example name="Is the slope significant?"}

In @exm-linear-model-six-points, $n-p=4$ and $q_{0.025}(t_4)\approx2.776$. The slope has $T^{(2)}=0.68/0.119\approx5.72$, p-value $\approx0.005$: significant at the $5\%$ level. The intercept has $T^{(1)}=0.72/0.463\approx1.56$, p-value $\approx0.19$: not significant. A $95\%$ confidence interval for the slope is $0.68\pm2.776\cdot0.119=[0.35,\,1.01]$.

:::

To test several coefficients at once, $H_0:\beta_j=0$ for all $j\in S$, running one $t$-test per coefficient at level $\alpha$ is wrong: the chance that at least one of them rejects a true null is larger than $\alpha$.

::: {#prp-bonferroni-test .proposition name="Bonferroni's test"}

Let $S\subseteq\{1,\dots,p\}$ with $|S|=k$, and $H_0:\beta_j=0$ for all $j\in S$. The test that rejects if any single test rejects at the reduced level $\alpha/k$,
$$\delta_\alpha^{B}=\max_{j\in S}\delta_{\alpha/k}^{(j)},$$
has level at most $\alpha$.

:::

::: {.proof}

1. Under $H_0$, $\Pr(\delta_\alpha^B=1)=\Pr\bigl(\bigcup_{j\in S}\{\delta_{\alpha/k}^{(j)}=1\}\bigr)\le\sum_{j\in S}\Pr(\delta_{\alpha/k}^{(j)}=1)$ by the union bound.

2. Each term equals $\alpha/k$ by @thm-coefficient-t-test, so the sum is $\alpha$.

:::

Bonferroni's correction needs no assumption on how the $k$ statistics depend on each other, which is its strength; it is conservative when $k$ is large. An exact test of a group of linear constraints uses the $F$ distribution (@def-f-distribution).

::: {#thm-f-test-linear-hypothesis .theorem name="F test of a linear hypothesis"}

Let $G\in\mathbb{R}^{k\times p}$ have rank $k\le p$ and $\lambda\in\mathbb{R}^k$, and test $H_0:G\beta=\lambda$ against $H_1:G\beta\ne\lambda$. Let

$$
S_n=\frac{(G\hat\beta-\lambda)^{\mathsf T}\bigl(G(\mathbb X^{\mathsf T}\mathbb X)^{-1}G^{\mathsf T}\bigr)^{-1}(G\hat\beta-\lambda)}{k\,\hat\sigma^2}.
$$

Under $H_0$, $S_n\sim F_{k,n-p}$, so $\delta_\alpha=\mathbf 1\{S_n>q_\alpha(F_{k,n-p})\}$ has level exactly $\alpha$.

:::

::: {.proof}

1. Write $C=G(\mathbb X^{\mathsf T}\mathbb X)^{-1}G^{\mathsf T}$. It is positive definite: for $v\ne0$, $G^{\mathsf T}v\ne0$ since $G$ has rank $k$, and $(\mathbb X^{\mathsf T}\mathbb X)^{-1}$ is positive definite.

2. Under $H_0$, $G\hat\beta-\lambda=G(\hat\beta-\beta)\sim N_k(0,\sigma^2C)$ (@thm-gaussian-linear-model, part 2, and @thm-jointly-gaussian-properties). Hence $W=\sigma^{-1}C^{-1/2}(G\hat\beta-\lambda)\sim N_k(0,I_k)$, and $U=\|W\|^2=(G\hat\beta-\lambda)^{\mathsf T}C^{-1}(G\hat\beta-\lambda)/\sigma^2\sim\chi^2_k$.

3. $V=(n-p)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p}$ is independent of $\hat\beta$, hence of $U$.

4. $S_n=\dfrac{U/k}{V/(n-p)}$ (the unknown $\sigma^2$ cancels), which is $F_{k,n-p}$ by definition.

:::

With $G$ the rows of $I_p$ indexed by $S$ and $\lambda=0$ this tests the group hypothesis of @prp-bonferroni-test exactly. With $k=1$ and $G=e_j^{\mathsf T}$, $S_n=(T^{(j)})^2$ and the $F$ test is the two-sided $t$-test, since $t_m^2\sim F_{1,m}$.

::: {#rmk-rank-deficient-design .remark name="When the design has rank less than p"}

If $\operatorname{rank}\mathbb X=k<p$, for example when $p>n$, different $\beta$ give the same mean $\mathbb X\beta$, so $\beta$ is not identified (@def-identifiable) and cannot be estimated without further assumptions. The mean $\mathbb X\beta$ is still identified: the fitted vector $\hat{\mathbf Y}$ is the projection of $\mathbf Y$ onto the column space, computed for instance with the pseudoinverse (@def-pseudoinverse) as $\hat{\mathbf Y}=\mathbb X\mathbb X^{+}\mathbf Y$. The proof of @thm-gaussian-linear-model, with $p$ replaced by $k$, shows $\|\mathbf Y-\hat{\mathbf Y}\|^2/\sigma^2\sim\chi^2_{n-k}$ independently of $\hat{\mathbf Y}$, so $\|\mathbf Y-\hat{\mathbf Y}\|^2/(n-k)$ is unbiased for $\sigma^2$.

:::

::: {#def-subset-selection-lasso .definition name="Penalised subset selection and the Lasso" related="def-regularization"}

When $p$ is large but only a few coefficients are believed to be non-zero, one selects a subset $S$ of covariates. Writing $\mathbb X_S$ for the columns indexed by $S$ and $\hat\beta^S$ for the LSE using only them, one chooses $S$ to minimise
$$\|\mathbf Y-\mathbb X_S\hat\beta^S\|^2+\lambda|S|,$$
a fit term plus a penalty on model size. The choice $\lambda=2\hat\sigma^2$ is *Mallows' $C_p$* (equivalent to *AIC* for Gaussian noise), and $\lambda=\hat\sigma^2\log n$ is *BIC*. Equivalently, $\hat\beta$ minimises $\|\mathbf Y-\mathbb Xb\|^2+\lambda\|b\|_0$, where $\|b\|_0$ is the number of non-zero entries. The *Lasso* replaces $\|b\|_0$ by $\|b\|_1=\sum_j|b_j|$:
$$\hat\beta^{L}\in\operatorname*{argmin}_{b\in\mathbb{R}^p}\ \|\mathbf Y-\mathbb Xb\|^2+\lambda\|b\|_1 .$$

:::

The $\ell_0$ problem is combinatorial: it compares $2^p$ subsets. The Lasso objective is a convex quadratic plus a norm, hence convex, and is solved efficiently; the corners of the $\ell_1$ ball make many coordinates of the minimiser exactly zero, so it still selects variables. How to choose $\lambda$ is a hard question of high-dimensional statistics.
