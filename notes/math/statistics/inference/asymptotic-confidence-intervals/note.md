---
title: "Asymptotic Confidence Intervals"
sources: [mit18650-1, mit18650-2]
requires: [math/statistics/inference/slutsky-and-delta-method, math/statistics/frequentist/confidence-intervals]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 1 (intervals from the central limit theorem and from Hoeffding's inequality) and Chapter 2 (confidence intervals of asymptotic level; three ways to remove the unknown variance), in our own wording; the numerical examples are our own. -->

A confidence interval (@def-confidence-interval) must cover the true parameter with probability at least $1-\alpha$ for every parameter value. Exact intervals exist only in special models, such as normal data (@thm-normal-confidence-intervals). For other models we settle for coverage that is correct in the limit of large samples. Throughout, $q_{\alpha/2}$ is the $(1-\alpha/2)$-quantile of $N(0,1)$, so $\Pr(|Z|\le q_{\alpha/2})=1-\alpha$ for $Z\sim N(0,1)$; $q_{0.025}\approx1.96$.

::: {#def-asymptotic-confidence-interval .definition name="Confidence interval of asymptotic level" related="def-confidence-interval"}

Let $(E,(\Pr_\theta)_{\theta\in\Theta})$ be a model with $\Theta\subseteq\mathbb{R}$, and $\alpha\in(0,1)$. A random interval $I_n$, computed from $X_1,\dots,X_n$ by a formula that does not involve $\theta$, is a *confidence interval of asymptotic level $1-\alpha$* if

$$
\liminf_{n\to\infty}\Pr_\theta\bigl(\theta\in I_n\bigr)\ge1-\alpha\qquad\text{for every }\theta\in\Theta .
$$

:::

The starting point is always an asymptotically normal estimator, $\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}N(0,\sigma^2(\theta))$. Then
$$\Pr_\theta\Bigl(|\hat\theta_n-\theta|\le\frac{q_{\alpha/2}\,\sigma(\theta)}{\sqrt n}\Bigr)\to1-\alpha,$$
but the interval $\hat\theta_n\pm q_{\alpha/2}\sigma(\theta)/\sqrt n$ is not allowed, because its endpoints involve the unknown $\theta$. There are three standard remedies.

::: {#prp-three-asymptotic-intervals .proposition name="Three ways to remove the unknown variance"}

Suppose $\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}N(0,\sigma^2(\theta))$ under every $\Pr_\theta$, with $\sigma(\theta)>0$.

1. *Conservative bound.* If $\sigma(\theta)\le\bar\sigma$ for all $\theta\in\Theta$, then $\hat\theta_n\pm q_{\alpha/2}\bar\sigma/\sqrt n$ has asymptotic level $1-\alpha$.
2. *Solving for $\theta$.* The set $\bigl\{\theta\in\Theta:\ |\hat\theta_n-\theta|\le q_{\alpha/2}\,\sigma(\theta)/\sqrt n\bigr\}$ has asymptotic coverage exactly $1-\alpha$; when it is an interval, its endpoints are found by solving the inequality for $\theta$.
3. *Plug-in.* If $\sigma$ is continuous, then $\hat\theta_n\pm q_{\alpha/2}\,\sigma(\hat\theta_n)/\sqrt n$ has asymptotic coverage exactly $1-\alpha$.

:::

::: {.proof}

1. Part 1: the interval contains the one with $\sigma(\theta)$ in place of $\bar\sigma$, whose coverage tends to $1-\alpha$.

2. Part 2: the event "$\theta$ lies in the set" is literally the event $|\sqrt n(\hat\theta_n-\theta)/\sigma(\theta)|\le q_{\alpha/2}$, whose probability tends to $\Pr(|Z|\le q_{\alpha/2})=1-\alpha$. The set is computed from the data alone.

3. Part 3: an asymptotically normal estimator is consistent (@prp-asymptotically-normal-consistent), so $\sigma(\hat\theta_n)\xrightarrow{P}\sigma(\theta)$ by continuous mapping (@thm-continuous-mapping), hence $\sigma(\theta)/\sigma(\hat\theta_n)\xrightarrow{P}1$.

4. By Slutsky's theorem (@thm-slutsky),
   $$\sqrt n\,\frac{\hat\theta_n-\theta}{\sigma(\hat\theta_n)}=\frac{\sigma(\theta)}{\sigma(\hat\theta_n)}\cdot\sqrt n\,\frac{\hat\theta_n-\theta}{\sigma(\theta)}\xrightarrow{d}N(0,1),$$
   and the plug-in interval is the event that this quantity lies in $[-q_{\alpha/2},q_{\alpha/2}]$. The normal CDF is continuous, so the probability tends to $1-\alpha$.

:::

::: {#exm-proportion-three-intervals .example name="Three intervals for a proportion" related="prp-conservative-proportion-interval"}

In a survey, $248$ of $n=400$ people answer yes. Model the answers as $\operatorname{Ber}(p)$; then $\hat p=\bar X_n=0.62$ and $\sigma^2(p)=p(1-p)$. With $\alpha=0.05$:

1. *Conservative:* $p(1-p)\le1/4$, so $\hat p\pm\dfrac{1.96}{2\sqrt{400}}=0.62\pm0.049$, that is $[0.571,\,0.669]$.
2. *Solving:* $|\hat p-p|\le1.96\sqrt{p(1-p)/400}$ is, after squaring, the quadratic inequality $(1+q^2/n)p^2-(2\hat p+q^2/n)p+\hat p^2\le0$ with $q=1.96$. Its roots give $[0.572,\,0.666]$ (the *Wilson interval*).
3. *Plug-in:* $0.62\pm1.96\sqrt{0.62\cdot0.38/400}=0.62\pm0.048$, that is $[0.572,\,0.668]$.

For $n$ this large and $\hat p$ away from $0$ and $1$ the three agree closely. The conservative interval is the widest because it uses the worst case $p=1/2$.

:::

::: {#exm-exponential-rate-intervals .example name="Intervals for an exponential rate"}

By @exm-delta-method-exponential, $\hat\lambda=1/\bar T_n$ has asymptotic variance $\lambda^2$. Suppose $n=100$ waiting times average $\bar T_n=2.5$, so $\hat\lambda=0.4$ and, with $c=q_{0.025}/\sqrt n=0.196$:

1. *Solving* $|\hat\lambda-\lambda|\le c\lambda$ gives $\hat\lambda/(1+c)\le\lambda\le\hat\lambda/(1-c)$, that is $[0.334,\,0.498]$.
2. *Plug-in:* $\hat\lambda(1\pm c)$, that is $[0.322,\,0.478]$.

No conservative bound exists here, since $\sigma(\lambda)=\lambda$ is unbounded on $(0,\infty)$.

:::

::: {#rmk-hoeffding-interval .remark name="A non-asymptotic interval from Hoeffding's inequality"}

The intervals above are justified only as $n\to\infty$. If the observations are bounded, $a\le X_i\le b$, Hoeffding's inequality (@thm-hoeffding-inequality, applied to $\pm(X_i-\mu)$ and combined by a union bound) gives for every $n$ and $\varepsilon>0$
$$\Pr\bigl(|\bar X_n-\mu|\ge\varepsilon\bigr)\le2\exp\Bigl(-\frac{2n\varepsilon^2}{(b-a)^2}\Bigr).$$
Setting the right side equal to $\alpha$, the interval $\bar X_n\pm(b-a)\sqrt{\log(2/\alpha)/(2n)}$ has level at least $1-\alpha$ for *every* $n$. In the survey of @exm-proportion-three-intervals this is $0.62\pm0.068$, wider than the asymptotic intervals: the guarantee for small samples costs length.

:::
