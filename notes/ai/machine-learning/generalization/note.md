---
title: "Generalization, Overfitting and Tuning"
sources: [cs188-20, cs188-21]
requires: [ai/machine-learning/supervised-learning]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 20 (training and testing, empirical risk minimisation, overfitting, generalisation, tuning on held-out data, features, errors, baselines, confidences) and the start of Lecture 21 (baselines and confidences), in our own wording; the polynomial example is our own, computed with NumPy (seed 2). -->

Minimising the training loss (@def-training-loss) is a means, not the goal: the goal is to predict well on inputs not seen during training. This note separates the two and describes how to measure and control the gap.

::: {#def-test-error .definition name="Training, held-out and test data; generalisation"}

Assume examples are drawn independently from a fixed distribution $\mathcal P$ over $\mathcal X\times\mathcal Y$. The *risk* (expected loss) of a predictor $f$ is $\mathbb E_{(x,y)\sim\mathcal P}\,\text{Loss}(x,y,f)$; minimising the training loss instead is *empirical risk minimisation*. A predictor *generalises* if its risk is close to its training loss.

Available labelled data is split into three disjoint parts: *training data*, used to fit the parameters; *held-out* (validation) data, used to choose *hyperparameters* (settings of the learning algorithm itself, such as a smoothing strength or a model size); and *test data*, used once, at the end, to estimate the risk of the final predictor.

:::

The test data estimates the risk only if nothing about the predictor was chosen by looking at it; a test set used to make choices becomes, in effect, training data, and its error underestimates the risk. The same holds for the held-out data after much tuning, which is why a separate test set is kept.

::: {#def-overfitting .definition name="Overfitting, underfitting"}

A predictor *overfits* when it fits the training data much better than new data, typically because its hypothesis class (@def-hypothesis-class) is rich enough to fit the noise and accidents of a small sample. It *underfits* when it fits even the training data poorly, because the hypothesis class cannot express the regularities present.

:::

::: {#exm-overfitting-polynomials .example name="Polynomials of growing degree"}

Ten training inputs equally spaced in $[0,1]$ have outputs $\sin(2\pi x)$ plus Gaussian noise of standard deviation $0.3$ (so no predictor can have squared error below $0.09$ on average). Fitting polynomials by least squares and measuring the average squared error on $10\,000$ fresh examples, one run gives

| degree | training error | test error |
|---|---|---|
| $1$ | $0.22$ | $0.33$ |
| $3$ | $0.086$ | $0.12$ |
| $9$ | $0.000$ | $0.84$ |

A line underfits. Degree $9$ passes through all ten points (zero training error) but oscillates between them and does worst on new data. Degree $3$, which is never best on the training data, is best on new data.

:::

Training error always decreases as the hypothesis class grows; the risk first decreases and then increases. Ways to control overfitting all limit how closely the training data is followed: fewer or simpler features, a smaller hypothesis class, smoothing of estimated probabilities (@def-laplace-smoothing), regularisation (penalising large parameters), stopping iterative training early, and more training data, which makes accidents rarer.

::: {#rmk-tuning .remark name="Tuning hyperparameters"}

To tune a hyperparameter, train one predictor per candidate value on the training data, measure each on the held-out data, and keep the value with the lowest held-out error; then, often, retrain on training and held-out data together with that value. With little data, *cross-validation* rotates which part is held out and averages the errors.

:::

::: {#rmk-baselines-confidence .remark name="Baselines and confidences"}

A test accuracy means little without a *baseline*: the simplest sensible predictor, such as always predicting the most frequent label, or a published simple method. If $90\%$ of emails are ham, a filter with $90\%$ accuracy has learnt nothing. Many classifiers also report a *confidence*, such as $P(y\mid x)$ from naive Bayes (@def-naive-bayes) or logistic regression (@def-logistic-regression). A classifier is *calibrated* if, among the predictions made with confidence about $p$, a fraction about $p$ is correct; naive Bayes tends to be overconfident, because it counts correlated features as independent evidence. When errors occur, inspecting them usually suggests better features, which help more than tuning.

:::
