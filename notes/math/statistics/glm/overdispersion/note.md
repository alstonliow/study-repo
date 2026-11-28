---
title: "Overdispersion and Quasi-Likelihood"
sources: [camii-sm-12, camii-sm-17]
requires: [math/statistics/glm/glm-canonical-form]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 4.3.3 (overdispersion due to clustering) with the remarks on dispersion in 4.8.2, in our own wording; the variance computation is written out in steps. The numerical example is our own. -->

A one-parameter family such as the binomial or Poisson fixes the variance as a function of the mean. Real data often show more variation than that. This is *overdispersion* (less variation is *underdispersion*). A dispersion parameter $\phi$ lets the variance be $\phi V(\mu)/w$ while keeping the same mean, as in @prp-glm-dispersion-estimation.

::: {#prp-clustered-binomial .proposition name="Clustering inflates the binomial variance"}

Let there be $n/k$ clusters of $k$ observations, $Z_{ij}\mid\pi_i\sim\mathrm{Bernoulli}(\pi_i)$ independent within clusters, and let the cluster probabilities $\pi_i$ be iid with $E\pi_i=\pi$ and $\operatorname{Var}\pi_i=\tau^2\pi(1-\pi)$. The total $Y=\sum_{i,j}Z_{ij}$ has
$$E[Y]=n\pi,\qquad\operatorname{Var}(Y)=\phi\,n\pi(1-\pi),\qquad\phi=1+\tau^2(k-1).$$

:::

::: {.proof}

1. A cluster total $S_i=\sum_jZ_{ij}$ given $\pi_i$ is $\mathrm{Binomial}(k,\pi_i)$. Hence $E[S_i]=k\pi$.

2. By the law of total variance, $\operatorname{Var}(S_i)=E[k\pi_i(1-\pi_i)]+\operatorname{Var}(k\pi_i)$.

3. Since $E[\pi_i^2]=\operatorname{Var}\pi_i+\pi^2=\tau^2\pi(1-\pi)+\pi^2$, we get $E[\pi_i(1-\pi_i)]=\pi(1-\pi)(1-\tau^2)$, so $\operatorname{Var}(S_i)=k\pi(1-\pi)(1-\tau^2)+k^2\tau^2\pi(1-\pi)=k\pi(1-\pi)\{1+\tau^2(k-1)\}$.

4. The clusters are independent, so summing the $n/k$ variances gives $n\pi(1-\pi)\phi$.

:::

The mean is unchanged and the variance is inflated by the factor $\phi\ge1$, with $\phi=1$ for $k=1$ or $\tau=0$ (@fig-overdispersion-1). With $n=100$, $k=5$ and $\tau^2=0.2$ one gets $\phi=1.8$: ignoring the clustering understates the standard error of $\hat\pi$ by a factor $\sqrt{1.8}=1.34$.

::: {#fig-overdispersion-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm,y=1.1cm]
\draw[->, muted] (0,0) -- (10.5,0) node[lab, right] {cluster size $k$};
\draw[->, muted] (0,0) -- (0,3.2);
\foreach \x in {1,5,10} \node[tick, below] at (\x,0) {$\x$};
\foreach \y in {1,2,3} \node[tick, left] at (0,\y) {$\y$};
\draw[emph, primary] (1,1) -- (10,{1+0.1*9});
\draw[emph, hl] (1,1) -- (10,{1+0.2*9});
\draw[emph] (1,1) -- (10,{1+0.3*9});
\node[lab, right] at (10,1.9) {$\tau^2=0.1$};
\node[lab, right] at (10,2.8) {$\tau^2=0.2$};
\node[lab, right] at (10,3.7) {$\tau^2=0.3$};
\end{tikzpicture}
\end{center}
```

The dispersion factor $\phi=1+\tau^2(k-1)$ grows linearly with the cluster size $k$ and the between-cluster variability $\tau^2$.

:::

Practical consequences when $\phi>1$ is suspected:

1. Estimate $\phi$ by the Pearson-type $\hat\phi$ of @prp-glm-dispersion-estimation; $\hat\phi$ much larger than $1$ signals overdispersion. The point estimate $\hat\beta$ is unchanged, but its standard errors are multiplied by $\sqrt{\hat\phi}$ (the *quasi-binomial* or *quasi-Poisson* fit).
2. In tests by analysis of deviance the deviance is divided by $\hat\phi$ and compared with an $F$ rather than $\chi^2$ distribution (@thm-analysis-of-deviance).
3. For counts, a variance-stabilising transformation of the response is an alternative (@prp-variance-stabilising), at the cost of working on a transformed scale.
