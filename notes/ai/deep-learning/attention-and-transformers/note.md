---
title: "Embeddings, Self-Attention and Transformers"
sources: [cs188-24, cs231n-13, cs231n-14, cs231na-3]
requires: [ai/deep-learning/training-deep-networks, ai/machine-learning/text-representation]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 24 (tokenization, word embeddings, autoregressive models, self-attention, multi-headed attention, the transformer architecture), in our own wording; the attention numbers were computed with NumPy; the permutation property and its proof are our addition. -->

A language model must turn a sequence of tokens (@def-tokenization) into vectors, and let each position use information from the others. Embeddings do the first; attention does the second; a transformer stacks the two with the tools of @sec-ai-deep-learning-training-deep-networks.

::: {#def-word-embedding .definition name="Embedding"}

For a vocabulary of $V$ tokens, an *embedding* is a matrix $E\in\mathbb R^{V\times d}$ whose row $E_t$ is the vector of token $t$. Embedding a sequence $t_1,\dots,t_n$ gives the matrix $X\in\mathbb R^{n\times d}$ with rows $E_{t_1},\dots,E_{t_n}$; equivalently $X=OE$, where $O$ stacks the one-hot vectors (@def-one-hot) of the tokens. The entries of $E$ are parameters, learnt with the rest of the model.

:::

One-hot vectors make all tokens equally different; learnt embeddings place tokens used in similar contexts near each other, so that what is learnt about one transfers to the others. Similarity is measured by dot products or by the cosine of the angle between vectors, and directions in the space often carry meaning (a fixed offset may turn a singular noun into its plural).

::: {#def-self-attention .definition name="Self-attention"}

Given inputs $X\in\mathbb R^{n\times d}$ (one row per position) and weight matrices $W_Q,W_K\in\mathbb R^{d\times d_k}$, $W_V\in\mathbb R^{d\times d_v}$, form the *queries*, *keys* and *values* $Q=XW_Q$, $K=XW_K$, $V=XW_V$. *Self-attention* outputs
$$
\operatorname{Attention}(X)=\operatorname{softmax}\Bigl(\frac{QK^{\top}}{\sqrt{d_k}}\Bigr)V,
$$
where the softmax (@def-softmax) is applied to each row. Row $i$ of the output is a weighted average of the value vectors, with weights $a_{ij}\propto\exp(\mathbf q_i\cdot\mathbf k_j/\sqrt{d_k})$ summing to $1$ over $j$. With a *causal mask*, the scores with $j>i$ are set to $-\infty$ before the softmax, so position $i$ attends only to positions $1,\dots,i$.

:::

::: {#fig-attention-and-transformers-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (x) at (0,0) {$X$};
\node[box] (q) at (2,1) {$Q=XW_Q$};
\node[box] (k) at (2,0) {$K=XW_K$};
\node[box] (v) at (2,-1) {$V=XW_V$};
\node[hl box] (s) at (5.2,0.5) {$\operatorname{softmax}\bigl(QK^\top/\sqrt{d_k}\bigr)$};
\node[box] (o) at (8.4,0) {output};
\draw[map] (x) -- (q.west);
\draw[map] (x) -- (k.west);
\draw[map] (x) -- (v.west);
\draw[map] (q.east) -- (s);
\draw[map] (k.east) -- (s);
\draw[map] (s) -- (o);
\draw[map] (v.east) -- (o);
\end{tikzpicture}
\end{center}
```

Self-attention: queries and keys give the attention weights, row by row, and each output row is the weighted average of the values

:::

Each position asks a question (its query), every position offers a description of itself (its key), and the answer is a mix of the offered contents (values) in proportion to how well key matches query. Unlike a recurrent network, every position reaches every other in one step, and all positions are computed in parallel. Dividing by $\sqrt{d_k}$ keeps the scores of order $1$ when the entries of $\mathbf q$ and $\mathbf k$ are of order $1$, so that the softmax does not saturate.

::: {#exm-self-attention-toy .example name="Three positions"}

Take $d=d_k=d_v=2$, $W_Q=W_K=W_V=I$ and rows $\mathbf x_1=(1,0)$, $\mathbf x_2=(0,1)$, $\mathbf x_3=(1,1)$. The scores $\mathbf x_i\cdot\mathbf x_j/\sqrt2$ are $0.707$ for $(1,1)$, $(1,3)$, $(2,2)$, $(2,3)$, $1.414$ for $(3,3)$ and $0$ for $(1,2)$. Row-wise softmax gives the weights $(0.401,0.198,0.401)$ for position $1$, $(0.198,0.401,0.401)$ for position $2$ and $(0.248,0.248,0.503)$ for position $3$, so the outputs are $(0.802,0.599)$, $(0.599,0.802)$ and $(0.752,0.752)$. With a causal mask, position $1$ sees only itself (output $(1,0)$) and position $2$ has weights $(0.330,0.670)$ on positions $1,2$ (output $(0.330,0.670)$); position $3$ is unchanged.

:::

::: {#fig-attention-and-transformers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[lab] at (1.12,2.15) {unmasked};
\draw[hl cell] (0.000,1.100) rectangle (0.750,1.850);
\node[lab] at (0.375,1.475) {$0.40$};
\draw[cell frame] (0.750,1.100) rectangle (1.500,1.850);
\node[lab] at (1.125,1.475) {$0.20$};
\draw[hl cell] (1.500,1.100) rectangle (2.250,1.850);
\node[lab] at (1.875,1.475) {$0.40$};
\node[lab, anchor=east] at (-0.100,1.475) {$i=1$};
\draw[cell frame] (0.000,0.350) rectangle (0.750,1.100);
\node[lab] at (0.375,0.725) {$0.20$};
\draw[hl cell] (0.750,0.350) rectangle (1.500,1.100);
\node[lab] at (1.125,0.725) {$0.40$};
\draw[hl cell] (1.500,0.350) rectangle (2.250,1.100);
\node[lab] at (1.875,0.725) {$0.40$};
\node[lab, anchor=east] at (-0.100,0.725) {$i=2$};
\draw[cell frame] (0.000,-0.400) rectangle (0.750,0.350);
\node[lab] at (0.375,-0.025) {$0.25$};
\draw[cell frame] (0.750,-0.400) rectangle (1.500,0.350);
\node[lab] at (1.125,-0.025) {$0.25$};
\draw[hl cell] (1.500,-0.400) rectangle (2.250,0.350);
\node[lab] at (1.875,-0.025) {$0.50$};
\node[lab, anchor=east] at (-0.100,-0.025) {$i=3$};
\node[lab] at (4.53,2.15) {causal mask};
\draw[hl cell] (3.400,1.100) rectangle (4.150,1.850);
\node[lab] at (3.775,1.475) {$1.00$};
\draw[cell frame] (4.150,1.100) rectangle (4.900,1.850);
\draw[cell frame] (4.900,1.100) rectangle (5.650,1.850);
\draw[cell frame] (3.400,0.350) rectangle (4.150,1.100);
\node[lab] at (3.775,0.725) {$0.33$};
\draw[hl cell] (4.150,0.350) rectangle (4.900,1.100);
\node[lab] at (4.525,0.725) {$0.67$};
\draw[cell frame] (4.900,0.350) rectangle (5.650,1.100);
\draw[cell frame] (3.400,-0.400) rectangle (4.150,0.350);
\node[lab] at (3.775,-0.025) {$0.25$};
\draw[cell frame] (4.150,-0.400) rectangle (4.900,0.350);
\node[lab] at (4.525,-0.025) {$0.25$};
\draw[hl cell] (4.900,-0.400) rectangle (5.650,0.350);
\node[lab] at (5.275,-0.025) {$0.50$};
\end{tikzpicture}
\end{center}
```

Attention weights $a_{ij}$ in @exm-self-attention-toy, row $i$ attending to column $j$, the largest weight of each row highlighted. With the causal mask the weights above the diagonal are $0$.

:::

::: {#prp-attention-permutation .proposition name="Attention ignores order"}

Without a mask, self-attention is permutation-equivariant: if $P$ is a permutation matrix, $\operatorname{Attention}(PX)=P\operatorname{Attention}(X)$.

:::

::: {.proof}

1. Replacing $X$ by $PX$ replaces $Q,K,V$ by $PQ,PK,PV$.
2. The scores become $PQK^{\top}P^{\top}$: the same entries with rows and columns permuted in the same way.
3. Row-wise softmax commutes with permuting rows, and permuting the columns of each row permutes the weights together with the entries they multiply, so $\operatorname{softmax}(PSP^{\top})=P\operatorname{softmax}(S)P^{\top}$ for $S=QK^{\top}/\sqrt{d_k}$.
4. Hence the output is $P\operatorname{softmax}(S)P^{\top}PV=P\operatorname{softmax}(S)V$, since $P^{\top}P=I$.

:::

So attention alone treats a sentence as a bag of words. Transformers therefore add a *positional encoding* to each embedding, a vector depending on the position (learnt, or built from sines and cosines of different frequencies), before the first layer.

::: {#def-multi-head-attention .definition name="Multi-head attention"}

*Multi-head attention* with $h$ heads computes $h$ self-attentions in parallel, each with its own $W_Q^{(i)},W_K^{(i)},W_V^{(i)}$ (usually with $d_k=d_v=d/h$), concatenates their outputs to an $n\times d$ matrix and multiplies by an output matrix $W_O\in\mathbb R^{d\times d}$.

:::

::: {#fig-attention-and-transformers-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (h0) at (0.0,0) {head 1};
\draw[map] (2.4,-1.3) -- (h0.south);
\draw[map] (h0.north) -- (2.4,1.1);
\node[box] (h1) at (1.6,0) {head 2};
\draw[map] (2.4,-1.3) -- (h1.south);
\draw[map] (h1.north) -- (2.4,1.1);
\node[box] (h2) at (3.2,0) {head 3};
\draw[map] (2.4,-1.3) -- (h2.south);
\draw[map] (h2.north) -- (2.4,1.1);
\node[box] (h3) at (4.80,0) {head 4};
\draw[map] (2.4,-1.3) -- (h3.south);
\draw[map] (h3.north) -- (2.4,1.1);
\node[lab] at (2.4,-1.5) {$X$};
\node[hl box] at (2.4,1.4) {concatenate, then $W_O$};
\end{tikzpicture}
\end{center}
```

Multi-head attention runs several attention heads with their own projections in parallel and mixes their concatenated outputs with $W_O$

:::

Different heads can attend to different things at once, say one to the previous token and another to the subject of the sentence; the reshaping into heads is a rearrange of axes (@exm-einsum-heads).

::: {#def-transformer-block .definition name="Transformer block"}

A *transformer block* maps $X\in\mathbb R^{n\times d}$ to a matrix of the same shape by
$$
X'=X+\operatorname{MultiHead}\bigl(\operatorname{LN}(X)\bigr),\qquad X''=X'+\operatorname{MLP}\bigl(\operatorname{LN}(X')\bigr),
$$
where $\operatorname{LN}$ is layer normalisation (@def-layer-normalization) and the MLP (@def-multi-layer-perceptron) is applied to each row separately. A *transformer* embeds the tokens, adds positional encodings, applies $L$ blocks, and maps each final row to scores over the vocabulary with a linear layer.

:::

::: {#fig-attention-and-transformers-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (b0) at (0.0,0) {$X$};
\node[box] (b1) at (1.75,0) {LN};
\draw[map] (b0) -- (b1);
\node[hl box] (b2) at (3.5,0) {MultiHead};
\draw[map] (b1) -- (b2);
\node[box] (b3) at (5.25,0) {$+$};
\draw[map] (b2) -- (b3);
\node[box] (b4) at (7.0,0) {LN};
\draw[map] (b3) -- (b4);
\node[hl box] (b5) at (8.75,0) {MLP};
\draw[map] (b4) -- (b5);
\node[box] (b6) at (10.5,0) {$+$};
\draw[map] (b5) -- (b6);
\draw[map] (b0.north) to[out=50, in=130] (b3.north);
\draw[map] (b3.north) to[out=50, in=130] (b6.north);
\end{tikzpicture}
\end{center}
```

A pre-norm transformer block: layer norm, multi-head attention and a residual connection, then layer norm, a row-wise MLP and a second residual connection

:::

Attention mixes information between positions; the MLP processes each position on its own; the residual connections (@def-residual-connection) and layer normalisation keep gradients well-behaved through dozens of blocks. Because every block keeps the shape $n\times d$, blocks stack freely, and the cost of attention, $O(n^{2}d)$ per layer, is what limits the context length $n$.

<!-- Added 2026-11-21 from Stanford CS231n course notes (Attention: general attention layers, masked and multi-head self-attention; Transformers: multi-headed attention step by step, encoder and decoder blocks, layer normalization and MLP) and Assignment 3 (transformer captioning), in our own wording; the variance proposition and its proof are our own. -->

::: {#prp-attention-score-variance .proposition name="Why scale by the square root of the key size" related="def-self-attention"}

Let $\mathbf q,\mathbf k\in\mathbb{R}^{d_k}$ have independent entries with mean $0$ and variance $1$. Then $\mathbf q\cdot\mathbf k$ has mean $0$ and variance $d_k$, so $\mathbf q\cdot\mathbf k/\sqrt{d_k}$ has variance $1$.

:::

::: {.proof}

1. Each term $q_ik_i$ has mean $\mathbb E[q_i]\,\mathbb E[k_i]=0$ and variance $\mathbb E[q_i^2]\,\mathbb E[k_i^2]=1$, by independence.
2. The $d_k$ terms are independent, so the variances add to $d_k$; dividing by $\sqrt{d_k}$ divides the variance by $d_k$.

:::

Without the scaling, scores of size $\sqrt{d_k}$ make the softmax nearly one-hot, and its gradient nearly zero, as soon as $d_k$ is in the hundreds. In multi-head attention the key size of each head is $d/h$, hence the factor $\sqrt{d/h}$.

::: {#def-cross-attention .definition name="Cross-attention"}

*Cross-attention* takes its queries from one sequence $X\in\mathbb{R}^{n\times d}$ and its keys and values from another, $Z\in\mathbb{R}^{m\times d'}$: with $Q=XW_Q$, $K=ZW_K$, $V=ZW_V$, it outputs $\operatorname{softmax}(QK^{\mathsf T}/\sqrt{d_k})V\in\mathbb{R}^{n\times d_v}$. Each of the $n$ query positions mixes the $m$ value vectors of $Z$. Self-attention (@def-self-attention) is the case $Z=X$.

:::

::: {#def-encoder-decoder-transformer .definition name="Encoder–decoder transformer"}

An *encoder–decoder transformer* maps an input sequence to an output sequence. The *encoder* is a stack of transformer blocks (@def-transformer-block) without a mask applied to the embedded input, giving $Z\in\mathbb{R}^{m\times d}$. Each *decoder block* applies, to the embedded output prefix $X$, three residual sublayers, each with layer normalization:

$$
X\gets X+\operatorname{MaskedMultiHead}(X),\qquad X\gets X+\operatorname{CrossAttention}(X,Z),\qquad X\gets X+\operatorname{MLP}(X),
$$

the first with a causal mask, the second with $h$ heads like multi-head attention. A linear layer and a softmax on the final rows predict the next output token.

:::

The decoder is autoregressive like a language model (@def-autoregressive-model), and the cross-attention lets every output position look at the whole input. In image captioning the "input sequence" is a set of image features from a convolutional network or a vision transformer (@sec-ai-deep-learning-vision-transformers), and the decoder generates the caption.

::: {#def-sinusoidal-positional-encoding .definition name="Sinusoidal positional encoding"}

For position $p=0,1,\dots$ and even model width $d$, the *sinusoidal positional encoding* $\mathbf{e}_p\in\mathbb{R}^d$ has entries

$$
e_{p,2i}=\sin\bigl(p/10000^{2i/d}\bigr),\qquad e_{p,2i+1}=\cos\bigl(p/10000^{2i/d}\bigr),\qquad i=0,\dots,d/2-1,
$$

and is added to the embedding of the token at position $p$.

:::

::: {#fig-attention-and-transformers-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.6,0) node[lab, right] {position};
\draw[faint] (0,2.6) -- (6.3,2.6);
\draw[hl, domain=0:6.3, samples=120, smooth, variable=\x] plot ({\x}, {2.6+0.35*sin(deg(1.0*\x*2))});
\node[tick, left] at (0,2.6) {dim $0$};
\draw[faint] (0,1.6) -- (6.3,1.6);
\draw[emph, domain=0:6.3, samples=120, smooth, variable=\x] plot ({\x}, {1.6+0.35*sin(deg(0.45*\x*2))});
\node[tick, left] at (0,1.6) {dim $2$};
\draw[faint] (0,0.6) -- (6.3,0.6);
\draw[emph, domain=0:6.3, samples=120, smooth, variable=\x] plot ({\x}, {0.6+0.35*sin(deg(0.2*\x*2))});
\node[tick, left] at (0,0.6) {dim $4$};
\end{tikzpicture}
\end{center}
```

Sinusoidal positional encoding: each pair of dimensions is a sine and cosine of the position at its own frequency, from fast (top) to slow (bottom), so every position gets a distinct pattern

:::

Each pair of coordinates is a point on a circle rotating with its own frequency, from one turn per $2\pi$ positions to one turn per $2\pi\cdot10^4$ positions; so $\mathbf{e}_{p+k}$ is a fixed rotation of $\mathbf{e}_p$ for each offset $k$, which makes relative positions easy to read off by a linear map. Learnt positional embeddings, one vector per position, work as well for a fixed maximum length.

::: {#rmk-attention-and-transformers-norm-placement .remark name="Where layer normalization goes"}

The original transformer applied layer normalization after each residual addition (*post-norm*, $X\gets\operatorname{LN}(X+\text{sublayer}(X))$). @def-transformer-block normalizes the input of each sublayer instead (*pre-norm*), which keeps an unnormalized identity path through the whole stack and trains more stably for deep models; it is the usual choice today.

:::

