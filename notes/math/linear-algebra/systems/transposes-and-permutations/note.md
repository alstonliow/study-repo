---
title: "Transposes and Permutations"
sources: [mit1806-5]
requires: [math/linear-algebra/systems/lu-factorization]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 5 (first half), in our own wording; proofs written out in steps. -->

::: {#def-transpose .definition name="Transpose"}

The *transpose* of an $m\times n$ matrix $A$ is the $n\times m$ matrix $A^{\mathsf T}$ with
$$(A^{\mathsf T})_{ij}=a_{ji}.$$
The columns of $A^{\mathsf T}$ are the rows of $A$. A column vector $\mathbf{x}$ becomes the row vector $\mathbf{x}^{\mathsf T}$, and $\mathbf{x}\cdot\mathbf{y}=\mathbf{x}^{\mathsf T}\mathbf{y}$.

:::

::: {#fig-transposes-and-permutations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.7]
\foreach \i/\j/\v in {1/1/1,1/2/2,1/3/3,2/1/4,2/2/5,2/3/6} \draw[cell frame] (\j-1,-\i) rectangle node[lab] {$\v$} (\j,-\i+1);
\foreach \j/\v in {1/1,2/2,3/3} \draw[hl cell] (\j-1,-1) rectangle node[lab] {$\v$} (\j,0);
\draw[map] (3.4,-1) -- (4.6,-1);
\foreach \i/\j/\v in {1/1/1,2/1/2,3/1/3,1/2/4,2/2/5,3/2/6} \draw[cell frame] (4.8+\j,-\i+0.5) rectangle node[lab] {$\v$} (5.8+\j,-\i+1.5);
\foreach \i/\v in {1/1,2/2,3/3} \draw[hl cell] (5.8,-\i+0.5) rectangle node[lab] {$\v$} (6.8,-\i+1.5);
\node[lab] at (1.5,-2.6) {$A$}; \node[lab] at (6.8,-3.1) {$A^{\mathsf T}$};
\end{tikzpicture}
\end{center}
```

The transpose turns rows into columns: row $1$ of $A$ (highlighted) becomes column $1$ of $A^{\mathsf T}$, so $(A^{\mathsf T})_{ij}=A_{ji}$ and a $2\times3$ matrix becomes $3\times2$.

:::

::: {#prp-transpose-rules .proposition name="Rules for transposes"}

Whenever the operations are defined,
$$(A+B)^{\mathsf T}=A^{\mathsf T}+B^{\mathsf T},\qquad (AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T},\qquad (A^{-1})^{\mathsf T}=(A^{\mathsf T})^{-1}.$$
Also $(A\mathbf{x})\cdot\mathbf{y}=\mathbf{x}\cdot(A^{\mathsf T}\mathbf{y})$.

:::

::: {.proof}

1. The first rule holds entry by entry.

2. Entry $(i,j)$ of $(AB)^{\mathsf T}$ is entry $(j,i)$ of $AB$, which is $\sum_ka_{jk}b_{ki}=\sum_k(B^{\mathsf T})_{ik}(A^{\mathsf T})_{kj}$, entry $(i,j)$ of $B^{\mathsf T}A^{\mathsf T}$.

3. Transposing $AA^{-1}=I$ with step 2 gives $(A^{-1})^{\mathsf T}A^{\mathsf T}=I$; transposing $A^{-1}A=I$ gives $A^{\mathsf T}(A^{-1})^{\mathsf T}=I$. So $(A^{-1})^{\mathsf T}$ is the inverse of $A^{\mathsf T}$.

4. $(A\mathbf{x})\cdot\mathbf{y}=(A\mathbf{x})^{\mathsf T}\mathbf{y}=\mathbf{x}^{\mathsf T}A^{\mathsf T}\mathbf{y}=\mathbf{x}\cdot(A^{\mathsf T}\mathbf{y})$ by step 2.

:::

::: {#fig-transposes-and-permutations-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0,0) rectangle (1.4,-0.8); \node[lab] at (0.7,-0.4) {$AB$};
\node[lab, tick] at (0.7,-1.05) {$m\times p$};
\draw[->] (1.6,-0.4) -- (2.3,-0.4) node[midway, above, lab, note] {${}^{\mathsf T}$};
\draw[hl cell] (2.5,0) rectangle (3.3,-1.4); \node[lab] at (2.9,-0.7) {\scriptsize$(AB)^{\mathsf T}$};
\node[lab, tick] at (2.9,-1.65) {$p\times m$};
\node[lab] at (3.6,-0.7) {$=$};
\draw[cell frame] (3.9,0) rectangle (5.7,-1.4); \node[lab] at (4.8,-0.7) {$B^{\mathsf T}$};
\node[lab, tick] at (4.8,-1.65) {$p\times n$};
\draw[cell frame] (5.9,0) rectangle (6.7,-1.8); \node[lab] at (6.30,-0.9) {$A^{\mathsf T}$};
\node[lab, tick] at (6.3,-2.05) {$n\times m$};
\end{tikzpicture}
\end{center}
```

Why the order reverses in $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$: with $A$ of size $m\times n$ and $B$ of size $n\times p$, the shapes only fit in that order. The product $A^{\mathsf T}B^{\mathsf T}$ would need $m=p$.

:::

::: {#def-symmetric-matrix .definition name="Symmetric matrix"}

A square matrix $S$ is *symmetric* if $S^{\mathsf T}=S$, that is $s_{ij}=s_{ji}$ for all $i,j$.

:::

::: {#fig-transposes-and-permutations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell, fill=primaryLight] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$2$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$3$};
\draw[cell, fill=primaryLight] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[hl cell] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$4$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$5$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$3$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$5$};
\draw[hl cell] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$6$};
\draw[cell, fill=secondarySoft] (1.1,1.65) rectangle (1.65,1.1); \node[lab] at (1.375,1.375) {$3$};
\draw[cell, fill=secondarySoft] (0,0.55) rectangle (0.55,0); \node[lab] at (0.275,0.275) {$3$};
\draw[cell, fill=accentSoft] (1.1,1.1) rectangle (1.65,0.55); \node[lab] at (1.375,0.825) {$5$};
\draw[cell, fill=accentSoft] (0.55,0.55) rectangle (1.1,0); \node[lab] at (0.825,0.275) {$5$};
\draw[dashed, faint] (-0.2,1.85) -- (1.85,-0.2);
\node[lab, note, anchor=west, align=left] at (2.2,0.825) {$s_{ij}=s_{ji}$:\\mirror image in\\the main diagonal};
\end{tikzpicture}
\end{center}
```

A symmetric matrix equals its transpose: entries in mirror positions across the main diagonal (same shade) are equal, and the diagonal (highlighted) is free.

:::

::: {#prp-ata-symmetric .proposition name="A^T A is symmetric"}

For every $m\times n$ matrix $R$, the $n\times n$ matrix $R^{\mathsf T}R$ and the $m\times m$ matrix $RR^{\mathsf T}$ are symmetric.

:::

::: {.proof}

1. $(R^{\mathsf T}R)^{\mathsf T}=R^{\mathsf T}(R^{\mathsf T})^{\mathsf T}=R^{\mathsf T}R$ by @prp-transpose-rules.

2. The same computation applies to $RR^{\mathsf T}$.

:::

::: {#prp-symmetric-ldlt .proposition name="Symmetric LU is LDL^T"}

If a symmetric matrix $S$ has $S=LDU$ as in @cor-ldu-factorization, then $U=L^{\mathsf T}$, so $S=LDL^{\mathsf T}$.

:::

::: {.proof}

1. Transposing $S=LDU$ gives $S=S^{\mathsf T}=U^{\mathsf T}DL^{\mathsf T}$, again lower triangular with unit diagonal, times diagonal, times upper triangular with unit diagonal.

2. By uniqueness in @cor-ldu-factorization, $L=U^{\mathsf T}$.

:::

::: {#def-permutation-matrix .definition name="Permutation matrix"}

A *permutation matrix* is $I$ with its rows in some order. Equivalently it has exactly one $1$ in each row and each column and $0$s elsewhere. Multiplying $PA$ puts the rows of $A$ in that order. There are $n!$ permutation matrices of size $n$. Each row exchange $P_{ij}$ (@def-permutation-matrix-row-exchange) is one of them.

:::

::: {#prp-permutation-inverse-transpose .proposition name="P^{-1} = P^T"}

Every permutation matrix satisfies $P^{\mathsf T}P=I$, so $P^{-1}=P^{\mathsf T}$. The product of two permutation matrices is a permutation matrix.

:::

::: {.proof}

1. Entry $(i,j)$ of $P^{\mathsf T}P$ is the dot product of columns $i$ and $j$ of $P$.

2. Each column has a single $1$ and different columns have their $1$ in different rows. So the dot product is $1$ for $i=j$ and $0$ otherwise.

3. $P_1P_2A$ puts the rows of $A$ in one order and then reorders them again, which is again an ordering of the rows of $I$ when $A=I$.

:::

::: {#exm-three-by-three-permutation-matrices .example name="The six 3 by 3 permutation matrices"}

Besides $I$ there are the three row exchanges $P_{12},P_{13},P_{23}$ and the two cyclic shifts
$$\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix},\qquad\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix},$$
which are inverse to each other (and transposes of each other).

:::

::: {#fig-transposes-and-permutations-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.800) rectangle (0.400,1.200);
\node[lab] at (0.200,1.000) {$1$};
\draw[cell frame] (0.400,0.800) rectangle (0.800,1.200);
\draw[cell frame] (0.800,0.800) rectangle (1.200,1.200);
\draw[cell frame] (0.000,0.400) rectangle (0.400,0.800);
\draw[hl cell] (0.400,0.400) rectangle (0.800,0.800);
\node[lab] at (0.600,0.600) {$1$};
\draw[cell frame] (0.800,0.400) rectangle (1.200,0.800);
\draw[cell frame] (0.000,-0.000) rectangle (0.400,0.400);
\draw[cell frame] (0.400,-0.000) rectangle (0.800,0.400);
\draw[hl cell] (0.800,-0.000) rectangle (1.200,0.400);
\node[lab] at (1.000,0.200) {$1$};
\node[lab, note] at (0.600,-0.300) {$I$};
\draw[cell frame] (2.000,0.800) rectangle (2.400,1.200);
\draw[hl cell] (2.400,0.800) rectangle (2.800,1.200);
\node[lab] at (2.600,1.000) {$1$};
\draw[cell frame] (2.800,0.800) rectangle (3.200,1.200);
\draw[hl cell] (2.000,0.400) rectangle (2.400,0.800);
\node[lab] at (2.200,0.600) {$1$};
\draw[cell frame] (2.400,0.400) rectangle (2.800,0.800);
\draw[cell frame] (2.800,0.400) rectangle (3.200,0.800);
\draw[cell frame] (2.000,-0.000) rectangle (2.400,0.400);
\draw[cell frame] (2.400,-0.000) rectangle (2.800,0.400);
\draw[hl cell] (2.800,-0.000) rectangle (3.200,0.400);
\node[lab] at (3.000,0.200) {$1$};
\node[lab, note] at (2.600,-0.300) {$P_{12}$};
\draw[cell frame] (4.000,0.800) rectangle (4.400,1.200);
\draw[cell frame] (4.400,0.800) rectangle (4.800,1.200);
\draw[hl cell] (4.800,0.800) rectangle (5.200,1.200);
\node[lab] at (5.000,1.000) {$1$};
\draw[cell frame] (4.000,0.400) rectangle (4.400,0.800);
\draw[hl cell] (4.400,0.400) rectangle (4.800,0.800);
\node[lab] at (4.600,0.600) {$1$};
\draw[cell frame] (4.800,0.400) rectangle (5.200,0.800);
\draw[hl cell] (4.000,-0.000) rectangle (4.400,0.400);
\node[lab] at (4.200,0.200) {$1$};
\draw[cell frame] (4.400,-0.000) rectangle (4.800,0.400);
\draw[cell frame] (4.800,-0.000) rectangle (5.200,0.400);
\node[lab, note] at (4.600,-0.300) {$P_{13}$};
\draw[hl cell] (6.000,0.800) rectangle (6.400,1.200);
\node[lab] at (6.200,1.000) {$1$};
\draw[cell frame] (6.400,0.800) rectangle (6.800,1.200);
\draw[cell frame] (6.800,0.800) rectangle (7.200,1.200);
\draw[cell frame] (6.000,0.400) rectangle (6.400,0.800);
\draw[cell frame] (6.400,0.400) rectangle (6.800,0.800);
\draw[hl cell] (6.800,0.400) rectangle (7.200,0.800);
\node[lab] at (7.000,0.600) {$1$};
\draw[cell frame] (6.000,-0.000) rectangle (6.400,0.400);
\draw[hl cell] (6.400,-0.000) rectangle (6.800,0.400);
\node[lab] at (6.600,0.200) {$1$};
\draw[cell frame] (6.800,-0.000) rectangle (7.200,0.400);
\node[lab, note] at (6.600,-0.300) {$P_{23}$};
\draw[cell frame] (8.000,0.800) rectangle (8.400,1.200);
\draw[hl cell] (8.400,0.800) rectangle (8.800,1.200);
\node[lab] at (8.600,1.000) {$1$};
\draw[cell frame] (8.800,0.800) rectangle (9.200,1.200);
\draw[cell frame] (8.000,0.400) rectangle (8.400,0.800);
\draw[cell frame] (8.400,0.400) rectangle (8.800,0.800);
\draw[hl cell] (8.800,0.400) rectangle (9.200,0.800);
\node[lab] at (9.000,0.600) {$1$};
\draw[hl cell] (8.000,-0.000) rectangle (8.400,0.400);
\node[lab] at (8.200,0.200) {$1$};
\draw[cell frame] (8.400,-0.000) rectangle (8.800,0.400);
\draw[cell frame] (8.800,-0.000) rectangle (9.200,0.400);
\node[lab, note] at (8.600,-0.300) {shift};
\draw[cell frame] (10.000,0.800) rectangle (10.400,1.200);
\draw[cell frame] (10.400,0.800) rectangle (10.800,1.200);
\draw[hl cell] (10.800,0.800) rectangle (11.200,1.200);
\node[lab] at (11.000,1.000) {$1$};
\draw[hl cell] (10.000,0.400) rectangle (10.400,0.800);
\node[lab] at (10.200,0.600) {$1$};
\draw[cell frame] (10.400,0.400) rectangle (10.800,0.800);
\draw[cell frame] (10.800,0.400) rectangle (11.200,0.800);
\draw[cell frame] (10.000,-0.000) rectangle (10.400,0.400);
\draw[hl cell] (10.400,-0.000) rectangle (10.800,0.400);
\node[lab] at (10.600,0.200) {$1$};
\draw[cell frame] (10.800,-0.000) rectangle (11.200,0.400);
\node[lab, note] at (10.600,-0.300) {shift back};
\end{tikzpicture}
\end{center}
```

The six $3\times3$ permutation matrices: one $1$ (highlighted) in every row and every column. Row $i$ of $PA$ is the row of $A$ picked out by the $1$ in row $i$ of $P$; the last two are the cyclic shifts of @exm-three-by-three-permutation-matrices.

:::
