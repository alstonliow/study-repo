---
title: "Generative Models and Autoregressive Image Models"
sources: [cs231n-15]
requires: [ai/unsupervised-learning/variational-autoencoders, ai/deep-learning/convolutional-layers, ai/deep-learning/recurrent-neural-networks]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Generative modeling: supervised versus unsupervised learning, explicit and implicit density models, PixelRNN, PixelCNN and masked convolutions), in our own wording; the masking proposition and its proof are our own. -->

A *generative model* learns a distribution $p_{\text{model}}$ close to the data distribution $p_{\text{data}}$ from unlabelled samples, and can draw new samples from it. Models differ in how they represent $p_{\text{model}}$:

1. *explicit, tractable density*: $p_{\text{model}}(\mathbf{x})$ can be computed exactly, as for the autoregressive models below;
2. *explicit, approximate density*: only a bound on $\log p_{\text{model}}(\mathbf{x})$ can be computed, as for the VAE (@def-vae) and diffusion models (@sec-ai-unsupervised-learning-diffusion-models);
3. *implicit density*: the model only samples, as a GAN does (@sec-ai-unsupervised-learning-generative-adversarial-networks).

::: {#def-autoregressive-image-model .definition name="Autoregressive image model"}

Order the $n$ pixel values of an image $\mathbf{x}=(x_1,\dots,x_n)$ (row by row, and within a pixel the colour channels R, G, B). An *autoregressive image model* writes the density by the chain rule,

$$
p_\theta(\mathbf{x})=\prod_{i=1}^{n}p_\theta(x_i\mid x_1,\dots,x_{i-1}),
$$

each factor a softmax over the $256$ possible values of $x_i$ computed by a network from the earlier pixels. It is trained by maximizing the log-likelihood $\sum_i\log p_\theta(x_i\mid x_{<i})$ of the training images, a sum of cross entropy losses.

:::

Every distribution can be written this way, so nothing is assumed except the network's ability to represent the conditionals. The models differ in how they compute them. *PixelRNN* runs recurrent layers (LSTMs, @def-lstm) along the rows and columns, so that each pixel's state depends on the pixel to its left and the one above, and through them on all earlier pixels. It is expressive but strictly sequential, in training as well as in sampling.

::: {#def-masked-convolution .definition name="Masked convolution"}

A *masked convolution* multiplies each $F\times F$ filter (@def-convolutional-layer, stride $1$, same padding, $F$ odd) by a fixed mask that zeroes the taps at the positions after the centre in raster order: all rows below the centre, and in the centre row all columns to its right. A mask of *type A* also zeroes the centre tap; a mask of *type B* keeps it. *PixelCNN* stacks one type-A layer followed by type-B layers, and outputs at each position the logits of that pixel's conditional.

:::

::: {#fig-autoregressive-image-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[hl cell] (0.00,0.00) rectangle (0.55,0.55);
\node[lab,tick] at (0.275,0.275) {$1$};
\draw[hl cell] (0.55,0.00) rectangle (1.10,0.55);
\node[lab,tick] at (0.825,0.275) {$1$};
\draw[hl cell] (1.10,0.00) rectangle (1.65,0.55);
\node[lab,tick] at (1.375,0.275) {$1$};
\draw[hl cell] (0.00,-0.55) rectangle (0.55,0.00);
\node[lab,tick] at (0.275,-0.275) {$1$};
\draw[cell frame] (0.55,-0.55) rectangle (1.10,0.00);
\node[lab,tick] at (0.825,-0.275) {$0$};
\draw[cell frame] (1.10,-0.55) rectangle (1.65,0.00);
\node[lab,tick] at (1.375,-0.275) {$0$};
\draw[cell frame] (0.00,-1.10) rectangle (0.55,-0.55);
\node[lab,tick] at (0.275,-0.825) {$0$};
\draw[cell frame] (0.55,-1.10) rectangle (1.10,-0.55);
\node[lab,tick] at (0.825,-0.825) {$0$};
\draw[cell frame] (1.10,-1.10) rectangle (1.65,-0.55);
\node[lab,tick] at (1.375,-0.825) {$0$};
\node[lab] at (0.825,0.85) {type A};
\draw[hl cell] (2.60,0.00) rectangle (3.15,0.55);
\node[lab,tick] at (2.875,0.275) {$1$};
\draw[hl cell] (3.15,0.00) rectangle (3.70,0.55);
\node[lab,tick] at (3.425,0.275) {$1$};
\draw[hl cell] (3.70,0.00) rectangle (4.25,0.55);
\node[lab,tick] at (3.975,0.275) {$1$};
\draw[hl cell] (2.60,-0.55) rectangle (3.15,0.00);
\node[lab,tick] at (2.875,-0.275) {$1$};
\draw[hl cell] (3.15,-0.55) rectangle (3.70,0.00);
\node[lab,tick] at (3.425,-0.275) {$1$};
\draw[cell frame] (3.70,-0.55) rectangle (4.25,0.00);
\node[lab,tick] at (3.975,-0.275) {$0$};
\draw[cell frame] (2.60,-1.10) rectangle (3.15,-0.55);
\node[lab,tick] at (2.875,-0.825) {$0$};
\draw[cell frame] (3.15,-1.10) rectangle (3.70,-0.55);
\node[lab,tick] at (3.425,-0.825) {$0$};
\draw[cell frame] (3.70,-1.10) rectangle (4.25,-0.55);
\node[lab,tick] at (3.975,-0.825) {$0$};
\node[lab] at (3.425,0.85) {type B};
\end{tikzpicture}
\end{center}
```

The $3\times3$ masks of PixelCNN (@def-masked-convolution): kept taps (1) lie in the row above or to the left in the centre row; type A also drops the centre, so the first layer never sees the pixel it predicts.

:::

::: {#prp-masked-convolution-causal .proposition name="Masked convolutions see only earlier pixels"}

In PixelCNN (one channel per pixel for simplicity), the output at position $i$ depends only on the input pixels $x_j$ with $j<i$ in raster order.

:::

::: {.proof}

1. Say a feature map is *causal* if its value at position $i$ depends only on inputs $x_j$ with $j<i$ (*strictly*), or with $j\le i$ (*weakly*).
2. The input itself is weakly causal. A type-A layer combines input values at positions strictly before $i$ in raster order (the kept taps lie in earlier rows, or in the same row to the left), so its output is strictly causal.
3. A type-B layer applied to a strictly causal map combines its values at positions $j\le i$, each depending on inputs before $j$, hence before $i$; so its output is again strictly causal, and element-wise activations preserve this.
4. By induction over the layers, the final output is strictly causal.

:::

So during training all $n$ conditionals are computed in one parallel forward pass over the real image, unlike PixelRNN. Sampling is still sequential: the model must be run once per pixel, feeding each sampled value back before computing the next.

```{=latex}
\begin{algorithm}
\caption{Sampling from an autoregressive image model}
\begin{algorithmic}
\INPUT trained conditionals $p_\theta(x_i\mid x_{<i})$, number $n$ of pixel values
\OUTPUT a sampled image $\mathbf{x}$
\STATE $\mathbf{x}\gets$ all zeros
\FOR{$i=1$ \TO $n$}
    \STATE compute the logits of $x_i$ by a forward pass on the current $\mathbf{x}$
    \STATE draw $x_i$ from their softmax
\ENDFOR
\RETURN $\mathbf{x}$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-autoregressive-image-models-1 .remark name="Strengths and weaknesses"}

Autoregressive models have an exact likelihood, which makes them easy to train and to compare (in bits per dimension), and their samples are diverse. Their samples are slow to draw, $n$ network evaluations for one image, and a plain masked stack has a *blind spot*: with $3\times3$ masks, some pixels above and to the right of $i$ never enter its receptive field. Later versions (gated PixelCNN) split the computation into a vertical and a horizontal stack to remove it. The same factorization over tokens is the basis of language models (@def-autoregressive-model).

:::
