---
title: "Visualizing What Convolutional Networks Learn"
sources: [cs231n-10]
requires: [ai/deep-learning/pooling-and-cnn-architectures]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Understanding and visualizing convolutional neural networks: activations and filters, maximally activating images, t-SNE embeddings, occlusion, data gradients, reconstruction from codes), in our own wording; the saliency proposition and its proof are our own. -->

A trained network is a function with millions of parameters; visualization methods ask which inputs it responds to and which parts of an input its decision depends on. Let $s_c(I)$ be the score of class $c$ for an image $I$, before the softmax.

::: {#rmk-network-visualization-filters .remark name="Filters, activations and maximally activating patches"}

1. *First-layer filters* act directly on pixels and can be shown as small images; in a well-trained network they are smooth oriented edges and colour blobs. Noisy filters indicate too little training or too little regularization.
2. *Activation maps* of later layers on a given image become sparser and more localized with depth; many all-zero maps may indicate dead units.
3. *Maximally activating patches*: run many images through the network and, for a chosen unit, keep the image regions (its receptive field, @def-convolutional-layer) with the largest activations. Units in higher layers respond to object parts, faces, text and the like.

:::

::: {#rmk-network-visualization-embedding .remark name="Embedding the codes"}

The activations of the last hidden layer (the *code* of an image, for example $4096$ numbers in VGG, @exm-vgg-sizes) can be embedded in the plane by t-SNE, a non-linear method that tries to keep nearby codes nearby. Images with similar codes then appear next to each other, and the picture shows that the code groups images by content rather than by colour or pixel layout, unlike the pixel distances of @sec-ai-machine-learning-nearest-neighbors.

:::

::: {#def-occlusion-sensitivity .definition name="Occlusion sensitivity"}

For an image $I$ with correct class $c$, *occlusion sensitivity* slides a grey square over $I$ and records, at each position of the square, the probability of class $c$ for the occluded image. Positions where the probability drops sharply are those the prediction depends on.

:::

::: {#fig-network-visualization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.00,0.00) rectangle (0.35,-0.35);
\draw[cell frame] (0.35,0.00) rectangle (0.70,-0.35);
\draw[cell frame] (0.70,0.00) rectangle (1.05,-0.35);
\draw[cell frame] (1.05,0.00) rectangle (1.40,-0.35);
\draw[cell frame] (1.40,0.00) rectangle (1.75,-0.35);
\draw[cell frame] (1.75,0.00) rectangle (2.10,-0.35);
\draw[cell frame] (2.10,0.00) rectangle (2.45,-0.35);
\draw[cell frame] (0.00,-0.35) rectangle (0.35,-0.70);
\draw[cell frame] (0.35,-0.35) rectangle (0.70,-0.70);
\draw[cell frame] (0.70,-0.35) rectangle (1.05,-0.70);
\draw[cell frame] (1.05,-0.35) rectangle (1.40,-0.70);
\draw[cell frame] (1.40,-0.35) rectangle (1.75,-0.70);
\draw[cell frame] (1.75,-0.35) rectangle (2.10,-0.70);
\draw[cell frame] (2.10,-0.35) rectangle (2.45,-0.70);
\draw[cell frame] (0.00,-0.70) rectangle (0.35,-1.05);
\draw[cell frame] (0.35,-0.70) rectangle (0.70,-1.05);
\draw[cell frame] (0.70,-0.70) rectangle (1.05,-1.05);
\draw[cell frame] (1.05,-0.70) rectangle (1.40,-1.05);
\draw[cell frame] (1.40,-0.70) rectangle (1.75,-1.05);
\draw[cell frame] (1.75,-0.70) rectangle (2.10,-1.05);
\draw[cell frame] (2.10,-0.70) rectangle (2.45,-1.05);
\draw[cell frame] (0.00,-1.05) rectangle (0.35,-1.40);
\draw[cell frame] (0.35,-1.05) rectangle (0.70,-1.40);
\draw[cell frame] (0.70,-1.05) rectangle (1.05,-1.40);
\draw[cell frame] (1.05,-1.05) rectangle (1.40,-1.40);
\draw[cell frame] (1.40,-1.05) rectangle (1.75,-1.40);
\draw[cell frame] (1.75,-1.05) rectangle (2.10,-1.40);
\draw[cell frame] (2.10,-1.05) rectangle (2.45,-1.40);
\draw[cell frame] (0.00,-1.40) rectangle (0.35,-1.75);
\draw[cell frame] (0.35,-1.40) rectangle (0.70,-1.75);
\draw[cell frame] (0.70,-1.40) rectangle (1.05,-1.75);
\draw[cell frame] (1.05,-1.40) rectangle (1.40,-1.75);
\draw[cell frame] (1.40,-1.40) rectangle (1.75,-1.75);
\draw[cell frame] (1.75,-1.40) rectangle (2.10,-1.75);
\draw[cell frame] (2.10,-1.40) rectangle (2.45,-1.75);
\draw[cell frame] (0.00,-1.75) rectangle (0.35,-2.10);
\draw[cell frame] (0.35,-1.75) rectangle (0.70,-2.10);
\draw[cell frame] (0.70,-1.75) rectangle (1.05,-2.10);
\draw[cell frame] (1.05,-1.75) rectangle (1.40,-2.10);
\draw[cell frame] (1.40,-1.75) rectangle (1.75,-2.10);
\draw[cell frame] (1.75,-1.75) rectangle (2.10,-2.10);
\draw[cell frame] (2.10,-1.75) rectangle (2.45,-2.10);
\draw[hl cell] (0.7,-0.7) rectangle (1.4,-1.4);
\node[tick, below] at (1.2,-2.15) {occluded image};
\draw[map] (2.65,-1.05) -- (3.35,-1.05);
\draw[cell frame] (3.60,-0.00) rectangle (3.95,-0.35);
\draw[cell frame] (3.95,-0.00) rectangle (4.30,-0.35);
\draw[cell frame] (4.30,-0.00) rectangle (4.65,-0.35);
\draw[cell frame] (4.65,-0.00) rectangle (5.00,-0.35);
\draw[cell frame] (5.00,-0.00) rectangle (5.35,-0.35);
\draw[cell frame] (5.35,-0.00) rectangle (5.70,-0.35);
\draw[cell frame] (5.70,-0.00) rectangle (6.05,-0.35);
\draw[cell frame] (3.60,-0.35) rectangle (3.95,-0.70);
\draw[cell frame] (3.95,-0.35) rectangle (4.30,-0.70);
\draw[shade] (4.30,-0.35) rectangle (4.65,-0.70);
\draw[hl cell] (4.65,-0.35) rectangle (5.00,-0.70);
\draw[shade] (5.00,-0.35) rectangle (5.35,-0.70);
\draw[cell frame] (5.35,-0.35) rectangle (5.70,-0.70);
\draw[cell frame] (5.70,-0.35) rectangle (6.05,-0.70);
\draw[cell frame] (3.60,-0.70) rectangle (3.95,-1.05);
\draw[shade] (3.95,-0.70) rectangle (4.30,-1.05);
\draw[hl cell] (4.30,-0.70) rectangle (4.65,-1.05);
\draw[hl cell] (4.65,-0.70) rectangle (5.00,-1.05);
\draw[hl cell] (5.00,-0.70) rectangle (5.35,-1.05);
\draw[cell frame] (5.35,-0.70) rectangle (5.70,-1.05);
\draw[cell frame] (5.70,-0.70) rectangle (6.05,-1.05);
\draw[cell frame] (3.60,-1.05) rectangle (3.95,-1.40);
\draw[shade] (3.95,-1.05) rectangle (4.30,-1.40);
\draw[hl cell] (4.30,-1.05) rectangle (4.65,-1.40);
\draw[hl cell] (4.65,-1.05) rectangle (5.00,-1.40);
\draw[hl cell] (5.00,-1.05) rectangle (5.35,-1.40);
\draw[cell frame] (5.35,-1.05) rectangle (5.70,-1.40);
\draw[cell frame] (5.70,-1.05) rectangle (6.05,-1.40);
\draw[cell frame] (3.60,-1.40) rectangle (3.95,-1.75);
\draw[cell frame] (3.95,-1.40) rectangle (4.30,-1.75);
\draw[shade] (4.30,-1.40) rectangle (4.65,-1.75);
\draw[hl cell] (4.65,-1.40) rectangle (5.00,-1.75);
\draw[shade] (5.00,-1.40) rectangle (5.35,-1.75);
\draw[cell frame] (5.35,-1.40) rectangle (5.70,-1.75);
\draw[cell frame] (5.70,-1.40) rectangle (6.05,-1.75);
\draw[cell frame] (3.60,-1.75) rectangle (3.95,-2.10);
\draw[cell frame] (3.95,-1.75) rectangle (4.30,-2.10);
\draw[cell frame] (4.30,-1.75) rectangle (4.65,-2.10);
\draw[cell frame] (4.65,-1.75) rectangle (5.00,-2.10);
\draw[cell frame] (5.00,-1.75) rectangle (5.35,-2.10);
\draw[cell frame] (5.35,-1.75) rectangle (5.70,-2.10);
\draw[cell frame] (5.70,-1.75) rectangle (6.05,-2.10);
\node[tick, below] at (4.8,-2.15) {drop in class score};
\end{tikzpicture}
\end{center}
```

Occlusion sensitivity: a grey patch slides over the image and the drop in the class score is recorded at each position. Large drops (highlighted) mark the regions the network relies on

:::

::: {#def-saliency-map .definition name="Saliency map"}

The *saliency map* of an image $I$ (shape $3\times H\times W$) for class $c$ is the $H\times W$ map

$$
M_{ij}=\max_{\text{channel }k}\ \Bigl\lvert\frac{\partial s_c}{\partial I_{k,i,j}}(I)\Bigr\rvert ,
$$

computed by one backward pass from $s_c$ to the input with the weights fixed.

:::

::: {#fig-network-visualization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (i) at (0,0) {image $I$};
\node[box] (n) at (3,0) {network};
\node[box] (s) at (5.6,0) {score $s_c(I)$};
\draw[map] (i) -- (n);
\draw[map] (n) -- (s);
\draw[map, hl] (s.south) to[bend left=30] node[edge label, text=accent] {$\partial s_c/\partial I$} (i.south);
\end{tikzpicture}
\end{center}
```

A saliency map backpropagates the class score to the pixels; the size of $\partial s_c/\partial I$ at each pixel shows how much a small change there would move the score

:::

::: {#prp-saliency-linear .proposition name="Saliency as a local linear model"}

If $s_c$ is differentiable at $I$, then $s_c(I+\Delta)=s_c(I)+\sum_{k,i,j}\frac{\partial s_c}{\partial I_{k,i,j}}\Delta_{k,i,j}+o(\lVert\Delta\rVert)$. For a linear model $s_c(I)=\mathbf{w}_c\cdot I+b_c$, the gradient is $\mathbf{w}_c$ itself, the class template of @sec-ai-machine-learning-multiclass-svm-loss.

:::

::: {.proof}

1. The first statement is the definition of differentiability (first-order Taylor expansion).
2. For the linear model, $\partial s_c/\partial I_{k,i,j}$ is the entry of $\mathbf{w}_c$ at $(k,i,j)$.

:::

So the saliency map shows the pixels whose small changes move the class score most: the weights of the best local linear approximation of the network around $I$. It tends to highlight the object, and it can be thresholded into a rough segmentation.

::: {#def-class-visualization .definition name="Class visualization by gradient ascent"}

*Class visualization* starts from a random or zero image $I$ and repeats the step $I\gets I+\alpha\nabla_I\bigl(s_c(I)-\lambda\lVert I\rVert_2^2\bigr)$ with the network's weights fixed, often with extra smoothing (blurring, small random shifts) between steps. The result is an image that the network scores highly as class $c$.

:::

::: {#fig-network-visualization-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.0,0) node[lab, right] {step};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$s_c(I)-\lambda\lVert I\rVert^2$};
\draw[hl, domain=0:5.6, samples=80, smooth, variable=\x] plot ({\x}, {2.2-1.9*exp(-0.6*\x)});
\end{tikzpicture}
\end{center}
```

Class visualisation runs gradient ascent on the image itself, with the network fixed, raising the regularised class score until it levels off

:::

```{=latex}
\begin{algorithm}
\caption{Class visualization by gradient ascent}
\begin{algorithmic}
\INPUT trained network with class score $s_c$, step size $\alpha$, penalty $\lambda$, steps $T$
\OUTPUT an image scored highly for class $c$
\STATE $I\gets$ small random image
\FOR{$t=1$ \TO $T$}
    \STATE $\mathbf{g}\gets\nabla_I s_c(I)$ \COMMENT{one forward and one backward pass}
    \STATE $I\gets I+\alpha(\mathbf{g}-2\lambda I)$
    \STATE optionally blur $I$ slightly or shift it by a random offset
\ENDFOR
\RETURN $I$
\end{algorithmic}
\end{algorithm}
```

The same loop with the activation of one hidden unit in place of $s_c$ visualizes what that unit detects; started from a real image and with a different objective it gives DeepDream-style images. Run in the other direction, decreasing $s_y$ for the true class or increasing $s_c$ for a wrong one, a few steps produce an image that looks unchanged but is misclassified: an adversarial example (@sec-ai-deep-learning-adversarial-examples).

::: {#rmk-network-visualization-inversion .remark name="Inverting the code" editor="No figure: saliency maps, occlusion maps and class visualizations are only meaningful for a trained image network on real images, which a static drawing cannot reproduce from the notes' own data."}

Given only the code $\boldsymbol\phi(I)$ of an image, gradient descent on $J$ for $\lVert\boldsymbol\phi(J)-\boldsymbol\phi(I)\rVert^2$ plus an image prior reconstructs images $J$ with the same code. Reconstructions from early layers are nearly exact; from late layers they keep the object and its rough layout but not the details, which shows which information each layer keeps.

:::
