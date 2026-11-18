---
title: "The Nullspace and Solving Ax = 0"
sources: [mit1806-6, mit1806-7]
requires: [math/linear-algebra/vector-spaces/vector-spaces-and-subspaces]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lectures 6 and 7, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-nullspace .definition name="Nullspace"}

The *nullspace* of an $m\times n$ matrix $A$ is
$$N(A)=\{\mathbf{x}\in\mathbb{R}^n: A\mathbf{x}=\mathbf{0}\}.$$
It is a subspace of $\mathbb{R}^n$: if $A\mathbf{x}=A\mathbf{y}=\mathbf{0}$ then $A(c\mathbf{x}+d\mathbf{y})=\mathbf{0}$.

:::

By contrast, the solutions of $A\mathbf{x}=\mathbf{b}$ with $\mathbf{b}\neq\mathbf{0}$ never form a subspace: $\mathbf{0}$ is not a solution.

## Echelon form and reduced row echelon form

Elimination works on rectangular matrices too. When a column has no pivot (all entries at or below the current row are zero), move on to the next column.

::: {#def-echelon-form .definition name="Echelon form, pivot and free variables"}

Elimination on an $m\times n$ matrix $A$ produces an *echelon* (staircase) matrix $U$: the first nonzero entry of each row, its *pivot*, lies to the right of the pivot in the row above, and zero rows come last. The number of pivots is the *rank* $r$ of $A$. The unknowns that belong to pivot columns are *pivot variables*; the other $n-r$ are *free variables*.

:::

::: {#def-reduced-row-echelon-form .definition name="Reduced row echelon form"}

Continuing elimination upwards to clear the entries above each pivot, and dividing each pivot row by its pivot, produces the *reduced row echelon form* $R=\operatorname{rref}(A)$: every pivot is $1$ and is the only nonzero entry in its column. Row operations do not change the nullspace, so
$$N(A)=N(U)=N(R).$$

:::

::: {#thm-special-solutions .theorem name="Special solutions span the nullspace"}

Let $A$ have rank $r$ and $n-r$ free variables. For each free variable, set it to $1$, the other free variables to $0$, and solve $R\mathbf{x}=\mathbf{0}$ for the pivot variables. These $n-r$ *special solutions* are in $N(A)$ and every vector of $N(A)$ is exactly one combination of them.

:::

::: {.proof}

1. In $R$, each nonzero row reads $x_{p}+\sum_{f\text{ free}}r_{f}x_f=0$ for its pivot variable $x_p$. So the free variables can be chosen at will and then determine the pivot variables uniquely.

2. A special solution is such a choice, so it lies in $N(R)=N(A)$.

3. Let $\mathbf{x}\in N(A)$ have free variables $x_{f_1},\dots,x_{f_{n-r}}$. The combination $\mathbf{y}=\sum_kx_{f_k}\mathbf{s}_k$ of the special solutions has the same free variables and is in $N(A)$. By step 1 the pivot variables agree too, so $\mathbf{x}=\mathbf{y}$.

4. The coefficients are forced to be the free variables of $\mathbf{x}$, so the combination is unique.

:::

::: {#cor-more-unknowns-than-equations .corollary name="More unknowns than equations"}

If $n>m$, then $A\mathbf{x}=\mathbf{0}$ has a nonzero solution.

:::

::: {.proof}

1. There is at most one pivot per row, so $r\le m<n$.

2. Hence there is at least one free variable, and its special solution is nonzero.

:::

::: {#exm-nullspace-three-by-four .example name="Nullspace of a 3 by 4 matrix"}

$$A=\begin{bmatrix}1&2&0&1\\2&4&1&4\\3&6&1&5\end{bmatrix}\ \longrightarrow\ R=\begin{bmatrix}1&2&0&1\\0&0&1&2\\0&0&0&0\end{bmatrix}.$$
The pivot columns are $1$ and $3$, so $r=2$ and $x_2,x_4$ are free. The special solutions are
$$\mathbf{s}_1=(-2,1,0,0),\qquad\mathbf{s}_2=(-1,0,-2,1),$$
and $N(A)$ is the plane of all $c\,\mathbf{s}_1+d\,\mathbf{s}_2$ in $\mathbb{R}^4$.

:::

::: {#prp-nullspace-matrix .proposition name="The nullspace matrix"}

If the pivot columns come first, $R=\begin{bmatrix}I&F\\0&0\end{bmatrix}$ with $F$ of size $r\times(n-r)$. Then the special solutions are the columns of
$$N=\begin{bmatrix}-F\\I\end{bmatrix},\qquad RN=0.$$
In general the rows of $N$ are placed in the order of the variables.

:::

::: {.proof}

1. By block multiplication (@prp-block-multiplication), $RN=\begin{bmatrix}-F+F\\0\end{bmatrix}=0$.

2. Column $k$ of $N$ has free part equal to column $k$ of $I$, which is the choice that defines the $k$-th special solution in @thm-special-solutions.

:::
