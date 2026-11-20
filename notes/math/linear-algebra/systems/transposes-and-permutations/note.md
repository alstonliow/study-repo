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

::: {#def-symmetric-matrix .definition name="Symmetric matrix"}

A square matrix $S$ is *symmetric* if $S^{\mathsf T}=S$, that is $s_{ij}=s_{ji}$ for all $i,j$.

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
