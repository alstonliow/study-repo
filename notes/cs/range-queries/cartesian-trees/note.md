---
title: "Cartesian Trees"
sources: [mit6851-15]
requires: [cs/data-structures/binary-trees, cs/data-structures/stacks-and-queues]
aliases: [cs/advanced-data-structures/cartesian-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 15, in our own wording; proofs written out in steps. The example is the lecture's array, the figure is our own. -->

A Cartesian tree turns an array into a binary tree in which "smallest element of a range" becomes "lowest common ancestor", so range-minimum queries can be answered by tree methods and the other way round.

::: {#def-cartesian-tree .definition name="Cartesian tree"}

Let $A[0..n-1]$ be an array. Its *Cartesian tree* is the binary tree on the positions $0,\dots,n-1$ defined recursively: the root is a position $m$ with $A[m]=\min A$ (the leftmost one if there are ties), its left subtree is the Cartesian tree of $A[0..m-1]$ and its right subtree is the Cartesian tree of $A[m+1..n-1]$.

An in-order walk of the tree lists the positions $0,1,\dots,n-1$, and every node has a value no larger than the values in its subtree (the tree is a min-heap on the values).

:::

::: {#exm-cartesian-trees-1 .example name="Eight numbers"}

For $A=[8,7,2,8,6,9,4,5]$ the minimum $2$ at position $2$ is the root. The left part $[8,7]$ gives $7$ (with child $8$), the right part $[8,6,9,4,5]$ gives $4$, whose left part $[8,6,9]$ gives $6$ with children $8,9$, and whose right part $[5]$ is a leaf.

:::

::: {#fig-cartesian-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (p2) at (1.4,0) {$2$};
\node[small vertex] (p1) at (0.7,-0.9) {$7$};
\node[small vertex] (p6) at (4.2,-0.9) {$4$};
\node[small vertex] (p0) at (0,-1.8) {$8$};
\node[small vertex] (p4) at (2.8,-1.8) {$6$};
\node[small vertex] (p7) at (4.9,-1.8) {$5$};
\node[small vertex] (p3) at (2.1,-2.7) {$8$};
\node[small vertex] (p5) at (3.5,-2.7) {$9$};
\draw (p2)--(p1); \draw (p2)--(p6); \draw (p1)--(p0); \draw (p6)--(p4); \draw (p6)--(p7); \draw (p4)--(p3); \draw (p4)--(p5);
\foreach \i/\v in {0/8,1/7,2/2,3/8,4/6,5/9,6/4,7/5}
  \node[lab,tick] at (0.7*\i,-3.5) {$\v$};
\end{tikzpicture}
\end{center}
```

The Cartesian tree of $A=[8,7,2,8,6,9,4,5]$; each node sits above its position in the array (bottom row).

:::

::: {#thm-cartesian-range-minimum .theorem name="Range minimum is a lowest common ancestor"}

For positions $i\le j$ the position of the leftmost minimum of $A[i..j]$ is $\operatorname{lca}(i,j)$ in the Cartesian tree of $A$.

:::

::: {.proof}

1. Let $c=\operatorname{lca}(i,j)$. In-order position is monotone along the tree, so $i\le c\le j$: $i$ lies in the left subtree of $c$ (or equals $c$) and $j$ in its right subtree (or equals $c$); otherwise both would lie in one child subtree, contradicting that $c$ is the lowest common ancestor.

2. The subtree of $c$ is a contiguous block of positions containing $i$ and $j$, hence all of $A[i..j]$; and $A[c]$ is the minimum of that block. So $A[c]$ is a minimum of $A[i..j]$ with $c\in[i,j]$.

3. $c$ is the leftmost minimum: a smaller-index position $c'\in[i,c)$ with $A[c']=A[c]$ would lie in the left subtree of $c$ and so have been preferred to $c$ as the leftmost minimum of the block.

:::

::: {#thm-cartesian-linear .theorem name="Linear-time construction"}

The Cartesian tree of $A$ is built in $O(n)$ time with a stack that holds the right spine of the tree built so far.

:::

```{=latex}
\begin{algorithm}
\caption{Cartesian tree by a stack}
\begin{algorithmic}
\INPUT Array $A[0..n-1]$
\OUTPUT Children $\mathrm{left}[\cdot],\mathrm{right}[\cdot]$ and the root
\STATE $S\gets$ empty stack of positions
\FOR{$i=0$ \TO $n-1$}
    \STATE $\mathit{last}\gets\textsc{nil}$
    \WHILE{$S$ not empty \AND $A[\mathrm{top}(S)]>A[i]$}
        \STATE $\mathit{last}\gets\mathrm{pop}(S)$
    \ENDWHILE
    \STATE $\mathrm{left}[i]\gets\mathit{last}$
    \IF{$S$ not empty}
        \STATE $\mathrm{right}[\mathrm{top}(S)]\gets i$
    \ENDIF
    \STATE push $i$ on $S$
\ENDFOR
\RETURN bottom of $S$ as the root
\end{algorithmic}
\end{algorithm}
```

::: {.proof}

1. *Invariant.* After step $i-1$ the stack holds the right spine of the Cartesian tree of $A[0..i-1]$, root at the bottom, with values increasing from bottom to top (equal values stay in order because only strictly larger values are popped).

2. *Step $i$.* The new position is the rightmost one, so it ends up on the right spine of the new tree. The spine nodes with value larger than $A[i]$ are exactly those popped; the last popped one (the highest of them) becomes the left child of $i$, and $i$ becomes the right child of the node now on top of the stack, which replaces the old right child.

3. *Cost.* Every position is pushed once and popped at most once, so all the loops together do $O(n)$ work.

:::

The tie rule matters only for uniqueness; any rule gives a tree in which @thm-cartesian-range-minimum returns *a* minimum. The map from the array to the tree keeps only the relative order of values, which is why the next note can assume the values are small integers.
