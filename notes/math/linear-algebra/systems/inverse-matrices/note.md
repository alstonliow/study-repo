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

For example $A=\begin{bmatrix}1&3\\2&6\end{bmatrix}$ is singular: $A\,(3,-1)=\mathbf{0}$. Its columns lie on one line, so $A\mathbf{x}=\mathbf{b}$ cannot be solved for every $\mathbf{b}$.

::: {#prp-inverse-of-product .proposition name="Inverse of a product"}

If $A$ and $B$ are invertible $n\times n$ matrices, then $AB$ is invertible and
$$(AB)^{-1}=B^{-1}A^{-1}.$$

:::

::: {.proof}

1. $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AA^{-1}=I$.

2. $(B^{-1}A^{-1})(AB)=B^{-1}(A^{-1}A)B=B^{-1}B=I$.

:::

The order reverses, as with taking off shoes after socks. The inverse of an elimination matrix $E_{ij}$ adds back what $E_{ij}$ subtracted: it is $I$ with $+\ell_{ij}$ in position $(i,j)$.

::: {#def-gauss-jordan .definition name="Gauss–Jordan elimination"}

To compute $A^{-1}$ for an $n\times n$ matrix $A$, apply elimination to the $n\times 2n$ matrix $[A\ I]$: first downwards to make $A$ upper triangular, then upwards to clear the entries above the pivots, and finally divide each row by its pivot. If $A$ has $n$ pivots the result is $[I\ A^{-1}]$.

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

::: {#rmk-inverse-matrices-1 .remark name="Do not compute inverses to solve equations"}

To solve $A\mathbf{x}=\mathbf{b}$ one never needs $A^{-1}$: elimination and back substitution cost about a third as much as computing the inverse, and are more accurate.

:::
