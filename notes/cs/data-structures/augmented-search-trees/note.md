---
title: "Augmented Search Trees: Order Statistics and Range Trees"
sources: [mit6046-9]
requires: [cs/data-structures/two-three-trees]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 9, in our own wording; proofs written out in steps. Builds on @def-subtree-augmentation. -->

Augmentation (@def-subtree-augmentation) stores at every node a value computed from its subtree. If the value of a node is computed in $O(1)$ time from the node and its children, it can be maintained through rotations in AVL trees and splits and merges in 2-3 trees, at the cost of updating the $O(\log n)$ ancestors of each change.

## Order-statistic trees

::: {#def-order-statistic-tree .definition name="Order-statistic tree"}

An *order-statistic tree* is a balanced binary search tree augmented with subtree sizes. Besides the set operations it supports

1. `rank(x)`: the number of stored keys smaller than $x$, and
2. `select(i)`: the key of rank $i$ (counting from $0$).

:::

::: {#prp-rank-select .proposition name="Rank and select in $O(\log n)$"}

1. `select(i)` from the root: with $n_L$ the size of the left subtree, return the root if $i=n_L$, go left if $i<n_L$, and go right with $i-n_L-1$ if $i>n_L$.
2. `rank(x)` for a node $x$: start with $r$ = size of $x$'s left subtree, and walk up to the root; whenever the step goes from a right child $c$ up to its parent $p$, add the size of $p$'s left subtree plus $1$.

Both take $O(\log n)$ time.

:::

::: {.proof}

1. `select` is @prp-subtree-at with the sorted order as traversal order.

2. For `rank`, the keys smaller than $x$ are those in $x$'s left subtree and, for each ancestor $p$ that has $x$ in its right subtree, $p$ itself and $p$'s left subtree; these are exactly the terms added. Both walks follow one root-to-node path, $O(\log n)$ long.

:::

```{=latex}
\begin{algorithm}
\caption{Select and rank}
\begin{algorithmic}
\STATE \textbf{select}$(i)$: \COMMENT{as in the $i$-th node of a binary tree}
\STATE $X\gets$ root
\WHILE{true}
    \STATE $n_L\gets$ size of $X.\mathrm{left}$
    \IF{$i=n_L$}
        \RETURN $X.\mathrm{key}$
    \ELSIF{$i<n_L$}
        \STATE $X\gets X.\mathrm{left}$
    \ELSE
        \STATE $i\gets i-n_L-1$; $X\gets X.\mathrm{right}$
    \ENDIF
\ENDWHILE
\STATE \textbf{rank}$(x)$: \COMMENT{$x$ a node}
\STATE $r\gets$ size of $x.\mathrm{left}$; $c\gets x$
\WHILE{$c$ is not the root}
    \STATE $p\gets c.\mathrm{parent}$
    \IF{$c=p.\mathrm{right}$}
        \STATE $r\gets r+(\text{size of }p.\mathrm{left})+1$
    \ENDIF
    \STATE $c\gets p$
\ENDWHILE
\RETURN $r$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-augmented-search-trees-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (1) at (0.00,-2.55) {$1$};
\node[lab,tick] at (0.40,-2.33) {1};
\node[small vertex] (2) at (0.62,-1.70) {$2$};
\node[lab,tick] at (1.02,-1.48) {3};
\node[small vertex] (3) at (1.24,-2.55) {$3$};
\node[lab,tick] at (1.64,-2.33) {1};
\node[small vertex] (4) at (1.86,-0.85) {$4$};
\node[lab,tick] at (2.26,-0.63) {7};
\node[small vertex] (5) at (2.48,-2.55) {$5$};
\node[lab,tick] at (2.88,-2.33) {1};
\node[small vertex, fill=accentLight, draw=accent] (6) at (3.10,-1.70) {$6$};
\node[lab,tick] at (3.50,-1.48) {3};
\node[small vertex] (7) at (3.72,-2.55) {$7$};
\node[lab,tick] at (4.12,-2.33) {1};
\node[small vertex] (8) at (4.34,0.00) {$8$};
\node[lab,tick] at (4.74,0.22) {14};
\node[small vertex] (9) at (4.96,-2.55) {$9$};
\node[lab,tick] at (5.36,-2.33) {1};
\node[small vertex] (10) at (5.58,-1.70) {$10$};
\node[lab,tick] at (5.98,-1.48) {3};
\node[small vertex, fill=accentLight, draw=accent] (11) at (6.20,-2.55) {$11$};
\node[lab,tick] at (6.60,-2.33) {1};
\node[small vertex] (13) at (6.82,-0.85) {$13$};
\node[lab,tick] at (7.22,-0.63) {6};
\node[small vertex] (14) at (7.44,-2.55) {$14$};
\node[lab,tick] at (7.84,-2.33) {1};
\node[small vertex] (15) at (8.06,-1.70) {$15$};
\node[lab,tick] at (8.46,-1.48) {2};
\draw[hl] (8)--(4);
\draw[hl, dashed] (8)--(13);
\draw[] (4)--(2);
\draw[hl] (4)--(6);
\draw[hl, dashed] (13)--(10);
\draw[] (13)--(15);
\draw[] (2)--(1);
\draw[] (2)--(3);
\draw[] (6)--(5);
\draw[] (6)--(7);
\draw[] (10)--(9);
\draw[hl, dashed] (10)--(11);
\draw[] (15)--(14);
\node[lab, anchor=west] at (9.00,0.00) {select$(5)$: at $8$, $n_L=7>5$, go left;};
\node[lab, anchor=west] at (9.00,-0.45) {at $4$, $n_L=3<5$: $i=1$, go right;};
\node[lab, anchor=west] at (9.00,-0.90) {at $6$, $n_L=1=i$: answer $6$.};
\node[lab, anchor=west] at (9.00,-1.50) {rank$(11)$: $r=0$; up from right child: $+2$};
\node[lab, anchor=west] at (9.00,-1.95) {(at $10$), then $+0$ (at $13$), $+8$ (at $8$): $r=10$.};
\end{tikzpicture}
\end{center}
```

Select and rank in the tree of @fig-augmented-search-trees-1 (small numbers are subtree sizes). `select(5)` walks down (highlighted edges) comparing $i$ with left subtree sizes. `rank(11)` walks up (dashed edges) and adds the left subtree size plus $1$ each time it steps up from a right child: ten keys, $1,\dots,10$, are smaller than $11$.

:::

Storing the rank itself at each node would not work: inserting a new minimum changes the rank of every key. The size is local, which is what augmentation needs.

## Range trees

A *range query* asks for the keys in an interval $[a,b]$, or for their number.

::: {#prp-one-d-range .proposition name="One-dimensional range queries"}

In a balanced binary search tree augmented with subtree sizes, the number of keys in $[a,b]$ is found in $O(\log n)$ time, and the $k$ keys themselves are listed in $O(\log n+k)$ time.

:::

::: {.proof}

1. Search for $a$ and for $b$; the two paths agree down to a *split node* and then separate.

2. Every key in $[a,b]$ is a node on the two paths or lies in a subtree hanging off the inner side of a path (to the right of the path to $a$ or to the left of the path to $b$). There are $O(\log n)$ such nodes and subtrees, and each whole subtree lies inside $[a,b]$.

3. Counting adds the stored sizes of these subtrees, $O(\log n)$ work; listing visits each subtree in $O(\text{its size})$ time.

:::

```{=latex}
\begin{algorithm}
\caption{Counting the keys in $[a,b]$}
\begin{algorithmic}
\INPUT Search tree with subtree sizes; numbers $a\le b$
\OUTPUT The number of stored keys in $[a,b]$
\RETURN below$(b,\le)-$below$(a,<)$
\STATE \textbf{below}$(x,\prec)$: \COMMENT{the number of keys $k$ with $k\prec x$}
\STATE $r\gets0$; $X\gets$ root
\WHILE{$X$ is not none}
    \IF{$X.\mathrm{key}\prec x$}
        \STATE $r\gets r+(\text{size of }X.\mathrm{left})+1$; $X\gets X.\mathrm{right}$
    \ELSE
        \STATE $X\gets X.\mathrm{left}$
    \ENDIF
\ENDWHILE
\RETURN $r$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-augmented-search-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (k1) at (0.000,-2.550) {$1$};
\node[small vertex] (k2) at (0.620,-1.700) {$2$};
\node[small vertex] (k3) at (1.240,-2.550) {$3$};
\node[small vertex] (k4) at (1.860,-0.850) {$4$};
\node[small vertex, fill=accentLight, draw=accent] (k5) at (2.480,-2.550) {$5$};
\node[small vertex, fill=accentLight, draw=accent] (k6) at (3.100,-1.700) {$6$};
\node[small vertex, fill=accentLight, draw=accent] (k7) at (3.720,-2.550) {$7$};
\node[small vertex, fill=accentLight, draw=accent] (k8) at (4.340,0.000) {$8$};
\node[small vertex, fill=accentLight, draw=accent] (k9) at (4.960,-2.550) {$9$};
\node[small vertex, fill=accentLight, draw=accent] (k10) at (5.580,-1.700) {$10$};
\node[small vertex, fill=accentLight, draw=accent] (k11) at (6.200,-2.550) {$11$};
\node[small vertex] (k13) at (6.820,-0.850) {$13$};
\node[small vertex] (k14) at (7.440,-2.550) {$14$};
\node[small vertex] (k15) at (8.060,-1.700) {$15$};
\draw (k8)--(k4);
\draw (k8)--(k13);
\draw (k4)--(k2);
\draw (k4)--(k6);
\draw (k13)--(k10);
\draw (k13)--(k15);
\draw (k2)--(k1);
\draw (k2)--(k3);
\draw (k6)--(k5);
\draw (k6)--(k7);
\draw (k10)--(k9);
\draw (k10)--(k11);
\draw (k15)--(k14);
\node[lab,tick] at (0.36,-2.33) {1};
\node[lab,tick] at (0.98,-1.48) {3};
\node[lab,tick] at (1.60,-2.33) {1};
\node[lab,tick] at (2.22,-0.63) {7};
\node[lab,tick] at (2.84,-2.33) {1};
\node[lab,tick] at (3.46,-1.48) {3};
\node[lab,tick] at (4.08,-2.33) {1};
\node[lab,tick] at (4.70,0.22) {14};
\node[lab,tick] at (5.32,-2.33) {1};
\node[lab,tick] at (5.94,-1.48) {3};
\node[lab,tick] at (6.56,-2.33) {1};
\node[lab,tick] at (7.18,-0.63) {6};
\node[lab,tick] at (7.80,-2.33) {1};
\node[lab,tick] at (8.42,-1.48) {2};
\end{tikzpicture}
\end{center}
```

A search tree augmented with subtree sizes (small numbers). The keys in $[5,12]$ (highlighted) are the nodes on the two search paths, for $5$ and $12$, plus whole subtrees hanging off them on the inner side; counting adds $O(\log n)$ stored sizes.

:::

::: {#def-range-tree .definition name="Two-dimensional range tree"}

For points in the plane, a *range tree* is a balanced search tree on the $x$-coordinates in which every node also stores a one-dimensional tree of the $y$-coordinates of the points in its subtree.

:::

A query for the rectangle $[a,b]\times[c,d]$ finds the $O(\log n)$ subtrees covering $[a,b]$ in $x$ as in @prp-one-d-range, and runs a one-dimensional query in $y$ on each: $O(\log^2n)$ time to count, plus $O(k)$ to list. Each point lies in the secondary trees of its $O(\log n)$ ancestors, so the space is $O(n\log n)$. In $d$ dimensions the same idea gives $O(\log^dn)$ queries.

::: {#rmk-augmented-search-trees-finger .remark name="Finger search"}

Linking the nodes of each level of a 2-3 tree to their neighbours, and storing in each node the smallest and largest key of its subtree, allows a search that starts from a known key $y$ and finds $x$ in $O(\log|{\rm rank}(x)-{\rm rank}(y)|)$ time: walk up and sideways from $y$ until a node's key range contains $x$, then down. Searches near a recent position are then cheap.

:::
