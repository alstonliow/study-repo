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

::: {#fig-matrix-spaces-and-rank-one-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.000,0.800) rectangle (0.400,1.200);
\draw[cell, fill=primaryLight] (0.400,0.800) rectangle (0.800,1.200);
\draw[cell, fill=primaryLight] (0.800,0.800) rectangle (1.200,1.200);
\draw[cell, fill=primaryLight] (0.000,0.400) rectangle (0.400,0.800);
\draw[cell, fill=primaryLight] (0.400,0.400) rectangle (0.800,0.800);
\draw[cell, fill=primaryLight] (0.800,0.400) rectangle (1.200,0.800);
\draw[cell, fill=primaryLight] (0.000,-0.000) rectangle (0.400,0.400);
\draw[cell, fill=primaryLight] (0.400,-0.000) rectangle (0.800,0.400);
\draw[cell, fill=primaryLight] (0.800,-0.000) rectangle (1.200,0.400);
\node[lab, note] at (0.600,-0.300) {$M$: $9$};
\draw[cell, fill=primaryLight] (2.000,0.800) rectangle (2.400,1.200);
\draw[cell, fill=primaryLight] (2.400,0.800) rectangle (2.800,1.200);
\draw[cell, fill=primaryLight] (2.800,0.800) rectangle (3.200,1.200);
\draw[cell frame] (2.000,0.400) rectangle (2.400,0.800);
\draw[cell, fill=primaryLight] (2.400,0.400) rectangle (2.800,0.800);
\draw[cell, fill=primaryLight] (2.800,0.400) rectangle (3.200,0.800);
\draw[cell frame] (2.000,-0.000) rectangle (2.400,0.400);
\draw[cell frame] (2.400,-0.000) rectangle (2.800,0.400);
\draw[cell, fill=primaryLight] (2.800,-0.000) rectangle (3.200,0.400);
\node[lab, note] at (2.600,-0.300) {$S$: $6$ choices};
\draw[faint, dashed] (2.0,1.2) -- (3.2,0.0);
\node[lab] at (2.85,1.3) {\scriptsize mirrored};
\draw[cell, fill=primaryLight] (4.000,0.800) rectangle (4.400,1.200);
\draw[cell, fill=primaryLight] (4.400,0.800) rectangle (4.800,1.200);
\draw[cell, fill=primaryLight] (4.800,0.800) rectangle (5.200,1.200);
\draw[cell frame] (4.000,0.400) rectangle (4.400,0.800);
\draw[cell, fill=primaryLight] (4.400,0.400) rectangle (4.800,0.800);
\draw[cell, fill=primaryLight] (4.800,0.400) rectangle (5.200,0.800);
\draw[cell frame] (4.000,-0.000) rectangle (4.400,0.400);
\draw[cell frame] (4.400,-0.000) rectangle (4.800,0.400);
\draw[cell, fill=primaryLight] (4.800,-0.000) rectangle (5.200,0.400);
\node[lab, note] at (4.600,-0.300) {$U$: $6$};
\draw[cell, fill=primaryLight] (6.000,0.800) rectangle (6.400,1.200);
\draw[cell frame] (6.400,0.800) rectangle (6.800,1.200);
\draw[cell frame] (6.800,0.800) rectangle (7.200,1.200);
\draw[cell frame] (6.000,0.400) rectangle (6.400,0.800);
\draw[cell, fill=primaryLight] (6.400,0.400) rectangle (6.800,0.800);
\draw[cell frame] (6.800,0.400) rectangle (7.200,0.800);
\draw[cell frame] (6.000,-0.000) rectangle (6.400,0.400);
\draw[cell frame] (6.400,-0.000) rectangle (6.800,0.400);
\draw[cell, fill=primaryLight] (6.800,-0.000) rectangle (7.200,0.400);
\node[lab, note] at (6.600,-0.300) {$S\cap U$: $3$};
\draw[cell, fill=primaryLight] (8.000,0.800) rectangle (8.400,1.200);
\draw[cell, fill=primaryLight] (8.400,0.800) rectangle (8.800,1.200);
\draw[cell, fill=primaryLight] (8.800,0.800) rectangle (9.200,1.200);
\draw[cell, fill=primaryLight] (8.000,0.400) rectangle (8.400,0.800);
\draw[cell, fill=primaryLight] (8.400,0.400) rectangle (8.800,0.800);
\draw[cell, fill=primaryLight] (8.800,0.400) rectangle (9.200,0.800);
\draw[cell, fill=primaryLight] (8.000,-0.000) rectangle (8.400,0.400);
\draw[cell, fill=primaryLight] (8.400,-0.000) rectangle (8.800,0.400);
\draw[cell, fill=primaryLight] (8.800,-0.000) rectangle (9.200,0.400);
\node[lab, note] at (8.600,-0.300) {$S+U=M$: $9$};
\end{tikzpicture}
\end{center}
```

Counting free entries in @exm-space-of-matrices. A symmetric matrix is fixed by its entries on and above the diagonal (the rest is mirrored), an upper triangular one by the same six positions, and a matrix in both is diagonal. The count checks $6+6=9+3$.

:::

<!-- Merged 2026-11-20 (owner): the block thm-dimension-of-sum was removed in favour of thm-dimension-of-sum-and-intersection (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Dimension of a sum.** For finite-dimensional subspaces $V$ and $W$ of a vector space, with $V+W=\{\mathbf{v}+\mathbf{w}\}$,
$$\dim(V+W)+\dim(V\cap W)=\dim V+\dim W.$$
The proof (extend a basis of $V\cap W$ to bases of $V$ and of $W$, and check that the combined list is a basis of $V+W$) is @thm-dimension-of-sum-and-intersection.

::: {#exm-solution-space-of-ode .example name="Solutions of a differential equation"}

The solutions of $y''+y=0$ form a vector space: combinations of solutions are solutions. It has basis $\cos x$, $\sin x$, so its dimension is $2$. The complete solution $y=c_1\cos x+c_2\sin x$ is the analogue of the nullspace of a matrix.

:::

::: {#fig-matrix-spaces-and-rank-one-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y={(0,0.7cm)}]
\draw[->, muted] (0,0) -- (6.6,0) node[right, lab, tick] {$x$}; \draw[->, muted] (0,-1.5) -- (0,1.6);
\draw[emph, primary, domain=0:6.28, samples=60] plot (\x, {cos(\x r)});
\draw[emph, secondary, domain=0:6.28, samples=60] plot (\x, {sin(\x r)});
\draw[bold, accent, domain=0:6.28, samples=80] plot (\x, {0.8*cos(\x r)+0.6*sin(\x r)});
\node[lab, note, primary] at (6.9,1) {$\cos x$}; \node[lab, note, secondary] at (5.1,-1.2) {$\sin x$};
\node[lab, note, accent, anchor=west] at (6.4,0.55) {$0.8\cos x+0.6\sin x$};
\end{tikzpicture}
\end{center}
```

The solution space of $y''+y=0$ has the basis $\cos x$, $\sin x$; every solution, such as $0.8\cos x+0.6\sin x$, is one combination of them, just as every nullspace vector is a combination of special solutions.

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

::: {#fig-matrix-spaces-and-rank-one-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$1$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$0$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\node[lab, note] at (0.550,-0.350) {rank $1$};
\node[lab] at (1.4,0.55) {$+$};
\draw[cell frame] (1.700,0.550) rectangle (2.250,1.100);
\node[lab] at (1.975,0.825) {$0$};
\draw[cell frame] (2.250,0.550) rectangle (2.800,1.100);
\node[lab] at (2.525,0.825) {$0$};
\draw[cell frame] (1.700,0.000) rectangle (2.250,0.550);
\node[lab] at (1.975,0.275) {$0$};
\draw[hl cell] (2.250,0.000) rectangle (2.800,0.550);
\node[lab] at (2.525,0.275) {$1$};
\node[lab, note] at (2.250,-0.350) {rank $1$};
\node[lab] at (3.1,0.55) {$=$};
\draw[hl cell] (3.400,0.550) rectangle (3.950,1.100);
\node[lab] at (3.675,0.825) {$1$};
\draw[cell frame] (3.950,0.550) rectangle (4.500,1.100);
\node[lab] at (4.225,0.825) {$0$};
\draw[cell frame] (3.400,0.000) rectangle (3.950,0.550);
\node[lab] at (3.675,0.275) {$0$};
\draw[hl cell] (3.950,0.000) rectangle (4.500,0.550);
\node[lab] at (4.225,0.275) {$1$};
\node[lab, note] at (3.950,-0.350) {rank $2$};
\end{tikzpicture}
\end{center}
```

The sum of two rank one matrices can have rank $2$, so the rank one matrices are not closed under addition and do not form a subspace.

:::
