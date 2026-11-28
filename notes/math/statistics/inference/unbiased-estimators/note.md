---
title: "Bias, Mean Squared Error and the Limits of Unbiasedness"
sources: [camib-st-2, camib-sts-1-q3]
requires: [math/probability/estimation/classical-estimation, math/probability/distributions/poisson-distribution]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 2 (estimation, bias and mean squared error, decision theory) and Example Sheet 1 (question 3), in our own wording. The definitions of bias, mean squared error and the bias–variance decomposition are in math/probability/estimation/classical-estimation and are not repeated. -->

Unbiasedness is the first property one asks of an estimator, but it is neither necessary nor always possible. Two examples show why, and a short decision-theoretic frame explains what is being compared.

::: {#exm-binomial-estimators .example name="Two estimators of a binomial proportion"}

Let $X\sim\mathrm{Bin}(n,\theta)$ with $n$ known.

1. The standard estimator $\hat\theta_U=X/n$ is unbiased with $\mathrm{MSE}(\hat\theta_U)=\theta(1-\theta)/n$.

2. Let $w=n/(n+2)$ and $\hat\theta_B=\dfrac{X+1}{n+2}=w\hat\theta_U+(1-w)\dfrac12$ (Laplace's estimator, the posterior mean for a flat prior). Then $\mathrm{bias}(\hat\theta_B)=(1-w)(\tfrac12-\theta)$ and
$$\mathrm{MSE}(\hat\theta_B)=w^2\frac{\theta(1-\theta)}n+(1-w)^2\Bigl(\frac12-\theta\Bigr)^2 .$$

3. For $n=10$ and $\theta=0.5$, $\mathrm{MSE}(\hat\theta_U)=0.025$ and $\mathrm{MSE}(\hat\theta_B)=0.0174$; for $\theta=0.9$ they are $0.0090$ and $0.0107$. So the biased estimator is better near $\theta=\tfrac12$ and worse near the ends: neither dominates, and the choice depends on where one believes $\theta$ to be.

:::

::: {#fig-unbiased-estimators-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=6cm,y=60cm]
\draw[->, muted] (0,0) -- (1.05,0) node[lab, right] {$\theta$};
\draw[->, muted] (0,0) -- (0,0.03);
\foreach \x in {0.5,1} \node[tick, below] at (\x,0) {$\x$};
\foreach \y in {0.01,0.02} \node[tick, left] at (0,\y) {$\y$};
\draw[emph, primary, domain=0:1, samples=50] plot (\x,{\x*(1-\x)/10});
\draw[emph, secondary, domain=0:1, samples=50] plot (\x,{(10/12)^2*\x*(1-\x)/10+(2/12)^2*(0.5-\x)^2});
\node[lab, primary] at (0.5,0.0275) {$\hat\theta_U$};
\node[lab, secondary] at (0.5,0.012) {$\hat\theta_B$};
\end{tikzpicture}
\end{center}
```

Mean squared errors of $\hat\theta_U$ and $\hat\theta_B$ for $n=10$. The biased estimator wins on a middle interval of $\theta$.

:::

::: {#prp-poisson-unbiased-unique .proposition name="An unbiased estimator that is useless"}

Let $X\sim\mathrm{Poisson}(\lambda)$ and $\theta=e^{-2\lambda}$. The only unbiased estimator of $\theta$ based on $X$ is $T(X)=(-1)^X$.

:::

::: {.proof}

1. If $g(X)$ is unbiased then $e^{-\lambda}\sum_{x\ge0}g(x)\lambda^x/x!=e^{-2\lambda}$ for all $\lambda>0$, that is
$$\sum_{x\ge0}g(x)\frac{\lambda^x}{x!}=e^{-\lambda}=\sum_{x\ge0}(-1)^x\frac{\lambda^x}{x!}.$$

2. Two power series that agree on an interval have the same coefficients, so $g(x)=(-1)^x$ for every $x$.

:::

::: {#rmk-unbiased-poisson-absurd .remark name="Why this is absurd"}

The estimator $(-1)^X$ takes only the values $\pm1$, while the parameter $e^{-2\lambda}$ lies in $(0,1)$; for $X$ odd the estimate is negative. Insisting on unbiasedness forces a nonsensical estimator, so unbiasedness is often too strong a requirement.

:::

::: {#def-risk-function .definition name="Decision rule, loss and risk"}

A *decision rule* is a map $d:\mathcal X\to D$ from data to a set $D$ of decisions (for point estimation $D=\Theta$). A *loss function* $L:\Theta\times D\to\mathbb R$ measures the cost of a decision, and the *risk* of $d$ is
$$R(\theta,d)=E_\theta\bigl\{L(\theta,d(X))\bigr\}.$$
The mean squared error is the risk for the quadratic loss $L(\theta,a)=(\theta-a)^2$. A rule $\hat d$ is *minimax* if it minimises $\max_{\theta\in\Theta}R(\theta,d)$ over rules $d$.

:::

::: {#rmk-risk-curves .remark name="Comparing risk curves"}

Risk is a function of $\theta$, so two rules are generally compared by a whole curve, as in @fig-unbiased-estimators-1. A rule is *better* than another only if its risk is nowhere larger and somewhere smaller. Restricting to a class (unbiased rules, giving UMVU estimators in @def-umvu) or to a summary of the curve (its maximum, giving minimax rules; or its prior average, giving Bayes rules) is what makes an "optimal" rule possible.

:::
