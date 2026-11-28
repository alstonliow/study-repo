---
title: "Exponential Families: Convexity, Mean Parametrisation and Likelihood Inference"
sources: [camii-sm-7, camii-sm-8, camii-sm-9, camii-sms-3-q8, camii-sms-3-q10]
requires: [math/probability/distributions/exponential-family, math/statistics/inference/composite-hypotheses]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Sections 3.1-3.3 (exponential tilting, cumulants, mean-value parametrisation, iid sampling, maximum likelihood, asymptotic inference, testing), and Example Sheet 3 (questions 7, 8, 10), in our own wording; proofs written out in steps. The definition, moments and dispersion families are already in math/probability/distributions/exponential-family and not repeated: this note uses its notation ($\eta$, $a(\eta)$, $b(y)$) for a one-parameter family with $T(y)=y$. The numerical example is our own. -->

Throughout, $Y$ has density $p(y;\eta)=b(y)\exp\{\eta y-a(\eta)\}$ (@def-exponential-family with $T(y)=y$) for $\eta$ in the *natural parameter space* $\Theta=\{\eta:\int b(y)e^{\eta y}dy<\infty\}$. Equivalently the family is obtained by *exponentially tilting* the base density $b$: $p(y;\eta)\propto e^{\eta y}b(y)$ with the normalising constant $e^{a(\eta)}$. Any member can serve as the base, since $p(y;\eta)=e^{(\eta-\eta_0)y-\{a(\eta)-a(\eta_0)\}}p(y;\eta_0)$. The family is *regular* if $\Theta$ is open, which holds for all families used here.

::: {#thm-log-partition-convex .theorem name="Convexity of the log partition function"}

$\Theta$ is a convex set and $a$ is convex on $\Theta$. If $Y$ is not almost surely constant, $a$ is strictly convex.

:::

::: {.proof}

1. Let $\eta_1,\eta_2\in\Theta$ and $\lambda\in(0,1)$. Write $e^{\lambda\eta_1y+(1-\lambda)\eta_2y}b(y)=\bigl(e^{\eta_1y}b\bigr)^\lambda\bigl(e^{\eta_2y}b\bigr)^{1-\lambda}$.

2. Hölder's inequality with exponents $1/\lambda$ and $1/(1-\lambda)$ gives $\int(e^{\eta_1y}b)^\lambda(e^{\eta_2y}b)^{1-\lambda}dy\le\bigl(\int e^{\eta_1y}b\bigr)^\lambda\bigl(\int e^{\eta_2y}b\bigr)^{1-\lambda}<\infty$, so $\lambda\eta_1+(1-\lambda)\eta_2\in\Theta$.

3. Taking logarithms, $a(\lambda\eta_1+(1-\lambda)\eta_2)\le\lambda a(\eta_1)+(1-\lambda)a(\eta_2)$. Strictness follows from @prp-exponential-family-moments: $a''(\eta)=\operatorname{Var}_\eta(Y)>0$.

:::

By @prp-exponential-family-moments the *mean function* and *variance function* are
$$\mu(\eta)=E_\eta Y=a'(\eta),\qquad V(\eta)=\operatorname{Var}_\eta Y=a''(\eta)=\mu'(\eta)>0 .$$
So $\mu$ is strictly increasing and can be inverted: the family can be indexed by its mean $\mu$ in the *mean space* $\{\mu(\eta):\eta\in\Theta\}$, with $d\eta/d\mu=1/V$ by the inverse function theorem. One then writes $V(\mu)$ for the variance function.

::: {#exm-natural-parametrisations .example name="Natural parameter, mean and variance function"}

| family | $\eta$ | $a(\eta)$ | $\mu(\eta)$ | $V(\mu)$ |
|---|---|---|---|---|
| $N(\mu,1)$ | $\mu$ | $\eta^2/2$ | $\eta$ | $1$ |
| $\mathrm{Poisson}(\lambda)$ | $\log\lambda$ | $e^\eta$ | $e^\eta$ | $\mu$ |
| $\mathrm{Bernoulli}(\pi)$ | $\log\frac\pi{1-\pi}$ | $\log(1+e^\eta)$ | $\frac{e^\eta}{1+e^\eta}$ | $\mu(1-\mu)$ |
| $\mathrm{Binomial}(m,\pi)$, $m$ fixed | $\log\frac\pi{1-\pi}$ | $m\log(1+e^\eta)$ | $m\pi$ | $\mu(1-\mu/m)$ |

For the multinomial with $L$ categories the counts satisfy $\sum Y_l=m$, so $(\log\pi_1,\dots,\log\pi_L)$ is not a minimal natural parameter. Taking the last category as baseline gives the $(L-1)$-dimensional natural parameter $\eta_l=\log(\pi_l/\pi_L)$ and the *softmax* inverse $\pi_l=e^{\eta_l}/\sum_{k=1}^Le^{\eta_k}$ with $\eta_L=0$ (see the softmax remark in @sec-ai-machine-learning-generalized-linear-models).

:::

::: {#thm-iid-exponential-family .theorem name="Independent samples stay in the family"}

Let $Y_1,\dots,Y_n$ be iid from $p(y;\eta)$. Their joint density is $\prod_ib(y_i)\exp\{n(\eta\bar y-a(\eta))\}$, so $\bar Y$ is sufficient and the sample is an exponential family with natural parameter $n\eta$, sufficient statistic $\bar y$ and log partition function $n\,a(\cdot/n)$. In mean parametrisation $E\bar Y=\mu$ and $\operatorname{Var}\bar Y=V/n$.

:::

::: {.proof}

1. Multiply the $n$ densities: $\prod_ib(y_i)\exp\{\eta\sum_iy_i-na(\eta)\}$. Rewrite the exponent as $(n\eta)\bar y-n\,a\bigl((n\eta)/n\bigr)$.

2. Differentiating $n\,a(\eta'/n)$ with respect to the natural parameter $\eta'=n\eta$ once gives $a'(\eta)=\mu$ and twice gives $a''(\eta)/n=V/n$.

:::

::: {#thm-exponential-family-mle .theorem name="The MLE matches the mean; asymptotic normality"}

For an iid sample from a regular family with $\bar y$ in the mean space, the log-likelihood is $\ell(\eta)=n\{\eta\bar Y-a(\eta)\}+\text{const}$ and it is strictly concave, with score $U(\eta)=n\{\bar Y-\mu(\eta)\}$. The MLE solves
$$\mu(\hat\eta)=\bar Y,\qquad\text{i.e. }\hat\eta=\eta(\bar Y).$$
The Fisher information of the sample is $i^{(n)}(\eta)=nV(\eta)$, and
$$\sqrt n(\hat\eta-\eta)\xrightarrow{d}N\bigl(0,\ 1/V(\eta)\bigr).$$

:::

::: {.proof}

1. The score is $\ell'(\eta)=n\{\bar Y-a'(\eta)\}$ and $\ell''(\eta)=-na''(\eta)=-nV(\eta)<0$, so $\ell$ is strictly concave and the unique solution of $U=0$ is the MLE.

2. The Fisher information is $E[-\ell'']=nV(\eta)$ (@prp-score-identities).

3. By the central limit theorem $\sqrt n(\bar Y-\mu)\to N(0,V(\eta))$. The delta method (@thm-delta-method) with $g=\eta(\cdot)$, $g'(\mu)=1/V(\eta)$ gives variance $V(\eta)/V(\eta)^2=1/V(\eta)$.

:::

So in an exponential family the Fisher information for the natural parameter is $n$ times the variance function, and the MLE agrees with the asymptotic theory of @thm-mle-asymptotic-normality.

::: {#exm-exponential-family-bernoulli-interval .example name="Log-odds of a Bernoulli sample"}

For $n=100$ Bernoulli trials with $\bar y=0.3$: $\hat\eta=\log(0.3/0.7)=-0.847$, and the information is $n\hat\pi(1-\hat\pi)=21$, so the standard error is $1/\sqrt{21}=0.218$. An approximate $95\%$ interval for $\eta$ is $-0.847\pm1.96(0.218)=(-1.27,-0.42)$, and applying the expit function gives $(0.22,0.40)$ for $\pi$.

:::

::: {#fig-exponential-family-inference-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm,y=3.6cm]
\draw[->, muted] (-5,0) -- (5,0) node[lab, right] {$\eta$};
\draw[->, muted] (0,-0.05) -- (0,1.1);
\node[tick, left] at (0,1) {$1$};
\draw[emph, primary, domain=-5:5, samples=80] plot (\x,{1/(1+exp(-\x))});
\draw[hl] (-5,0.3) -- (-0.847,0.3);
\draw[faint] (-0.847,0.3) -- (-0.847,0);
\node[lab, left] at (-5,0.3) {$\bar y$};
\node[lab, below] at (-0.847,0) {$\hat\eta$};
\node[lab] at (3.2,0.7) {$\mu(\eta)=a'(\eta)$};
\end{tikzpicture}
\end{center}
```

The mean function $\mu(\eta)=a'(\eta)$ of the Bernoulli family is strictly increasing, so the equation $\mu(\hat\eta)=\bar y$ has exactly one solution.

:::

::: {#thm-ump-exponential-family .theorem name="One-sided tests in an exponential family" related="thm-z-test-ump"}

Let $Y_1,\dots,Y_n$ be iid from a regular exponential family. For $H_0:\eta\le\eta_0$ against $H_1:\eta>\eta_0$, the test that rejects when $\bar Y>c$, with $c$ the $(1-\alpha)$-quantile of $\bar Y$ under $\eta_0$, is uniformly most powerful of size $\alpha$.

:::

::: {.proof}

1. For $\eta_1>\eta_0$ the log likelihood ratio is $n\{(\eta_1-\eta_0)\bar Y-a(\eta_1)+a(\eta_0)\}$, strictly increasing in $\bar Y$. So the likelihood ratio test of two simple hypotheses rejects for large $\bar Y$, and by the Neyman–Pearson lemma (@thm-neyman-pearson) $\{\bar Y>c\}$ is most powerful of its size for $\eta_0$ against $\eta_1$. It does not depend on $\eta_1$, hence is most powerful against every $\eta_1>\eta_0$ simultaneously.

2. For $\eta<\eta_0$ let $\alpha'=P_\eta(\bar Y>c)$. The same argument (with $\eta,\eta_0$ in place of $\eta_0,\eta_1$) shows that $\{\bar Y>c\}$ is most powerful among tests of size $\alpha'$ for $\eta$ against $\eta_0$. The constant test with value $\alpha'$ has size $\alpha'$ and power $\alpha'$, so $P_{\eta_0}(\bar Y>c)\ge\alpha'$. Hence $P_\eta(\text{reject})\le\alpha$ for all $\eta\le\eta_0$, and the test has size $\alpha$ for the composite null.

3. Any test of size $\alpha$ for the composite null has size $\le\alpha$ at $\eta_0$, so by step 1 its power at each $\eta_1>\eta_0$ is at most that of $\{\bar Y>c\}$.

:::
