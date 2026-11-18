---
title: "Linear Classification"
sources: [cs221-3]
requires: [ai/machine-learning/linear-regression]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 3 (linear classifiers, margin, zero-one loss), in our own wording. -->

In *binary classification* the output is one of two labels, written $y\in\{-1,+1\}$; in *multiclass classification* it is one of $K$ labels $y\in\{0,\dots,K-1\}$. A linear classifier keeps the linear predictor of regression and thresholds it.

::: {#def-linear-classifier .definition name="Logit, linear classifier, decision boundary"}

For parameters $\theta=(\mathbf{w},b)$ with $\mathbf{w}\in\mathbb{R}^d$, $b\in\mathbb{R}$, the *logit* (score) of an input $\mathbf{x}\in\mathbb{R}^d$ is $\mathbf{w}\cdot\mathbf{x}+b$, and the *linear classifier* is

$$
f_\theta(\mathbf{x})=\operatorname{sign}(\mathbf{w}\cdot\mathbf{x}+b)=\begin{cases}+1&\text{if }\mathbf{w}\cdot\mathbf{x}+b>0,\\-1&\text{otherwise.}\end{cases}
$$

Its *decision boundary* is the hyperplane $\{\mathbf{x}:\mathbf{w}\cdot\mathbf{x}+b=0\}$, which separates the inputs classified $+1$ from those classified $-1$.

:::

The sign of the logit is the prediction and its size a measure of confidence. The tie at logit $0$ is broken arbitrarily (here towards $-1$). Classifiers from richer hypothesis classes can have curved or disconnected decision boundaries; a linear one always cuts the input space by a hyperplane.

::: {#def-margin .definition name="Margin, zero-one loss"}

The *margin* of $f_\theta$ on an example $(\mathbf{x},y)$ is $y\,(\mathbf{w}\cdot\mathbf{x}+b)$; it is positive exactly when the prediction is correct, and large when it is correct with high confidence. The *zero-one loss* is

$$
\text{Loss}_{0\text{-}1}(\mathbf{x},y,\theta)=\mathbf{1}\bigl[f_\theta(\mathbf{x})\ne y\bigr]=\mathbf{1}\bigl[y\,(\mathbf{w}\cdot\mathbf{x}+b)\le0\bigr],
$$

and its training loss is the fraction of training examples classified wrongly (the training *error rate*).

:::

::: {#exm-linear-classification-1 .example name="A classifier on three points"}

Take the training data $\bigl((1,2),-1\bigr)$, $\bigl((2,0),+1\bigr)$, $\bigl((0,0),-1\bigr)$ and $\mathbf{w}=(1,-1)$, $b=-1$, so the logit is $x_1-x_2-1$. The logits are $-2$, $1$, $-1$ and the margins $2$, $1$, $1$: all positive, so every example is classified correctly and the training zero-one loss is $0$. The decision boundary is the line $x_2=x_1-1$.

:::

::: {#fig-linear-classification-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\fill[tintA] (-0.5,-1.5) -- (3.5,2.5) -- (3.5,-1.5) -- cycle;
\draw[->] (-1,0) -- (3.5,0) node[lab,anchor=north east] {$x_1$};
\draw[->] (0,-1.5) -- (0,2.6) node[lab,anchor=north west] {$x_2$};
\draw[hl] (-0.3,-1.3) -- (3.3,2.3) node[lab,anchor=south east] {$x_1-x_2-1=0$};
\node[hollow dot] at (1,2) {}; \node[lab,anchor=west] at (1.1,2) {$(1,2)$, $-1$};
\node[hollow dot] at (0,0) {}; \node[lab,anchor=north east] at (-0.05,-0.05) {$(0,0)$, $-1$};
\node[dot] at (2,0) {}; \node[lab,anchor=north west] at (2.05,-0.05) {$(2,0)$, $+1$};
\node[lab] at (2.9,-1.0) {$f=+1$};
\node[lab] at (0.6,1.3) {$f=-1$};
\end{tikzpicture}
\end{center}
```

The classifier of @exm-linear-classification-1: the shaded half-plane is classified $+1$. Filled points have label $+1$, hollow points $-1$.

:::

::: {#prp-zero-one-loss-gradient .proposition name="The zero-one loss has zero gradient"}

At every $\theta$ where no training example has margin exactly $0$,

$$
\nabla_\theta\text{TrainLoss}_{0\text{-}1}(\theta)=\mathbf{0},
$$

and at every $\theta$ where some margin is $0$ the training loss is not differentiable.

:::

::: {.proof}

1. Each margin $y\,(\mathbf{w}\cdot\mathbf{x}+b)$ is a continuous function of $\theta$.

2. If no margin is $0$ at $\theta$, each has a fixed sign on a small ball around $\theta$, so each term $\mathbf{1}[\text{margin}\le0]$, and hence the training loss, is constant on that ball. A function constant near a point has zero gradient there.

3. If some margins are $0$ at $\theta$, those examples all count as wrong at $\theta$, since the zero-one loss uses $\text{margin}\le0$. Change $b$ by a small $\varepsilon$, so small that no other margin changes sign: each of these margins becomes $y\varepsilon$. For $\varepsilon>0$ the examples among them with $y=+1$ become correct, and for $\varepsilon<0$ those with $y=-1$ do. One of the two groups is non-empty, so on one side the training loss drops by at least $1/\lvert\mathcal D\rvert$. Thus the loss is discontinuous at $\theta$, hence not differentiable.

:::

So gradient descent on the zero-one loss never moves: a wrongly classified example stays wrong under any small change of the parameters, and the gradient gives no direction. Logistic regression (@sec-ai-machine-learning-logistic-regression) replaces this loss by a smooth one.
