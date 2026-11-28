---
title: "Two-Sample Problems, Paired Tests and Power"
sources: [camib-st-16, camib-st-14]
requires: [math/statistics/frequentist/anova-nested-models, math/statistics/frequentist/exact-tests]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lectures 14 and 16, in our own wording; proofs written out in steps. The $t$-tests themselves are in math/statistics/frequentist/t-tests; the equivalence of the two-sample $t$-test and the ANOVA $F$-test is in math/statistics/frequentist/anova-nested-models. The sample-size numbers were recomputed by a short script. -->

Two samples can be compared in several ways, depending on what is assumed about their spread, their pairing and their distributions. The last subsection asks the design question: how large must the samples be?

::: {#def-two-sample-formulations .definition name="Formulations of the two-sample problem"}

Let $A_1,\dots,A_n$ be iid with law $F$ and $B_1,\dots,B_m$ iid with law $G$. The question *are $F$ and $G$ alike?* is made precise in three standard ways.

1. *Equal variances:* $A,B$ independent, $F=N(\mu_1,\sigma^2)$, $G=N(\mu_2,\sigma^2)$, $H_0:\mu_1=\mu_2$. The two-sample $t$-test and the ANOVA $F$-test coincide (@prp-two-sample-t-f).
2. *Unequal variances* (the Behrens–Fisher problem): $F=N(\mu_1,\sigma_1^2)$, $G=N(\mu_2,\sigma_2^2)$ with $H_0:\mu_1=\mu_2$. There is no exact $t$-type solution; Welch's $t$-test, with a data-dependent number of degrees of freedom, is an accepted approximation.
3. *No distributional assumption:* $H_0:F=G$. The permutation test (@def-permutation-test) applied to the difference of means is exact, and asymptotically equivalent to the $t$-test of item 1.

:::

::: {#prp-paired-t-test .proposition name="The paired t-test"}

Let $(A_i,B_i)$, $i=1,\dots,n$, be results for pair $i$ and suppose, with independent noise,
$$A_i=\mu_1+\alpha_i+\varepsilon_i,\qquad B_i=\mu_2+\alpha_i+\varepsilon_i',\qquad\varepsilon_i,\varepsilon_i'\ \text{iid }N(0,\sigma^2),$$
where $\alpha_i$ is an unknown effect of pair $i$ shared by both members. Then $D_i=A_i-B_i$ are iid $N(\mu_1-\mu_2,2\sigma^2)$, free of the nuisance parameters $\alpha_i$, so $H_0:\mu_1=\mu_2$ is tested by Student's one-sample $t$-test applied to $D_1,\dots,D_n$, with $n-1$ degrees of freedom.

:::

::: {.proof}

$D_i=(\mu_1-\mu_2)+(\varepsilon_i-\varepsilon_i')$; the shared $\alpha_i$ cancels, and $\varepsilon_i-\varepsilon_i'\sim N(0,2\sigma^2)$ with independence across $i$. The statistic $\sqrt n\bar D/s_D\sim t_{n-1}$ under $H_0$ (@def-one-sample-t-test).

:::

::: {#rmk-paired-design .remark name="Why pair"}

If the pair effects $\alpha_i$ vary a lot, comparing $\bar A$ with $\bar B$ as two independent samples would add the variance of the $\alpha_i$ to the noise. Pairing removes it, and randomising which member of a pair gets which treatment keeps the comparison fair.

:::

::: {#def-noncentral-t .definition name="Noncentral t-distribution"}

If $Z\sim N(0,1)$ and $Y\sim\chi^2_k$ are independent and $\delta\in\mathbb R$, then $(Z+\delta)/\sqrt{Y/k}$ has the *noncentral $t$-distribution* with $k$ degrees of freedom and noncentrality parameter $\delta$. For $\delta=0$ it is $t_k$.

:::

::: {#prp-t-test-power .proposition name="Power of the two-sample t-test"}

Let $A_1,\dots,A_n$ be iid $N(\mu_1,\sigma^2)$ and $B_1,\dots,B_n$ iid $N(\mu_2,\sigma^2)$, independent. With $\hat\sigma^2$ the pooled variance estimate on $2n-2$ degrees of freedom, the statistic $T=(\bar A-\bar B)/(\hat\sigma\sqrt{2/n})$ has the noncentral $t$-distribution with $2n-2$ degrees of freedom and noncentrality $\delta=(\mu_1-\mu_2)/(\sigma\sqrt{2/n})$. The power of the two-sided test is $P(|T|>t_{2n-2}(\alpha/2))$ under this law.

:::

::: {.proof}

1. $\bar A-\bar B\sim N(\mu_1-\mu_2,2\sigma^2/n)$, so $Z=(\bar A-\bar B-(\mu_1-\mu_2))/(\sigma\sqrt{2/n})\sim N(0,1)$ and $(\bar A-\bar B)/(\sigma\sqrt{2/n})=Z+\delta$.

2. $(2n-2)\hat\sigma^2/\sigma^2\sim\chi^2_{2n-2}$ is independent of the sample means (@thm-normal-sample-theory), so independent of $Z$.

3. $T=(Z+\delta)\big/\sqrt{\hat\sigma^2/\sigma^2}$, which is the stated noncentral $t$ variable.

:::

::: {#exm-sample-size .example name="Sample size for a given power"}

A trial compares a treatment with a control, $n$ patients per arm, effect $\delta_0$ (a drop in mean) and known standard deviation $\sigma$. The one-sided $z$-test of size $\alpha$ rejects when $Z=(\bar A-\bar B)/(\sigma\sqrt{2/n})>z_\alpha$, and its power is
$$1-\Phi\Bigl(z_\alpha-\frac{\delta_0\sqrt n}{\sigma\sqrt2}\Bigr)\ \ge\ \pi\iff n\ \ge\ \frac{2\sigma^2(z_\alpha+z_{1-\pi})^2}{\delta_0^2},$$
where $z_\beta$ denotes the upper $\beta$-quantile of $N(0,1)$. For $\alpha=0.05$, power $\pi=0.9$ and $\delta_0=\sigma/2$: $z_{0.05}=1.645$, $z_{0.1}=1.282$, and $n\ge2(2.927)^2/0.25=68.5$, so $n=69$ per arm gives power $0.902$. With $\sigma$ unknown the $t$-test needs slightly more patients, computed from @prp-t-test-power.

:::

::: {#fig-two-sample-power-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.7cm,y=3.6cm]
\draw[->, muted] (-3.5,0) -- (7,0) node[lab, right] {$z$};
\draw[->, muted] (-3.5,0) -- (-3.5,0.5);
\draw[emph, primary, domain=-3.4:3.4, samples=60] plot (\x,{exp(-\x*\x/2)/2.5066});
\draw[emph, secondary, domain=-0.5:6.5, samples=60] plot (\x,{exp(-(\x-2.94)^2/2)/2.5066});
\draw[hl] (1.645,0) -- (1.645,0.45);
\node[lab] at (1.645,0.5) {$z_\alpha$};
\node[lab, primary] at (-1.7,0.38) {$H_0$};
\node[lab, secondary] at (4.9,0.38) {$H_1$ ($n=69$)};
\end{tikzpicture}
\end{center}
```

The null and alternative distributions of the $z$-statistic for $n=69$. The alternative is shifted by $\delta_0\sqrt n/(\sigma\sqrt2)=2.94$; the power is the mass of the shifted curve to the right of the critical value $z_\alpha$.

:::
