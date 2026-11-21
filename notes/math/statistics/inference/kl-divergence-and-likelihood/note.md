---
title: "Total Variation, KL Divergence and the Likelihood Principle"
sources: [mit18650-3]
requires: [math/statistics/inference/statistical-models, math/probability/information-theory/entropy]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 3 (total variation distance, Kullback-Leibler divergence, maximum likelihood as minimising an estimated divergence, likelihood of discrete and continuous models), in our own wording; proofs written out in steps, the numerical examples are our own. -->

An estimator $\hat\theta$ is good when the fitted distribution $\Pr_{\hat\theta}$ is close to the true one $\Pr_{\theta^*}$. To make "close" precise we need a way of comparing two distributions. The obvious distance cannot be estimated from data; a less obvious one can, and minimising its estimate is exactly maximum likelihood.

::: {#def-total-variation .definition name="Total variation distance"}

The *total variation distance* between two probability distributions $\Pr$ and $\mathrm Q$ on the same sample space $E$ is the largest difference in the probability they give to an event:

$$
\operatorname{TV}(\Pr,\mathrm Q)=\sup_{A\subseteq E}\bigl|\Pr(A)-\mathrm Q(A)\bigr| .
$$

:::

::: {#prp-total-variation-formula .proposition name="Total variation from mass or density functions"}

If $\Pr$ and $\mathrm Q$ have mass functions $p,q$ on a countable $E$, or densities $p,q$ on $E\subseteq\mathbb{R}^d$, then

$$
\operatorname{TV}(\Pr,\mathrm Q)=\frac12\sum_{x\in E}|p(x)-q(x)|\qquad\text{or}\qquad\operatorname{TV}(\Pr,\mathrm Q)=\frac12\int_E|p(x)-q(x)|\,dx,
$$

and the supremum is attained at $A^*=\{x:p(x)>q(x)\}$. Consequently $\operatorname{TV}$ is a metric on distributions: it is symmetric, non-negative, zero only when $\Pr=\mathrm Q$, and satisfies the triangle inequality; and $0\le\operatorname{TV}\le1$.

:::

::: {.proof}

1. We write sums; for densities replace them by integrals. Let $A^*=\{p>q\}$ and $B^*=E\setminus A^*=\{p\le q\}$.

2. Since $\sum_xp(x)=\sum_xq(x)=1$, the total excess on $A^*$ equals the total deficit on $B^*$: $\sum_{A^*}(p-q)=\sum_{B^*}(q-p)$. Their sum is $\sum_x|p-q|$, so each equals $\frac12\sum_x|p-q|$.

3. For any event $A$, $\Pr(A)-\mathrm Q(A)=\sum_{A}(p-q)\le\sum_{A\cap A^*}(p-q)\le\sum_{A^*}(p-q)$, because dropping the points where $p-q\le0$ and adding points where $p-q>0$ can only increase the sum. Likewise $\mathrm Q(A)-\Pr(A)\le\sum_{B^*}(q-p)$.

4. So $|\Pr(A)-\mathrm Q(A)|\le\frac12\sum_x|p-q|$ for every $A$, with equality for $A=A^*$. This proves the formula.

5. The metric properties follow from the formula: $|p-q|=|q-p|$; the sum is zero only if $p=q$ everywhere (almost everywhere for densities), that is $\Pr=\mathrm Q$; and $|p-r|\le|p-q|+|q-r|$ pointwise gives the triangle inequality. Finally $\frac12\sum|p-q|\le\frac12\sum(p+q)=1$.

:::

The trouble with total variation as a target for estimation is that $\operatorname{TV}(\Pr_\theta,\Pr_{\theta^*})$ depends on $\theta^*$ through $|p_\theta(x)-p_{\theta^*}(x)|$, and there is no simple way to estimate this from a sample of $\Pr_{\theta^*}$. The next divergence avoids the absolute value.

::: {#def-kl-divergence .definition name="Kullback–Leibler divergence" generalizes="def-relative-entropy"}

The *Kullback–Leibler (KL) divergence* of $\mathrm Q$ from $\Pr$, for mass functions or densities $p,q$, is

$$
\operatorname{KL}(\Pr,\mathrm Q)=\sum_{x\in E}p(x)\log\frac{p(x)}{q(x)}\qquad\text{or}\qquad\operatorname{KL}(\Pr,\mathrm Q)=\int_Ep(x)\log\frac{p(x)}{q(x)}\,dx,
$$

with the conventions $0\log(0/q)=0$ and $\operatorname{KL}=+\infty$ if $q(x)=0<p(x)$ on a set of positive $\Pr$-probability. Equivalently $\operatorname{KL}(\Pr,\mathrm Q)=E_{\Pr}\bigl[\log\bigl(p(X)/q(X)\bigr)\bigr]$. With $\log_2$ and mass functions this is the relative entropy $D(p\,\|\,q)$ of information theory.

:::

::: {#prp-kl-properties .proposition name="KL is a divergence, not a distance"}

1. $\operatorname{KL}(\Pr,\mathrm Q)\ge0$, with equality if and only if $\Pr=\mathrm Q$.
2. In general $\operatorname{KL}(\Pr,\mathrm Q)\ne\operatorname{KL}(\mathrm Q,\Pr)$, and the triangle inequality can fail.

:::

::: {.proof}

1. Assume $\operatorname{KL}(\Pr,\mathrm Q)<\infty$ (otherwise part 1 is clear) and let $S=\{p>0\}$. Since $\log$ is concave, Jensen's inequality gives
   $$-\operatorname{KL}(\Pr,\mathrm Q)=E_{\Pr}\Bigl[\log\frac{q(X)}{p(X)}\Bigr]\le\log E_{\Pr}\Bigl[\frac{q(X)}{p(X)}\Bigr]=\log\sum_{x\in S}q(x)\le\log1=0 .$$

2. Equality in Jensen for the strictly concave $\log$ forces $q(X)/p(X)$ to be constant on $S$, and equality in the last step forces $\sum_Sq=1$. Together $q=p$ on $S$ and $q=0$ off $S$, so $\Pr=\mathrm Q$. Conversely $\operatorname{KL}(\Pr,\Pr)=0$.

3. For part 2, with $\log=\ln$: $\operatorname{KL}(\operatorname{Ber}(0.5),\operatorname{Ber}(0.25))=\tfrac12\ln\tfrac43\approx0.144$ while $\operatorname{KL}(\operatorname{Ber}(0.25),\operatorname{Ber}(0.5))\approx0.131$. For the triangle inequality, $\operatorname{KL}(\operatorname{Ber}(0.1),\operatorname{Ber}(0.9))\approx1.758$ exceeds $\operatorname{KL}(\operatorname{Ber}(0.1),\operatorname{Ber}(0.5))+\operatorname{KL}(\operatorname{Ber}(0.5),\operatorname{Ber}(0.9))\approx0.879$.

:::

From now on $\log=\ln$. The asymmetry is what makes KL estimable. Fix the first argument at the truth:

$$
\operatorname{KL}(\Pr_{\theta^*},\Pr_\theta)=E_{\theta^*}\bigl[\log p_{\theta^*}(X)\bigr]-E_{\theta^*}\bigl[\log p_\theta(X)\bigr].
$$

The first term does not depend on $\theta$. The second is an expectation under the true distribution, which the law of large numbers lets us replace by a sample average.

::: {#prp-mle-minimises-estimated-kl .proposition name="Maximum likelihood minimises an estimate of KL" related="def-maximum-likelihood"}

Let $X_1,\dots,X_n$ be independent with mass function or density $p_{\theta^*}$ in a model $(p_\theta)_{\theta\in\Theta}$, and define the estimate
$$\widehat{\operatorname{KL}}_n(\theta)=C-\frac1n\sum_{i=1}^n\log p_\theta(X_i),$$
where $C$ is any constant not depending on $\theta$. Then:

1. if $E_{\theta^*}|\log p_\theta(X)|<\infty$, $\widehat{\operatorname{KL}}_n(\theta)\to\operatorname{KL}(\Pr_{\theta^*},\Pr_\theta)$ almost surely when $C=E_{\theta^*}[\log p_{\theta^*}(X)]$;
2. for every $C$, $\theta$ minimises $\widehat{\operatorname{KL}}_n$ if and only if it maximises the *likelihood* $L_n(X_1,\dots,X_n;\theta)=\prod_{i=1}^np_\theta(X_i)$.

So the *maximum likelihood estimator*
$$\hat\theta_n^{\mathrm{MLE}}=\operatorname*{argmax}_{\theta\in\Theta}L_n(X_1,\dots,X_n;\theta)=\operatorname*{argmax}_{\theta\in\Theta}\sum_{i=1}^n\log p_\theta(X_i)$$
(when it exists) is the minimiser of the estimated divergence from the truth.

:::

::: {.proof}

1. Part 1 is the strong law of large numbers applied to the independent, integrable variables $\log p_\theta(X_i)$.

2. For part 2, $-\frac1n\sum_i\log p_\theta(X_i)$ is a strictly decreasing function of $\sum_i\log p_\theta(X_i)=\log L_n(\theta)$, and $\log$ is strictly increasing, so the minimisers of $\widehat{\operatorname{KL}}_n$, the maximisers of $\log L_n$ and the maximisers of $L_n$ coincide.

:::

By @prp-kl-properties the true parameter is the unique minimiser of $\theta\mapsto\operatorname{KL}(\Pr_{\theta^*},\Pr_\theta)$ exactly when the model is identified (@def-identifiable). This is the heuristic reason why maximum likelihood is consistent; making it rigorous needs the estimated curves to converge uniformly in $\theta$.

::: {#exm-mle-bernoulli-poisson .example name="Bernoulli and Poisson"}

1. *Bernoulli.* $L_n(p)=p^{S}(1-p)^{n-S}$ with $S=\sum_iX_i$. The log-likelihood $S\log p+(n-S)\log(1-p)$ has derivative $S/p-(n-S)/(1-p)$, which vanishes at $p=S/n$; the second derivative $-S/p^2-(n-S)/(1-p)^2$ is negative, so $\hat p^{\mathrm{MLE}}=\bar X_n$ (if $S=0$ or $S=n$ the maximum is at the boundary value $0$ or $1$, which the formula still gives).
2. *Poisson.* $L_n(\lambda)=e^{-n\lambda}\lambda^{S}/\prod_iX_i!$. The log-likelihood $-n\lambda+S\log\lambda+\text{const}$ has derivative $-n+S/\lambda$ and is strictly concave, so $\hat\lambda^{\mathrm{MLE}}=\bar X_n$ (for $S>0$).

For the Gaussian model the MLE is $(\bar X_n,\hat\sigma^2)$ with $\hat\sigma^2=\frac1n\sum_i(X_i-\bar X_n)^2$ (@exm-ml-normal).

:::

::: {#rmk-concave-log-likelihood .remark name="Concave log-likelihoods"}

In both examples the log-likelihood is strictly concave in the parameter: the second derivative (for vector parameters, the Hessian) is negative (negative definite). A strictly concave function has at most one maximiser, and if one exists it is the unique solution of $\nabla\log L_n(\theta)=0$. When there is no closed form, such a maximiser can be found reliably by convex optimisation methods (@sec-math-optimization-algorithms-newtons-method-for-minimization). Without concavity, numerical methods may stop at a local maximum.

:::
