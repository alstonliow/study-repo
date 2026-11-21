---
title: "Training Deep Networks"
sources: [cs221-5, cs231n-6]
requires: [ai/deep-learning/neural-networks]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 5 (vanishing and exploding gradients, residual connections, layer normalization, initialization, optimizers), in our own wording. The variance computation for initialization is our own; proofs written out in steps. -->

Deep networks were long hard to train because signals and gradients shrink or grow geometrically with depth. Four standard fixes keep their size under control.

::: {#prp-vanishing-exploding-gradients .proposition name="Vanishing and exploding gradients"}

Let a network of $L$ scalar layers compute $x_\ell=w\,x_{\ell-1}$ with the same weight $w$, so $x_L=w^Lx_0$. Then

$$
\frac{\partial x_L}{\partial x_0}=w^L,\qquad \frac{\partial x_L}{\partial w}=L\,w^{L-1}x_0 .
$$

For $\lvert w\rvert<1$ both tend to $0$ geometrically in $L$ (vanishing gradients); for $\lvert w\rvert>1$ they grow geometrically (exploding gradients).

:::

::: {.proof}

1. $x_L=w^Lx_0$ by induction on $L$.

2. Differentiating in $x_0$ gives $w^L$, and in $w$ gives $Lw^{L-1}x_0$.

3. $\lvert w\rvert^L\to0$ for $\lvert w\rvert<1$, and $L\lvert w\rvert^{L-1}\to0$ too, since the geometric factor beats the linear one; both grow without bound for $\lvert w\rvert>1$.

:::

With $x_0=1$ and $L=20$: for $w=\tfrac12$, $x_L\approx9.5\times10^{-7}$ and $\partial x_L/\partial w\approx3.8\times10^{-5}$; for $w=2$, $x_L=1048576$ and $\partial x_L/\partial w\approx1.05\times10^{7}$. For matrices the same happens unless the singular values of the weight matrices stay close to $1$.

::: {#fig-training-deep-networks-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.22cm,y=0.12cm]
\draw[->] (0,0) -- (21.5,0) node[lab,anchor=north east] {layer $\ell$};
\draw[->] (0,-21) -- (0,21) node[lab,anchor=north west] {$\log_2 x_\ell$};
\draw[faint] (0,-21) -- (0,21);
\foreach \l in {5,10,15,20} { \node[lab,tick] at (\l,-1.8) {\l}; }
\foreach \y in {-20,-10,10,20} { \node[lab,tick] at (-1.5,\y) {\y}; }
\draw[hl] (0,0) -- (20,20) node[lab,anchor=west] {$w=2$};
\draw[hl,dashed] (0,0) -- (20,-20) node[lab,anchor=west] {$w=\tfrac12$};
\draw[emph] (0,0) -- (20,{20*log2(1.5)}) node[lab,anchor=west] {$x\mapsto x+\tfrac12x$};
\end{tikzpicture}
\end{center}
```

Size of $x_\ell=w^\ell$ through $20$ scalar layers (logarithmic scale): it explodes for $w=2$, vanishes for $w=\tfrac12$ and stays on the axis for $w=1$. With a residual connection, the layer with $w=\tfrac12$ multiplies by $1.5$ instead: still growing, but much more slowly than $w=2$, and away from zero.

:::

::: {#def-residual-connection .definition name="Residual connection"}

A layer $f$ with a *residual* (skip) *connection* computes $\mathbf{x}\mapsto\mathbf{x}+f(\mathbf{x})$ instead of $\mathbf{x}\mapsto f(\mathbf{x})$.

:::

For $f(x)=wx$ the layer multiplies by $1+w$ instead of $w$, which keeps the factor away from $0$ when $w$ is small; it can still explode when $w$ is large. The derivative of each layer is the identity plus that of $f$, so gradients reach early layers even when $f$ contributes little. Residual connections appear in LSTMs and residual networks, and in every modern deep architecture.

::: {#def-layer-normalization .definition name="Layer normalization"}

For a vector $\mathbf{x}\in\mathbb{R}^d$ with mean $\mu=\frac1d\sum_ix_i$ and variance $s^2=\frac1d\sum_i(x_i-\mu)^2$, *layer normalization* outputs

$$
\operatorname{LN}(\mathbf{x})_i=\gamma_i\,\frac{x_i-\mu}{\sqrt{s^2+\varepsilon}}+\beta_i ,
$$

where $\varepsilon>0$ is a small constant (such as $10^{-5}$) that prevents division by zero, and the scale $\boldsymbol\gamma\in\mathbb{R}^d$ and shift $\boldsymbol\beta\in\mathbb{R}^d$ are learned parameters ($2d$ per layer).

:::

::: {#prp-layer-normalization-scale .proposition name="Layer normalization removes scale"}

With $\varepsilon=0$, $\boldsymbol\gamma=\mathbf{1}$, $\boldsymbol\beta=\mathbf{0}$ and $\mathbf{x}$ not constant, $\operatorname{LN}(\mathbf{x})$ has mean $0$ and variance $1$, and $\operatorname{LN}(c\mathbf{x}+t\mathbf{1})=\operatorname{LN}(\mathbf{x})$ for every $c>0$ and $t\in\mathbb{R}$.

:::

::: {.proof}

1. The entries $(x_i-\mu)/s$ sum to $\frac1s\bigl(\sum_ix_i-d\mu\bigr)=0$, and their squares average to $s^2/s^2=1$.

2. Replacing $\mathbf{x}$ by $c\mathbf{x}+t\mathbf{1}$ replaces $\mu$ by $c\mu+t$ and $s$ by $cs$, so $x_i-\mu$ becomes $c(x_i-\mu)$ and the quotient is unchanged.

:::

For example, $(1,2,3)$ and $(100,200,300)$ both normalize to $\approx(-1.22,\,0,\,1.22)$. Whatever the size of a layer's input, its output has a fixed size, which keeps activations away from $0$ and $\infty$ (batch normalization normalizes over the examples of a batch instead).

::: {#prp-initialization-variance .proposition name="Scaling the initialization"}

Let $\mathbf{x}\in\mathbb{R}^d$ be fixed and let the weights $w_1,\dots,w_d$ be independent with mean $0$ and variance $v$. Then $y=\mathbf{w}\cdot\mathbf{x}$ has mean $0$ and variance $v\lVert\mathbf{x}\rVert^2$. In particular, if the entries of $\mathbf{x}$ have size about $1$, then $y$ has standard deviation about $\sqrt{v\,d}$, which is about $1$ for every $d$ exactly when $v=1/d$.

:::

::: {.proof}

1. By linearity of expectation, $E[y]=\sum_ix_iE[w_i]=0$.

2. The terms $x_iw_i$ are independent, so their variances add: $\operatorname{Var}(y)=\sum_ix_i^2\operatorname{Var}(w_i)=v\lVert\mathbf{x}\rVert^2$.

3. If each $x_i^2\approx1$ then $\lVert\mathbf{x}\rVert^2\approx d$, so $\operatorname{Var}(y)\approx vd$, which equals $1$ for $v=1/d$.

:::

::: {#def-xavier-initialization .definition name="Scaled initialization"}

A weight matrix with input dimension $d_{\text{in}}$ is *initialized* with independent entries drawn from a normal distribution with mean $0$ and standard deviation $1/\sqrt{d_{\text{in}}}$, often truncated to $[-3\sigma,3\sigma]$ to rule out rare large weights. Up to a constant factor this is *Xavier* (Glorot) initialization.

:::

By @prp-initialization-variance, the outputs of a layer then have about the same size as its inputs, whatever $d_{\text{in}}$, so changing the width of a network does not change the scale of its activations.

::: {#rmk-training-deep-networks-1 .remark name="Minibatches in practice"}

Stochastic gradient descent (@def-stochastic-gradient-descent) is usually run in *epochs*: each epoch shuffles the training examples and takes consecutive chunks of the shuffled order as minibatches, so every example is used once per epoch. Most networks are trained with adaptive optimizers such as Adam rather than plain SGD.

:::

<!-- Added 2026-11-21 from Stanford CS231n course notes (Neural networks part 2: weight initialization), in our own wording; the ReLU variance computation is written out as our own proof. -->

::: {#rmk-zero-initialization .remark name="Why not initialize at zero"}

If all weights of a layer start equal (for example all zero), every unit of the layer computes the same output and receives the same gradient, so the units stay identical for ever. Random initialization breaks this symmetry. Biases may start at zero.

:::

::: {#prp-he-initialization .proposition name="Initialization for ReLU layers" related="prp-initialization-variance"}

Let $z_1,\dots,z_d$ be independent, each symmetric about $0$ with variance $s^2$, let $x_j=\operatorname{ReLU}(z_j)$, and let $w_1,\dots,w_d$ be independent of them and of each other with mean $0$ and variance $v$. Then $y=\sum_jw_jx_j$ has mean $0$ and variance $\tfrac12dvs^2$. In particular $v=2/d$ gives $\operatorname{Var}(y)=s^2$.

:::

::: {.proof}

1. By independence and $\mathbb E[w_j]=0$, $\mathbb E[w_jx_j]=\mathbb E[w_j]\,\mathbb E[x_j]=0$, so $\mathbb E[y]=0$.
2. The terms $w_jx_j$ are independent with mean $0$, so $\operatorname{Var}(y)=\sum_j\mathbb E[w_j^2x_j^2]=\sum_jv\,\mathbb E[x_j^2]$.
3. By symmetry of $z_j$, $\mathbb E[x_j^2]=\mathbb E[z_j^2\,\mathbb 1\{z_j>0\}]=\tfrac12\mathbb E[z_j^2]=\tfrac12s^2$.
4. Hence $\operatorname{Var}(y)=dv\cdot\tfrac12s^2$, which equals $s^2$ when $v=2/d$.

:::

ReLU sets half of its inputs to zero, so it halves the second moment; *He initialization*, standard deviation $\sqrt{2/d_{\text{in}}}$, doubles the variance of @def-xavier-initialization to compensate, and keeps the size of the pre-activations constant through a deep ReLU network.

