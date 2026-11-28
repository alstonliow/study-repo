---
title: "Fractional Cascading and Layered Range Trees"
sources: [mit6851-3]
requires: [cs/range-queries/range-trees]
aliases: [cs/advanced-data-structures/fractional-cascading]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 3, in our own wording; proofs written out in steps. Dynamic layered range trees (weight-balanced trees), the $O(\log^{d-2}n)$ query of Lecture 4 and the general graph version are only mentioned. The example lists were checked by computation. -->

A binary search for the same key in many related sorted lists costs a logarithm per list. Fractional cascading saves all but the first logarithm by leaving, in each list, a sample of its successor list, so that a position in one list gives a position in the next in $O(1)$ time.

::: {#def-fractional-cascading .definition name="Cascaded lists"}

Let $L_1,\dots,L_k$ be sorted lists of length at most $n$. Define $L'_k=L_k$ and, for $i<k$, let $L'_i$ be the merge of $L_i$ with every other element of $L'_{i+1}$. Every element of $L'_i$ keeps a pointer to its predecessor and successor among the elements of $L_i$, and to its predecessor and successor among the elements of $L'_{i+1}$ that came from $L'_{i+1}$ (the *bridges*).

:::

::: {#exm-fractional-cascading-1 .example name="Three lists"}

Let $L_1=[2,5,9,12]$, $L_2=[1,4,6,11]$, $L_3=[3,7,8,10]$. Then $L'_3=L_3$; $L'_2=L_2\cup\{3,8\}=[1,3,4,6,8,11]$ (every other element of $L'_3$ is $3,8$); $L'_1=L_1\cup\{1,4,8\}=[1,2,4,5,8,9,12]$.

:::

::: {#fig-fractional-cascading-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \v/\h [count=\i from 0] in {1/1,2/0,4/1,5/0,8/1,9/0,12/0} {\ifnum\h=1 \draw[hl cell] (0.55*\i,1.6) rectangle +(0.55,0.55); \else \draw[cell frame] (0.55*\i,1.6) rectangle +(0.55,0.55);\fi \node[lab] at (0.55*\i+0.275,1.875) {$\v$};}
\foreach \v/\h [count=\i from 0] in {1/0,3/1,4/0,6/0,8/1,11/0} {\ifnum\h=1 \draw[hl cell] (0.55*\i,0.8) rectangle +(0.55,0.55); \else \draw[cell frame] (0.55*\i,0.8) rectangle +(0.55,0.55);\fi \node[lab] at (0.55*\i+0.275,1.075) {$\v$};}
\foreach \v [count=\i from 0] in {3,7,8,10} {\draw[cell frame] (0.55*\i,0) rectangle +(0.55,0.55); \node[lab] at (0.55*\i+0.275,0.275) {$\v$};}
\node[lab, anchor=east] at (-0.1,1.875) {$L'_1$};
\node[lab, anchor=east] at (-0.1,1.075) {$L'_2$};
\node[lab, anchor=east] at (-0.1,0.275) {$L'_3$};
\end{tikzpicture}
\end{center}
```

The lists of @exm-fractional-cascading-1; shaded entries of $L'_i$ were copied from $L'_{i+1}$ and bridge to it.

:::

::: {#thm-fractional-cascading .theorem name="Fractional cascading"}

The lists $L'_i$ have total size at most $2\sum_i|L_i|$, and after one binary search for $x$ in $L'_1$ the successor of $x$ in each of $L_1,\dots,L_k$ is found in $O(1)$ more time per list: in total $O(k+\log n)$ instead of $O(k\log n)$.

:::

::: {.proof}

1. *Size.* $|L'_i|=|L_i|+\tfrac12|L'_{i+1}|$, so unfolding gives $|L'_i|\le\sum_{j\ge i}2^{-(j-i)}|L_j|$, and summed over $i$ at most $2\sum_j|L_j|$.

2. *From $L'_i$ to $L'_{i+1}$.* Suppose we know the position of $x$ in $L'_i$, that is its two neighbours. The bridges lead to the two neighbours of $x$ among the elements copied from $L'_{i+1}$. Between two consecutive copied elements of $L'_{i+1}$ there is exactly one element of $L'_{i+1}$ that was not copied (every other element was copied), so one comparison of $x$ with that element finishes the position of $x$ in $L'_{i+1}$.

3. *From $L'_i$ to $L_i$.* The pointers to the neighbours inside $L_i$ give the successor of $x$ in $L_i$ in $O(1)$.

4. Thus one search in $L'_1$ ($O(\log n)$ time) plus $O(1)$ per list gives all $k$ answers.

:::

::: {#thm-layered-range-tree .theorem name="Layered range trees"}

For $n$ points in the plane, a range tree on the $x$-coordinate whose nodes store, instead of $y$-range trees, arrays of their points sorted by $y$ with fractional-cascading pointers between the array of a node and the arrays of its two children, uses $O(n\log n)$ space and reports the $k$ points in a rectangle in $O(\log n+k)$ time (counting: $O(\log n)$). In $d$ dimensions, applying the idea in the last dimension, the query time is $O(\log^{d-1}n+k)$ for $d\ge2$ and the space is $O(n\log^{d-1}n)$.

:::

::: {.proof}

1. A rectangle $[a_1,b_1]\times[a_2,b_2]$ is split by the $x$-range tree (@def-range-tree) into $O(\log n)$ canonical subtrees whose points have $x$ in $[a_1,b_1]$; the answer is the points with $y\in[a_2,b_2]$ in these subtrees.

2. In a plain range tree each canonical subtree needs its own binary search for $a_2$ and $b_2$, giving $O(\log^2n+k)$.

3. With arrays and bridges, binary search once for $a_2$ and $b_2$ in the array of the root; then, walking down the search paths in the $x$-tree, each step to a child converts the positions in the parent's array to positions in the child's array in $O(1)$ time (the child's array is a subset of the parent's, in the same $y$-order, exactly the situation of @thm-fractional-cascading, with a pointer to the successor whenever an element is not in the child). At each canonical node the two positions delimit the answer in its array.

4. The total is $O(\log n)$ for the searches and $O(1)$ per visited node, plus the output. Space is $O(n)$ per level, $O(n\log n)$ in all.

:::

::: {#rmk-fractional-cascading-1 .remark name="Beyond the lecture's proofs"}

Replacing "every other element" by a smaller fraction $\alpha$ lets the technique run on any graph in which every vertex has bounded in-degree for each key, and a walk visiting $k$ vertices then costs $O(k+\log n)$ (Chazelle–Guibas). Layered range trees are made dynamic with weight-balanced trees BB[$\alpha$] (rebuild an unbalanced subtree, charging the rebuild to the updates since it was balanced), for $O(\log^dn)$ amortised updates. For static $d\ge3$ the query can be reduced to $O(\log^{d-2}n)$ at the price of more space (Chazelle–Guibas), and the space of the $O(\log^{d-1}n)$ structure to $O(n\log^{d-1}n/\log\log n)$.

:::
