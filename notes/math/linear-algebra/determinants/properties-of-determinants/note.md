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

::: {#fig-properties-of-determinants-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-0.2,0) -- (2.6,0); \draw[->, muted] (0,-0.2) -- (0,2.2);
\fill[tintA] (0.000,0.000) -- (1.200,0.200) -- (1.500,1.200) -- (0.300,1.000) -- cycle;
\draw[->, emph, primary] (0,0) -- (1.2, 0.2) node[below right, lab, tick] {$\mathbf r_1$};
\draw[->, emph, primary] (0,0) -- (0.3, 1.0) node[left, lab, tick] {$\mathbf r_2$};
\node[lab, note, align=center] at (1.1,-0.6) {$\det=1.14$};
\end{scope}
\begin{scope}[shift={(3.3,0)}]
\draw[->, muted] (-0.2,0) -- (2.6,0); \draw[->, muted] (0,-0.2) -- (0,2.2);
\fill[tintB] (0.000,0.000) -- (2.400,0.400) -- (2.700,1.400) -- (0.300,1.000) -- cycle;
\draw[->, emph, accent] (0,0) -- (2.4, 0.4) node[below right, lab, tick] {$\mathbf r_1$};
\draw[->, emph, accent] (0,0) -- (0.3, 1.0) node[left, lab, tick] {$\mathbf r_2$};
\node[lab, note, align=center] at (1.1,-0.6) {row $1$ doubled:\\$\det=2.28$};
\end{scope}
\begin{scope}[shift={(6.6,0)}]
\draw[->, muted] (-0.2,0) -- (2.6,0); \draw[->, muted] (0,-0.2) -- (0,2.2);
\fill[tintC] (0.000,0.000) -- (1.200,0.200) -- (2.700,1.400) -- (1.500,1.200) -- cycle;
\draw[->, emph, secondary] (0,0) -- (1.2, 0.2) node[below right, lab, tick] {$\mathbf r_1$};
\draw[->, emph, secondary] (0,0) -- (1.5, 1.2) node[left, lab, tick] {$\mathbf r_2$};
\node[lab, note, align=center] at (1.1,-0.6) {$\mathbf r_2+\mathbf r_1$:\\$\det=1.14$};
\end{scope}
\draw[faint, dashed] (6.6+0.3,1.0) -- (6.6+1.5,1.2);
\end{tikzpicture}
\end{center}
```

Rule 3 as area, for $\mathbf r_1=(1.2,0.2)$, $\mathbf r_2=(0.3,1)$. Scaling a row scales the area; adding a multiple of one row to another shears the parallelogram along that row and keeps the area. Exchanging the rows (rule 2) reverses the orientation, which is the sign.

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

::: {#fig-properties-of-determinants-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.0]
\draw[->] (-0.3,0) -- (5.7,0);
\draw[->] (0,-0.3) -- (0,2.4);
\fill[tintA] (0,0) -- (2,0) -- (3.2,1.8) -- (1.2,1.8) -- cycle;
\draw[emph, primary] (0,0) -- (2,0) -- (3.2,1.8) -- (1.2,1.8) -- cycle;
\draw[emph, accent, dashed] (2,0) -- (5.2,1.8) -- (3.2,1.8);
\draw[->, emph] (0,0) -- node[lab, below] {$\mathbf r_1$} (2,0);
\draw[->, emph] (0,0) -- node[lab, left] {$\mathbf r_2$} (1.2,1.8);
\draw[->, emph, accent] (0,0) -- (3.2,1.8) node[lab, above] {$\mathbf r_2+\mathbf r_1$};
\draw[faint, dashed] (5.5,0) -- (5.5,1.8); \node[lab, right] at (5.5,0.9) {same height};
\end{tikzpicture}
\end{center}
```

For a $2\times2$ matrix with rows $\mathbf r_1,\mathbf r_2$, $\lvert\det\rvert$ is the area of the parallelogram they span. Adding $\mathbf r_1$ to $\mathbf r_2$ slides the top side along itself (dashed): same base, same height, same area, matching the rule that this row operation leaves the determinant unchanged.

:::

::: {#cor-determinant-pivots .corollary name="Determinant from the pivots"}

If $PA=LU$, then $\det A=\pm(\text{product of the pivots})$, with the sign $+$ for an even number of row exchanges and $-$ for an odd number.

:::

::: {#fig-properties-of-determinants-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$1$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$3$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$5$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$4$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$5$};
\node[lab, note] at (0.825,-0.350) {$A$};
\draw[->] (1.9,0.825) -- (2.9,0.825) node[midway, above, lab, tick] {elimination};
\draw[hl cell] (3.100,1.100) rectangle (3.650,1.650);
\node[lab] at (3.375,1.375) {$1$};
\draw[cell frame] (3.650,1.100) rectangle (4.200,1.650);
\node[lab] at (3.925,1.375) {$1$};
\draw[cell frame] (4.200,1.100) rectangle (4.750,1.650);
\node[lab] at (4.475,1.375) {$1$};
\draw[cell frame] (3.100,0.550) rectangle (3.650,1.100);
\node[lab] at (3.375,0.825) {$0$};
\draw[hl cell] (3.650,0.550) rectangle (4.200,1.100);
\node[lab] at (3.925,0.825) {$1$};
\draw[cell frame] (4.200,0.550) rectangle (4.750,1.100);
\node[lab] at (4.475,0.825) {$3$};
\draw[cell frame] (3.100,-0.000) rectangle (3.650,0.550);
\node[lab] at (3.375,0.275) {$0$};
\draw[cell frame] (3.650,-0.000) rectangle (4.200,0.550);
\node[lab] at (3.925,0.275) {$0$};
\draw[hl cell] (4.200,-0.000) rectangle (4.750,0.550);
\node[lab] at (4.475,0.275) {$13$};
\node[lab, note] at (3.925,-0.350) {$U$};
\node[lab, anchor=west] at (5.1,0.825) {$\det A=\det U=1\cdot1\cdot13=13$};
\end{tikzpicture}
\end{center}
```

Subtracting multiples of rows does not change the determinant, and a triangular determinant is the product of its diagonal. For the matrix of @exm-elimination-three-by-three no row exchange is needed, so $\det A$ is the product of the pivots.

:::

<!-- Merged 2026-11-20 (owner): the block thm-product-rule-determinants was removed in favour of thm-determinant-multiplicative (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Product rule.** For $n\times n$ matrices, $\det(AB)=\det A\cdot\det B$. The idea: for fixed $B$ with $\det B\ne0$, $A\mapsto\det(AB)/\det B$ has the three defining properties, and only $\det$ has them. The proof over any field is @thm-determinant-multiplicative.

::: {#cor-determinant-inverse-transpose .corollary name="Inverse and transpose"}

$\det A^{-1}=1/\det A$ and $\det A^{\mathsf T}=\det A$. Consequently every property stated for rows holds for columns as well.

:::

::: {.proof}

1. $\det A\cdot\det A^{-1}=\det(AA^{-1})=\det I=1$ by @thm-determinant-multiplicative.

2. Write $PA=LU$. Then $A^{\mathsf T}P^{\mathsf T}=U^{\mathsf T}L^{\mathsf T}$, and by the product rule $\det A\det P=\det L\det U$ and $\det A^{\mathsf T}\det P^{\mathsf T}=\det U^{\mathsf T}\det L^{\mathsf T}$.

3. Triangular matrices have the same diagonal as their transposes, so (7) gives $\det L=\det L^{\mathsf T}=1$ and $\det U=\det U^{\mathsf T}$. And $P^{\mathsf T}P=I$ gives $\det P\det P^{\mathsf T}=1$ with both equal to $\pm1$, so $\det P=\det P^{\mathsf T}$. Hence $\det A^{\mathsf T}=\det A$.

:::

::: {#rmk-properties-of-determinants-1 .remark name="Determinants are not linear"}

$\det(A+B)\neq\det A+\det B$ in general, and $\det(2A)=2^n\det A$ for $n\times n$ $A$: linearity holds in one row at a time only.

:::

::: {#fig-properties-of-determinants-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, muted] (-0.2,0) -- (2.4,0); \draw[->, muted] (0,-0.2) -- (0,2.4);
\fill[tintB] (0,0) rectangle (2,2); \draw[accent] (0,0) rectangle (2,2);
\fill[tintA] (0,0) rectangle (1,1); \draw[primary, emph] (0,0) rectangle (1,1);
\draw[faint] (1,0) -- (1,2); \draw[faint] (0,1) -- (2,1);
\node[lab, note] at (0.5,0.5) {$I$}; \node[lab, note, accent] at (1.5,1.5) {$2I$};
\node[lab, note, anchor=west, align=left] at (2.6,1) {$\det(2I)=4\ne2\det I$:\\each of the $n$ rows is doubled,\\so $\det(tA)=t^n\det A$};
\end{tikzpicture}
\end{center}
```

Doubling a $2\times2$ matrix doubles both edges of its square, which multiplies the area by $4$, not $2$. The determinant is linear in each row separately, not in the whole matrix.

:::
