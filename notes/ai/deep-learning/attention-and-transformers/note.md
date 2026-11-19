---
title: "Embeddings, Self-Attention and Transformers"
sources: [cs188-24]
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

Different heads can attend to different things at once, say one to the previous token and another to the subject of the sentence; the reshaping into heads is a rearrange of axes (@exm-einsum-heads).

::: {#def-transformer-block .definition name="Transformer block"}

A *transformer block* maps $X\in\mathbb R^{n\times d}$ to a matrix of the same shape by
$$
X'=X+\operatorname{MultiHead}\bigl(\operatorname{LN}(X)\bigr),\qquad X''=X'+\operatorname{MLP}\bigl(\operatorname{LN}(X')\bigr),
$$
where $\operatorname{LN}$ is layer normalisation (@def-layer-normalization) and the MLP (@def-multi-layer-perceptron) is applied to each row separately. A *transformer* embeds the tokens, adds positional encodings, applies $L$ blocks, and maps each final row to scores over the vocabulary with a linear layer.

:::

Attention mixes information between positions; the MLP processes each position on its own; the residual connections (@def-residual-connection) and layer normalisation keep gradients well-behaved through dozens of blocks. Because every block keeps the shape $n\times d$, blocks stack freely, and the cost of attention, $O(n^{2}d)$ per layer, is what limits the context length $n$.
