---
title: "Classical Parameter Estimation"
sources: [mit6041-23, mit6041-24]
requires: [math/probability/continuous/modes-of-convergence]
status: draft
---

<!-- Added 2026-11-20 from MIT 6.041 (Fall 2010), Lectures 23 and 24, in our own wording; proofs written out in steps. -->

In the classical (frequentist) view the unknown $\theta$ is a fixed constant, not a random variable. The data $X=(X_1,\dots,X_n)$ have a distribution $p_X(x;\theta)$ or $f_X(x;\theta)$ for each value of $\theta$, and statements must hold whatever $\theta$ is.

::: {#def-estimator-properties .definition name="Estimator, bias, consistency"}

An *estimator* is a random variable $\hat\Theta_n=g(X_1,\dots,X_n)$. For each $\theta$:

1. its *bias* is $b_\theta(\hat\Theta_n)=E_\theta[\hat\Theta_n]-\theta$, and it is *unbiased* if the bias is $0$ for every $\theta$, *asymptotically unbiased* if the bias tends to $0$ as $n\to\infty$;
2. it is *consistent* if $\hat\Theta_n$ converges to $\theta$ in probability (@def-convergence-in-probability) for every $\theta$;
3. its *mean squared error* is $E_\theta[(\hat\Theta_n-\theta)^2]$.

:::

::: {#prp-mse-bias-variance .proposition name="Mean squared error = variance + bias squared"}

$$E_\theta\bigl[(\hat\Theta_n-\theta)^2\bigr]=\mathrm{Var}_\theta(\hat\Theta_n)+b_\theta(\hat\Theta_n)^2.$$

:::

::: {.proof}

1. Write $\hat\Theta_n-\theta=(\hat\Theta_n-E_\theta[\hat\Theta_n])+b_\theta$, a centred random variable plus a constant.

2. Square and take expectations. The cross term is $2b_\theta\,E_\theta[\hat\Theta_n-E_\theta[\hat\Theta_n]]=0$.

3. What remains is $\mathrm{Var}_\theta(\hat\Theta_n)+b_\theta^2$.

:::

::: {#fig-classical-estimation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.4,0) node[lab, right] {$\hat\theta$};
\draw[emph, domain=0:7, samples=80, smooth, variable=\x] plot ({\x}, {2.6*exp(-((\x-3.4)^2)/(2*1.1^2))/(1.1*sqrt(2*pi))});
\draw[hl, domain=1.8:7, samples=80, smooth, variable=\x] plot ({\x}, {2.6*exp(-((\x-4.4)^2)/(2*0.45^2))/(0.45*sqrt(2*pi))});
\draw[faint, dashed] (3.4,0) -- (3.4,2.4);
\draw (3.4,0) -- (3.4,-0.08) node[tick, below] {$\theta$};
\node[tick] at (1.5,0.75) {unbiased, wide};
\node[tick, text=accent] at (5.9,1.6) {biased, narrow};
\end{tikzpicture}
\end{center}
```

Sampling distributions of two estimators of $\theta$. One is unbiased but variable, the other biased but tight; the mean squared error, $\text{bias}^2+\text{variance}$, can favour either

:::

::: {#exm-sample-mean-estimator .example name="The sample mean" related="prp-sample-mean"}

If $X_1,\dots,X_n$ are independent with unknown mean $\theta$ and variance $\sigma^2$, the sample mean $M_n=(X_1+\dots+X_n)/n$ is unbiased, has mean squared error $\sigma^2/n$, and is consistent by the law of large numbers (@thm-law-of-large-numbers).

:::

::: {#def-maximum-likelihood .definition name="Maximum likelihood estimate"}

Given the observation $x$, the *likelihood* is $\theta\mapsto p_X(x;\theta)$ (or $f_X(x;\theta)$). The *maximum likelihood (ML) estimate* $\hat\theta_n$ is a value of $\theta$ that maximises it. For independent observations the likelihood is a product, and one maximises the *log-likelihood*
$$\sum_{i=1}^n\ln p_{X_i}(x_i;\theta)\quad\text{or}\quad\sum_{i=1}^n\ln f_{X_i}(x_i;\theta).$$

:::

::: {#fig-classical-estimation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.4,0) node[lab, right] {$p$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$L(p)$};
\draw[emph, domain=0:5, samples=100, smooth, variable=\x] plot ({\x}, {2.2*((\x/5)^3*(1-\x/5)^7)/(0.3^3*0.7^7)});
\draw[hl, dashed] (1.5,0) -- (1.5,2.2);
\draw (1.5,0) -- (1.5,-0.08) node[tick, below] {$0.3$};
\draw (5,0) -- (5,-0.08) node[tick, below] {$1$};
\end{tikzpicture}
\end{center}
```

The likelihood $L(p)=p^3(1-p)^7$ of $3$ heads in $10$ tosses, scaled to height $1$; it peaks at the maximum likelihood estimate $\hat p=0.3$

:::

::: {#rmk-ml-and-map .remark name="ML and MAP" related="def-map-lms-estimates"}

If $\theta$ is given a uniform prior over the set of its possible values, the posterior is proportional to the likelihood, so the ML estimate is the MAP estimate of that Bayesian model. ML is also *invariant*: the ML estimate of $h(\theta)$ for a one-to-one $h$ is $h(\hat\theta_n)$. Under mild conditions ML estimates are consistent and asymptotically normal.

:::

::: {#exm-ml-exponential .example name="Exponential rate"}

For independent $X_i\sim\operatorname{Exp}(\theta)$ the log-likelihood is $n\ln\theta-\theta\sum_ix_i$. Its derivative $n/\theta-\sum_ix_i$ vanishes at
$$\hat\theta_n=\frac n{x_1+\dots+x_n},$$
the reciprocal of the sample mean. By invariance the ML estimate of the mean $1/\theta$ is the sample mean.

:::

::: {#exm-ml-normal .example name="Normal mean and variance"}

For independent $X_i\sim N(\mu,v)$ with both parameters unknown, the log-likelihood is $-\frac n2\ln(2\pi v)-\frac1{2v}\sum_i(x_i-\mu)^2$. Setting both partial derivatives to zero gives
$$\hat\mu_n=M_n=\frac1n\sum_ix_i,\qquad\hat v_n=\frac1n\sum_i(x_i-M_n)^2.$$
The variance estimate is biased, $E[\hat V_n]=\frac{n-1}nv$, but asymptotically unbiased; $\frac n{n-1}\hat V_n$ is unbiased.

:::

::: {#def-confidence-interval .definition name="Confidence interval"}

For $0<\alpha<1$, a *$1-\alpha$ confidence interval* is a pair of estimators $\hat\Theta_n^-\le\hat\Theta_n^+$ such that
$$\Pr_\theta\bigl(\hat\Theta_n^-\le\theta\le\hat\Theta_n^+\bigr)\ge1-\alpha\qquad\text{for every }\theta.$$

:::

::: {#fig-classical-estimation-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl, dashed] (2.5,-0.2) -- (2.5,4.3) node[tick, above] {$\theta$};
\draw[emph] (1.71,0.00) -- (3.67,0.00);
\node[dot] at (2.69,0.00) {};
\draw[hl] (2.79,0.20) -- (4.75,0.20);
\node[hl dot] at (3.77,0.20) {};
\draw[emph] (2.07,0.40) -- (4.03,0.40);
\node[dot] at (3.05,0.40) {};
\draw[emph] (2.08,0.60) -- (4.04,0.60);
\node[dot] at (3.06,0.60) {};
\draw[emph] (1.84,0.80) -- (3.80,0.80);
\node[dot] at (2.82,0.80) {};
\draw[emph] (1.71,1.00) -- (3.67,1.00);
\node[dot] at (2.69,1.00) {};
\draw[emph] (1.86,1.20) -- (3.82,1.20);
\node[dot] at (2.84,1.20) {};
\draw[emph] (1.52,1.40) -- (3.48,1.40);
\node[dot] at (2.50,1.40) {};
\draw[emph] (1.17,1.60) -- (3.13,1.60);
\node[dot] at (2.15,1.60) {};
\draw[emph] (1.09,1.80) -- (3.05,1.80);
\node[dot] at (2.07,1.80) {};
\draw[emph] (0.96,2.00) -- (2.92,2.00);
\node[dot] at (1.94,2.00) {};
\draw[emph] (1.69,2.20) -- (3.65,2.20);
\node[dot] at (2.67,2.20) {};
\draw[emph] (1.85,2.40) -- (3.81,2.40);
\node[dot] at (2.83,2.40) {};
\draw[emph] (2.40,2.60) -- (4.36,2.60);
\node[dot] at (3.38,2.60) {};
\draw[emph] (1.83,2.80) -- (3.79,2.80);
\node[dot] at (2.81,2.80) {};
\draw[emph] (1.71,3.00) -- (3.67,3.00);
\node[dot] at (2.69,3.00) {};
\draw[emph] (1.91,3.20) -- (3.87,3.20);
\node[dot] at (2.89,3.20) {};
\draw[emph] (1.57,3.40) -- (3.53,3.40);
\node[dot] at (2.55,3.40) {};
\draw[emph] (0.62,3.60) -- (2.58,3.60);
\node[dot] at (1.60,3.60) {};
\draw[emph] (2.11,3.80) -- (4.07,3.80);
\node[dot] at (3.09,3.80) {};
\end{tikzpicture}
\end{center}
```

Twenty $95\%$ confidence intervals from independent samples. The interval is random and $\theta$ is fixed; in the long run about one interval in twenty misses $\theta$ (highlighted)

:::

The random object is the interval, not $\theta$: over many repetitions, at least a fraction $1-\alpha$ of the intervals contain the true value.

::: {#exm-confidence-interval-mean .example name="Interval for a mean"}

Let $X_1,\dots,X_n$ be independent $N(\theta,\sigma^2)$ with $\sigma$ known. Then $(M_n-\theta)\sqrt n/\sigma$ is standard normal, and $\Phi(1.96)\approx0.975$, so
$$\Bigl[M_n-\frac{1.96\,\sigma}{\sqrt n},\ M_n+\frac{1.96\,\sigma}{\sqrt n}\Bigr]$$
is a $95\%$ confidence interval. For other distributions with variance $\sigma^2$ the central limit theorem (@thm-central-limit-theorem) makes it an approximate $95\%$ interval for large $n$. When $\sigma$ is unknown, replace it by an estimate such as $\sqrt{\frac n{n-1}\hat V_n}$, or by an upper bound ($\sigma\le\frac12$ for a Bernoulli variable).

:::
