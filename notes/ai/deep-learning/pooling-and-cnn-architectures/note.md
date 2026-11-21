---
title: "Pooling and Convolutional Network Architectures"
sources: [cs231n-9, cs231na-2]
requires: [ai/deep-learning/convolutional-layers, ai/deep-learning/batch-normalization]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Convolutional neural networks: pooling layer, layer patterns, layer sizing patterns, case studies, VGGNet in detail, computational considerations) and Assignment 2 (max pooling, three-layer convolutional network), in our own wording; the VGG totals and the example were computed in Python (our activation count differs from the one printed in the course notes); proofs written out in steps. -->

A convolutional network alternates convolutional layers (@def-convolutional-layer), activations and *pooling* layers, which shrink the spatial size, and ends with one or more fully connected layers that produce the class scores.

::: {#def-max-pooling .definition name="Max pooling"}

A *max pooling* layer with window $F$ and stride $S$ maps each channel of an input $C\times H\times W$ separately to

$$
Y_{c,i,j}=\max_{0\le u,v<F}X_{c,\,iS+u,\,jS+v},
$$

of shape $C\times H'\times W'$ with $H'=(H-F)/S+1$ and $W'=(W-F)/S+1$. It has no parameters. *Average pooling* takes the mean instead of the maximum; *global average pooling* averages each channel over all positions, giving a vector of length $C$.

:::

The usual setting is $F=S=2$, which halves height and width and discards $75\%$ of the activations; $F=3$, $S=2$ (overlapping pooling) is also seen. Larger windows lose too much information.

::: {#exm-max-pooling-1 .example name="Pooling a four-by-four map"}

With $F=S=2$, the map with rows $(1,3,2,1)$, $(4,6,5,0)$, $(3,1,1,2)$, $(0,2,4,3)$ is cut into four $2\times2$ blocks with maxima $6,5,3,4$, so the output has rows $(6,5)$ and $(3,4)$.

:::

::: {#fig-pooling-and-cnn-architectures-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[cell frame] (0.0,0.0) rectangle (0.5,0.5);
\node[lab] at (0.25,0.25) {$1$};
\draw[cell frame] (0.5,0.0) rectangle (1.0,0.5);
\node[lab] at (0.75,0.25) {$3$};
\draw[cell frame] (1.0,0.0) rectangle (1.5,0.5);
\node[lab] at (1.25,0.25) {$2$};
\draw[cell frame] (1.5,0.0) rectangle (2.0,0.5);
\node[lab] at (1.75,0.25) {$1$};
\draw[cell frame] (0.0,-0.5) rectangle (0.5,0.0);
\node[lab] at (0.25,-0.25) {$4$};
\draw[hl cell] (0.5,-0.5) rectangle (1.0,0.0);
\node[lab] at (0.75,-0.25) {$6$};
\draw[hl cell] (1.0,-0.5) rectangle (1.5,0.0);
\node[lab] at (1.25,-0.25) {$5$};
\draw[cell frame] (1.5,-0.5) rectangle (2.0,0.0);
\node[lab] at (1.75,-0.25) {$0$};
\draw[hl cell] (0.0,-1.0) rectangle (0.5,-0.5);
\node[lab] at (0.25,-0.75) {$3$};
\draw[cell frame] (0.5,-1.0) rectangle (1.0,-0.5);
\node[lab] at (0.75,-0.75) {$1$};
\draw[cell frame] (1.0,-1.0) rectangle (1.5,-0.5);
\node[lab] at (1.25,-0.75) {$1$};
\draw[cell frame] (1.5,-1.0) rectangle (2.0,-0.5);
\node[lab] at (1.75,-0.75) {$2$};
\draw[cell frame] (0.0,-1.5) rectangle (0.5,-1.0);
\node[lab] at (0.25,-1.25) {$0$};
\draw[cell frame] (0.5,-1.5) rectangle (1.0,-1.0);
\node[lab] at (0.75,-1.25) {$2$};
\draw[hl cell] (1.0,-1.5) rectangle (1.5,-1.0);
\node[lab] at (1.25,-1.25) {$4$};
\draw[cell frame] (1.5,-1.5) rectangle (2.0,-1.0);
\node[lab] at (1.75,-1.25) {$3$};
\draw[emph] (1,0.5) -- (1,-1.5); \draw[emph] (0,-0.5) -- (2,-0.5);
\draw[cell frame] (3.0,-0.5) rectangle (3.5,0.0);
\node[lab] at (3.25,-0.25) {$6$};
\draw[cell frame] (3.5,-0.5) rectangle (4.0,0.0);
\node[lab] at (3.75,-0.25) {$5$};
\draw[cell frame] (3.0,-1.0) rectangle (3.5,-0.5);
\node[lab] at (3.25,-0.75) {$3$};
\draw[cell frame] (3.5,-1.0) rectangle (4.0,-0.5);
\node[lab] at (3.75,-0.75) {$4$};
\draw[->] (2.2,-0.5) -- (2.85,-0.5);
\end{tikzpicture}
\end{center}
```

Max pooling with $F=S=2$ on the map of @exm-max-pooling-1. The highlighted maxima are the only entries that receive gradient in the backward pass (@prp-max-pooling-backward).

:::

::: {#prp-max-pooling-backward .proposition name="Backward pass of max pooling"}

If each window has a unique maximum, then $\partial L/\partial X_{c,p,q}=\sum\partial L/\partial Y_{c,i,j}$ over the windows $(i,j)$ whose maximum is at $(p,q)$, and $0$ if $(p,q)$ is the maximum of no window.

:::

::: {.proof}

1. Near a point where each window's maximum is unique, $Y_{c,i,j}$ equals the input entry at the maximizing position and does not depend on the others; so its derivative is $1$ with respect to that entry and $0$ for the rest (the max node of @sec-ai-deep-learning-backpropagation).
2. Summing over all windows that contain $(p,q)$ (only one when $S=F$) gives the formula.

:::

The forward pass therefore records the position of each maximum (the *switches*) for use in the backward pass.

::: {#prp-stacked-receptive-field .proposition name="Stacking small filters"}

A stack of $L$ convolutional layers with filter size $F$ and stride $1$ gives each output unit a receptive field of size $1+L(F-1)$ in the input. With $C$ channels throughout, three $3\times3$ layers have the receptive field $7\times7$ of one $7\times7$ layer, with $27C^2$ instead of $49C^2$ weights.

:::

::: {.proof}

1. Induction on $L$. One layer sees $F=1+(F-1)$ positions in each direction.
2. If a unit of layer $L-1$ sees $r$ consecutive input positions, a unit of layer $L$ combines $F$ consecutive units of layer $L-1$, whose fields are shifted by $1$ each, so it sees $r+F-1$ positions.
3. With $F=3$, $L=3$: $1+3\cdot2=7$. The weights are $3\cdot(3\cdot3\cdot C\cdot C)=27C^2$ against $7\cdot7\cdot C\cdot C=49C^2$.

:::

::: {#fig-pooling-and-cnn-architectures-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[dot] (n00) at (0.0,0.0) {};
\node[hl dot] (n01) at (0.6,0.0) {};
\node[hl dot] (n02) at (1.2,0.0) {};
\node[hl dot] (n03) at (1.80,0.0) {};
\node[hl dot] (n04) at (2.4,0.0) {};
\node[hl dot] (n05) at (3.0,0.0) {};
\node[hl dot] (n06) at (3.60,0.0) {};
\node[hl dot] (n07) at (4.2,0.0) {};
\node[dot] (n08) at (4.8,0.0) {};
\node[tick, left] at (-0.3,0.0) {input};
\node[dot] (n10) at (0.0,1.0) {};
\node[dot] (n11) at (0.6,1.0) {};
\node[hl dot] (n12) at (1.2,1.0) {};
\node[hl dot] (n13) at (1.80,1.0) {};
\node[hl dot] (n14) at (2.4,1.0) {};
\node[hl dot] (n15) at (3.0,1.0) {};
\node[hl dot] (n16) at (3.60,1.0) {};
\node[dot] (n17) at (4.2,1.0) {};
\node[dot] (n18) at (4.8,1.0) {};
\node[tick, left] at (-0.3,1.0) {layer 1};
\node[dot] (n20) at (0.0,2.0) {};
\node[dot] (n21) at (0.6,2.0) {};
\node[dot] (n22) at (1.2,2.0) {};
\node[hl dot] (n23) at (1.80,2.0) {};
\node[hl dot] (n24) at (2.4,2.0) {};
\node[hl dot] (n25) at (3.0,2.0) {};
\node[dot] (n26) at (3.60,2.0) {};
\node[dot] (n27) at (4.2,2.0) {};
\node[dot] (n28) at (4.8,2.0) {};
\node[tick, left] at (-0.3,2.0) {layer 2};
\node[dot] (n30) at (0.0,3.0) {};
\node[dot] (n31) at (0.6,3.0) {};
\node[dot] (n32) at (1.2,3.0) {};
\node[dot] (n33) at (1.80,3.0) {};
\node[hl dot] (n34) at (2.4,3.0) {};
\node[dot] (n35) at (3.0,3.0) {};
\node[dot] (n36) at (3.60,3.0) {};
\node[dot] (n37) at (4.2,3.0) {};
\node[dot] (n38) at (4.8,3.0) {};
\node[tick, left] at (-0.3,3.0) {layer 3};
\draw[faint] (n12) -- (n01);
\draw[faint] (n12) -- (n02);
\draw[faint] (n12) -- (n03);
\draw[faint] (n13) -- (n02);
\draw[faint] (n13) -- (n03);
\draw[faint] (n13) -- (n04);
\draw[faint] (n14) -- (n03);
\draw[faint] (n14) -- (n04);
\draw[faint] (n14) -- (n05);
\draw[faint] (n15) -- (n04);
\draw[faint] (n15) -- (n05);
\draw[faint] (n15) -- (n06);
\draw[faint] (n16) -- (n05);
\draw[faint] (n16) -- (n06);
\draw[faint] (n16) -- (n07);
\draw[faint] (n23) -- (n12);
\draw[faint] (n23) -- (n13);
\draw[faint] (n23) -- (n14);
\draw[faint] (n24) -- (n13);
\draw[faint] (n24) -- (n14);
\draw[faint] (n24) -- (n15);
\draw[faint] (n25) -- (n14);
\draw[faint] (n25) -- (n15);
\draw[faint] (n25) -- (n16);
\draw[faint] (n34) -- (n23);
\draw[faint] (n34) -- (n24);
\draw[faint] (n34) -- (n25);
\end{tikzpicture}
\end{center}
```

Three stacked $3$-wide convolutions: one unit of layer $3$ sees $7$ inputs (highlighted), the same receptive field as a single $7$-wide filter but with fewer parameters and more non-linearity

:::

The stack also puts two more non-linearities between input and output, so it is more expressive as well as cheaper.

::: {#rmk-cnn-layer-patterns .remark name="Layer patterns"}

The classical pattern is

$$
\text{INPUT}\to\bigl[(\text{CONV}\to\text{RELU})\times N\to\text{POOL}\bigr]\times M\to(\text{FC}\to\text{RELU})\times K\to\text{FC},
$$

with $N\le3$, $K<3$, and batch normalization (@def-batch-normalization) after each convolution. Convolutions use $3\times3$ filters, stride $1$ and same padding, so only the pooling layers change the spatial size; input sizes divisible by $2$ many times ($32$, $64$, $224$) avoid fractional sizes. Newer architectures depart from a plain chain: GoogLeNet's modules run several filter sizes in parallel, and residual networks (ResNet) add the skip connections of @def-residual-connection around pairs of convolutional layers and replace the large fully connected layers by global average pooling, which made networks of over $100$ layers trainable. In practice one reuses an architecture that works well on ImageNet, often with pretrained weights (@sec-ai-deep-learning-transfer-learning).

:::

::: {#fig-pooling-and-cnn-architectures-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (b0) at (0.0,0) {input};
\node[box] (b1) at (1.6,0) {conv};
\draw[map] (b0) -- (b1);
\node[box] (b2) at (3.2,0) {ReLU};
\draw[map] (b1) -- (b2);
\node[box] (b3) at (4.80,0) {conv};
\draw[map] (b2) -- (b3);
\node[box] (b4) at (6.4,0) {ReLU};
\draw[map] (b3) -- (b4);
\node[hl box] (b5) at (8.0,0) {pool};
\draw[map] (b4) -- (b5);
\node[hl box] (b6) at (9.60,0) {FC};
\draw[map] (b5) -- (b6);
\draw[faint, dashed] (0.85,-0.55) rectangle (8.6,0.55);
\node[tick, above] at (4.7,0.55) {repeat};
\end{tikzpicture}
\end{center}
```

The common pattern: blocks of convolutions with ReLU followed by pooling, repeated, then fully connected layers at the end

:::

::: {#exm-vgg-sizes .example name="The size of VGG-16"}

VGG-16 takes a $3\times224\times224$ image through thirteen $3\times3$ convolutional layers (same padding) with $64,64,128,128,256,256,256,512,\dots,512$ channels, a $2\times2$ max pooling after layers $2,4,7,10,13$, and fully connected layers of $4096$, $4096$ and $1000$ units. Counting, it has about $138$ million parameters, of which about $103$ million are in the first fully connected layer ($7\cdot7\cdot512\cdot4096$ weights). The forward pass stores about $15.2$ million activations, about $61$ MB per image in 32-bit floats and about twice that with the gradients of the backward pass; most of them sit in the first two convolutional layers ($2\cdot64\cdot224\cdot224\approx6.4$ million).

:::

::: {#rmk-cnn-memory .remark name="Memory"}

Training memory has three parts: the activations (and their gradients) of every layer, kept for the backward pass, which dominate and scale with the batch size; the parameters, their gradients and the optimizer's state (Adam keeps two more copies, @def-adam); and miscellaneous buffers such as the im2col matrices of @prp-im2col. When a model does not fit, the batch size is the first thing to reduce.

:::
