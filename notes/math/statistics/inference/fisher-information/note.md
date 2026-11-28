---
title: "Fisher Information and Asymptotics of the MLE"
sources: [mit18650-3, camii-sms-2-q7, camii-sms-2-q8, camii-sms-3-q3]
requires: [math/statistics/inference/kl-divergence-and-likelihood, math/statistics/inference/slutsky-and-delta-method]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 3 (Fisher information, asymptotic normality of the maximum likelihood estimator), in our own wording. The proof of the two score identities, the one-parameter proof of the theorem (under stated assumptions), the Bernoulli example and the remark on a moving support are our own. -->

Maximum likelihood (@prp-mle-minimises-estimated-kl) gives estimators; this note says how accurate they are. The answer is governed by the curvature of the log-likelihood at the true parameter: a sharply peaked log-likelihood pins the parameter down well.

::: {#def-fisher-information .definition name="Score, Fisher information"}

Let $(p_\theta)_{\theta\in\Theta}$, $\Theta\subseteq\mathbb{R}^d$ open, be a model of mass functions or densities, and let
$$\ell(\theta)=\log p_\theta(X)$$
be the log-likelihood of one observation $X\sim\Pr_\theta$, assumed twice differentiable in $\theta$. Its gradient $\nabla\ell(\theta)$ is the *score*. The *Fisher information* is the $d\times d$ covariance matrix of the score,

$$
I(\theta)=E_\theta\bigl[\nabla\ell(\theta)\nabla\ell(\theta)^{\mathsf T}\bigr]-E_\theta\bigl[\nabla\ell(\theta)\bigr]E_\theta\bigl[\nabla\ell(\theta)\bigr]^{\mathsf T}.
$$

For $d=1$, $I(\theta)=\mathrm{Var}_\theta\bigl(\ell'(\theta)\bigr)$.

:::

::: {#prp-score-identities .proposition name="The score has mean zero; information is expected curvature"}

Suppose the support $\{x:p_\theta(x)>0\}$ does not depend on $\theta$ and that $\int p_\theta(x)\,dx$ (or the sum) may be differentiated twice in $\theta$ under the integral sign. Then

$$
E_\theta\bigl[\nabla\ell(\theta)\bigr]=0,\qquad I(\theta)=-E_\theta\bigl[\nabla^2\ell(\theta)\bigr].
$$

:::

::: {.proof}

1. We give the case $d=1$ with densities; partial derivatives handle $d>1$ entry by entry, and sums replace integrals for mass functions. Write $p=p_\theta(x)$ and primes for $\partial/\partial\theta$.

2. Since $\ell'=p'/p$ on the support, $E_\theta[\ell'(\theta)]=\int p'\,dx=\dfrac{d}{d\theta}\int p\,dx=\dfrac{d}{d\theta}1=0$.

3. Differentiate $\ell'=p'/p$ once more: $\ell''=\dfrac{p''}{p}-\Bigl(\dfrac{p'}{p}\Bigr)^2=\dfrac{p''}{p}-(\ell')^2$.

4. Take expectations. As in step 2, $E_\theta[p''/p]=\int p''\,dx=\dfrac{d^2}{d\theta^2}1=0$. Hence $E_\theta[\ell'']=-E_\theta[(\ell')^2]=-\mathrm{Var}_\theta(\ell')$, using step 2 for the last equality.

:::

::: {#exm-fisher-information-bernoulli .example name="Bernoulli"}

For $X\sim\operatorname{Ber}(p)$, $\ell(p)=X\log p+(1-X)\log(1-p)$, so
$$\ell'(p)=\frac Xp-\frac{1-X}{1-p},\qquad \ell''(p)=-\frac X{p^2}-\frac{1-X}{(1-p)^2}.$$
Then $E_p[\ell'(p)]=1-1=0$ and
$$I(p)=-E_p[\ell''(p)]=\frac1p+\frac1{1-p}=\frac1{p(1-p)} .$$
The information is smallest at $p=1/2$, where a single toss is least predictable. Its inverse $p(1-p)$ is the asymptotic variance of $\hat p=\bar X_n$ (@exm-sample-mean-asymptotics), as the next theorem predicts.

:::

::: {#thm-mle-asymptotic-normality .theorem name="Asymptotic normality of the MLE"}

Let $X_1,\dots,X_n$ be independent with distribution $\Pr_{\theta^*}$ in a model $(\Pr_\theta)_{\theta\in\Theta}$, $\Theta\subseteq\mathbb{R}^d$, and assume:

1. the parameter is identified;
2. the support of $\Pr_\theta$ does not depend on $\theta$;
3. $\theta^*$ is an interior point of $\Theta$;
4. $I(\theta)$ is invertible for $\theta$ near $\theta^*$;
5. further regularity conditions (smoothness of $\theta\mapsto p_\theta(x)$ with integrable bounds on its derivatives).

Then the MLE $\hat\theta_n$ is consistent and

$$
\sqrt n\,\bigl(\hat\theta_n-\theta^*\bigr)\xrightarrow{d}N_d\bigl(0,\ I(\theta^*)^{-1}\bigr)\qquad\text{under }\Pr_{\theta^*}.
$$

:::

::: {.proof}

We prove the normal limit for $d=1$, taking consistency ($\hat\theta_n\xrightarrow{P}\theta^*$) as given and assuming, as the regularity in condition 5, that $\ell$ is three times differentiable with $|\ell'''(\theta)|\le M(X)$ for $\theta$ near $\theta^*$, where $E_{\theta^*}[M(X)]<\infty$.

1. Write $\ell_n(\theta)=\sum_{i=1}^n\log p_\theta(X_i)$. By consistency and condition 3, with probability tending to $1$ the maximiser $\hat\theta_n$ is an interior point near $\theta^*$, so $\ell_n'(\hat\theta_n)=0$.

2. Expand $\ell_n'$ around $\theta^*$ by Taylor's theorem with the Lagrange remainder:
   $$0=\ell_n'(\hat\theta_n)=\ell_n'(\theta^*)+(\hat\theta_n-\theta^*)\ell_n''(\theta^*)+\tfrac12(\hat\theta_n-\theta^*)^2\ell_n'''(\tilde\theta_n)$$
   for some $\tilde\theta_n$ between $\theta^*$ and $\hat\theta_n$.

3. Solve for the error and scale:
   $$\sqrt n(\hat\theta_n-\theta^*)=\frac{n^{-1/2}\ell_n'(\theta^*)}{-n^{-1}\ell_n''(\theta^*)-\tfrac12(\hat\theta_n-\theta^*)\,n^{-1}\ell_n'''(\tilde\theta_n)} .$$

4. *Numerator.* $\ell_n'(\theta^*)$ is a sum of $n$ independent copies of the score, which has mean $0$ and variance $I(\theta^*)$ (@prp-score-identities). By the central limit theorem the numerator converges in distribution to $N(0,I(\theta^*))$.

5. *Denominator.* By the law of large numbers $-n^{-1}\ell_n''(\theta^*)\to-E_{\theta^*}[\ell''(\theta^*)]=I(\theta^*)$ in probability. The last term is at most $\tfrac12|\hat\theta_n-\theta^*|\cdot n^{-1}\sum_iM(X_i)$ in absolute value; the average converges to $E[M(X)]$ and $|\hat\theta_n-\theta^*|\xrightarrow{P}0$, so the term tends to $0$ in probability. The denominator therefore tends to $I(\theta^*)>0$.

6. By Slutsky's theorem (@thm-slutsky) the ratio converges in distribution to $W/I(\theta^*)$ with $W\sim N(0,I(\theta^*))$, which is $N(0,I(\theta^*)^{-1})$.

:::

So, to first order, $\hat\theta_n$ is normal with covariance $I(\theta^*)^{-1}/n$; $n\,I(\theta)$ is the information in the whole sample, because informations of independent observations add. No reasonable estimator does better: under similar conditions an unbiased estimator has variance at least $I(\theta)^{-1}/n$ (the Cramér–Rao bound), which is why the MLE is called *asymptotically efficient*.

::: {#exm-mle-moving-support .example name="When the support moves"}

Condition 2 is not a technicality. For $X_i$ uniform on $[0,\theta]$ the likelihood is $\theta^{-n}$ for $\theta\ge\max_iX_i$ and $0$ otherwise, so $\hat\theta_n=\max_iX_i$. Here $\theta-\hat\theta_n$ is of order $1/n$, not $1/\sqrt n$, and $n(\theta-\hat\theta_n)/\theta$ has an exponential, not a normal, limit. The score identities fail because differentiation under the integral sign is impossible when the range of integration depends on $\theta$.

:::
