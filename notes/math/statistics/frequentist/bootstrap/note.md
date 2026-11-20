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

::: {#fig-bootstrap-1}

```{=latex}
\begin{tikzpicture}
\draw[fill=neutral] (-2.750,0) rectangle (-2.475,0.024);
\draw[fill=neutral] (-2.475,0) rectangle (-2.200,0.048);
\draw[fill=neutral] (-2.200,0) rectangle (-1.925,0.096);
\draw[fill=neutral] (-1.925,0) rectangle (-1.650,0.132);
\draw[fill=neutral] (-1.650,0) rectangle (-1.375,0.240);
\draw[fill=neutral] (-1.375,0) rectangle (-1.100,0.516);
\draw[fill=neutral] (-1.100,0) rectangle (-0.825,0.792);
\draw[fill=primarySoft] (-0.825,0) rectangle (-0.550,0.948);
\draw[fill=primarySoft] (-0.550,0) rectangle (-0.275,1.296);
\draw[fill=primarySoft] (-0.275,0) rectangle (0.000,1.512);
\draw[fill=primarySoft] (0.000,0) rectangle (0.275,1.536);
\draw[fill=primarySoft] (0.275,0) rectangle (0.550,1.656);
\draw[fill=primarySoft] (0.550,0) rectangle (0.825,1.356);
\draw[fill=neutral] (0.825,0) rectangle (1.100,0.888);
\draw[fill=neutral] (1.100,0) rectangle (1.375,0.588);
\draw[fill=neutral] (1.375,0) rectangle (1.650,0.288);
\draw[fill=neutral] (1.650,0) rectangle (1.925,0.072);
\draw[fill=neutral] (1.925,0) rectangle (2.200,0.012);
\draw[->] (-3.47,0) -- (2.92,0) node[lab, right] {$\delta^*$};
\draw (-3.30,0) -- (-3.30,-0.08) node[lab, below] {$-6$};
\draw (-2.20,0) -- (-2.20,-0.08) node[lab, below] {$-4$};
\draw (-1.10,0) -- (-1.10,-0.08) node[lab, below] {$-2$};
\draw (0.00,0) -- (0.00,-0.08) node[lab, below] {$0$};
\draw (1.10,0) -- (1.10,-0.08) node[lab, below] {$2$};
\draw (2.20,0) -- (2.20,-0.08) node[lab, below] {$4$};
\draw[dashed, emph] (-1.045,0) -- (-1.045,2.01) node[lab, above] {$q_{0.1}=-1.9$};
\draw[dashed, emph] (0.990,0) -- (0.990,2.01) node[lab, above] {$q_{0.9}=1.8$};
\end{tikzpicture}
```

Histogram of the $1000$ bootstrap differences $\delta^*=\bar x^*-\bar x$ of @exm-bootstrap-mean (bins of width $0.5$). The dashed lines are the $0.1$- and $0.9$-quantiles; the $80\%$ interval is $[\bar x-q_{0.9},\ \bar x-q_{0.1}]=[38.5,\ 42.2]$.

:::

::: {#def-parametric-bootstrap .definition name="Parametric bootstrap"}

If the data are assumed to come from a family $f(x\mid\theta)$, the *parametric bootstrap* replaces step 2 of @def-empirical-bootstrap-interval by: draw $x_1^*,\dots,x_n^*$ independently from $f(x\mid\hat\theta)$. The rest is the same.

:::

::: {#rmk-bootstrap-other-statistics .remark name="Other statistics"}

Nothing in the method is specific to the mean: the same steps give intervals for a median, a trimmed mean, a correlation or a ratio, for which no formula like @thm-normal-confidence-intervals exists. The bootstrap needs a reasonably large sample, since the empirical distribution must resemble the population; it also handles extreme statistics such as the maximum poorly.

:::
