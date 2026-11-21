---
title: "Self-Supervised and Contrastive Representation Learning"
sources: [cs231na-3]
requires: [ai/deep-learning/transfer-learning, ai/deep-learning/vision-transformers]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n Assignment 3 (self-supervised learning with SimCLR; CLIP and DINO: contrastive image–text training, zero-shot classification, retrieval, self-distillation), in our own wording; the two propositions and their proofs are our own. This note also fills the representation-learning chapter that the CS229 integration left to the deep learning courses. -->

Labels are expensive; images and text are not. *Self-supervised learning* trains a network on a task built from unlabelled data alone, and keeps the network as a feature extractor for other tasks (@def-transfer-learning). *Contrastive* methods build the task from pairs: two views that belong together (a *positive pair*) should get similar representations, and views that do not (*negatives*) dissimilar ones.

::: {#def-cosine-similarity .definition name="Cosine similarity and temperature"}

The *cosine similarity* of nonzero vectors is $\operatorname{sim}(\mathbf{u},\mathbf{v})=\mathbf{u}\cdot\mathbf{v}/(\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert)\in[-1,1]$. Contrastive losses divide similarities by a *temperature* $\tau>0$ before a softmax (@def-softmax); a small $\tau$ makes the softmax sharper.

:::

::: {#def-simclr .definition name="SimCLR and the NT-Xent loss"}

*SimCLR* takes a minibatch of $N$ images, applies two random augmentations (random resized crop, horizontal flip, colour jitter, random greyscale) to each, and obtains $2N$ views $\tilde{\mathbf{x}}_1,\dots,\tilde{\mathbf{x}}_{2N}$, numbered so that views $k$ and $k+N$ come from the same image. An encoder $f$ gives representations $\mathbf{h}_k=f(\tilde{\mathbf{x}}_k)$ and a small MLP *projection head* $g$ gives $\mathbf{z}_k=g(\mathbf{h}_k)$. With $s_{ik}=\operatorname{sim}(\mathbf{z}_i,\mathbf{z}_k)/\tau$, the loss of the ordered positive pair $(i,j)$ is

$$
\ell(i,j)=-\log\frac{e^{s_{ij}}}{\sum_{k\ne i}e^{s_{ik}}},\qquad L=\frac{1}{2N}\sum_{k=1}^{N}\bigl(\ell(k,k+N)+\ell(k+N,k)\bigr).
$$

After training, $g$ is discarded and $f$ is the feature extractor.

:::

::: {#fig-contrastive-learning-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[faint] (0.0,0.0) rectangle (0.5,0.5);
\node[lab,tick] at (0.25,0.25) {$-\infty$};
\draw[cell frame] (0.5,0.0) rectangle (1.0,0.5);
\draw[cell frame] (1.0,0.0) rectangle (1.5,0.5);
\draw[hl cell] (1.5,0.0) rectangle (2.0,0.5);
\draw[cell frame] (2.0,0.0) rectangle (2.5,0.5);
\draw[cell frame] (2.5,0.0) rectangle (3.0,0.5);
\node[lab,tick,anchor=east] at (-0.05,0.25) {$1$};
\node[lab,tick,anchor=south] at (0.25,0.52) {$1$};
\draw[cell frame] (0.0,-0.5) rectangle (0.5,0.0);
\draw[faint] (0.5,-0.5) rectangle (1.0,0.0);
\node[lab,tick] at (0.75,-0.25) {$-\infty$};
\draw[cell frame] (1.0,-0.5) rectangle (1.5,0.0);
\draw[cell frame] (1.5,-0.5) rectangle (2.0,0.0);
\draw[hl cell] (2.0,-0.5) rectangle (2.5,0.0);
\draw[cell frame] (2.5,-0.5) rectangle (3.0,0.0);
\node[lab,tick,anchor=east] at (-0.05,-0.25) {$2$};
\node[lab,tick,anchor=south] at (0.75,0.52) {$2$};
\draw[cell frame] (0.0,-1.0) rectangle (0.5,-0.5);
\draw[cell frame] (0.5,-1.0) rectangle (1.0,-0.5);
\draw[faint] (1.0,-1.0) rectangle (1.5,-0.5);
\node[lab,tick] at (1.25,-0.75) {$-\infty$};
\draw[cell frame] (1.5,-1.0) rectangle (2.0,-0.5);
\draw[cell frame] (2.0,-1.0) rectangle (2.5,-0.5);
\draw[hl cell] (2.5,-1.0) rectangle (3.0,-0.5);
\node[lab,tick,anchor=east] at (-0.05,-0.75) {$3$};
\node[lab,tick,anchor=south] at (1.25,0.52) {$3$};
\draw[hl cell] (0.0,-1.5) rectangle (0.5,-1.0);
\draw[cell frame] (0.5,-1.5) rectangle (1.0,-1.0);
\draw[cell frame] (1.0,-1.5) rectangle (1.5,-1.0);
\draw[faint] (1.5,-1.5) rectangle (2.0,-1.0);
\node[lab,tick] at (1.75,-1.25) {$-\infty$};
\draw[cell frame] (2.0,-1.5) rectangle (2.5,-1.0);
\draw[cell frame] (2.5,-1.5) rectangle (3.0,-1.0);
\node[lab,tick,anchor=east] at (-0.05,-1.25) {$4$};
\node[lab,tick,anchor=south] at (1.75,0.52) {$4$};
\draw[cell frame] (0.0,-2.0) rectangle (0.5,-1.5);
\draw[hl cell] (0.5,-2.0) rectangle (1.0,-1.5);
\draw[cell frame] (1.0,-2.0) rectangle (1.5,-1.5);
\draw[cell frame] (1.5,-2.0) rectangle (2.0,-1.5);
\draw[faint] (2.0,-2.0) rectangle (2.5,-1.5);
\node[lab,tick] at (2.25,-1.75) {$-\infty$};
\draw[cell frame] (2.5,-2.0) rectangle (3.0,-1.5);
\node[lab,tick,anchor=east] at (-0.05,-1.75) {$5$};
\node[lab,tick,anchor=south] at (2.25,0.52) {$5$};
\draw[cell frame] (0.0,-2.5) rectangle (0.5,-2.0);
\draw[cell frame] (0.5,-2.5) rectangle (1.0,-2.0);
\draw[hl cell] (1.0,-2.5) rectangle (1.5,-2.0);
\draw[cell frame] (1.5,-2.5) rectangle (2.0,-2.0);
\draw[cell frame] (2.0,-2.5) rectangle (2.5,-2.0);
\draw[faint] (2.5,-2.5) rectangle (3.0,-2.0);
\node[lab,tick] at (2.75,-2.25) {$-\infty$};
\node[lab,tick,anchor=east] at (-0.05,-2.25) {$6$};
\node[lab,tick,anchor=south] at (2.75,0.52) {$6$};
\end{tikzpicture}
\end{center}
```

The similarity matrix of one SimCLR step with $N=3$ images, six views. Row $i$ is a softmax classification whose correct class is the other view of the same image (highlighted, column $i\pm3$); the diagonal is excluded.

:::

Each $\ell(i,j)$ is a cross entropy loss (@def-cross-entropy-loss) for a $(2N-1)$-way classification: among all other views in the batch, pick the one that came from the same image. The augmentations decide what the representation must ignore (position, scale, colour), and the negatives keep it from mapping everything to one point.

```{=latex}
\begin{algorithm}
\caption{One SimCLR training step}
\begin{algorithmic}
\INPUT minibatch of $N$ images, augmentation distribution, encoder $f$, head $g$, temperature $\tau$
\OUTPUT updated $f$ and $g$
\FOR{each image $\mathbf{x}_k$, $k=1,\dots,N$}
    \STATE draw two augmentations; $\tilde{\mathbf{x}}_k,\tilde{\mathbf{x}}_{k+N}\gets$ the two views of $\mathbf{x}_k$
\ENDFOR
\STATE $\mathbf{z}_i\gets g(f(\tilde{\mathbf{x}}_i))$ for $i=1,\dots,2N$
\STATE $S_{ik}\gets\operatorname{sim}(\mathbf{z}_i,\mathbf{z}_k)/\tau$ for all $i,k$; set $S_{ii}\gets-\infty$
\STATE $L\gets$ mean over $i$ of the cross entropy of row $i$ of $S$ with target column $i\pm N$
\STATE take a gradient step on $L$ in the parameters of $f$ and $g$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-nt-xent-batch-size .proposition name="The best possible loss depends on the batch size"}

For every choice of the $\mathbf{z}_k$, $\ell(i,j)\ge\log\bigl(1+(2N-2)e^{-2/\tau}\bigr)$.

:::

::: {.proof}

1. Cosine similarities lie in $[-1,1]$, so $e^{s_{ij}}\le e^{1/\tau}$ and each of the $2N-2$ negative terms satisfies $e^{s_{ik}}\ge e^{-1/\tau}$.
2. Hence $\dfrac{e^{s_{ij}}}{e^{s_{ij}}+\sum_{k\ne i,j}e^{s_{ik}}}\le\dfrac{e^{1/\tau}}{e^{1/\tau}+(2N-2)e^{-1/\tau}}$, since $a/(a+b)$ increases in $a$ and decreases in $b$.
3. Taking $-\log$ gives $\ell(i,j)\ge\log\bigl(1+(2N-2)e^{-2/\tau}\bigr)$.

:::

More negatives make the classification harder and the signal richer, so contrastive methods work best with very large batches (thousands of examples). With a fixed batch size, a *memory bank* or queue of representations from earlier batches (as in MoCo, with a slowly updated momentum encoder) supplies more negatives, or methods without negatives such as DINO below are used.

::: {#def-clip .definition name="CLIP"}

*CLIP* trains an image encoder $f$ (a ViT or ResNet) and a text encoder $g$ (a transformer) on $N$ image–caption pairs per minibatch. With normalized embeddings $\mathbf{u}_i=f(\text{image}_i)/\lVert f(\text{image}_i)\rVert$ and $\mathbf{v}_j=g(\text{text}_j)/\lVert g(\text{text}_j)\rVert$ and the $N\times N$ matrix $S_{ij}=\mathbf{u}_i\cdot\mathbf{v}_j/\tau$, the loss is the average of two cross entropy losses: each row of $S$ should classify its image's own caption, and each column its caption's own image,

$$
L=\frac{1}{2N}\sum_{i=1}^{N}\Bigl(-\log\operatorname{softmax}(S_{i,:})_i-\log\operatorname{softmax}(S_{:,i})_i\Bigr).
$$

:::

::: {#def-zero-shot-classification .definition name="Zero-shot classification"}

Given class names $c_1,\dots,c_K$, a *zero-shot classifier* built from CLIP embeds a text for each class (for example "a photo of a $c_k$") as $\mathbf{v}_k$, and assigns an image with embedding $\mathbf{u}$ to $\arg\max_k\mathbf{u}\cdot\mathbf{v}_k$. *Text-to-image retrieval* ranks images by the same similarity with a query text.

:::

No image of the target classes is needed to build the classifier, which makes CLIP features useful for any label set. The same idea extends to more modalities by training encoders for each of them into one shared space, with contrastive losses between pairs of modalities that occur together (for example image–text, image–audio), possibly using one modality, such as images, as the hub.

::: {#def-dino .definition name="DINO: self-distillation without labels"}

*DINO* trains a *student* network $\theta_s$ to match a *teacher* network $\theta_t$ of the same architecture on different views of the same image. Both end in a softmax over $K$ output dimensions, with temperatures $\tau_s>\tau_t$ (the teacher's output is sharper). For views $\mathbf{x}',\mathbf{x}''$, the loss is the cross entropy $H\bigl(p_t(\mathbf{x}'),p_s(\mathbf{x}'')\bigr)$ (@def-cross-entropy), where the teacher sees only large crops and the student also small ones. Only the student is trained by gradients; the teacher's weights are an exponential moving average $\theta_t\gets\lambda\theta_t+(1-\lambda)\theta_s$ with $\lambda$ near $1$, and the teacher's logits are *centred* by subtracting a running mean before its softmax.

:::

::: {#rmk-contrastive-learning-collapse .remark name="Collapse and what DINO features show"}

Without negatives, a trivial solution maps every image to the same output. DINO avoids it by combining centring, which pushes the teacher away from always choosing one dimension, with sharpening, which pushes it away from the uniform output; the moving-average teacher makes the targets change slowly. DINO's ViT patch features carry much spatial information: their principal components separate objects from background and parts of objects, and its attention maps outline objects without any segmentation labels. CLIP's image features are trained only to match a global caption, so they localize less well, and a segmentation model trained on DINO patch features is expected to do better than one on CLIP patch features.

:::
