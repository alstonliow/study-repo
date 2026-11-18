---
title: "Factorization into A = LU"
sources: [mit1806-4]
requires: [math/linear-algebra/systems/inverse-matrices]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 4, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

Elimination produces $EA=U$. Inverting $E$ moves the elimination steps to the other side and records them in a lower triangular matrix.

::: {#thm-lu-factorization .theorem name="A = LU"}

Suppose elimination on the $n\times n$ matrix $A$ needs no row exchanges and finds $n$ pivots. Then
$$A=LU,$$
where $U$ is the upper triangular result of elimination and $L$ is lower triangular with $1$s on the diagonal and the multiplier $\ell_{ij}$ (@def-gaussian-elimination) in position $(i,j)$ below the diagonal.

:::

::: {.proof}

1. Elimination in the usual order gives $E_{n,n-1}\cdots E_{31}E_{21}A=U$. By @prp-inverse-of-product,
   $$A=E_{21}^{-1}E_{31}^{-1}\cdots E_{n,n-1}^{-1}\,U.$$

2. Each $E_{ij}^{-1}=I+\ell_{ij}\mathbf{e}_i\mathbf{e}_j^{\mathsf T}$, where $\mathbf{e}_i$ is column $i$ of $I$. For a fixed column $j$ let $\mathbf{u}_j=\sum_{i>j}\ell_{ij}\mathbf{e}_i$. The factors belonging to column $j$ multiply to $L_j=I+\mathbf{u}_j\mathbf{e}_j^{\mathsf T}$, because $\mathbf{e}_j^{\mathsf T}\mathbf{e}_i=0$ for $i>j$ kills every cross term.

3. So $L=L_1L_2\cdots L_{n-1}$. For $j<k$,
   $$(I+\mathbf{u}_j\mathbf{e}_j^{\mathsf T})(I+\mathbf{u}_k\mathbf{e}_k^{\mathsf T})=I+\mathbf{u}_j\mathbf{e}_j^{\mathsf T}+\mathbf{u}_k\mathbf{e}_k^{\mathsf T}+\mathbf{u}_j(\mathbf{e}_j^{\mathsf T}\mathbf{u}_k)\mathbf{e}_k^{\mathsf T},$$
   and $\mathbf{e}_j^{\mathsf T}\mathbf{u}_k=0$ since $\mathbf{u}_k$ has nonzero entries only in positions $>k>j$. By induction on the number of factors, $L=I+\sum_j\mathbf{u}_j\mathbf{e}_j^{\mathsf T}$.

4. This is the lower triangular matrix with $1$s on the diagonal and $\ell_{ij}$ in position $(i,j)$: the multipliers land in $L$ unchanged.

:::

The opposite product $E=E_{n,n-1}\cdots E_{21}$ mixes the multipliers; in @exm-elimination-three-by-three, $E$ has entry $(3,1)$ equal to $-12$, not $-4$. That is why $L$, not $E$, is the matrix to keep.

::: {#exm-lu-three-by-three .example name="LU of the 3 by 3 example"}

From @exm-elimination-three-by-three, with multipliers $\ell_{21}=2$, $\ell_{31}=4$, $\ell_{32}=-4$:
$$\begin{bmatrix}1&1&1\\2&3&5\\4&0&5\end{bmatrix}=\begin{bmatrix}1&0&0\\2&1&0\\4&-4&1\end{bmatrix}\begin{bmatrix}1&1&1\\0&1&3\\0&0&13\end{bmatrix}.$$

:::

::: {#cor-ldu-factorization .corollary name="A = LDU"}

Under the same assumptions $A=LDU'$, where $D$ is the diagonal matrix of pivots and $U'=D^{-1}U$ is upper triangular with $1$s on the diagonal. This factorization is unique.

:::

::: {.proof}

1. Dividing row $i$ of $U$ by its pivot $d_i\ne0$ gives $U'$, so $U=DU'$ and $A=LDU'$.

2. Uniqueness: if $L_1D_1U_1=L_2D_2U_2$, then $L_2^{-1}L_1D_1=D_2U_2U_1^{-1}$. The left side is lower triangular and the right side is upper triangular, so both are diagonal.

3. The diagonal of $L_2^{-1}L_1$ is all $1$s, so $L_2^{-1}L_1D_1=D_1$ forces $L_2^{-1}L_1=I$; similarly $U_2U_1^{-1}=I$; then $D_1=D_2$.

:::

::: {#thm-cost-of-elimination .theorem name="Cost of elimination"}

Elimination on an $n\times n$ matrix uses about $\frac13n^3$ multiplications (each followed by a subtraction). Each right side $\mathbf{b}$ then costs about $n^2$: $\frac12n^2$ for forward substitution with $L$ and $\frac12n^2$ for back substitution with $U$.

:::

::: {.proof}

1. Clearing column $k$ changes the lower-right $(n-k)\times(n-k+1)$ part, about $(n-k+1)^2$ operations.

2. Summing over $k$ gives $\sum_{j=1}^{n}j^2\approx\frac13n^3$.

3. Solving $L\mathbf{c}=\mathbf{b}$ uses row $i$ of $L$ with $i-1$ known values, $\sum_i(i-1)\approx\frac12n^2$ operations; back substitution with $U$ is the same.

:::

::: {#thm-pa-equals-lu .theorem name="PA = LU"}

If $A$ is invertible but elimination meets a zero in a pivot position, exchange rows. Doing all the needed exchanges first, there is a permutation matrix $P$ (@def-permutation-matrix) such that
$$PA=LU,$$
with $L$ and $U$ as in @thm-lu-factorization.

:::

::: {.proof}

1. Since $A$ is invertible, every column of the partly eliminated matrix has a nonzero entry on or below the diagonal; otherwise the first $k$ columns of the partly eliminated matrix would be dependent and $A\mathbf{x}=\mathbf{0}$ would have a nonzero solution, contradicting @thm-singular-if-nonzero-null-vector. So an exchange always finds a pivot.

2. Record the exchanges made during elimination and let $P$ be their product. Exchanging two rows below column $k$ before or after the steps of columns $<k$ only swaps the corresponding multipliers, which are entries of rows that both lie below the current pivot.

3. Hence running elimination on $PA$ from the start meets the same pivots without any exchange, and @thm-lu-factorization gives $PA=LU$.

:::

::: {#rmk-lu-factorization-1 .remark name="Why the order of rows matters"}

$A=\begin{bmatrix}0&1\\1&1\end{bmatrix}$ has no LU factorization: the first pivot would be $0$. Exchanging the rows gives $PA=\begin{bmatrix}1&1\\0&1\end{bmatrix}$, which is already $U$, with $L=I$.

:::
