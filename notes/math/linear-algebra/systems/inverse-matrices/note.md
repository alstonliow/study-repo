---
title: "Inverse Matrices"
sources: [mit1806-3]
requires: [math/linear-algebra/systems/matrix-multiplication]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 3, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-inverse-matrix .definition name="Inverse matrix"}

A square matrix $A$ is *invertible* (nonsingular) if there is a matrix $A^{-1}$ with
$$A^{-1}A=I\qquad\text{and}\qquad AA^{-1}=I.$$
Otherwise $A$ is *singular*.

:::

::: {#prp-inverse-is-unique .proposition name="The inverse is unique"}

If $BA=I$ and $AC=I$ then $B=C$. In particular a matrix has at most one inverse.

:::

::: {.proof}

1. By associativity (@prp-matrix-product-laws), $B=B(AC)=(BA)C=C$.

:::

::: {#thm-singular-if-nonzero-null-vector .theorem name="A test for singularity"}

If $A\mathbf{x}=\mathbf{0}$ for some $\mathbf{x}\neq\mathbf{0}$, then $A$ is not invertible.

:::

::: {.proof}

1. Suppose $A^{-1}$ existed. Multiply $A\mathbf{x}=\mathbf{0}$ by $A^{-1}$ on the left.

2. This gives $\mathbf{x}=A^{-1}\mathbf{0}=\mathbf{0}$, contradicting $\mathbf{x}\neq\mathbf{0}$.

:::

::: {#fig-inverse-matrices-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}
\draw[gridline] (-1.5,-1.5) grid[step=0.5] (1.5,1.5);
\draw[->, muted] (-1.6,0) -- (1.7,0); \draw[->, muted] (0,-1.6) -- (0,1.7);
\draw[hl] (-1.5,0.75) -- (1.5,-0.75);
\node[lab, note, accent] at (1.25,-1.15) {$N(A)$};
\fill[accent] (1,-0.5) circle[pt] node[above right, lab, tick] {$(2,-1)/2$};
\node[lab, note] at (0,-1.95) {all of $\mathbb R^2$};
\end{scope}
\draw[->] (1.9,0) -- (3.1,0) node[midway, above, lab, note] {$A$};
\begin{scope}[shift={(5,0)}]
\draw[->, muted] (-1.6,0) -- (1.7,0); \draw[->, muted] (0,-1.6) -- (0,1.7);
\draw[emph, primary] (-0.75,-1.5) -- (0.75,1.5);
\fill[accent] (0,0) circle[pt] node[below right, lab, tick] {$\mathbf 0$};
\node[lab, note, primary] at (1.1,1.4) {$C(A)$};
\node[lab, note] at (0,-1.95) {only a line is reached};
\end{scope}
\end{tikzpicture}
\end{center}
```

Why a nonzero solution of $A\mathbf x=\mathbf 0$ rules out an inverse, for $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$. The whole line through $(2,-1)$ is sent to $\mathbf 0$, and the plane is flattened onto the line through $(1,2)$. Since different vectors land on the same point, no matrix can send them back.

:::

For example $A=\begin{bmatrix}1&3\\2&6\end{bmatrix}$ is singular: $A\,(3,-1)=\mathbf{0}$. Its columns lie on one line, so $A\mathbf{x}=\mathbf{b}$ cannot be solved for every $\mathbf{b}$.

::: {#prp-inverse-of-product .proposition name="Inverse of a product"}

If $A$ and $B$ are invertible $n\times n$ matrices, then $AB$ is invertible and
$$(AB)^{-1}=B^{-1}A^{-1}.$$

:::

::: {.proof}

1. $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AA^{-1}=I$.

2. $(B^{-1}A^{-1})(AB)=B^{-1}(A^{-1}A)B=B^{-1}B=I$.

:::

::: {#fig-inverse-matrices-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[set] (U) at (0,0) {};
\node[set] (V) at (3.2,0) {};
\node[lab, above] at (0,1.3) {$\mathbb R^n$};
\node[lab, above] at (3.2,1.3) {$\mathbb R^n$};
\fill[ink] (0,0.3) circle[pt] node[left, lab] {$\mathbf x$};
\fill[ink] (3.2,0.3) circle[pt] node[right, lab] {$A\mathbf x$};
\draw[map, emph, primary] (0,0.3) to[bend left=25] node[above, lab] {$A$} (3.2,0.3);
\draw[map, emph, accent] (3.2,0.3) to[bend left=25] node[below, lab] {$A^{-1}$} (0,0.3);
\begin{scope}[shift={(6,0)}]
\node[box] (a) at (0,0) {$\mathbf x$}; \node[box] (b) at (2,0) {$B\mathbf x$}; \node[box] (c) at (4.2,0) {$AB\mathbf x$};
\draw[->, emph, primary] (a) to[bend left=30] node[above, lab] {$B$} (b);
\draw[->, emph, primary] (b) to[bend left=30] node[above, lab] {$A$} (c);
\draw[->, emph, accent] (c) to[bend left=30] node[below, lab] {$A^{-1}$} (b);
\draw[->, emph, accent] (b) to[bend left=30] node[below, lab] {$B^{-1}$} (a);
\end{scope}
\end{tikzpicture}
\end{center}
```

Left: $A^{-1}$ undoes $A$, so $A^{-1}A\mathbf x=\mathbf x$. Right: to undo $AB$ (first $B$, then $A$), undo the last step first: $(AB)^{-1}=B^{-1}A^{-1}$, the inverses in reverse order.

:::

The order reverses, as with taking off shoes after socks. The inverse of an elimination matrix $E_{ij}$ adds back what $E_{ij}$ subtracted: it is $I$ with $+\ell_{ij}$ in position $(i,j)$.

::: {#def-gauss-jordan .definition name="Gauss–Jordan elimination"}

To compute $A^{-1}$ for an $n\times n$ matrix $A$, apply elimination to the $n\times 2n$ matrix $[A\ I]$: first downwards to make $A$ upper triangular, then upwards to clear the entries above the pivots, and finally divide each row by its pivot. If $A$ has $n$ pivots the result is $[I\ A^{-1}]$.

:::

::: {#fig-inverse-matrices-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,0) {$\begin{bmatrix}A & I\end{bmatrix}$};
\node[box] (b) at (3.9,0) {$\begin{bmatrix}U & \ast\end{bmatrix}$};
\node[hl box] (c) at (7.8,0) {$\begin{bmatrix}I & A^{-1}\end{bmatrix}$};
\draw[map] (a) -- node[edge label, above=4pt, align=center] {eliminate\\downwards} (b);
\draw[map] (b) -- node[edge label, above=4pt, align=center] {upwards, divide\\by pivots} (c);
\end{tikzpicture}
\end{center}
```

Gauss–Jordan elimination works on the whole $n\times2n$ matrix. When the left half has become $I$, every row operation has been applied to $I$ as well, so the right half is $A^{-1}$.

:::

::: {#thm-gauss-jordan-correct .theorem name="Gauss–Jordan computes the inverse"}

If Gauss–Jordan turns $[A\ I]$ into $[I\ X]$, then $X=A^{-1}$.

:::

::: {.proof}

1. Every step is a row operation, so the whole process is multiplication on the left by one matrix $E$ (@prp-row-operations-are-left-multiplication, associativity). Then $E[A\ I]=[EA\ E]$ by block multiplication (@prp-block-multiplication).

2. The result is $[I\ X]$, so $EA=I$ and $E=X$. Thus $XA=I$.

3. Each elementary operation has an inverse operation, so $E$ is a product of invertible matrices and is invertible (@prp-inverse-of-product). From $EA=I$ we get $A=E^{-1}$, hence $AX=E^{-1}E=I$ as well.

:::

::: {#exm-gauss-jordan-two-by-two .example name="Gauss–Jordan on a 2 by 2 matrix"}

$$\left[\begin{array}{cc|cc}1&3&1&0\\2&7&0&1\end{array}\right]
\to\left[\begin{array}{cc|cc}1&3&1&0\\0&1&-2&1\end{array}\right]
\to\left[\begin{array}{cc|cc}1&0&7&-3\\0&1&-2&1\end{array}\right],$$
so $\begin{bmatrix}1&3\\2&7\end{bmatrix}^{-1}=\begin{bmatrix}7&-3\\-2&1\end{bmatrix}$. In general
$$\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1}=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}\qquad(ad-bc\neq0).$$

:::

::: {#fig-inverse-matrices-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$1$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$3$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$1$};
\draw[cell frame] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$0$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$2$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$7$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$0$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$1$};
\node[lab, note] at (1.100,-0.350) {$[A\ I]$};
\draw[bold, ink] (1.100,1.150) -- (1.100,-0.050);
\draw[->] (2.4,0.55) -- (3.5,0.55) node[midway, above, lab, tick] {$R_2-2R_1$};
\draw[cell frame] (3.700,0.550) rectangle (4.250,1.100);
\node[lab] at (3.975,0.825) {$1$};
\draw[hl cell] (4.250,0.550) rectangle (4.800,1.100);
\node[lab] at (4.525,0.825) {$3$};
\draw[cell frame] (4.800,0.550) rectangle (5.350,1.100);
\node[lab] at (5.075,0.825) {$1$};
\draw[cell frame] (5.350,0.550) rectangle (5.900,1.100);
\node[lab] at (5.625,0.825) {$0$};
\draw[cell frame] (3.700,0.000) rectangle (4.250,0.550);
\node[lab] at (3.975,0.275) {$0$};
\draw[hl cell] (4.250,0.000) rectangle (4.800,0.550);
\node[lab] at (4.525,0.275) {$1$};
\draw[cell frame] (4.800,0.000) rectangle (5.350,0.550);
\node[lab] at (5.075,0.275) {$-2$};
\draw[cell frame] (5.350,0.000) rectangle (5.900,0.550);
\node[lab] at (5.625,0.275) {$1$};
\draw[bold, ink] (4.800,1.150) -- (4.800,-0.050);
\draw[->] (6.1,0.55) -- (7.2,0.55) node[midway, above, lab, tick] {$R_1-3R_2$};
\draw[cell frame] (7.400,0.550) rectangle (7.950,1.100);
\node[lab] at (7.675,0.825) {$1$};
\draw[cell frame] (7.950,0.550) rectangle (8.500,1.100);
\node[lab] at (8.225,0.825) {$0$};
\draw[cell, fill=primaryLight] (8.500,0.550) rectangle (9.050,1.100);
\node[lab] at (8.775,0.825) {$7$};
\draw[cell, fill=primaryLight] (9.050,0.550) rectangle (9.600,1.100);
\node[lab] at (9.325,0.825) {$-3$};
\draw[cell frame] (7.400,0.000) rectangle (7.950,0.550);
\node[lab] at (7.675,0.275) {$0$};
\draw[cell frame] (7.950,0.000) rectangle (8.500,0.550);
\node[lab] at (8.225,0.275) {$1$};
\draw[cell, fill=primaryLight] (8.500,0.000) rectangle (9.050,0.550);
\node[lab] at (8.775,0.275) {$-2$};
\draw[cell, fill=primaryLight] (9.050,0.000) rectangle (9.600,0.550);
\node[lab] at (9.325,0.275) {$1$};
\node[lab, note] at (8.500,-0.350) {$[I\ A^{-1}]$};
\draw[bold, ink] (8.500,1.150) -- (8.500,-0.050);
\end{tikzpicture}
\end{center}
```

@exm-gauss-jordan-two-by-two step by step. The first step clears below the pivot (ordinary elimination); the second clears above the second pivot, which is the extra work of Gauss–Jordan. The right half, shaded at the end, is $A^{-1}$.

:::

::: {#rmk-inverse-matrices-1 .remark name="Do not compute inverses to solve equations"}

To solve $A\mathbf{x}=\mathbf{b}$ one never needs $A^{-1}$: elimination and back substitution cost about a third as much as computing the inverse, and are more accurate.

:::
