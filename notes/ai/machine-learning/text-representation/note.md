---
title: "Representing Text as Tensors"
sources: [cs221-3]
requires: [ai/machine-learning/linear-classification]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 3 (representing text), in our own wording. -->

Learning works on tensors, but inputs such as documents are strings. They are turned into tensors in two steps.

::: {#def-tokenization .definition name="Tokenization, vocabulary"}

A *tokenizer* splits a string into a sequence of *tokens* (for example words, or sub-word pieces) and maps each token to an index in $\{0,\dots,V-1\}$ through a fixed *vocabulary* of $V$ tokens. A string becomes a sequence of indices $t_1,\dots,t_L$.

:::

::: {#fig-text-representation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (t0) at (0.0,0) {the};
\node[tick, below] at (0.0,-0.45) {$4$};
\node[box] (t1) at (1.15,0) {cat};
\node[tick, below] at (1.15,-0.45) {$1$};
\node[box] (t2) at (2.3,0) {sat};
\node[tick, below] at (2.3,-0.45) {$3$};
\node[box] (t3) at (3.45,0) {on};
\node[tick, below] at (3.45,-0.45) {$2$};
\node[box] (t4) at (4.6,0) {the};
\node[tick, below] at (4.6,-0.45) {$4$};
\node[box] (t5) at (5.75,0) {mat};
\node[tick, below] at (5.75,-0.45) {$0$};
\node[tick, left] at (-0.6,-0.6) {token id};
\end{tikzpicture}
\end{center}
```

Tokenization splits a text into tokens and maps each to its index in the vocabulary; the vocabulary here is cat, mat, on, sat, the, numbered from $0$ in alphabetical order

:::

The simplest tokenizer splits at spaces and gives each new word the next unused index. Language models use sub-word tokenizers such as byte-pair encoding, which keep the vocabulary finite while still covering every string.

::: {#def-one-hot .definition name="One-hot vector"}

The *one-hot* vector of an index $i\in\{0,\dots,V-1\}$ is the standard basis vector $\mathbf{e}_i\in\{0,1\}^V$, with $1$ in position $i$ and $0$ elsewhere. A token sequence $t_1,\dots,t_L$ becomes the $L\times V$ matrix with rows $\mathbf{e}_{t_1}^{\mathsf T},\dots,\mathbf{e}_{t_L}^{\mathsf T}$.

:::

::: {#fig-text-representation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,-0.0) rectangle (0.45,0.45);
\draw[cell frame] (0.45,-0.0) rectangle (0.9,0.45);
\draw[cell frame] (0.9,-0.0) rectangle (1.35,0.45);
\draw[cell frame] (1.35,-0.0) rectangle (1.8,0.45);
\draw[hl cell] (1.8,-0.0) rectangle (2.25,0.45);
\node[tick, left] at (0,0.22) {the};
\draw[cell frame] (0.0,-0.45) rectangle (0.45,0.0);
\draw[hl cell] (0.45,-0.45) rectangle (0.9,0.0);
\draw[cell frame] (0.9,-0.45) rectangle (1.35,0.0);
\draw[cell frame] (1.35,-0.45) rectangle (1.8,0.0);
\draw[cell frame] (1.8,-0.45) rectangle (2.25,0.0);
\node[tick, left] at (0,-0.23) {cat};
\draw[cell frame] (0.0,-0.9) rectangle (0.45,-0.45);
\draw[cell frame] (0.45,-0.9) rectangle (0.9,-0.45);
\draw[cell frame] (0.9,-0.9) rectangle (1.35,-0.45);
\draw[hl cell] (1.35,-0.9) rectangle (1.8,-0.45);
\draw[cell frame] (1.8,-0.9) rectangle (2.25,-0.45);
\node[tick, left] at (0,-0.68) {sat};
\draw[cell frame] (0.0,-1.35) rectangle (0.45,-0.90);
\draw[cell frame] (0.45,-1.35) rectangle (0.9,-0.90);
\draw[hl cell] (0.9,-1.35) rectangle (1.35,-0.90);
\draw[cell frame] (1.35,-1.35) rectangle (1.8,-0.90);
\draw[cell frame] (1.8,-1.35) rectangle (2.25,-0.90);
\node[tick, left] at (0,-1.13) {on};
\draw[cell frame] (0.0,-1.8) rectangle (0.45,-1.35);
\draw[cell frame] (0.45,-1.8) rectangle (0.9,-1.35);
\draw[cell frame] (0.9,-1.8) rectangle (1.35,-1.35);
\draw[cell frame] (1.35,-1.8) rectangle (1.8,-1.35);
\draw[hl cell] (1.8,-1.8) rectangle (2.25,-1.35);
\node[tick, left] at (0,-1.58) {the};
\draw[hl cell] (0.0,-2.25) rectangle (0.45,-1.8);
\draw[cell frame] (0.45,-2.25) rectangle (0.9,-1.8);
\draw[cell frame] (0.9,-2.25) rectangle (1.35,-1.8);
\draw[cell frame] (1.35,-2.25) rectangle (1.8,-1.8);
\draw[cell frame] (1.8,-2.25) rectangle (2.25,-1.8);
\node[tick, left] at (0,-2.03) {mat};
\node[tick, above] at (0.22,0.45) {$0$};
\node[tick, above] at (0.67,0.45) {$1$};
\node[tick, above] at (1.12,0.45) {$2$};
\node[tick, above] at (1.57,0.45) {$3$};
\node[tick, above] at (2.02,0.45) {$4$};
\end{tikzpicture}
\end{center}
```

One-hot encoding of the tokens of @fig-text-representation-1: each token becomes a row with a single $1$ (highlighted) in the column of its index, so the text becomes a $6\times5$ matrix

:::

::: {#rmk-text-representation-1 .remark name="Indices instead of one-hot vectors"}

One-hot vectors are convenient in the mathematics and wasteful in code. Since $\mathbf{w}\cdot\mathbf{e}_i=w_i$ and $W\mathbf{e}_i$ is column $i$ of $W$, a product with a one-hot vector is just a lookup, so code stores the indices and indexes into the weights.

:::

::: {#def-bag-of-words .definition name="Bag of words"}

The *bag-of-words* representation of a token sequence $t_1,\dots,t_L$ is the average of its one-hot vectors,

$$
\boldsymbol{\phi}=\frac{1}{L}\sum_{i=1}^{L}\mathbf{e}_{t_i}\in\mathbb{R}^V,
$$

whose entry $v$ is the fraction of tokens equal to $v$. A linear classifier on it has logit $\mathbf{w}\cdot\boldsymbol{\phi}+b=\frac1L\sum_i w_{t_i}+b$.

:::

::: {#fig-text-representation-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (3.0,0) node[lab, right] {};
\path[bar] (0.175,0) rectangle (0.525,0.600);
\node[tick, below] at (0.350,0) {cat};
\path[bar] (0.725,0) rectangle (1.075,0.600);
\node[tick, below] at (0.900,0) {mat};
\path[bar] (1.275,0) rectangle (1.625,0.600);
\node[tick, below] at (1.450,0) {on};
\path[bar] (1.825,0) rectangle (2.175,0.600);
\node[tick, below] at (2.000,0) {sat};
\path[hl cell] (2.375,0) rectangle (2.725,1.200);
\node[tick, below] at (2.550,0) {the};
\end{tikzpicture}
\end{center}
```

The bag of words of the same text is the column sum of its one-hot matrix: word counts, with the order of the words forgotten

:::

::: {#exm-text-representation-1 .example name="Word order is lost"}

With the vocabulary $\text{dog}\mapsto0$, $\text{bites}\mapsto1$, $\text{man}\mapsto2$, the strings "dog bites man" and "man bites dog" become the index sequences $(0,1,2)$ and $(2,1,0)$ but have the same bag of words $(\tfrac13,\tfrac13,\tfrac13)$. The representation has a fixed length $V$ whatever the length of the text, at the price of ignoring word order.

:::
