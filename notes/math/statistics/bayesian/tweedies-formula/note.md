---
title: "Exponential Family Posteriors, Tweedie's Formula and Shrinkage"
sources: [camii-sm-8, camii-sms-3-q6]
requires: [math/probability/distributions/exponential-family, math/statistics/bayesian/conjugate-priors]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Sections 3.2.4-3.2.5 (Bayesian posterior and empirical Bayes) and Example Sheet 3 (question 6), in our own wording; proofs written out in steps. The James-Stein estimator is stated without proof, as in the source. -->

The exponential family density is symmetric in the natural parameter and the sufficient statistic, so the posterior of the natural parameter is again of exponential-family form, now with the roles exchanged.

::: {#prp-exponential-family-posterior .proposition name="Posterior of the natural parameter"}

Let $Y\mid\eta$ have density $p(y;\eta)=b(y)e^{\eta y-a(\eta)}$ and let $\eta$ have a prior density $\pi(\eta)$. Then, with $f(y)=\int\pi(\eta)p(y;\eta)\,d\eta$ the marginal density of $Y$,
$$\pi(\eta\mid Y=y)=\exp\Bigl\{y\eta-\log\frac{f(y)}{b(y)}\Bigr\}\,\pi(\eta)e^{-a(\eta)} .$$
This is an exponential family in the variable $\eta$, with "natural parameter" $y$, sufficient statistic $\eta$, base density $\pi(\eta)e^{-a(\eta)}$ and log partition function $\log\{f(y)/b(y)\}$.

:::

::: {.proof}

1. Bayes' formula gives $\pi(\eta\mid y)=\pi(\eta)p(y;\eta)/f(y)=\pi(\eta)\,b(y)e^{\eta y-a(\eta)}/f(y)$.

2. Write $b(y)/f(y)=\exp\{-\log(f(y)/b(y))\}$ and collect the factor $e^{y\eta}$.

:::

Applying @prp-exponential-family-moments to this family (its log partition function is a function of $y$) gives the posterior mean directly. For the normal case this is Tweedie's formula.

::: {#thm-tweedie .theorem name="Tweedie's formula"}

Let $\mu\sim\pi$ have an arbitrary prior density and $Y\mid\mu\sim N(\mu,\sigma^2)$ with $\sigma^2$ known, with marginal density $f$ of $Y$. Then
$$E[\mu\mid Y]=Y+\sigma^2\,\frac{f'(Y)}{f(Y)} .$$

:::

::: {.proof}

1. Write the $N(\mu,\sigma^2)$ density as $\exp\{\mu y/\sigma^2-\mu^2/(2\sigma^2)\}\cdot(2\pi\sigma^2)^{-1/2}e^{-y^2/(2\sigma^2)}$: an exponential family in $\eta=\mu/\sigma^2$ with $T(y)=y$ and $b(y)\propto e^{-y^2/(2\sigma^2)}$.

2. By @prp-exponential-family-posterior the posterior of $\eta$ is an exponential family with natural parameter $y$ and log partition function $\psi(y)=\log\{f(y)/b(y)\}$. By @prp-exponential-family-moments its mean is $E[\eta\mid y]=\psi'(y)$.

3. $\psi'(y)=f'(y)/f(y)-b'(y)/b(y)=f'(y)/f(y)+y/\sigma^2$.

4. Multiplying by $\sigma^2$, $E[\mu\mid y]=\sigma^2E[\eta\mid y]=y+\sigma^2f'(y)/f(y)$.

:::

The posterior mean depends on the prior only through the marginal density $f$, which can be estimated from the data. The correction $\sigma^2f'/f$ is *shrinkage*: it moves $Y$ toward regions where $f$ is large and so reduces variance at the price of bias.

::: {#exm-tweedie-normal-prior .example name="A normal prior"}

If $\mu\sim N(0,\tau^2)$ then $Y\sim N(0,\sigma^2+\tau^2)$ and $f'(y)/f(y)=-y/(\sigma^2+\tau^2)$, so
$$E[\mu\mid Y]=Y\Bigl(1-\frac{\sigma^2}{\sigma^2+\tau^2}\Bigr)=\frac{\tau^2}{\sigma^2+\tau^2}\,Y,$$
the familiar conjugate update of @thm-normal-normal-update with prior mean $0$. For $\sigma=1$, $\tau=2$ and $Y=3$ it equals $2.4$.

:::

::: {#fig-tweedies-formula-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.9cm]
\draw[->, muted] (-4.3,0) -- (4.5,0) node[lab, right] {$y$};
\draw[->, muted] (0,-3.8) -- (0,4.3);
\draw[faint, domain=-4:4] plot (\x,\x);
\draw[emph, primary, domain=-4:4] plot (\x,{0.8*\x});
\node[lab] at (3.6,3.9) {$y$ (MLE)};
\node[lab] at (3.5,1.9) {$E[\mu\mid y]$};
\draw[hl] (3,3) -- (3,2.4);
\node[small vertex] at (3,3) {};
\node[small vertex] at (3,2.4) {};
\end{tikzpicture}
\end{center}
```

With $\sigma=1$ and $\tau=2$ the posterior mean is $0.8y$: every observation is pulled toward $0$, here by $20\%$ (arrow at $y=3$).

:::

When the prior is unknown, *empirical Bayes* estimates it from the data: for $Y_i\sim N(\mu_i,\sigma^2)$ with $\mu_i$ iid from an unknown $\pi$, @thm-tweedie shows that only the marginal density of the $Y_i$ is needed. This explains the *James–Stein estimator* $\bigl(1-\frac{(p-2)\sigma^2}{\|Y\|^2}\bigr)Y$ of $\mu\in\mathbb R^p$ ($p\ge3$): it is the estimator of the form of @exm-tweedie-normal-prior with the shrinkage factor estimated from $\|Y\|^2$ (derived under $\mu_i\sim N(0,\tau^2)$, using $E\{(p-2)/\chi^2_p\}=1$). It has strictly smaller mean squared error than the MLE $Y$ for every value of $\mu$, even if the normal prior is wrong, which is a proof-level result of the Principles of Statistics course.
