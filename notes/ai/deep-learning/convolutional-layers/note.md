---
title: "Convolutional Layers"
sources: [cs231n-9, cs231na-2]
requires: [ai/deep-learning/neural-networks]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Convolutional neural networks: convolutional layer, local connectivity, spatial arrangement, parameter sharing, im2col, backpropagation, dilated convolutions, converting fully connected layers) and Assignment 2 (convolutional networks), in our own wording; the sizes were computed in Python; the propositions on im2col and the backward pass are written out as our own proofs. -->

A fully connected layer on a $224\times224\times3$ image would give every hidden unit $150{,}528$ weights. Images have local structure, and the same pattern (an edge, a texture) can appear anywhere. A *convolutional layer* uses both facts: each output unit looks at a small window of the input (*local connectivity*), and all units of one output channel use the same weights (*parameter sharing*).

::: {#def-convolutional-layer .definition name="Convolutional layer"}

The input is a tensor $X$ of shape $C\times H\times W$ (channels, height, width). A *convolutional layer* with $K$ *filters* $W^{(k)}$ of shape $C\times F\times F$, biases $b_k$, *stride* $S$ and *zero-padding* $P$ first pads $X$ with $P$ rows and columns of zeros on every side, then outputs the tensor $Y$ of shape $K\times H'\times W'$ with

$$
Y_{k,i,j}=b_k+\sum_{c=1}^{C}\sum_{u=0}^{F-1}\sum_{v=0}^{F-1}W^{(k)}_{c,u,v}\,X^{\text{pad}}_{c,\,iS+u,\,jS+v},\qquad 0\le i<H',\ 0\le j<W'.
$$

Each output channel $Y_{k,:,:}$ is an *activation map*; the $F\times F$ window of an output unit is its *receptive field* in the layer's input.

:::

Strictly this is a cross-correlation; a convolution would flip the filter. The name is universal in deep learning and the difference is immaterial, since the filters are learnt.

::: {#prp-conv-output-size .proposition name="Output size and parameter count"}

The output of @def-convolutional-layer has

$$
H'=\frac{H-F+2P}{S}+1,\qquad W'=\frac{W-F+2P}{S}+1,
$$

provided these are integers (otherwise the windows do not tile the padded input). The layer has $K(CF^2+1)$ parameters, independent of $H$ and $W$; it has $KH'W'$ output units, each with $CF^2$ weights.

:::

::: {.proof}

1. The padded input has width $W+2P$. The window of output column $j$ covers input columns $jS,\dots,jS+F-1$, so $j$ is allowed when $jS+F-1\le W+2P-1$, that is $j\le(W-F+2P)/S$.
2. Counting $j=0,1,\dots,(W-F+2P)/S$ gives $W'$; the same argument gives $H'$.
3. Each of the $K$ filters has $CF^2$ weights and one bias, shared by all $H'W'$ positions of its activation map.

:::

::: {#exm-conv-sizes .example name="Sizes of a first layer"}

An input of $3\times227\times227$ with $K=96$ filters of size $F=11$, stride $S=4$ and no padding gives $H'=W'=(227-11)/4+1=55$, so $96\cdot55\cdot55=290{,}400$ output units, each with $11\cdot11\cdot3=363$ weights. Without sharing that would be about $105$ million weights; with sharing the layer has $96\cdot(363+1)=34{,}944$ parameters. With $F=3$, $S=1$ and $P=1$, instead, $H'=H$: this *same* padding keeps the spatial size, and is the usual choice.

:::

::: {#fig-convolutional-layers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[faint] (0.0,0.0) rectangle (0.5,0.5);
\node[lab,tick] at (0.25,0.25) {$0$};
\draw[faint] (0.5,0.0) rectangle (1.0,0.5);
\node[lab,tick] at (0.75,0.25) {$0$};
\draw[faint] (1.0,0.0) rectangle (1.5,0.5);
\node[lab,tick] at (1.25,0.25) {$0$};
\draw[faint] (1.5,0.0) rectangle (2.0,0.5);
\node[lab,tick] at (1.75,0.25) {$0$};
\draw[faint] (2.0,0.0) rectangle (2.5,0.5);
\node[lab,tick] at (2.25,0.25) {$0$};
\draw[faint] (2.5,0.0) rectangle (3.0,0.5);
\node[lab,tick] at (2.75,0.25) {$0$};
\draw[faint] (3.0,0.0) rectangle (3.5,0.5);
\node[lab,tick] at (3.25,0.25) {$0$};
\draw[faint] (0.0,-0.5) rectangle (0.5,0.0);
\node[lab,tick] at (0.25,-0.25) {$0$};
\draw[cell frame] (0.5,-0.5) rectangle (1.0,0.0);
\draw[cell frame] (1.0,-0.5) rectangle (1.5,0.0);
\draw[cell frame] (1.5,-0.5) rectangle (2.0,0.0);
\draw[cell frame] (2.0,-0.5) rectangle (2.5,0.0);
\draw[cell frame] (2.5,-0.5) rectangle (3.0,0.0);
\draw[faint] (3.0,-0.5) rectangle (3.5,0.0);
\node[lab,tick] at (3.25,-0.25) {$0$};
\draw[faint] (0.0,-1.0) rectangle (0.5,-0.5);
\node[lab,tick] at (0.25,-0.75) {$0$};
\draw[cell frame] (0.5,-1.0) rectangle (1.0,-0.5);
\draw[hl cell] (1.0,-1.0) rectangle (1.5,-0.5);
\draw[hl cell] (1.5,-1.0) rectangle (2.0,-0.5);
\draw[hl cell] (2.0,-1.0) rectangle (2.5,-0.5);
\draw[cell frame] (2.5,-1.0) rectangle (3.0,-0.5);
\draw[faint] (3.0,-1.0) rectangle (3.5,-0.5);
\node[lab,tick] at (3.25,-0.75) {$0$};
\draw[faint] (0.0,-1.5) rectangle (0.5,-1.0);
\node[lab,tick] at (0.25,-1.25) {$0$};
\draw[cell frame] (0.5,-1.5) rectangle (1.0,-1.0);
\draw[hl cell] (1.0,-1.5) rectangle (1.5,-1.0);
\draw[hl cell] (1.5,-1.5) rectangle (2.0,-1.0);
\draw[hl cell] (2.0,-1.5) rectangle (2.5,-1.0);
\draw[cell frame] (2.5,-1.5) rectangle (3.0,-1.0);
\draw[faint] (3.0,-1.5) rectangle (3.5,-1.0);
\node[lab,tick] at (3.25,-1.25) {$0$};
\draw[faint] (0.0,-2.0) rectangle (0.5,-1.5);
\node[lab,tick] at (0.25,-1.75) {$0$};
\draw[cell frame] (0.5,-2.0) rectangle (1.0,-1.5);
\draw[hl cell] (1.0,-2.0) rectangle (1.5,-1.5);
\draw[hl cell] (1.5,-2.0) rectangle (2.0,-1.5);
\draw[hl cell] (2.0,-2.0) rectangle (2.5,-1.5);
\draw[cell frame] (2.5,-2.0) rectangle (3.0,-1.5);
\draw[faint] (3.0,-2.0) rectangle (3.5,-1.5);
\node[lab,tick] at (3.25,-1.75) {$0$};
\draw[faint] (0.0,-2.5) rectangle (0.5,-2.0);
\node[lab,tick] at (0.25,-2.25) {$0$};
\draw[cell frame] (0.5,-2.5) rectangle (1.0,-2.0);
\draw[cell frame] (1.0,-2.5) rectangle (1.5,-2.0);
\draw[cell frame] (1.5,-2.5) rectangle (2.0,-2.0);
\draw[cell frame] (2.0,-2.5) rectangle (2.5,-2.0);
\draw[cell frame] (2.5,-2.5) rectangle (3.0,-2.0);
\draw[faint] (3.0,-2.5) rectangle (3.5,-2.0);
\node[lab,tick] at (3.25,-2.25) {$0$};
\draw[faint] (0.0,-3.0) rectangle (0.5,-2.5);
\node[lab,tick] at (0.25,-2.75) {$0$};
\draw[faint] (0.5,-3.0) rectangle (1.0,-2.5);
\node[lab,tick] at (0.75,-2.75) {$0$};
\draw[faint] (1.0,-3.0) rectangle (1.5,-2.5);
\node[lab,tick] at (1.25,-2.75) {$0$};
\draw[faint] (1.5,-3.0) rectangle (2.0,-2.5);
\node[lab,tick] at (1.75,-2.75) {$0$};
\draw[faint] (2.0,-3.0) rectangle (2.5,-2.5);
\node[lab,tick] at (2.25,-2.75) {$0$};
\draw[faint] (2.5,-3.0) rectangle (3.0,-2.5);
\node[lab,tick] at (2.75,-2.75) {$0$};
\draw[faint] (3.0,-3.0) rectangle (3.5,-2.5);
\node[lab,tick] at (3.25,-2.75) {$0$};
\draw[cell frame] (5.0,-1.0) rectangle (5.5,-0.5);
\draw[cell frame] (5.5,-1.0) rectangle (6.0,-0.5);
\draw[cell frame] (6.0,-1.0) rectangle (6.5,-0.5);
\draw[cell frame] (5.0,-1.5) rectangle (5.5,-1.0);
\draw[hl cell] (5.5,-1.5) rectangle (6.0,-1.0);
\draw[cell frame] (6.0,-1.5) rectangle (6.5,-1.0);
\draw[cell frame] (5.0,-2.0) rectangle (5.5,-1.5);
\draw[cell frame] (5.5,-2.0) rectangle (6.0,-1.5);
\draw[cell frame] (6.0,-2.0) rectangle (6.5,-1.5);
\draw[->] (2.6,-0.75) -- (4.9,-1.25);
\node[lab] at (1.75,0.85) {padded input $7\times7$};
\node[lab] at (5.75,0.35) {output $3\times3$};
\end{tikzpicture}
\end{center}
```

A $5\times5$ input with one row and column of zero padding ($P=1$), filter size $F=3$ and stride $S=2$: the highlighted window produces the centre output unit, and the output has size $(5-3+2)/2+1=3$.

:::

::: {#prp-im2col .proposition name="Convolution as one matrix product"}

Let $X_{\text{col}}$ be the matrix of shape $CF^2\times H'W'$ whose column for output position $(i,j)$ lists the entries of the padded input in the window of $(i,j)$, and let $W_{\text{row}}$ be the matrix of shape $K\times CF^2$ whose row $k$ lists the entries of $W^{(k)}$ in the same order. Then $W_{\text{row}}X_{\text{col}}+\mathbf{b}\mathbf{1}^{\mathsf T}$, reshaped to $K\times H'\times W'$, is $Y$.

:::

::: {.proof}

1. Entry $(k,(i,j))$ of $W_{\text{row}}X_{\text{col}}$ is the inner product of row $k$ with column $(i,j)$, that is $\sum_{c,u,v}W^{(k)}_{c,u,v}X^{\text{pad}}_{c,iS+u,jS+v}$, because both list their entries in the same order of $(c,u,v)$.
2. Adding $b_k$ gives $Y_{k,i,j}$ of @def-convolutional-layer.

:::

This *im2col* form runs a convolution as one large, highly optimized matrix product, at the price of memory: overlapping windows copy each input entry up to $F^2/S^2$ times.

::: {#prp-conv-backward .proposition name="Backward pass of a convolutional layer"}

Let $G=\partial L/\partial Y$, reshaped to $G_{\text{row}}$ of shape $K\times H'W'$. Then

$$
\frac{\partial L}{\partial W_{\text{row}}}=G_{\text{row}}X_{\text{col}}^{\mathsf T},\qquad \frac{\partial L}{\partial b_k}=\sum_{i,j}G_{k,i,j},\qquad \frac{\partial L}{\partial X_{\text{col}}}=W_{\text{row}}^{\mathsf T}G_{\text{row}},
$$

and $\partial L/\partial X^{\text{pad}}$ is obtained by adding each entry of $\partial L/\partial X_{\text{col}}$ to the input position it was copied from. In one dimension with one channel, stride $1$ and no padding, $y_i=\sum_uw_ux_{i+u}$ gives $\partial L/\partial x_m=\sum_ug_{m-u}w_u$ (terms with $m-u$ out of range omitted): a full convolution of $\mathbf{g}$ with the flipped filter.

:::

::: {.proof}

1. By @prp-im2col, $Y_{\text{row}}=W_{\text{row}}X_{\text{col}}+\mathbf{b}\mathbf{1}^{\mathsf T}$; @prp-matrix-product-gradient gives the gradients with respect to $W_{\text{row}}$ and $X_{\text{col}}$, and each $b_k$ is added to every entry of row $k$.
2. Each entry of $X_{\text{col}}$ is a copy of one entry of $X^{\text{pad}}$, and an entry of $X^{\text{pad}}$ used in several columns receives the sum of their gradients (gradients add at forks, @sec-ai-deep-learning-backpropagation).
3. In the one-dimensional case, $x_m$ appears in $y_i$ exactly when $i+u=m$, with coefficient $w_u$, so $\partial L/\partial x_m=\sum_ug_{m-u}w_u$.

:::

So the backward pass of a convolution is again a convolution, and costs about as much as the forward pass.

::: {#rmk-conv-variants .remark name="One-by-one and dilated convolutions"}

1. A $1\times1$ convolution ($F=1$) applies the same fully connected map to the $C$ channels at every position; it changes the number of channels cheaply.
2. A *dilated* convolution with dilation $d$ spaces the filter taps $d$ apart, using $X^{\text{pad}}_{c,iS+du,jS+dv}$: a $3\times3$ filter with $d=2$ covers a $5\times5$ window with $9$ weights, so receptive fields grow quickly with depth.
3. A fully connected layer on an input of shape $C\times H\times W$ is a convolutional layer with $F=H=W$ (one output position per filter). Converting a classifier's fully connected layers this way lets the network slide over a larger image in one pass, sharing the computation of overlapping windows.

:::
