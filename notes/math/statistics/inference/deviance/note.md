---
title: "Deviance and Deviance Residuals"
sources: [camii-sm-9, camii-sm-10, camii-sms-3-q7]
requires: [math/statistics/inference/exponential-family-inference]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Sections 3.3.4-3.3.5 and 3.4.2 and Example Sheets 3 (questions 7, 12) and 4 (question 6a), in our own wording; proofs written out in steps. The residual comparison for the gamma family (skewness $0.00$ against $0.89$) is our own simulation with $10^6$ draws. The Bartlett correction is only mentioned. Deviance additivity for nested GLMs is in the note on analysis of deviance. -->

In the normal model the squared distance $(y-\mu)^2$ measures how far an observation is from a fitted mean. The deviance extends this to every exponential family.

::: {#def-deviance .definition name="Deviance" related="def-kl-divergence"}

In a one-parameter exponential family (@def-exponential-family with $T(y)=y$) the *deviance* of $\eta_2$ from $\eta_1$ is
$$D(\eta_1,\eta_2)=2E_{\eta_1}\Bigl[\log\frac{p(Y;\eta_1)}{p(Y;\eta_2)}\Bigr]=2\bigl\{(\eta_1-\eta_2)\mu_1-a(\eta_1)+a(\eta_2)\bigr\},\qquad\mu_1=a'(\eta_1).$$
It is twice the Kullback–Leibler divergence. With a slight abuse of notation $D(\mu_1,\mu_2)$ denotes the same quantity in the mean parametrisation. For vectors, $D^{(n)}(\mu,\tilde\mu)=\sum_iD(\mu_i,\tilde\mu_i)$ is the *total deviance*.

:::

Since $\mu_1=a'(\eta_1)$, the formula can be rewritten as $D(\eta_1,\eta_2)=2\{a(\eta_2)-a(\eta_1)-(\eta_2-\eta_1)a'(\eta_1)\}$: it is twice the gap between the convex function $a$ and its tangent at $\eta_1$, evaluated at $\eta_2$ (@fig-deviance-1). It is not symmetric and does not satisfy the triangle inequality, but it behaves like squared distance locally.

::: {#fig-deviance-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.7cm,y=1.1cm]
\draw[->, muted] (-1.6,0) -- (1.8,0) node[lab, right] {$\eta$};
\draw[emph, primary, domain=-1.5:1.4, samples=60] plot (\x,{exp(\x)});
\draw[faint, domain=-1.2:1.4] plot (\x,{1+\x});
\draw[hl] (1,2) -- (1,2.718);
\draw[faint] (0,0) -- (0,1);
\draw[faint] (1,0) -- (1,2);
\node[small vertex] at (0,1) {};
\node[small vertex] at (1,2.718) {};
\node[lab, below] at (0,0) {$\eta_1$};
\node[lab, below] at (1,0) {$\eta_2$};
\node[lab, right] at (1,2.35) {$D/2$};
\node[lab, left] at (-0.2,1.5) {tangent at $\eta_1$};
\node[lab] at (-1,2.2) {$a(\eta)=e^\eta$};
\end{tikzpicture}
\end{center}
```

For the Poisson family, $a(\eta)=e^\eta$. The deviance of $\eta_2=1$ from $\eta_1=0$ (means $\mu_1=1$, $\mu_2=e$) is twice the vertical gap between the curve and its tangent at $\eta_1$: $D=2(e-2)=1.436$.

:::

::: {#exm-deviance-formulas .example name="Deviances of standard families"}

1. Normal $N(\mu,1)$: $a=\eta^2/2$ gives $D(\mu_1,\mu_2)=(\mu_1-\mu_2)^2$.
2. Poisson: $D(\mu_1,\mu_2)=2\bigl(\mu_1\log\frac{\mu_1}{\mu_2}-\mu_1+\mu_2\bigr)$. At $\mu_1=1,\mu_2=e$ this is $2(-1-1+e)=1.436$.
3. $\mathrm{Binomial}(m,\pi)$ with $m$ fixed: $D(\pi_1,\pi_2)=2m\bigl(\pi_1\log\frac{\pi_1}{\pi_2}+(1-\pi_1)\log\frac{1-\pi_1}{1-\pi_2}\bigr)$.
4. Gamma with shape $\alpha$ and mean $\mu$: $D(\mu_1,\mu_2)=2\alpha\bigl(\log\frac{\mu_2}{\mu_1}+\frac{\mu_1}{\mu_2}-1\bigr)$.

In a model with dispersion $\phi$ (@def-exponential-dispersion-family) the deviance is computed in the family with $\phi=1$ and the log-likelihood differences carry an extra factor $1/\phi$.

:::

::: {#prp-deviance-local .proposition name="Deviance is locally squared distance"}

$D(\eta_1,\eta_2)\approx V(\eta_1)(\eta_2-\eta_1)^2$ for $\eta_2$ near $\eta_1$, where $V=a''$ is the Fisher information of one observation. For $n$ independent observations from the same member, $D^{(n)}(\eta_1,\eta_2)=nD(\eta_1,\eta_2)$.

:::

::: {.proof}

1. Taylor-expand $a(\eta_2)=a(\eta_1)+(\eta_2-\eta_1)a'(\eta_1)+\frac12(\eta_2-\eta_1)^2a''(\eta_1)+\dots$ in the tangent form of $D$; the first two terms cancel and the remainder is $2\cdot\frac12(\eta_2-\eta_1)^2V(\eta_1)$.

2. The log likelihood ratio of $n$ independent observations is a sum of $n$ identical terms, and so is its expectation.

:::

::: {#thm-deviance-lrt .theorem name="The likelihood ratio statistic is a deviance"}

For an iid sample from a regular one-parameter family, the likelihood ratio statistic for $H_0:\eta=\eta_0$ against $H_1:\eta\ne\eta_0$ is
$$2\{\ell(\hat\eta)-\ell(\eta_0)\}=D^{(n)}(\hat\eta,\eta_0)=nD(\hat\eta,\eta_0),$$
and under $H_0$ it converges in distribution to $\chi^2_1$.

:::

::: {.proof}

1. By @thm-iid-exponential-family, $2\{\ell(\hat\eta)-\ell(\eta_0)\}=2n\{(\hat\eta-\eta_0)\bar Y-a(\hat\eta)+a(\eta_0)\}$. Since $\mu(\hat\eta)=\bar Y$ (@thm-exponential-family-mle), this is $2n\{(\hat\eta-\eta_0)\mu(\hat\eta)-a(\hat\eta)+a(\eta_0)\}=nD(\hat\eta,\eta_0)$.

2. By @prp-deviance-local, $nD(\hat\eta,\eta_0)\approx nV(\eta_0)(\hat\eta-\eta_0)^2$ (the approximation is justified by $\hat\eta\to\eta_0$).

3. By @thm-exponential-family-mle, $\sqrt{nV(\eta_0)}(\hat\eta-\eta_0)\to N(0,1)$, and the square of a standard normal is $\chi^2_1$. Slutsky's theorem (@thm-slutsky) handles the approximation.

:::

::: {#def-deviance-residual .definition name="Deviance and Pearson residuals"}

For the mean $\bar Y$ of an iid sample with true mean $\mu$, the *deviance residual* and the *Pearson residual* are
$$R_D=\operatorname{sign}(\bar Y-\mu)\sqrt{D^{(n)}(\bar Y,\mu)},\qquad R_P=\frac{\bar Y-\mu}{\sqrt{V(\mu)/n}}.$$
In the normal model with unit variance both reduce to $\sqrt n(\bar Y-\mu)$.

:::

By @thm-deviance-lrt, $R_D^2\to\chi^2_1$, so $R_D\to N(0,1)$, and so does $R_P$ by the central limit theorem. For small $n$ the deviance residual is usually much closer to normal than the Pearson residual, because it removes much of the skewness.

::: {#exm-deviance-residual-gamma .example name="Gamma observations"}

Let $Y\sim\mathrm{Gamma}(\alpha=5,\beta=1)$ (one observation, $n=1$, $\mu=5$), so the Pearson residual is $(Y-5)/\sqrt5$ and the deviance residual is $\operatorname{sign}(Y-5)\sqrt{10(\log(5/Y)+Y/5-1)}$. The skewness of the Gamma law is $2/\sqrt\alpha=0.894$, and this is exactly the skewness of $R_P$. A simulation of $10^6$ draws gives skewness $0.00$ for $R_D$, mean $-0.15$ and standard deviation $1.00$: the deviance residual is symmetric to this accuracy, with a small shift in the mean. A normal quantile plot of $R_D$ is close to a straight line, that of $R_P$ is visibly curved.

:::

The refinement known as the *Bartlett correction* expresses $R_D$ as $N(-a_n,(1+b_n)^2)$ up to an error $O_p(n^{-3/2})$, where $a_n=O(n^{-1/2})$ depends on the skewness and $b_n=O(n^{-1})$ on the skewness and kurtosis, which explains the accuracy of the normal approximation of $R_D$ in small samples.
