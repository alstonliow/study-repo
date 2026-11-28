---
title: "Prediction Error, Bias and Variance, and Mallows' C_p"
sources: [camii-sm-5, camii-sms-1-q8, camii-sms-2-q3]
requires: [math/statistics/frequentist/regression-inference, math/statistics/frequentist/misspecified-linear-models]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 2.5.2 and the first half of 2.5.3, and Example Sheets 1 (question 8) and 2 (question 3), in our own wording; proofs written out in steps. The numerical example (coefficients $1/j$) is our own and checked by computation. A different bias-variance statement for general learning algorithms is in ai/machine-learning/bias-variance-tradeoff. -->

How well will a fitted linear model predict new responses? Writing $\mu=E[\mathbf Y\mid\mathbb X]$ for the true conditional mean, which need not be of the form $\mathbb X\beta$, the question can be answered without assuming the linear model is right.

::: {#def-mspe .definition name="Mean squared prediction error"}

Let $\mathbf Y^*=\mu+\boldsymbol\varepsilon^*$ be a new response vector at the same design points, with $\boldsymbol\varepsilon^*$ independent of the data, $E[\boldsymbol\varepsilon^*]=0$ and $\operatorname{Cov}(\boldsymbol\varepsilon^*)=\sigma^2I_n$. For a fit $\hat\mu$, the *mean squared prediction error* is
$$\mathrm{MSPE}=E\bigl[\|\mathbf Y^*-\hat\mu\|^2\mid\mathbb X\bigr]=\sum_{i=1}^nE\bigl[(Y_i^*-\hat\mu_i)^2\mid\mathbb X\bigr].$$

:::

::: {#thm-linear-bias-variance .theorem name="Bias-variance decomposition for least squares" related="thm-bias-variance-decomposition"}

For the least squares fit $\hat\mu=P\mathbf Y$ with $\operatorname{rank}\mathbb X=p$, with the errors of the data uncorrelated of variance $\sigma^2$,
$$\mathrm{MSPE}=\underbrace{\|(I-P)\mu\|^2}_{\text{bias}^2}+\underbrace{p\,\sigma^2}_{\text{variance}}+\underbrace{n\sigma^2}_{\text{irreducible}} .$$

:::

::: {.proof}

1. Write $\mathbf Y^*-\hat\mu=(\mu-E[\hat\mu])+(E[\hat\mu]-\hat\mu)+\boldsymbol\varepsilon^*$. The three terms are respectively deterministic, centred, and centred and independent of the other two, so all cross terms in $E\|\cdot\|^2$ vanish (this step does not use how $\hat\mu$ was obtained).

2. For the least squares fit $E[\hat\mu\mid\mathbb X]=P\mu$, so the first term has squared norm $\|\mu-P\mu\|^2=\|(I-P)\mu\|^2$.

3. $\hat\mu-E\hat\mu=P(\mathbf Y-\mu)=P\boldsymbol\varepsilon$ with $E\|P\boldsymbol\varepsilon\|^2=\sigma^2\operatorname{tr}(P^{\mathsf T}P)=\sigma^2\operatorname{tr}P=p\sigma^2$ (@prp-projection-rank-trace).

4. $E\|\boldsymbol\varepsilon^*\|^2=n\sigma^2$.

:::

Averaging over observations gives $\frac1n\mathrm{MSPE}=\frac1n\|(I-P)\mu\|^2+\frac{p\sigma^2}n+\sigma^2$. A richer model (larger $p$, bigger column space) shrinks the bias term but increases the variance term $p\sigma^2/n$: the *bias-variance trade-off*. The complexity of a least squares fit is its number of free parameters $p=\operatorname{tr}P$.

::: {#exm-bias-variance-curve .example name="Choosing the number of regressors"}

Take $n=20$, $\sigma^2=1$ and orthonormal regressors, so that $\frac1n\|(I-P)\mu\|^2=\sum_{j>p}\theta_j^2$ for coefficients $\theta_j=1/j$, $j\le10$ (and $0$ afterwards). The excess prediction error $\frac1n\|(I-P)\mu\|^2+p/20$ above the irreducible $\sigma^2$ is

| $p$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| bias$^2$ | 1.550 | 0.550 | 0.300 | 0.189 | 0.126 | 0.086 | 0.058 | 0.038 |
| variance | 0 | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 | 0.35 |
| total | 1.550 | 0.600 | 0.400 | 0.339 | **0.326** | 0.336 | 0.358 | 0.388 |

The minimum is at $p=4$ (@fig-prediction-error-in-linear-models-1).

:::

::: {#fig-prediction-error-in-linear-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=3cm]
\draw[->, muted] (0,0) -- (9,0) node[lab, right] {$p$};
\draw[->, muted] (0,0) -- (0,1.1);
\foreach \x in {0,2,4,6,8} \node[tick, below] at (\x,0) {$\x$};
\draw[emph, primary] plot coordinates {(1,0.5498) (2,0.2998) (3,0.1887) (4,0.1262) (5,0.0862) (6,0.0584) (7,0.038) (8,0.0223)};
\draw[emph, hl] plot coordinates {(0,0) (8,0.4)};
\draw[emph] plot coordinates {(1,0.6) (2,0.4) (3,0.3387) (4,0.3262) (5,0.3362) (6,0.3584) (7,0.388) (8,0.4223)};
\node[lab] at (2.6,0.2) {bias$^2$};
\node[lab] at (7.6,0.1) {variance $p/20$};
\node[lab] at (6.3,0.55) {total};
\end{tikzpicture}
\end{center}
```

Excess prediction error as a function of $p$: bias$^2$ decreases, variance increases, and the total is smallest at $p=4$. The point $p=0$ (total $1.55$) is off the scale.

:::

The bias term involves the unknown $\mu$, so the decomposition cannot be evaluated directly. The training error $\|\mathbf Y-\hat\mu\|^2$ is computed from the same data used to fit and is too optimistic. The next result fixes this for every linear smoother.

::: {#thm-mallows-cp .theorem name="Unbiased estimation of the prediction error (Mallows' $C_p$)"}

Let $\hat\mu=M\mathbf Y$ where the matrix $M$ depends on the data only through $\mathbb X$, and the errors have covariance $\sigma^2I_n$. Then
$$C_M=\|\mathbf Y-\hat\mu\|^2+2\sigma^2\operatorname{tr}(M)$$
is an unbiased estimator of $\mathrm{MSPE}$, conditional on $\mathbb X$. For least squares $M=P$ this is *Mallows' $C_p$*: $C_p=\|\mathbf Y-\hat\mu\|^2+2p\sigma^2$, and $\operatorname{tr}M$ plays the role of the degrees of freedom.

:::

::: {.proof}

1. $E\|\mathbf Y-M\mathbf Y\|^2=\|(I-M)\mu\|^2+\sigma^2\operatorname{tr}\bigl((I-M)(I-M)^{\mathsf T}\bigr)=\|(I-M)\mu\|^2+\sigma^2\bigl(n-2\operatorname{tr}M+\|M\|_F^2\bigr)$, where $\|M\|_F^2=\operatorname{tr}(MM^{\mathsf T})$.

2. For the new response, as in the proof of @thm-linear-bias-variance, $E\|\mathbf Y^*-M\mathbf Y\|^2=\|(I-M)\mu\|^2+\sigma^2\|M\|_F^2+n\sigma^2$.

3. The difference is $\mathrm{MSPE}-E\|\mathbf Y-\hat\mu\|^2=2\sigma^2\operatorname{tr}M$, so adding this "optimism" to the training error gives an unbiased estimator.

:::

For least squares the optimism is $2p\sigma^2$, proportional to $p$. When $\sigma^2$ is unknown it is replaced by $\hat\sigma^2$ of the largest model considered. Selecting the model that minimises $C_p$ is the criterion discussed in @sec-math-statistics-frequentist-model-selection-criteria.
