---
title: "The Bias-Variance Tradeoff and Double Descent"
sources: [cs229-8]
requires: [ai/machine-learning/generalization, math/probability/estimation/classical-estimation]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 8.1-8.2 (the bias-variance tradeoff, its decomposition for regression, model-wise and sample-wise double descent), in our own wording. The constant-model example is our own and was checked by simulation in Python; proofs written out in steps. The estimator version of the decomposition is @prp-mse-bias-variance. -->

Test error has two different sources. A model may be too simple to capture the pattern (it *underfits*), or so flexible that it fits the accidents of its particular training set (it *overfits*, @def-overfitting). For squared loss the two can be separated exactly.

::: {#def-bias-variance-setting .definition name="Bias and variance of a learning algorithm"}

Suppose the data satisfy $y=h^\star(\mathbf{x})+\xi$, where the noise $\xi$ has mean $0$ and variance $\sigma^2$ and is independent of $\mathbf{x}$ and of the training data. A learning algorithm applied to a random training set $S$ of $N$ examples returns a predictor $h_S$. At a fixed input $\mathbf{x}$, define the *average predictor* $h_{\text{avg}}(\mathbf{x})=E_S[h_S(\mathbf{x})]$ and

$$
\text{bias}^2(\mathbf{x})=\bigl(h^\star(\mathbf{x})-h_{\text{avg}}(\mathbf{x})\bigr)^2,\qquad \text{variance}(\mathbf{x})=E_S\bigl[\bigl(h_S(\mathbf{x})-h_{\text{avg}}(\mathbf{x})\bigr)^2\bigr].
$$

The bias is the error the algorithm would make even with infinitely many training sets averaged; the variance measures how much its output moves from one training set to another.

:::

::: {#thm-bias-variance-decomposition .theorem name="Bias-variance decomposition"}

At a fixed input $\mathbf{x}$, with a fresh label $y=h^\star(\mathbf{x})+\xi$,

$$
E_{S,\xi}\bigl[(y-h_S(\mathbf{x}))^2\bigr]=\sigma^2+\text{bias}^2(\mathbf{x})+\text{variance}(\mathbf{x}).
$$

:::

::: {.proof}

1. Write $y-h_S(\mathbf{x})=\xi+\bigl(h^\star(\mathbf{x})-h_S(\mathbf{x})\bigr)$. The noise $\xi$ has mean $0$ and is independent of $S$, so the cross term has expectation $0$ and

   $$
   E\bigl[(y-h_S(\mathbf{x}))^2\bigr]=\sigma^2+E_S\bigl[(h^\star(\mathbf{x})-h_S(\mathbf{x}))^2\bigr].
   $$

2. Write $h^\star(\mathbf{x})-h_S(\mathbf{x})=\bigl(h^\star(\mathbf{x})-h_{\text{avg}}(\mathbf{x})\bigr)+\bigl(h_{\text{avg}}(\mathbf{x})-h_S(\mathbf{x})\bigr)$. The first part is a constant and the second has mean $0$ over $S$, so again the cross term vanishes.

3. The two squares that remain are $\text{bias}^2(\mathbf{x})$ and $\text{variance}(\mathbf{x})$.

:::

The noise term $\sigma^2$ cannot be reduced by any algorithm. Richer hypothesis classes usually lower the bias and raise the variance; more training data lowers the variance and leaves the bias unchanged.

::: {#exm-bias-variance-constant .example name="Fitting a constant to a line"}

Let $x$ be uniform on $[0,1]$, $h^\star(x)=x$ and noise variance $\sigma^2$. The algorithm ignores the inputs and predicts the mean label: $h_S(x)=\bar y=\frac1N\sum_iy^{(i)}$. Each $y^{(i)}=x^{(i)}+\xi^{(i)}$ has mean $\tfrac12$ and variance $\tfrac1{12}+\sigma^2$, so

$$
h_{\text{avg}}(x)=\tfrac12,\qquad \text{bias}^2(x)=\bigl(x-\tfrac12\bigr)^2,\qquad \text{variance}(x)=\frac{1/12+\sigma^2}{N}.
$$

Averaged over a test input, the bias term is $E[(x-\tfrac12)^2]=\tfrac1{12}$ whatever $N$ is, while the variance term tends to $0$. With $\sigma^2=0.1$ and $N=10$ the expected test error is $0.1+0.0833+0.0183\approx0.202$. Fitting a line instead removes the bias completely, at the price of some variance.

:::

::: {#rmk-double-descent .remark name="Double descent"}

The classical picture is a U-shaped test error as the model grows. Modern experiments often show a second descent. For linear regression with $d$ features on $N$ examples, fitted by least squares and, when $d>N$, by the minimum-norm interpolating solution (@prp-gd-min-norm), the test error typically rises to a sharp peak near $d=N$ and then falls again as $d$ grows (*model-wise double descent*). For fixed $d$ the same peak appears as $N$ passes through $d$ (*sample-wise double descent*): more data can briefly hurt. The peak comes from the near-singular matrix $X^{\mathsf T}X$ at $d\approx N$, which makes the fitted parameters very large; a well-tuned ridge penalty (@def-regularization) largely removes it. Over-parametrized models can generalize because the algorithm, not only the hypothesis class, decides which interpolating solution is found: the number of parameters is not the right measure of complexity.

:::
