---
title: "The Geometry of Linear Equations"
sources: [mit1806-1]
requires: [math/linear-algebra/systems/vectors-and-dot-products]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 1, in our own wording. -->

The central problem is to solve $n$ linear equations in $n$ unknowns. Take
$$x+2y=5,\qquad 3x-y=1.$$
There are three ways to look at it.

## Row picture

Each equation describes a line in the plane (a plane in $\mathbb{R}^3$, a hyperplane in $\mathbb{R}^n$). A solution is a point on all of them. Here the lines $x+2y=5$ and $3x-y=1$ meet at $(1,2)$.

## Column picture

Collect the coefficients of each unknown into a column:
$$x\begin{bmatrix}1\\3\end{bmatrix}+y\begin{bmatrix}2\\-1\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}.$$
Now the question is which linear combination (@def-linear-combination) of the two columns produces the right side. The answer $x=1$, $y=2$ is the same, but the picture is different: one copy of the first column plus two copies of the second.

## Matrix picture

::: {#def-matrix-times-vector .definition name="Matrix times vector"}

Let $A$ be an $m\times n$ matrix with columns $\mathbf{a}_1,\dots,\mathbf{a}_n$ and let $\mathbf{x}\in\mathbb{R}^n$. Then
$$A\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\dots+x_n\mathbf{a}_n.$$
Equivalently, the $i$-th component of $A\mathbf{x}$ is the dot product of row $i$ of $A$ with $\mathbf{x}$ (@def-dot-product). A system of linear equations is the single equation $A\mathbf{x}=\mathbf{b}$.

:::

::: {#fig-geometry-of-linear-equations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$1$};
\draw[cell, fill=primaryLight] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$3$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$5$};
\draw[cell, fill=primaryLight] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$4$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$5$};
\draw[cell frame] (1.900,1.100) rectangle (2.450,1.650);
\node[lab] at (2.175,1.375) {$1$};
\draw[cell frame] (1.900,0.550) rectangle (2.450,1.100);
\node[lab] at (2.175,0.825) {$2$};
\draw[cell frame] (1.900,-0.000) rectangle (2.450,0.550);
\node[lab] at (2.175,0.275) {$3$};
\node[lab] at (2.75,0.825) {$=$};
\node[lab] at (3.25,0.825) {$1$};
\draw[cell, fill=primaryLight] (3.500,1.100) rectangle (4.050,1.650);
\node[lab] at (3.775,1.375) {$1$};
\draw[cell, fill=primaryLight] (3.500,0.550) rectangle (4.050,1.100);
\node[lab] at (3.775,0.825) {$2$};
\draw[cell, fill=primaryLight] (3.500,-0.000) rectangle (4.050,0.550);
\node[lab] at (3.775,0.275) {$4$};
\node[lab] at (4.3,0.825) {$+\,2$};
\draw[cell frame] (4.700,1.100) rectangle (5.250,1.650);
\node[lab] at (4.975,1.375) {$1$};
\draw[cell frame] (4.700,0.550) rectangle (5.250,1.100);
\node[lab] at (4.975,0.825) {$3$};
\draw[cell frame] (4.700,-0.000) rectangle (5.250,0.550);
\node[lab] at (4.975,0.275) {$0$};
\node[lab] at (5.5,0.825) {$+\,3$};
\draw[cell frame] (5.900,1.100) rectangle (6.450,1.650);
\node[lab] at (6.175,1.375) {$1$};
\draw[cell frame] (5.900,0.550) rectangle (6.450,1.100);
\node[lab] at (6.175,0.825) {$5$};
\draw[cell frame] (5.900,-0.000) rectangle (6.450,0.550);
\node[lab] at (6.175,0.275) {$5$};
\node[lab] at (6.75,0.825) {$=$};
\draw[hl cell] (7.050,1.100) rectangle (7.600,1.650);
\node[lab] at (7.325,1.375) {$6$};
\draw[hl cell] (7.050,0.550) rectangle (7.600,1.100);
\node[lab] at (7.325,0.825) {$23$};
\draw[hl cell] (7.050,-0.000) rectangle (7.600,0.550);
\node[lab] at (7.325,0.275) {$19$};
\node[lab, note] at (0.825,-0.35) {$A$};
\node[lab, note] at (2.175,-0.35) {$\mathbf x$};
\node[lab, note] at (5.4,-0.35) {columns of $A$};
\node[lab, note] at (7.325,-0.35) {$\mathbf b$};
\end{tikzpicture}
\end{center}
```

The column view of $A\mathbf x$ for the system of @exm-three-by-three-column-picture: the entries of $\mathbf x$ are the weights of the columns of $A$, and $A\mathbf x$ is the weighted sum.

:::

::: {#prp-row-and-column-views-agree .proposition name="The two ways to compute Ax agree"}

The column definition and the row (dot-product) rule give the same vector:
$$(A\mathbf{x})_i=\sum_{j=1}^n a_{ij}x_j.$$

:::

::: {.proof}

1. Component $i$ of $x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$ is $x_1a_{i1}+\dots+x_na_{in}$, because vectors are added component by component.

2. The dot product of row $i$, $(a_{i1},\dots,a_{in})$, with $\mathbf{x}$ is the same sum.

:::

::: {#fig-geometry-of-linear-equations-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$1$};
\draw[hl cell] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[hl cell] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$3$};
\draw[hl cell] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$5$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$4$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$5$};
\draw[cell, fill=primaryLight] (1.900,1.100) rectangle (2.450,1.650);
\node[lab] at (2.175,1.375) {$1$};
\draw[cell, fill=primaryLight] (1.900,0.550) rectangle (2.450,1.100);
\node[lab] at (2.175,0.825) {$2$};
\draw[cell, fill=primaryLight] (1.900,-0.000) rectangle (2.450,0.550);
\node[lab] at (2.175,0.275) {$3$};
\node[lab] at (2.75,0.825) {$=$};
\draw[cell frame] (3.050,1.100) rectangle (3.600,1.650);
\node[lab] at (3.325,1.375) {$6$};
\draw[hl cell] (3.050,0.550) rectangle (3.600,1.100);
\node[lab] at (3.325,0.825) {$23$};
\draw[cell frame] (3.050,-0.000) rectangle (3.600,0.550);
\node[lab] at (3.325,0.275) {$19$};
\node[lab, anchor=west] at (4.0,0.825) {$\underbrace{2\cdot1+3\cdot2+5\cdot3}_{\text{row }2\,\cdot\,\mathbf x}=23$};
\end{tikzpicture}
\end{center}
```

The row view of the same product: entry $i$ of $A\mathbf x$ is the dot product of row $i$ of $A$ with $\mathbf x$. The row view and the column view add up the same nine products $a_{ij}x_j$, grouped by rows or by columns.

:::

::: {#fig-geometry-of-linear-equations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.500,0) -- (3.200,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.600) -- (0,3.400) node[lab, above] {$y$};
\draw[emph] (-0.275,1.513) -- (3.025,-0.138) node[lab, below left] {$x+2y=5$};
\draw[emph] (0.000,-0.550) -- (0.770,1.760) node[lab, right] {$3x-y=1$};
\node[hl dot] at (0.550,1.100) {};
\node[lab, left] at (0.400,1.150) {$(1,2)$};
\node[lab] at (1.4,-0.9) {row picture};
\draw[->, faint] (4.900,0.6) -- (8.200,0.6);
\draw[->, faint] (5.200,0.1) -- (5.200,2.4);
\draw[->, emph] (5.200,0.600) -- (5.700,2.100);
\node[lab, left] at (5.700,2.100) {$\mathbf{a}_1$};
\draw[->, emph] (5.700,2.100) -- (6.700,1.600);
\draw[->, emph] (6.700,1.600) -- (7.700,1.100);
\node[lab, right] at (7.700,1.100) {$2\mathbf{a}_2$};
\draw[->, hl] (5.200,0.600) -- (7.700,1.100);
\node[lab, below right] at (7.700,1.100) {$\mathbf{b}$};
\node[lab] at (6.500,-0.9) {column picture: $1\mathbf{a}_1+2\mathbf{a}_2=\mathbf{b}$};
\end{tikzpicture}
\end{center}
```

Row picture: the two lines meet at $(1,2)$. Column picture: one copy of column 1 plus two copies of column 2 give $\mathbf{b}=(5,1)$.

:::

::: {#rmk-geometry-of-linear-equations-1 .remark name="When is Ax = b solvable for every b"}

$A\mathbf{x}=\mathbf{b}$ has a solution exactly when $\mathbf{b}$ is a combination of the columns of $A$. For a square $n\times n$ matrix the question "can we solve for every $\mathbf{b}$?" becomes "do the combinations of the columns fill $\mathbb{R}^n$?" In $\mathbb{R}^3$ this fails when the three columns lie in one plane: then only right sides in that plane can be reached. In the row picture the same failure shows up as three planes with no common point (or a whole line of common points). The later notes make this precise with the column space (@sec-math-linear-algebra-vector-spaces-vector-spaces-and-subspaces).

:::

::: {#fig-geometry-of-linear-equations-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-0.3,0) -- (3.2,0);
\draw[->, muted] (0,-0.3) -- (0,3.2);
\draw[emph, primary] (0,3) -- (3,0);
\draw[emph, accent] (0.5,-0.5) -- (3,2);
\fill[ink] (2,1) circle[pt];
\node[lab, tick, above right] at (2,1) {$(2,1)$};
\node[lab, note] at (1.45,-0.6) {one solution};
\end{scope}
\begin{scope}[shift={(4.2,0)}]
\draw[->, muted] (-0.3,0) -- (3.2,0);
\draw[->, muted] (0,-0.3) -- (0,3.2);
\draw[emph, primary] (0,1) -- (1,0);
\draw[emph, accent] (0,3) -- (3,0);
\node[lab, note] at (1.45,-0.6) {parallel: no solution};
\end{scope}
\begin{scope}[shift={(8.4,0)}]
\draw[->, muted] (-0.3,0) -- (3.2,0);
\draw[->, muted] (0,-0.3) -- (0,3.2);
\draw[bold, primary] (0,2) -- (2,0);
\draw[emph, accent, dashed] (0,2) -- (2,0);
\node[lab, note] at (1.45,-0.6) {same line: infinitely many};
\end{scope}
\end{tikzpicture}
\end{center}
```

The three possibilities for two equations in two unknowns, in the row picture. Left: $x+y=3$ and $x-y=1$ cross at $(2,1)$. Middle: $x+y=1$ and $x+y=3$ never meet. Right: $x+y=2$ and $2x+2y=4$ are the same line. In the column picture the last two cases are the ones where both columns lie on one line.

:::

::: {#exm-three-by-three-column-picture .example name="A 3 by 3 system in columns"}

The system $x+y+z=6$, $2x+3y+5z=23$, $4x+5z=19$ asks for
$$x\begin{bmatrix}1\\2\\4\end{bmatrix}+y\begin{bmatrix}1\\3\\0\end{bmatrix}+z\begin{bmatrix}1\\5\\5\end{bmatrix}=\begin{bmatrix}6\\23\\19\end{bmatrix}.$$
The combination $x=1$, $y=2$, $z=3$ works: $(1+2+3,\ 2+6+15,\ 4+0+15)=(6,23,19)$. The next note finds it systematically.

:::

::: {#fig-geometry-of-linear-equations-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x={(-0.5cm,-0.35cm)}, y={(0.26cm,0)}, z={(0,0.24cm)}]
\draw[->, muted] (0,0,0) -- (8,0,0) node[below left, lab, tick] {$x$};
\draw[->, muted] (0,0,0) -- (0,26,0) node[right, lab, tick] {$y$};
\draw[->, muted] (0,0,0) -- (0,0,22) node[above, lab, tick] {$z$};
\draw[->, emph, primary] (0,0,0) -- (1,2,4) node[midway, left, lab, note] {$1\cdot\text{col}_1$};
\draw[->, emph, secondary] (1,2,4) -- (3,8,4) node[pos=0.7, below=3pt, lab, note] {$2\cdot\text{col}_2$};
\draw[->, emph, accent] (3,8,4) -- (6,23,19) node[midway, below right, lab, note] {$3\cdot\text{col}_3$};
\draw[->, faint, dashed] (0,0,0) -- (6,23,19);
\fill[ink] (6,23,19) circle[pt] node[above right, lab] {$\mathbf b=(6,23,19)$};
\draw[faint, dotted] (6,23,19) -- (6,23,0) -- (0,23,0); \draw[faint, dotted] (6,23,0) -- (6,0,0);
\end{scope}
\end{tikzpicture}
\end{center}
```

The column picture in $\mathbb R^3$: one copy of column $1$, two of column $2$ and three of column $3$, placed head to tail, end at $\mathbf b$. The three columns do not lie in one plane, so every $\mathbf b$ can be reached this way.

:::
