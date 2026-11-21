---
title: "The Multiclass SVM Loss"
sources: [cs231n-2]
requires: [ai/machine-learning/regularization-and-model-selection]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Linear classification: score functions, bias trick, multiclass SVM loss, regularization, softmax versus SVM), in our own wording; the example was computed with NumPy; the gradient theorem and the scale propositions are written out as our own proofs. -->

A multiclass linear model (@def-softmax) gives each class $k\in\{0,\dots,K-1\}$ a score $s_k=\mathbf{w}_k\cdot\mathbf{x}+b_k$, the vector $\mathbf{s}=W\mathbf{x}+\mathbf{b}$. The cross entropy loss (@def-cross-entropy-loss) reads the scores as log-probabilities. The *multiclass SVM loss* reads them only through their differences: it asks the correct score to beat every other score by a fixed margin.

::: {#rmk-bias-trick .remark name="The bias trick"}

Appending a constant coordinate $1$ to every input, $\tilde{\mathbf{x}}=(\mathbf{x},1)$, and the column $\mathbf{b}$ to $W$, $\tilde W=[W\ \mathbf{b}]$, gives $\tilde W\tilde{\mathbf{x}}=W\mathbf{x}+\mathbf{b}$. So a linear model with biases is a linear map on the extended inputs, and formulas may be written for $\mathbf{s}=W\mathbf{x}$ alone.

:::

Each row $\mathbf{w}_k$ is a *template* for class $k$: the score is an inner product, large when $\mathbf{x}$ looks like $\mathbf{w}_k$. For images, the learnt rows look like blurred average images of their classes, one template per class, which is why a linear model cannot represent a class with several distinct appearances.

::: {#def-multiclass-svm-loss .definition name="Multiclass SVM loss"}

For scores $\mathbf{s}\in\mathbb{R}^K$, a correct class $y$ and a margin $\Delta>0$, the *multiclass SVM* (hinge) *loss* is

$$
L(\mathbf{s},y)=\sum_{j\ne y}\max\bigl(0,\ s_j-s_y+\Delta\bigr).
$$

For a linear model $\mathbf{s}=W\mathbf{x}_i$ on training data $(\mathbf{x}_i,y_i)_{i=1}^N$, the regularized objective is

$$
J(W)=\frac1N\sum_{i=1}^{N}L(W\mathbf{x}_i,y_i)+\lambda\sum_{k,l}W_{kl}^2 .
$$

:::

::: {#fig-multiclass-svm-loss-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw (0,0) -- (3.4,0);
\path[hl cell] (0.40,0) rectangle (1.00,1.28);
\node[tick, above] at (0.70,1.28) {$3.2$};
\path[bar] (1.50,0) rectangle (2.10,2.04);
\node[tick, above] at (1.80,2.04) {$5.1$};
\path[bar] (2.60,0) rectangle (3.20,-0.68);
\node[tick, below] at (2.90,-0.68) {$-1.7$};
\draw[faint, dashed] (0,0.88) -- (3.4,0.88) node[tick, right] {$s_y-\Delta$};
\node[tick, below] at (0.70,-0.25) {cat};
\node[tick, below] at (1.80,-0.25) {car};
\node[tick, below] at (2.90,-0.93) {frog};
\end{tikzpicture}
\end{center}
```

Scores for an image of a cat (correct class highlighted) with $\Delta=1$. Every wrong class scoring above $s_y-\Delta$ adds its excess: car adds $5.1-3.2+1=2.9$, frog adds $0$, so the loss is $2.9$

:::

A term is zero exactly when the correct score exceeds the score of class $j$ by at least $\Delta$. With $K=2$ and scores $\pm\tfrac12\mathbf{w}\cdot\mathbf{x}$, the loss is the binary hinge loss of @prp-soft-margin-hinge.

::: {#exm-multiclass-svm-loss-1 .example name="Three classes"}

Let $\mathbf{s}=(2,5,-1)$, $y=0$, $\Delta=1$. The terms are $\max(0,5-2+1)=4$ for $j=1$ and $\max(0,-1-2+1)=0$ for $j=2$, so $L=4$. Only class $1$ violates the margin. The cross entropy loss of the same scores is $-\log\operatorname{softmax}(\mathbf{s})_0=3.051$.

Raising the correct score to $s_0=12$ makes $L=0$, since both margins now hold; the cross entropy loss drops to $0.0009$ but stays positive.

:::

::: {#fig-multiclass-svm-loss-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm,y=0.8cm]
\draw[->] (-3.2,0) -- (2.4,0) node[lab,anchor=west] {$s_j-s_y$};
\draw[->] (0,-0.2) -- (0,3.0) node[lab,anchor=south] {term};
\draw[hl] (-3.000,0.000) -- (-1.000,0.000) -- (1.800,2.800);
\draw[tick] (-1,0) -- (-1,-0.1) node[lab,anchor=north] {$-\Delta$};
\node[dot] at (1,2) {};
\node[lab,anchor=south east] at (1,2) {class 1};
\node[dot] at (-3,0) {};
\node[lab,anchor=south east] at (-3,0) {class 2};
\end{tikzpicture}
\end{center}
```

One term $\max(0,s_j-s_y+\Delta)$ of the multiclass SVM loss as a function of the score difference, with the two wrong classes of @exm-multiclass-svm-loss-1 ($\Delta=1$): class $1$ (difference $3$) contributes $4$; class $2$ (difference $-3$) is beyond the margin and contributes $0$.

:::

::: {#thm-multiclass-svm-gradient .theorem name="Gradient of the multiclass SVM loss"}

Let $\mathbf{s}=W\mathbf{x}$ and suppose no term of $L$ has $s_j-s_y+\Delta=0$. Let $\mathbb 1_j=1$ if $s_j-s_y+\Delta>0$ and $0$ otherwise ($j\ne y$). Then $L$ is differentiable at $W$ and its gradient has rows

$$
\nabla_{\mathbf{w}_j}L=\mathbb 1_j\,\mathbf{x}\quad(j\ne y),\qquad \nabla_{\mathbf{w}_y}L=-\Bigl(\sum_{j\ne y}\mathbb 1_j\Bigr)\mathbf{x}.
$$

:::

::: {.proof}

1. Near a point where $s_j-s_y+\Delta\ne0$, the term $\max(0,s_j-s_y+\Delta)$ equals either $0$ or $s_j-s_y+\Delta$ on a neighbourhood, so it is differentiable with derivative $\mathbb 1_j$ in $s_j$ and $-\mathbb 1_j$ in $s_y$.
2. Summing over $j\ne y$: $\partial L/\partial s_j=\mathbb 1_j$ for $j\ne y$ and $\partial L/\partial s_y=-\sum_{j\ne y}\mathbb 1_j$.
3. Since $s_k=\mathbf{w}_k\cdot\mathbf{x}$, the chain rule gives $\nabla_{\mathbf{w}_k}L=(\partial L/\partial s_k)\,\mathbf{x}$.

:::

At a point with $s_j-s_y+\Delta=0$ (a *kink*) the loss is not differentiable; numerical gradient checks (@sec-ai-deep-learning-gradient-checking) near such points can disagree with the formula.

::: {#prp-svm-scale-ambiguity .proposition name="Without regularization the weights are not determined"}

If $W$ gives zero data loss $\frac1N\sum_iL(W\mathbf{x}_i,y_i)$, then so does $cW$ for every $c\ge1$.

:::

::: {.proof}

1. Zero loss means $s_{y_i}-s_j\ge\Delta$ for all $i$ and $j\ne y_i$, where $\mathbf{s}=W\mathbf{x}_i$.
2. For $cW$ the score differences are multiplied by $c$, so they are at least $c\Delta\ge\Delta$, and every term stays $0$.

:::

The $\ell_2$ penalty (@def-regularization) picks among these the weights of smallest norm, which spreads weight over many input dimensions instead of a few. The same scaling shows that $\Delta$ itself carries no information once $\lambda$ is free: replacing $W$ by $W/\Delta$ turns margin $\Delta$ into margin $1$ and only rescales $\lambda$, so in practice $\Delta=1$.

::: {#rmk-svm-versus-softmax .remark name="SVM loss versus cross entropy"}

The SVM loss is satisfied once every margin holds: further changes of the scores do not change it (@exm-multiclass-svm-loss-1). The cross entropy loss is never exactly $0$ and keeps pushing the correct probability towards $1$. So adding a training example whose margins already hold leaves the SVM loss unchanged but increases the cross entropy loss. In accuracy the two classifiers are usually comparable; the softmax classifier also yields calibrated-looking probabilities, whose sharpness depends on the regularization strength.

:::
