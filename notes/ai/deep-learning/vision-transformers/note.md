---
title: "Vision Transformers"
sources: [cs231na-3]
requires: [ai/deep-learning/attention-and-transformers, ai/deep-learning/convolutional-layers]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n Assignment 3 (vision transformer on CIFAR-10: patch embedding, encoder layers, average pooling, positional encoding), in our own wording; the cost proposition, its proof and the numbers are our own. -->

A transformer (@def-transformer-block) works on a sequence of vectors. A *vision transformer* (ViT) turns an image into such a sequence by cutting it into square patches, and then uses an unmasked transformer encoder exactly as for text.

::: {#def-patch-embedding .definition name="Patch embedding"}

Let an image have shape $C\times H\times W$ and let $P$ divide $H$ and $W$. The *patch embedding* cuts the image into $N=HW/P^2$ non-overlapping patches of $P\times P$ pixels, flattens each to a vector of length $CP^2$, and maps it to $\mathbb{R}^d$ by one shared linear layer $E\in\mathbb{R}^{d\times CP^2}$ with a bias. It equals a convolutional layer (@def-convolutional-layer) with $d$ filters of size $P$ and stride $S=P$.

:::

::: {#fig-vision-transformers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[cell frame] (0.00,0.00) rectangle (0.32,0.32);
\draw[cell frame] (0.32,0.00) rectangle (0.64,0.32);
\draw[cell frame] (0.64,0.00) rectangle (0.96,0.32);
\draw[cell frame] (0.96,0.00) rectangle (1.28,0.32);
\draw[cell frame] (1.28,0.00) rectangle (1.60,0.32);
\draw[cell frame] (1.60,0.00) rectangle (1.92,0.32);
\draw[cell frame] (1.92,0.00) rectangle (2.24,0.32);
\draw[cell frame] (2.24,0.00) rectangle (2.56,0.32);
\draw[cell frame] (2.56,0.00) rectangle (2.88,0.32);
\draw[cell frame] (2.88,0.00) rectangle (3.20,0.32);
\draw[cell frame] (3.20,0.00) rectangle (3.52,0.32);
\draw[cell frame] (3.52,0.00) rectangle (3.84,0.32);
\draw[cell frame] (0.00,-0.32) rectangle (0.32,0.00);
\draw[cell frame] (0.32,-0.32) rectangle (0.64,0.00);
\draw[cell frame] (0.64,-0.32) rectangle (0.96,0.00);
\draw[cell frame] (0.96,-0.32) rectangle (1.28,0.00);
\draw[cell frame] (1.28,-0.32) rectangle (1.60,0.00);
\draw[cell frame] (1.60,-0.32) rectangle (1.92,0.00);
\draw[cell frame] (1.92,-0.32) rectangle (2.24,0.00);
\draw[cell frame] (2.24,-0.32) rectangle (2.56,0.00);
\draw[cell frame] (2.56,-0.32) rectangle (2.88,0.00);
\draw[cell frame] (2.88,-0.32) rectangle (3.20,0.00);
\draw[cell frame] (3.20,-0.32) rectangle (3.52,0.00);
\draw[cell frame] (3.52,-0.32) rectangle (3.84,0.00);
\draw[cell frame] (0.00,-0.64) rectangle (0.32,-0.32);
\draw[cell frame] (0.32,-0.64) rectangle (0.64,-0.32);
\draw[cell frame] (0.64,-0.64) rectangle (0.96,-0.32);
\draw[cell frame] (0.96,-0.64) rectangle (1.28,-0.32);
\draw[cell frame] (1.28,-0.64) rectangle (1.60,-0.32);
\draw[cell frame] (1.60,-0.64) rectangle (1.92,-0.32);
\draw[cell frame] (1.92,-0.64) rectangle (2.24,-0.32);
\draw[cell frame] (2.24,-0.64) rectangle (2.56,-0.32);
\draw[cell frame] (2.56,-0.64) rectangle (2.88,-0.32);
\draw[cell frame] (2.88,-0.64) rectangle (3.20,-0.32);
\draw[cell frame] (3.20,-0.64) rectangle (3.52,-0.32);
\draw[cell frame] (3.52,-0.64) rectangle (3.84,-0.32);
\draw[cell frame] (0.00,-0.96) rectangle (0.32,-0.64);
\draw[cell frame] (0.32,-0.96) rectangle (0.64,-0.64);
\draw[cell frame] (0.64,-0.96) rectangle (0.96,-0.64);
\draw[cell frame] (0.96,-0.96) rectangle (1.28,-0.64);
\draw[cell frame] (1.28,-0.96) rectangle (1.60,-0.64);
\draw[cell frame] (1.60,-0.96) rectangle (1.92,-0.64);
\draw[cell frame] (1.92,-0.96) rectangle (2.24,-0.64);
\draw[cell frame] (2.24,-0.96) rectangle (2.56,-0.64);
\draw[cell frame] (2.56,-0.96) rectangle (2.88,-0.64);
\draw[cell frame] (2.88,-0.96) rectangle (3.20,-0.64);
\draw[cell frame] (3.20,-0.96) rectangle (3.52,-0.64);
\draw[cell frame] (3.52,-0.96) rectangle (3.84,-0.64);
\draw[cell frame] (0.00,-1.28) rectangle (0.32,-0.96);
\draw[cell frame] (0.32,-1.28) rectangle (0.64,-0.96);
\draw[cell frame] (0.64,-1.28) rectangle (0.96,-0.96);
\draw[cell frame] (0.96,-1.28) rectangle (1.28,-0.96);
\draw[cell frame] (1.28,-1.28) rectangle (1.60,-0.96);
\draw[cell frame] (1.60,-1.28) rectangle (1.92,-0.96);
\draw[cell frame] (1.92,-1.28) rectangle (2.24,-0.96);
\draw[cell frame] (2.24,-1.28) rectangle (2.56,-0.96);
\draw[cell frame] (2.56,-1.28) rectangle (2.88,-0.96);
\draw[cell frame] (2.88,-1.28) rectangle (3.20,-0.96);
\draw[cell frame] (3.20,-1.28) rectangle (3.52,-0.96);
\draw[cell frame] (3.52,-1.28) rectangle (3.84,-0.96);
\draw[cell frame] (0.00,-1.60) rectangle (0.32,-1.28);
\draw[cell frame] (0.32,-1.60) rectangle (0.64,-1.28);
\draw[cell frame] (0.64,-1.60) rectangle (0.96,-1.28);
\draw[cell frame] (0.96,-1.60) rectangle (1.28,-1.28);
\draw[cell frame] (1.28,-1.60) rectangle (1.60,-1.28);
\draw[cell frame] (1.60,-1.60) rectangle (1.92,-1.28);
\draw[cell frame] (1.92,-1.60) rectangle (2.24,-1.28);
\draw[cell frame] (2.24,-1.60) rectangle (2.56,-1.28);
\draw[cell frame] (2.56,-1.60) rectangle (2.88,-1.28);
\draw[cell frame] (2.88,-1.60) rectangle (3.20,-1.28);
\draw[cell frame] (3.20,-1.60) rectangle (3.52,-1.28);
\draw[cell frame] (3.52,-1.60) rectangle (3.84,-1.28);
\draw[cell frame] (0.00,-1.92) rectangle (0.32,-1.60);
\draw[cell frame] (0.32,-1.92) rectangle (0.64,-1.60);
\draw[cell frame] (0.64,-1.92) rectangle (0.96,-1.60);
\draw[cell frame] (0.96,-1.92) rectangle (1.28,-1.60);
\draw[cell frame] (1.28,-1.92) rectangle (1.60,-1.60);
\draw[cell frame] (1.60,-1.92) rectangle (1.92,-1.60);
\draw[cell frame] (1.92,-1.92) rectangle (2.24,-1.60);
\draw[cell frame] (2.24,-1.92) rectangle (2.56,-1.60);
\draw[cell frame] (2.56,-1.92) rectangle (2.88,-1.60);
\draw[cell frame] (2.88,-1.92) rectangle (3.20,-1.60);
\draw[cell frame] (3.20,-1.92) rectangle (3.52,-1.60);
\draw[cell frame] (3.52,-1.92) rectangle (3.84,-1.60);
\draw[cell frame] (0.00,-2.24) rectangle (0.32,-1.92);
\draw[cell frame] (0.32,-2.24) rectangle (0.64,-1.92);
\draw[cell frame] (0.64,-2.24) rectangle (0.96,-1.92);
\draw[cell frame] (0.96,-2.24) rectangle (1.28,-1.92);
\draw[cell frame] (1.28,-2.24) rectangle (1.60,-1.92);
\draw[cell frame] (1.60,-2.24) rectangle (1.92,-1.92);
\draw[cell frame] (1.92,-2.24) rectangle (2.24,-1.92);
\draw[cell frame] (2.24,-2.24) rectangle (2.56,-1.92);
\draw[cell frame] (2.56,-2.24) rectangle (2.88,-1.92);
\draw[cell frame] (2.88,-2.24) rectangle (3.20,-1.92);
\draw[cell frame] (3.20,-2.24) rectangle (3.52,-1.92);
\draw[cell frame] (3.52,-2.24) rectangle (3.84,-1.92);
\draw[emph] (0.00,0.32) rectangle (1.28,-0.96);
\node[lab] at (0.64,-0.32) {$0$};
\draw[emph] (1.28,0.32) rectangle (2.56,-0.96);
\node[lab] at (1.92,-0.32) {$1$};
\draw[emph] (2.56,0.32) rectangle (3.84,-0.96);
\node[lab] at (3.20,-0.32) {$2$};
\draw[emph] (0.00,-0.96) rectangle (1.28,-2.24);
\node[lab] at (0.64,-1.60) {$3$};
\draw[hl] (1.28,-0.96) rectangle (2.56,-2.24);
\node[lab] at (1.92,-1.60) {$4$};
\draw[emph] (2.56,-0.96) rectangle (3.84,-2.24);
\node[lab] at (3.20,-1.60) {$5$};
\draw[cell frame] (4.80,-0.9) rectangle (5.25,-0.45);
\node[lab,tick] at (5.025,-0.675) {$0$};
\draw[cell frame] (5.25,-0.9) rectangle (5.70,-0.45);
\node[lab,tick] at (5.475,-0.675) {$1$};
\draw[cell frame] (5.70,-0.9) rectangle (6.15,-0.45);
\node[lab,tick] at (5.925,-0.675) {$2$};
\draw[cell frame] (6.15,-0.9) rectangle (6.60,-0.45);
\node[lab,tick] at (6.375,-0.675) {$3$};
\draw[hl cell] (6.60,-0.9) rectangle (7.05,-0.45);
\node[lab,tick] at (6.825,-0.675) {$4$};
\draw[cell frame] (7.05,-0.9) rectangle (7.50,-0.45);
\node[lab,tick] at (7.275,-0.675) {$5$};
\draw[->] (3.95,-0.65) -- (4.7,-0.65);
\node[lab] at (6.15,-0.2) {$N=6$ tokens};
\end{tikzpicture}
\end{center}
```

Patch embedding of an $8\times12$ image with $P=4$: six patches, numbered row by row, become a sequence of six tokens, each the flattened patch ($CP^2$ numbers) mapped linearly to $\mathbb{R}^d$.

:::

::: {#def-vision-transformer .definition name="Vision transformer"}

A *vision transformer* for $K$ classes embeds the $N$ patches (@def-patch-embedding), adds positional encodings (learnt, or sinusoidal as in @def-sinusoidal-positional-encoding), applies $L$ transformer blocks without a mask, pools the $N$ output vectors into one, and maps it to $K$ scores by a linear layer. The pooling is either the average of the $N$ vectors or the output at an extra learnt *class token* prepended to the sequence.

:::

::: {#prp-vit-attention-cost .proposition name="Cost of attention in a vision transformer"}

With $N=HW/P^2$ tokens of width $d$, the attention scores and the weighted sums of one layer (ignoring the query, key, value and output projections) cost $\Theta(N^2d)$ operations, and a model with $L$ layers $\Theta(LN^2d)$. Hence, other things fixed, doubling $d$ doubles the cost; doubling both $H$ and $W$ multiplies $N$ by $4$ and the cost by $16$; doubling $P$ divides $N$ by $4$ and the cost by $16$; doubling $L$ doubles the cost.

:::

::: {.proof}

1. The score matrix $QK^{\mathsf T}$ has $N^2$ entries, each an inner product of length $d/h$ in each of $h$ heads: $N^2d$ multiplications in all. The products of the $N\times N$ weight matrices with the values cost the same.
2. Layers are independent, so the total is $L$ times one layer.
3. $N=HW/P^2$ is multiplied by $4$ when $H$ and $W$ double, and by $1/4$ when $P$ doubles; $N^2$ changes by the square of that factor.

:::

For a $224\times224$ image and $P=16$, $N=196$; for a $32\times32$ CIFAR-10 image and $P=4$, $N=64$. The projections cost $\Theta(Nd^2)$ per layer, so at moderate $N$ they, not the attention, dominate.

::: {#rmk-vit-inductive-bias .remark name="Why ViTs need more data than CNNs"}

A convolutional network builds in two assumptions about images: locality (each unit sees a small window) and translation equivariance (the same filter everywhere). A ViT builds in neither beyond the patch grid: every token attends to every other from the first layer, and the positional encodings carry the only spatial information. On a large dataset this flexibility pays off and ViTs scale better; on a small one they overfit and lag behind CNNs. Remedies are pretraining on a large dataset (supervised or self-supervised, @sec-ai-unsupervised-learning-contrastive-learning) and fine-tuning, strong data augmentation and regularization, distillation from a CNN teacher, and hybrid designs that add convolutions or local attention.

:::
