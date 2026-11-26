---
title: "Dynamic Programming on Trees"
sources: [cs97si-4]
requires: [cs/algorithm-design/subproblem-design]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 4 (tree DP), in our own wording; proofs written out in steps. The example and figure are our own; values checked by computation. -->

In a rooted tree the natural subproblems are the subtrees. Once the choice at a vertex is fixed, the subtrees of its children are independent, so a subproblem keeps the vertex and a small *state* (here: whether the vertex is taken) and the relation sums over the children. A DFS that finishes each vertex after its children gives the order.

An *independent set* of a graph is a set of vertices no two of which are adjacent. In general graphs a maximum one is NP-hard to find (@thm-independent-set-np-complete); in trees it takes linear time.

::: {#exm-tree-dp-independent-set .example name="Maximum independent set in a tree"}

Given a tree with $n$ vertices, find the size of a largest independent set. Root the tree at any vertex $r$ and let $\operatorname{ch}(v)$ be the children of $v$.

1. *Subproblems:* for each vertex $v$, $B(v)$ = the largest independent set of the subtree of $v$ that contains $v$, and $W(v)$ = the largest one that does not contain $v$.
2. *Relation:* if $v$ is taken its children are not, and otherwise each child is free:
   $$B(v)=1+\sum_{u\in\operatorname{ch}(v)}W(u),\qquad W(v)=\sum_{u\in\operatorname{ch}(v)}\max\{B(u),W(u)\}.$$
3. *Order:* children before parents, for example the DFS finishing order (@def-dfs).
4. *Base:* a leaf has $B=1$, $W=0$ (the empty sums are $0$).
5. *Original:* $\max\{B(r),W(r)\}$; recording which term gave each maximum recovers a set.
6. *Time:* each vertex is handled once and each edge appears in one sum, so $O(n)$.

:::

```{=latex}
\begin{algorithm}
\caption{Maximum independent set in a tree}
\begin{algorithmic}
\INPUT A tree as adjacency lists, a root $r$
\OUTPUT The size of a maximum independent set
\STATE \textbf{function} $\mathrm{solve}(v,\mathit{parent})$
\STATE \quad $B(v)\gets1$; $W(v)\gets0$
\FOR{$u\in\operatorname{Adj}(v)$ with $u\ne\mathit{parent}$}
    \STATE $\mathrm{solve}(u,v)$
    \STATE $B(v)\gets B(v)+W(u)$; $W(v)\gets W(v)+\max\{B(u),W(u)\}$
\ENDFOR
\STATE $\mathrm{solve}(r,\text{none})$
\RETURN $\max\{B(r),W(r)\}$
\end{algorithmic}
\end{algorithm}
```

::: {#lem-tree-dp-independent-set .lemma name="Why the relation is right"}

$B(v)$ and $W(v)$ as given by the relation are the sizes of the largest independent sets of the subtree of $v$ that contain, respectively avoid, $v$.

:::

::: {.proof}

1. Induct on the height of $v$. A leaf's subtree is $\{v\}$, so $B=1$ and $W=0$.

2. Let $S$ be an independent set of the subtree of $v$, and $S_u$ its part in the subtree of the child $u$. The subtrees of different children are joined only through $v$, so $S$ is independent exactly when every $S_u$ is independent and, if $v\in S$, no child $u$ is in $S$.

3. *Taking $v$.* Then each $S_u$ is an independent set avoiding $u$, of size at most $W(u)$, and any such choices combine. So the best size is $1+\sum W(u)$.

4. *Avoiding $v$.* Then each $S_u$ is any independent set of the subtree of $u$, of size at most $\max\{B(u),W(u)\}$, and any choices combine. So the best size is $\sum\max\{B(u),W(u)\}$.

:::

::: {#fig-tree-dp-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=1.05cm, every node/.style={small vertex},
  level 1/.style={sibling distance=3.6cm}, level 2/.style={sibling distance=1.6cm}, level 3/.style={sibling distance=1.1cm}]
\node[fill=accentLight] (1) {$1$}
  child {node (2) {$2$}
    child {node[fill=accentLight] (4) {$4$} child {node (7) {$7$} child {node[fill=accentLight] (10) {$10$}}} child {node (8) {$8$}}}
    child {node[fill=accentLight] (5) {$5$}}}
  child {node (3) {$3$}
    child {node (6) {$6$} child {node[fill=accentLight] (9) {$9$}}}};
\foreach \v/\b/\w/\a in {1/5/5/right,2/3/3/left,3/2/1/right,4/2/2/left,5/1/0/right,6/1/1/right,7/1/1/left,8/1/0/right,9/1/0/right,10/1/0/right}
  \node[lab,tick,\a=3pt] at (\v) {$\b|\w$};
\end{tikzpicture}
\end{center}
```

@exm-tree-dp-independent-set on a tree rooted at $1$; each vertex is labelled $B(v)|W(v)$. For example $B(1)=1+W(2)+W(3)=1+3+1=5$. The highlighted set $\{1,4,5,9,10\}$ is a maximum independent set of size $5$.

:::

::: {#rmk-tree-dp-1 .remark name="Other tree DPs"}

The same shape solves minimum vertex cover and minimum dominating set on trees (more states per vertex), subtree sizes and sums of distances (a second pass from the root down, "rerooting"), and knapsack-like choices on trees (the children are merged one by one, like the items of a knapsack). Deep trees can overflow the call stack; an explicit stack or processing vertices in reverse BFS order avoids recursion.

:::
