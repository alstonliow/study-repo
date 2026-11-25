---
title: "Decision Trees and Comparison Lower Bounds"
sources: [mit6006-4, mit6006-5, mit6006r-4]
requires: [cs/sorting/comparison-sorting, math/discrete/graph/trees]
aliases: [cs/data-structures/comparison-lower-bounds]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lectures 4-5 and Recitation 4, in our own wording; proofs written out in steps. -->

Binary search finds a key with $O(\log n)$ comparisons and merge sort sorts with $O(n\log n)$. In a model where items can only be compared, neither can be beaten.

::: {#def-comparison-model .definition name="Comparison model"}

In the *comparison model*, items are black boxes: the only way an algorithm can learn about them is to compare two of them ($<,\le,=,\dots$), getting a yes/no answer. Its running time is at least the number of comparisons it makes.

:::

::: {#def-decision-tree .definition name="Decision tree"}

Fix a comparison algorithm and an input size $n$. Its *decision tree* is a rooted binary tree (@def-rooted-tree): each internal node is a comparison, with one child for each answer, and each leaf is an output. Running the algorithm on an input follows one root-to-leaf path, and the number of comparisons made is the length of that path. So the worst-case number of comparisons is the *height* of the tree, the length of its longest root-to-leaf path.

:::

::: {#fig-comparison-lower-bounds-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r) at (0,0.0) {$a{<}b$};
\node[box] (l) at (-3,-1.1) {$b{<}c$};
\node[box] (rr) at (3,-1.1) {$a{<}c$};
\node[hl box] (ll) at (-4.4,-2.2) {$abc$};
\node[box] (lr) at (-1.6,-2.2) {$a{<}c$};
\node[hl box] (rl) at (1.6,-2.2) {$bac$};
\node[box] (rrr) at (4.4,-2.2) {$b{<}c$};
\node[hl box] (lrl) at (-2.4,-3.3) {$acb$};
\node[hl box] (lrr) at (-0.8,-3.3) {$cab$};
\node[hl box] (rrl) at (3.6,-3.3) {$bca$};
\node[hl box] (rrrr) at (5.2,-3.3) {$cba$};
\draw (r) -- node[edge label] {yes} (l);
\draw (r) -- node[edge label] {no} (rr);
\draw (l) -- node[edge label] {yes} (ll);
\draw (l) -- node[edge label] {no} (lr);
\draw (rr) -- node[edge label] {yes} (rl);
\draw (rr) -- node[edge label] {no} (rrr);
\draw (lr) -- node[edge label] {yes} (lrl);
\draw (lr) -- node[edge label] {no} (lrr);
\draw (rrr) -- node[edge label] {yes} (rrl);
\draw (rrr) -- node[edge label] {no} (rrrr);
\end{tikzpicture}
\end{center}
```

A decision tree for sorting three distinct items $a,b,c$ (the comparisons made by insertion sort). Internal nodes are comparisons and the $3!=6$ leaves are the possible outputs. Its height is $3=\lceil\log_26\rceil$, so no comparison sort does better on three items.

:::

::: {#lem-binary-tree-leaves .lemma name="Leaves of a binary tree"}

A rooted tree in which every node has at most $b$ children and the height is $h$ has at most $b^h$ leaves. So a binary tree with $L$ leaves has height at least $\lceil\log_2L\rceil$.

:::

::: {.proof}

By induction on $h$. A tree of height $0$ is a single leaf. A tree of height $h\ge1$ consists of a root and at most $b$ subtrees of height at most $h-1$, each with at most $b^{h-1}$ leaves by induction, so at most $b\cdot b^{h-1}=b^h$ leaves in all. For $b=2$, $L\le2^h$ gives $h\ge\log_2L$, and $h$ is an integer.

:::

::: {#thm-comparison-search-lower-bound .theorem name="Searching needs $\Omega(\log n)$ comparisons"}

Any comparison algorithm that, given $n$ stored items and a key $k$, returns the item with key $k$ or reports that there is none, makes at least $\lceil\log_2(n+1)\rceil$ comparisons in the worst case.

:::

::: {.proof}

1. There are $n+1$ possible correct outputs (one of the $n$ items, or "none"), and each must appear at some leaf of the decision tree, since on some input it is the only correct output.

2. So the tree has at least $n+1$ leaves and, by @lem-binary-tree-leaves, height at least $\lceil\log_2(n+1)\rceil$.

:::

::: {#thm-comparison-sort-lower-bound .theorem name="Sorting needs $\Omega(n\log n)$ comparisons"}

Any comparison sorting algorithm makes $\Omega(n\log n)$ comparisons in the worst case on inputs of $n$ distinct items.

:::

::: {.proof}

1. For distinct items, each of the $n!$ orderings of the input needs a different output permutation, so the decision tree has at least $n!$ leaves and height at least $\log_2n!$.

2. The largest $n/2$ factors of $n!$ are each at least $n/2$, so $n!\ge(n/2)^{n/2}$ and $\log_2n!\ge\frac n2\log_2\frac n2=\Omega(n\log n)$.

:::

So merge sort (@thm-merge-sort) is optimal among comparison sorts, and binary search (@prp-binary-search) is optimal among comparison searches. (Stirling's formula, @thm-stirling, gives the sharper $\log_2n!=n\log_2n-\Theta(n)$.)

::: {#rmk-comparison-lower-bounds-escape .remark name="Escaping the comparison model"}

The bounds hold only for algorithms that compare. In the word-RAM, using a key as an *array index* gives an operation with up to $n$ outcomes instead of two, and @lem-binary-tree-leaves with large $b$ allows much shallower trees. This is how hashing finds keys in $O(1)$ expected time (@sec-cs-data-structures-hashing) and how counting and radix sort sort integers in linear time (@sec-cs-sorting-linear-sorting).

:::
