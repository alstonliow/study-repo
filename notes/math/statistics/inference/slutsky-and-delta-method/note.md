---
title: "Slutsky's Theorem and the Delta Method"
sources: [mit18650-1, mit18650-4]
requires: [math/statistics/inference/statistical-models, math/probability/estimation/jointly-gaussian]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 1 (Slutsky's theorem, the delta method) and Chapter 4 (multivariate delta method), in our own wording; proofs written out in steps, the example is our own. -->

The central limit theorem describes $\sqrt n(\bar X_n-\mu)$. Most estimators are not sample means but smooth functions of them, and most standardisations use an estimated variance instead of the true one. Two results transfer the central limit theorem to these situations.

::: {#thm-slutsky .theorem name="Slutsky's theorem"}

Let $X_n\xrightarrow{d}X$ and $Y_n\xrightarrow{P}c$, where $c$ is a constant. Then $(X_n,Y_n)\xrightarrow{d}(X,c)$, and in particular

$$
X_n+Y_n\xrightarrow{d}X+c,\qquad X_nY_n\xrightarrow{d}cX,\qquad \frac{X_n}{Y_n}\xrightarrow{d}\frac Xc\ \ (c\ne0).
$$

The same holds for random vectors and matrices of compatible sizes.

:::

::: {.proof}

1. We use the test of @prp-convergence-in-distribution-tests, part 1, in its form for vectors and in the (equivalent, also stated there without proof) version that needs only bounded *uniformly* continuous test functions: it suffices to show $E[h(X_n,Y_n)]\to E[h(X,c)]$ for every uniformly continuous $h$ with $|h|\le M$.

2. Split
   $$\bigl|E[h(X_n,Y_n)]-E[h(X,c)]\bigr|\le E\bigl|h(X_n,Y_n)-h(X_n,c)\bigr|+\bigl|E[h(X_n,c)]-E[h(X,c)]\bigr| .$$

3. The second term tends to $0$, because $x\mapsto h(x,c)$ is bounded and continuous and $X_n\xrightarrow{d}X$.

4. For the first term fix $\varepsilon>0$ and take $\delta>0$ with $|h(x,y)-h(x,y')|\le\varepsilon$ whenever $|y-y'|\le\delta$. Then the first term is at most $\varepsilon+2M\Pr(|Y_n-c|>\delta)$, and $\Pr(|Y_n-c|>\delta)\to0$.

5. Hence $\limsup_n|E[h(X_n,Y_n)]-E[h(X,c)]|\le\varepsilon$ for every $\varepsilon>0$, which proves $(X_n,Y_n)\xrightarrow{d}(X,c)$.

6. The three displayed statements follow from the continuous mapping theorem (@thm-continuous-mapping, for vectors) applied to $(x,y)\mapsto x+y$, $xy$ and $x/y$; the last map is continuous at every point $(x,c)$ with $c\ne0$, which is enough.

:::

The constant matters: the example after @prp-limits-of-sums-products shows that two sequences converging in distribution to non-constant limits cannot be added this way.

::: {#thm-multivariate-clt .theorem name="Multivariate central limit theorem" generalizes="thm-central-limit-theorem"}

Let $X_1,X_2,\dots$ be independent random vectors in $\mathbb{R}^d$ with the distribution of $X$, mean $\mu=E[X]$ and finite covariance matrix $\Sigma=E[(X-\mu)(X-\mu)^{\mathsf T}]$. Then
$$\sqrt n\,(\bar X_n-\mu)\xrightarrow{d}N_d(0,\Sigma).$$

:::

::: {.proof}

1. Fix $t\in\mathbb{R}^d$. The numbers $t^{\mathsf T}X_i$ are independent and identically distributed with mean $t^{\mathsf T}\mu$ and variance $t^{\mathsf T}\Sigma t$.

2. By the central limit theorem (@thm-central-limit-theorem; if $t^{\mathsf T}\Sigma t=0$ the variable is constant and the claim is trivial), $t^{\mathsf T}\sqrt n(\bar X_n-\mu)\xrightarrow{d}N(0,t^{\mathsf T}\Sigma t)$, which is the law of $t^{\mathsf T}W$ for $W\sim N_d(0,\Sigma)$ (@thm-jointly-gaussian-properties, part 2).

3. Convergence in distribution of real variables implies convergence of characteristic functions at the point $1$ (the function $x\mapsto e^{ix}$ is bounded and continuous, so its real and imaginary parts are covered by @prp-convergence-in-distribution-tests, part 1). Hence $E\bigl[e^{i\,t^{\mathsf T}\sqrt n(\bar X_n-\mu)}\bigr]\to E\bigl[e^{i\,t^{\mathsf T}W}\bigr]$.

4. This holds for every $t\in\mathbb{R}^d$, so by Lévy's continuity theorem for vectors (@prp-convergence-in-distribution-tests, part 2) $\sqrt n(\bar X_n-\mu)\xrightarrow{d}W$. (Testing all linear combinations in this way is the *Cramér–Wold device*.)

:::

::: {#thm-delta-method .theorem name="Delta method"}

Let $\sqrt n\,(Z_n-\theta)\xrightarrow{d}N(0,\sigma^2)$ for a constant $\theta\in\mathbb{R}$, and let $g:\mathbb{R}\to\mathbb{R}$ be differentiable at $\theta$. Then

$$
\sqrt n\,\bigl(g(Z_n)-g(\theta)\bigr)\xrightarrow{d}N\bigl(0,\ g'(\theta)^2\sigma^2\bigr).
$$

:::

::: {.proof}

1. Define $q(z)=\dfrac{g(z)-g(\theta)}{z-\theta}$ for $z\ne\theta$ and $q(\theta)=g'(\theta)$. Differentiability of $g$ at $\theta$ says exactly that $q$ is continuous at $\theta$, and $g(z)-g(\theta)=q(z)(z-\theta)$ for all $z$.

2. Since $\sqrt n(Z_n-\theta)$ converges in distribution, $Z_n\xrightarrow{P}\theta$ (the argument of @prp-asymptotically-normal-consistent). By continuity of $q$ at $\theta$, $q(Z_n)\xrightarrow{P}g'(\theta)$ (the proof of @thm-continuous-mapping needs continuity only at the limit point when the limit is a constant).

3. Now $\sqrt n\bigl(g(Z_n)-g(\theta)\bigr)=q(Z_n)\cdot\sqrt n(Z_n-\theta)$. By Slutsky's theorem (@thm-slutsky) the product converges in distribution to $g'(\theta)W$ with $W\sim N(0,\sigma^2)$, and $g'(\theta)W\sim N(0,g'(\theta)^2\sigma^2)$.

:::

If $g'(\theta)=0$ the limit is the point mass at $0$: the fluctuations of $g(Z_n)$ are then of smaller order than $1/\sqrt n$.

::: {#thm-multivariate-delta-method .theorem name="Multivariate delta method"}

Let $T_n$ be random vectors in $\mathbb{R}^p$ with $\sqrt n\,(T_n-\theta)\xrightarrow{d}N_p(0,\Sigma)$, and let $g:\mathbb{R}^p\to\mathbb{R}^k$ be differentiable at $\theta$, with Jacobian matrix $J=Dg(\theta)\in\mathbb{R}^{k\times p}$, $J_{ji}=\partial g_j/\partial\theta_i$. Then

$$
\sqrt n\,\bigl(g(T_n)-g(\theta)\bigr)\xrightarrow{d}N_k\bigl(0,\ J\Sigma J^{\mathsf T}\bigr).
$$

:::

::: {.proof}

1. Differentiability at $\theta$ means $g(t)-g(\theta)=J(t-\theta)+r(t)\,\|t-\theta\|$ with $r(t)\to0$ as $t\to\theta$ (set $r(\theta)=0$).

2. Multiply by $\sqrt n$ and put $t=T_n$:
   $$\sqrt n\bigl(g(T_n)-g(\theta)\bigr)=J\sqrt n(T_n-\theta)+r(T_n)\,\bigl\|\sqrt n(T_n-\theta)\bigr\| .$$

3. As in the scalar case $T_n\xrightarrow{P}\theta$, so $r(T_n)\xrightarrow{P}0$; and $\|\sqrt n(T_n-\theta)\|$ converges in distribution. By Slutsky's theorem the second term tends to $0$ in distribution, hence in probability (@thm-convergence-implications, part 3).

4. The first term converges in distribution to $JW$ with $W\sim N_p(0,\Sigma)$, which is $N_k(0,J\Sigma J^{\mathsf T})$ (a linear map of a Gaussian vector, @thm-jointly-gaussian-properties). Adding a term that tends to $0$ in probability does not change the limit (Slutsky again).

:::

In many texts the gradient $\nabla g(\theta)=J^{\mathsf T}\in\mathbb{R}^{p\times k}$ is used instead, and the covariance is written $\nabla g(\theta)^{\mathsf T}\Sigma\,\nabla g(\theta)$; it is the same matrix.

::: {#exm-delta-method-exponential .example name="The rate of an exponential"}

Let $T_1,\dots,T_n$ be independent $\operatorname{Exp}(\lambda)$ waiting times. Then $E[T_1]=1/\lambda$ and $\mathrm{Var}(T_1)=1/\lambda^2$, so by the central limit theorem $\sqrt n(\bar T_n-1/\lambda)\xrightarrow{d}N(0,\lambda^{-2})$. The natural estimator of the rate is $\hat\lambda=g(\bar T_n)$ with $g(t)=1/t$, and $g'(1/\lambda)=-\lambda^2$. By the delta method

$$
\sqrt n\,(\hat\lambda-\lambda)\xrightarrow{d}N\bigl(0,\ \lambda^4\cdot\lambda^{-2}\bigr)=N(0,\lambda^2).
$$

So $\hat\lambda$ is asymptotically normal with asymptotic variance $\lambda^2$. The variance involves the unknown $\lambda$; @sec-math-statistics-inference-asymptotic-confidence-intervals shows how to still build an interval from this.

:::
