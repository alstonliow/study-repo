---
title: "Change of Basis, Equivalent Matrices and Rank"
sources: [camib-la-2]
requires: [math/linear-algebra/linear-maps/matrices-of-linear-maps, math/linear-algebra/linear-maps/rank-nullity, math/linear-algebra/positive-definite/change-of-basis]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Sections 2.4 and 2.5, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 treats change of basis for one space (thm-change-of-basis-similar) and proves row rank = column rank by elimination (thm-fundamental-theorem-dimensions); the two-basis change and the rank normal form here carry generalizes= and related=. -->

Let $\alpha:U\to V$ with $\dim U=m$, $\dim V=n$. Changing the bases of $U$ and $V$ changes the matrix of $\alpha$; this note finds how, and what is left unchanged.

::: {#thm-change-of-basis-two-spaces .theorem name="Change of basis"}

Let $\mathcal B,\mathcal B'$ be bases of $U$ and $\mathcal C,\mathcal C'$ bases of $V$. Let $P\in\operatorname{GL}_m(F)$ be the matrix whose column $j$ is $[e_j']_{\mathcal B}$, and $Q\in\operatorname{GL}_n(F)$ the matrix whose column $j$ is $[f_j']_{\mathcal C}$. Then
$$[\alpha]_{\mathcal B',\mathcal C'}=Q^{-1}\,[\alpha]_{\mathcal B,\mathcal C}\,P.$$

:::

::: {.proof}

1. $P=[\iota_U]_{\mathcal B',\mathcal B}$ is the matrix of the identity map of $U$ from the new basis to the old (@def-matrix-of-linear-map), and likewise $Q=[\iota_V]_{\mathcal C',\mathcal C}$. These are invertible with $Q^{-1}=[\iota_V]_{\mathcal C,\mathcal C'}$, by @thm-matrix-of-linear-map item 3 applied to $\iota_V\iota_V=\iota_V$.

2. Write $\alpha=\iota_V\,\alpha\,\iota_U$ and apply @thm-matrix-of-linear-map item 3:
$$[\alpha]_{\mathcal B',\mathcal C'}=[\iota_V]_{\mathcal C,\mathcal C'}\,[\alpha]_{\mathcal B,\mathcal C}\,[\iota_U]_{\mathcal B',\mathcal B}=Q^{-1}[\alpha]_{\mathcal B,\mathcal C}P.$$

:::

::: {#def-equivalent-matrices .definition name="Equivalent matrices"}

$A,B\in\operatorname{Mat}_{n,m}(F)$ are *equivalent* if $B=Q^{-1}AP$ for some invertible $P\in\operatorname{GL}_m(F)$ and $Q\in\operatorname{GL}_n(F)$.

:::

Equivalence is an equivalence relation, and by @thm-change-of-basis-two-spaces two matrices are equivalent exactly when they represent the same linear map in different bases (every invertible $P$ is the matrix of some change of basis: take its columns as the coordinates of the new basis vectors).

::: {#thm-rank-normal-form .theorem name="Rank normal form"}

If $\alpha:U\to V$ has rank $r$, there are bases of $U$ and $V$ in which
$$[\alpha]=\begin{bmatrix}I_r&0\\0&0\end{bmatrix}.$$
Hence two $n\times m$ matrices are equivalent if and only if they have the same rank, where the rank of a matrix is the rank of $\mathbf x\mapsto A\mathbf x$, the dimension of its column space.

:::

::: {.proof}

1. Choose a basis $e_{r+1},\dots,e_m$ of $\ker\alpha$, which has dimension $m-r$ (@thm-rank-nullity), and extend it to a basis $e_1,\dots,e_m$ of $U$.

2. As in the direct proof of @thm-rank-nullity, $f_i=\alpha(e_i)$ for $i\le r$ form a basis of $\operatorname{im}\alpha$. Extend it to a basis $f_1,\dots,f_n$ of $V$.

3. Then $\alpha(e_j)=f_j$ for $j\le r$ and $\alpha(e_j)=0$ for $j>r$, which is the stated matrix.

4. Equivalent matrices represent the same map, so have the same rank. Conversely, two matrices of rank $r$ are both equivalent to the normal form, hence to each other.

:::

::: {#thm-row-rank-equals-column-rank .theorem name="Row rank equals column rank" related="thm-fundamental-theorem-dimensions"}

For every $A\in\operatorname{Mat}_{n,m}(F)$, the column space and row space of $A$ have the same dimension: $r(A)=r(A^{\mathsf T})$.

:::

::: {.proof}

1. By @thm-rank-normal-form, $Q^{-1}AP=N$ with $N=\begin{bmatrix}I_r&0\\0&0\end{bmatrix}$ ($n\times m$) and $r=r(A)$.

2. Transposing, $P^{\mathsf T}A^{\mathsf T}(Q^{\mathsf T})^{-1}=N^{\mathsf T}$, which is the $m\times n$ normal form with the same $r$. Since $P^{\mathsf T}$ and $Q^{\mathsf T}$ are invertible, $A^{\mathsf T}$ is equivalent to $N^{\mathsf T}$, whose rank is $r$.

:::

A second proof through dual spaces is @thm-dual-map-rank.

::: {#def-elementary-matrices .definition name="Elementary matrices" generalizes="def-elimination-matrix"}

The *elementary matrices* in $\operatorname{GL}_n(F)$ are

1. $S_{ij}$ ($i\ne j$): the identity with rows $i$ and $j$ exchanged;
2. $E_{ij}(\lambda)$ ($i\ne j$): the identity with an extra entry $\lambda$ in position $(i,j)$;
3. $T_i(\lambda)$ ($\lambda\ne0$): the identity with entry $(i,i)$ replaced by $\lambda$.

Multiplying $A$ on the left by one of them exchanges two rows, adds $\lambda$ times row $j$ to row $i$, or scales row $i$ by $\lambda$; multiplying on the right does the same to columns. Each is invertible, with inverse $S_{ij}$, $E_{ij}(-\lambda)$, $T_i(\lambda^{-1})$.

:::

::: {#prp-normal-form-by-elementary-operations .proposition name="Reduction by row and column operations"}

Every $A\in\operatorname{Mat}_{n,m}(F)$ can be brought to $\begin{bmatrix}I_r&0\\0&0\end{bmatrix}$ by elementary row and column operations. Consequently every invertible matrix is a product of elementary matrices.

:::

::: {.proof}

1. If $A=0$, stop with $r=0$. Otherwise move a non-zero entry to position $(1,1)$ by a row and a column exchange, and scale row $1$ to make it $1$.

2. Subtract multiples of row $1$ from the other rows, and of column $1$ from the other columns, to clear the rest of the first row and column. The matrix is now $\begin{bmatrix}1&0\\0&A'\end{bmatrix}$.

3. Operations on the rows and columns $2,3,\dots$ do not disturb the first row and column, so by induction on the size, $A'$ can be reduced the same way.

4. For invertible $A\in\operatorname{GL}_n(F)$ the result is $I_n$ (the rank is $n$), so $E_k\cdots E_1AE_1'\cdots E_l'=I$ and $A=E_1^{-1}\cdots E_k^{-1}E_l'^{-1}\cdots E_1'^{-1}$, a product of elementary matrices.

:::

```{=latex}
\begin{algorithm}
\caption{Reduction to rank normal form}
\begin{algorithmic}
\INPUT A matrix $A\in\operatorname{Mat}_{n,m}(F)$
\OUTPUT The rank $r$, with $A$ reduced to $\begin{bmatrix}I_r&0\\0&0\end{bmatrix}$ by row and column operations
\STATE $r\gets0$
\WHILE{the block of rows and columns $r+1,\dots$ contains a non-zero entry $a_{ij}$}
    \STATE exchange rows $r+1,i$ and columns $r+1,j$; divide row $r+1$ by its pivot
    \STATE subtract multiples of row $r+1$ from the rows below it and of column $r+1$ from the columns to its right, to clear them
    \STATE $r\gets r+1$
\ENDWHILE
\RETURN $r$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-rank-normal-form .example name="Reducing a rank-one matrix"}

$A=\begin{bmatrix}1&2&3\\2&4&6\end{bmatrix}$ has rank $1$. Subtracting $2\times$ row $1$ from row $2$ gives $\begin{bmatrix}1&2&3\\0&0&0\end{bmatrix}$; subtracting $2\times$ column $1$ from column $2$ and $3\times$ column $1$ from column $3$ gives $\begin{bmatrix}1&0&0\\0&0&0\end{bmatrix}$. In terms of bases: $e_2'=(-2,1,0)^{\mathsf T}$ and $e_3'=(-3,0,1)^{\mathsf T}$ span $\ker A$, $e_1'=(1,0,0)^{\mathsf T}$ maps to $f_1'=(1,2)^{\mathsf T}$, and $f_2'=(0,1)^{\mathsf T}$ completes a basis of $F^2$.

:::

::: {#fig-equivalence-and-rank-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$3$};
\draw[cell frame] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$2$};
\draw[cell frame] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$4$};
\draw[cell frame] (1.100,-0.550) rectangle (1.650,0.000);
\node[lab] at (1.375,-0.275) {$6$};
\draw[cell frame] (3.600,0.000) rectangle (4.150,0.550);
\node[lab] at (3.875,0.275) {$1$};
\draw[cell frame] (4.150,0.000) rectangle (4.700,0.550);
\node[lab] at (4.425,0.275) {$2$};
\draw[cell frame] (4.700,0.000) rectangle (5.250,0.550);
\node[lab] at (4.975,0.275) {$3$};
\draw[hl cell] (3.600,-0.550) rectangle (4.150,0.000);
\node[lab] at (3.875,-0.275) {$0$};
\draw[hl cell] (4.150,-0.550) rectangle (4.700,0.000);
\node[lab] at (4.425,-0.275) {$0$};
\draw[hl cell] (4.700,-0.550) rectangle (5.250,0.000);
\node[lab] at (4.975,-0.275) {$0$};
\draw[cell frame] (8.000,0.000) rectangle (8.550,0.550);
\node[lab] at (8.275,0.275) {$1$};
\draw[hl cell] (8.550,0.000) rectangle (9.100,0.550);
\node[lab] at (8.825,0.275) {$0$};
\draw[hl cell] (9.100,0.000) rectangle (9.650,0.550);
\node[lab] at (9.375,0.275) {$0$};
\draw[cell frame] (8.000,-0.550) rectangle (8.550,0.000);
\node[lab] at (8.275,-0.275) {$0$};
\draw[cell frame] (8.550,-0.550) rectangle (9.100,0.000);
\node[lab] at (8.825,-0.275) {$0$};
\draw[cell frame] (9.100,-0.550) rectangle (9.650,0.000);
\node[lab] at (9.375,-0.275) {$0$};
\draw[map] (1.8,0.25) -- (3.45,0.25) node[midway, edge label, above=2pt] {$R_2-2R_1$};
\draw[map] (5.4,0.25) -- (7.85,0.25) node[midway, edge label, above=2pt] {$C_2-2C_1,\ C_3-3C_1$};
\node[lab] at (0.825,-0.9) {$A$};
\node[lab] at (8.825,-1.0) {$\begin{bmatrix}I_1&0\\0&0\end{bmatrix}$};
\end{tikzpicture}
\end{center}
```

Reducing $A$ of @exm-rank-normal-form to its rank normal form: one row operation clears the second row, two column operations clear the first row. Highlighted cells changed in that step.

:::
