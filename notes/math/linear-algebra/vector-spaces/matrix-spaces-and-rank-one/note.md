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

<!-- Merged 2026-11-20 (owner): the block thm-dimension-of-sum was removed in favour of thm-dimension-of-sum-and-intersection (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Dimension of a sum.** For finite-dimensional subspaces $V$ and $W$ of a vector space, with $V+W=\{\mathbf{v}+\mathbf{w}\}$,
$$\dim(V+W)+\dim(V\cap W)=\dim V+\dim W.$$
The proof (extend a basis of $V\cap W$ to bases of $V$ and of $W$, and check that the combined list is a basis of $V+W$) is @thm-dimension-of-sum-and-intersection.

::: {#exm-solution-space-of-ode .example name="Solutions of a differential equation"}

The solutions of $y''+y=0$ form a vector space: combinations of solutions are solutions. It has basis $\cos x$, $\sin x$, so its dimension is $2$. The complete solution $y=c_1\cos x+c_2\sin x$ is the analogue of the nullspace of a matrix.

:::

::: {#def-rank-one-matrix .definition name="Rank one matrix"}

An $m\times n$ matrix has *rank one* when it can be written as
$$A=\mathbf{u}\mathbf{v}^{\mathsf T},\qquad \mathbf{u}\in\mathbb{R}^m,\ \mathbf{v}\in\mathbb{R}^n,\ \mathbf{u},\mathbf{v}\neq\mathbf{0}.$$
Every column is a multiple of $\mathbf{u}$ and every row is a multiple of $\mathbf{v}^{\mathsf T}$.

:::

::: {#fig-matrix-spaces-and-rank-one-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.62]
\foreach \i in {1,2,3} \draw[cell frame, fill=primaryLight] (0,-\i) rectangle node[tick] {$u_{\i}$} (1,-\i+1);
\foreach \j in {1,...,4} \draw[cell frame, fill=accentLight] (0.4+\j,-1) rectangle node[tick] {$v_{\j}$} (1.4+\j,-2);
\node[lab] at (6.9,-1.5) {$=$};
\foreach \i in {1,2,3} \foreach \j in {1,...,4} \draw[cell frame, fill=primarySoft] (6.1+1.3*\j,-\i) rectangle node[tick] {$u_{\i}v_{\j}$} (7.4+1.3*\j,-\i+1);
\node[lab] at (0.5,-3.6) {$\mathbf u$}; \node[lab] at (3.4,-2.6) {$\mathbf v^{\mathsf T}$}; \node[lab] at (10.1,-3.6) {$\mathbf u\mathbf v^{\mathsf T}$};
\end{tikzpicture}
\end{center}
```

A rank one matrix $\mathbf u\mathbf v^{\mathsf T}$ ($3\times4$ here). Its $(i,j)$ entry is $u_iv_j$: column $j$ is $v_j\mathbf u$ and row $i$ is $u_i\mathbf v^{\mathsf T}$.

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
