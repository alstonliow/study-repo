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
