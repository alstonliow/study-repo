---
title: "Bayesian Inference"
sources: [mit6041-21, mit6041-22]
requires: [math/probability/estimation/linear-estimation]
status: draft
---

<!-- Added 2026-11-20 from MIT 6.041 (Fall 2010), Lectures 21 and 22, in our own wording; proofs written out in steps. -->

In Bayesian inference the unknown quantity is itself a random variable $\Theta$, with a *prior* distribution that expresses what is believed before the data arrive. Observing $X=x$ turns the prior into a *posterior*.

::: {#def-bayesian-model .definition name="Bayesian model, prior, posterior"}

A *Bayesian model* consists of

1. a *prior* $p_\Theta$ (or density $f_\Theta$) of the unknown $\Theta$, and
2. an *observation model* $p_{X\mid\Theta}(x\mid\theta)$ (or $f_{X\mid\Theta}$): the distribution of the data for each value of $\Theta$.

The *posterior* is the conditional distribution of $\Theta$ given the observed $X=x$.

:::

::: {#thm-bayes-rule-mixed .theorem name="Bayes' rule for random variables" generalizes="thm-bayes-theorem"}

When $\Theta$ and $X$ are both continuous,
$$f_{\Theta\mid X}(\theta\mid x)=\frac{f_\Theta(\theta)\,f_{X\mid\Theta}(x\mid\theta)}{\int f_\Theta(\theta')\,f_{X\mid\Theta}(x\mid\theta')\,d\theta'}\qquad(f_X(x)>0).$$
The same formula holds with PMFs in place of densities for a discrete $\Theta$ or a discrete $X$, with sums in place of integrals over $\theta'$ when $\Theta$ is discrete.

:::

::: {.proof}

1. By the definition of conditional densities (@def-marginal-conditional-density), $f_{\Theta,X}(\theta,x)=f_\Theta(\theta)f_{X\mid\Theta}(x\mid\theta)=f_X(x)f_{\Theta\mid X}(\theta\mid x)$.

2. Divide by $f_X(x)$, and write $f_X(x)=\int f_{\Theta,X}(\theta',x)\,d\theta'$ as the marginal of the joint density.

3. For discrete variables the same two steps hold with $\Pr(\Theta=\theta,X=x)$, which is Bayes' theorem (@thm-bayes-theorem); in the mixed cases, a PMF for one variable and a density for the other, the products in step 1 are still valid joint descriptions.

:::

The denominator does not depend on $\theta$; so in computations one writes $f_{\Theta\mid X}(\theta\mid x)\propto f_\Theta(\theta)f_{X\mid\Theta}(x\mid\theta)$ and normalises at the end.

::: {#def-map-lms-estimates .definition name="MAP and LMS estimates" related="def-map-mle"}

Given the observation $X=x$:

1. the *maximum a posteriori (MAP) estimate* $\hat\theta$ maximises the posterior $p_{\Theta\mid X}(\theta\mid x)$ or $f_{\Theta\mid X}(\theta\mid x)$ over $\theta$;
2. the *least mean squares (LMS) estimate* is the posterior mean $\hat\theta=E[\Theta\mid X=x]$.

The corresponding *estimators* are the random variables $\hat\Theta=g(X)$ obtained by using the observed value.

:::

::: {#rmk-map-lms-optimal .remark name="What each estimate is best at"}

For a discrete $\Theta$ the MAP rule minimises the probability of a wrong guess (@thm-map-minimises-error). The LMS estimator minimises the mean squared error $E[(\Theta-g(X))^2]$ over all functions $g$ (@thm-mmse-conditional-expectation), and its error $\tilde\Theta=\hat\Theta-\Theta$ has mean $0$ and is uncorrelated with every function of $X$.

:::

::: {#exm-coin-bias-uniform-prior .example name="A coin with unknown bias"}

Let $\Theta$ be uniform on $[0,1]$ and, given $\Theta=\theta$, toss a coin with heads probability $\theta$ independently $n$ times; observe $k$ heads. The posterior is
$$f_{\Theta\mid X}(\theta\mid k)\propto\theta^k(1-\theta)^{n-k},\qquad0\le\theta\le1,$$
a Beta$(k+1,n-k+1)$ density. Setting the derivative of $k\ln\theta+(n-k)\ln(1-\theta)$ to zero gives the MAP estimate $k/n$, while the LMS estimate is
$$E[\Theta\mid X=k]=\frac{\int_0^1\theta^{k+1}(1-\theta)^{n-k}\,d\theta}{\int_0^1\theta^k(1-\theta)^{n-k}\,d\theta}=\frac{k+1}{n+2}.$$
For $n=10$ and $k=3$: MAP $0.3$, LMS $1/3$. The LMS estimate is pulled towards the prior mean $1/2$.

:::

::: {#fig-bayesian-inference-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[xscale=6, yscale=0.9]
\draw[->] (0,0) -- (1.08,0) node[lab, right] {$\theta$};
\draw[->] (0,0) -- (0,3.4);
\foreach \x in {0,0.5,1} {\draw (\x,-0.05) -- (\x,0.05); \node[tick, below] at (\x,-0.05) {$\x$};}
\draw[faint, dashed] (0,1) -- (1,1) node[lab, right] {prior};
\draw[emph, primary, domain=0:1, samples=80] plot (\x, {1320*\x^3*(1-\x)^7});
\draw[faint] (0.3,0) -- (0.3,2.935) node[lab, above] {MAP $0.3$};
\draw[faint, dashed] (0.3333,0) -- (0.3333,2.3);
\node[lab, right] at (0.36,1.6) {LMS $1/3$};
\end{tikzpicture}
\end{center}
```

Uniform prior and the posterior after $3$ heads in $10$ tosses (@exm-coin-bias-uniform-prior).

:::

::: {#exm-waiting-for-a-friend .example name="Waiting for a late friend"}

A friend is late by $X$ hours, uniform on $[0,\Theta]$, and $\Theta$ is uniform on $[0,1]$. Observing $X=x$, the posterior is
$$f_{\Theta\mid X}(\theta\mid x)=\frac{1\cdot\frac1\theta}{\int_x^1\frac{d\theta'}{\theta'}}=\frac1{\theta\,\lvert\ln x\rvert},\qquad x\le\theta\le1.$$
It is decreasing in $\theta$, so the MAP estimate is $\hat\theta=x$, the smallest value consistent with the data; the LMS estimate is
$$E[\Theta\mid X=x]=\int_x^1\frac{\theta\,d\theta}{\theta\lvert\ln x\rvert}=\frac{1-x}{\lvert\ln x\rvert}.$$

:::

::: {#exm-normal-prior-normal-noise .example name="Normal prior, normal noise" related="thm-jointly-gaussian-properties"}

Let $\Theta\sim N(x_0,\sigma_0^2)$ and $X=\Theta+W$ with $W\sim N(0,\sigma^2)$ independent of $\Theta$. The exponent of $f_\Theta(\theta)f_{X\mid\Theta}(x\mid\theta)$ is a quadratic in $\theta$, so the posterior is normal; completing the square gives mean and variance
$$\hat\theta=\frac{x_0/\sigma_0^2+x/\sigma^2}{1/\sigma_0^2+1/\sigma^2},\qquad\frac1{1/\sigma_0^2+1/\sigma^2}.$$
The posterior mean is a precision-weighted average of the prior mean and the observation. A normal density peaks at its mean, so here MAP and LMS agree, and the estimate is linear in $x$.

:::
