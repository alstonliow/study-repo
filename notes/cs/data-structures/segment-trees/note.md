---
title: "Segment Trees"
sources: []
requires: [cs/data-structures/interfaces]
status: draft
---

<!-- Added 2026-11-26 for the CSES range-query problems, in our own wording. TODO: add a source once the owner picks a lecture or textbook reference. -->

A Fenwick tree (@sec-cs-data-structures-fenwick-trees) needs an invertible operation such as $+$. A *segment tree* works for any associative operation $\star$ (sum, minimum, maximum, gcd, matrix product), and it is the usual tool for "update one entry, query a range".

::: {#def-segment-tree .definition name="Segment tree"}

Let $a_0,\dots,a_{n-1}$ be values in a set with an associative operation $\star$. The segment tree is a binary tree whose leaves are $a_0,\dots,a_{n-1}$ and in which each internal node $v$ stores $s(v)=s(\text{left})\star s(\text{right})$, the value of $\star$ over the interval of positions below $v$. The root covers $[0,n-1]$, and a node covering $[l,r]$ with $l<r$ has children covering $[l,m]$ and $[m+1,r]$, where $m=\lfloor (l+r)/2\rfloor$. Operations:

- $\operatorname{update}(i,x)$: set $a_i\gets x$, then recompute the stored values on the path from leaf $i$ to the root;
- $\operatorname{query}(i,j)$: return $a_i\star\dots\star a_j$, found by descending from the root: a node whose interval lies inside $[i,j]$ returns its stored value, a node whose interval is disjoint from $[i,j]$ returns the neutral element, and any other node combines the answers of its two children.

:::

::: {#thm-segment-tree .theorem name="Segment tree"}

The tree has at most $2n-1$ nodes and height $\lceil\log_2 n\rceil$, it is built in $O(n)$ time, and both $\operatorname{update}$ and $\operatorname{query}$ take $O(\log n)$ time.

:::

::: {.proof}

1. *Size and build.* A binary tree with $n$ leaves in which every internal node has two children has $n-1$ internal nodes. Each stored value is one application of $\star$ to the values of the children, so the build is $O(n)$.

2. *Height.* A node of height $h$ covers at most $\lceil n/2^{\,d}\rceil$ positions at depth $d$, so after $\lceil\log_2 n\rceil$ halvings an interval has length $1$.

3. *Update.* Only the nodes whose interval contains $i$ change, and these form one root-to-leaf path, which has at most $\lceil\log_2 n\rceil+1$ nodes.

4. *Query correctness.* The nodes returning a stored value are *maximal* nodes inside $[i,j]$, because their parent was split. Their intervals are disjoint and their union is $[i,j]$, and associativity lets us combine them left to right, so the result is $a_i\star\dots\star a_j$.

5. *Query time.* At each depth at most two nodes are split: a node is split only if its interval contains an endpoint of $[i,j]$ strictly inside it, and each of the two endpoints lies in one node per depth. So at most four nodes are visited per depth, giving $O(\log n)$.

:::

::: {#exm-segment-trees-1 .example name="Range minimum"}

For $a=(5,3,8,1,4,7,2,6)$ with $\star=\min$ the stored values are $3,1,4,2$ on the level above the leaves, $1,2$ above them, and $1$ at the root. The query $\operatorname{query}(2,6)$ uses the maximal nodes $[2,3]$, $[4,5]$ and $[6,6]$, with values $1$, $4$ and $2$, so the answer is $1$.

:::

::: {#fig-segment-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.9cm]
\foreach \i/\v in {0/5,1/3,2/8,3/1,4/4,5/7,6/2,7/6} {
  \draw[cell frame] (\i,0) rectangle +(0.9,0.6); \node[lab] at (\i+0.45,0.3) {$\v$};
}
\foreach \i/\v in {0/3,2/1,4/4,6/2} {
  \draw[cell frame] (\i,1) rectangle +(1.9,0.6); \node[lab] at (\i+0.95,1.3) {$\v$};
}
\foreach \i/\v in {0/1,4/2} {
  \draw[cell frame] (\i,2) rectangle +(3.9,0.6); \node[lab] at (\i+1.95,2.3) {$\v$};
}
\draw[cell frame] (0,3) rectangle +(7.9,0.6); \node[lab] at (3.95,3.3) {$1$};
\draw[hl cell] (2,1) rectangle +(1.9,0.6);
\draw[hl cell] (4,1) rectangle +(1.9,0.6);
\draw[hl cell] (6,0) rectangle +(0.9,0.6);
\end{tikzpicture}
\end{center}
```

@exm-segment-trees-1: one row per level, each box labelled with the minimum of the positions it covers. The three highlighted boxes are the maximal nodes of $\operatorname{query}(2,6)$.

:::

::: {#rmk-segment-trees-1 .remark name="Implementation and uses"}

A segment tree is usually stored in an array of size $2N$ (with $N$ a power of two) where node $v$ has children $2v$ and $2v+1$. A node can store more than one number, so that one tree answers harder queries: for the maximum subarray sum, each node keeps the pair (total, best prefix, best suffix, best subarray), which is combined associatively. Descending the tree also finds, in $O(\log n)$, the first position whose value is at least a threshold (store maxima). Range *updates* need lazy propagation (@sec-cs-data-structures-lazy-propagation).

:::
