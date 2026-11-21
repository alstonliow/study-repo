---
title: "Batch Normalization"
sources: [cs231n-6, cs231na-2]
requires: [ai/deep-learning/training-deep-networks, ai/deep-learning/data-preprocessing]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Neural networks part 2: batch normalization) and Assignment 2 (batch and layer normalization, forward and backward passes), in our own wording; the backward-pass theorem and the scale proposition are our own proofs; the example was computed with NumPy. -->

Preprocessing (@def-centring-scaling) standardizes the inputs of the first layer only. *Batch normalization* standardizes the inputs of later layers as well, using the statistics of the current minibatch, and then lets the network rescale them.

::: {#def-batch-normalization .definition name="Batch normalization"}

Let a minibatch give a layer the inputs $X\in\mathbb{R}^{N\times D}$ (one row per example). In *training mode*, *batch normalization* with learnt $\boldsymbol\gamma,\boldsymbol\beta\in\mathbb{R}^D$ and a small $\varepsilon>0$ computes, for each feature $j$,

$$
\mu_j=\frac1N\sum_{i=1}^NX_{ij},\qquad \sigma_j^2=\frac1N\sum_{i=1}^N(X_{ij}-\mu_j)^2,\qquad \hat X_{ij}=\frac{X_{ij}-\mu_j}{\sqrt{\sigma_j^2+\varepsilon}},\qquad Y_{ij}=\gamma_j\hat X_{ij}+\beta_j .
$$

It also keeps running averages $\bar\mu_j\gets m\bar\mu_j+(1-m)\mu_j$ and $\bar\sigma_j^2\gets m\bar\sigma_j^2+(1-m)\sigma_j^2$ with a momentum $m$ such as $0.9$. In *test mode* it uses $\bar\mu_j,\bar\sigma_j^2$ in place of $\mu_j,\sigma_j^2$, so each example's output no longer depends on the rest of the batch.

:::

::: {#fig-batch-normalization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[cell frame] (0.00,0.00) rectangle (0.55,0.55);
\draw[hl cell] (0.55,0.00) rectangle (1.10,0.55);
\draw[cell frame] (1.10,0.00) rectangle (1.65,0.55);
\draw[cell frame] (1.65,0.00) rectangle (2.20,0.55);
\draw[cell frame] (2.20,0.00) rectangle (2.75,0.55);
\draw[cell frame] (0.00,-0.55) rectangle (0.55,0.00);
\draw[hl cell] (0.55,-0.55) rectangle (1.10,0.00);
\draw[cell frame] (1.10,-0.55) rectangle (1.65,0.00);
\draw[cell frame] (1.65,-0.55) rectangle (2.20,0.00);
\draw[cell frame] (2.20,-0.55) rectangle (2.75,0.00);
\draw[cell frame] (0.00,-1.10) rectangle (0.55,-0.55);
\draw[hl cell] (0.55,-1.10) rectangle (1.10,-0.55);
\draw[cell frame] (1.10,-1.10) rectangle (1.65,-0.55);
\draw[cell frame] (1.65,-1.10) rectangle (2.20,-0.55);
\draw[cell frame] (2.20,-1.10) rectangle (2.75,-0.55);
\draw[cell frame] (0.00,-1.65) rectangle (0.55,-1.10);
\draw[hl cell] (0.55,-1.65) rectangle (1.10,-1.10);
\draw[cell frame] (1.10,-1.65) rectangle (1.65,-1.10);
\draw[cell frame] (1.65,-1.65) rectangle (2.20,-1.10);
\draw[cell frame] (2.20,-1.65) rectangle (2.75,-1.10);
\node[lab] at (1.375,0.9) {batch norm: one column};
\node[lab,tick,anchor=east] at (-0.05,-0.55) {$N$};
\node[lab,tick,anchor=north] at (1.375,-1.7) {$D$};
\draw[cell frame] (4.20,0.00) rectangle (4.75,0.55);
\draw[cell frame] (4.75,0.00) rectangle (5.30,0.55);
\draw[cell frame] (5.30,0.00) rectangle (5.85,0.55);
\draw[cell frame] (5.85,0.00) rectangle (6.40,0.55);
\draw[cell frame] (6.40,0.00) rectangle (6.95,0.55);
\draw[cell frame] (4.20,-0.55) rectangle (4.75,0.00);
\draw[cell frame] (4.75,-0.55) rectangle (5.30,0.00);
\draw[cell frame] (5.30,-0.55) rectangle (5.85,0.00);
\draw[cell frame] (5.85,-0.55) rectangle (6.40,0.00);
\draw[cell frame] (6.40,-0.55) rectangle (6.95,0.00);
\draw[hl cell] (4.20,-1.10) rectangle (4.75,-0.55);
\draw[hl cell] (4.75,-1.10) rectangle (5.30,-0.55);
\draw[hl cell] (5.30,-1.10) rectangle (5.85,-0.55);
\draw[hl cell] (5.85,-1.10) rectangle (6.40,-0.55);
\draw[hl cell] (6.40,-1.10) rectangle (6.95,-0.55);
\draw[cell frame] (4.20,-1.65) rectangle (4.75,-1.10);
\draw[cell frame] (4.75,-1.65) rectangle (5.30,-1.10);
\draw[cell frame] (5.30,-1.65) rectangle (5.85,-1.10);
\draw[cell frame] (5.85,-1.65) rectangle (6.40,-1.10);
\draw[cell frame] (6.40,-1.65) rectangle (6.95,-1.10);
\node[lab] at (5.575,0.9) {layer norm: one row};
\node[lab,tick,anchor=east] at (4.15,-0.55) {$N$};
\node[lab,tick,anchor=north] at (5.575,-1.7) {$D$};
\end{tikzpicture}
\end{center}
```

Which entries share a mean and a variance, for a batch of $N$ examples (rows) with $D$ features (columns): batch normalization standardizes each column over the batch, layer normalization each row over its features.

:::

Layer normalization (@def-layer-normalization) applies the same formula along the other axis: over the $D$ features of one example instead of over the $N$ examples of one feature. With $\boldsymbol\gamma=\sqrt{\boldsymbol\sigma^2+\varepsilon}$ and $\boldsymbol\beta=\boldsymbol\mu$ the layer could undo the normalization, so it removes no expressive power. It is usually placed after a fully connected or convolutional layer and before the activation.

```{=latex}
\begin{algorithm}
\caption{Batch normalization, training-mode forward pass}
\begin{algorithmic}
\INPUT minibatch $X\in\mathbb{R}^{N\times D}$, $\boldsymbol\gamma,\boldsymbol\beta$, $\varepsilon$, momentum $m$, running $\bar{\boldsymbol\mu},\bar{\boldsymbol\sigma}^2$
\OUTPUT $Y$ and updated running statistics
\FOR{$j=1$ \TO $D$}
    \STATE $\mu_j\gets$ mean of column $j$; $\sigma_j^2\gets$ its variance (divided by $N$)
    \STATE $\hat X_{:j}\gets(X_{:j}-\mu_j)/\sqrt{\sigma_j^2+\varepsilon}$; $Y_{:j}\gets\gamma_j\hat X_{:j}+\beta_j$
    \STATE $\bar\mu_j\gets m\bar\mu_j+(1-m)\mu_j$; $\bar\sigma_j^2\gets m\bar\sigma_j^2+(1-m)\sigma_j^2$
\ENDFOR
\RETURN $Y$, $\bar{\boldsymbol\mu}$, $\bar{\boldsymbol\sigma}^2$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-batch-normalization-1 .example name="One feature, three examples"}

Let one feature take the values $1,2,6$ in a batch of three, with $\varepsilon=0$, $\gamma=1$, $\beta=0$. Then $\mu=3$, $\sigma^2=\tfrac{4+1+9}{3}=\tfrac{14}{3}$, $\sigma\approx2.160$, and the outputs are $-0.926,\ -0.463,\ 1.389$, with mean $0$ and variance $1$. Changing the third value to $60$ changes all three outputs, so in training mode an example's output depends on its batch.

:::

::: {#thm-batch-normalization-backward .theorem name="Backward pass of batch normalization"}

Fix a feature $j$ and drop the index $j$: inputs $x_1,\dots,x_N$, $\hat x_i=(x_i-\mu)/s$ with $s=\sqrt{\sigma^2+\varepsilon}$, outputs $y_i=\gamma\hat x_i+\beta$. Let $g_i=\partial L/\partial y_i$. Then

$$
\frac{\partial L}{\partial\gamma}=\sum_ig_i\hat x_i,\qquad \frac{\partial L}{\partial\beta}=\sum_ig_i,\qquad
\frac{\partial L}{\partial x_i}=\frac{\gamma}{Ns}\Bigl(Ng_i-\sum_kg_k-\hat x_i\sum_kg_k\hat x_k\Bigr).
$$

:::

::: {.proof}

1. The formulas for $\gamma$ and $\beta$ follow from $\partial y_i/\partial\gamma=\hat x_i$ and $\partial y_i/\partial\beta=1$, summed over the batch.
2. Write $h_i=\partial L/\partial\hat x_i=\gamma g_i$. Each $\hat x_k$ depends on $x_i$ directly and through $\mu$ and $s$.
3. $\partial\mu/\partial x_i=1/N$. Since $\sigma^2=\frac1N\sum_k(x_k-\mu)^2$ and $\sum_k(x_k-\mu)=0$, $\partial\sigma^2/\partial x_i=\frac2N(x_i-\mu)$, so $\partial s/\partial x_i=\frac{x_i-\mu}{Ns}=\frac{\hat x_i}{N}$.
4. Hence $\dfrac{\partial\hat x_k}{\partial x_i}=\dfrac{\delta_{ki}-1/N}{s}-\dfrac{x_k-\mu}{s^2}\cdot\dfrac{\hat x_i}{N}=\dfrac1s\Bigl(\delta_{ki}-\dfrac1N-\dfrac{\hat x_k\hat x_i}{N}\Bigr)$.
5. Then $\dfrac{\partial L}{\partial x_i}=\sum_kh_k\dfrac{\partial\hat x_k}{\partial x_i}=\dfrac1{Ns}\Bigl(Nh_i-\sum_kh_k-\hat x_i\sum_kh_k\hat x_k\Bigr)$, and substituting $h_k=\gamma g_k$ gives the claim.

:::

The gradient on the inputs is the upstream gradient with its mean removed and its component along $\hat{\mathbf{x}}$ removed, then scaled: two directions the normalization makes the loss insensitive to.

::: {#prp-batch-normalization-scale .proposition name="Batch normalization ignores the scale of the previous layer"}

Let $X=HW$ for inputs $H$ and weights $W$, and let $\varepsilon=0$ and no column of $X$ be constant. For every $c>0$ the training-mode output for $HW$ and for $H(cW)$ is the same.

:::

::: {.proof}

1. Replacing $W$ by $cW$ multiplies every column of $X$ by $c$.
2. Then $\mu_j$ becomes $c\mu_j$ and $\sigma_j$ becomes $c\sigma_j$, so $\hat X_{ij}=(cX_{ij}-c\mu_j)/(c\sigma_j)$ is unchanged, and so is $Y$.

:::

So a network with batch normalization is much less sensitive to the scale of its initial weights (@prp-initialization-variance), and tolerates larger learning rates.

::: {#rmk-batch-normalization-1 .remark name="Batch size, spatial batch normalization and alternatives"}

The batch statistics are noisy estimates of the true ones, so batch normalization works poorly with very small batches, and the mismatch between batch statistics (training) and running averages (test) grows. The noise also acts as a mild regularizer. For convolutional layers with activations of shape $N\times C\times H\times W$, *spatial batch normalization* computes one mean and variance per channel over the $N\cdot H\cdot W$ values, so that every position of a feature map is treated alike. Layer normalization, which uses no batch statistics, is preferred in recurrent networks and transformers; it works poorly when an example has only a few features, since its statistics are then noisy. *Group normalization* normalizes each example over groups of channels, between the two.

:::
