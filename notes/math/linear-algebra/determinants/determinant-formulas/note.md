---
title: "Determinant Formulas and Cofactors"
sources: [mit1806-19]
requires: [math/linear-algebra/determinants/properties-of-determinants]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 19, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#thm-big-formula-determinant .theorem name="The big formula"}

For an $n\times n$ matrix,
$$\det A=\sum_{\sigma}\operatorname{sign}(\sigma)\,a_{1\sigma(1)}a_{2\sigma(2)}\cdots a_{n\sigma(n)},$$
summed over all $n!$ permutations $\sigma$ of $\{1,\dots,n\}$, where $\operatorname{sign}(\sigma)=\det P_\sigma=\pm1$ for the permutation matrix $P_\sigma$ with $1$s in positions $(i,\sigma(i))$.

:::

::: {.proof}

1. Write row $i$ of $A$ as $\sum_ja_{ij}\mathbf{e}_j^{\mathsf T}$. Expanding by linearity in each row (property 3 of @def-determinant-properties) gives
   $$\det A=\sum_{j_1,\dots,j_n}a_{1j_1}\cdots a_{nj_n}\det\begin{bmatrix}\mathbf{e}_{j_1}^{\mathsf T}\\\vdots\\\mathbf{e}_{j_n}^{\mathsf T}\end{bmatrix}.$$

2. If two of the $j$'s are equal, the matrix has two equal rows and its determinant is $0$ (@thm-determinant-consequences).

3. The remaining terms have $j_i=\sigma(i)$ for a permutation $\sigma$, and the matrix is $P_\sigma$.

4. $\det P_\sigma=\pm1$: it is reached from $I$ by row exchanges, each flipping the sign.

:::

For $n=2$ this gives $ad-bc$. For $n=3$ there are six terms:
$$\begin{vmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{vmatrix}
=a_{11}a_{22}a_{33}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}.$$

The big formula also proves that the determinant exists: it is linear in each row, gives $1$ for $I$, and exchanging two rows changes the sign of every term. Together with uniqueness (step 3 in the proof of @thm-product-rule-determinants), the three properties define exactly one function.

::: {#def-cofactor .definition name="Minor and cofactor"}

The *minor* $M_{ij}$ is the $(n-1)\times(n-1)$ matrix obtained from $A$ by deleting row $i$ and column $j$. The *cofactor* is
$$C_{ij}=(-1)^{i+j}\det M_{ij}.$$

:::

::: {#fig-determinant-formulas-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.7]
\foreach \i in {1,3,4} \foreach \j in {1,2,4} \draw[cell frame, fill=primaryLight] (\j-1,-\i) rectangle (\j,-\i+1);
\foreach \j in {1,...,4} \draw[hl cell] (\j-1,-2) rectangle (\j,-1);
\foreach \i in {1,3,4} \draw[hl cell] (2,-\i) rectangle (3,-\i+1);
\node[lab] at (2.5,-1.5) {$a_{23}$};
\node[lab, left] at (-0.1,-1.5) {row $2$};
\node[lab, above] at (2.5,0.05) {column $3$};
\end{tikzpicture}
\end{center}
```

The minor $M_{23}$ of a $4\times4$ matrix: delete row $2$ and column $3$ (highlighted). The remaining $3\times3$ entries (shaded) form $M_{23}$, and $C_{23}=(-1)^{2+3}\det M_{23}$.

:::

::: {#thm-cofactor-expansion .theorem name="Cofactor expansion"}

For every row $i$,
$$\det A=a_{i1}C_{i1}+a_{i2}C_{i2}+\dots+a_{in}C_{in},$$
and similarly along every column.

:::

::: {.proof}

1. Group the terms of the big formula by the entry $a_{ij}$ chosen from row $i$. The terms containing $a_{ij}$ have the form $a_{ij}\times$(a product with one entry from each other row and each other column $\ne j$).

2. For $i=j=1$, these are exactly the terms of the big formula for $\det M_{11}$, with the same signs (a permutation fixing $1$ has the same sign as its restriction). So their sum is $a_{11}\det M_{11}=a_{11}C_{11}$.

3. For general $(i,j)$, move row $i$ to the top by $i-1$ exchanges of neighbouring rows and column $j$ to the left by $j-1$ exchanges of neighbouring columns. The order of the other rows and columns is kept, so the new $(1,1)$ minor is $M_{ij}$, and the sign changes by $(-1)^{i+j-2}=(-1)^{i+j}$ (columns behave like rows by @cor-determinant-inverse-transpose).

4. Summing over $j$ gives the expansion along row $i$; transposing gives the one along a column.

:::

::: {#exm-tridiagonal-determinants .example name="A tridiagonal family"}

Let $A_n$ be the $n\times n$ matrix with $2$ on the diagonal and $-1$ just above and below it. Expanding along the first row: the $(1,1)$ cofactor is $\det A_{n-1}$; the $(1,2)$ minor has first column $(-1,0,\dots,0)$, and expanding it down that column gives $-\det A_{n-2}$. So
$$\det A_n=2\det A_{n-1}-\det A_{n-2}.$$
With $\det A_1=2$ and $\det A_2=3$, induction gives $\det A_n=n+1$.

:::
