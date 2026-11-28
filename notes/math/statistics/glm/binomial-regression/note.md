---
title: "Binomial Regression, Link Functions and the Odds Ratio"
sources: [camii-sm-16, camii-sms-4-q1, camii-sms-4-q4, camii-sms-4-q7, camii-sms-4-q9]
requires: [math/statistics/glm/glm-canonical-form]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 4.7, and Example Sheet 4 (questions 1, 4, 7, 9), in our own wording; proofs written out in steps. The numbers in the odds-ratio example and the curves in the figure are our own and checked by computation. Gradient-descent training of the logistic model is in ai/machine-learning/logistic-regression. -->

In binomial regression $Y_i\sim\mathrm{Binomial}(n_i,\mu_i)$ independently, with $n_i$ known, and the success probability depends on covariates through $g(\mu_i)=X_i^{\mathsf T}\beta$. The proportion $Y_i/n_i$ is a dispersion-family variable with $\phi=1$ and weight $w_i=n_i$ (@exm-natural-parametrisations), and its canonical parameter is the *log odds* $\theta=\log\frac{\mu}{1-\mu}$. The canonical link is therefore the *logit* $g(\mu)=\log\{\mu/(1-\mu)\}$; its inverse is the logistic function. Any strictly increasing $g:(0,1)\to\mathbb R$ will do as a link; if $g^{-1}=F$ is a continuous distribution function, $g$ is its quantile function.

::: {#exm-binomial-links .example name="Common links"}

1. *logit*: $g(\mu)=\log\frac\mu{1-\mu}$, $g^{-1}=$ logistic distribution function.
2. *probit*: $g(\mu)=\Phi^{-1}(\mu)$, $g^{-1}=\Phi$ the standard normal distribution function.
3. *complementary log–log*: $g(\mu)=\log\{-\log(1-\mu)\}$, $g^{-1}(\eta)=1-\exp(-e^\eta)$.
4. identity: $g(\mu)=\mu$ (only valid if the predictor stays in $(0,1)$).

:::

::: {#fig-binomial-regression-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=3cm]
\draw[->, muted] (-3.3,0) -- (3.5,0) node[lab, right] {$\eta$};
\draw[->, muted] (0,-0.05) -- (0,1.1);
\node[tick, left] at (0,1) {$1$};
\draw[emph, primary] plot coordinates {(-3,0.047) (-2.5,0.076) (-2,0.119) (-1.5,0.182) (-1,0.269) (-0.5,0.378) (0,0.5) (0.5,0.622) (1,0.731) (1.5,0.818) (2,0.881) (2.5,0.924) (3,0.953)};
\draw[emph, hl] plot coordinates {(-3,0.001) (-2.5,0.006) (-2,0.023) (-1.5,0.067) (-1,0.159) (-0.5,0.309) (0,0.5) (0.5,0.691) (1,0.841) (1.5,0.933) (2,0.977) (2.5,0.994) (3,0.999)};
\draw[emph] plot coordinates {(-3,0.049) (-2.5,0.079) (-2,0.127) (-1.5,0.2) (-1,0.308) (-0.5,0.455) (0,0.632) (0.5,0.808) (1,0.934) (1.5,0.989) (2,0.999) (2.5,1) (3,1)};
\node[lab] at (-1.6,0.55) {logit};
\node[lab] at (-2.3,0.05) {probit};
\node[lab] at (1.3,0.95) {cloglog};
\end{tikzpicture}
\end{center}
```

The inverse links $\mu=g^{-1}(\eta)$ for logit (blue), probit and complementary log–log. Logit and probit are symmetric about $\eta=0$; the complementary log–log curve is not.

:::

The link has a *latent variable* interpretation. Suppose $Y^*=\eta+\varepsilon$ with $\varepsilon$ independent noise of distribution function $F$ and one observes only the sign, $Y=\mathbf 1\{Y^*>0\}$.

::: {#prp-latent-variable .proposition name="Latent variable interpretation of links"}

1. If $F$ is symmetric about $0$, then $\mu=P(Y=1)=F(\eta)$, i.e. the link is $g=F^{-1}$: probit for normal noise, logit for logistic noise.
2. If $Y^*\sim\mathrm{Poisson}(e^\eta)$ and $Y=\mathbf 1\{Y^*>0\}$, then $\mu=1-\exp(-e^\eta)$: the complementary log–log link.
3. If $Y_i^*=f(X_i^{\mathsf T}\beta^*+\varepsilon_i)$ with $f$ strictly increasing and $\varepsilon_i\sim N(0,\sigma^2)$ iid, and one observes $Y_i=\mathbf 1\{Y_i^*>c\}$ where the first coordinate of $X_i$ is $1$, then $Y_i$ are independent Bernoulli with $E[Y_i]=\Phi(X_i^{\mathsf T}\beta)$, $\beta=(\beta^*_1-f^{-1}(c),\beta_2^*,\dots,\beta_p^*)/\sigma$ (a probit model).

:::

::: {.proof}

1. $P(Y^*>0)=P(\varepsilon>-\eta)=1-F(-\eta)=F(\eta)$ by symmetry.

2. $1-\mu=P(Y=0)=P(Y^*=0)=\exp(-e^\eta)$, so $\mu=1-\exp(-e^\eta)$ and $\log\{-\log(1-\mu)\}=\eta$.

3. $Y_i=1$ iff $f(X_i^{\mathsf T}\beta^*+\varepsilon_i)>c$ iff $\varepsilon_i>f^{-1}(c)-X_i^{\mathsf T}\beta^*$ (as $f$ is strictly increasing). By symmetry of the normal law, $P(Y_i=1)=\Phi\{(X_i^{\mathsf T}\beta^*-f^{-1}(c))/\sigma\}$. Absorbing the shift $-f^{-1}(c)$ in the intercept (first coordinate $1$) gives $X_i^{\mathsf T}\beta$ with the stated $\beta$. Independence follows from independence of the $\varepsilon_i$.

:::

So one can fit a linear model to the unobserved $Y^*$ from sign data alone when the noise law is known. Hence the fitted coefficient is not the coefficient of the original linear model, only that coefficient divided by the noise standard deviation.

::: {#prp-binary-logistic-loglik .proposition name="Logistic log-likelihood in $\pm1$ form"}

For binary responses $Y_i\in\{0,1\}$ with the canonical link, put $\tilde Y_i=2Y_i-1\in\{-1,1\}$. The log-likelihood is
$$\ell(\beta)=-\sum_{i=1}^n\log\bigl(1+\exp(-\tilde Y_iX_i^{\mathsf T}\beta)\bigr).$$

:::

::: {.proof}

1. With $\mu_i=\{1+e^{-\eta_i}\}^{-1}$ and $\eta_i=X_i^{\mathsf T}\beta$, $\log P(Y_i=1)=-\log(1+e^{-\eta_i})$ and $\log P(Y_i=0)=\log\frac{e^{-\eta_i}}{1+e^{-\eta_i}}=-\log(1+e^{\eta_i})$.

2. If $\tilde Y_i=1$ the term is the first of these, and if $\tilde Y_i=-1$ the second; both equal $-\log(1+\exp(-\tilde Y_i\eta_i))$.

:::

This is the logistic loss of machine learning (@def-logistic-regression) written with $\pm1$ labels.

*Odds ratios.* With the logit link the odds $\mu_i/(1-\mu_i)=e^{\eta_i}=\prod_je^{\beta_jX_{ij}}$ are multiplied by $e^{\beta_j}$ per unit increase of the $j$th regressor (not necessarily a causal effect). For a single binary regressor $X$ the saturated model $\operatorname{logit}\mu=\beta_0+\beta_1X$ gives the *odds ratio*
$$\frac{P(Y=1\mid X=1)/P(Y=0\mid X=1)}{P(Y=1\mid X=0)/P(Y=0\mid X=0)}=e^{\beta_1}.$$

::: {#thm-odds-ratio-symmetry .theorem name="Symmetry of the odds ratio and case-control sampling"}

1. The odds ratio is symmetric in $X$ and $Y$:
$$\frac{P(Y=1\mid X=1)/P(Y=0\mid X=1)}{P(Y=1\mid X=0)/P(Y=0\mid X=0)}=\frac{P(X=1\mid Y=1)/P(X=0\mid Y=1)}{P(X=1\mid Y=0)/P(X=0\mid Y=0)} .$$
2. (Retrospective sampling.) Let $(Y_i,X_i)$ follow $\log\frac{\pi_i}{1-\pi_i}=\alpha+X_i^{\mathsf T}\beta$ with $\pi_i=P(Y_i=1)$, and let $Z_i\in\{0,1\}$ indicate that the unit is sampled, with $P(Z_i=1\mid Y_i=1)=p_1$ and $P(Z_i=1\mid Y_i=0)=p_0$. Then
$$\frac{P(Y_i=1\mid Z_i=1)}{1-P(Y_i=1\mid Z_i=1)}=\frac{p_1}{p_0}\exp(\alpha+X_i^{\mathsf T}\beta).$$
So $\beta$ can be estimated from a sample chosen by the response (e.g. all cases and a few controls), but $\alpha$ cannot, since $p_1/p_0$ is unknown.

:::

::: {.proof}

1. Both sides equal $\dfrac{P(X=1,Y=1)P(X=0,Y=0)}{P(X=0,Y=1)P(X=1,Y=0)}$, after cancelling the marginal probabilities of $X$ in the left side and of $Y$ in the right side.

2. By Bayes' rule, $\dfrac{P(Y_i=1\mid Z_i=1)}{P(Y_i=0\mid Z_i=1)}=\dfrac{P(Z_i=1\mid Y_i=1)\,\pi_i}{P(Z_i=1\mid Y_i=0)(1-\pi_i)}=\dfrac{p_1}{p_0}\cdot\dfrac{\pi_i}{1-\pi_i}$. Substituting the logistic model gives the result.

:::

For a rare disease the odds ratio approximates the more interpretable risk ratio $P(Y=1\mid X=1)/P(Y=1\mid X=0)$, since $P(Y=0)\approx1$.

::: {#exm-odds-ratio .example name="The same odds ratio both ways"}

Let $P(X=1)=0.5$, $P(Y=1\mid X=1)=0.4$ and $P(Y=1\mid X=0)=0.2$. Then the odds are $2/3$ and $1/4$, so the odds ratio is $8/3=2.67$ and $\beta_1=\log(8/3)=0.98$. The joint probabilities are $(Y,X)$: $(1,1)=0.2$, $(0,1)=0.3$, $(1,0)=0.1$, $(0,0)=0.4$. Conditioning on $Y$: $P(X=1\mid Y=1)=2/3$ (odds $2$) and $P(X=1\mid Y=0)=3/7$ (odds $3/4$), so the reversed odds ratio is $2/(3/4)=8/3$ again.

:::
