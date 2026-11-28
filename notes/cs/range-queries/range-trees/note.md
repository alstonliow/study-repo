---
title: "Range Trees"
sources: [mit6046-9]
requires: [cs/data-structures/augmented-search-trees]
aliases: [cs/data-structures/range-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 9, in our own wording; proofs written out in steps. Split from cs/data-structures/augmented-search-trees on 2026-11-25 (one data structure per note, SPEC §8.6). -->

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
