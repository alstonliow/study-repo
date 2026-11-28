---
title: "The Rao–Blackwell Theorem"
sources: [camib-st-3, camib-sts-1-q4, camib-sts-1-q12]
requires: [math/statistics/inference/sufficient-statistics, math/probability/joint-distributions/iterated-expectations]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 3 and Example Sheet 1 (questions 4, 12), in our own wording; proofs written out in steps. -->

Given any estimator, averaging it over the data that share the same value of a sufficient statistic cannot make it worse. This is the main reason for working with sufficient statistics.

::: {#thm-rao-blackwell .theorem name="Rao–Blackwell"}

Let $\Theta\subseteq\mathbb R$, let $T$ be sufficient for $\theta$, and let $\tilde\theta$ be an estimator of $\theta$ with $E_\theta(\tilde\theta^2)<\infty$. Put
$$
\hat\theta=E_\theta(\tilde\theta\mid T).
$$
Then $\hat\theta$ is an estimator (its formula does not involve $\theta$), it has the same bias as $\tilde\theta$, and
$$
\mathrm{MSE}(\hat\theta)\le\mathrm{MSE}(\tilde\theta)\quad\text{for all }\theta,
$$
with equality for all $\theta$ if and only if $\tilde\theta$ is a function of $T$ (almost surely).

:::

::: {.proof}

1. Since $T$ is sufficient, the conditional distribution of $X$ given $T$ does not depend on $\theta$ (@def-sufficient-statistic). Hence $E(\tilde\theta(X)\mid T)$, computed from this conditional distribution, is a function of $T$ alone and does not involve $\theta$: $\hat\theta$ is an estimator.

2. By the law of total expectation (@def-conditional-expectation-random-variable), $E_\theta(\hat\theta)=E_\theta(\tilde\theta)$, so the biases agree.

3. By the law of total variance,
$$\mathrm{Var}_\theta(\tilde\theta)=E_\theta\bigl(\mathrm{Var}(\tilde\theta\mid T)\bigr)+\mathrm{Var}_\theta\bigl(E(\tilde\theta\mid T)\bigr)\ \ge\ \mathrm{Var}_\theta(\hat\theta).$$

4. Since $\mathrm{MSE}=\mathrm{Var}+\mathrm{bias}^2$ (@prp-mse-bias-variance) and the biases agree, $\mathrm{MSE}(\tilde\theta)\ge\mathrm{MSE}(\hat\theta)$.

5. Equality for a given $\theta$ forces $E_\theta\mathrm{Var}(\tilde\theta\mid T)=0$, that is $\tilde\theta=E(\tilde\theta\mid T)$ almost surely: $\tilde\theta$ is a function of $T$. The converse is clear.

:::

::: {#fig-rao-blackwell-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->, muted] (0,0) -- (7,0);
\foreach \x in {1,2.4,3.8,5.2,6.4} \draw[faint] (\x,0) -- (\x,2.2);
\foreach \x/\y in {0.6/0.5,0.8/1.6,1.2/1.0,1.8/0.4,2.0/1.7,2.8/1.2,3.2/0.4,3.6/1.8,4.2/0.7,4.6/1.5,5.6/0.8,5.8/1.9,6.8/1.1}
  \node[small vertex] at (\x,\y) {};
\foreach \a/\b/\y in {0/1/1.1,1/2.4/1.05,2.4/3.8/1.07,3.8/5.2/1.15,5.2/6.4/1.35}
  \draw[hl] (\a+0.1,\y) -- (\b-0.1,\y);
\node[lab, right] at (7,0) {$T$};
\node[lab] at (3.5,2.7) {points: values of $\tilde\theta$; bars: their averages $\hat\theta$ in each strip of $T$};
\end{tikzpicture}
\end{center}
```

Rao–Blackwellisation replaces the value of $\tilde\theta$ by its average over the strip $\{T=t\}$. The mean is unchanged, and the spread inside strips, which is wasted variance, is removed.

:::

::: {#exm-rao-blackwell-poisson .example name="Estimating $e^{-\lambda}$ from Poisson data"}

Let $X_1,\dots,X_n$ be iid $\mathrm{Poisson}(\lambda)$ and $\theta=e^{-\lambda}=P(X_1=0)$.

1. $\tilde\theta=\mathbf 1\{X_1=0\}$ is unbiased, and $T=\sum_iX_i$ is sufficient with $T\sim\mathrm{Poisson}(n\lambda)$.

2. Given $T=t$, the counts are multinomial with equal cell probabilities, so $X_1\mid T=t\sim\mathrm{Bin}(t,1/n)$ and
$$\hat\theta=P(X_1=0\mid T)=\Bigl(1-\frac1n\Bigr)^{T}.$$

3. This is unbiased: $E(1-\tfrac1n)^T=\exp\{n\lambda(1-\tfrac1n-1)\}=e^{-\lambda}$, using the generating function of the Poisson distribution.

4. Its variance is $E(1-\frac1n)^{2T}-e^{-2\lambda}=e^{-2\lambda}(e^{\lambda/n}-1)$, against $e^{-\lambda}(1-e^{-\lambda})$ for $\tilde\theta$. For $\lambda=1$, $n=5$ these are $0.030$ and $0.233$.

:::

::: {#exm-rao-blackwell-uniform .example name="Estimating $\theta$ from $\mathrm{Unif}[0,\theta]$"}

Let $X_1,\dots,X_n$ be iid $\mathrm{Unif}[0,\theta]$. The maximum $T=\max_iX_i$ is sufficient (@exm-sufficient-uniform), and $\tilde\theta=2X_1$ is unbiased.

1. Given $T=t$, the first observation equals $t$ with probability $1/n$ and otherwise is uniform on $(0,t)$. So $E(X_1\mid T)=\frac1nT+\frac{n-1}{n}\cdot\frac T2=\frac{n+1}{2n}T$.

2. Hence $\hat\theta=\dfrac{n+1}{n}\,T$. It is unbiased, as $E(T)=\frac{n}{n+1}\theta$.

3. Its variance is $\bigl(\frac{n+1}{n}\bigr)^2\frac{n\theta^2}{(n+1)^2(n+2)}=\dfrac{\theta^2}{n(n+2)}$, against $\mathrm{Var}(2X_1)=\theta^2/3$. The improvement grows like $n^2$.

:::

::: {#def-umvu .definition name="Uniformly minimum variance unbiased estimator"}

An unbiased estimator $\hat\theta$ of $\theta$ with $E_\theta(\hat\theta^2)<\infty$ is a *uniformly minimum variance unbiased* (UMVU) estimator if $\mathrm{Var}_\theta(\hat\theta)\le\mathrm{Var}_\theta(\tilde\theta)$ for all $\theta\in\Theta$ and every other unbiased estimator $\tilde\theta$.

:::

::: {#rmk-umvu-search .remark name="Where to look for a UMVU estimator"}

By @thm-rao-blackwell a UMVU estimator, when it exists, can be taken to be a function of a sufficient statistic, and nothing is gained by looking elsewhere. In practice one starts from any unbiased estimator and Rao–Blackwellises it. That the result is then UMVU needs a further property of $T$ (completeness), which is not needed here.

:::
