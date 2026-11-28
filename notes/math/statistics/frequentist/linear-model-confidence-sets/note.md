---
title: "Confidence Ellipsoids in the Normal Linear Model"
sources: [camib-st-14, camib-sts-3-q11]
requires: [math/statistics/frequentist/regression-inference, math/statistics/frequentist/gaussian-projections]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 14 and Example Sheet 3 (question 11), in our own wording; proofs written out in steps. The $t$-interval for a single coefficient is in math/statistics/frequentist/regression-inference. -->

A confidence interval for one coefficient is a statement about a single direction in the parameter space. For all coefficients at once the pivot is a quadratic form, and the confidence set is an ellipsoid.

::: {#thm-ellipsoid-pivot .theorem name="Pivot for the whole coefficient vector"}

In the normal linear model $Y\sim N_n(X\beta,\sigma^2I_n)$ with $X$ of full column rank $p$, let $\hat\beta$ be the least squares estimator and $\hat\sigma^2=\|Y-X\hat\beta\|^2/(n-p)$. Then
$$\frac{(\hat\beta-\beta)^{\mathsf T}X^{\mathsf T}X(\hat\beta-\beta)}{\sigma^2}\sim\chi^2_p,\qquad\frac{\|X(\hat\beta-\beta)\|^2}{p\,\hat\sigma^2}\sim F_{p,\,n-p},$$
and the second quantity is a pivot for $(\beta,\sigma^2)$.

:::

::: {.proof}

1. By @thm-gaussian-linear-model, $\hat\beta\sim N_p(\beta,\sigma^2(X^{\mathsf T}X)^{-1})$. Let $B=(X^{\mathsf T}X)^{1/2}$ be the symmetric positive definite square root. Then $B(\hat\beta-\beta)\sim N_p(0,\sigma^2B(X^{\mathsf T}X)^{-1}B)=N_p(0,\sigma^2I_p)$ (@thm-jointly-gaussian-properties).

2. Hence $\|B(\hat\beta-\beta)\|^2/\sigma^2=(\hat\beta-\beta)^{\mathsf T}X^{\mathsf T}X(\hat\beta-\beta)/\sigma^2\sim\chi^2_p$, and the numerator $\|X(\hat\beta-\beta)\|^2$ equals this quadratic form.

3. $(n-p)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p}$ and is independent of $\hat\beta$ (@thm-gaussian-linear-model, part 4), hence of the quadratic form.

4. The ratio $\bigl(\text{form}/\sigma^2\bigr)/p$ over $\bigl((n-p)\hat\sigma^2/\sigma^2\bigr)/(n-p)$ is $F_{p,n-p}$ (@def-f-distribution); the unknown $\sigma^2$ cancels, so its law is free of the parameters.

:::

::: {#cor-confidence-ellipsoid .corollary name="Confidence ellipsoid"}

The set
$$C(Y)=\Bigl\{b\in\mathbb R^p:\ (\hat\beta-b)^{\mathsf T}X^{\mathsf T}X(\hat\beta-b)\le p\,\hat\sigma^2F_{p,n-p}(\alpha)\Bigr\}$$
satisfies $P_{\beta,\sigma^2}(\beta\in C(Y))=1-\alpha$ for all $\beta$ and $\sigma^2$. It is an ellipsoid centred at $\hat\beta$, with principal axes along the eigenvectors of $X^{\mathsf T}X$ and semi-axis lengths proportional to $\lambda_j^{-1/2}$ for the eigenvalues $\lambda_j$ of $X^{\mathsf T}X$.

:::

::: {.proof}

The event $\{\beta\in C(Y)\}$ is $\{\|X(\hat\beta-\beta)\|^2/(p\hat\sigma^2)\le F_{p,n-p}(\alpha)\}$, which has probability $1-\alpha$ by @thm-ellipsoid-pivot. In the eigenbasis of the positive definite matrix $X^{\mathsf T}X$ the defining inequality reads $\sum_j\lambda_jc_j^2\le r^2$ for the coordinates $c_j$ of $b-\hat\beta$, an ellipsoid with semi-axes $r/\sqrt{\lambda_j}$.

:::

::: {#fig-linear-model-confidence-sets-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->, muted] (-3,0) -- (3.2,0) node[lab, right] {$\beta_1$};
\draw[->, muted] (0,-2) -- (0,2.2) node[lab, above] {$\beta_2$};
\draw[emph, rotate=30] (0,0) ellipse (2.3 and 0.9);
\node[hl dot] at (0,0) {};
\node[lab, below left] at (0,0) {$\hat\beta$};
\draw[hl] (-1.6,-0.65) -- (1.6,-0.65);
\draw[hl] (-1.6,0.65) -- (1.6,0.65);
\draw[faint] (-1.6,-1.7) -- (-1.6,1.7);
\draw[faint] (1.6,-1.7) -- (1.6,1.7);
\end{tikzpicture}
\end{center}
```

A joint confidence ellipsoid for $(\beta_1,\beta_2)$ (heavy curve) and the rectangle formed by the two individual intervals (lines). The ellipsoid is tilted when the columns of $X$ are correlated; the two regions differ in shape and in joint coverage.

:::

::: {#rmk-joint-versus-marginal .remark name="Joint versus individual statements"}

The rectangle of individual $t$-intervals does not have joint coverage $1-\alpha$, since each interval controls only one coordinate; shrinking the individual levels to $\alpha/p$ (Bonferroni, @prp-bonferroni-test) gives a conservative joint rectangle, while the ellipsoid has exact joint coverage. A hypothesis $H_0:\beta=\beta_0$ is rejected at level $\alpha$ exactly when $\beta_0\notin C(Y)$, the $F$-test of @thm-f-test-linear-hypothesis with $G=I$.

:::
