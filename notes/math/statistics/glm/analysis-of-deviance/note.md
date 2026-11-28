---
title: "Nested GLMs and Analysis of Deviance"
sources: [camii-sm-13, camii-sms-4-q6]
requires: [math/statistics/inference/deviance, math/statistics/glm/glm-canonical-form, math/statistics/frequentist/anova-nested-models]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 4.4, and Example Sheet 4 (question 6), in our own wording; proofs written out in steps. The Poisson example is our own and checked by computation. -->

Analysis of deviance extends the $F$-test for nested linear models (@thm-nested-f-test) to canonical-link GLMs. As in @thm-nested-projections write $\mathbb X=(\mathbb X_0\ \mathbb X_1)$ with $\mathbb X_0\in\mathbb R^{n\times p_0}$ and $\beta=(\beta_0,\beta_1)$. The *full model* has $\eta=\mathbb X\beta$, the *null model* has $\eta=\mathbb X_0\beta_0$, and the hypothesis is $H_0:\beta_1=0$. Denote by $\hat\mu$ and $\hat\mu_0$ the fitted means of the two models. A GLM is *saturated* if $\operatorname{rank}\mathbb X=n$, in which case $\hat\mu=Y$; the smallest GLM with an intercept has $\mathbb X=\mathbf 1$ and $\hat\mu=\bar Y\mathbf 1$.

::: {#fig-analysis-of-deviance-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[emph, primary] (0,0.4) to[out=15,in=190] (7,1.6);
\draw[emph, hl] (0.5,0.1) to[out=5,in=185] (3.5,0.15);
\node[lab, right] at (7,1.6) {$\mathcal M=\{\mu(\mathbb X\beta)\}$};
\node[lab, below] at (2,0) {$\mathcal M_0$};
\node[small vertex] (y) at (6,3.6) {};
\node[lab, above] at (6,3.6) {$Y$};
\node[small vertex] (m) at (5.2,1.1) {};
\node[lab, below right] at (5.2,1.1) {$\hat\mu$};
\node[small vertex] (m0) at (2.5,0.13) {};
\node[lab, below] at (2.5,-0.2) {$\hat\mu_0$};
\draw[faint] (y) -- (m);
\draw[faint] (y) -- (m0);
\draw[emph] (m) -- (m0);
\end{tikzpicture}
\end{center}
```

The data $Y$, the full fit $\hat\mu$ on the curved model manifold $\mathcal M$ and the null fit $\hat\mu_0$ on the sub-manifold $\mathcal M_0$. Deviance plays the role of squared length: $D(Y,\hat\mu_0)=D(Y,\hat\mu)+D(\hat\mu,\hat\mu_0)$, a Pythagorean identity for the canonical link.

:::

::: {#thm-deviance-additivity .theorem name="Deviance additivity"}

For nested canonical-link GLMs with unit dispersion,
$$D^{(n)}(\hat\mu,\hat\mu_0)=2\{\ell(\hat\mu)-\ell(\hat\mu_0)\},\qquad D^{(n)}(Y,\hat\mu_0)=D^{(n)}(Y,\hat\mu)+D^{(n)}(\hat\mu,\hat\mu_0).$$
For the normal family with identity link and $\sigma^2=1$, $D^{(n)}(\mu_1,\mu_2)=\|\mu_1-\mu_2\|^2$ and the second identity is Pythagoras' theorem.

:::

::: {.proof}

1. With natural parameters $\hat\eta=\mathbb X\hat\beta$ and $\hat\eta_0=\mathbb X_0\hat\beta_0$, @def-deviance gives $D^{(n)}(\hat\mu,\hat\mu_0)=2\sum_i\{(\hat\eta_i-\hat\eta_{0,i})\hat\mu_i-a(\hat\eta_i)+a(\hat\eta_{0,i})\}$, whereas $2\{\ell(\hat\mu)-\ell(\hat\mu_0)\}=2\sum_i\{(\hat\eta_i-\hat\eta_{0,i})Y_i-a(\hat\eta_i)+a(\hat\eta_{0,i})\}$.

2. The difference is $2(\hat\eta-\hat\eta_0)^{\mathsf T}(\hat\mu-Y)$. Now $\hat\eta-\hat\eta_0=\mathbb X(\hat\beta-(\hat\beta_0,0))$ lies in the column space of $\mathbb X$, and $\mathbb X^{\mathsf T}(Y-\hat\mu)=0$ by the normal equations (@thm-glm-normal-equations), so the difference vanishes. This is the first identity.

3. The same computation with the saturated model $\hat\mu^{\mathrm{sat}}=Y$ in place of $\hat\mu_0$ shows $D^{(n)}(Y,\hat\mu)=2\{\ell(Y)-\ell(\hat\mu)\}$ (the saturated log-likelihood $\ell(Y)$ is the largest possible).

4. Hence $D^{(n)}(Y,\hat\mu_0)=2\{\ell(Y)-\ell(\hat\mu_0)\}=2\{\ell(Y)-\ell(\hat\mu)\}+2\{\ell(\hat\mu)-\ell(\hat\mu_0)\}$, which is the second identity.

:::

For a non-canonical link the first identity and Wilks' theorem still hold, but the additive decomposition does not.

::: {#thm-analysis-of-deviance .theorem name="Analysis of deviance test"}

Under $H_0:\beta_1=0$, as $n\to\infty$,
$$D^{(n)}(\hat\mu,\hat\mu_0)=2\{\ell(\hat\mu)-\ell(\hat\mu_0)\}\xrightarrow{d}\chi^2_{p-p_0}.$$
Reject $H_0$ at level $\alpha$ if $D^{(n)}(\hat\mu,\hat\mu_0)>\chi^2_{p-p_0}(\alpha)$. If the dispersion $\phi$ is unknown, divide by $\hat\phi$ (@prp-glm-dispersion-estimation) and reject if $D^{(n)}(\hat\mu,\hat\mu_0)/\hat\phi>(p-p_0)F_{p-p_0,n-p}(\alpha)$, which is more accurate in small samples and is the $F$-test of the normal linear model when the family is normal.

:::

::: {.proof}

The first identity of @thm-deviance-additivity writes the deviance as a log-likelihood ratio statistic, and Wilks' theorem (@thm-likelihood-ratio-test) gives the $\chi^2_{p-p_0}$ limit, as the full parameter space has $p$ and the null $p_0$ free parameters. With dispersion $\phi$ the deviance is $\phi$ times the log-likelihood ratio (the deviance is computed in the family with $\phi=1$), hence the division by $\hat\phi$.

:::

With a sequence of nested models one can decompose the total deviance step by step into a table, exactly as the ANOVA table decomposes the total sum of squares.

::: {#exm-poisson-analysis-of-deviance .example name="Is there a group effect in Poisson counts?"}

Two groups of three counts, $(3,5,4)$ and $(9,7,8)$, are modelled as $Y_i\sim\mathrm{Poisson}(\mu_i)$ with $\log\mu_i=\beta_0+\beta_1x_i$, $x_i\in\{0,1\}$ the group. The null model ($\beta_1=0$) has $\hat\mu_0=\bar Y=6$ for all six counts. The full model fits each group mean: $\hat\mu=4$ and $8$. Using $D(\mu_1,\mu_2)=2(\mu_1\log\frac{\mu_1}{\mu_2}-\mu_1+\mu_2)$:

1. $D^{(n)}(\hat\mu,\hat\mu_0)=2\cdot3\{(4\log\frac46-4+6)+(8\log\frac86-8+6)\}=4.078$.
2. $D^{(n)}(Y,\hat\mu)=0.756$ (residual deviance, $6-2=4$ degrees of freedom) and $D^{(n)}(Y,\hat\mu_0)=4.834$, so the decomposition $4.834=0.756+4.078$ checks.
3. $4.078>\chi^2_1(0.05)=3.84$ ($p=0.043$): there is evidence of a group effect at the $5\%$ level.

:::
