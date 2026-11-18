---
title: "Matrix Spaces and Rank One Matrices"
sources: [mit1806-11]
requires: [math/linear-algebra/vector-spaces/four-fundamental-subspaces]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 11, in our own wording; proofs written out in steps. -->

Vector spaces need not consist of columns. The ideas of basis and dimension apply unchanged.

::: {#exm-space-of-matrices .example name="Spaces of 3 by 3 matrices"}

Let $M$ be the space of all real $3\times3$ matrices. The nine matrices with a single entry $1$ form a basis, so $\dim M=9$. Inside $M$:

1. the symmetric matrices $S$ have $\dim S=6$ (choose the diagonal and the entries above it);
2. the upper triangular matrices $U$ have $\dim U=6$;
3. $S\cap U$ is the diagonal matrices, of dimension $3$;
4. $S+U=\{s+u:s\in S,u\in U\}$ is all of $M$, of dimension $9$.

Note $\dim S+\dim U=12=\dim(S+U)+\dim(S\cap U)$.

:::

::: {#thm-dimension-of-sum .theorem name="Dimension of a sum of subspaces"}

For finite-dimensional subspaces $V$ and $W$ of a vector space,
$$\dim(V+W)+\dim(V\cap W)=\dim V+\dim W,$$
where $V+W=\{\mathbf{v}+\mathbf{w}:\mathbf{v}\in V,\mathbf{w}\in W\}$.

:::

::: {.proof}

1. Take a basis $\mathbf{u}_1,\dots,\mathbf{u}_k$ of $V\cap W$ and extend it to a basis $\mathbf{u}_i,\mathbf{v}_1,\dots,\mathbf{v}_p$ of $V$ and to a basis $\mathbf{u}_i,\mathbf{w}_1,\dots,\mathbf{w}_q$ of $W$ (extension works as in step 2 of @cor-basis-from-independent-set).

2. The list $\mathbf{u}_i,\mathbf{v}_j,\mathbf{w}_l$ spans $V+W$.

3. It is independent: if $\sum a_i\mathbf{u}_i+\sum b_j\mathbf{v}_j+\sum c_l\mathbf{w}_l=\mathbf{0}$, then $\sum c_l\mathbf{w}_l=-\sum a_i\mathbf{u}_i-\sum b_j\mathbf{v}_j$ lies in $V\cap W$, so it is a combination of the $\mathbf{u}_i$. Independence of the basis of $W$ forces all $c_l=0$, and then independence of the basis of $V$ forces all $a_i,b_j=0$.

4. Counting, $\dim(V+W)=k+p+q=(k+p)+(k+q)-k$.

:::

::: {#exm-solution-space-of-ode .example name="Solutions of a differential equation"}

The solutions of $y''+y=0$ form a vector space: combinations of solutions are solutions. It has basis $\cos x$, $\sin x$, so its dimension is $2$. The complete solution $y=c_1\cos x+c_2\sin x$ is the analogue of the nullspace of a matrix.

:::

::: {#def-rank-one-matrix .definition name="Rank one matrix"}

An $m\times n$ matrix has *rank one* when it can be written as
$$A=\mathbf{u}\mathbf{v}^{\mathsf T},\qquad \mathbf{u}\in\mathbb{R}^m,\ \mathbf{v}\in\mathbb{R}^n,\ \mathbf{u},\mathbf{v}\neq\mathbf{0}.$$
Every column is a multiple of $\mathbf{u}$ and every row is a multiple of $\mathbf{v}^{\mathsf T}$.

:::

::: {#prp-rank-one-iff .proposition name="Rank one matrices"}

A matrix has rank $1$ if and only if it has the form $\mathbf{u}\mathbf{v}^{\mathsf T}$ with nonzero $\mathbf{u},\mathbf{v}$. A matrix of rank $r$ is a sum of $r$ rank one matrices.

:::

::: {.proof}

1. Column $j$ of $\mathbf{u}\mathbf{v}^{\mathsf T}$ is $v_j\mathbf{u}$, so $C(\mathbf{u}\mathbf{v}^{\mathsf T})$ is the line through $\mathbf{u}$ and the rank is $1$.

2. Conversely, if $\operatorname{rank}A=1$, $C(A)$ is a line through some $\mathbf{u}\neq\mathbf{0}$, so column $j$ is $v_j\mathbf{u}$ for some numbers $v_j$, not all zero. Then $A=\mathbf{u}\mathbf{v}^{\mathsf T}$.

3. For rank $r$, let $C$ hold the $r$ pivot columns of $A$ and let $R'$ hold the $r$ nonzero rows of $\operatorname{rref}(A)$. Then $A=CR'$ (each column of $A$ is the combination of pivot columns recorded in the matching column of $R'$), and columns times rows (@thm-four-ways-to-multiply) writes $CR'$ as a sum of $r$ rank one matrices.

:::

::: {#rmk-matrix-spaces-and-rank-one-1 .remark name="Rank one matrices do not form a subspace"}

The sum of two rank one matrices usually has rank $2$, so the matrices of rank $1$ (or of any fixed rank) are not a subspace. In contrast, $\{\mathbf{v}\in\mathbb{R}^4:v_1+v_2+v_3+v_4=0\}$ is a subspace: it is the nullspace of the $1\times4$ matrix $[1\ 1\ 1\ 1]$, of dimension $4-1=3$.

:::
