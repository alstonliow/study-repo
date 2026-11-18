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

::: {#prp-row-and-column-views-agree .proposition name="The two ways to compute Ax agree"}

The column definition and the row (dot-product) rule give the same vector:
$$(A\mathbf{x})_i=\sum_{j=1}^n a_{ij}x_j.$$

:::

::: {.proof}

1. Component $i$ of $x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$ is $x_1a_{i1}+\dots+x_na_{in}$, because vectors are added component by component.

2. The dot product of row $i$, $(a_{i1},\dots,a_{in})$, with $\mathbf{x}$ is the same sum.

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

::: {#exm-three-by-three-column-picture .example name="A 3 by 3 system in columns"}

The system $x+y+z=6$, $2x+3y+5z=23$, $4x+5z=19$ asks for
$$x\begin{bmatrix}1\\2\\4\end{bmatrix}+y\begin{bmatrix}1\\3\\0\end{bmatrix}+z\begin{bmatrix}1\\5\\5\end{bmatrix}=\begin{bmatrix}6\\23\\19\end{bmatrix}.$$
The combination $x=1$, $y=2$, $z=3$ works: $(1+2+3,\ 2+6+15,\ 4+0+15)=(6,23,19)$. The next note finds it systematically.

:::
