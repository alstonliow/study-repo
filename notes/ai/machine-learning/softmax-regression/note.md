---
title: "Softmax and Cross Entropy"
sources: [cs221-3, eecs126-7]
requires: [ai/machine-learning/logistic-regression]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 3 (multiclass classification, softmax, cross entropy), in our own wording. Gibbs' inequality, the gradient formula and the two-class reduction are our own additions; proofs written out in steps. -->

For $K$ classes $y\in\{0,\dots,K-1\}$, a linear model computes one logit per class and turns the logits into a probability distribution.

::: {#def-softmax .definition name="Softmax"}

The *softmax* of a vector of logits $\mathbf{z}=(z_0,\dots,z_{K-1})\in\mathbb{R}^K$ is the probability vector

$$
\operatorname{softmax}(\mathbf{z})_k=\frac{e^{z_k}}{\sum_{j=0}^{K-1}e^{z_j}},\qquad k=0,\dots,K-1.
$$

The *multiclass linear model* has a weight vector $\mathbf{w}_k$ and bias $b_k$ for each class, that is, a matrix $W$ with rows $\mathbf{w}_k^{\mathsf T}$ and a vector $\mathbf{b}$, and sets $p_\theta(k\mid\mathbf{x})=\operatorname{softmax}(W\mathbf{x}+\mathbf{b})_k$. It predicts the class of largest logit.

:::

::: {#fig-softmax-regression-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw (0,0) -- (3.2,0);
\path[bar] (0.20,0) rectangle (0.60,1.40);
\node[tick, above] at (0.40,1.40) {$2.0$};
\path[bar] (0.95,0) rectangle (1.35,0.70);
\node[tick, above] at (1.15,0.70) {$1.0$};
\path[bar] (1.70,0) rectangle (2.10,0.07);
\node[tick, above] at (1.90,0.07) {$0.1$};
\path[bar] (2.45,0) rectangle (2.85,-0.70);
\node[tick, below] at (2.65,-0.70) {$-1.0$};
\node[tick] at (1.6,-1.3) {logits $\mathbf z$};
\draw[map] (3.4,0.5) -- node[tick, above] {softmax} (4.8,0.5);
\begin{scope}[xshift=5.0cm]
\draw (0,0) -- (3.2,0);
\path[hl cell] (0.20,0) rectangle (0.60,1.53);
\node[tick, above] at (0.40,1.53) {$0.64$};
\path[hl cell] (0.95,0) rectangle (1.35,0.56);
\node[tick, above] at (1.15,0.56) {$0.23$};
\path[hl cell] (1.70,0) rectangle (2.10,0.23);
\node[tick, above] at (1.90,0.23) {$0.10$};
\path[hl cell] (2.45,0) rectangle (2.85,0.08);
\node[tick, above] at (2.65,0.08) {$0.03$};
\node[tick] at (1.6,-1.3) {probabilities};
\end{scope}
\end{tikzpicture}
\end{center}
```

Softmax turns logits $\mathbf z=(2,1,0.1,-1)$ into probabilities: it keeps the order, makes every entry positive and normalizes the sum to $1$

:::

::: {#prp-softmax-shift .proposition name="Softmax ignores a common shift"}

For every $c\in\mathbb{R}$, $\operatorname{softmax}(\mathbf{z}+c\mathbf{1})=\operatorname{softmax}(\mathbf{z})$. With $K=2$, $\operatorname{softmax}(z_0,z_1)_1=\sigma(z_1-z_0)$, the logistic function of the difference of logits.

:::

::: {.proof}

1. Each term $e^{z_k+c}=e^c e^{z_k}$, so numerator and denominator are both multiplied by $e^c$.

2. For $K=2$, divide numerator and denominator by $e^{z_1}$: $\dfrac{e^{z_1}}{e^{z_0}+e^{z_1}}=\dfrac{1}{1+e^{-(z_1-z_0)}}=\sigma(z_1-z_0)$.

:::

So binary logistic regression is the case $K=2$ with a single logit $z_1-z_0$. In code the shift is used with $c=-\max_k z_k$, which keeps the exponentials from overflowing.

::: {#def-cross-entropy .definition name="Cross entropy"}

For probability distributions $p$ (the target) and $q$ (the prediction) on $\{0,\dots,K-1\}$, the *cross entropy* is

$$
H(p,q)=-\sum_{k}p(k)\log q(k),
$$

and the *entropy* of $p$ is $H(p)=H(p,p)$. It is large when $p$ puts mass on an outcome to which $q$ gives low probability.

:::

::: {#thm-gibbs-inequality .theorem name="Gibbs' inequality"}

For all distributions $p,q$ with $q(k)>0$ wherever $p(k)>0$,

$$
H(p,q)\ \ge\ H(p),
$$

with equality if and only if $q=p$. Equivalently, in terms of the relative entropy $D(p\,\|\,q)=H(p,q)-H(p)$ (@def-relative-entropy),
$$
D(p\,\|\,q)\ \ge\ 0 .
$$
So for a fixed target, the cross entropy is smallest when the prediction equals the target.

:::

::: {#fig-softmax-regression-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.6,0) node[lab, right] {$k$};
\path[bar] (0.20,0) rectangle (0.50,1.80);
\path[hl cell] (0.50,0) rectangle (0.80,0.75);
\path[bar] (1.20,0) rectangle (1.50,0.75);
\path[hl cell] (1.50,0) rectangle (1.80,0.75);
\path[bar] (2.20,0) rectangle (2.50,0.30);
\path[hl cell] (2.50,0) rectangle (2.80,0.75);
\path[bar] (3.20,0) rectangle (3.50,0.15);
\path[hl cell] (3.50,0) rectangle (3.80,0.75);
\node[tick, right] at (2.4,1.9) {dark $\mathbf p$, light $\mathbf q$};
\end{tikzpicture}
\end{center}
```

Gibbs' inequality: the cross entropy $-\sum_kp_k\log q_k$ of $\mathbf p$ relative to any $\mathbf q$ (here uniform) is at least the entropy of $\mathbf p$, with equality only when $\mathbf q=\mathbf p$

:::

<!-- Merged 2026-11-19 (owner decision): this block also replaces thm-gibbs-inequality from UC Berkeley EECS126 (note "Information Theory Introduction"), which stated the D(p||q) >= 0 form with the same proof. Statement and proof are the CS221 version; the D(p||q) form was added from EECS126. -->

::: {.proof}

1. Let $S=\{k:p(k)>0\}$. Then $H(p,q)-H(p)=-\sum_{k\in S}p(k)\log\dfrac{q(k)}{p(k)}$.

2. Use $\log t\le t-1$ for $t>0$, with equality only at $t=1$. With $t=q(k)/p(k)$,
$$
-\sum_{k\in S}p(k)\log\frac{q(k)}{p(k)}\ \ge\ -\sum_{k\in S}p(k)\Bigl(\frac{q(k)}{p(k)}-1\Bigr)=\sum_{k\in S}p(k)-\sum_{k\in S}q(k)=1-\sum_{k\in S}q(k)\ \ge\ 0 .
$$

3. Equality throughout needs $q(k)=p(k)$ for every $k\in S$ (step 2's inequality) and then $q$ has total mass $1$ on $S$, so $q=0$ off $S$, that is, $q=p$. Conversely $q=p$ gives equality.

:::

::: {#def-cross-entropy-loss .definition name="Cross entropy loss"}

For the multiclass linear model and an example $(\mathbf{x},y)$, take the target to be the one-hot distribution on $y$. Its cross entropy with the prediction is the *cross entropy loss*

$$
\text{Loss}(\mathbf{x},y,\theta)=-\log\operatorname{softmax}(W\mathbf{x}+\mathbf{b})_y ,
$$

the negative log probability of the correct class. For $K=2$ it is the logistic loss.

:::

::: {#fig-softmax-regression-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.6,0) node[lab, right] {$p_y$};
\draw[->] (0,0) -- (0,2.8) node[lab, above] {loss};
\draw[emph, domain=0.12:4, samples=80, smooth, variable=\x] plot ({\x}, {-0.6*ln(\x/4)});
\draw (4,0) -- (4,-0.08) node[tick, below] {$1$};
\draw (2,0) -- (2,-0.08) node[tick, below] {$\tfrac12$};
\end{tikzpicture}
\end{center}
```

The cross entropy loss $-\log p_y$ as a function of the probability $p_y$ given to the correct class: $0$ when $p_y=1$ and unbounded as $p_y\to0$

:::

::: {#thm-cross-entropy-gradient .theorem name="Gradient of the cross entropy loss"}

Let $\mathbf{z}=W\mathbf{x}+\mathbf{b}$, $\mathbf{q}=\operatorname{softmax}(\mathbf{z})$ and $\mathbf{e}_y$ the one-hot vector of $y$. Then

$$
\nabla_{\mathbf{z}}\text{Loss}=\mathbf{q}-\mathbf{e}_y,\qquad
\nabla_{W}\text{Loss}=(\mathbf{q}-\mathbf{e}_y)\,\mathbf{x}^{\mathsf T},\qquad
\nabla_{\mathbf{b}}\text{Loss}=\mathbf{q}-\mathbf{e}_y .
$$

:::

::: {.proof}

1. $\text{Loss}=-z_y+\log\sum_j e^{z_j}$.

2. Differentiating in $z_k$: $\dfrac{\partial\,\text{Loss}}{\partial z_k}=-\mathbf{1}[k=y]+\dfrac{e^{z_k}}{\sum_j e^{z_j}}=q_k-\mathbf{1}[k=y]$.

3. Since $z_k=\mathbf{w}_k\cdot\mathbf{x}+b_k$, we have $\partial z_k/\partial W_{kj}=x_j$, $\partial z_k/\partial b_k=1$, and $z_k$ does not depend on the other rows. The chain rule gives $\partial\,\text{Loss}/\partial W_{kj}=(q_k-\mathbf{1}[k=y])\,x_j$ and $\partial\,\text{Loss}/\partial b_k=q_k-\mathbf{1}[k=y]$.

:::

::: {#exm-softmax-regression-1 .example name="Three classes"}

Logits $\mathbf{z}=(1,2,3)$ give $\operatorname{softmax}(\mathbf{z})\approx(0.090,\,0.245,\,0.665)$, the same as for $(101,102,103)$. If the target is class $0$, the loss is $-\log0.090\approx2.41$, and the gradient with respect to the logits is $\mathbf{q}-\mathbf{e}_0\approx(-0.910,\,0.245,\,0.665)$: gradient descent raises the logit of the target class and lowers the others in proportion to their probabilities.

:::
