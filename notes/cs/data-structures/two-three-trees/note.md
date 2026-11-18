---
title: "2-3 Trees and B-Trees"
sources: [mit6046r-2]
requires: [cs/data-structures/avl-trees]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Recitation 2, in our own wording; proofs written out in steps. -->

AVL trees stay balanced by rotations. Another way is to let a node hold more than one key, so that all leaves can be kept at exactly the same depth.

::: {#def-two-three-tree .definition name="2-3 tree"}

A *2-3 tree* is a rooted search tree in which every internal node either holds one key and has two children (a *2-node*) or holds two keys and has three children (a *3-node*), every leaf holds one or two keys, and all leaves are at the same depth. Keys are ordered as in a binary search tree: in a 3-node with keys $a<b$, the keys of the left, middle and right subtrees are less than $a$, between $a$ and $b$, and greater than $b$.

:::

::: {#prp-two-three-height .proposition name="Height of a 2-3 tree"}

A 2-3 tree of height $h$ (edges from the root to a leaf) has between $2^h$ and $3^h$ leaves. Hence a 2-3 tree with $n$ keys has height $\Theta(\log n)$.

:::

::: {.proof}

1. By induction on $h$: a tree of height $0$ is one leaf; for $h\ge1$ the root has $2$ or $3$ subtrees of height $h-1$, each with between $2^{h-1}$ and $3^{h-1}$ leaves.

2. Each node holds one or two keys and there are between $2^h$ and $2\cdot3^h$ nodes, so $2^h\le n\le4\cdot3^h$, which gives $\log_3(n/4)\le h\le\log_2n$.

:::

Searching works as in a binary search tree, comparing with one or two keys per node: $O(\log n)$ time.

```{=latex}
\begin{algorithm}
\caption{Search in a 2-3 tree}
\begin{algorithmic}
\INPUT Root $X$ of a 2-3 tree, key $k$
\OUTPUT Whether $k$ is stored
\WHILE{$X$ is not none}
    \IF{$k$ is a key of $X$}
        \RETURN yes
    \ENDIF
    \STATE $X\gets$ the child of $X$ whose key range contains $k$ \COMMENT{none at a leaf}
\ENDWHILE
\RETURN no
\end{algorithmic}
\end{algorithm}
```

::: {#prp-two-three-insert .proposition name="Insertion by splitting"}

To insert a key, search down to the leaf where it belongs and add it there. If a node now holds three keys $a<b<c$, *split* it: $a$ and $c$ become two separate nodes (sharing the four children, two each) and $b$ moves up into the parent. Repeat at the parent if it overflows; if the root splits, the middle key becomes a new root. Insertion takes $O(\log n)$ time and keeps all leaves at the same depth.

:::

::: {.proof}

1. A split replaces one overfull node by two valid nodes at the same depth and gives the parent one more key and one more child, so no leaf changes depth.

2. The middle key $b$ separates the keys of the two new nodes, so the search order is kept.

3. Only a split of the root adds a level, and it adds it above every leaf at once. Each split takes $O(1)$ time and happens at most once per level: $O(\log n)$ in total.

:::

```{=latex}
\begin{algorithm}
\caption{Insert in a 2-3 tree}
\begin{algorithmic}
\INPUT 2-3 tree, new key $k$
\STATE $X\gets$ the leaf reached by searching for $k$; add $k$ to $X$
\WHILE{$X$ holds three keys $a<b<c$}
    \STATE split $X$ into a node with $a$ and a node with $c$, giving each two of $X$'s children
    \IF{$X$ is the root}
        \STATE make a new root holding $b$ with these two children \COMMENT{the tree grows at the top}
        \RETURN
    \ENDIF
    \STATE move $b$ into $X.\mathrm{parent}$, between the two new nodes; $X\gets X.\mathrm{parent}$
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

::: {#fig-two-three-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=0.9cm]
\node[box] (r) at (1.5,0) {$10\;\;20$};
\node[box] (a) at (0,-1.2) {$5$}; \node[box] (b) at (1.5,-1.2) {$15$}; \node[hl box] (c) at (3,-1.2) {$25\;\;30\;\;35$};
\draw (r)--(a) (r)--(b) (r)--(c);
\draw[emph,->] (4.2,-0.6) -- (5.2,-0.6);
\node[hl box] (r2) at (7.5,1.2) {$20$};
\node[box] (l2) at (6.2,0) {$10$}; \node[box] (m2) at (8.8,0) {$30$};
\node[box] (a2) at (5.5,-1.2) {$5$}; \node[box] (b2) at (6.9,-1.2) {$15$}; \node[box] (c2) at (8.1,-1.2) {$25$}; \node[box] (d2) at (9.5,-1.2) {$35$};
\draw (r2)--(l2) (r2)--(m2) (l2)--(a2) (l2)--(b2) (m2)--(c2) (m2)--(d2);
\end{tikzpicture}
\end{center}
```

Inserting $35$ overfills a leaf ($25,30,35$). It splits and sends $30$ up; now the root holds $10,20,30$ and splits too, sending $20$ up as a new root. The tree grows by one level at the top, so all leaves stay at the same depth.

:::

Deletion is the reverse. Swap a key in an internal node with its successor (which is in a leaf) and remove it from the leaf. If a node becomes empty, *borrow* a key through the parent from a neighbouring sibling that has two keys, or else *merge* with a sibling by pulling a key down from the parent, and repeat upwards. This also takes $O(\log n)$ time.

::: {#def-b-tree .definition name="B-tree"}

A *B-tree* with branching parameter $B\ge2$ generalises 2-3 trees: every internal node other than the root has between $B$ and $2B$ children (and one key fewer than children), the root has between $2$ and $2B$ children, and all leaves are at the same depth. Insertion splits overfull nodes and deletion borrows or merges, as above.

:::

A B-tree has height $\Theta(\log_Bn)$. If a node fits in one block of memory, a search reads only $O(\log_Bn)$ blocks instead of $O(\log_2n)$, which is why B-trees are used for databases and file systems (see @sec-cs-models-of-computation-cache-oblivious-algorithms).
