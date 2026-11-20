---
title: "The Bootstrap"
sources: [mit1805-24]
requires: [math/statistics/frequentist/confidence-intervals]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Class 24, in our own wording; proofs written out in steps. -->

The intervals of @thm-normal-confidence-intervals need the distribution of a statistic around the true parameter. When that distribution is unknown, the bootstrap estimates it by simulation, using the data themselves in place of the unknown population.

::: {#def-empirical-distribution .definition name="Empirical distribution"}

The *empirical distribution* of data $x_1,\dots,x_n$ is the discrete distribution that gives probability $1/n$ to each data point (a value that occurs $j$ times gets $j/n$). A *resample* is a sample of size $n$ drawn from it, that is, drawn from the data *with replacement*; quantities computed from a resample are marked with a star: $x_1^*,\dots,x_n^*$ and $\bar x^*$.

:::

::: {#rmk-bootstrap-principle .remark name="The bootstrap principle"}

Let $\hat\theta$ be a statistic estimating a parameter $\theta$ of the population, and $\delta=\hat\theta-\theta$. The bootstrap principle is the approximation
$$\text{distribution of }\delta^*=\hat\theta^*-\hat\theta\ \approx\ \text{distribution of }\delta=\hat\theta-\theta,$$
where $\hat\theta^*$ is the statistic computed from a resample. The empirical distribution plays the role of the population, and $\hat\theta$ the role of $\theta$. The resample has the same size $n$ as the data because the spread of $\delta$ depends on $n$. The approximation is about the *variation* of the statistic; $\hat\theta^*$ is centred near $\hat\theta$, not near $\theta$, so the bootstrap does not improve the estimate itself.

:::

::: {#def-empirical-bootstrap-interval .definition name="Empirical bootstrap confidence interval"}

Given data $x_1,\dots,x_n$, a statistic $\hat\theta$, a number $B$ of resamples and a level $1-\alpha$:

1. compute $\hat\theta$ from the data;
2. for $b=1,\dots,B$, draw a resample, compute $\hat\theta^*_b$ and $\delta^*_b=\hat\theta^*_b-\hat\theta$;
3. let $q_{\alpha/2}$ and $q_{1-\alpha/2}$ be the $\alpha/2$- and $1-\alpha/2$-quantiles of $\delta^*_1,\dots,\delta^*_B$;
4. report the interval
$$\bigl[\hat\theta-q_{1-\alpha/2},\ \hat\theta-q_{\alpha/2}\bigr].$$

:::

```{=latex}
\begin{algorithm}
\caption{Empirical bootstrap confidence interval}
\begin{algorithmic}
\INPUT Data $x_1,\dots,x_n$; a statistic $\hat\theta(\cdot)$; resamples $B$; level $1-\alpha$
\OUTPUT An approximate $1-\alpha$ confidence interval for $\theta$
\STATE $\hat\theta\gets\hat\theta(x_1,\dots,x_n)$
\FOR{$b=1$ \TO $B$}
    \STATE draw $x_1^*,\dots,x_n^*$ uniformly from $\{x_1,\dots,x_n\}$ with replacement
    \STATE $\delta^*_b\gets\hat\theta(x_1^*,\dots,x_n^*)-\hat\theta$
\ENDFOR
\STATE $q_{\alpha/2},q_{1-\alpha/2}\gets$ the $\alpha/2$- and $(1-\alpha/2)$-quantiles of $\delta^*_1,\dots,\delta^*_B$
\RETURN $[\hat\theta-q_{1-\alpha/2},\ \hat\theta-q_{\alpha/2}]$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-bootstrap-1 .remark editor="TODO: add a static figure (histogram of the bootstrap differences of @exm-bootstrap-mean with the two quantiles marked); deferred to save tokens in the 18.05 round."}

A figure for this algorithm is still to be drawn.

:::

::: {#prp-bootstrap-interval-derivation .proposition name="Why the endpoints are reversed"}

If $\delta=\hat\theta-\theta$ had exactly the quantiles $q_{\alpha/2}$ and $q_{1-\alpha/2}$, the interval of @def-empirical-bootstrap-interval would contain $\theta$ with probability $1-\alpha$.

:::

::: {.proof}

1. By the definition of quantiles, $\Pr(q_{\alpha/2}\le\hat\theta-\theta\le q_{1-\alpha/2})=1-\alpha$.

2. Subtract $\hat\theta$ and multiply by $-1$, which reverses the inequalities: $\hat\theta-q_{1-\alpha/2}\le\theta\le\hat\theta-q_{\alpha/2}$.

3. The bootstrap principle replaces the unknown quantiles of $\delta$ by those of $\delta^*$, so the interval is approximate.

:::

::: {#exm-bootstrap-mean .example name="An interval for a mean"}

<!-- Numbers from a seeded simulation (numpy default_rng(1805), B = 1000). -->

The data $30,37,36,43,42,43,43,46,41,42$ have $\bar x=40.3$. In one run of $B=1000$ resamples, the $0.1$- and $0.9$-quantiles of $\delta^*=\bar x^*-\bar x$ were $-1.9$ and $1.8$, so the $80\%$ bootstrap interval for the mean is
$$[40.3-1.8,\ 40.3+1.9]=[38.5,\ 42.2].$$
Another run gives slightly different numbers; larger $B$ reduces this simulation noise but not the error of the bootstrap principle itself, which depends on $n$.

:::

::: {#def-parametric-bootstrap .definition name="Parametric bootstrap"}

If the data are assumed to come from a family $f(x\mid\theta)$, the *parametric bootstrap* replaces step 2 of @def-empirical-bootstrap-interval by: draw $x_1^*,\dots,x_n^*$ independently from $f(x\mid\hat\theta)$. The rest is the same.

:::

::: {#rmk-bootstrap-other-statistics .remark name="Other statistics"}

Nothing in the method is specific to the mean: the same steps give intervals for a median, a trimmed mean, a correlation or a ratio, for which no formula like @thm-normal-confidence-intervals exists. The bootstrap needs a reasonably large sample, since the empirical distribution must resemble the population; it also handles extreme statistics such as the maximum poorly.

:::
