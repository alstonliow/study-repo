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

::: {#fig-supervised-learning-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (d) at (0,1.2) {training data $\mathcal D$};
\node[hl box] (l) at (3.4,1.2) {learner};
\node[box] (f) at (3.4,0) {predictor $f$};
\node[lab] (x) at (1.2,0) {$x$};
\node[lab] (y) at (5.6,0) {$\hat y=f(x)$};
\draw[map] (d) -- (l);
\draw[map] (l) -- (f);
\draw[map] (x) -- (f);
\draw[map] (f) -- (y);
\end{tikzpicture}
\end{center}
```

Supervised learning in two stages: a learner turns the training data into a predictor $f$, which then maps each new input $x$ to a prediction

:::

::: {#def-hypothesis-class .definition name="Parameters, hypothesis class"}

A *parametrized family* of predictors assigns a predictor $f_\theta$ to each parameter value $\theta$ in a set $\Theta$ (in practice $\theta$ is a collection of tensors). The *hypothesis class* is

$$
\mathcal F=\{f_\theta:\theta\in\Theta\}.
$$

In deep learning the hypothesis class is called a *model architecture* and a single $f_\theta$ a *model*.

:::

::: {#fig-supervised-learning-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) ellipse (2.7 and 1.5);
\node[lab] at (-2.0,1.0) {all predictors};
\draw[regionA] (0.3,-0.2) ellipse (1.5 and 0.9);
\node[lab] at (0.3,0.45) {$\mathcal F$};
\node[hl dot] (s) at (2.2,-0.6) {};
\node[tick, right] at (s.east) {best predictor};
\node[dot] (g) at (1.2,-0.4) {};
\node[tick, left] at (g.west) {best in $\mathcal F$};
\draw[faint, dashed] (g) -- (s);
\end{tikzpicture}
\end{center}
```

The hypothesis class $\mathcal F$ is the set the learner searches. If the best predictor lies outside it, even the best member of $\mathcal F$ makes an approximation error (dashed)

:::

::: {#def-training-loss .definition name="Loss, training loss"}

A *loss function* $\text{Loss}(x,y,\theta)\ge0$ measures how badly the predictor $f_\theta$ does on the example $(x,y)$. The *training loss* is its average over the training data,

$$
\text{TrainLoss}(\theta)=\frac{1}{\lvert\mathcal D\rvert}\sum_{(x,y)\in\mathcal D}\text{Loss}(x,y,\theta).
$$

Learning then means solving the optimization problem $\min_{\theta\in\Theta}\text{TrainLoss}(\theta)$.

:::

::: {#fig-supervised-learning-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.8,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,2.8) node[lab, above] {$y$};
\draw[emph] (0,0.4) -- (4.4,2.38);
\draw[hl] (0.50,1.08) -- (0.50,0.62);
\draw[hl] (1.00,1.36) -- (1.00,0.85);
\draw[hl] (1.50,1.10) -- (1.50,1.08);
\draw[hl] (2.00,1.03) -- (2.00,1.30);
\draw[hl] (2.50,1.14) -- (2.50,1.52);
\draw[hl] (3.00,1.76) -- (3.00,1.75);
\draw[hl] (3.50,1.62) -- (3.50,1.98);
\draw[hl] (4.00,1.70) -- (4.00,2.20);
\node[dot] at (0.50,1.08) {};
\node[dot] at (1.00,1.36) {};
\node[dot] at (1.50,1.10) {};
\node[dot] at (2.00,1.03) {};
\node[dot] at (2.50,1.14) {};
\node[dot] at (3.00,1.76) {};
\node[dot] at (3.50,1.62) {};
\node[dot] at (4.00,1.70) {};
\end{tikzpicture}
\end{center}
```

The training loss averages the loss of the predictor (line) over the training examples; for squared loss each term is the square of a highlighted residual

:::

::: {#rmk-supervised-learning-1 .remark name="Three design questions"}

Every learning method answers three questions: which predictors are possible (the hypothesis class), how good a predictor is (the loss function), and how to find the best one (the optimization algorithm, usually @sec-ai-machine-learning-gradient-descent). Linear regression (@sec-ai-machine-learning-linear-regression) and linear classification (@sec-ai-machine-learning-linear-classification) answer the first question in the same way and differ in the second.

:::
