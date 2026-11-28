---
title: "Lowest Common Ancestor by Binary Lifting"
sources: [cs97si-3]
requires: [math/discrete/graph/trees, cs/graph-algorithms/depth-first-search]
aliases: [cs/advanced-data-structures/lowest-common-ancestor]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 3, in our own wording; proofs written out in steps. The example and figures are our own. -->

In a rooted tree, the *lowest common ancestor* $\operatorname{lca}(u,v)$ of two vertices is the deepest vertex that is an ancestor of both (a vertex counts as its own ancestor). Binary lifting stores, for every vertex, its ancestors at distances $1,2,4,\dots$, and answers each query in $O(\log n)$.

::: {#def-binary-lifting .definition name="Binary lifting table"}

Let $T$ be a tree with $n$ vertices and root $r$, let $d(v)$ be the depth of $v$ ($d(r)=0$) and $p(v)$ its parent, with $p(r)=r$. For $k\ge0$ let

$$
A[v][0]=p(v),\qquad A[v][k]=A\bigl[A[v][k-1]\bigr][k-1],
$$

so $A[v][k]$ is the ancestor of $v$ at distance $2^k$ (or $r$ if the tree is not that deep). The table has $K=\lceil\log_2 n\rceil+1$ columns and is filled column by column after one DFS from $r$ that computes $d$ and $p$.

:::

To answer $\operatorname{lca}(u,v)$ with $d(u)\ge d(v)$: lift $u$ by $d(u)-d(v)$, using the binary digits of that number; if now $u=v$, that is the answer. Otherwise, for $k=K-1,\dots,0$, replace $(u,v)$ by $(A[u][k],A[v][k])$ whenever these differ. Finally return $p(u)$.

```{=latex}
\begin{algorithm}
\caption{LCA query by binary lifting}
\begin{algorithmic}
\INPUT Table $A$, depths $d$, vertices $u,v$
\OUTPUT $\operatorname{lca}(u,v)$
\IF{$d(u)<d(v)$}
    \STATE swap $u$ and $v$
\ENDIF
\FOR{$k=K-1$ \TO $0$ step $-1$}
    \IF{$d(u)-2^k\ge d(v)$}
        \STATE $u\gets A[u][k]$ \COMMENT{now $d(u)=d(v)$ at the end}
    \ENDIF
\ENDFOR
\IF{$u=v$}
    \RETURN $u$
\ENDIF
\FOR{$k=K-1$ \TO $0$ step $-1$}
    \IF{$A[u][k]\ne A[v][k]$}
        \STATE $u\gets A[u][k]$; $v\gets A[v][k]$
    \ENDIF
\ENDFOR
\RETURN $p(u)$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-binary-lifting .theorem name="Binary lifting"}

The table takes $O(n\log n)$ time and space to build, and each query returns $\operatorname{lca}(u,v)$ in $O(\log n)$ time.

:::

::: {.proof}

1. *Table.* The ancestor at distance $2^k$ is the ancestor at distance $2^{k-1}$ of the ancestor at distance $2^{k-1}$, which is the recurrence; each of the $nK$ entries costs $O(1)$.

2. *Equal depths.* The first loop subtracts the powers $2^k$ of the binary expansion of $d(u)-d(v)$, largest first, so it moves $u$ to its ancestor at depth $d(v)$. The ancestors of the original $u$ at depth $\ge d(v)$ include the lca, so the lca of the new pair is the same.

3. *Same vertex.* If now $u=v$, then $v$ is an ancestor of the original $u$ and the answer is $v$.

4. *Second loop.* Let $c=\operatorname{lca}(u,v)$ and $h=d(u)-d(c)\ge1$; the depths of $u$ and $v$ are equal. Their ancestors at the same depth coincide exactly when that depth is $\le d(c)$, so $A[u][k]\ne A[v][k]$ exactly when $2^k<h$ (with $A$ capped at the root, a jump of $2^k\ge h$ always lands on a common ancestor). The loop therefore jumps by $2^k$ exactly when $2^k\le h-1$, for $k$ from large to small, which subtracts the binary digits of $h-1$ and leaves $h=1$.

5. After the loop $u$ and $v$ are distinct vertices at depth $d(c)+1$, so their common parent is $c$.

6. *Query time.* Two loops of $K=O(\log n)$ steps.

:::

::: {#exm-lowest-common-ancestor-1 .example name="Ten vertices"}

Root the tree with edges $1\text{-}2$, $1\text{-}3$, $2\text{-}4$, $2\text{-}5$, $3\text{-}6$, $4\text{-}7$, $4\text{-}8$, $6\text{-}9$, $7\text{-}10$ at $1$. Then $A[10]=(7,4,1)$ and $A[9]=(6,3,1)$. For $\operatorname{lca}(10,5)$: $d(10)=4$, $d(5)=2$, so lift $10$ by $2$ to $4$; then $A[4][0]=A[5][0]=2$, so nothing moves and the answer is $p(4)=2$. For $\operatorname{lca}(10,9)$: lift $10$ by $1$ to $7$; $A[7][1]=2\ne3=A[9][1]$ moves the pair to $(2,3)$, and the answer is $p(2)=1$.

:::

::: {#fig-lowest-common-ancestor-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=1.05cm, every node/.style={small vertex},
  level 1/.style={sibling distance=3.4cm}, level 2/.style={sibling distance=1.5cm}, level 3/.style={sibling distance=1.1cm}]
\node (1) {$1$}
  child {node[fill=accentLight] (2) {$2$}
    child {node (4) {$4$} child {node (7) {$7$} child {node[draw=accent] (10) {$10$}}} child {node (8) {$8$}}}
    child {node[draw=accent] (5) {$5$}}}
  child {node (3) {$3$}
    child {node (6) {$6$} child {node (9) {$9$}}}};
\draw[->,hl] (10) to[bend left=40] node[edge label] {$2^1$} (4);
\draw[->,faint,dashed] (10) to[bend right=45] node[edge label] {$2^2$} (1);
\end{tikzpicture}
\end{center}
```

@exm-lowest-common-ancestor-1: one jump $A[10][1]=4$ brings $10$ to the depth of $5$; their parents agree, so $\operatorname{lca}(10,5)=2$. The dashed jump $A[10][2]=1$ is the root.

:::

::: {#rmk-lowest-common-ancestor-1 .remark name="Other methods"}

The same table answers "the ancestor $k$ levels up" in $O(\log n)$ and, with an extra table of edge weights, path maxima or sums. An Euler tour of the tree turns LCA into a range-minimum query on depths, which a sparse table answers in $O(1)$ after $O(n\log n)$ preprocessing; Tarjan's offline method answers a batch of queries with union-find (@sec-cs-data-structures-union-find).

:::
