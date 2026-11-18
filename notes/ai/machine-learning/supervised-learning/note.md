---
title: "Supervised Learning"
sources: [cs221-2, cs221-3]
requires: []
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lectures 2 and 3 (the machine learning pipeline), in our own wording. -->

A program that maps inputs to outputs is usually written by hand. In supervised learning it is instead produced from examples of the task, by choosing the best function in a family of candidates.

::: {#def-predictor .definition name="Predictor, training data, learning algorithm"}

Let $\mathcal X$ be a set of inputs and $\mathcal Y$ a set of outputs. A *predictor* is a function $f:\mathcal X\to\mathcal Y$. An *example* is a pair $(x,y)\in\mathcal X\times\mathcal Y$ of an input and its target output, and the *training data* $\mathcal D$ is a finite set (or list) of examples. A *learning algorithm* maps training data to a predictor. The task is *regression* when $\mathcal Y=\mathbb{R}$ and *classification* when $\mathcal Y$ is a finite set of *labels* (classes).

:::

::: {#def-hypothesis-class .definition name="Parameters, hypothesis class"}

A *parametrized family* of predictors assigns a predictor $f_\theta$ to each parameter value $\theta$ in a set $\Theta$ (in practice $\theta$ is a collection of tensors). The *hypothesis class* is

$$
\mathcal F=\{f_\theta:\theta\in\Theta\}.
$$

In deep learning the hypothesis class is called a *model architecture* and a single $f_\theta$ a *model*.

:::

::: {#def-training-loss .definition name="Loss, training loss"}

A *loss function* $\text{Loss}(x,y,\theta)\ge0$ measures how badly the predictor $f_\theta$ does on the example $(x,y)$. The *training loss* is its average over the training data,

$$
\text{TrainLoss}(\theta)=\frac{1}{\lvert\mathcal D\rvert}\sum_{(x,y)\in\mathcal D}\text{Loss}(x,y,\theta).
$$

Learning then means solving the optimization problem $\min_{\theta\in\Theta}\text{TrainLoss}(\theta)$.

:::

::: {#rmk-supervised-learning-1 .remark name="Three design questions"}

Every learning method answers three questions: which predictors are possible (the hypothesis class), how good a predictor is (the loss function), and how to find the best one (the optimization algorithm, usually @sec-ai-machine-learning-gradient-descent). Linear regression (@sec-ai-machine-learning-linear-regression) and linear classification (@sec-ai-machine-learning-linear-classification) answer the first question in the same way and differ in the second.

:::
