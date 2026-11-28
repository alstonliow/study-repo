---
title: "Succinct Binary Tries and Balanced Parentheses"
sources: [mit6851-17]
requires: [cs/data-structure-models/rank-and-select]
aliases: [cs/advanced-data-structures/succinct-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 17, in our own wording; proofs written out in steps. The example tree is the lecture's; the figure is our own, and the bit string was checked by computation. The survey of other succinct structures in the lecture is only summarised. -->

There are $C_n=\binom{2n}{n}/(n+1)\approx4^n$ binary tries (binary trees) on $n$ nodes, so $\mathrm{OPT}=2n-O(\log n)$ bits. Two encodings reach $2n+o(n)$ bits and still answer navigation queries in $O(1)$ time.

::: {#def-level-order-trie .definition name="Level-order encoding"}

Complete every missing child of a binary trie with an *external* node. Visit all nodes in level order, left to right in each level, and write $1$ for an internal node and $0$ for an external node. A trie with $n$ nodes has $n+1$ external nodes, so the string has $2n+1$ bits.

:::

::: {#exm-succinct-trees-1 .example name="Seven nodes"}

Let $A$ have the left child $B$ and the right child $C$, $B$ a right child $D$, $C$ the children $E$ and $F$, and $D$ a right child $G$. Level order $A;B,C;D,E,F;G$ gives the string $111011101000000$ (the bits $1\,1\,1\,0\,1\,1\,1\,0\,1\,0^6$ for $A,B,C,\cdot,D,E,F,\cdot,G,\cdot\cdots$).

:::

::: {#fig-succinct-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (A) at (0,0) {$A$};
\node[small vertex] (B) at (-1.2,-0.9) {$B$};
\node[small vertex] (C) at (1.2,-0.9) {$C$};
\node[small vertex] (D) at (-0.6,-1.8) {$D$};
\node[small vertex] (E) at (0.6,-1.8) {$E$};
\node[small vertex] (F) at (1.8,-1.8) {$F$};
\node[small vertex] (G) at (0,-2.7) {$G$};
\draw (A)--(B); \draw (A)--(C); \draw (B)--(D); \draw (C)--(E); \draw (C)--(F); \draw (D)--(G);
\foreach \b [count=\i from 0] in {1,1,1,0,1,1,1,0,1,0,0,0,0,0,0} {\draw[cell frame] (-3.75+0.5*\i,-3.9) rectangle +(0.5,0.5); \node[lab] at (-3.5+0.5*\i,-3.65) {$\b$};}
\end{tikzpicture}
\end{center}
```

The trie of @exm-succinct-trees-1 and its level-order bit string; position $p$ of the string belongs to the $p$th node of the level order (internal or external).

:::

::: {#thm-level-order-trie .theorem name="Navigation in the level-order string"}

Number the internal nodes $1,2,\dots$ in level order and the string positions $1,\dots,2n+1$. The children of the $i$th internal node are at the positions $2i$ and $2i+1$. Hence, with $B$ the bit string,

$$
\mathrm{left}(p)=2\operatorname{rank}(p),\qquad \mathrm{right}(p)=2\operatorname{rank}(p)+1,\qquad \mathrm{parent}(p)=\operatorname{select}\bigl(\lfloor p/2\rfloor\bigr),
$$

each in $O(1)$ time using $2n+1$ bits and $o(n)$ extra bits for @thm-rank and @prp-select. Subtree sizes are not available this way.

:::

::: {.proof}

1. Induction on $i$. The root is internal node $1$ at position $1$, and its children come next in level order, at the positions $2$ and $3$.

2. Suppose the children of internal node $i-1$ are at $2i-2$ and $2i-1$. Level order keeps the order of the children the same as the order of the parents (if $u$ precedes $v$ then the children of $u$ precede those of $v$).

3. Between the internal nodes $i-1$ and $i$ in level order there are only external nodes, which have no children. So the children of $i$ come immediately after those of $i-1$: positions $2i$ and $2i+1$.

4. For a position $p$, the node at $p$ has $\operatorname{rank}(p)$ internal nodes up to it, so if it is internal, it is the node number $\operatorname{rank}(p)$ and its children are at $2\operatorname{rank}(p)$ and $+1$; the parent of $p$ is the internal node number $\lfloor p/2\rfloor$, at position $\operatorname{select}(\lfloor p/2\rfloor)$.

:::

For subtree sizes one uses depth-first order. Rotate the trie so that a binary trie becomes a rooted ordered tree: the left child becomes the first child and the right child the next sibling. A depth-first traversal that writes $($ on entering and $)$ on leaving a node turns this tree into a balanced parentheses string.

::: {#def-balanced-parentheses .definition name="Balanced parentheses encoding"}

For a binary trie $v$ with subtrees $L,R$ let $\operatorname{par}(v)=\text{(}\ \operatorname{par}(L)\ \text{)}\ \operatorname{par}(R)$, and $\operatorname{par}(\text{empty})$ the empty string. Writing $1$ for $($ and $0$ for $)$ gives $2n$ bits, which is optimal up to $o(n)$: the three objects binary tries, rooted ordered trees and balanced parentheses strings are counted by the same Catalan number $C_n$ and are in bijection.

:::

In this encoding the operations become:

| trie | rooted ordered tree | parentheses |
|---|---|---|
| node | node | an opening paren together with its matching closing paren |
| left child | first child | the next character, if it is an opening paren |
| right child | next sibling | the character after the matching closing paren, if opening |
| subtree size | node plus its right siblings | half the distance from the opening paren to the enclosing closing paren |

The matching-parenthesis query $\operatorname{match}(i)$ is the only non-trivial operation. A compact structure for it uses $O(n)$ bits and $O(1)$ time (this is the content of one of the problem sets); succinct versions with $o(n)$ extra bits are known (Clark–Munro).

::: {#rmk-succinct-trees-1 .remark name="Other succinct structures"}

The lecture surveys: a static dictionary of $n$ keys from a universe of size $u$ in $\log_2\binom un+o(\cdot)$ bits with $O(1)$ membership; succinct rooted ordered trees in $2n+o(n)$ bits (Clark–Munro); almost succinct $k$-ary tries in about $(\log k+\log e)n$ bits; succinct permutations answering $\pi^k(i)$ queries in $(1+\varepsilon)n\log n$ bits (Munro et al.); and an implicit dynamic search tree with $O(\log n)$ insert, delete and predecessor (Franceschini–Grossi). None is proved here.

:::
