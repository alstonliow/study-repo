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

The simplest tokenizer splits at spaces and gives each new word the next unused index. Language models use sub-word tokenizers such as byte-pair encoding, which keep the vocabulary finite while still covering every string.

::: {#def-one-hot .definition name="One-hot vector"}

The *one-hot* vector of an index $i\in\{0,\dots,V-1\}$ is the standard basis vector $\mathbf{e}_i\in\{0,1\}^V$, with $1$ in position $i$ and $0$ elsewhere. A token sequence $t_1,\dots,t_L$ becomes the $L\times V$ matrix with rows $\mathbf{e}_{t_1}^{\mathsf T},\dots,\mathbf{e}_{t_L}^{\mathsf T}$.

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

::: {#exm-text-representation-1 .example name="Word order is lost"}

With the vocabulary $\text{dog}\mapsto0$, $\text{bites}\mapsto1$, $\text{man}\mapsto2$, the strings "dog bites man" and "man bites dog" become the index sequences $(0,1,2)$ and $(2,1,0)$ but have the same bag of words $(\tfrac13,\tfrac13,\tfrac13)$. The representation has a fixed length $V$ whatever the length of the text, at the price of ignoring word order.

:::
