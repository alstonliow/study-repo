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

::: {#fig-determinant-formulas-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.800) rectangle (0.400,1.200);
\draw[cell frame] (0.400,0.800) rectangle (0.800,1.200);
\draw[cell frame] (0.800,0.800) rectangle (1.200,1.200);
\draw[cell frame] (0.000,0.400) rectangle (0.400,0.800);
\draw[hl cell] (0.400,0.400) rectangle (0.800,0.800);
\draw[cell frame] (0.800,0.400) rectangle (1.200,0.800);
\draw[cell frame] (0.000,-0.000) rectangle (0.400,0.400);
\draw[cell frame] (0.400,-0.000) rectangle (0.800,0.400);
\draw[hl cell] (0.800,-0.000) rectangle (1.200,0.400);
\node[lab, tick] at (0.6,-0.25) {$+\,a_{11}a_{22}a_{33}$};
\draw[cell frame] (1.900,0.800) rectangle (2.300,1.200);
\draw[hl cell] (2.300,0.800) rectangle (2.700,1.200);
\draw[cell frame] (2.700,0.800) rectangle (3.100,1.200);
\draw[cell frame] (1.900,0.400) rectangle (2.300,0.800);
\draw[cell frame] (2.300,0.400) rectangle (2.700,0.800);
\draw[hl cell] (2.700,0.400) rectangle (3.100,0.800);
\draw[hl cell] (1.900,-0.000) rectangle (2.300,0.400);
\draw[cell frame] (2.300,-0.000) rectangle (2.700,0.400);
\draw[cell frame] (2.700,-0.000) rectangle (3.100,0.400);
\node[lab, tick] at (2.5,-0.25) {$+\,a_{12}a_{23}a_{31}$};
\draw[cell frame] (3.800,0.800) rectangle (4.200,1.200);
\draw[cell frame] (4.200,0.800) rectangle (4.600,1.200);
\draw[hl cell] (4.600,0.800) rectangle (5.000,1.200);
\draw[hl cell] (3.800,0.400) rectangle (4.200,0.800);
\draw[cell frame] (4.200,0.400) rectangle (4.600,0.800);
\draw[cell frame] (4.600,0.400) rectangle (5.000,0.800);
\draw[cell frame] (3.800,-0.000) rectangle (4.200,0.400);
\draw[hl cell] (4.200,-0.000) rectangle (4.600,0.400);
\draw[cell frame] (4.600,-0.000) rectangle (5.000,0.400);
\node[lab, tick] at (4.40,-0.25) {$+\,a_{13}a_{21}a_{32}$};
\draw[cell frame] (5.700,0.800) rectangle (6.100,1.200);
\draw[cell, fill=primaryLight] (6.100,0.800) rectangle (6.500,1.200);
\draw[cell frame] (6.500,0.800) rectangle (6.900,1.200);
\draw[cell, fill=primaryLight] (5.700,0.400) rectangle (6.100,0.800);
\draw[cell frame] (6.100,0.400) rectangle (6.500,0.800);
\draw[cell frame] (6.500,0.400) rectangle (6.900,0.800);
\draw[cell frame] (5.700,-0.000) rectangle (6.100,0.400);
\draw[cell frame] (6.100,-0.000) rectangle (6.500,0.400);
\draw[cell, fill=primaryLight] (6.500,-0.000) rectangle (6.900,0.400);
\node[lab, tick] at (6.30,-0.25) {$-\,a_{12}a_{21}a_{33}$};
\draw[cell frame] (7.600,0.800) rectangle (8.000,1.200);
\draw[cell frame] (8.000,0.800) rectangle (8.400,1.200);
\draw[cell, fill=primaryLight] (8.400,0.800) rectangle (8.800,1.200);
\draw[cell frame] (7.600,0.400) rectangle (8.000,0.800);
\draw[cell, fill=primaryLight] (8.000,0.400) rectangle (8.400,0.800);
\draw[cell frame] (8.400,0.400) rectangle (8.800,0.800);
\draw[cell, fill=primaryLight] (7.600,-0.000) rectangle (8.000,0.400);
\draw[cell frame] (8.000,-0.000) rectangle (8.400,0.400);
\draw[cell frame] (8.400,-0.000) rectangle (8.800,0.400);
\node[lab, tick] at (8.2,-0.25) {$-\,a_{13}a_{22}a_{31}$};
\draw[cell, fill=primaryLight] (9.500,0.800) rectangle (9.900,1.200);
\draw[cell frame] (9.900,0.800) rectangle (10.300,1.200);
\draw[cell frame] (10.300,0.800) rectangle (10.700,1.200);
\draw[cell frame] (9.500,0.400) rectangle (9.900,0.800);
\draw[cell frame] (9.900,0.400) rectangle (10.300,0.800);
\draw[cell, fill=primaryLight] (10.300,0.400) rectangle (10.700,0.800);
\draw[cell frame] (9.500,-0.000) rectangle (9.900,0.400);
\draw[cell, fill=primaryLight] (9.900,-0.000) rectangle (10.300,0.400);
\draw[cell frame] (10.300,-0.000) rectangle (10.700,0.400);
\node[lab, tick] at (10.1,-0.25) {$-\,a_{11}a_{23}a_{32}$};
\end{tikzpicture}
\end{center}
```

The six terms of the big formula for $n=3$: each picks one entry from every row and every column, a permutation pattern. The three even patterns (red) come with $+$, the three odd ones (blue, one row exchange away from $I$) with $-$.

:::

For $n=2$ this gives $ad-bc$. For $n=3$ there are six terms:
$$\begin{vmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{vmatrix}
=a_{11}a_{22}a_{33}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}.$$

The big formula also proves that the determinant exists: it is linear in each row, gives $1$ for $I$, and exchanging two rows changes the sign of every term. Together with uniqueness (by @thm-determinant-consequences, elimination turns any function with the three properties into $\pm$ the product of the pivots), the three properties define exactly one function.

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

::: {#fig-determinant-formulas-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.600,1.100) rectangle (1.150,1.650);
\node[lab] at (0.875,1.375) {$a_{11}$};
\draw[cell frame] (1.150,1.100) rectangle (1.700,1.650);
\node[lab] at (1.425,1.375) {$a_{12}$};
\draw[cell frame] (1.700,1.100) rectangle (2.250,1.650);
\node[lab] at (1.975,1.375) {$a_{13}$};
\draw[cell frame] (0.600,0.550) rectangle (1.150,1.100);
\draw[cell, fill=primaryLight] (1.150,0.550) rectangle (1.700,1.100);
\draw[cell, fill=primaryLight] (1.700,0.550) rectangle (2.250,1.100);
\draw[cell frame] (0.600,-0.000) rectangle (1.150,0.550);
\draw[cell, fill=primaryLight] (1.150,-0.000) rectangle (1.700,0.550);
\draw[cell, fill=primaryLight] (1.700,-0.000) rectangle (2.250,0.550);
\node[lab] at (0.3,0.825) {$+$};
\node[lab, tick] at (1.42,-0.3) {$a_{11}C_{11}$};
\draw[cell frame] (3.600,1.100) rectangle (4.150,1.650);
\node[lab] at (3.875,1.375) {$a_{11}$};
\draw[hl cell] (4.150,1.100) rectangle (4.700,1.650);
\node[lab] at (4.425,1.375) {$a_{12}$};
\draw[cell frame] (4.700,1.100) rectangle (5.250,1.650);
\node[lab] at (4.975,1.375) {$a_{13}$};
\draw[cell, fill=primaryLight] (3.600,0.550) rectangle (4.150,1.100);
\draw[cell frame] (4.150,0.550) rectangle (4.700,1.100);
\draw[cell, fill=primaryLight] (4.700,0.550) rectangle (5.250,1.100);
\draw[cell, fill=primaryLight] (3.600,-0.000) rectangle (4.150,0.550);
\draw[cell frame] (4.150,-0.000) rectangle (4.700,0.550);
\draw[cell, fill=primaryLight] (4.700,-0.000) rectangle (5.250,0.550);
\node[lab] at (3.3,0.825) {$-$};
\node[lab, tick] at (4.42,-0.3) {$a_{12}C_{12}$};
\draw[cell frame] (6.600,1.100) rectangle (7.150,1.650);
\node[lab] at (6.875,1.375) {$a_{11}$};
\draw[cell frame] (7.150,1.100) rectangle (7.700,1.650);
\node[lab] at (7.425,1.375) {$a_{12}$};
\draw[hl cell] (7.700,1.100) rectangle (8.250,1.650);
\node[lab] at (7.975,1.375) {$a_{13}$};
\draw[cell, fill=primaryLight] (6.600,0.550) rectangle (7.150,1.100);
\draw[cell, fill=primaryLight] (7.150,0.550) rectangle (7.700,1.100);
\draw[cell frame] (7.700,0.550) rectangle (8.250,1.100);
\draw[cell, fill=primaryLight] (6.600,-0.000) rectangle (7.150,0.550);
\draw[cell, fill=primaryLight] (7.150,-0.000) rectangle (7.700,0.550);
\draw[cell frame] (7.700,-0.000) rectangle (8.250,0.550);
\node[lab] at (6.3,0.825) {$+$};
\node[lab, tick] at (7.42,-0.3) {$a_{13}C_{13}$};
\end{tikzpicture}
\end{center}
```

Cofactor expansion along row $1$ for $n=3$. Each entry $a_{1j}$ (highlighted) multiplies the determinant of the $2\times2$ matrix left after deleting its row and column (shaded), with the sign $(-1)^{1+j}$.

:::

::: {#exm-tridiagonal-determinants .example name="A tridiagonal family"}

Let $A_n$ be the $n\times n$ matrix with $2$ on the diagonal and $-1$ just above and below it. Expanding along the first row: the $(1,1)$ cofactor is $\det A_{n-1}$; the $(1,2)$ minor has first column $(-1,0,\dots,0)$, and expanding it down that column gives $-\det A_{n-2}$. So
$$\det A_n=2\det A_{n-1}-\det A_{n-2}.$$
With $\det A_1=2$ and $\det A_2=3$, induction gives $\det A_n=n+1$.

:::

::: {#fig-determinant-formulas-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,2.200) rectangle (0.550,2.750);
\node[lab] at (0.275,2.475) {$2$};
\draw[cell, fill=primaryLight] (0.550,2.200) rectangle (1.100,2.750);
\node[lab] at (0.825,2.475) {$-1$};
\draw[cell frame] (1.100,2.200) rectangle (1.650,2.750);
\draw[cell frame] (1.650,2.200) rectangle (2.200,2.750);
\draw[cell frame] (2.200,2.200) rectangle (2.750,2.750);
\draw[cell, fill=primaryLight] (0.000,1.650) rectangle (0.550,2.200);
\node[lab] at (0.275,1.925) {$-1$};
\draw[hl cell] (0.550,1.650) rectangle (1.100,2.200);
\node[lab] at (0.825,1.925) {$2$};
\draw[cell, fill=primaryLight] (1.100,1.650) rectangle (1.650,2.200);
\node[lab] at (1.375,1.925) {$-1$};
\draw[cell frame] (1.650,1.650) rectangle (2.200,2.200);
\draw[cell frame] (2.200,1.650) rectangle (2.750,2.200);
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\draw[cell, fill=primaryLight] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$-1$};
\draw[hl cell] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$2$};
\draw[cell, fill=primaryLight] (1.650,1.100) rectangle (2.200,1.650);
\node[lab] at (1.925,1.375) {$-1$};
\draw[cell frame] (2.200,1.100) rectangle (2.750,1.650);
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\draw[cell, fill=primaryLight] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$-1$};
\draw[hl cell] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$2$};
\draw[cell, fill=primaryLight] (2.200,0.550) rectangle (2.750,1.100);
\node[lab] at (2.475,0.825) {$-1$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\draw[cell, fill=primaryLight] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$-1$};
\draw[hl cell] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$2$};
\node[lab, note] at (1.375,-0.350) {$A_5$};
\begin{scope}[shift={(3.6,0)}]
\draw[->, muted] (0,0) -- (3.4,0) node[right, lab, tick] {$n$}; \draw[->, muted] (0,0) -- (0,2.9) node[above, lab, tick] {$\det A_n$};
\fill[accent] (0.6,0.8) circle[pt]; \node[lab, tick] at (0.6,-0.2) {1}; \node[lab, tick, above left] at (0.6,0.8) {2};
\fill[accent] (1.2,1.20) circle[pt]; \node[lab, tick] at (1.2,-0.2) {2}; \node[lab, tick, above left] at (1.2,1.20) {3};
\fill[accent] (1.80,1.6) circle[pt]; \node[lab, tick] at (1.80,-0.2) {3}; \node[lab, tick, above left] at (1.80,1.6) {4};
\fill[accent] (2.4,2.0) circle[pt]; \node[lab, tick] at (2.4,-0.2) {4}; \node[lab, tick, above left] at (2.4,2.0) {5};
\fill[accent] (3.0,2.40) circle[pt]; \node[lab, tick] at (3.0,-0.2) {5}; \node[lab, tick, above left] at (3.0,2.40) {6};
\draw[faint, dashed] (0,0.4) -- (3.2,2.53);
\end{scope}
\end{tikzpicture}
\end{center}
```

@exm-tridiagonal-determinants: the matrices $A_n$ have $2$ on the diagonal and $-1$ beside it. The recursion $\det A_n=2\det A_{n-1}-\det A_{n-2}$ makes the determinants grow by $1$ each time: $\det A_n=n+1$.

:::
