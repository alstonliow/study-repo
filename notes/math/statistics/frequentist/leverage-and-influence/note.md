---
title: "Leverage, Residuals and Influence"
sources: [camii-sm-4, camii-sms-2-q5, camii-sms-2-q6, camii-sms-2-q11, camii-sms-2-q12]
requires: [math/statistics/frequentist/regression-inference, math/statistics/frequentist/gaussian-projections]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 2.5.1 and Example Sheet 2 (questions 5, 6, 11, 12), in our own wording; proofs written out in steps. The five-point example is our own and was checked by computation (including a brute-force leave-one-out refit). -->

After fitting a linear model one asks which observations the fit depends on most, and whether the residuals look like the model says they should. Everything below is a function of the *hat matrix* $P=\mathbb X(\mathbb X^{\mathsf T}\mathbb X)^{-1}\mathbb X^{\mathsf T}$ (@def-linear-model), for which $\hat{\mathbf Y}=P\mathbf Y$.

::: {#def-leverage .definition name="Leverage"}

The *leverage* of observation $i$ is the $i$th diagonal entry $P_{ii}=X_i^{\mathsf T}(\mathbb X^{\mathsf T}\mathbb X)^{-1}X_i$ of the hat matrix. Since $\hat\mu_i=P_{ii}Y_i+\sum_{k\ne i}P_{ik}Y_k$, it measures how much $Y_i$ alone determines its own fitted value.

:::

::: {#prp-leverage-properties .proposition name="Properties of leverage"}

Let $\mathbb X$ have full column rank $p$.

1. $0\le P_{ii}\le1$ and $\sum_iP_{ii}=p$.
2. In the normal linear model the residual $\hat\varepsilon_i=Y_i-\hat\mu_i$ has $\operatorname{Var}(\hat\varepsilon_i)=\sigma^2(1-P_{ii})$.
3. For simple regression with an intercept, $P_{ii}=\dfrac1n+\dfrac{(x_i-\bar x)^2}{\sum_k(x_k-\bar x)^2}$.

:::

::: {.proof}

1. $P$ is a symmetric projection matrix, so $P_{ii}=\sum_kP_{ik}^2\ge P_{ii}^2$ (using $P=P^2=P^{\mathsf T}P$), hence $0\le P_{ii}\le1$. The trace of $P$ equals its rank $p$ (@prp-projection-rank-trace).

2. $\hat{\boldsymbol\varepsilon}=(I-P)\mathbf Y=(I-P)\boldsymbol\varepsilon$ since $(I-P)\mathbb X=0$. Hence $\operatorname{Cov}(\hat{\boldsymbol\varepsilon})=\sigma^2(I-P)(I-P)^{\mathsf T}=\sigma^2(I-P)$, and the $i$th diagonal entry is $\sigma^2(1-P_{ii})$.

3. Replacing $x$ by $x-\bar x$ does not change the column space, so use the design with columns $\mathbf 1$ and $\mathbf x-\bar x\mathbf 1$, which are orthogonal. Then $\mathbb X^{\mathsf T}\mathbb X=\operatorname{diag}(n,\sum_k(x_k-\bar x)^2)$ and $X_i^{\mathsf T}(\mathbb X^{\mathsf T}\mathbb X)^{-1}X_i=\frac1n+\frac{(x_i-\bar x)^2}{\sum_k(x_k-\bar x)^2}$.

:::

So points far from the centre of the covariates have leverage near $1$: the fitted line is forced through them and their residuals are small. Because the residual variances differ, residuals are compared after standardising.

::: {#def-studentised-residual .definition name="Standardised and externally studentised residuals"}

The *standardised* (internally studentised) residual is
$$\eta_i=\frac{\hat\varepsilon_i}{\hat\sigma\sqrt{1-P_{ii}}},\qquad\hat\sigma^2=\frac{\|(I-P)\mathbf Y\|^2}{n-p}.$$
The *externally studentised* residual replaces $\hat\sigma$ by $\hat\sigma_{(-i)}$, the estimate computed from the other $n-1$ observations:
$$\tilde\eta_i=\frac{\hat\varepsilon_i}{\hat\sigma_{(-i)}\sqrt{1-P_{ii}}}.$$

:::

Two exact identities make leave-one-out quantities cheap. They rest on the Sherman–Morrison formula $(A+uv^{\mathsf T})^{-1}=A^{-1}-\dfrac{A^{-1}uv^{\mathsf T}A^{-1}}{1+v^{\mathsf T}A^{-1}u}$.

::: {#thm-leave-one-out .theorem name="Leave-one-out formulae"}

Let $\hat\beta_{(-i)}$ be the least squares estimate computed without observation $i$, assuming $P_{ii}<1$. Then
$$\hat\beta-\hat\beta_{(-i)}=\frac{(\mathbb X^{\mathsf T}\mathbb X)^{-1}X_i\,\hat\varepsilon_i}{1-P_{ii}},\qquad\hat\mu_i=P_{ii}Y_i+(1-P_{ii})\hat\mu_{(-i)},$$
where $\hat\mu_{(-i)}=X_i^{\mathsf T}\hat\beta_{(-i)}$. Consequently $Y_i-\hat\mu_{(-i)}=\hat\varepsilon_i/(1-P_{ii})$.

:::

::: {.proof}

1. Write $A=\mathbb X^{\mathsf T}\mathbb X$. Removing a row gives $\mathbb X_{(-i)}^{\mathsf T}\mathbb X_{(-i)}=A-X_iX_i^{\mathsf T}$, and Sherman–Morrison with $u=-X_i$, $v=X_i$ gives $(A-X_iX_i^{\mathsf T})^{-1}=A^{-1}+\dfrac{A^{-1}X_iX_i^{\mathsf T}A^{-1}}{1-P_{ii}}$, because $X_i^{\mathsf T}A^{-1}X_i=P_{ii}$.

2. Also $\mathbb X_{(-i)}^{\mathsf T}\mathbf Y_{(-i)}=\mathbb X^{\mathsf T}\mathbf Y-X_iY_i$. Hence
$$\hat\beta_{(-i)}=\Bigl(A^{-1}+\tfrac{A^{-1}X_iX_i^{\mathsf T}A^{-1}}{1-P_{ii}}\Bigr)(\mathbb X^{\mathsf T}\mathbf Y-X_iY_i)=\hat\beta-A^{-1}X_iY_i+\tfrac{A^{-1}X_i(X_i^{\mathsf T}\hat\beta-P_{ii}Y_i)}{1-P_{ii}} .$$

3. Combining the terms in $A^{-1}X_i$: $-Y_i+\dfrac{\hat\mu_i-P_{ii}Y_i}{1-P_{ii}}=\dfrac{-Y_i+P_{ii}Y_i+\hat\mu_i-P_{ii}Y_i}{1-P_{ii}}=-\dfrac{\hat\varepsilon_i}{1-P_{ii}}$. This is the first formula.

4. Multiply it by $X_i^{\mathsf T}$: $\hat\mu_i-\hat\mu_{(-i)}=P_{ii}\hat\varepsilon_i/(1-P_{ii})$. Substituting $\hat\varepsilon_i=Y_i-\hat\mu_i$ and solving gives $\hat\mu_i=P_{ii}Y_i+(1-P_{ii})\hat\mu_{(-i)}$, and then $Y_i-\hat\mu_{(-i)}=(Y_i-\hat\mu_i)/(1-P_{ii})$.

:::

::: {#def-cooks-distance .definition name="Cook's distance"}

The *influence* of observation $i$ is the standardised change in all fitted values when it is removed,
$$D_i=\frac{\|\mathbb X(\hat\beta-\hat\beta_{(-i)})\|^2}{p\,\hat\sigma^2}.$$

:::

::: {#prp-cooks-distance-formula .proposition name="Cook's distance from leverage and residual"}

$$D_i=\frac1p\,\frac{P_{ii}}{1-P_{ii}}\,\eta_i^2 .$$
A value of $D_i$ above the median $F_{p,n-p}(0.5)$ of the $F_{p,n-p}$ distribution is a common warning sign, because $\{\beta:\|\mathbb X(\hat\beta-\beta)\|^2\le p\hat\sigma^2F_{p,n-p}(0.5)\}$ is the $50\%$ confidence ellipsoid of @cor-confidence-ellipsoid, and a point is influential if deleting it moves $\hat\beta$ to its boundary.

:::

::: {.proof}

1. By @thm-leave-one-out, $\|\mathbb X(\hat\beta-\hat\beta_{(-i)})\|^2=\dfrac{\hat\varepsilon_i^2}{(1-P_{ii})^2}X_i^{\mathsf T}(\mathbb X^{\mathsf T}\mathbb X)^{-1}\mathbb X^{\mathsf T}\mathbb X(\mathbb X^{\mathsf T}\mathbb X)^{-1}X_i=\dfrac{\hat\varepsilon_i^2P_{ii}}{(1-P_{ii})^2}$.

2. Divide by $p\hat\sigma^2$ and use $\hat\varepsilon_i^2/\hat\sigma^2=(1-P_{ii})\eta_i^2$.

:::

::: {#thm-external-studentised-t .theorem name="Outlier test"}

In the normal linear model with $P_{ii}<1$, $\tilde\eta_i\sim t_{n-p-1}$. Hence $H_0:\ $observation $i$ follows the model, tested against a shifted mean, is rejected when $|\tilde\eta_i|>t_{n-p-1}(\alpha/2)$.

:::

::: {.proof}

1. By @thm-leave-one-out, $\hat\varepsilon_i/(1-P_{ii})=Y_i-\hat\mu_{(-i)}$. Now $Y_i$ is independent of the other $n-1$ observations, and so of $\hat\beta_{(-i)}$ and $\hat\sigma_{(-i)}$.

2. $Y_i-\hat\mu_{(-i)}$ is normal with mean $0$ and variance $\sigma^2\bigl(1+X_i^{\mathsf T}(A-X_iX_i^{\mathsf T})^{-1}X_i\bigr)$. By step 1 of the proof of @thm-leave-one-out this equals $\sigma^2\bigl(1+P_{ii}+\tfrac{P_{ii}^2}{1-P_{ii}}\bigr)=\sigma^2/(1-P_{ii})$.

3. So $Z=\hat\varepsilon_i/\bigl(\sigma\sqrt{1-P_{ii}}\bigr)\sim N(0,1)$, independent of $\hat\sigma_{(-i)}^2$, and $(n-p-1)\hat\sigma_{(-i)}^2/\sigma^2\sim\chi^2_{n-p-1}$ by @thm-gaussian-linear-model for the reduced sample.

4. $\tilde\eta_i=Z/\sqrt{\chi^2_{n-p-1}/(n-p-1)}$ is a ratio of this type, hence $t_{n-p-1}$.

:::

The test is exact only for one observation fixed in advance. If one picks the most extreme residual out of $n$ after looking at the data, the level is no longer $\alpha$ (a multiple-testing problem).

::: {#exm-leverage-five-points .example name="One far-away point"}

Fit a line to $x=(1,2,3,4,10)$, $y=(1.1,1.9,3.2,3.9,4.0)$. Then $\hat\beta=(1.724,0.274)$ and $\hat\sigma^2=0.918$, and

| $i$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $P_{ii}$ | 0.38 | 0.28 | 0.22 | 0.20 | 0.92 |
| $\eta_i$ | $-1.19$ | $-0.46$ | $0.77$ | $1.26$ | $-1.71$ |
| $D_i$ | 0.43 | 0.04 | 0.08 | 0.20 | 16.86 |

The leverages add to $2=p$. Point 5 has an ordinary standardised residual but $D_5=16.9$, far above $F_{2,3}(0.5)=0.88$: removing it changes the fitted line a lot. The direct refit without point 5 reproduces $Y_5-\hat\mu_{(-5)}=-5.8=\hat\varepsilon_5/(1-P_{55})$.

:::

::: {#fig-leverage-and-influence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.4cm]
\draw[->, muted] (0,0) -- (10.8,0) node[lab, right] {$x$};
\draw[->, muted] (0,0) -- (0,10.5);
\draw[emph, primary] (0,1.724) -- (10.5,{1.724+0.274*10.5});
\draw[hl] (0,0.1) -- (10,9.8);
\foreach \x/\y in {1/1.1,2/1.9,3/3.2,4/3.9} \node[small vertex] at (\x,\y) {};
\node[small vertex] at (10,4.0) {};
\node[lab, above] at (9.3,4.3) {$P_{55}=0.92$};
\node[lab] at (5.2,0.8) {fit with point 5 (flat)};
\node[lab] at (4,6.5) {fit without point 5};
\end{tikzpicture}
\end{center}
```

A single point far from the others has leverage near $1$ and tilts the line. The fit without it is drawn from the four remaining points, $\hat\beta_{(-5)}\approx(0.10,0.97)$.

:::
