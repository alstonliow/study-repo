---
title: "Backtracking"
sources: []
requires: [cs/algorithm-design/recursive-algorithms]
status: draft
---

<!-- Added 2026-11-26 in our own words (owner decision 2026-11-26: new notes for the LeetCode Hot 100 problems without a fitting note). No single source; TODO: add a source if one is integrated later. The examples and figures are our own. -->

*Backtracking* enumerates the solutions of a search problem by building a candidate one choice at a time, recursing on each choice and undoing it afterwards. It explores a tree of partial candidates depth first, and abandons a subtree as soon as its root cannot be extended to a solution.

::: {#def-state-space-tree .definition name="State-space tree"}

A *state-space tree* has one node per partial candidate $(c_1,\dots,c_k)$; the children of a node are its extensions $(c_1,\dots,c_k,c)$ by every allowed next choice $c$, and the leaves are complete candidates. A *pruning test* is a predicate on partial candidates that is false only when no descendant is a solution.

:::

```{=latex}
\begin{algorithm}
\caption{Backtracking}
\begin{algorithmic}
\PROCEDURE{Extend}{$x$} \COMMENT{$x$ is a partial candidate}
    \IF{$x$ is complete}
        \STATE report $x$ if it is a solution; \textbf{return}
    \ENDIF
    \FOR{each allowed next choice $c$}
        \STATE append $c$ to $x$
        \IF{the pruning test passes on $x$}
            \STATE \CALL{Extend}{$x$}
        \ENDIF
        \STATE remove $c$ from $x$ \COMMENT{undo: back to the state before the choice}
    \ENDFOR
\ENDPROCEDURE
\end{algorithmic}
\end{algorithm}
```

The undo step lets one mutable candidate, and any bookkeeping attached to it, serve the whole search, so the extra space is proportional to the depth of the tree.

## Subsets, permutations, combinations

::: {#prp-backtracking-counts .proposition name="Enumerating subsets and permutations"}

For $n$ distinct items, backtracking lists all $2^n$ subsets in $O(n2^n)$ time and all $n!$ permutations in $O(n\cdot n!)$ time, each exactly once.

:::

::: {.proof}

1. *Subsets.* At depth $k$ decide whether item $k$ is in or out. Every subset corresponds to exactly one root-to-leaf path, the tree has $2^n$ leaves and fewer than $2^{n+1}$ nodes, and copying a leaf's subset costs $O(n)$.

2. *Permutations.* At depth $k$ choose any unused item for position $k+1$, keeping a used-flag per item. A permutation is one root-to-leaf path. The tree has $n!/(n-k)!$ nodes at depth $k$, and $\sum_{k=0}^{n}n!/(n-k)!=n!\sum_{j=0}^{n}1/j!<e\cdot n!$. Each node does $O(n)$ work scanning the flags, giving $O(n\cdot n!)$.

:::

::: {#fig-backtracking-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=1cm, level 1/.style={sibling distance=4cm}, level 2/.style={sibling distance=2cm}, level 3/.style={sibling distance=1cm}, every node/.style={lab,note}]
\node {$\{\}$}
  child {node {$\{1\}$} child {node {$\{1,2\}$} child {node {$\{1,2,3\}$}} child {node {$\{1,2\}$}}} child {node {$\{1\}$} child {node {$\{1,3\}$}} child {node {$\{1\}$}}}}
  child {node {$\{\}$} child {node {$\{2\}$} child {node {$\{2,3\}$}} child {node {$\{2\}$}}} child {node {$\{\}$} child {node {$\{3\}$}} child {node {$\{\}$}}}};
\end{tikzpicture}
\end{center}
```

The state-space tree for the subsets of $\{1,2,3\}$: at depth $k$ the left branch takes item $k$ and the right branch skips it. The $8$ leaves are the $8$ subsets.

:::

::: {#rmk-backtracking-1 .remark name="Combinations without repeats"}

To list multisets of values from a list $v_1,\dots,v_m$ (each usable many times) with a given sum, make the choices nondecreasing in index: a node whose last choice was $v_i$ may only extend by $v_i,\dots,v_m$. Then each multiset is built in exactly one order. With the values sorted, a branch can stop as soon as the remaining target is negative. Listing all strings obtained by choosing one letter per digit is the simplest case: the tree is a product of independent choices.

:::

## Pruning

::: {#exm-backtracking-parentheses .example name="Balanced parentheses"}

A string of $n$ opening and $n$ closing parentheses is balanced exactly when no prefix has more closings than openings. So extend with `(` while fewer than $n$ have been used and with `)` while closings are fewer than openings. Every leaf reached is then balanced: there is no dead end, and the work is proportional to the output, the Catalan number $\frac1{n+1}\binom{2n}{n}$ of strings times their length.

:::

::: {#exm-backtracking-queens .example name="Non-attacking queens"}

To place $n$ queens on an $n\times n$ board with no two in the same row, column or diagonal, put one queen per row. Keep three sets: used columns $c$, used differences $r-c$ and used sums $r+c$ (each diagonal has a constant difference or sum). A square is allowed in $O(1)$ time exactly when none of its three values is used. Adding and removing a queen updates the sets.

:::

::: {#fig-backtracking-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.6cm]
\foreach \r in {0,...,3} \foreach \c in {0,...,3} { \draw[cell frame] (\c,3-\r) rectangle (\c+1,4-\r); }
\foreach \r/\c in {0/1,1/3,2/0,3/2} { \draw[hl cell] (\c,3-\r) rectangle (\c+1,4-\r); \node[hl dot] at (\c+0.5,3.5-\r) {}; }
\begin{scope}[xshift=4cm]
\foreach \r in {0,...,3} \foreach \c in {0,...,3} { \draw[cell frame] (\c,3-\r) rectangle (\c+1,4-\r); }
\node[hl dot] at (0.5,3.5) {}; \node[hl dot] at (2.5,2.5) {};
\foreach \c in {0,1,2,3} { \node[lab] at (\c+0.5,1.5) {$\times$}; }
\node[lab,note,anchor=west] at (4.3,1.5) {dead end: prune};
\end{scope}
\end{tikzpicture}
\end{center}
```

Left: a solution for $n=4$. Right: after queens at $(1,1)$ and $(2,3)$, every square of row $3$ is attacked, so the search abandons this branch and undoes the second queen.

:::

::: {#exm-backtracking-grid .example name="Paths in a grid"}

To decide whether a word $w$ can be spelled by a path of horizontally or vertically adjacent cells of a letter grid, each cell used at most once, start a search from every cell matching $w[1]$. At depth $k$ step to a neighbour holding $w[k+1]$ that is not on the current path. Mark a cell when entering it and unmark it when backtracking, so the marks are always exactly the current path.

:::

::: {#rmk-backtracking-2 .remark name="Cutting a string"}

Partitions of a string into palindromes are enumerated by choosing the end of the first piece, keeping it only if it is a palindrome, and recursing on the rest. Precomputing whether each $s[i..j]$ is a palindrome (by dynamic programming over increasing lengths) makes every test $O(1)$.

:::
