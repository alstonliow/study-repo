---
title: "Statistical Models and Estimators"
sources: [mit18650-2]
requires: [math/probability/estimation/classical-estimation]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 2 (statistical models, identification, estimators and their properties), in our own wording; the examples and the proof are our own. -->

Probability starts from a known distribution and computes what the data will look like. Statistics goes the other way: from data $X_1,\dots,X_n$, independent copies of a random variable $X$, it tries to learn the distribution of $X$. A *model* restricts the candidate distributions to a family indexed by a few numbers, so that learning the distribution means learning those numbers.

::: {#def-statistical-model .definition name="Statistical model"}

Let the data be $X_1,\dots,X_n$, independent with a common distribution $\Pr$ on a sample space $E$ (usually $E\subseteq\mathbb{R}$ or $\mathbb{R}^d$). A *statistical model* for this experiment is a pair
$$\bigl(E,\ (\Pr_\theta)_{\theta\in\Theta}\bigr),$$
where $(\Pr_\theta)_{\theta\in\Theta}$ is a family of probability distributions on $E$ and $\Theta$ is the *parameter set*.

1. The model is *well specified* if $\Pr=\Pr_{\theta^*}$ for some $\theta^*\in\Theta$, the (unknown) *true parameter*.
2. The model is *parametric* if $\Theta\subseteq\mathbb{R}^d$ for some $d\ge1$.

We write $E_\theta$, $\mathrm{Var}_\theta$ for expectations and variances when $X\sim\Pr_\theta$.

:::

::: {#exm-statistical-models .example name="Four parametric models"}

1. Yes/no answers: $\bigl(\{0,1\},(\operatorname{Ber}(p))_{p\in(0,1)}\bigr)$.
2. Waiting times: $\bigl((0,\infty),(\operatorname{Exp}(\lambda))_{\lambda>0}\bigr)$.
3. Counts: $\bigl(\{0,1,2,\dots\},(\operatorname{Poisson}(\lambda))_{\lambda>0}\bigr)$.
4. Measurements with noise: $\bigl(\mathbb{R},(N(\mu,\sigma^2))_{(\mu,\sigma^2)\in\mathbb{R}\times(0,\infty)}\bigr)$, a parameter of dimension $d=2$.

Without a model, a count taking values $1,\dots,6$ or "at least $7$" needs seven probabilities (six free ones); the Poisson model needs one number.

:::

::: {#def-identifiable .definition name="Identifiable parameter"}

The parameter of a model $(E,(\Pr_\theta)_{\theta\in\Theta})$ is *identified* (identifiable) if the map $\theta\mapsto\Pr_\theta$ is one to one:
$$\theta\ne\theta'\implies\Pr_\theta\ne\Pr_{\theta'} .$$

:::

If two parameters give the same distribution, no amount of data can tell them apart, so identifiability is the minimum requirement for estimating $\theta$.

::: {#exm-identifiability-signs .example name="Observing only signs"}

Let $Y_1,\dots,Y_n$ be independent $N(\mu,\sigma^2)$, but suppose we only observe $X_i=\mathbf 1\{Y_i\ge0\}$. Then $X_i\sim\operatorname{Ber}(q)$ with
$$q=\Pr(Y_i\ge0)=\Pr\Bigl(\frac{Y_i-\mu}{\sigma}\ge-\frac\mu\sigma\Bigr)=\Phi\Bigl(\frac\mu\sigma\Bigr).$$
The distribution of the data depends on $(\mu,\sigma^2)$ only through $\mu/\sigma$: $(\mu,\sigma^2)=(1,1)$ and $(2,4)$ give the same law. So $(\mu,\sigma^2)$ is not identified, but $\mu/\sigma$ is, since $\Phi$ is strictly increasing.

:::

An *estimator* of $\theta$ is a statistic, that is a function of the data alone, whose formula does not involve $\theta$ (@def-estimator-properties). Besides bias, consistency and mean squared error (the *quadratic risk*; @prp-mse-bias-variance), two asymptotic properties matter most in what follows.

::: {#def-asymptotic-normality .definition name="Strong consistency, asymptotic normality" related="def-estimator-properties"}

Let $\hat\theta_n$ be an estimator of $\theta\in\Theta\subseteq\mathbb{R}^d$ based on $n$ observations.

1. $\hat\theta_n$ is *weakly consistent* if $\hat\theta_n\to\theta$ in probability, and *strongly consistent* if $\hat\theta_n\to\theta$ almost surely, under $\Pr_\theta$ for every $\theta\in\Theta$.
2. $\hat\theta_n$ is *asymptotically normal* if for every $\theta$ there is a covariance matrix $\Sigma(\theta)$, the *asymptotic covariance* (for $d=1$ the *asymptotic variance* $\sigma^2(\theta)$), with
   $$\sqrt n\,(\hat\theta_n-\theta)\xrightarrow{d}N_d\bigl(0,\Sigma(\theta)\bigr)\qquad\text{under }\Pr_\theta .$$

:::

::: {#prp-asymptotically-normal-consistent .proposition name="Asymptotic normality implies consistency"}

An asymptotically normal estimator is weakly consistent.

:::

::: {.proof}

1. Fix $\theta$ and $\varepsilon>0$, and let $Z\sim N_d(0,\Sigma(\theta))$. Take $d=1$ first.

2. For any $K>0$ and all $n$ with $\sqrt n\,\varepsilon>K$,
   $$\Pr_\theta\bigl(|\hat\theta_n-\theta|>\varepsilon\bigr)=\Pr_\theta\bigl(|\sqrt n(\hat\theta_n-\theta)|>\sqrt n\,\varepsilon\bigr)\le\Pr_\theta\bigl(|\sqrt n(\hat\theta_n-\theta)|>K\bigr).$$

3. By convergence in distribution (the normal CDF is continuous) the right side tends to $\Pr(|Z|>K)$. Hence $\limsup_n\Pr_\theta(|\hat\theta_n-\theta|>\varepsilon)\le\Pr(|Z|>K)$ for every $K$.

4. Letting $K\to\infty$ gives $0$. For $d>1$ apply this to each coordinate, which is asymptotically normal with the corresponding diagonal entry of $\Sigma(\theta)$ as variance, and use $\Pr(\|v\|>\varepsilon)\le\sum_j\Pr(|v_j|>\varepsilon/\sqrt d)$.

:::

::: {#exm-sample-mean-asymptotics .example name="The sample proportion"}

In the Bernoulli model the sample mean $\bar X_n$ is unbiased, strongly consistent by the strong law of large numbers, and asymptotically normal with asymptotic variance $p(1-p)$ by the central limit theorem (@thm-central-limit-theorem). Its quadratic risk is $p(1-p)/n$.

:::
