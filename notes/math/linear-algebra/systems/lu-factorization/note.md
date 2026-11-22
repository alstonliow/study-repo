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

::: {#fig-lu-factorization-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.00,0.00) rectangle (0.30,-0.30);
\draw[cell frame] (0.30,0.00) rectangle (0.60,-0.30);
\draw[cell frame] (0.60,0.00) rectangle (0.90,-0.30);
\draw[cell frame] (0.90,0.00) rectangle (1.20,-0.30);
\draw[cell frame] (1.20,0.00) rectangle (1.50,-0.30);
\draw[cell, fill=primaryMid] (0.00,-0.30) rectangle (0.30,-0.60);
\draw[cell, fill=primaryMid] (0.30,-0.30) rectangle (0.60,-0.60);
\draw[cell, fill=primaryMid] (0.60,-0.30) rectangle (0.90,-0.60);
\draw[cell, fill=primaryMid] (0.90,-0.30) rectangle (1.20,-0.60);
\draw[cell, fill=primaryMid] (1.20,-0.30) rectangle (1.50,-0.60);
\draw[cell, fill=primaryMid] (0.00,-0.60) rectangle (0.30,-0.90);
\draw[cell, fill=primaryMid] (0.30,-0.60) rectangle (0.60,-0.90);
\draw[cell, fill=primaryMid] (0.60,-0.60) rectangle (0.90,-0.90);
\draw[cell, fill=primaryMid] (0.90,-0.60) rectangle (1.20,-0.90);
\draw[cell, fill=primaryMid] (1.20,-0.60) rectangle (1.50,-0.90);
\draw[cell, fill=primaryMid] (0.00,-0.90) rectangle (0.30,-1.20);
\draw[cell, fill=primaryMid] (0.30,-0.90) rectangle (0.60,-1.20);
\draw[cell, fill=primaryMid] (0.60,-0.90) rectangle (0.90,-1.20);
\draw[cell, fill=primaryMid] (0.90,-0.90) rectangle (1.20,-1.20);
\draw[cell, fill=primaryMid] (1.20,-0.90) rectangle (1.50,-1.20);
\draw[cell, fill=primaryMid] (0.00,-1.20) rectangle (0.30,-1.50);
\draw[cell, fill=primaryMid] (0.30,-1.20) rectangle (0.60,-1.50);
\draw[cell, fill=primaryMid] (0.60,-1.20) rectangle (0.90,-1.50);
\draw[cell, fill=primaryMid] (0.90,-1.20) rectangle (1.20,-1.50);
\draw[cell, fill=primaryMid] (1.20,-1.20) rectangle (1.50,-1.50);
\node[lab, tick] at (0.75,-1.85) {step 1: $4\times5$};
\draw[cell frame] (2.00,0.00) rectangle (2.30,-0.30);
\draw[cell frame] (2.30,0.00) rectangle (2.60,-0.30);
\draw[cell frame] (2.60,0.00) rectangle (2.90,-0.30);
\draw[cell frame] (2.90,0.00) rectangle (3.20,-0.30);
\draw[cell frame] (3.20,0.00) rectangle (3.50,-0.30);
\draw[cell frame] (2.00,-0.30) rectangle (2.30,-0.60);
\draw[hl cell] (2.30,-0.30) rectangle (2.60,-0.60);
\draw[cell frame] (2.60,-0.30) rectangle (2.90,-0.60);
\draw[cell frame] (2.90,-0.30) rectangle (3.20,-0.60);
\draw[cell frame] (3.20,-0.30) rectangle (3.50,-0.60);
\draw[cell frame] (2.00,-0.60) rectangle (2.30,-0.90);
\draw[cell, fill=primaryMid] (2.30,-0.60) rectangle (2.60,-0.90);
\draw[cell, fill=primaryMid] (2.60,-0.60) rectangle (2.90,-0.90);
\draw[cell, fill=primaryMid] (2.90,-0.60) rectangle (3.20,-0.90);
\draw[cell, fill=primaryMid] (3.20,-0.60) rectangle (3.50,-0.90);
\draw[cell frame] (2.00,-0.90) rectangle (2.30,-1.20);
\draw[cell, fill=primaryMid] (2.30,-0.90) rectangle (2.60,-1.20);
\draw[cell, fill=primaryMid] (2.60,-0.90) rectangle (2.90,-1.20);
\draw[cell, fill=primaryMid] (2.90,-0.90) rectangle (3.20,-1.20);
\draw[cell, fill=primaryMid] (3.20,-0.90) rectangle (3.50,-1.20);
\draw[cell frame] (2.00,-1.20) rectangle (2.30,-1.50);
\draw[cell, fill=primaryMid] (2.30,-1.20) rectangle (2.60,-1.50);
\draw[cell, fill=primaryMid] (2.60,-1.20) rectangle (2.90,-1.50);
\draw[cell, fill=primaryMid] (2.90,-1.20) rectangle (3.20,-1.50);
\draw[cell, fill=primaryMid] (3.20,-1.20) rectangle (3.50,-1.50);
\node[lab, tick] at (2.75,-1.85) {step 2: $3\times4$};
\draw[cell frame] (4.00,0.00) rectangle (4.30,-0.30);
\draw[cell frame] (4.30,0.00) rectangle (4.60,-0.30);
\draw[cell frame] (4.60,0.00) rectangle (4.90,-0.30);
\draw[cell frame] (4.90,0.00) rectangle (5.20,-0.30);
\draw[cell frame] (5.20,0.00) rectangle (5.50,-0.30);
\draw[cell frame] (4.00,-0.30) rectangle (4.30,-0.60);
\draw[cell frame] (4.30,-0.30) rectangle (4.60,-0.60);
\draw[cell frame] (4.60,-0.30) rectangle (4.90,-0.60);
\draw[cell frame] (4.90,-0.30) rectangle (5.20,-0.60);
\draw[cell frame] (5.20,-0.30) rectangle (5.50,-0.60);
\draw[cell frame] (4.00,-0.60) rectangle (4.30,-0.90);
\draw[cell frame] (4.30,-0.60) rectangle (4.60,-0.90);
\draw[hl cell] (4.60,-0.60) rectangle (4.90,-0.90);
\draw[cell frame] (4.90,-0.60) rectangle (5.20,-0.90);
\draw[cell frame] (5.20,-0.60) rectangle (5.50,-0.90);
\draw[cell frame] (4.00,-0.90) rectangle (4.30,-1.20);
\draw[cell frame] (4.30,-0.90) rectangle (4.60,-1.20);
\draw[cell, fill=primaryMid] (4.60,-0.90) rectangle (4.90,-1.20);
\draw[cell, fill=primaryMid] (4.90,-0.90) rectangle (5.20,-1.20);
\draw[cell, fill=primaryMid] (5.20,-0.90) rectangle (5.50,-1.20);
\draw[cell frame] (4.00,-1.20) rectangle (4.30,-1.50);
\draw[cell frame] (4.30,-1.20) rectangle (4.60,-1.50);
\draw[cell, fill=primaryMid] (4.60,-1.20) rectangle (4.90,-1.50);
\draw[cell, fill=primaryMid] (4.90,-1.20) rectangle (5.20,-1.50);
\draw[cell, fill=primaryMid] (5.20,-1.20) rectangle (5.50,-1.50);
\node[lab, tick] at (4.75,-1.85) {step 3: $2\times3$};
\draw[cell frame] (6.00,0.00) rectangle (6.30,-0.30);
\draw[cell frame] (6.30,0.00) rectangle (6.60,-0.30);
\draw[cell frame] (6.60,0.00) rectangle (6.90,-0.30);
\draw[cell frame] (6.90,0.00) rectangle (7.20,-0.30);
\draw[cell frame] (7.20,0.00) rectangle (7.50,-0.30);
\draw[cell frame] (6.00,-0.30) rectangle (6.30,-0.60);
\draw[cell frame] (6.30,-0.30) rectangle (6.60,-0.60);
\draw[cell frame] (6.60,-0.30) rectangle (6.90,-0.60);
\draw[cell frame] (6.90,-0.30) rectangle (7.20,-0.60);
\draw[cell frame] (7.20,-0.30) rectangle (7.50,-0.60);
\draw[cell frame] (6.00,-0.60) rectangle (6.30,-0.90);
\draw[cell frame] (6.30,-0.60) rectangle (6.60,-0.90);
\draw[cell frame] (6.60,-0.60) rectangle (6.90,-0.90);
\draw[cell frame] (6.90,-0.60) rectangle (7.20,-0.90);
\draw[cell frame] (7.20,-0.60) rectangle (7.50,-0.90);
\draw[cell frame] (6.00,-0.90) rectangle (6.30,-1.20);
\draw[cell frame] (6.30,-0.90) rectangle (6.60,-1.20);
\draw[cell frame] (6.60,-0.90) rectangle (6.90,-1.20);
\draw[hl cell] (6.90,-0.90) rectangle (7.20,-1.20);
\draw[cell frame] (7.20,-0.90) rectangle (7.50,-1.20);
\draw[cell frame] (6.00,-1.20) rectangle (6.30,-1.50);
\draw[cell frame] (6.30,-1.20) rectangle (6.60,-1.50);
\draw[cell frame] (6.60,-1.20) rectangle (6.90,-1.50);
\draw[cell, fill=primaryMid] (6.90,-1.20) rectangle (7.20,-1.50);
\draw[cell, fill=primaryMid] (7.20,-1.20) rectangle (7.50,-1.50);
\node[lab, tick] at (6.75,-1.85) {step 4: $1\times2$};
\end{tikzpicture}
\end{center}
```

Where the work is, for $n=5$. At step $k$ the pivot (highlighted) is used to update the shaded block below it, about $(n-k)^2$ entries. Adding $(n-1)^2+(n-2)^2+\dots+1^2\approx\frac13n^3$ gives the cost in @thm-cost-of-elimination.

:::

::: {#fig-lu-factorization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (1.6,1.6); \node[lab] at (0.8,0.8) {$A$};
\node[lab] at (2.05,0.8) {$=$};
\fill[primaryLight] (2.5,1.6) -- (2.5,0) -- (4.1,0) -- cycle;
\draw[rule] (2.5,0) rectangle (4.1,1.6); \draw[primary] (2.5,1.6) -- (4.1,0);
\node[lab] at (3.0,0.5) {$\ell_{ij}$}; \node[tick] at (3.6,1.25) {$0$};
\fill[accentLight] (4.5,1.6) -- (6.1,1.6) -- (6.1,0) -- cycle;
\draw[rule] (4.5,0) rectangle (6.1,1.6); \draw[accent] (4.5,1.6) -- (6.1,0);
\node[lab] at (5.6,1.1) {$u_{ij}$}; \node[tick] at (5.0,0.35) {$0$};
\node[lab, below] at (3.3,-0.05) {$L$}; \node[lab, below] at (5.3,-0.05) {$U$};
\end{tikzpicture}
\end{center}
```

The shapes in $A=LU$: $L$ is lower triangular with $1$s on its diagonal and the multipliers $\ell_{ij}$ below it, and $U$ is upper triangular with the pivots on its diagonal.

:::

The opposite product $E=E_{n,n-1}\cdots E_{21}$ mixes the multipliers; in @exm-elimination-three-by-three, $E$ has entry $(3,1)$ equal to $-12$, not $-4$. That is why $L$, not $E$, is the matrix to keep.

::: {#exm-lu-three-by-three .example name="LU of the 3 by 3 example"}

From @exm-elimination-three-by-three, with multipliers $\ell_{21}=2$, $\ell_{31}=4$, $\ell_{32}=-4$:
$$\begin{bmatrix}1&1&1\\2&3&5\\4&0&5\end{bmatrix}=\begin{bmatrix}1&0&0\\2&1&0\\4&-4&1\end{bmatrix}\begin{bmatrix}1&1&1\\0&1&3\\0&0&13\end{bmatrix}.$$

:::

::: {#fig-lu-factorization-2}

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
\node[lab] at (1.95,0.825) {$=$};
\draw[cell frame] (2.250,1.100) rectangle (2.800,1.650);
\node[lab] at (2.525,1.375) {$1$};
\draw[cell frame] (2.800,1.100) rectangle (3.350,1.650);
\node[lab] at (3.075,1.375) {$0$};
\draw[cell frame] (3.350,1.100) rectangle (3.900,1.650);
\node[lab] at (3.625,1.375) {$0$};
\draw[hl cell] (2.250,0.550) rectangle (2.800,1.100);
\node[lab] at (2.525,0.825) {$2$};
\draw[cell frame] (2.800,0.550) rectangle (3.350,1.100);
\node[lab] at (3.075,0.825) {$1$};
\draw[cell frame] (3.350,0.550) rectangle (3.900,1.100);
\node[lab] at (3.625,0.825) {$0$};
\draw[hl cell] (2.250,-0.000) rectangle (2.800,0.550);
\node[lab] at (2.525,0.275) {$4$};
\draw[hl cell] (2.800,-0.000) rectangle (3.350,0.550);
\node[lab] at (3.075,0.275) {$-4$};
\draw[cell frame] (3.350,-0.000) rectangle (3.900,0.550);
\node[lab] at (3.625,0.275) {$1$};
\node[lab, note] at (3.075,-0.350) {$L$: multipliers};
\draw[hl cell] (4.300,1.100) rectangle (4.850,1.650);
\node[lab] at (4.575,1.375) {$1$};
\draw[cell frame] (4.850,1.100) rectangle (5.400,1.650);
\node[lab] at (5.125,1.375) {$1$};
\draw[cell frame] (5.400,1.100) rectangle (5.950,1.650);
\node[lab] at (5.675,1.375) {$1$};
\draw[cell frame] (4.300,0.550) rectangle (4.850,1.100);
\node[lab] at (4.575,0.825) {$0$};
\draw[hl cell] (4.850,0.550) rectangle (5.400,1.100);
\node[lab] at (5.125,0.825) {$1$};
\draw[cell frame] (5.400,0.550) rectangle (5.950,1.100);
\node[lab] at (5.675,0.825) {$3$};
\draw[cell frame] (4.300,-0.000) rectangle (4.850,0.550);
\node[lab] at (4.575,0.275) {$0$};
\draw[cell frame] (4.850,-0.000) rectangle (5.400,0.550);
\node[lab] at (5.125,0.275) {$0$};
\draw[hl cell] (5.400,-0.000) rectangle (5.950,0.550);
\node[lab] at (5.675,0.275) {$13$};
\node[lab, note] at (5.125,-0.350) {$U$: pivots};
\end{tikzpicture}
\end{center}
```

@exm-lu-three-by-three in cells. Below the diagonal, $L$ records the multipliers $\ell_{21}=2$, $\ell_{31}=4$, $\ell_{32}=-4$ in the positions they were used; the diagonal of $U$ holds the pivots $1,1,13$.

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

::: {#fig-lu-factorization-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (b) at (0,0) {$\mathbf b=\begin{bmatrix}6\\23\\19\end{bmatrix}$};
\node[box] (c) at (4.8,0) {$\mathbf c=\begin{bmatrix}6\\11\\39\end{bmatrix}$};
\node[hl box] (x) at (9.6,0) {$\mathbf x=\begin{bmatrix}1\\2\\3\end{bmatrix}$};
\draw[->, emph] (b) -- node[above, lab, note, align=center] {solve $L\mathbf c=\mathbf b$\\(forward, top down)} (c);
\draw[->, emph] (c) -- node[above, lab, note, align=center] {solve $U\mathbf x=\mathbf c$\\(back, bottom up)} (x);
\node[lab, tick] at (2.4,-0.85) {about $\tfrac12n^2$ steps}; \node[lab, tick] at (7.2,-0.85) {about $\tfrac12n^2$ steps};
\end{tikzpicture}
\end{center}
```

Once $A=LU$ is known, each new right side costs two triangular solves. With the factors of @exm-lu-three-by-three: forward substitution turns $\mathbf b$ into $\mathbf c$ (the right side elimination would produce), and back substitution gives $\mathbf x$.

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

::: {#fig-lu-factorization-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$0$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$1$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$1$};
\node[lab, note] at (0.550,-0.350) {$A$: pivot $0$};
\draw[->] (1.4,0.55) -- (3.2,0.55) node[midway, above, lab, note] {exchange rows};
\draw[<->, accent, emph] (-0.2,0.825) to[bend right=60] (-0.2,0.275);
\draw[hl cell] (3.400,0.550) rectangle (3.950,1.100);
\node[lab] at (3.675,0.825) {$1$};
\draw[cell frame] (3.950,0.550) rectangle (4.500,1.100);
\node[lab] at (4.225,0.825) {$1$};
\draw[cell frame] (3.400,0.000) rectangle (3.950,0.550);
\node[lab] at (3.675,0.275) {$0$};
\draw[hl cell] (3.950,0.000) rectangle (4.500,0.550);
\node[lab] at (4.225,0.275) {$1$};
\node[lab, note] at (3.950,-0.350) {$PA=U$, $L=I$};
\end{tikzpicture}
\end{center}
```

The matrix $\begin{bmatrix}0&1\\1&1\end{bmatrix}$ from the remark above. With a zero in the first pivot position no multiple of row $1$ can clear the $1$ below it; after the exchange the matrix is already upper triangular.

:::
