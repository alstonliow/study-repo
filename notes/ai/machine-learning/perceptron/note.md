---
title: "The Perceptron"
sources: [cs188-21]
requires: [ai/machine-learning/linear-classification]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 21 (linear classifiers, the binary and multiclass perceptron, separability, convergence, problems with the perceptron, the move to probabilistic decisions), in our own wording; the mistake bound and its proof are written out in steps; the trace was computed in Python. -->

A linear classifier (@def-linear-classifier) needs weights. The perceptron finds them with the simplest possible rule: look at one example at a time, and change the weights only when the current weights get it wrong. Here the bias is folded into the weights by giving every feature vector $\mathbf f(x)$ a constant feature $1$, so the score is $\mathbf w\cdot\mathbf f(x)$.

::: {#def-perceptron .definition name="Binary perceptron"}

The *perceptron* for labels $y\in\{-1,+1\}$ starts with $\mathbf w=\mathbf 0$ and passes repeatedly over the training examples. For each example $(x,y)$ it predicts $\hat y=+1$ if $\mathbf w\cdot\mathbf f(x)>0$ and $-1$ otherwise; if $\hat y\ne y$ it updates
$$
\mathbf w\gets\mathbf w+y\,\mathbf f(x).
$$
It stops after a pass with no mistakes.

:::

```{=latex}
\begin{algorithm}
\caption{Binary perceptron}
\begin{algorithmic}
\INPUT Training examples $(x_1,y_1),\dots,(x_m,y_m)$, $y_i\in\{-1,+1\}$
\OUTPUT Weights $\mathbf w$
\STATE $\mathbf w\gets\mathbf 0$
\REPEAT
    \STATE $\mathit{mistakes}\gets0$
    \FOR{$i=1$ \textbf{to} $m$}
        \IF{$y_i\,\mathbf w\cdot\mathbf f(x_i)\le0$}
            \STATE $\mathbf w\gets\mathbf w+y_i\,\mathbf f(x_i)$; $\mathit{mistakes}\gets\mathit{mistakes}+1$
        \ENDIF
    \ENDFOR
\UNTIL{$\mathit{mistakes}=0$}
\RETURN $\mathbf w$
\end{algorithmic}
\end{algorithm}
```

After an update on a mistake, the score of that example changes by $y\,\|\mathbf f(x)\|^{2}$, in the right direction: the update moves the decision boundary towards classifying it correctly, though one update may not be enough. A mistake is the margin (@def-margin) being $\le0$, so the perceptron is stochastic gradient descent (@def-stochastic-gradient-descent) with step size $1$ on the loss $\max(0,-y\,\mathbf w\cdot\mathbf f(x))$.

::: {#exm-perceptron-trace .example name="Four points"}

With feature vectors $(1,a,b)$ for points $(a,b)$, let the examples, in this order, be $(1,2)$ labelled $+1$, $(2,0)$ labelled $-1$, $(0,1)$ labelled $+1$ and $(3,2)$ labelled $-1$. The first pass makes three mistakes: on $(1,2)$, giving $\mathbf w=(1,1,2)$; on $(2,0)$, giving $(0,-1,2)$; and on $(3,2)$, whose score is $-2+4=2>0$, giving $(-1,-4,0)$. The second pass makes one mistake, on $(1,2)$, giving $\mathbf w=(0,-3,2)$, which classifies all four points correctly (scores $1,-6,2,-5$); the third pass makes no mistakes and the perceptron stops.

:::

::: {#fig-perceptron-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[->] (-0.3,0) -- (3.6,0) node[lab, anchor=west] {$a$};
\draw[->] (0,-0.3) -- (0,3.2) node[lab, anchor=south] {$b$};
\node[hl dot] at (1,2) {};
\node[lab, tick, anchor=south west] at (1,2) {$(1,2)$};
\node[hollow dot] at (2,0) {};
\node[lab, tick, anchor=south west] at (2,0) {$(2,0)$};
\node[hl dot] at (0,1) {};
\node[lab, tick, anchor=south west] at (0,1) {$(0,1)$};
\node[hollow dot] at (3,2) {};
\node[lab, tick, anchor=south west] at (3,2) {$(3,2)$};
\draw[emph] (0,0) -- (2,3) node[lab, tick, anchor=south] {$-3a+2b=0$};
\end{tikzpicture}
\end{center}
```

The four examples of @exm-perceptron-trace (filled: $+1$, hollow: $-1$) and the final decision boundary $-3a+2b=0$ of the perceptron, which separates them.

:::

::: {#def-separable .definition name="Linearly separable"}

Training data is *linearly separable with margin $\gamma>0$* if there is a unit vector $\mathbf u$ with $y\,\mathbf u\cdot\mathbf f(x)\ge\gamma$ for every training example $(x,y)$.

:::

::: {#thm-perceptron-convergence .theorem name="Perceptron mistake bound"}

If the training data is linearly separable with margin $\gamma$ and $\|\mathbf f(x)\|\le R$ for every example, the perceptron makes at most $R^{2}/\gamma^{2}$ mistakes in total, whatever the order of the examples; in particular it stops.

:::

::: {.proof}

Let $\mathbf w_k$ be the weights after $k$ mistakes, $\mathbf w_0=\mathbf 0$, and let the $k$-th mistake be on $(x,y)$, so $\mathbf w_k=\mathbf w_{k-1}+y\,\mathbf f(x)$ and $y\,\mathbf w_{k-1}\cdot\mathbf f(x)\le0$.

1. Progress along $\mathbf u$: $\mathbf u\cdot\mathbf w_k=\mathbf u\cdot\mathbf w_{k-1}+y\,\mathbf u\cdot\mathbf f(x)\ge\mathbf u\cdot\mathbf w_{k-1}+\gamma$, so by induction $\mathbf u\cdot\mathbf w_k\ge k\gamma$.
2. Slow growth of the length: $\|\mathbf w_k\|^{2}=\|\mathbf w_{k-1}\|^{2}+2y\,\mathbf w_{k-1}\cdot\mathbf f(x)+\|\mathbf f(x)\|^{2}\le\|\mathbf w_{k-1}\|^{2}+R^{2}$, because the middle term is $\le0$ at a mistake. So $\|\mathbf w_k\|^{2}\le kR^{2}$.
3. By the Cauchy–Schwarz inequality and $\|\mathbf u\|=1$, $k\gamma\le\mathbf u\cdot\mathbf w_k\le\|\mathbf w_k\|\le\sqrt k\,R$.
4. Hence $\sqrt k\le R/\gamma$, that is $k\le R^{2}/\gamma^{2}$. Since every pass but the last makes a mistake, the number of passes is finite.

:::

::: {#def-multiclass-perceptron .definition name="Multiclass perceptron"}

For labels $y$ in a finite set, the *multiclass perceptron* keeps one weight vector $\mathbf w_y$ per label, predicts $\hat y=\operatorname{arg\,max}_y\mathbf w_y\cdot\mathbf f(x)$, and on a mistake ($\hat y\ne y$) updates
$$
\mathbf w_y\gets\mathbf w_y+\mathbf f(x),\qquad\mathbf w_{\hat y}\gets\mathbf w_{\hat y}-\mathbf f(x).
$$

:::

The update raises the score of the right label and lowers the score of the wrongly predicted one. With two labels and $\mathbf w=\mathbf w_{+1}-\mathbf w_{-1}$ it is the binary perceptron, with every step doubled.

::: {#rmk-perceptron-problems .remark name="Problems with the perceptron"}

If the data is not separable, the perceptron never stops and its weights keep jumping; averaging the weights over all steps (the *averaged perceptron*) gives a steadier and usually better classifier. On separable data it stops at the first separating weights it reaches, which may barely separate the data and so generalise poorly (@def-overfitting). And it outputs a decision but no confidence. Logistic regression (@def-logistic-regression) and its multiclass version, softmax regression (@def-softmax), address the last two: they turn scores into probabilities and choose the weights that make the training labels most probable, which prefers boundaries far from the data.

:::
