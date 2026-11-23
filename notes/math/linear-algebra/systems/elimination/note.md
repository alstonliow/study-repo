---
title: "Elimination with Matrices"
sources: [mit1806-2]
requires: [math/linear-algebra/systems/geometry-of-linear-equations]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 2, in our own wording. Example numbers checked with sympy. -->

Elimination is the standard way to solve $A\mathbf{x}=\mathbf{b}$: subtract multiples of one equation from the equations below it until the system is triangular, then solve from the bottom up.

::: {#def-gaussian-elimination .definition name="Elimination, pivots, multipliers"}

Elimination on an $n\times n$ matrix $A$ works column by column. In column $k$ the *pivot* is the entry in row $k$ after the earlier steps. For each row $i>k$ subtract $\ell_{ik}$ times row $k$ from row $i$,
$$R_i\leftarrow R_i-\ell_{ik}R_k,$$
where $R_i$ denotes row $i$ and the *multiplier* is
$$\ell_{ik}=\frac{\text{entry to eliminate in row }i}{\text{pivot in row }k}.$$
This makes every entry below the pivot zero. The result is an upper triangular matrix $U$ whose diagonal holds the pivots. The same operations applied to $\mathbf{b}$ give a vector $\mathbf{c}$, and $U\mathbf{x}=\mathbf{c}$ is solved by *back substitution*: the last equation first, then upwards.

:::

::: {#fig-elimination-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$1$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$0$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$1$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$3$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[hl cell] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$13$};
\node[lab] at (1.85,0.825) {$\mathbf x$};
\node[lab] at (2.2,0.825) {$=$};
\draw[cell frame] (2.500,1.100) rectangle (3.050,1.650);
\node[lab] at (2.775,1.375) {$6$};
\draw[cell frame] (2.500,0.550) rectangle (3.050,1.100);
\node[lab] at (2.775,0.825) {$11$};
\draw[cell frame] (2.500,-0.000) rectangle (3.050,0.550);
\node[lab] at (2.775,0.275) {$39$};
\node[lab, anchor=west] (s3) at (3.6,0.275) {\textcircled{1} $13z=39\ \Rightarrow\ z=3$};
\node[lab, anchor=west] (s2) at (3.6,0.825) {\textcircled{2} $y+3\cdot3=11\ \Rightarrow\ y=2$};
\node[lab, anchor=west] (s1) at (3.6,1.375) {\textcircled{3} $x+2+3=6\ \Rightarrow\ x=1$};
\draw[->, emph, accent] (8.4,0.275) -- (8.4,1.375) node[midway, right, lab, note] {upwards};
\end{tikzpicture}
\end{center}
```

Back substitution on the triangular system $U\mathbf x=\mathbf c$ of @exm-elimination-three-by-three. The last row has one unknown; each row above it has one new unknown once the lower ones are known.

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

The *elimination matrix* $E_{ij}$ is the identity matrix with the entry $-\ell_{ij}$ in row $i$, column $j$ (with $i>j$):
$$E_{ij}=I-\ell_{ij}\,\mathbf{e}_i\mathbf{e}_j^{\mathsf T}.$$
Multiplying $E_{ij}A$ subtracts $\ell_{ij}$ times row $j$ of $A$ from row $i$ and leaves the other rows unchanged.

:::

::: {#fig-elimination-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[regionB, align=center] (L) at (0,0) {\textbf{start}: $A\mathbf x=\mathbf b$\\[3pt] $\begin{bmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}b_1\\b_2\\b_3\end{bmatrix}$};
\node[regionA, align=center] (R) at (8.2,0) {\textbf{goal}: $U\mathbf x=\mathbf c$\\[3pt] $\begin{bmatrix}u_{11}&u_{12}&u_{13}\\\textcolor{accent}{0}&u_{22}&u_{23}\\\textcolor{accent}{0}&\textcolor{accent}{0}&u_{33}\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}c_1\\c_2\\c_3\end{bmatrix}$};
\node[regionC, align=center] (B) at (4.1,-3.7) {\textbf{row operations on both sides}\\[3pt] $E_{32}E_{31}E_{21}\,\begin{bmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=E_{32}E_{31}E_{21}\,\begin{bmatrix}b_1\\b_2\\b_3\end{bmatrix}$};
\draw[->, bold, dashed, muted] (L.east) -- (R.west) node[midway, above, lab, note, align=center] {elimination};
\draw[->, bold, ink] ([xshift=-1.4cm]L.south) |- (B.west) node[pos=0.25, left, lab, note, align=right] {multiply\\on the left};
\draw[->, bold, ink] (B.east) -| ([xshift=1.4cm]R.south) node[pos=0.75, right, lab, note, align=left] {$E_{32}E_{31}E_{21}A=U$\\$E_{32}E_{31}E_{21}\mathbf b=\mathbf c$};
\end{tikzpicture}
\end{center}
```

What elimination does, in matrix language. Going straight from $A\mathbf x=\mathbf b$ to the triangular system $U\mathbf x=\mathbf c$ (dashed) is the same as multiplying both sides on the left by the elimination matrices $E_{21}$, $E_{31}$, $E_{32}$ in turn. Each one creates one zero below the diagonal (the three zeros of $U$); the same product turns $\mathbf b$ into $\mathbf c$, so the solution $\mathbf x$ does not change.

:::

::: {#prp-row-operations-are-left-multiplication .proposition name="Row operations are multiplication on the left"}

For any matrix $M$ with $n$ columns and any $A$ with $n$ rows, row $i$ of $MA$ is the combination
$$\operatorname{row}_i(MA)=\sum_{j=1}^n m_{ij}\operatorname{row}_j(A)=m_{i1}\,(\text{row }1\text{ of }A)+\dots+m_{in}\,(\text{row }n\text{ of }A).$$ In particular $E_{ij}$ acts as described in @def-elimination-matrix.

:::

::: {.proof}

1. Entry $(i,k)$ of $MA$ is $\sum_j m_{ij}a_{jk}$ (@prp-row-and-column-views-agree applied to column $k$ of $A$).

2. Reading this for all $k$ at once, row $i$ of $MA$ is $\sum_j m_{ij}\,(\text{row }j\text{ of }A)$.

3. Row $i$ of $E_{ij}$ is $\mathbf{e}_i^{\mathsf T}-\ell_{ij}\mathbf{e}_j^{\mathsf T}$, so row $i$ of $E_{ij}A$ is row $i$ minus $\ell_{ij}$ times row $j$. Every other row of $E_{ij}$ is a row of $I$ and copies the corresponding row of $A$.

:::

::: {#fig-elimination-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$0$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[hl cell] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$\mathbf{-2}$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$1$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$0$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\node[lab, note] at (0.825,-0.350) {$E_{21}$};
\node[lab] at (1.9,0.825) {$\times$};
\draw[cell, fill=primaryLight] (2.200,1.100) rectangle (2.750,1.650);
\node[lab] at (2.475,1.375) {$1$};
\draw[cell, fill=primaryLight] (2.750,1.100) rectangle (3.300,1.650);
\node[lab] at (3.025,1.375) {$1$};
\draw[cell, fill=primaryLight] (3.300,1.100) rectangle (3.850,1.650);
\node[lab] at (3.575,1.375) {$1$};
\draw[hl cell] (2.200,0.550) rectangle (2.750,1.100);
\node[lab] at (2.475,0.825) {$2$};
\draw[cell frame] (2.750,0.550) rectangle (3.300,1.100);
\node[lab] at (3.025,0.825) {$3$};
\draw[cell frame] (3.300,0.550) rectangle (3.850,1.100);
\node[lab] at (3.575,0.825) {$5$};
\draw[cell frame] (2.200,-0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$4$};
\draw[cell frame] (2.750,-0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$0$};
\draw[cell frame] (3.300,-0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$5$};
\node[lab, note] at (3.025,-0.350) {$A$};
\node[lab] at (4.1,0.825) {$=$};
\draw[cell frame] (4.400,1.100) rectangle (4.950,1.650);
\node[lab] at (4.675,1.375) {$1$};
\draw[cell frame] (4.950,1.100) rectangle (5.500,1.650);
\node[lab] at (5.225,1.375) {$1$};
\draw[cell frame] (5.500,1.100) rectangle (6.050,1.650);
\node[lab] at (5.775,1.375) {$1$};
\draw[hl cell] (4.400,0.550) rectangle (4.950,1.100);
\node[lab] at (4.675,0.825) {$0$};
\draw[cell, fill=primaryLight] (4.950,0.550) rectangle (5.500,1.100);
\node[lab] at (5.225,0.825) {$1$};
\draw[cell, fill=primaryLight] (5.500,0.550) rectangle (6.050,1.100);
\node[lab] at (5.775,0.825) {$3$};
\draw[cell frame] (4.400,-0.000) rectangle (4.950,0.550);
\node[lab] at (4.675,0.275) {$4$};
\draw[cell frame] (4.950,-0.000) rectangle (5.500,0.550);
\node[lab] at (5.225,0.275) {$0$};
\draw[cell frame] (5.500,-0.000) rectangle (6.050,0.550);
\node[lab] at (5.775,0.275) {$5$};
\node[lab, note] at (5.225,-0.350) {$E_{21}A$};
\node[lab, note, anchor=west, align=left] at (6.3,0.825) {row $2\;-\;2\times$row $1$:\\$(2,3,5)-2(1,1,1)=(0,1,3)$\\other rows copied};
\end{tikzpicture}
\end{center}
```

$E_{21}$ is the identity with $-\ell_{21}=-2$ in position $(2,1)$. Row $2$ of $E_{21}A$ takes $1$ times row $2$ of $A$ and $-2$ times row $1$ (shaded), which puts a zero below the first pivot; rows $1$ and $3$ of $E_{21}$ are rows of $I$, so they copy rows $1$ and $3$ of $A$.

:::

In @exm-elimination-three-by-three, $E_{32}E_{31}E_{21}A=U$ with
$$E_{21}=\begin{bmatrix}1&0&0\\-2&1&0\\0&0&1\end{bmatrix},\quad
E_{31}=\begin{bmatrix}1&0&0\\0&1&0\\-4&0&1\end{bmatrix},\quad
E_{32}=\begin{bmatrix}1&0&0\\0&1&0\\0&4&1\end{bmatrix}.$$

::: {#def-permutation-matrix-row-exchange .definition name="Row exchange matrix"}

The matrix $P_{ij}$ obtained from $I$ by exchanging rows $i$ and $j$ is a *row exchange* (elementary permutation) matrix. $P_{ij}A$ is $A$ with rows $i$ and $j$ exchanged; $AP_{ij}$ is $A$ with columns $i$ and $j$ exchanged.

:::

::: {#fig-elimination-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$1$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$2$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$5$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$4$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$6$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$8$};
\draw[->] (1.8,0.825) -- (2.6,0.825) node[midway, above, lab, note, align=center] {$\ell_{21}{=}2$\\$\ell_{31}{=}4$};
\draw[cell frame] (2.800,1.100) rectangle (3.350,1.650);
\node[lab] at (3.075,1.375) {$1$};
\draw[cell frame] (3.350,1.100) rectangle (3.900,1.650);
\node[lab] at (3.625,1.375) {$1$};
\draw[cell frame] (3.900,1.100) rectangle (4.450,1.650);
\node[lab] at (4.175,1.375) {$1$};
\draw[cell frame] (2.800,0.550) rectangle (3.350,1.100);
\node[lab] at (3.075,0.825) {$0$};
\draw[hl cell] (3.350,0.550) rectangle (3.900,1.100);
\node[lab] at (3.625,0.825) {$0$};
\draw[cell frame] (3.900,0.550) rectangle (4.450,1.100);
\node[lab] at (4.175,0.825) {$3$};
\draw[cell frame] (2.800,-0.000) rectangle (3.350,0.550);
\node[lab] at (3.075,0.275) {$0$};
\draw[cell frame] (3.350,-0.000) rectangle (3.900,0.550);
\node[lab] at (3.625,0.275) {$2$};
\draw[cell frame] (3.900,-0.000) rectangle (4.450,0.550);
\node[lab] at (4.175,0.275) {$4$};
\node[lab, note] at (3.625,-0.350) {zero in pivot position};
\draw[->] (4.6,0.825) -- (5.4,0.825) node[midway, above, lab, note] {$P_{23}$};
\draw[cell frame] (5.600,1.100) rectangle (6.150,1.650);
\node[lab] at (5.875,1.375) {$1$};
\draw[cell frame] (6.150,1.100) rectangle (6.700,1.650);
\node[lab] at (6.425,1.375) {$1$};
\draw[cell frame] (6.700,1.100) rectangle (7.250,1.650);
\node[lab] at (6.975,1.375) {$1$};
\draw[cell frame] (5.600,0.550) rectangle (6.150,1.100);
\node[lab] at (5.875,0.825) {$0$};
\draw[hl cell] (6.150,0.550) rectangle (6.700,1.100);
\node[lab] at (6.425,0.825) {$2$};
\draw[cell frame] (6.700,0.550) rectangle (7.250,1.100);
\node[lab] at (6.975,0.825) {$4$};
\draw[cell frame] (5.600,-0.000) rectangle (6.150,0.550);
\node[lab] at (5.875,0.275) {$0$};
\draw[cell frame] (6.150,-0.000) rectangle (6.700,0.550);
\node[lab] at (6.425,0.275) {$0$};
\draw[hl cell] (6.700,-0.000) rectangle (7.250,0.550);
\node[lab] at (6.975,0.275) {$3$};
\node[lab, note] at (6.425,-0.350) {pivots $1,2,3$};
\draw[<->, accent, emph] (4.45,0.55) to[bend left=50] (4.45,0.0);
\end{tikzpicture}
\end{center}
```

A zero in a pivot position does not stop elimination if a lower row can help. Here after column $1$ the $(2,2)$ entry is $0$, but row $3$ has a nonzero entry in column $2$; the row exchange $P_{23}$ swaps the two rows and the elimination is finished, with pivots $1,2,3$.

:::

::: {#rmk-elimination-1 .remark name="Rows on the left, columns on the right"}

Multiplying by a matrix on the left combines rows; multiplying on the right combines columns. Elimination uses only row operations, so the elimination matrices always stand on the left of $A$.

:::

::: {#fig-elimination-6}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box, align=center] (a) at (0,0) {\textbf{matrix product}\\[2pt]$E_{ij}=I-\ell_{ij}\,\mathbf e_i\mathbf e_j^{\mathsf T}$};
\node[box, align=center] (b) at (5.3,0) {\textbf{combination of rows}\\[2pt]$\operatorname{row}_i(MA)=\sum_j m_{ij}\operatorname{row}_j(A)$};
\node[hl box, align=center] (c) at (10.4,0) {\textbf{elimination step}\\[2pt]$R_i\leftarrow R_i-\ell_{ij}R_j$};
\draw[->, bold] (a) -- (b); \draw[->, bold] (b) -- (c);
\node[lab, note, align=center] at (2.55,-1.0) {row $i$ of $E_{ij}$ is\\$\mathbf e_i^{\mathsf T}-\ell_{ij}\mathbf e_j^{\mathsf T}$};
\node[lab, note, align=center] at (7.95,-1.0) {so row $i$ of $E_{ij}A$ is\\row $i$ minus $\ell_{ij}$ times row $j$};
\end{tikzpicture}
\end{center}
```

The three formulas of this note and how they connect. The matrix $E_{ij}$ differs from $I$ in one entry; by @prp-row-operations-are-left-multiplication, multiplying by it on the left combines rows of $A$ with the weights in its rows; the only row that changes is row $i$, which is exactly the elimination step.

:::
