---
title: "The Method of Moments"
sources: [mit18650-4]
requires: [math/statistics/inference/slutsky-and-delta-method, math/analysis/real/uniform-convergence/weierstrass-approximation]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 4 (moments determine a distribution: Weierstrass approximation and the finite-support case; moment estimators and their asymptotic normality; comparison with maximum likelihood), in our own wording. The uniqueness proof, the Gamma and uniform examples are our own. -->

Maximum likelihood fits a model by matching the whole distribution. A cruder but often simpler idea is to match a few averages: choose the parameter whose distribution has the same first few moments as the sample.

::: {#prp-moments-determine-distribution .proposition name="Moments determine a distribution on an interval"}

1. Let $f$ and $g$ be densities on a bounded interval $[a,b]$ with the same moments: $\int_a^bx^kf(x)\,dx=\int_a^bx^kg(x)\,dx$ for $k=1,2,\dots$. Then $\int_a^bh\,f=\int_a^bh\,g$ for every continuous $h$, so $f$ and $g$ define the same distribution.
2. Let $X$ take values in a finite set $\{x_1,\dots,x_r\}$ of distinct numbers. Then the moments $m_k=E[X^k]$, $k=1,\dots,r-1$, determine the mass function of $X$.

:::

::: {.proof}

1. By linearity, $\int P\,f=\int P\,g$ for every polynomial $P$ (the constant term matches because both integrate to $1$).

2. Let $h$ be continuous on $[a,b]$ and $\varepsilon>0$. By the Weierstrass approximation theorem (@thm-weierstrass-approximation) there is a polynomial $P$ with $|h-P|\le\varepsilon$ on $[a,b]$. Then $\bigl|\int h\,f-\int h\,g\bigr|\le\int|h-P|f+\int|h-P|g\le2\varepsilon$. As $\varepsilon$ is arbitrary, $\int h\,f=\int h\,g$.

3. Expectations of all continuous functions determine the CDF (approximate the indicator of $(-\infty,t]$ from above and below by continuous functions and use monotone convergence), so the two distributions agree.

4. For part 2, the unknowns $p_j=\Pr(X=x_j)$ satisfy the $r$ linear equations
   $$\sum_{j=1}^rx_j^kp_j=m_k\quad(k=1,\dots,r-1),\qquad\sum_{j=1}^rp_j=1 .$$
   Its coefficient matrix, with rows $(x_1^k,\dots,x_r^k)$ for $k=0,\dots,r-1$, is a Vandermonde matrix with determinant $\pm\prod_{j<k}(x_k-x_j)\ne0$, since the $x_j$ are distinct. So the system has exactly one solution.

:::

In a parametric model fewer moments usually suffice: as a rule of thumb, a parameter in $\mathbb{R}^d$ needs $d$ moments.

::: {#def-method-of-moments .definition name="Method of moments estimator"}

Let $X_1,\dots,X_n$ be independent with distribution $\Pr_\theta$, $\theta\in\Theta\subseteq\mathbb{R}^d$. Define the *population moments* and *empirical moments*
$$m_k(\theta)=E_\theta[X^k],\qquad \hat m_k=\frac1n\sum_{i=1}^nX_i^k,\qquad k=1,\dots,d,$$
and the map $\psi:\Theta\to\mathbb{R}^d$, $\psi(\theta)=\bigl(m_1(\theta),\dots,m_d(\theta)\bigr)$. If $\psi$ is one to one, the *method of moments estimator* is
$$\hat\theta_n^{\mathrm{MM}}=\psi^{-1}\bigl(\hat m_1,\dots,\hat m_d\bigr),$$
whenever $(\hat m_1,\dots,\hat m_d)$ lies in the range of $\psi$.

:::

Any $d$ functions $g_1,\dots,g_d$ with $E_\theta[g_k(X)]$ one to one in $\theta$ can replace the powers $x^k$; central moments such as the variance are a common choice.

::: {#exm-mom-gamma .example name="Gamma shape and scale"}

Let $X\sim\operatorname{Gamma}(k,s)$ with shape $k>0$ and scale $s>0$ (density proportional to $x^{k-1}e^{-x/s}$ on $x>0$). Then $E[X]=ks$ and $\mathrm{Var}(X)=ks^2$, so $m_1=ks$ and $m_2-m_1^2=ks^2$. Solving,
$$s=\frac{m_2-m_1^2}{m_1},\qquad k=\frac{m_1^2}{m_2-m_1^2},$$
and the moment estimators are these expressions with $\hat m_1,\hat m_2$ in place of $m_1,m_2$. For a sample with $\hat m_1=6$ and $\hat m_2=48$ the empirical variance is $12$, giving $\hat s=2$ and $\hat k=3$. The MLE of $k$ has no closed form (it involves the derivative of $\log\Gamma$), so the moment estimator is a useful starting point for a numerical search.

:::

::: {#thm-mom-asymptotic-normality .theorem name="Asymptotic normality of moment estimators"}

In @def-method-of-moments write $M(\theta)=\psi(\theta)$ and $\hat M=(\hat m_1,\dots,\hat m_d)$, and let $\Sigma(\theta)$ be the covariance matrix of the random vector $(X,X^2,\dots,X^d)$ under $\Pr_\theta$ (assumed finite). If $\psi^{-1}$ is differentiable at $M(\theta)$ with Jacobian $J(\theta)=D\psi^{-1}\bigl(M(\theta)\bigr)$, then $\hat\theta_n^{\mathrm{MM}}$ is consistent and

$$
\sqrt n\,\bigl(\hat\theta_n^{\mathrm{MM}}-\theta\bigr)\xrightarrow{d}N_d\bigl(0,\ J(\theta)\,\Sigma(\theta)\,J(\theta)^{\mathsf T}\bigr).
$$

:::

::: {.proof}

1. The vectors $(X_i,X_i^2,\dots,X_i^d)$ are independent with mean $M(\theta)$ and covariance $\Sigma(\theta)$, and $\hat M$ is their average. By the multivariate central limit theorem (@thm-multivariate-clt), $\sqrt n(\hat M-M(\theta))\xrightarrow{d}N_d(0,\Sigma(\theta))$.

2. Since $\hat\theta_n^{\mathrm{MM}}=\psi^{-1}(\hat M)$ and $\theta=\psi^{-1}(M(\theta))$, the multivariate delta method (@thm-multivariate-delta-method) with $g=\psi^{-1}$ gives the stated limit.

3. Consistency follows from asymptotic normality (@prp-asymptotically-normal-consistent).

:::

::: {#exm-mom-uniform .example name="Uniform on an interval: moments against maximum likelihood"}

Let $X_i$ be uniform on $[0,\theta]$. Then $m_1(\theta)=\theta/2$, so $\hat\theta^{\mathrm{MM}}=2\bar X_n$. Here $d=1$, $\Sigma(\theta)=\mathrm{Var}(X)=\theta^2/12$ and $J=(\psi^{-1})'=2$, so
$$\sqrt n\,(2\bar X_n-\theta)\xrightarrow{d}N\bigl(0,\theta^2/3\bigr).$$
The MLE $\max_iX_i$ has error of order $1/n$ instead (@exm-mle-moving-support), far smaller for large $n$. The moment estimator can even be impossible: $2\bar X_n$ is sometimes smaller than $\max_iX_i$, a value of $\theta$ the data rule out.

:::

::: {#rmk-mle-versus-moments .remark name="Maximum likelihood or moments?"}

When the conditions of @thm-mle-asymptotic-normality hold, the MLE usually has smaller asymptotic variance than a moment estimator, because its variance $I(\theta)^{-1}$ is the smallest possible. Moment estimators win on computation: they need only averages and the inversion of $\psi$, while the MLE may have no closed form. When the log-likelihood is concave, its maximiser can be computed by convex optimisation; when it is not, only local methods such as EM (@sec-ai-unsupervised-learning-em-algorithm) are available, and they may stop at a local maximum. A moment estimator is then a good starting point.

:::
