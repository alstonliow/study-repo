---
title: "AVL Trees"
sources: [mit6006-7, mit6006r-7]
requires: [cs/data-structures/binary-trees]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 7 and Recitation 7, in our own wording; proofs written out in steps. -->

A binary tree is *balanced* if its height stays $O(\log n)$ under insertions and deletions. AVL trees (Adelson-Velsky and Landis, 1962) were the first balancing scheme; red-black trees, splay trees and 2-3 trees are others.

## Rotations

::: {#def-rotation .definition name="Rotation"}

Let $D$ be a node with left child $B$, let $A$ and $C$ be the left and right subtrees of $B$, and $E$ the right subtree of $D$. A *right rotation* at $D$ makes $B$ take $D$'s place (attached to $D$'s old parent), with left subtree $A$ and right child $D$, and gives $D$ the subtrees $C$ and $E$. A *left rotation* at $B$ is the inverse operation.

:::

::: {#fig-avl-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.9cm]
\node[vertex] (d) at (1,2) {$D$}; \node[vertex] (b) at (0,1) {$B$};
\node[lab] (a) at (-0.6,0) {$A$}; \node[lab] (c) at (0.6,0) {$C$}; \node[lab] (e) at (1.8,1) {$E$};
\draw (d)--(b) (b)--(a) (b)--(c) (d)--(e);
\node[lab] at (4.1,1.35) {right rotation at $D$};
\draw[emph,->] (3.1,1) -- (5.1,1);
\draw[emph,->] (5.1,0.7) -- (3.1,0.7);
\node[lab] at (4.1,0.35) {left rotation at $B$};
\node[vertex] (b2) at (7.2,2) {$B$}; \node[vertex] (d2) at (8.2,1) {$D$};
\node[lab] (a2) at (6.4,1) {$A$}; \node[lab] (c2) at (7.6,0) {$C$}; \node[lab] (e2) at (8.8,0) {$E$};
\draw (b2)--(a2) (b2)--(d2) (d2)--(c2) (d2)--(e2);
\end{tikzpicture}
\end{center}
```

A rotation changes $O(1)$ pointers and keeps the traversal order $A,B,C,D,E$.

:::

Both trees in @fig-avl-trees-1 have traversal order $A,B,C,D,E$ (each letter of a subtree standing for its nodes in order), so a rotation never changes the stored sequence or set. Rotations are enough to reach any shape: repeatedly rotating right turns any tree into a path hanging to the right, after at most $n-1$ rotations (each one increases the depth of the last node by one), and reversing these steps reaches any other tree with the same traversal order. So $O(n)$ rotations transform any tree into any other with the same order; AVL trees need only $O(\log n)$ per update.

## Height balance

::: {#def-height-balanced .definition name="Height-balanced, AVL tree"}

The *skew* of a node is the height of its right subtree minus the height of its left subtree, where an empty subtree has height $-1$. A node is *height-balanced* if its skew is $-1$, $0$ or $1$. An *AVL tree* is a binary tree in which every node is height-balanced.

:::

::: {#thm-avl-height .theorem name="AVL trees are shallow"}

An AVL tree with $n$ nodes has height $h<2\log_2(n+1)$. So $h=O(\log n)$.

:::

::: {.proof}

1. Let $F(h)$ be the fewest nodes in an AVL tree of height $h$. Then $F(0)=1$ and $F(1)=2$.

2. For $h\ge2$, the root has a subtree of height $h-1$, and by height balance the other subtree has height at least $h-2$. Both subtrees are AVL trees, so $F(h)\ge1+F(h-1)+F(h-2)$.

3. $F$ is increasing, so $F(h)>2F(h-2)$, and by induction $F(h)\ge2^{h/2}$ (true for $h=0,1$).

4. So $n\ge2^{h/2}$, that is, $h\le2\log_2n<2\log_2(n+1)$.

:::

(In fact $F(h)+1$ is a Fibonacci number, so $h\approx1.44\log_2n$ at worst.)

## Rebalancing

Adding or removing a leaf changes the heights only of its ancestors, each by at most $1$, so afterwards every skew lies in $\{-2,\dots,2\}$. We repair the lowest node that is not height-balanced, and move up.

::: {#lem-avl-local-rebalance .lemma name="Local rebalance"}

Let $B$ be a node of skew $2$ whose subtree is otherwise height-balanced, and let $F$ be its right child.

1. If the skew of $F$ is $0$ or $1$, a left rotation at $B$ makes the subtree height-balanced.
2. If the skew of $F$ is $-1$, a right rotation at $F$ followed by a left rotation at $B$ makes it height-balanced.

The height of the subtree afterwards equals its old height, or is one less. It is one less except in case 1 with skew $0$. Skew $-2$ is symmetric.

:::

::: {.proof}

Let $A$ be the left subtree of $B$, of height $a$. Since the skew of $B$ is $2$, $F$ has height $a+2$, and the subtree of $B$ has height $a+3$.

1. *Skew of $F$ is $0$ or $1$.* Let $D$ and $G$ be the left and right subtrees of $F$. Then $G$ has height $a+1$, and $D$ has height $a+1$ (skew $0$) or $a$ (skew $1$). After the left rotation, $B$ has subtrees $A$ and $D$, so its skew is $1$ or $0$ and its height is $a+2$ or $a+1$; $F$ has subtrees $B$ and $G$, so its skew is $-1$ or $0$, and its height is $a+3$ or $a+2$.

2. *Skew of $F$ is $-1$.* Then the left child $D$ of $F$ has height $a+1$ and the right subtree $G$ of $F$ has height $a$. Let $C$ and $E$ be the subtrees of $D$; both have height $a$ or $a-1$, at least one of them $a$. After the two rotations, $D$ is on top with children $B$ (subtrees $A$, $C$) and $F$ (subtrees $E$, $G$). Then $B$ has skew $0$ or $-1$, $F$ has skew $0$ or $1$, both have height $a+1$, and $D$ has skew $0$ and height $a+2$.

3. Nodes inside $A,C,E,G$ are unchanged, so the whole subtree is height-balanced.

:::

::: {#fig-avl-trees-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (b) at (0,0) {$B$};
\node[small vertex] (f) at (0.9,-0.8) {$F$};
\draw (b) -- (-0.5,-0.8);
\draw (b)--(f);
\draw (f) -- (0.45,-1.55);
\draw (f) -- (1.35,-1.55);
\draw (-0.50,-0.80) -- (-0.85,-1.80) -- (-0.15,-1.80) -- cycle;
\node[lab,tick] at (-0.50,-1.55) {$A$};
\draw (0.45,-1.55) -- (0.10,-2.55) -- (0.80,-2.55) -- cycle;
\node[lab,tick] at (0.45,-2.30) {$D$};
\draw (1.35,-1.55) -- (1.00,-2.95) -- (1.70,-2.95) -- cycle;
\node[lab,tick] at (1.35,-2.70) {$G$};
\draw[emph,->] (2.0,-0.9) -- (3.0,-0.9);
\node[lab,tick] at (2.5,-0.6) {left at $B$};
\node[small vertex] (f2) at (4.6,0) {$F$};
\node[small vertex] (b2) at (3.7,-0.8) {$B$};
\draw (f2)--(b2);
\draw (b2) -- (3.25,-1.55);
\draw (b2) -- (4.15,-1.55);
\draw (f2) -- (5.1,-0.8);
\draw (3.25,-1.55) -- (2.90,-2.55) -- (3.60,-2.55) -- cycle;
\node[lab,tick] at (3.25,-2.30) {$A$};
\draw (4.15,-1.55) -- (3.80,-2.55) -- (4.50,-2.55) -- cycle;
\node[lab,tick] at (4.15,-2.30) {$D$};
\draw (5.10,-0.80) -- (4.75,-2.20) -- (5.45,-2.20) -- cycle;
\node[lab,tick] at (5.10,-1.95) {$G$};
\node[lab] at (2.3,-3.2) {skew of $F$ is $1$: one rotation};
\node[small vertex] (bb) at (7.0,0) {$B$};
\node[small vertex] (ff) at (8.2,-0.8) {$F$};
\node[small vertex] (dd) at (7.6,-1.6) {$D$};
\draw (bb) -- (6.5,-0.8);
\draw (bb)--(ff);
\draw (ff)--(dd);
\draw (ff) -- (8.7,-1.6);
\draw (dd) -- (7.2,-2.3);
\draw (dd) -- (8.0,-2.3);
\draw (6.50,-0.80) -- (6.15,-1.80) -- (6.85,-1.80) -- cycle;
\node[lab,tick] at (6.50,-1.55) {$A$};
\draw (8.70,-1.60) -- (8.35,-2.60) -- (9.05,-2.60) -- cycle;
\node[lab,tick] at (8.70,-2.35) {$G$};
\draw (7.20,-2.30) -- (6.85,-3.05) -- (7.55,-3.05) -- cycle;
\node[lab,tick] at (7.20,-2.80) {$C$};
\draw (8.00,-2.30) -- (7.65,-3.05) -- (8.35,-3.05) -- cycle;
\node[lab,tick] at (8.00,-2.80) {$E$};
\draw[emph,->] (9.2,-0.9) -- (10.2,-0.9);
\node[lab,tick] at (9.7,-0.6) {right at $F$,};
\node[lab,tick] at (9.7,-1.2) {left at $B$};
\node[small vertex] (d3) at (11.6,0) {$D$};
\node[small vertex] (b3) at (10.80,-0.8) {$B$};
\node[small vertex] (f3) at (12.4,-0.8) {$F$};
\draw (d3)--(b3);
\draw (d3)--(f3);
\draw (b3) -- (10.45,-1.55);
\draw (b3) -- (11.15,-1.55);
\draw (f3) -- (12.05,-1.55);
\draw (f3) -- (12.75,-1.55);
\draw (10.45,-1.55) -- (10.10,-2.55) -- (10.80,-2.55) -- cycle;
\node[lab,tick] at (10.45,-2.30) {$A$};
\draw (11.15,-1.55) -- (10.80,-2.30) -- (11.50,-2.30) -- cycle;
\node[lab,tick] at (11.15,-2.05) {$C$};
\draw (12.05,-1.55) -- (11.70,-2.30) -- (12.40,-2.30) -- cycle;
\node[lab,tick] at (12.05,-2.05) {$E$};
\draw (12.75,-1.55) -- (12.40,-2.55) -- (13.10,-2.55) -- cycle;
\node[lab,tick] at (12.75,-2.30) {$G$};
\node[lab] at (9.4,-3.2) {skew of $F$ is $-1$: two rotations};
\end{tikzpicture}
\end{center}
```

The two cases of @lem-avl-local-rebalance, with subtree heights drawn to scale ($A$ has height $h$). Left: $B$ has skew $2$ and its right child $F$ has skew $1$; one left rotation balances both. Right: $F$ has skew $-1$; rotating right at $F$ and then left at $B$ lifts $D$ to the top.

:::

::: {#thm-avl-global-rebalance .theorem name="Global rebalance"}

After adding or removing a leaf in an AVL tree, the tree can be made an AVL tree again with $O(\log n)$ rotations, by repairing, from the bottom up, every ancestor of the changed leaf that is not height-balanced.

:::

::: {.proof}

1. Only ancestors of the changed leaf change height, and there are at most $h+1=O(\log n)$ of them (@thm-avl-height). Let $X$ be the lowest one that is not height-balanced; its subtree is otherwise balanced, so @lem-avl-local-rebalance applies, with at most two rotations.

2. *Insertion.* The new leaf is in the subtree of the heavy child of $X$ and made that child one taller. A balanced node whose height just grew because of one new leaf below it has skew $\pm1$, not $0$. So the heavy child has skew $1$ or $-1$, and in both cases the lemma reduces the height of $X$'s subtree by one, back to its height before the insertion, so no ancestor of $X$ changes height or skew: one repair suffices.

3. *Deletion.* The repair can lower the height of $X$'s subtree by one, which may unbalance an ancestor. Repeat at the next unbalanced ancestor; each repair costs $O(1)$ rotations, and there are $O(\log n)$ ancestors.

:::

To find unbalanced nodes quickly, every node stores its height. This is an instance of a general technique.

::: {#def-subtree-augmentation .definition name="Subtree augmentation"}

A binary tree is *augmented* with a subtree property $P$ if every node $X$ stores $P(X)$, a value that depends only on $X$'s subtree and can be computed in $O(1)$ time from $X$'s item and the stored values of its children. Examples are the height ($1+\max$ of the children's heights) and the size ($1+$ the sum of the children's sizes).

:::

An augmentation is kept correct at no extra asymptotic cost: after a rotation, recompute it for the $O(1)$ relinked nodes, from the bottom up; after adding or removing a leaf, recompute it for the $O(\log n)$ ancestors.

::: {#thm-avl-operations .theorem name="AVL trees as sets and sequences"}

1. A *set AVL tree* (an AVL binary search tree) supports `find`, `insert`, `delete`, `find_min`, `find_max`, `find_prev` and `find_next` in $O(\log n)$ time, `build` in $O(n\log n)$ time and `iter_ord` in $O(n)$ time.
2. A *sequence AVL tree* (augmented with subtree sizes) supports `get_at`, `set_at`, `insert_at`, `delete_at` and the operations at both ends in $O(\log n)$ time, and `build` and `iter_seq` in $O(n)$ time.

:::

::: {.proof}

Each operation of @sec-cs-data-structures-binary-trees takes $O(h)$ time and changes at most one leaf, after which rebalancing takes $O(\log n)$ rotations and augmentation updates (@thm-avl-global-rebalance). With $h=O(\log n)$ (@thm-avl-height) all of these are $O(\log n)$. The sequence build splits at the middle, which gives a tree whose skews are all in $\{-1,0,1\}$, in $O(n)$ time.

:::

Any set data structure gives a sorting algorithm: build it, then list the items in order. With a set AVL tree this is *AVL sort*, another $O(n\log n)$ comparison sort (optimal by @thm-comparison-sort-lower-bound).
