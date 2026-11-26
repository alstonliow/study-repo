---
title: "Link-Cut Trees (Dynamic Trees)"
sources: [mit6854-7, mit6854-8]
requires: [cs/advanced-data-structures/splay-trees]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lectures 7 and 8, in our own wording; proofs written out in steps. The lecture orders each splay tree from the deepest node to the top; we use the mirror image (in-order = from the top down), which is the usual convention today. -->

*Dynamic trees* (Sleator and Tarjan), also called *link-cut trees*, maintain a forest of rooted trees under linking and cutting, together with a cost on every node, and answer questions about the path from a node to its root. Every operation takes $O(\log n)$ amortized time. They give the fastest known bounds for several flow algorithms, for example the cancel step of @def-cancel-and-tighten.

## The interface

Write $p(v)$ for the parent of $v$. In flow algorithms the cost of $v$ is the residual capacity of the edge $(p(v),v)$, and a root has cost $+\infty$.

::: {#def-dynamic-tree-operations .definition name="Dynamic tree operations"}

1. `make-tree(v)`: a new one-node tree with cost $+\infty$.
2. `find-root(v)`: the root of the tree containing $v$.
3. `find-cost(v)`: the cost of $v$.
4. `find-min(v)`: the node of least cost on the path from $v$ to its root (ties go to the node nearest the root).
5. `add-cost(v, x)`: add $x$ to the cost of every node on the path from the root to $v$.
6. `cut(v)`: remove the edge from $v$ to its parent; $v$ becomes a root, of cost $+\infty$.
7. `link(v, w, x)`: if $w$ is a root of another tree, make $v$ the parent of $w$ and set the cost of $w$ to $x$.

:::

Storing each tree with parent pointers makes `link` and `cut` cheap but path queries cost the depth. The data structure below cuts every tree into paths and keeps each path in a splay tree.

## Representation

::: {#def-virtual-tree .definition name="Solid paths, virtual tree"}

Partition every rooted tree into vertex-disjoint downward paths: each node has at most one *solid* child edge, the other child edges are *dashed*. The *virtual tree* stores

1. each solid path in its own splay tree, ordered by depth (in-order = from the top of the path down);
2. for each splay tree, a *path-parent* pointer from its root to the parent, in the real tree, of the top node of the path.

So a node has a left and a right child in its splay tree and any number of *middle children*, the roots of the splay trees hanging off it by path-parent pointers.

:::

Rotations inside a splay tree change neither the in-order nor the path, so they do not change the real tree. Neither does *splicing*: if $w$ is the root of its splay tree and $v$ is a middle child of $w$, exchange the right subtree of $w$ (the part of $w$'s path below $w$) with $v$'s splay tree. The path through $w$ now continues into $v$'s path, and the old lower part hangs from $w$ as a middle child.

::: {#def-expose .definition name="Expose"}

`expose(v)` makes the path from the root of $v$'s tree to $v$ one solid path, kept in one splay tree whose root is $v$ and which holds nothing below $v$:

1. Walk from $v$ up to the root of the virtual tree, splaying each node at which the walk enters a new splay tree. Afterwards $v$ is joined to the virtual root by middle edges only.
2. Walk up again and splice at each middle edge, so the whole way up is solid.
3. Splay $v$ in the single splay tree that now holds the path; finally make $v$'s right subtree a middle child, so the path ends at $v$.

:::

::: {#fig-link-cut-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (L0a) at (2.00,0.00) {$a$};
\node[small vertex] (L0b) at (1.00,-1.00) {$b$};
\node[small vertex] (L0c) at (3.00,-1.00) {$c$};
\node[small vertex] (L0d) at (0.50,-2.00) {$d$};
\node[small vertex] (L0e) at (1.50,-2.00) {$e$};
\node[small vertex] (L0f) at (3.00,-2.00) {$f$};
\node[small vertex] (L0g) at (0.50,-3.00) {$g$};
\node[small vertex] (L0h) at (1.50,-3.00) {$h$};
\draw[faint, dashed] (L0a)--(L0b);
\draw[emph] (L0a)--(L0c);
\draw[emph] (L0b)--(L0d);
\draw[faint, dashed] (L0b)--(L0e);
\draw[emph] (L0c)--(L0f);
\draw[emph] (L0d)--(L0g);
\draw[emph] (L0e)--(L0h);
\node[small vertex] (L5a) at (7.00,0.00) {$a$};
\node[small vertex] (L5b) at (6.00,-1.00) {$b$};
\node[small vertex] (L5c) at (8.00,-1.00) {$c$};
\node[small vertex] (L5d) at (5.50,-2.00) {$d$};
\node[small vertex] (L5e) at (6.50,-2.00) {$e$};
\node[small vertex] (L5f) at (8.00,-2.00) {$f$};
\node[small vertex] (L5g) at (5.50,-3.00) {$g$};
\node[small vertex, fill=accentLight, draw=accent] (L5h) at (6.50,-3.00) {$h$};
\draw[emph] (L5a)--(L5b);
\draw[faint, dashed] (L5a)--(L5c);
\draw[faint, dashed] (L5b)--(L5d);
\draw[emph] (L5b)--(L5e);
\draw[emph] (L5c)--(L5f);
\draw[emph] (L5d)--(L5g);
\draw[emph] (L5e)--(L5h);
\node[lab] at (2,0.6) {before};
\node[lab] at (7,0.6) {after \texttt{expose(h)}};
\end{tikzpicture}
\end{center}
```

A rooted tree cut into solid paths (thick; dashed edges are not on a path). After \texttt{expose(h)} the whole path from the root $a$ to $h$ is one solid path, kept in one splay tree; the old solid edge $a$–$c$ became dashed.

:::

```{=latex}
\begin{algorithm}
\caption{Expose (access) in a link-cut tree}
\begin{algorithmic}
\INPUT a node $v$
\OUTPUT $v$ is the root of the splay tree of the solid path from its tree's root to $v$
\STATE $last\gets$ none; $u\gets v$
\WHILE{$u\ne$ none}
\STATE splay $u$ in its splay tree
\STATE make the right subtree of $u$ a middle child of $u$; set the right child of $u$ to $last$ \COMMENT{splice}
\STATE $last\gets u$; $u\gets$ path-parent of $u$
\ENDWHILE
\STATE splay $v$
\end{algorithmic}
\end{algorithm}
```

The pseudocode interleaves steps 1 and 2 and cuts off what lies below $v$ in the first round; this is the usual way to implement expose and does the same work.

## Keeping costs

Costs are stored as differences, so that `add-cost` on a whole path is a constant-time change. For a node $x$ of a splay tree let $\operatorname{mincost}(x)$ be the least cost in its splay subtree, and store
$$\Delta\operatorname{cost}(x)=\begin{cases}\operatorname{cost}(x)&x\text{ the root of its splay tree},\\\operatorname{cost}(x)-\operatorname{cost}(\text{splay parent of }x)&\text{otherwise},\end{cases}\qquad\Delta\min(x)=\operatorname{cost}(x)-\operatorname{mincost}(x).$$

::: {#prp-link-cut-cost-update .proposition name="Local updates"}

With left child $l$ and right child $r$ (missing children omitted),
$$\Delta\min(x)=\max\big(0,\ \Delta\min(l)-\Delta\operatorname{cost}(l),\ \Delta\min(r)-\Delta\operatorname{cost}(r)\big),$$
and a rotation or a splice changes $\Delta\operatorname{cost}$ and $\Delta\min$ only at the $O(1)$ nodes whose splay parent or children change. So both are kept in $O(1)$ time per rotation or splice.

:::

::: {.proof}

1. $\operatorname{mincost}(x)=\min\big(\operatorname{cost}(x),\operatorname{mincost}(l),\operatorname{mincost}(r)\big)$, so $\Delta\min(x)=\max\big(0,\operatorname{cost}(x)-\operatorname{mincost}(l),\operatorname{cost}(x)-\operatorname{mincost}(r)\big)$.

2. $\operatorname{cost}(x)-\operatorname{mincost}(l)=\big(\operatorname{cost}(l)-\operatorname{mincost}(l)\big)-\big(\operatorname{cost}(l)-\operatorname{cost}(x)\big)=\Delta\min(l)-\Delta\operatorname{cost}(l)$, and the same for $r$.

3. A rotation at the edge $vw$ ($v$ the child) changes the splay parents of $v$, $w$ and of one subtree root $b$ that moves from $v$ to $w$. Their new differences are sums of old ones: the new $\Delta\operatorname{cost}(v)$ is $\Delta\operatorname{cost}(v)+\Delta\operatorname{cost}(w)$, the new $\Delta\operatorname{cost}(w)$ is $-\Delta\operatorname{cost}(v)$, and the new $\Delta\operatorname{cost}(b)$ is $\Delta\operatorname{cost}(b)+\Delta\operatorname{cost}(v)$. Then recompute $\Delta\min$ at $w$ and then $v$ by step 1. A splice is the same kind of change.

:::

::: {#def-link-cut-implementation .definition name="Implementing the operations"}

1. `find-cost(v)`: expose $v$; return $\Delta\operatorname{cost}(v)$.
2. `find-root(v)`: expose $v$, walk to the leftmost node of its splay tree, splay it and return it.
3. `find-min(v)`: expose $v$ and walk down from $v$, going to the child that attains the maximum in @prp-link-cut-cost-update until $\Delta\min$ is $0$ at the current node; splay it and return it.
4. `add-cost(v, x)`: expose $v$ and add $x$ to $\Delta\operatorname{cost}(v)$ (the whole path is $v$'s splay tree).
5. `cut(v)`: expose $v$ and detach its left subtree (the part of the path above $v$), adjusting the stored differences.
6. `link(v, w, x)`: expose $w$ and $v$, then hang $w$ below $v$ as a middle child with $\Delta\operatorname{cost}(w)=x$.

:::

## Analysis

::: {#thm-link-cut-trees .theorem name="Link-cut trees"}

Any sequence of $m$ dynamic tree operations on $n$ nodes takes $O\big((m+n)\log n\big)$ time.

:::

::: {.proof}

1. Let $s(x)$ be the number of nodes in the subtree of $x$ in the *whole virtual tree* (middle children included), $r(x)=\log s(x)$, and $\Phi=3\sum_xr(x)$, three times the potential of @thm-access-lemma.

2. *Step 1 of expose.* Let it splay $k$ nodes $u_1=v,u_2,\dots,u_k$, each $u_{i+1}$ being the path-parent of the splay root $t_i$ above $u_i$. Middle children do not affect the access lemma, so with the factor $3$ the splay of $u_i$ costs at most $9\big(r(t_i)-r(u_i)\big)+1$. Since $t_i$ hangs below $u_{i+1}$, $r(t_i)\le r(u_{i+1})$, and the sum telescopes to at most $9\big(r(\text{root})-r(v)\big)+k\le9\log n+k$.

3. *Step 2.* Splicing does not change any virtual subtree, so $\Phi$ is unchanged and the cost is $k$.

4. *Step 3.* $v$ is now $k$ levels below the root of one splay tree. Splaying it costs at least $k$ rotations, and by @thm-access-lemma (with the factor $3$) actual cost plus change of $\Phi$ is at most $3\big(3\log n+1\big)$ while the actual cost alone is at least $k$. Because $\Phi$ carries a factor $3$, the amortized cost of this splay is at most $3(3\log n+1)-2k$, which pays for the $2k$ of steps 1 and 2. Detaching the part below $v$ only lowers ranks. So `expose` costs $O(\log n)$ amortized.

5. Every operation is one or two exposes plus a walk that is charged to a splay. `cut` only lowers ranks. `link` raises only the rank of $v$, by at most $\log n$. So every operation costs $O(\log n)$ amortized.

6. Finally $0\le\Phi\le3n\log n$, so the actual total exceeds the amortized total by at most $O(n\log n)$.

:::

::: {#rmk-link-cut-trees-1 .remark name="Uses"}

Link-cut trees give an $O(mn\log n)$ maximum flow algorithm (Dinic's blocking flows with dynamic trees), the cancel step of @def-cancel-and-tighten in $O(m\log n)$, and online connectivity in forests. In programming contests they are usually written with `access` (= expose) and a reversal flag that allows re-rooting a tree (`make-root`), which turns the rooted interface into one for unrooted trees.

:::
