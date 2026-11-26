---
title: "Domino Tilings of a 3 × n Board"
sources: [cs97si-4]
requires: [cs/algorithm-design/subproblem-design]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 4 (one-dimensional DP examples), in our own wording; the derivation with a second family of boards, the examples and the figure are our own; counts checked by a brute-force count. -->

Counting problems are dynamic programs too: the relation adds the counts of the cases of the last step instead of taking a minimum. When the board left after the last step is not of the original shape, a second family of subproblems is added (subproblem expansion, @sec-cs-algorithm-design-subproblem-design).

::: {#rmk-tri-tiling-warm-up .remark name="Warm-up: one row"}

The number $D_n$ of ways to write $n$ as an ordered sum of $1$, $3$ and $4$ (equivalently, to tile a $1\times n$ strip with pieces of these lengths) satisfies $D_n=D_{n-1}+D_{n-3}+D_{n-4}$, with $D_0=1$ and $D_k=0$ for $k<0$, by the length of the last piece: $D_0,\dots,D_8=1,1,1,2,4,6,9,15,25$.

:::

::: {#exm-tri-tiling .example name="Domino tilings of a 3 × n board"}

Count the tilings of a $3\times n$ board by $1\times2$ dominoes.

1. *Subproblems:* $f(n)$, the number of tilings of the $3\times n$ board, and $g(n)$, the number of tilings of the $3\times n$ board with the top-left cell removed (by symmetry the same as with the bottom-left cell removed).
2. *Relation:* look at how column $1$ is covered.
   - Full board: either three horizontal dominoes cover columns $1$ and $2$, leaving a full board of width $n-2$; or a vertical domino covers the top two cells of column $1$ and a horizontal domino the bottom cell, leaving width $n-1$ with one corner cell removed; or the mirror image of that.
   - Board with the top-left cell removed: either a vertical domino covers the two remaining cells of column $1$, leaving a full board of width $n-1$; or two horizontal dominoes cover them, and then the free top cell of column $2$ forces a horizontal domino on columns $2$ and $3$, leaving width $n-2$ with a corner removed.

   So
   $$f(n)=f(n-2)+2\,g(n-1),\qquad g(n)=f(n-1)+g(n-2).$$
3. *Order:* increasing $n$.
4. *Base:* $f(0)=1$, $f(1)=0$, $g(0)=0$, $g(1)=1$.
5. *Original:* $f(n)$.
6. *Time:* $O(n)$. Eliminating $g$ gives $f(n)=4f(n-2)-f(n-4)$ for even $n\ge4$, and $f(n)=0$ for odd $n$ (the area is odd).

The counts for $n=0,2,4,6,8,10$ are $1,3,11,41,153,571$.

:::

::: {#fig-tri-tiling-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.55]
\begin{scope}
\fill[tintA] (0,0) rectangle (2,3);
\draw[gridline] (0,0) grid (5,3);
\foreach \y in {0,1,2} \draw[emph] (0.08,\y+0.08) rectangle (1.92,\y+0.92);
\node[lab,note] at (3.5,-0.7) {$f(n-2)$};
\node[lab,note] at (1,-0.7) {three flat};
\end{scope}
\begin{scope}[xshift=7cm]
\fill[tintB] (0,0) rectangle (1,3); \fill[tintB] (1,0) rectangle (2,1);
\draw[gridline] (0,0) grid (5,3);
\draw[emph] (0.08,1.08) rectangle (0.92,2.92);
\draw[emph] (0.08,0.08) rectangle (1.92,0.92);
\node[lab,note] at (3.2,-0.7) {$g(n-1)$, twice};
\end{scope}
\begin{scope}[xshift=14cm]
\draw[gridline] (0,0) grid (5,3);
\fill[neutral] (0,2) rectangle (1,3);
\draw[emph] (0.08,0.08) rectangle (0.92,1.92);
\node[lab,note] at (2.5,-0.7) {$g(n)$: vertical leaves $f(n-1)$};
\end{scope}
\end{tikzpicture}
\end{center}
```

The cases of @exm-tri-tiling. Left: three horizontal dominoes leave a full board of width $n-2$. Middle: a vertical domino and one horizontal domino leave a board with a corner removed (and its mirror image). Right: in a board with its top-left cell removed, a vertical domino in column $1$ leaves a full board of width $n-1$; two horizontal dominoes instead leave a board of shape $g(n-2)$.

:::
