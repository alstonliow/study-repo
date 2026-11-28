---
title: "Splay Trees"
sources: [mit6854-5, mit6854-6]
requires: [cs/data-structures/avl-trees, cs/data-structures/amortized-analysis]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lectures 5 (end) and 6, in our own wording; the example is our own (checked by simulation); proofs written out in steps. -->

A splay tree is a binary search tree that keeps no balance information at all. Every time a node is accessed it is rotated (@def-rotation) all the way to the root, in pairs of rotations chosen so that the path to it is roughly halved. A single operation can cost $\Theta(n)$, but any sequence of operations costs $O(\log n)$ amortized each, and frequently used keys stay near the root.

## Splaying

::: {#def-splay .definition name="Splay step, splay"}

Let $x$ be a node with parent $y$ and, if it exists, grandparent $z$. A *splay step* at $x$ is:

1. *zig:* if $y$ is the root, rotate the edge $xy$;
2. *zig-zig:* if $x$ and $y$ are both left children or both right children, rotate the edge $yz$ first, then the edge $xy$;
3. *zig-zag:* otherwise ($x$ a right child and $y$ a left child, or the mirror image), rotate the edge $xy$, then the edge $xz$.

To *splay* $x$ is to repeat splay steps at $x$ until $x$ is the root.

:::

```{=latex}
\begin{algorithm}
\caption{Splay}
\begin{algorithmic}
\INPUT a node $x$ of a binary search tree
\OUTPUT the same tree with $x$ at the root
\WHILE{$x$ is not the root}
\STATE $y\gets$ parent of $x$
\IF{$y$ is the root}
\STATE rotate $xy$ \COMMENT{zig}
\ELSIF{$x$ and $y$ are children on the same side}
\STATE rotate $y$ with its parent, then rotate $xy$ \COMMENT{zig-zig}
\ELSE
\STATE rotate $xy$, then rotate $x$ with its new parent \COMMENT{zig-zag}
\ENDIF
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

The zig-zig case is what makes splaying different from simply rotating $x$ upwards one edge at a time. On a path $n,n-1,\dots,1$ of left children, single rotations bring $1$ to the root but leave a path of the same height; splaying $1$ roughly halves the depth of every node on the path (see the figure below).

::: {#exm-splay-chain .example name="Splaying the deepest node of a path"}

Take the keys $1,\dots,7$ stored as a path of left children with root $7$. Splaying $1$ makes three zig-zig steps, with $z=3,5,7$ in turn. The result has root $1$, its right child $6$, then $4$ (left child of $6$), $7$ (right child of $6$), and $2,5$ below $4$, $3$ below $2$. The depth of the tree drops from $6$ to $4$. Single rotations would have left a path of depth $6$ with $1$ on top.

:::

::: {#fig-splay-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight, draw=accent] (n0_1) at (0.000,-4.500) {$1$};
\node[small vertex] (n0_2) at (0.420,-3.750) {$2$};
\node[small vertex] (n0_3) at (0.840,-3.000) {$3$};
\node[small vertex] (n0_4) at (1.260,-2.250) {$4$};
\node[small vertex] (n0_5) at (1.680,-1.500) {$5$};
\node[small vertex] (n0_6) at (2.100,-0.750) {$6$};
\node[small vertex] (n0_7) at (2.520,0.000) {$7$};
\draw (n0_7)--(n0_6);
\draw (n0_6)--(n0_5);
\draw (n0_5)--(n0_4);
\draw (n0_4)--(n0_3);
\draw (n0_3)--(n0_2);
\draw (n0_2)--(n0_1);
\node[small vertex, fill=accentLight, draw=accent] (n5_1) at (5.000,0.000) {$1$};
\node[small vertex] (n5_2) at (5.500,-2.250) {$2$};
\node[small vertex] (n5_3) at (6.000,-3.000) {$3$};
\node[small vertex] (n5_4) at (6.500,-1.500) {$4$};
\node[small vertex] (n5_5) at (7.000,-2.250) {$5$};
\node[small vertex] (n5_6) at (7.500,-0.750) {$6$};
\node[small vertex] (n5_7) at (8.000,-1.500) {$7$};
\draw (n5_1)--(n5_6);
\draw (n5_6)--(n5_4);
\draw (n5_6)--(n5_7);
\draw (n5_4)--(n5_2);
\draw (n5_4)--(n5_5);
\draw (n5_2)--(n5_3);
\node[lab] at (1.3,0.6) {path $7,\dots,1$};
\node[lab] at (6.5,0.6) {after splaying $1$};
\draw[->, emph] (3.2,-2.2) -- (4.4,-2.2);
\end{tikzpicture}
\end{center}
```

Splaying the deepest node $1$ of a path of left children: three zig-zig steps bring $1$ to the root and cut the depth from $6$ to $4$.

:::

## Amortized analysis

Give every node $x$ a weight $w(x)>0$, let $s(x)$ be the total weight of the subtree rooted at $x$, its *size*, and $r(x)=\log s(x)$ its *rank*. The potential (@def-potential-method) of the tree is $\Phi=\sum_xr(x)$, and a rotation costs $1$.

::: {#lem-splay-step-cost .lemma name="Cost of a splay step"}

Let a splay step at $x$ change the ranks from $r$ to $r'$. Its amortized cost is at most $3\big(r'(x)-r(x)\big)$ for a zig-zig or zig-zag, and at most $3\big(r'(x)-r(x)\big)+1$ for a zig.

:::

::: {.proof}

1. Only $x$, $y$ (and $z$) change their subtrees, so only their ranks change. After the step $x$ has the old subtree of the top node: $r'(x)=r(y)$ for a zig and $r'(x)=r(z)$ otherwise. Also $r(y)\ge r(x)$ (as $y$ was above $x$) and $r'(y),r'(z)\le r'(x)$ (as they are now below $x$).

2. *zig.* The cost is $1+r'(x)+r'(y)-r(x)-r(y)=1+r'(y)-r(x)\le1+r'(x)-r(x)$, and $r'(x)-r(x)\ge0$, so this is at most $1+3\big(r'(x)-r(x)\big)$.

3. A tool for the other cases: since $\log$ is concave and increasing, if $a+b\le c$ then $\log a+\log b\le2\log(c/2)=2\log c-2$.

4. *zig-zig.* The cost is $2+r'(y)+r'(z)-r(x)-r(y)\le2+r'(x)+r'(z)-2r(x)$. The old subtree of $x$ and the new subtree of $z$ are disjoint and lie inside the new subtree of $x$, so $s(x)+s'(z)\le s'(x)$ and by step 3, $r(x)+r'(z)\le2r'(x)-2$. Substituting $r'(z)\le2r'(x)-r(x)-2$ gives a cost of at most $3r'(x)-3r(x)$.

5. *zig-zag.* The cost is $2+r'(y)+r'(z)-r(x)-r(y)\le2+r'(y)+r'(z)-2r(x)$. Now $y$ and $z$ are the two children of $x$, so $s'(y)+s'(z)\le s'(x)$ and $r'(y)+r'(z)\le2r'(x)-2$. The cost is at most $2r'(x)-2r(x)\le3\big(r'(x)-r(x)\big)$.

:::

::: {#thm-access-lemma .theorem name="Access lemma"}

The amortized cost of splaying a node $x$ in a tree with root $t$ is at most
$$3\big(r(t)-r(x)\big)+1=O\Big(1+\log\frac{s(t)}{s(x)}\Big).$$

:::

::: {.proof}

1. Let the splay consist of $k$ steps and let $r_i(x)$ be the rank of $x$ after step $i$, so $r_0(x)=r(x)$ and $r_k(x)=r(t)$ (at the end $x$ holds the whole tree).

2. Only the last step can be a zig. Adding @lem-splay-step-cost over the steps, the sum telescopes: $\sum_i3\big(r_i(x)-r_{i-1}(x)\big)+1=3\big(r(t)-r(x)\big)+1$.

:::

The weights appear only in the analysis, so one may choose them freely for each bound. With all weights $1$, the size of the root is at most $n$ and every splay costs $O(\log n)$ amortized.

## Operations

Every operation walks down the tree like an ordinary search and then splays the last node it reached. The walk has the same length as the splay, so its cost is charged to the splay.

::: {#def-splay-tree-operations .definition name="Splay tree operations"}

1. `find(k)`: search for $k$ and splay the node found (or the last node visited if $k$ is absent).
2. `find-min`, `find-max`: walk left (right) to the end and splay that node.
3. `join(T1, T2)` when every key of $T_1$ is smaller than every key of $T_2$: splay the maximum of $T_1$, which then has no right child, and hang $T_2$ there.
4. `split(T, k)`: `find(k)`, then cut off the left or right subtree of the new root, depending on whether the root's key is at most $k$.
5. `insert(k)`: split at $k$ and make $k$ a new root with the two parts as its subtrees.
6. `delete(k)`: `find(k)`, remove the root and join its two subtrees.

:::

::: {#thm-splay-sequence .theorem name="Splay trees are balanced on average"}

Any sequence of $m$ operations on a splay tree that never holds more than $n$ keys costs $O\big((m+n)\log n\big)$ in total.

:::

::: {.proof}

1. Take all weights $1$, so every rank lies between $0$ and $\log n$. By @thm-access-lemma each splay costs $O(\log n)$ amortized.

2. Hanging $T_2$ below the root in `join`, or a new root in `insert`, raises only the rank of the root, by at most $\log n$. Cutting off a subtree in `split` or `delete` only lowers ranks. So each operation costs $O(\log n)$ amortized.

3. The actual total cost is the amortized total plus $\Phi_0-\Phi_m$. Each of the at most $n$ nodes contributes at most $\log n$ to $\Phi_0$ and at least $0$ to $\Phi_m$, so $\Phi_0-\Phi_m\le n\log n$.

:::

## Comparison with other search trees

A *static* search tree is one that is never restructured. Suppose only `find` is used, key $i$ being accessed $m_i\ge1$ times.

::: {#thm-splay-static-optimality .theorem name="Static optimality"}

For every static binary search tree $T$ on the same keys, the total cost of the accesses in a splay tree, whatever its initial shape, is at most a constant times their total cost in $T$.

:::

::: {.proof}

1. Let $\ell(i)\ge1$ be the number of nodes on the path from the root of $T$ to $i$; the cost of the accesses in $T$ is $\sum_i\ell(i)m_i$.

2. Choose the weights $w(i)=3^{-\ell(i)}$. $T$ has at most $2^{d-1}$ nodes at depth $\ell=d$, so the total weight is at most $\sum_{d\ge1}2^{d-1}3^{-d}=1$. By @thm-access-lemma an access to $i$ costs $O\big(1+\log(1/3^{-\ell(i)})\big)=O\big(\ell(i)\big)$ amortized, $O\big(\sum_i\ell(i)m_i\big)$ in all.

3. The drop of potential over the whole sequence is at most $\sum_i\big(\log1-\log w(i)\big)=\sum_i\ell(i)\log3$, since every size lies between $w(i)$ and $1$. As $m_i\ge1$ this is $O\big(\sum_i\ell(i)m_i\big)$ as well.

:::

::: {#rmk-splay-trees-1 .remark name="Dynamic optimality and sequential access"}

The *dynamic optimality conjecture* (Sleator and Tarjan, 1985) says more: that splay trees are within a constant factor of every binary search tree that may rotate between accesses, even one that knows the access sequence in advance. It is still open. A known special case: accessing all keys $1,2,\dots,n$ in increasing order costs $O(n)$, whatever the initial tree (the *scanning theorem*).

:::
