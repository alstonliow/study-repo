---
title: "Properties of Determinants"
sources: [mit1806-18]
requires: [math/linear-algebra/systems/lu-factorization]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 18, in our own wording; proofs written out in steps. The determinant is defined by three properties; the next note shows that a function with these properties exists and is unique. -->

The determinant is a number attached to every square matrix. It is defined by three properties; all others follow from them.

::: {#def-determinant-properties .definition name="Determinant (defining properties)"}

The *determinant* is the function $A\mapsto\det A=\lvert A\rvert$ on $n\times n$ matrices with

1. $\det I=1$;
2. exchanging two rows reverses the sign of the determinant;
3. it is linear in each row separately (the other rows held fixed):
$$\begin{vmatrix}t\,a&t\,b\\c&d\end{vmatrix}=t\begin{vmatrix}a&b\\c&d\end{vmatrix},\qquad
\begin{vmatrix}a+a'&b+b'\\c&d\end{vmatrix}=\begin{vmatrix}a&b\\c&d\end{vmatrix}+\begin{vmatrix}a'&b'\\c&d\end{vmatrix},$$
and the same in every other row.

:::

::: {#thm-determinant-consequences .theorem name="Consequences of the three properties"}

For every $n\times n$ matrix $A$:

4. If two rows are equal, $\det A=0$.
5. Subtracting $\ell$ times row $j$ from row $i$ leaves $\det A$ unchanged.
6. A zero row gives $\det A=0$.
7. If $A$ is triangular, $\det A=a_{11}a_{22}\cdots a_{nn}$.
8. $\det A=0$ exactly when $A$ is singular.

:::

::: {.proof}

1. **(4)** Exchanging the two equal rows does not change $A$ but reverses the sign by property 2, so $\det A=-\det A$ and $\det A=0$.

2. **(5)** By linearity in row $i$ (property 3), the new determinant is $\det A-\ell\cdot\det(A')$, where $A'$ has row $j$ in place of row $i$. $A'$ has two equal rows, so $\det A'=0$ by (4).

3. **(6)** Multiplying the zero row by $t=0$ does not change $A$, so by property 3 $\det A=0\cdot\det A=0$.

4. **(7)** If the diagonal entries are nonzero, subtract multiples of rows (upwards for upper triangular) to clear the off-diagonal entries without changing the determinant (5). Then factor $a_{ii}$ out of each row (property 3) and use $\det I=1$. If some $a_{ii}=0$, elimination produces a zero row and (6) gives $0$, which matches the product.

5. **(8)** Elimination with row exchanges turns $A$ into $U$, changing $\det$ only by the sign $\pm1$ (properties 2 and 5). By (7), $\det A=\pm u_{11}\cdots u_{nn}$, which is zero exactly when $U$ has fewer than $n$ pivots, i.e. when $A$ is singular.

:::

::: {#cor-determinant-pivots .corollary name="Determinant from the pivots"}

If $PA=LU$, then $\det A=\pm(\text{product of the pivots})$, with the sign $+$ for an even number of row exchanges and $-$ for an odd number.

:::

::: {#thm-product-rule-determinants .theorem name="Product rule"}

For $n\times n$ matrices, $\det(AB)=\det A\cdot\det B$.

:::

::: {.proof}

1. If $\det B=0$, $B$ is singular, so $B\mathbf{x}=\mathbf{0}$ for some $\mathbf{x}\ne\mathbf{0}$; then $AB\mathbf{x}=\mathbf{0}$ and $AB$ is singular, so both sides are $0$.

2. Otherwise consider $D(A)=\det(AB)/\det B$ as a function of $A$. Row $i$ of $AB$ is (row $i$ of $A$)$\,B$, so $D$ is linear in each row of $A$, changes sign when two rows of $A$ are exchanged, and $D(I)=1$.

3. The properties determine the function uniquely: by @thm-determinant-consequences any function with them equals $\pm$(product of pivots) after elimination. Hence $D(A)=\det A$.

:::

::: {#cor-determinant-inverse-transpose .corollary name="Inverse and transpose"}

$\det A^{-1}=1/\det A$ and $\det A^{\mathsf T}=\det A$. Consequently every property stated for rows holds for columns as well.

:::

::: {.proof}

1. $\det A\cdot\det A^{-1}=\det(AA^{-1})=\det I=1$ by @thm-product-rule-determinants.

2. Write $PA=LU$. Then $A^{\mathsf T}P^{\mathsf T}=U^{\mathsf T}L^{\mathsf T}$, and by the product rule $\det A\det P=\det L\det U$ and $\det A^{\mathsf T}\det P^{\mathsf T}=\det U^{\mathsf T}\det L^{\mathsf T}$.

3. Triangular matrices have the same diagonal as their transposes, so (7) gives $\det L=\det L^{\mathsf T}=1$ and $\det U=\det U^{\mathsf T}$. And $P^{\mathsf T}P=I$ gives $\det P\det P^{\mathsf T}=1$ with both equal to $\pm1$, so $\det P=\det P^{\mathsf T}$. Hence $\det A^{\mathsf T}=\det A$.

:::

::: {#rmk-properties-of-determinants-1 .remark name="Determinants are not linear"}

$\det(A+B)\neq\det A+\det B$ in general, and $\det(2A)=2^n\det A$ for $n\times n$ $A$: linearity holds in one row at a time only.

:::
