---
title: "Fusion Trees"
sources: [mit6851-12]
requires: [cs/integer-data-structures/y-fast-trees, cs/data-structures/two-three-trees]
aliases: [cs/advanced-data-structures/fusion-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 12, in our own wording. Brief version (owner scope: integer structures briefly): the multiplication trick for approximate sketches and the constant-time most-significant-bit routine are only stated. The example and figure are our own; the example was checked by computation. -->

A *fusion tree* (Fredman and Willard) stores a static set of $n$ keys of $w$ bits in $O(n)$ space and answers predecessor queries in $O(\log_wn)$ time on the word RAM. It is a B-tree with branching factor about $w^{1/5}$; the work is in searching one node in $O(1)$ time, although a node holds $w^{1/5}$ keys, that is $w^{6/5}$ bits, more than a word.

::: {#def-sketch .definition name="Perfect sketch"}

Let $x_0<\dots<x_{k-1}$ be the keys of a node, written as $w$-bit strings, and overlay their root-to-leaf paths in the binary trie of depth $w$. The paths branch at most $k-1$ times, at some bit positions $b_0<\dots<b_{r-1}$ with $r\le k-1$. The *perfect sketch* of any $w$-bit word $y$ is the $r$-bit string $\operatorname{sketch}(y)$ whose $i$-th bit is the bit $b_i$ of $y$.

:::

::: {#exm-fusion-trees-1 .example name="Four keys"}

The keys $010000$, $010001$, $010011$, $011011$ (bit $1$ is the leftmost) branch at the bit positions $3,5,6$, so their sketches are $000,001,011,111$.

:::

::: {#fig-fusion-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.00,2.4) rectangle +(0.55,0.55); \node[lab] at (0.275,2.675) {$0$};
\draw[cell frame] (0.55,2.4) rectangle +(0.55,0.55); \node[lab] at (0.825,2.675) {$1$};
\draw[hl cell] (1.10,2.4) rectangle +(0.55,0.55); \node[lab] at (1.375,2.675) {$0$};
\draw[cell frame] (1.65,2.4) rectangle +(0.55,0.55); \node[lab] at (1.925,2.675) {$0$};
\draw[hl cell] (2.20,2.4) rectangle +(0.55,0.55); \node[lab] at (2.475,2.675) {$0$};
\draw[hl cell] (2.75,2.4) rectangle +(0.55,0.55); \node[lab] at (3.025,2.675) {$0$};
\node[lab, anchor=west] at (3.5,2.675) {$\to 000$};
\draw[cell frame] (0.00,1.6) rectangle +(0.55,0.55); \node[lab] at (0.275,1.875) {$0$};
\draw[cell frame] (0.55,1.6) rectangle +(0.55,0.55); \node[lab] at (0.825,1.875) {$1$};
\draw[hl cell] (1.10,1.6) rectangle +(0.55,0.55); \node[lab] at (1.375,1.875) {$0$};
\draw[cell frame] (1.65,1.6) rectangle +(0.55,0.55); \node[lab] at (1.925,1.875) {$0$};
\draw[hl cell] (2.20,1.6) rectangle +(0.55,0.55); \node[lab] at (2.475,1.875) {$0$};
\draw[hl cell] (2.75,1.6) rectangle +(0.55,0.55); \node[lab] at (3.025,1.875) {$1$};
\node[lab, anchor=west] at (3.5,1.875) {$\to 001$};
\draw[cell frame] (0.00,0.8) rectangle +(0.55,0.55); \node[lab] at (0.275,1.075) {$0$};
\draw[cell frame] (0.55,0.8) rectangle +(0.55,0.55); \node[lab] at (0.825,1.075) {$1$};
\draw[hl cell] (1.10,0.8) rectangle +(0.55,0.55); \node[lab] at (1.375,1.075) {$0$};
\draw[cell frame] (1.65,0.8) rectangle +(0.55,0.55); \node[lab] at (1.925,1.075) {$0$};
\draw[hl cell] (2.20,0.8) rectangle +(0.55,0.55); \node[lab] at (2.475,1.075) {$1$};
\draw[hl cell] (2.75,0.8) rectangle +(0.55,0.55); \node[lab] at (3.025,1.075) {$1$};
\node[lab, anchor=west] at (3.5,1.075) {$\to 011$};
\draw[cell frame] (0.00,0.0) rectangle +(0.55,0.55); \node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.55,0.0) rectangle +(0.55,0.55); \node[lab] at (0.825,0.275) {$1$};
\draw[hl cell] (1.10,0.0) rectangle +(0.55,0.55); \node[lab] at (1.375,0.275) {$1$};
\draw[cell frame] (1.65,0.0) rectangle +(0.55,0.55); \node[lab] at (1.925,0.275) {$0$};
\draw[hl cell] (2.20,0.0) rectangle +(0.55,0.55); \node[lab] at (2.475,0.275) {$1$};
\draw[hl cell] (2.75,0.0) rectangle +(0.55,0.55); \node[lab] at (3.025,0.275) {$1$};
\node[lab, anchor=west] at (3.5,0.275) {$\to 111$};
\end{tikzpicture}
\end{center}
```

The four keys of @exm-fusion-trees-1; the shaded columns (bits $3,5,6$) are the branching bits, and the sketch is read off them.

:::

::: {#prp-sketch-order .proposition name="Sketches keep the order of the keys"}

$\operatorname{sketch}(x_0)<\dots<\operatorname{sketch}(x_{k-1})$, and all $k$ sketches together have $O(k\cdot k)=O(w^{2/5})=o(w)$ bits, so they fit in one word.

:::

::: {.proof}

1. Two keys $x_i<x_j$ first differ at a branching bit $b_m$ (their paths separate there), where $x_i$ has $0$ and $x_j$ has $1$, and agree on all earlier bits.

2. Earlier sketch bits are copies of earlier bits of the keys, so they agree too, and the sketches first differ at position $m$ in the same direction: $\operatorname{sketch}(x_i)<\operatorname{sketch}(x_j)$.

3. Each sketch has $r\le k-1<w^{1/5}$ bits.

:::

A query $q$ need not be one of the keys, and its path may leave the overlaid paths at a bit that is not sketched, so its sketch can land in the wrong place among the key sketches. *Desketching* repairs this.

::: {#prp-desketching .proposition name="Desketching"}

Let $x_i,x_{i+1}$ be the two keys whose sketches surround $\operatorname{sketch}(q)$, and let $p$ be the longest common prefix of $q$ with a key of the node, of length $y$ (it is attained by $x_i$ or $x_{i+1}$). If bit $y+1$ of $q$ is $1$, the predecessor of $q$ among the keys is the largest key $\le p01\cdots1$ (the largest word with the prefix $p0$), and if it is $0$ the successor of $q$ is the smallest key $\ge p10\cdots0$; searching with this word by sketch is then correct, because it leaves the overlaid paths at a sketched bit.

:::

::: {.proof}

1. The node $p$ of the trie is where $q$'s path leaves the union of the keys' paths, and the child of $p$ on $q$'s side contains no key.

2. The other child contains a key (the one chosen above), hence the predecessor or the successor of $q$ is in it, namely its maximum or its minimum on that side.

3. The word $p01\cdots1$ (or $p10\cdots0$) is exactly the extreme word of that child's side, and it branches off the key paths at a sketched bit, so its sketch is placed correctly among the key sketches, and one more predecessor or successor step among the sketches finishes.

:::

::: {#prp-parallel-comparison .proposition name="Parallel comparison"}

Given the node word $1\,\operatorname{sketch}(x_0)\,1\,\operatorname{sketch}(x_1)\cdots1\,\operatorname{sketch}(x_{k-1})$ and a query sketch, the number of key sketches smaller than $\operatorname{sketch}(q)$ is computed with $O(1)$ word operations.

:::

::: {.proof}

1. Multiply $\operatorname{sketch}(q)$ by $0\cdots01\,0\cdots01\cdots$ to get $k$ copies $0\operatorname{sketch}(q)$ in $k$ blocks.

2. Subtract this word from the node word. Because each block of the node word has a leading $1$ and each block of the copies a leading $0$, no borrow crosses a block, and the leading bit of block $i$ of the result is $1$ exactly when $\operatorname{sketch}(x_i)\ge\operatorname{sketch}(q)$.

3. Mask the leading bits. The sketches are sorted, so the $1$s form a suffix of blocks; their number is found by one multiplication by $0\cdots01\cdots0\cdots01$ (which adds all leading bits into one block) and a shift, or equivalently by finding the most significant set bit. The count gives the rank of $q$.

:::

::: {#thm-fusion-tree .theorem name="Fusion tree (Fredman–Willard)"}

A static set of $n$ $w$-bit keys can be stored in $O(n)$ space so that predecessor and successor queries take $O(\log_wn)$ time on the word RAM.

:::

::: {.proof}

1. Build a B-tree with branching factor $k=w^{1/5}$ and $\Theta(\log_wn)$ levels; each node is stored as its sketch word, the node word of @prp-parallel-comparison and the keys themselves.

2. At each node, find the rank of $q$ among the key sketches (@prp-parallel-comparison), apply @prp-desketching to correct it, and descend: $O(1)$ time per node, with the sketch of a word computed in $O(1)$ by the approximate-sketch construction below.

3. The space is $O(1)$ words per key.

:::

::: {#rmk-fusion-trees-1 .remark name="What is not proved here"}

The perfect sketch is a single operation in the AC$^0$ model. On the word RAM the lecture computes an *approximate sketch*: mask the branching bits, multiply by a constant $m=\sum_j2^{m_j}$ with the $m_j$ chosen so that the products $b_i+m_j$ do not collide and keep their order, and the useful bits end up in a window of $O(w^{4/5})$ bits, with garbage between them that does not matter for comparisons. The most significant set bit of a word is found in $O(1)$ time by the same word-parallel tricks applied to $\sqrt w$ clusters of $\sqrt w$ bits. Dynamic versions exist (via exponential trees, $O(\log_wn+\log\log n)$ update; via hashing, expected $O(\log_wn)$).

:::
