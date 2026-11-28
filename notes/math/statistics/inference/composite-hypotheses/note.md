---
title: "Composite Hypotheses: Power Functions, UMP Tests and Generalised Likelihood Ratio Tests"
sources: [camib-st-8, camib-sts-2-q3, camib-sts-2-q8]
requires: [math/statistics/inference/parametric-tests]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 8 and Example Sheet 2 (questions 3, 8), in our own wording; proofs written out in steps. The Neyman–Pearson lemma for simple hypotheses is in math/probability/estimation/hypothesis-testing and the asymptotic likelihood ratio test (Wilks) in math/statistics/inference/parametric-tests; neither is repeated. -->

The Neyman–Pearson lemma (@thm-neyman-pearson) settles simple against simple hypotheses. Most hypotheses are composite, and the question is then whether one test is best against every alternative at once.

::: {#def-power-function .definition name="Power function and size"}

For a test $T:\mathcal X\to\{0,1\}$ of $H_0:\theta\in\Theta_0$ against $H_1:\theta\in\Theta_1$ (disjoint), the *power function* is
$$\beta(T;\theta)=P_\theta\bigl(T(X)=1\bigr),\qquad\theta\in\Theta .$$
On $\Theta_0$ it is the type I error rate, on $\Theta_1$ one minus the type II error rate, and the *size* of $T$ is $\sup_{\theta\in\Theta_0}\beta(T;\theta)$ (compare @def-significance-power).

:::

::: {#def-ump-test .definition name="Uniformly most powerful test"}

A test $T$ is a *uniformly most powerful* (UMP) test of size $\alpha$ of $H_0:\theta\in\Theta_0$ against $H_1:\theta\in\Theta_1$ if

1. $\sup_{\theta\in\Theta_0}\beta(T;\theta)=\alpha$, and
2. every test $\tilde T$ of size at most $\alpha$ has $\beta(T;\theta)\ge\beta(\tilde T;\theta)$ for all $\theta\in\Theta_1$.

:::

::: {#exm-power-function-z-test .example name="Power function of the $z$-test"}

Let $X_1,\dots,X_n$ be iid $N(\mu,\sigma_0^2)$ with $\sigma_0^2$ known, and $T=\mathbf 1\{Z>z_\alpha\}$ with $Z=\sqrt n(\bar X-\mu_0)/\sigma_0$. Since $\bar X\sim N(\mu,\sigma_0^2/n)$,
$$\beta(T;\mu)=P_\mu\Bigl(Z>z_\alpha\Bigr)=1-\Phi\Bigl(z_\alpha+\frac{\sqrt n(\mu_0-\mu)}{\sigma_0}\Bigr),$$
which is increasing in $\mu$ with $\beta(T;\mu_0)=\alpha$.

:::

::: {#thm-z-test-ump .theorem name="The one-sided $z$-test is UMP"}

In the normal location problem with known variance, $T=\mathbf 1\{Z>z_\alpha\}$ is a UMP test of size $\alpha$ of $H_0:\mu\le\mu_0$ against $H_1:\mu>\mu_0$.

:::

::: {.proof}

1. By @exm-power-function-z-test, $\beta(T;\mu)$ is increasing in $\mu$ and equals $\alpha$ at $\mu_0$, so the size of $T$ over $\Theta_0=(-\infty,\mu_0]$ is exactly $\alpha$.

2. Fix $\mu_1>\mu_0$ and consider the simple problem $\mu=\mu_0$ against $\mu=\mu_1$. The likelihood ratio is $\exp\{n(\mu_1-\mu_0)(\bar x-\tfrac12(\mu_0+\mu_1))/\sigma_0^2\}$, increasing in $\bar x$ since $\mu_1>\mu_0$, so a likelihood ratio test rejects for $\bar X$ large, that is for $Z>z_\alpha$ at size $\alpha$. By the Neyman–Pearson lemma $T$ is most powerful for this pair, and the rejection region does not involve $\mu_1$.

3. Let $\tilde T$ be any test of size at most $\alpha$ for the composite null. Then $\beta(\tilde T;\mu_0)\le\alpha$, so $\tilde T$ is a competitor in the simple problem, and $\beta(T;\mu_1)\ge\beta(\tilde T;\mu_1)$. This holds for every $\mu_1>\mu_0$.

:::

::: {#fig-composite-hypotheses-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.2cm,y=3.2cm]
\draw[->, muted] (3.9,0) -- (7.15,0) node[lab, right] {$\mu$};
\draw[->, muted] (4,0) -- (4,1.08);
\foreach \x in {4,5,6,7} \node[tick, below] at (\x,0) {$\x$};
\foreach \y in {0.5,1} \node[tick, left] at (4,\y) {$\y$};
\draw[faint] (4,0.05) -- (7,0.05);
\draw[emph, primary] plot coordinates {(4,0.000) (4.25,0.001) (4.5,0.004) (4.75,0.016) (5,0.050) (5.25,0.126) (5.5,0.259) (5.75,0.442) (6,0.639) (6.25,0.804) (6.5,0.912) (6.75,0.968) (7,0.991)};
\draw[emph, secondary] plot coordinates {(4,0.516) (4.25,0.323) (4.5,0.170) (4.75,0.079) (5,0.050) (5.25,0.079) (5.5,0.170) (5.75,0.323) (6,0.516) (6.25,0.705) (6.5,0.851) (6.75,0.938) (7,0.979)};
\node[lab, primary] at (6.3,0.55) {one-sided};
\node[lab, secondary] at (4.35,0.62) {two-sided};
\end{tikzpicture}
\end{center}
```

Power functions of the one-sided and the two-sided $z$-test for $\mu_0=5$, $\sigma_0=1$, $n=4$, $\alpha=0.05$. The one-sided test is more powerful for $\mu>5$ and has almost no power for $\mu<5$; the two-sided test spends power on both sides.

:::

::: {#prp-no-ump-two-sided .proposition name="No UMP test for a two-sided alternative"}

In the normal location problem, there is no UMP test of size $\alpha$ of $H_0:\mu=\mu_0$ against $H_1:\mu\ne\mu_0$.

:::

::: {.proof}

1. Suppose $T$ were UMP, and let $T_+=\mathbf 1\{Z>z_\alpha\}$. For every $\mu_1>\mu_0$ the test $T_+$ is most powerful for $\mu_0$ against $\mu_1$ (step 2 of @thm-z-test-ump) and $T$ has size $\alpha$, so $\beta(T;\mu_1)\le\beta(T_+;\mu_1)$; being UMP gives $\ge$. So $T$ has the same power as $T_+$, and is itself a most powerful test of $\mu_0$ against $\mu_1$.

2. The Neyman–Pearson test is the only most powerful test up to a set of probability $0$, so $T=T_+$ almost surely. By the same argument on the other side, $T=T_-=\mathbf 1\{Z<-z_\alpha\}$ almost surely.

3. But $T_+\ne T_-$ with positive probability, a contradiction.

:::

::: {#def-glrt .definition name="Generalised likelihood ratio test"}

For $H_0:\theta\in\Theta_0$ against $H_1:\theta\in\Theta_1$, with $\Theta_0\cup\Theta_1=\Theta$, the *generalised likelihood ratio statistic* is
$$\Lambda(X)=\frac{\sup_{\theta\in\Theta}p(X;\theta)}{\sup_{\theta\in\Theta_0}p(X;\theta)},$$
and the size $\alpha$ test rejects $H_0$ if $\Lambda>c_\alpha$, where $c_\alpha$ satisfies $\sup_{\theta\in\Theta_0}P_\theta(\Lambda(X)>c_\alpha)=\alpha$.

:::

::: {#rmk-glrt-notes .remark name="Using the generalised likelihood ratio"}

For simple $\Theta_0=\{\theta_0\}$, $\Theta_1=\{\theta_1\}$ this is the likelihood ratio test of the Neyman–Pearson lemma (the supremum over $\Theta$ is then attained at $\theta_0$ or $\theta_1$, which changes $\Lambda$ only by taking a maximum with $1$). Computing $\Lambda$ needs two maximisations, the unrestricted and the restricted likelihood; the threshold $c_\alpha$ is easiest when the null distribution of $\Lambda$ is the same for all $\theta\in\Theta_0$. For large $n$, $2\log\Lambda$ is approximately $\chi^2_{d-d_0}$ under $H_0$ (Wilks' theorem, @thm-likelihood-ratio-test), where $d$ and $d_0$ are the numbers of free parameters under $\Theta$ and $\Theta_0$.

:::

::: {#exm-two-sided-z-glrt .example name="The two-sided $z$-test is a generalised likelihood ratio test"}

For iid $N(\mu,\sigma_0^2)$ data with $\sigma_0^2$ known and $H_0:\mu=\mu_0$ against $H_1:\mu\ne\mu_0$:

1. The unrestricted maximum is at $\hat\mu=\bar X$, and $\sum(x_i-\mu_0)^2-\sum(x_i-\bar x)^2=n(\bar x-\mu_0)^2$.

2. Hence $2\log\Lambda=n(\bar X-\mu_0)^2/\sigma_0^2=Z^2$, an increasing function of $|Z|$.

3. Under $H_0$, $Z\sim N(0,1)$ so $2\log\Lambda\sim\chi^2_1$ *exactly*, and the size $\alpha$ test rejects when $|Z|>z_{\alpha/2}$.

By @prp-no-ump-two-sided this test is not UMP; it is what remains when no uniformly best test exists.

:::
