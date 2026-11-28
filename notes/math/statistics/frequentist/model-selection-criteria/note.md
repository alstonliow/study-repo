---
title: "Model Selection: Cross-Validation, AIC, BIC and Search Algorithms"
sources: [camii-sm-5, camii-sms-2-q4]
requires: [math/statistics/frequentist/prediction-error-in-linear-models, math/statistics/frequentist/leverage-and-influence, math/statistics/inference/fisher-information]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 2.5.3 (leave-one-out cross-validation, AIC, BIC) and 2.5.4 (best subset, forward and backward stepwise), and Example Sheet 2 (question 4), in our own wording; proofs written out in steps. The three-regressor RSS table is our own construction (the lecturer's Figure 2.7 gives no numbers) and satisfies the stated selections. Regularisation (ridge, lasso) is in regularization-and-model-selection and regression-inference; inference after selection is not covered here. -->

Given several candidate regressor sets one needs a score that rewards fit but charges for complexity. Mallows' $C_p$ (@thm-mallows-cp) is one such score for squared error; this note adds cross-validation and the two likelihood-based criteria, then the algorithms that search the exponentially many subsets.

::: {#thm-loo-cv-formula .theorem name="Leave-one-out cross-validation for least squares" related="def-cross-validation"}

The leave-one-out cross-validation score $\mathrm{LOO\text{-}CV}=\sum_i(Y_i-\hat\mu_{(-i)})^2$ of a least squares fit equals
$$\mathrm{LOO\text{-}CV}=\sum_{i=1}^n\frac{(Y_i-\hat\mu_i)^2}{(1-P_{ii})^2},$$
so it is computed from a single fit.

:::

::: {.proof}

By @thm-leave-one-out, $Y_i-\hat\mu_{(-i)}=\hat\varepsilon_i/(1-P_{ii})$ for every $i$. Squaring and summing gives the formula.

:::

For linear models $C_p$ and LOO-CV usually give similar answers; cross-validation has the advantage that it extends to any fitting method, even when no closed formula exists. For a generalised linear model the squared error is replaced by the deviance (@sec-math-statistics-glm-glm-diagnostics).

::: {#def-aic-bic .definition name="AIC and BIC"}

Let $\hat\theta_k$ be the maximum likelihood estimate in a parametric model $\Theta_k$ of dimension $\dim\Theta_k$, fitted to $n$ observations. Then
$$\mathrm{AIC}(\Theta_k)=-2\sum_{i=1}^n\log f(Y_i;\hat\theta_k)+2\dim\Theta_k,\qquad\mathrm{BIC}(\Theta_k)=-2\sum_{i=1}^n\log f(Y_i;\hat\theta_k)+\dim\Theta_k\,\log n .$$
For regression the density is the conditional density of $Y_i$ given $X_i$. A smaller value is better.

:::

*Motivation.* The expected log-likelihood of a new observation at $\hat\theta_k$ is overestimated by the maximised log-likelihood of the sample, because the same data chose $\hat\theta_k$; the penalty $2\dim\Theta_k$ is an estimate of this optimism (the same idea as in $C_p$; AIC divided by $n$ is a consistent estimator of its target). BIC comes from a Bayesian argument: with a uniform prior on the models, $P(\Theta_k\mid\text{data})\propto e^{-\mathrm{BIC}(\Theta_k)/2}$ as $n\to\infty$. Since $\log n>2$ for $n\ge8$, BIC penalises complexity more and tends to choose smaller models. As a rule of thumb AIC suits prediction and BIC suits recovering the true set of regressors.

::: {#prp-aic-normal-linear .proposition name="AIC for the normal linear model"}

In the normal linear model with unknown $\sigma^2$ and $\hat\sigma^2_{\mathrm{MLE}}=\|(I-P)\mathbf Y\|^2/n$,
$$\mathrm{AIC}=n\bigl\{1+\log(2\pi\hat\sigma^2_{\mathrm{MLE}})\bigr\}+2(p+1).$$
If $\sigma^2$ is known, $\mathrm{AIC}=n\log(2\pi\sigma^2)+\sigma^{-2}\|\mathbf Y-\hat\mu\|^2+2p$, which is $\sigma^{-2}C_p$ plus a constant: AIC and Mallows' $C_p$ select the same model.

:::

::: {.proof}

1. The log-likelihood is $-\frac n2\log(2\pi\sigma^2)-\frac1{2\sigma^2}\|\mathbf Y-\mathbb X\beta\|^2$. At the MLE $\hat\sigma^2_{\mathrm{MLE}}$ the second term equals $-n/2$, so $-2\ell=n\log(2\pi\hat\sigma^2_{\mathrm{MLE}})+n$. The model has $p+1$ parameters, giving the first formula.

2. With $\sigma^2$ known the parameter dimension is $p$ and $-2\ell(\hat\beta)=n\log(2\pi\sigma^2)+\|\mathbf Y-\hat\mu\|^2/\sigma^2$. Adding $2p$ gives $\sigma^{-2}(\|\mathbf Y-\hat\mu\|^2+2p\sigma^2)+n\log(2\pi\sigma^2)=\sigma^{-2}C_p+\text{const}$.

:::

With $p$ regressors there are $2^p$ subsets, so exhaustive search is infeasible beyond about $p=30$. RSS $=\|\mathbf Y-\hat\mu\|^2$ is the negative log-likelihood in the normal model and a fair way to compare subsets of the same size; the criteria above then choose among the sizes.

::: {#def-subset-algorithms .definition name="Best subset, forward and backward stepwise selection"}

For each size $k=0,\dots,p$ the three algorithms produce one subset $S_k$ of regressors:

1. *Best subset*: $S_k$ is the size-$k$ subset with the smallest RSS (all $2^p$ subsets are fitted).
2. *Forward stepwise*: $S_0=\emptyset$ and $S_{k+1}=S_k\cup\{j\}$, where $j\notin S_k$ gives the smallest RSS.
3. *Backward stepwise*: $S_p=\{1,\dots,p\}$ and $S_{k-1}=S_k\setminus\{j\}$, where $j\in S_k$ gives the smallest RSS.

Stepwise methods examine only $O(p^2)$ subsets but need not find the best one of each size. The resulting path indexed by $k$ is then cut at a single model with $C_p$, AIC, BIC or cross-validation.

:::

```{=latex}
\begin{algorithm}
\caption{Forward stepwise selection}
\begin{algorithmic}
\INPUT Design columns $1,\dots,p$, response $\mathbf Y$
\OUTPUT Nested subsets $S_0\subset S_1\subset\dots\subset S_p$
\STATE $S_0\gets\emptyset$
\FOR{$k=0$ \TO $p-1$}
    \FORALL{$j\notin S_k$}
        \STATE fit least squares on $S_k\cup\{j\}$ and record its RSS
    \ENDFOR
    \STATE $S_{k+1}\gets S_k\cup\{j^*\}$ for the $j^*$ with the smallest recorded RSS
\ENDFOR
\RETURN $S_0,\dots,S_p$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-stepwise-three-regressors .example name="Greedy search can miss the best subset"}

Let $p=3$ and suppose the RSS of the subsets is

| subset | $\emptyset$ | 1 | 2 | 3 | 12 | 13 | 23 | 123 |
|---|---|---|---|---|---|---|---|---|
| RSS | 100 | 90 | 70 | 60 | 20 | 55 | 40 | 15 |

1. Best subset selects $\emptyset,\{3\},\{1,2\},\{1,2,3\}$ for $k=0,1,2,3$.
2. Forward stepwise starts with $\{3\}$ (RSS $60$) and then adds regressor 2 ($\{2,3\}$ has RSS $40$, against $55$ for $\{1,3\}$): it selects $\emptyset,\{3\},\{2,3\},\{1,2,3\}$ and misses $\{1,2\}$.
3. Backward stepwise removes from $\{1,2,3\}$ the regressor whose removal costs least: removing 3 gives $\{1,2\}$ with RSS $20$, so $S_2=\{1,2\}$; from it, removing 1 gives $\{2\}$ (RSS $70$) rather than $\{1\}$ ($90$): it selects $\emptyset,\{2\},\{1,2\},\{1,2,3\}$ and misses $\{3\}$.

:::

::: {#fig-model-selection-criteria-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2cm,y=1.1cm]
\node[box] (e) at (0,0) {$\emptyset$};
\node[box] (a) at (1,1.2) {1};
\node[hl box] (b) at (1,0) {3};
\node[box] (c) at (1,-1.2) {2};
\node[box] (ab) at (2,1.2) {12};
\node[hl box] (bc) at (2,0) {23};
\node[box] (ac) at (2,-1.2) {13};
\node[box] (f) at (3,0) {123};
\draw[faint] (e) -- (a); \draw[emph] (e) -- (b); \draw[faint] (e) -- (c);
\draw[faint] (a) -- (ab); \draw[faint] (a) -- (ac); \draw[faint] (b) -- (ac); \draw[emph] (b) -- (bc);
\draw[faint] (c) -- (ab); \draw[faint] (c) -- (bc);
\draw[faint] (ab) -- (f); \draw[emph] (bc) -- (f); \draw[faint] (ac) -- (f);
\end{tikzpicture}
\end{center}
```

The forward path of @exm-stepwise-three-regressors through the lattice of subsets of $\{1,2,3\}$ (thick edges). The best size-two subset $\{1,2\}$ is not on the path.

:::
