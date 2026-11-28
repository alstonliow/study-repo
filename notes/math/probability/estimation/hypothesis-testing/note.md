---
title: "Hypothesis Testing"
sources: [eecs126-9, eecs126hw-12, eecs126d-11]
requires: [math/probability/foundations/bayes-theorem, math/probability/distributions/normal-distribution]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Hypothesis Testing", Homework 12 and Discussion 11, in our own wording; proofs written out in steps. -->

We observe $Y$ and must decide which of two hypotheses produced it: $X=0$ ($H_0$, "no signal") or $X=1$ ($H_1$, "signal"). Under $H_x$, $Y$ has PMF or density $f(y\mid x)$.

::: {#def-map-mle .definition name="MAP and ML decisions"}

The *maximum a posteriori* (MAP) and *maximum likelihood* (ML) rules decide
$$\hat X_{\mathrm{MAP}}(y)=\arg\max_x\Pr(X=x)f(y\mid x),\qquad\hat X_{\mathrm{ML}}(y)=\arg\max_xf(y\mid x).$$

:::

::: {#thm-map-minimises-error .theorem name="MAP minimises the probability of error"}

When $X$ has a prior distribution, among all decision rules $g$ the MAP rule minimises $\Pr(g(Y)\ne X)$. ML is MAP for a uniform prior.

:::

::: {.proof}

1. Conditioning on $Y=y$, $\Pr(g(Y)=X\mid Y=y)=\Pr(X=g(y)\mid Y=y)$.

2. By Bayes' rule (@thm-bayes-theorem) $\Pr(X=x\mid Y=y)\propto\Pr(X=x)f(y\mid x)$, so for each $y$ the MAP choice maximises the conditional probability of being right.

3. Averaging over $Y$, MAP maximises $\Pr(g(Y)=X)$.

:::

::: {#fig-hypothesis-testing-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.4,0) node[lab, right] {$y$};
\draw[emph, domain=0:7, samples=80, smooth, variable=\x] plot ({\x}, {4.2*exp(-((\x-2.5)^2)/(2*1^2))/(1*sqrt(2*pi))});
\draw[hl, domain=0:7, samples=80, smooth, variable=\x] plot ({\x}, {2.6*exp(-((\x-4.6)^2)/(2*1^2))/(1*sqrt(2*pi))});
\draw[faint, dashed] (3.78,0) -- (3.78,2.0);
\node[tick] at (1.9,2.0) {decide $0$};
\node[tick] at (5.6,2.0) {decide $1$};
\node[tick] at (1.3,0.95) {$\pi_0f_0$};
\node[tick, text=accent] at (5.9,0.75) {$\pi_1f_1$};
\end{tikzpicture}
\end{center}
```

The MAP rule decides for the hypothesis with the larger weighted density $\pi_if_i(y)$; the threshold sits where the curves cross, shifted away from the more likely hypothesis

:::

Often there is no sensible prior, and the two errors have different costs (a missed alarm versus a false alarm). Then we fix the false-alarm probability and maximise the detection probability.

::: {#def-neyman-pearson-problem .definition name="Errors, likelihood ratio"}

For a randomised decision rule $\hat X$, the *probability of false alarm* is $\mathrm{PFA}=\Pr(\hat X=1\mid X=0)$ and the *probability of correct detection* is $\mathrm{PCD}=\Pr(\hat X=1\mid X=1)$. The *likelihood ratio* is $L(y)=f(y\mid1)/f(y\mid0)$.

:::

::: {#thm-neyman-pearson .theorem name="Neyman–Pearson lemma"}

Fix $\beta\in(0,1)$. Among all rules with $\mathrm{PFA}\le\beta$, $\mathrm{PCD}$ is maximised by the *likelihood ratio test*
$$\hat X=\begin{cases}1&L(Y)>\lambda,\\1\text{ with probability }\gamma&L(Y)=\lambda,\\0&L(Y)<\lambda,\end{cases}$$
with the threshold $\lambda\ge0$ and $\gamma\in[0,1]$ chosen so that $\mathrm{PFA}=\beta$.

:::

::: {.proof}

1. Write $\phi(y)\in[0,1]$ for the probability that the test decides $1$ on $y$, and $\psi(y)$ for that of any other rule with $\mathrm{PFA}\le\beta$. Then $\mathrm{PCD}=\int\phi f(\cdot\mid1)$ and $\mathrm{PFA}=\int\phi f(\cdot\mid0)$ (sums for PMFs).

2. Pointwise, $(\phi(y)-\psi(y))\bigl(f(y\mid1)-\lambda f(y\mid0)\bigr)\ge0$: where $f(y\mid1)>\lambda f(y\mid0)$, $\phi=1\ge\psi$; where it is smaller, $\phi=0\le\psi$.

3. Integrating, $\mathrm{PCD}_\phi-\mathrm{PCD}_\psi\ge\lambda(\mathrm{PFA}_\phi-\mathrm{PFA}_\psi)=\lambda(\beta-\mathrm{PFA}_\psi)\ge0$.

:::

The randomisation $\gamma$ is only needed when $L(Y)$ has an atom at the threshold (discrete observations). When $L$ is increasing in $y$, the test is simply "decide $1$ when $y$ exceeds a threshold".

::: {#exm-neyman-pearson-gaussian .example name="Gaussian mean"}

Under $H_0$, $Y\sim N(0,1)$; under $H_1$, $Y\sim N(1,1)$. Then $L(y)=e^{y-1/2}$ is increasing, so the test decides $1$ when $Y>t$. For $\mathrm{PFA}=0.05$, $t\approx1.645$, and $\mathrm{PCD}=\Pr(N(1,1)>1.645)\approx0.26$. With a uniform prior, MAP decides $1$ when $L(y)>1$, that is $y>\tfrac12$, with error probability $\Phi(-\tfrac12)\approx0.31$.

:::

::: {#fig-hypothesis-testing-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[xscale=1.2, yscale=5]
\fill[tintB] plot[domain=1.645:4, samples=40] (\x,{exp(-(\x-1)^2/2)/sqrt(2*pi)}) -- (4,0) -- (1.645,0) -- cycle;
\fill[accent] plot[domain=1.645:3.5, samples=40] (\x,{exp(-(\x)^2/2)/sqrt(2*pi)}) -- (3.5,0) -- (1.645,0) -- cycle;
\draw[emph, primary] plot[domain=-3:3.5, samples=80] (\x,{exp(-(\x)^2/2)/sqrt(2*pi)});
\draw[emph, secondary] plot[domain=-2:4, samples=80] (\x,{exp(-(\x-1)^2/2)/sqrt(2*pi)});
\draw[->] (-3.2,0) -- (4.4,0) node[lab, right] {$y$};
\draw[dashed] (1.645,0) -- (1.645,0.46) node[lab, above] {$t\approx1.645$};
\node[lab, primary] at (-1.3,0.36) {$H_0$: $N(0,1)$};
\node[lab, secondary] at (2.8,0.36) {$H_1$: $N(1,1)$};
\node[lab] at (2.75,0.13) {$\mathrm{PCD}\approx0.26$};
\draw[->, accent] (2.6,-0.07) node[lab, right] {$\mathrm{PFA}=0.05$} -- (1.95,0.02);
\end{tikzpicture}
\end{center}
```

The test of @exm-neyman-pearson-gaussian decides $1$ when $Y>t$. The dark area under the $H_0$ density is the false-alarm probability $0.05$; the shaded area under the $H_1$ density is the probability of correct detection.

:::

::: {#rmk-hypothesis-testing-roc .remark name="The ROC curve"}

Plotting the best $\mathrm{PCD}$ against $\mathrm{PFA}=\beta$ for all $\beta$ gives the *receiver operating characteristic*. It is concave and increasing, from $(0,0)$ to $(1,1)$; the further it bends towards $(0,1)$, the easier the two hypotheses are to tell apart.

:::

::: {#fig-hypothesis-testing-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (3.4,0) node[lab, right] {$\mathrm{PFA}$};
\draw[->] (0,0) -- (0,3.4) node[lab, above] {$\mathrm{PCD}$};
\draw[faint, dashed] (0,0) -- (3,3);
\draw[faint] (3,0) -- (3,3) -- (0,3);
\node[tick, below] at (3,0) {$1$}; \node[tick, left] at (0,3) {$1$};
\draw[emph, primary] (0.000,0.000) -- (0.075,0.506) -- (0.150,0.779) -- (0.225,0.990) -- (0.300,1.167) -- (0.375,1.321) -- (0.450,1.456) -- (0.525,1.578) -- (0.600,1.689) -- (0.675,1.790) -- (0.750,1.883) -- (0.825,1.969) -- (0.900,2.048) -- (0.975,2.123) -- (1.050,2.192) -- (1.125,2.257) -- (1.200,2.317) -- (1.275,2.374) -- (1.350,2.427) -- (1.425,2.477) -- (1.500,2.524) -- (1.575,2.568) -- (1.650,2.610) -- (1.725,2.648) -- (1.800,2.685) -- (1.875,2.719) -- (1.950,2.751) -- (2.025,2.781) -- (2.100,2.809) -- (2.175,2.835) -- (2.250,2.859) -- (2.325,2.881) -- (2.400,2.902) -- (2.475,2.920) -- (2.550,2.937) -- (2.625,2.953) -- (2.700,2.966) -- (2.775,2.978) -- (2.850,2.988) -- (2.925,2.995) -- (3.000,3.000);
\node[hl dot] at (0.15,0.78) {};
\node[lab, right] at (0.2,0.7) {$(0.05,0.26)$};
\node[lab, primary] at (2.1,1.3) {$N(0,1)$ vs $N(1,1)$};
\end{tikzpicture}
\end{center}
```

The ROC curve of @exm-neyman-pearson-gaussian. The marked point is the test with $\mathrm{PFA}=0.05$; the dashed diagonal is what guessing achieves, and curves closer to the corner $(0,1)$ belong to easier problems.

:::
