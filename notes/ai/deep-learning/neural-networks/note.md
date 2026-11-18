---
title: "Neural Networks"
sources: [cs221-5]
requires: [ai/deep-learning/backpropagation, ai/machine-learning/softmax-regression]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 5 (non-linear features, multi-layer perceptrons, deep networks), in our own wording; proof written out in steps. -->

A linear classifier cuts the input space by a hyperplane, so it fails on data that are not *linearly separable*, such as one class surrounded by the other. Non-linear predictors can be obtained from the same linear machinery.

::: {#def-feature-map .definition name="Feature map"}

A *feature map* is a function $\boldsymbol\phi:\mathcal X\to\mathbb{R}^p$. A linear predictor on features is $f_\theta(x)=\mathbf{w}\cdot\boldsymbol\phi(x)+b$ (or its sign, for classification). It is linear in the parameters, so it is trained exactly as before on the data $(\boldsymbol\phi(x),y)$, yet it can be non-linear in $x$.

:::

::: {#exm-neural-networks-1 .example name="A circle as a linear boundary"}

The classifier $\operatorname{sign}\bigl((x_1-1)^2+(x_2-1)^2-2\bigr)$ labels the points outside the circle of centre $(1,1)$ and radius $\sqrt2$ as $+1$. Expanding, $(x_1-1)^2+(x_2-1)^2-2=-2x_1-2x_2+(x_1^2+x_2^2)$, so with $\boldsymbol\phi(\mathbf{x})=(x_1,x_2,x_1^2+x_2^2)$ it is the linear classifier $\operatorname{sign}(\mathbf{w}\cdot\boldsymbol\phi(\mathbf{x}))$ with $\mathbf{w}=(-2,-2,1)$, $b=0$. For example $(1,1)$ has score $-2$ (inside) and $(3,0)$ has score $3$ (outside).

:::

::: {#fig-neural-networks-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\fill[tintA, even odd rule] (-1.3,-1.3) rectangle (3.4,3.4) (1,1) circle ({sqrt(2)});
\draw[hl] (1,1) circle ({sqrt(2)});
\draw[->] (-1.3,0) -- (3.4,0) node[lab,anchor=north east] {$x_1$};
\draw[->] (0,-1.3) -- (0,3.4) node[lab,anchor=north west] {$x_2$};
\node[hollow dot] at (1,1) {}; \node[lab,anchor=north] at (1,0.9) {$-2$};
\node[dot] at (3,0) {}; \node[lab,anchor=south] at (3,0.1) {$3$};
\node[lab] at (2.9,3.0) {$+1$};
\node[lab] at (1.5,1.6) {$-1$};
\end{tikzpicture}
\end{center}
```

The classifier of @exm-neural-networks-1: linear in the features $(x_1,x_2,x_1^2+x_2^2)$, circular in the input. Scores of two points are shown; the shaded region is classified $+1$.

:::

The drawback is that $\boldsymbol\phi$ is chosen by hand. A neural network learns the feature map as well, by making it a parametrized layer.

::: {#prp-linear-network-collapse .proposition name="Stacked linear layers are linear"}

For matrices $W_1,W_2$ and vectors $\mathbf{b}_1,\mathbf{b}_2$ of compatible sizes,

$$
W_2(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2=W\mathbf{x}+\mathbf{b},\qquad W=W_2W_1,\quad \mathbf{b}=W_2\mathbf{b}_1+\mathbf{b}_2 .
$$

So any number of linear layers defines the same hypothesis class as one linear layer (or a subset of it).

:::

::: {.proof}

1. By distributivity, $W_2(W_1\mathbf{x}+\mathbf{b}_1)=W_2W_1\mathbf{x}+W_2\mathbf{b}_1$, and associativity of the matrix product gives $(W_2W_1)\mathbf{x}$.

2. Adding $\mathbf{b}_2$ gives the stated form. By induction the same holds for any number of layers.

:::

::: {#def-activation-function .definition name="Activation function"}

An *activation function* is a fixed non-linear function $a:\mathbb{R}\to\mathbb{R}$ applied elementwise. Common choices are the *rectified linear unit* $\operatorname{ReLU}(z)=\max(z,0)$, the logistic function $\sigma$ and $\tanh$.

:::

ReLU has derivative $0$ for $z<0$: a unit whose input is negative on every example passes back no gradient and stops learning (a "dead neuron"). Activation functions balance being close to linear, so that gradients stay away from zero, against being non-linear enough to add expressive power.

::: {#def-multi-layer-perceptron .definition name="Multi-layer perceptron"}

A *multi-layer perceptron* (MLP, a feed-forward neural network) with one hidden layer computes

$$
\mathbf{h}=a(W_1\mathbf{x}+\mathbf{b}_1),\qquad \mathbf{z}=W_2\mathbf{h}+\mathbf{b}_2,
$$

where $\mathbf{h}\in\mathbb{R}^m$ are the *hidden units* (activations, neurons) and $\mathbf{z}$ the output logits. A *deep* network composes $L$ such layers, $\mathbf{h}_0=\mathbf{x}$ and $\mathbf{h}_\ell=a(W_\ell\mathbf{h}_{\ell-1}+\mathbf{b}_\ell)$ for $\ell=1,\dots,L-1$, followed by a linear output layer. The parameters are all $W_\ell,\mathbf{b}_\ell$; gradients come from backpropagation (@sec-ai-deep-learning-backpropagation) and training uses (stochastic) gradient descent on, for example, the cross entropy loss.

:::

The first layer plays the role of a learned feature map and the last is a linear predictor on those features; each further layer can compute more abstract features of the input. In code, a model maps inputs to logits, a loss maps logits and targets to a number, and an optimizer updates the parameters from the gradients.

::: {#fig-neural-networks-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.6cm,y=0.7cm]
\foreach \i in {1,2} { \node[small vertex] (x\i) at (0,{1.5-\i}) {$x_{\i}$}; }
\foreach \j in {1,2,3,4} { \node[small vertex] (h\j) at (1,{2.5-\j}) {$h_{\j}$}; }
\node[small vertex] (z) at (2,0) {$z$};
\foreach \i in {1,2} { \foreach \j in {1,2,3,4} { \draw[faint] (x\i) -- (h\j); } }
\foreach \j in {1,2,3,4} { \draw[faint] (h\j) -- (z); }
\node[lab] at (0.5,-2.3) {$W_1,\mathbf{b}_1,a$};
\node[lab] at (1.5,-2.3) {$W_2,\mathbf{b}_2$};
\end{tikzpicture}
\end{center}
```

An MLP with two inputs, four hidden units and one output logit: each hidden unit is an activation of a linear function of the inputs, and the output is a linear function of the hidden units.

:::
