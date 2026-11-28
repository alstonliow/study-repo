---
title: "Log-Linear Models and Contingency Tables"
sources: [camii-sm-18, camii-sms-4-q10]
requires: [math/statistics/glm/poisson-trick, math/statistics/glm/analysis-of-deviance, math/statistics/frequentist/contingency-tables]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Statistical Modelling (Michaelmas 2024, lecturer's notes), Section 4.9 (two-way and three-way contingency tables; the graphical-model subsection is not covered, as in the source), in our own wording; proofs written out in steps. The numerical example is our own and checked by computation. Pearson's test of independence is already in contingency-tables. -->

A contingency table counts how many of $n$ individuals fall in each cell of a cross-classification. Two views are equivalent: the counts $Y_{jk}$ are the aggregate of iid pairs $(A_i,B_i)$, so $Y\sim\mathrm{Multinomial}(n,\pi)$; or, by the Poisson trick (@thm-poisson-trick-likelihood), they can be treated as independent $\mathrm{Poisson}(\mu_{jk})$ counts, with $\pi_{jk}=\mu_{jk}/\mu_{++}$. Inference on cell probabilities is the same in both.

::: {#thm-independence-log-linear .theorem name="Independence is a log-linear submodel" related="thm-independence-test"}

For a $J\times K$ table, $H_0:A\perp B$ means $\pi_{jk}=\pi^A_j\pi^B_k$, which in the surrogate Poisson model is equivalent to
$$\log\mu_{jk}=\alpha+\beta_j^A+\beta_k^B,$$
a submodel with $1+(J-1)+(K-1)=J+K-1$ free parameters of the saturated model $\log\mu_{jk}=\alpha+\beta_j^A+\beta_k^B+\beta_{jk}^{AB}$ ($JK$ parameters; the over-parametrisation is removed by taking a reference level, e.g. $\beta_1^A=\beta_1^B=\beta^{AB}_{1k}=\beta^{AB}_{j1}=0$). The deviance (or Pearson's $\chi^2$) between the two models is asymptotically $\chi^2_{(J-1)(K-1)}$ under $H_0$, and is the test of independence.

:::

::: {.proof}

1. $\mu_{jk}=\mu_{++}\pi_{jk}$. If $\pi_{jk}=\pi_j^A\pi_k^B$, then $\log\mu_{jk}=\log\mu_{++}+\log\pi_j^A+\log\pi_k^B$, of the stated form; conversely a model of this form has $\pi_{jk}=\mu_{jk}/\mu_{++}$ with product structure.

2. By analysis of deviance (@thm-analysis-of-deviance) the deviance difference is asymptotically $\chi^2$ with degrees of freedom $JK-(J+K-1)=(J-1)(K-1)$.

3. For fitted means near the observed counts the deviance and Pearson's statistic agree (@prp-poisson-deviance-pearson), recovering the classical test.

:::

::: {#exm-two-by-two-log-linear .example name="A $2\times2$ table"}

With levels coded $0,1$ and baseline $\beta_1^A=\beta_1^B=0$, the design matrix of the independence model for $(\log\mu_{11},\log\mu_{12},\log\mu_{21},\log\mu_{22})$ in the parameters $(\alpha,\beta_2^A,\beta_2^B)$ and of the saturated model, which adds $\beta_{22}^{AB}$, are
$$X_0=\begin{pmatrix}1&0&0\\1&0&1\\1&1&0\\1&1&1\end{pmatrix},\qquad X=\begin{pmatrix}1&0&0&0\\1&0&1&0\\1&1&0&0\\1&1&1&1\end{pmatrix}.$$
For the table $\begin{pmatrix}30&10\\20&40\end{pmatrix}$ the independence fit is $\hat\mu_{jk}=y_{j+}y_{+k}/n$, that is $\begin{pmatrix}20&20\\30&30\end{pmatrix}$. The deviance is $2\sum y\log(y/\hat\mu)=17.26$ and Pearson's statistic is $16.67$, both on $(2-1)(2-1)=1$ degree of freedom, so independence is clearly rejected ($p<10^{-4}$).

:::

For three variables $(A_i,B_i,C_i)$ with cell probabilities $\pi_{jkl}$ five nested hypotheses are of interest. Each corresponds to a log-linear model that includes certain interaction terms and no others (the over-parametrisation is again removed by reference levels); they are tested by the deviance between two nested ones.

::: {#def-three-way-models .definition name="Models for three-way tables"}

| model | structure of $\pi_{jkl}$ | meaning | log-linear terms beyond the main effects $A,B,C$ |
|---|---|---|---|
| $H_1$ | $\pi^A_j\pi^B_k\pi^C_l$ | $A\perp B\perp C$ | none |
| $H_2$ | $\pi^A_j\pi^{BC}_{kl}$ | $A\perp(B,C)$ | $BC$ |
| $H_3$ | $\pi^{AB}_{jk}\pi^{BC}_{kl}/\pi^B_k$ | $A\perp C\mid B$ | $AB$, $BC$ |
| $H_4$ | $\pi^{AB}_{jk}\pi^{BC}_{kl}\pi^{AC}_{jl}$ | no three-way interaction | $AB,BC,AC$ |
| $H_5$ | unrestricted | saturated | $AB,BC,AC,ABC$ |

The five models are nested, $H_1\subset H_2\subset H_3\subset H_4\subset H_5$: each adds interaction terms to the previous one. $H_3$ and $H_4$ are written as products of marginal and pairwise factors (any positive $\pi$ whose logarithm is a sum of terms each depending on at most two of the indices for $H_4$).

:::

For $J=K=L=2$ the models have $4,5,6,7,8$ free parameters, so the deviance between consecutive models is tested against $\chi^2_1$. Conditional independence $H_3$, for example, is equivalent to $P(A=j,C=l\mid B=k)=P(A=j\mid B=k)P(C=l\mid B=k)$: given $B$, the variables $A$ and $C$ are independent, and a log-linear model of this type has no $AC$ and no $ABC$ term.

::: {#fig-log-linear-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\begin{scope}
\node[small vertex, label=above:$A$] (a) at (0,1) {};
\node[small vertex, label=below:$B$] (b) at (-0.7,0) {};
\node[small vertex, label=below:$C$] (c) at (0.7,0) {};
\node[lab] at (0,-1) {$H_1$};
\end{scope}
\begin{scope}[xshift=3cm]
\node[small vertex, label=above:$A$] (a) at (0,1) {};
\node[small vertex, label=below:$B$] (b) at (-0.7,0) {};
\node[small vertex, label=below:$C$] (c) at (0.7,0) {};
\draw[emph] (b) -- (c);
\node[lab] at (0,-1) {$H_2$};
\end{scope}
\begin{scope}[xshift=6cm]
\node[small vertex, label=above:$A$] (a) at (0,1) {};
\node[small vertex, label=below:$B$] (b) at (-0.7,0) {};
\node[small vertex, label=below:$C$] (c) at (0.7,0) {};
\draw[emph] (a) -- (b); \draw[emph] (b) -- (c);
\node[lab] at (0,-1) {$H_3$};
\end{scope}
\begin{scope}[xshift=9cm]
\node[small vertex, label=above:$A$] (a) at (0,1) {};
\node[small vertex, label=below:$B$] (b) at (-0.7,0) {};
\node[small vertex, label=below:$C$] (c) at (0.7,0) {};
\draw[emph] (a) -- (b); \draw[emph] (b) -- (c); \draw[emph] (a) -- (c);
\node[lab] at (0,-1) {$H_4,H_5$};
\end{scope}
\end{tikzpicture}
\end{center}
```

An edge joins two variables when the model has their pairwise interaction. $H_4$ and $H_5$ have the same graph and are distinguished by the three-way interaction $ABC$; they imply no (conditional) independence.

:::
