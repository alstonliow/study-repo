---
title: "Elimination with Matrices"
sources: [mit1806-2]
requires: [math/linear-algebra/systems/geometry-of-linear-equations]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 2, in our own wording. Example numbers checked with sympy. -->

Elimination is the standard way to solve $A\mathbf{x}=\mathbf{b}$: subtract multiples of one equation from the equations below it until the system is triangular, then solve from the bottom up.

::: {#def-gaussian-elimination .definition name="Elimination, pivots, multipliers"}

Elimination on an $n\times n$ matrix $A$ works column by column. In column $k$ the *pivot* is the entry in row $k$ after the earlier steps. For each row $i>k$ subtract $\ell_{ik}$ times row $k$ from row $i$, where the *multiplier* is
$$\ell_{ik}=\frac{\text{entry to eliminate in row }i}{\text{pivot in row }k}.$$
This makes every entry below the pivot zero. The result is an upper triangular matrix $U$ whose diagonal holds the pivots. The same operations applied to $\mathbf{b}$ give a vector $\mathbf{c}$, and $U\mathbf{x}=\mathbf{c}$ is solved by *back substitution*: the last equation first, then upwards.

:::

Pivots are never zero by definition. If a zero appears in a pivot position, exchange with a lower row that has a nonzero entry there. If no such row exists, elimination *breaks down*: the matrix has fewer than $n$ pivots and is not invertible (@sec-math-linear-algebra-systems-inverse-matrices).

::: {#exm-elimination-three-by-three .example name="Elimination on a 3 by 3 system"}

Solve $x+y+z=6$, $2x+3y+5z=23$, $4x+5z=19$. Work on the augmented matrix $[A\ \mathbf{b}]$:
$$\begin{bmatrix}1&1&1&6\\2&3&5&23\\4&0&5&19\end{bmatrix}
\xrightarrow{\ \ell_{21}=2,\ \ell_{31}=4\ }
\begin{bmatrix}1&1&1&6\\0&1&3&11\\0&-4&1&-5\end{bmatrix}
\xrightarrow{\ \ell_{32}=-4\ }
\begin{bmatrix}1&1&1&6\\0&1&3&11\\0&0&13&39\end{bmatrix}.$$
The pivots are $1,1,13$. Back substitution: $13z=39$ gives $z=3$; $y+3z=11$ gives $y=2$; $x+y+z=6$ gives $x=1$.

:::

::: {#fig-elimination-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$1$};
\draw[cell frame] (1.650,1.100) rectangle (2.200,1.650);
\node[lab] at (1.925,1.375) {$6$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$3$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$5$};
\draw[cell frame] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$23$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$4$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$5$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$19$};
\node[lab, note] at (1.100,-0.35) {$[A\ \mathbf b]$};
\draw[->] (2.350,0.825) -- (2.850,0.825);
\draw[cell frame] (3.000,1.100) rectangle (3.550,1.650);
\node[lab] at (3.275,1.375) {$1$};
\draw[cell frame] (3.550,1.100) rectangle (4.100,1.650);
\node[lab] at (3.825,1.375) {$1$};
\draw[cell frame] (4.100,1.100) rectangle (4.650,1.650);
\node[lab] at (4.375,1.375) {$1$};
\draw[cell frame] (4.650,1.100) rectangle (5.200,1.650);
\node[lab] at (4.925,1.375) {$6$};
\draw[cell frame] (3.000,0.550) rectangle (3.550,1.100);
\node[lab] at (3.275,0.825) {$0$};
\draw[hl cell] (3.550,0.550) rectangle (4.100,1.100);
\node[lab] at (3.825,0.825) {$1$};
\draw[cell frame] (4.100,0.550) rectangle (4.650,1.100);
\node[lab] at (4.375,0.825) {$3$};
\draw[cell frame] (4.650,0.550) rectangle (5.200,1.100);
\node[lab] at (4.925,0.825) {$11$};
\draw[cell frame] (3.000,0.000) rectangle (3.550,0.550);
\node[lab] at (3.275,0.275) {$0$};
\draw[cell frame] (3.550,0.000) rectangle (4.100,0.550);
\node[lab] at (3.825,0.275) {$-4$};
\draw[cell frame] (4.100,0.000) rectangle (4.650,0.550);
\node[lab] at (4.375,0.275) {$1$};
\draw[cell frame] (4.650,0.000) rectangle (5.200,0.550);
\node[lab] at (4.925,0.275) {$-5$};
\node[lab, note] at (4.100,-0.35) {after column 1};
\draw[->] (5.350,0.825) -- (5.850,0.825);
\draw[cell frame] (6.000,1.100) rectangle (6.550,1.650);
\node[lab] at (6.275,1.375) {$1$};
\draw[cell frame] (6.550,1.100) rectangle (7.100,1.650);
\node[lab] at (6.825,1.375) {$1$};
\draw[cell frame] (7.100,1.100) rectangle (7.650,1.650);
\node[lab] at (7.375,1.375) {$1$};
\draw[cell frame] (7.650,1.100) rectangle (8.200,1.650);
\node[lab] at (7.925,1.375) {$6$};
\draw[cell frame] (6.000,0.550) rectangle (6.550,1.100);
\node[lab] at (6.275,0.825) {$0$};
\draw[cell frame] (6.550,0.550) rectangle (7.100,1.100);
\node[lab] at (6.825,0.825) {$1$};
\draw[cell frame] (7.100,0.550) rectangle (7.650,1.100);
\node[lab] at (7.375,0.825) {$3$};
\draw[cell frame] (7.650,0.550) rectangle (8.200,1.100);
\node[lab] at (7.925,0.825) {$11$};
\draw[cell frame] (6.000,0.000) rectangle (6.550,0.550);
\node[lab] at (6.275,0.275) {$0$};
\draw[cell frame] (6.550,0.000) rectangle (7.100,0.550);
\node[lab] at (6.825,0.275) {$0$};
\draw[hl cell] (7.100,0.000) rectangle (7.650,0.550);
\node[lab] at (7.375,0.275) {$13$};
\draw[cell frame] (7.650,0.000) rectangle (8.200,0.550);
\node[lab] at (7.925,0.275) {$39$};
\node[lab, note] at (7.100,-0.35) {after column 2: $U$};
\end{tikzpicture}
\end{center}
```

Elimination column by column; the highlighted entry is the pivot used in the next step. The last matrix is upper triangular with pivots $1,1,13$.

:::

## Elimination matrices

Each step of elimination is a multiplication on the left by a simple matrix.

::: {#def-elimination-matrix .definition name="Elimination matrix"}

The *elimination matrix* $E_{ij}$ is the identity matrix with the entry $-\ell_{ij}$ in row $i$, column $j$ (with $i>j$). Multiplying $E_{ij}A$ subtracts $\ell_{ij}$ times row $j$ of $A$ from row $i$ and leaves the other rows unchanged.

:::

::: {#prp-row-operations-are-left-multiplication .proposition name="Row operations are multiplication on the left"}

For any matrix $M$ with $n$ columns and any $A$ with $n$ rows, row $i$ of $MA$ is the combination
$$m_{i1}\,(\text{row }1\text{ of }A)+\dots+m_{in}\,(\text{row }n\text{ of }A).$$ In particular $E_{ij}$ acts as described in @def-elimination-matrix.

:::

::: {.proof}

1. Entry $(i,k)$ of $MA$ is $\sum_j m_{ij}a_{jk}$ (@prp-row-and-column-views-agree applied to column $k$ of $A$).

2. Reading this for all $k$ at once, row $i$ of $MA$ is $\sum_j m_{ij}\,(\text{row }j\text{ of }A)$.

3. Row $i$ of $E_{ij}$ is $\mathbf{e}_i^{\mathsf T}-\ell_{ij}\mathbf{e}_j^{\mathsf T}$, so row $i$ of $E_{ij}A$ is row $i$ minus $\ell_{ij}$ times row $j$. Every other row of $E_{ij}$ is a row of $I$ and copies the corresponding row of $A$.

:::

In @exm-elimination-three-by-three, $E_{32}E_{31}E_{21}A=U$ with
$$E_{21}=\begin{bmatrix}1&0&0\\-2&1&0\\0&0&1\end{bmatrix},\quad
E_{31}=\begin{bmatrix}1&0&0\\0&1&0\\-4&0&1\end{bmatrix},\quad
E_{32}=\begin{bmatrix}1&0&0\\0&1&0\\0&4&1\end{bmatrix}.$$

::: {#def-permutation-matrix-row-exchange .definition name="Row exchange matrix"}

The matrix $P_{ij}$ obtained from $I$ by exchanging rows $i$ and $j$ is a *row exchange* (elementary permutation) matrix. $P_{ij}A$ is $A$ with rows $i$ and $j$ exchanged; $AP_{ij}$ is $A$ with columns $i$ and $j$ exchanged.

:::

::: {#rmk-elimination-1 .remark name="Rows on the left, columns on the right"}

Multiplying by a matrix on the left combines rows; multiplying on the right combines columns. Elimination uses only row operations, so the elimination matrices always stand on the left of $A$.

:::
