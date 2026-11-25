---
title: "Order-Statistic Trees"
sources: [mit6046-9]
requires: [cs/data-structures/augmented-search-trees]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 9, in our own wording; proofs written out in steps. Split from cs/data-structures/augmented-search-trees on 2026-11-25 (one data structure per note, SPEC §8.6). -->

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
