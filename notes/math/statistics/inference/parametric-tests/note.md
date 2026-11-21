---
title: "Asymptotic Tests: Wald, Likelihood Ratio and Pearson"
sources: [mit18650-5]
requires: [math/statistics/inference/fisher-information, math/statistics/frequentist/chi-square-and-f-tests]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 5 (tests as statistics with values in {0,1}; level, asymptotic level, power and p-values; Wald's test; the likelihood ratio test; testing implicit hypotheses; the chi-square test for a multinomial), in our own wording. The coin example, the proofs (the likelihood ratio theorem in the case of a simple null) and the remark on one-sided tests are our own. -->

Significance tests (@def-significance-test) were built so far from exact null distributions: binomial, normal, $t$, $\chi^2$. For a general parametric model the exact distribution of a test statistic is rarely known, but the asymptotic normality of the MLE (@thm-mle-asymptotic-normality) gives approximate null distributions for whole families of tests. Throughout, $q_\alpha(\chi^2_k)$ denotes the $(1-\alpha)$-quantile of $\chi^2_k$ (@def-chi-square-distribution).

::: {#def-test-asymptotic-level .definition name="Test, level and power as functions of the parameter" related="def-significance-power"}

Let $(E,(\Pr_\theta)_{\theta\in\Theta})$ be a model and $\Theta_0,\Theta_1\subseteq\Theta$ disjoint. To test $H_0:\theta\in\Theta_0$ against $H_1:\theta\in\Theta_1$, a *test* is a statistic $\psi=\psi(X_1,\dots,X_n)\in\{0,1\}$; $\psi=1$ means "reject $H_0$". Usually $\psi=\mathbf 1\{T_n>c\}$ for a *test statistic* $T_n$ and a threshold $c$.

1. The *type I error* is the function $\alpha_\psi(\theta)=\Pr_\theta(\psi=1)$ on $\Theta_0$, the *type II error* the function $\beta_\psi(\theta)=\Pr_\theta(\psi=0)$ on $\Theta_1$, and the *power* is $\pi_\psi=\inf_{\theta\in\Theta_1}\bigl(1-\beta_\psi(\theta)\bigr)$.
2. $\psi$ has *level* $\alpha$ if $\alpha_\psi(\theta)\le\alpha$ for all $\theta\in\Theta_0$, and *asymptotic level* $\alpha$ if $\limsup_{n\to\infty}\alpha_\psi(\theta)\le\alpha$ for all $\theta\in\Theta_0$.
3. For a family of tests $\psi_\alpha$, one for each level, the (asymptotic) *p-value* is the smallest $\alpha$ at which $\psi_\alpha$ rejects. It is a statistic, and $H_0$ is rejected at level $\alpha$ exactly when the p-value is at most $\alpha$ (compare @prp-p-value-rule).

:::

The two hypotheses are not symmetric: the data are used only to look for evidence against $H_0$, and failing to reject is not evidence for $H_0$. The trivial test $\psi=0$ has level $0$ and power $0$; the aim is high power at a given level.

::: {#thm-wald-test .theorem name="Wald's test"}

Under the conditions of @thm-mle-asymptotic-normality, with $\Theta\subseteq\mathbb{R}^d$, $\theta_0\in\Theta$ given and $I$ continuous, consider $H_0:\theta=\theta_0$ against $H_1:\theta\ne\theta_0$, and the *Wald statistic*

$$
T_n=n\,\bigl(\hat\theta_n-\theta_0\bigr)^{\mathsf T}I(\hat\theta_n)\bigl(\hat\theta_n-\theta_0\bigr),
$$

where $\hat\theta_n$ is the MLE. If $H_0$ is true, $T_n\xrightarrow{d}\chi^2_d$, so $\psi=\mathbf 1\{T_n>q_\alpha(\chi^2_d)\}$ has asymptotic level $\alpha$.

:::

::: {.proof}

1. Under $\Pr_{\theta_0}$, $\sqrt n(\hat\theta_n-\theta_0)\xrightarrow{d}W\sim N_d(0,I(\theta_0)^{-1})$.

2. The MLE is consistent and $I$ is continuous, so $I(\hat\theta_n)\xrightarrow{P}I(\theta_0)$ entrywise; the symmetric square root $A\mapsto A^{1/2}$ is continuous on positive definite matrices, so $I(\hat\theta_n)^{1/2}\xrightarrow{P}I(\theta_0)^{1/2}$.

3. By Slutsky's theorem (@thm-slutsky), $I(\hat\theta_n)^{1/2}\sqrt n(\hat\theta_n-\theta_0)\xrightarrow{d}I(\theta_0)^{1/2}W$, which is $N_d(0,I_d)$ by @thm-jointly-gaussian-properties, part 2.

4. $T_n$ is the squared length of this vector. By continuous mapping it converges in distribution to the squared length of a standard normal vector, which is $\chi^2_d$ by definition.

:::

The same statistic, or its signed version $\sqrt{n I(\hat\theta_n)}\,(\hat\theta_n-\theta_0)$ when $d=1$, also tests one-sided alternatives such as $\theta>\theta_0$: reject when the signed statistic exceeds the $(1-\alpha)$-quantile of $N(0,1)$.

::: {#thm-likelihood-ratio-test .theorem name="Likelihood ratio test"}

Let $\ell_n(\theta)=\sum_{i=1}^n\log p_\theta(X_i)$, $\Theta\subseteq\mathbb{R}^d$, and let the null hypothesis fix the last $d-r$ coordinates,
$$H_0:\ (\theta_{r+1},\dots,\theta_d)=(\theta^{(0)}_{r+1},\dots,\theta^{(0)}_d),\qquad 0\le r<d .$$
Let $\hat\theta_n$ maximise $\ell_n$ over $\Theta$ and $\hat\theta_n^{c}$ maximise it over $\Theta_0=\{\theta\in\Theta:\theta\text{ satisfies }H_0\}$ (the *constrained MLE*). Under $H_0$ and the conditions of @thm-mle-asymptotic-normality,

$$
T_n=2\bigl(\ell_n(\hat\theta_n)-\ell_n(\hat\theta_n^{c})\bigr)\xrightarrow{d}\chi^2_{d-r},
$$

so $\psi=\mathbf 1\{T_n>q_\alpha(\chi^2_{d-r})\}$ has asymptotic level $\alpha$.

:::

::: {.proof}

We prove the case $r=0$, a simple null $\theta=\theta_0$, where $\hat\theta^c_n=\theta_0$; the general case (Wilks' theorem) needs the same expansion for the constrained MLE as well and is not proved here. As in the proof of @thm-mle-asymptotic-normality we assume three bounded derivatives, and write the proof for $d=1$; the vector case replaces squares by quadratic forms.

1. Expand $\ell_n$ around $\hat\theta_n$, where $\ell_n'(\hat\theta_n)=0$ with probability tending to $1$:
   $$\ell_n(\theta_0)=\ell_n(\hat\theta_n)+\tfrac12(\theta_0-\hat\theta_n)^2\,\ell_n''(\bar\theta_n)$$
   for some $\bar\theta_n$ between $\theta_0$ and $\hat\theta_n$.

2. Hence
   $$T_n=2\bigl(\ell_n(\hat\theta_n)-\ell_n(\theta_0)\bigr)=\Bigl(-\frac1n\ell_n''(\bar\theta_n)\Bigr)\cdot\bigl(\sqrt n(\hat\theta_n-\theta_0)\bigr)^2 .$$

3. Since $\bar\theta_n\xrightarrow{P}\theta_0$ and $\ell'''$ is bounded by an integrable function, $-\frac1n\ell_n''(\bar\theta_n)\xrightarrow{P}I(\theta_0)$, exactly as in step 5 of that proof.

4. By Slutsky's theorem and continuous mapping, $T_n\xrightarrow{d}I(\theta_0)W^2$ with $W\sim N(0,I(\theta_0)^{-1})$. Since $\sqrt{I(\theta_0)}\,W\sim N(0,1)$, the limit is $\chi^2_1=\chi^2_{d-r}$.

:::

::: {#exm-wald-lrt-coin .example name="Wald and likelihood ratio tests for a coin"}

A coin lands heads $118$ times in $n=200$ tosses; test $H_0:p=1/2$ at asymptotic level $5\%$. Here $d=1$, $\hat p=0.59$, $I(p)=1/(p(1-p))$ (@exm-fisher-information-bernoulli), and $q_{0.05}(\chi^2_1)=1.96^2\approx3.84$.

1. *Wald:* $T_n=200\,(0.09)^2/(0.59\cdot0.41)\approx6.70$, p-value $\Pr(\chi^2_1>6.70)\approx0.0097$.
2. *Likelihood ratio:* $T_n=2\bigl[118\log\frac{0.59}{0.5}+82\log\frac{0.41}{0.5}\bigr]\approx6.52$, p-value $\approx0.0107$.
3. For comparison the $z$-test of @def-z-test, which standardises with the null variance $1/4$, has $z^2=6.48$ and p-value $\approx0.0109$.

All three reject $H_0$; they differ only in how the variance is estimated, and agree to first order.

:::

::: {#thm-implicit-hypothesis-test .theorem name="Testing an implicit hypothesis"}

Let $\hat\theta_n$ be an estimator of $\theta\in\mathbb{R}^d$ with $\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}N_d(0,\Sigma(\theta))$, and let $g:\mathbb{R}^d\to\mathbb{R}^k$, $k\le d$, be continuously differentiable with Jacobian $J(\theta)$ of rank $k$. Put $\Gamma(\theta)=J(\theta)\Sigma(\theta)J(\theta)^{\mathsf T}$ and assume $\Sigma$ is continuous and invertible. To test $H_0:g(\theta)=0$ against $H_1:g(\theta)\ne0$, use

$$
T_n=n\,g(\hat\theta_n)^{\mathsf T}\,\Gamma(\hat\theta_n)^{-1}\,g(\hat\theta_n).
$$

Under $H_0$, $T_n\xrightarrow{d}\chi^2_k$, so $\psi=\mathbf 1\{T_n>q_\alpha(\chi^2_k)\}$ has asymptotic level $\alpha$.

:::

::: {.proof}

1. By the multivariate delta method (@thm-multivariate-delta-method), $\sqrt n(g(\hat\theta_n)-g(\theta))\xrightarrow{d}N_k(0,\Gamma(\theta))$, and under $H_0$ the centring term $g(\theta)$ is $0$.

2. $\Gamma(\theta)$ is invertible: for $v\ne0$, $J^{\mathsf T}v\ne0$ because $J$ has rank $k$, so $v^{\mathsf T}\Gamma v=(J^{\mathsf T}v)^{\mathsf T}\Sigma(J^{\mathsf T}v)>0$.

3. $\Gamma$ is continuous and $\hat\theta_n$ is consistent, so $\Gamma(\hat\theta_n)^{-1/2}\xrightarrow{P}\Gamma(\theta)^{-1/2}$. As in the proof of @thm-wald-test, $\Gamma(\hat\theta_n)^{-1/2}\sqrt n\,g(\hat\theta_n)\xrightarrow{d}N_k(0,I_k)$, and $T_n$, its squared length, tends to $\chi^2_k$.

:::

Examples: $g(\theta)=\theta_1-\theta_2$ tests equality of two coordinates ($k=1$); $g(\theta)=(\theta_1,\theta_2)$ tests that two coordinates vanish ($k=2$). Wald's test is the case $g(\theta)=\theta-\theta_0$ with $\hat\theta_n$ the MLE and $\Sigma=I^{-1}$.

::: {#thm-pearson-chi-square-limit .theorem name="Pearson's statistic is asymptotically chi-square" related="def-goodness-of-fit"}

Let $X_1,\dots,X_n$ be independent with values in $\{a_1,\dots,a_K\}$ and $\Pr(X_i=a_j)=p_j$, let $N_j$ be the number of $i$ with $X_i=a_j$ and $\hat p_j=N_j/n$ (the MLE of $p$). If $p=p^0$ with all $p^0_j>0$, then

$$
T_n=n\sum_{j=1}^K\frac{(\hat p_j-p^0_j)^2}{p^0_j}=\sum_{j=1}^K\frac{(N_j-np^0_j)^2}{np^0_j}\xrightarrow{d}\chi^2_{K-1}.
$$

:::

::: {.proof}

1. Let $Y_i\in\mathbb{R}^K$ be the indicator vector with entries $\mathbf 1\{X_i=a_j\}$, so $\hat p=\bar Y_n$. The $Y_i$ are independent with mean $p^0$ and covariance $\Sigma=D-p^0p^{0\mathsf T}$, where $D=\operatorname{diag}(p^0)$: indeed $\mathrm{Var}(\mathbf 1\{X=a_j\})=p_j^0(1-p_j^0)$ and, for $j\ne k$, $\operatorname{Cov}=0-p^0_jp^0_k$ because the two indicators are never both $1$.

2. By the multivariate central limit theorem (@thm-multivariate-clt), $\sqrt n(\hat p-p^0)\xrightarrow{d}W\sim N_K(0,\Sigma)$. Then $U_n=D^{-1/2}\sqrt n(\hat p-p^0)\xrightarrow{d}D^{-1/2}W\sim N_K(0,P)$ with
   $$P=D^{-1/2}\Sigma D^{-1/2}=I_K-uu^{\mathsf T},\qquad u=\bigl(\sqrt{p^0_1},\dots,\sqrt{p^0_K}\bigr)^{\mathsf T}.$$

3. Since $\|u\|^2=\sum_jp_j^0=1$, $P$ is the orthogonal projection onto the hyperplane $u^\perp$, of dimension $K-1$. Choose an orthonormal basis $v_1,\dots,v_{K-1}$ of $u^\perp$; a vector $V\sim N_K(0,P)$ has the law of $\sum_{m=1}^{K-1}Z_mv_m$ with $Z_m$ independent $N(0,1)$ (both are centred Gaussian with covariance $\sum_mv_mv_m^{\mathsf T}=P$), so $\|V\|^2\sim\chi^2_{K-1}$.

4. $T_n=\|U_n\|^2$, so by continuous mapping $T_n\xrightarrow{d}\chi^2_{K-1}$.

:::

This is the theorem behind the chi-square test for goodness of fit (@def-goodness-of-fit) with no estimated parameters. When the cell probabilities are $p_j(\theta)$ for a $d$-dimensional parameter estimated by maximum likelihood under $H_0$, the statistic $n\sum_j(\hat p_j-p_j(\hat\theta))^2/p_j(\hat\theta)$ tends to $\chi^2_{K-1-d}$ instead (for $d<K-1$, under regularity conditions; not proved here). For data on an infinite space one first groups the values into $K$ bins.
