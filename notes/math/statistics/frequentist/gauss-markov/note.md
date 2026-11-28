---
title: "The Gauss–Markov Theorem"
sources: [camib-st-13, camib-sts-3-q8, camii-sms-1-q7]
requires: [math/statistics/frequentist/multiple-linear-regression]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 13 and Example Sheet 3 (question 8), in our own wording; proofs written out in steps. -->

Least squares is the maximum likelihood estimator under Gaussian noise, but it is also best among linear unbiased estimators when the noise is not Gaussian at all, as long as it is uncorrelated with constant variance.

::: {#def-linear-expectation-model .definition name="Linear conditional expectation model"}

The *linear conditional expectation model* is $Y=X\beta+\varepsilon$ with $X\in\mathbb R^{n\times p}$ fixed of full column rank, $\beta\in\mathbb R^p$, and noise with
$$E(\varepsilon)=0,\qquad\mathrm{Cov}(\varepsilon)=\sigma^2I_n .$$
No distribution is assumed for $\varepsilon$. An estimator of $\beta$ is *linear* if it has the form $\tilde\beta=AY$ for a fixed matrix $A\in\mathbb R^{p\times n}$.

:::

::: {#thm-gauss-markov .theorem name="Gauss–Markov theorem (BLUE)"}

In the linear conditional expectation model let $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$ be the least squares estimator and $\tilde\beta=AY$ any linear unbiased estimator of $\beta$. Then
$$\mathrm{Cov}(\tilde\beta)-\mathrm{Cov}(\hat\beta)\ \text{is positive semidefinite},$$
so $\mathrm{Var}(a^{\mathsf T}\hat\beta)\le\mathrm{Var}(a^{\mathsf T}\tilde\beta)$ for every $a\in\mathbb R^p$: $\hat\beta$ is the *best linear unbiased estimator* (BLUE).

:::

::: {.proof}

1. $\hat\beta$ is linear, with matrix $A_0=(X^{\mathsf T}X)^{-1}X^{\mathsf T}$, and unbiased: $E\hat\beta=A_0X\beta=\beta$. Its covariance is $\sigma^2A_0A_0^{\mathsf T}=\sigma^2(X^{\mathsf T}X)^{-1}$.

2. If $\tilde\beta=AY$ is unbiased, $AX\beta=\beta$ for all $\beta$, so $AX=I_p$. Put $D=A-A_0$; then $DX=AX-A_0X=I_p-I_p=0$.

3. $\mathrm{Cov}(\tilde\beta)=\sigma^2AA^{\mathsf T}=\sigma^2(A_0+D)(A_0+D)^{\mathsf T}=\sigma^2\bigl(A_0A_0^{\mathsf T}+A_0D^{\mathsf T}+DA_0^{\mathsf T}+DD^{\mathsf T}\bigr)$.

4. The cross terms vanish: $DA_0^{\mathsf T}=DX(X^{\mathsf T}X)^{-1}=0$, and $A_0D^{\mathsf T}$ is its transpose.

5. So $\mathrm{Cov}(\tilde\beta)-\mathrm{Cov}(\hat\beta)=\sigma^2DD^{\mathsf T}$, which is positive semidefinite since $v^{\mathsf T}DD^{\mathsf T}v=\|D^{\mathsf T}v\|^2\ge0$. Taking $v=a$ gives the statement about $a^{\mathsf T}\beta$.

:::

::: {#fig-gauss-markov-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[faint, rotate=25] (0,0) ellipse (2.6 and 1.3);
\draw[emph, rotate=25] (0,0) ellipse (1.4 and 0.7);
\node[small vertex] at (0,0) {};
\node[lab, below] at (0,-0.1) {$\beta$};
\node[lab, primary] at (1.2,0.9) {$\hat\beta$};
\node[lab] at (2.8,1.5) {$\tilde\beta$};
\end{tikzpicture}
\end{center}
```

Contour ellipses of the covariance matrices around the true $\beta$: the ellipse of the least squares estimator $\hat\beta$ (inner) lies inside that of any other linear unbiased estimator $\tilde\beta$ (outer), which is what $\mathrm{Cov}(\tilde\beta)\succeq\mathrm{Cov}(\hat\beta)$ says.

:::

::: {#exm-gauss-markov-mean .example name="The sample mean is BLUE"}

For $Y_i=\mu+\varepsilon_i$ the design matrix is $X=\mathbf 1$ and $\hat\beta=(\mathbf 1^{\mathsf T}\mathbf 1)^{-1}\mathbf 1^{\mathsf T}Y=\bar Y$. By @thm-gauss-markov the sample mean has the smallest variance among all unbiased estimators $\sum_ic_iY_i$ with $\sum_ic_i=1$ (which is also visible directly: $\sigma^2\sum c_i^2\ge\sigma^2/n$ by the Cauchy–Schwarz inequality).

:::

::: {#thm-gls-gauss-markov .theorem name="Gauss–Markov theorem for generalised least squares"}

Let $Y=X\beta+\varepsilon$ with $E\varepsilon=0$ and $\mathrm{Cov}(\varepsilon)=\sigma^2\Sigma$, where $\Sigma$ is a known positive definite matrix and $\sigma^2$ is unknown, and $X$ has full column rank. The generalised least squares estimator (@def-generalized-least-squares)
$$\tilde\beta_{\mathrm{GLS}}=\operatorname*{arg\,min}_\beta\,(Y-X\beta)^{\mathsf T}\Sigma^{-1}(Y-X\beta)=(X^{\mathsf T}\Sigma^{-1}X)^{-1}X^{\mathsf T}\Sigma^{-1}Y$$
is unbiased with $\mathrm{Cov}(\tilde\beta_{\mathrm{GLS}})=\sigma^2(X^{\mathsf T}\Sigma^{-1}X)^{-1}$, and it is the BLUE: for every linear unbiased estimator $\tilde\beta=AY$, $\mathrm{Cov}(\tilde\beta)-\mathrm{Cov}(\tilde\beta_{\mathrm{GLS}})$ is positive semidefinite.

:::

::: {.proof}

1. Let $\Sigma^{-1/2}$ be the symmetric positive definite square root of $\Sigma^{-1}$ and put $Y'=\Sigma^{-1/2}Y$, $X'=\Sigma^{-1/2}X$, $\varepsilon'=\Sigma^{-1/2}\varepsilon$. Then $Y'=X'\beta+\varepsilon'$ with $E\varepsilon'=0$ and $\mathrm{Cov}(\varepsilon')=\sigma^2\Sigma^{-1/2}\Sigma\Sigma^{-1/2}=\sigma^2I_n$, and $X'$ has full column rank.

2. The objective is $(Y-X\beta)^{\mathsf T}\Sigma^{-1}(Y-X\beta)=\|Y'-X'\beta\|^2$, so $\tilde\beta_{\mathrm{GLS}}$ is the ordinary least squares estimator of the transformed model, $(X'^{\mathsf T}X')^{-1}X'^{\mathsf T}Y'$, which is the stated formula.

3. $\tilde\beta=AY$ is linear in $Y$ if and only if it is linear in $Y'$, since $AY=(A\Sigma^{1/2})Y'$ and the map $A\mapsto A\Sigma^{1/2}$ is a bijection; unbiasedness is a property of the estimator and does not depend on the parametrisation of the data.

4. Applying @thm-gauss-markov to the transformed model gives the covariance ordering, and $\mathrm{Cov}(\tilde\beta_{\mathrm{GLS}})=\sigma^2(X'^{\mathsf T}X')^{-1}=\sigma^2(X^{\mathsf T}\Sigma^{-1}X)^{-1}$.

:::
