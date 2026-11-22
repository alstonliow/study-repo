---
title: "Matrix Multiplication"
sources: [mit1806-3]
requires: [math/linear-algebra/systems/elimination]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 3, in our own wording; proofs written out in steps. -->

::: {#def-matrix-product .definition name="Matrix product"}

If $A$ is $m\times n$ and $B$ is $n\times p$, the product $AB$ is the $m\times p$ matrix with entries
$$(AB)_{ij}=\sum_{k=1}^n a_{ik}b_{kj}=(\text{row }i\text{ of }A)\cdot(\text{column }j\text{ of }B).$$
The number of columns of $A$ must equal the number of rows of $B$.

:::

::: {#fig-matrix-multiplication-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (1.6,-1.0); \node[lab] at (0.8,-0.5) {$A$};
\draw[decorate, decoration={brace, amplitude=3pt, mirror}] (-0.1,0) -- (-0.1,-1.0) node[midway, left=3pt, lab, tick] {$m$};
\draw[decorate, decoration={brace, amplitude=3pt}] (0,0.1) -- (1.6,0.1) node[midway, above=3pt, lab, tick, accent] {$n$};
\node[lab] at (1.85,-0.5) {$\times$};
\draw[cell frame] (2.1,0) rectangle (3.0,-1.6); \node[lab] at (2.55,-0.8) {$B$};
\draw[decorate, decoration={brace, amplitude=3pt}] (3.1,0) -- (3.1,-1.6) node[midway, right=3pt, lab, tick, accent] {$n$};
\draw[decorate, decoration={brace, amplitude=3pt}] (2.1,0.1) -- (3.0,0.1) node[midway, above=3pt, lab, tick] {$p$};
\node[lab] at (3.7,-0.5) {$=$};
\draw[hl cell] (4.0,0) rectangle (4.9,-1.0); \node[lab] at (4.45,-0.5) {$AB$};
\draw[decorate, decoration={brace, amplitude=3pt}] (5.0,0) -- (5.0,-1.0) node[midway, right=3pt, lab, tick] {$m$};
\draw[decorate, decoration={brace, amplitude=3pt}] (4.0,0.1) -- (4.9,0.1) node[midway, above=3pt, lab, tick] {$p$};
\end{tikzpicture}
\end{center}
```

Shapes in a product: an $m\times n$ matrix times an $n\times p$ matrix is $m\times p$. The inner sizes (both $n$) must agree, because each entry of $AB$ is a dot product of a row of $A$ with a column of $B$.

:::

::: {#fig-matrix-multiplication-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.5]
\foreach \i in {1,2,3} \foreach \j in {1,...,4} \draw[cell frame] (\j-1,-\i) rectangle (\j,-\i+1);
\foreach \j in {1,...,4} \draw[hl cell] (\j-1,-2) rectangle (\j,-1);
\foreach \i in {1,...,4} \foreach \j in {1,2,3} \draw[cell frame] (4.5+\j,1.5-\i) rectangle (5.5+\j,2.5-\i);
\foreach \i in {1,...,4} \draw[hl cell] (7.5,1.5-\i) rectangle (8.5,2.5-\i);
\node[lab] at (9.5,-1.5) {$=$};
\foreach \i in {1,2,3} \foreach \j in {1,2,3} \draw[cell frame] (9.5+\j,-\i) rectangle (10.5+\j,-\i+1);
\draw[hl cell] (12.5,-2) rectangle (13.5,-1);
\node[lab] at (2,-3.7) {$A$ ($3\times4$)}; \node[lab] at (7,-3.7) {$B$ ($4\times3$)}; \node[lab] at (12,-3.7) {$AB$ ($3\times3$)};
\end{tikzpicture}
\end{center}
```

Entry $(i,j)$ of $AB$ is the dot product of row $i$ of $A$ with column $j$ of $B$ (here $i=2$, $j=3$). This needs the number of columns of $A$ to equal the number of rows of $B$.

:::

::: {#thm-four-ways-to-multiply .theorem name="Four ways to see AB"}

Let $A$ be $m\times n$ with columns $\mathbf{a}_k$ and $B$ be $n\times p$ with rows $\mathbf{b}_k^{\mathsf T}$.

1. **Entries:** $(AB)_{ij}$ is a dot product, as in @def-matrix-product.
2. **Columns:** column $j$ of $AB$ is $A$ times column $j$ of $B$, a combination of the columns of $A$.
3. **Rows:** row $i$ of $AB$ is row $i$ of $A$ times $B$, a combination of the rows of $B$.
4. **Columns times rows:** $AB$ is a sum of $n$ matrices of rank one (@sec-math-linear-algebra-vector-spaces-matrix-spaces-and-rank-one),
$$AB=\sum_{k=1}^n\mathbf{a}_k\mathbf{b}_k^{\mathsf T}.$$

:::

::: {.proof}

1. View 1 is the definition.

2. Column $j$ of $AB$ has entries $\sum_k a_{ik}b_{kj}$ for $i=1,\dots,m$. That is $A$ times the vector $(b_{1j},\dots,b_{nj})$ by @prp-row-and-column-views-agree, and by @def-matrix-times-vector it is the combination $\sum_k b_{kj}\mathbf{a}_k$.

3. Row $i$ of $AB$ has entries $\sum_k a_{ik}b_{kj}$ for $j=1,\dots,p$, which is $\sum_k a_{ik}\mathbf{b}_k^{\mathsf T}$.

4. The $(i,j)$ entry of $\mathbf{a}_k\mathbf{b}_k^{\mathsf T}$ is $a_{ik}b_{kj}$. Summing over $k$ gives $(AB)_{ij}$.

:::

::: {#fig-matrix-multiplication-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$1$};
\draw[cell, fill=primaryLight] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$2$};
\draw[cell, fill=primaryLight] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$3$};
\draw[cell, fill=primaryLight] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$4$};
\node[lab, note] at (0.550,-0.350) {$A$};
\draw[cell frame] (1.400,0.550) rectangle (1.950,1.100);
\node[lab] at (1.675,0.825) {$5$};
\draw[hl cell] (1.950,0.550) rectangle (2.500,1.100);
\node[lab] at (2.225,0.825) {$6$};
\draw[cell frame] (1.400,0.000) rectangle (1.950,0.550);
\node[lab] at (1.675,0.275) {$7$};
\draw[hl cell] (1.950,0.000) rectangle (2.500,0.550);
\node[lab] at (2.225,0.275) {$8$};
\node[lab, note] at (1.950,-0.350) {$B$};
\node[lab] at (2.75,0.55) {$=$};
\draw[cell frame] (3.050,0.550) rectangle (3.600,1.100);
\node[lab] at (3.325,0.825) {$19$};
\draw[hl cell] (3.600,0.550) rectangle (4.150,1.100);
\node[lab] at (3.875,0.825) {$22$};
\draw[cell frame] (3.050,0.000) rectangle (3.600,0.550);
\node[lab] at (3.325,0.275) {$43$};
\draw[hl cell] (3.600,0.000) rectangle (4.150,0.550);
\node[lab] at (3.875,0.275) {$50$};
\node[lab, note] at (3.600,-0.350) {$AB$};
\node[lab, anchor=west] at (4.5,0.55) {$A\begin{bmatrix}6\\8\end{bmatrix}=6\begin{bmatrix}1\\3\end{bmatrix}+8\begin{bmatrix}2\\4\end{bmatrix}=\begin{bmatrix}22\\50\end{bmatrix}$};
\begin{scope}[shift={(0,-2.2)}]
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$1$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$2$};
\draw[hl cell] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$3$};
\draw[hl cell] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$4$};
\node[lab, note] at (0.550,-0.350) {$A$};
\draw[cell, fill=primaryLight] (1.400,0.550) rectangle (1.950,1.100);
\node[lab] at (1.675,0.825) {$5$};
\draw[cell, fill=primaryLight] (1.950,0.550) rectangle (2.500,1.100);
\node[lab] at (2.225,0.825) {$6$};
\draw[cell, fill=primaryLight] (1.400,0.000) rectangle (1.950,0.550);
\node[lab] at (1.675,0.275) {$7$};
\draw[cell, fill=primaryLight] (1.950,0.000) rectangle (2.500,0.550);
\node[lab] at (2.225,0.275) {$8$};
\node[lab, note] at (1.950,-0.350) {$B$};
\node[lab] at (2.75,0.55) {$=$};
\draw[cell frame] (3.050,0.550) rectangle (3.600,1.100);
\node[lab] at (3.325,0.825) {$19$};
\draw[cell frame] (3.600,0.550) rectangle (4.150,1.100);
\node[lab] at (3.875,0.825) {$22$};
\draw[hl cell] (3.050,0.000) rectangle (3.600,0.550);
\node[lab] at (3.325,0.275) {$43$};
\draw[hl cell] (3.600,0.000) rectangle (4.150,0.550);
\node[lab] at (3.875,0.275) {$50$};
\node[lab, note] at (3.600,-0.350) {$AB$};
\node[lab, anchor=west] at (4.5,0.55) {$[3\ \ 4]\,B=3\,[5\ \ 6]+4\,[7\ \ 8]=[43\ \ 50]$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Ways 2 and 3 of @thm-four-ways-to-multiply on the matrices of @exm-columns-times-rows. Top: a column of $AB$ is $A$ times that column of $B$, a combination of the columns of $A$. Bottom: a row of $AB$ is that row of $A$ times $B$, a combination of the rows of $B$.

:::

::: {#prp-matrix-product-laws .proposition name="Laws of matrix multiplication"}

Whenever the sizes match,
$$(AB)C=A(BC),\qquad A(B+C)=AB+AC,\qquad (A+B)C=AC+BC.$$
In general $AB\neq BA$.

:::

::: {.proof}

1. Entry $(i,l)$ of $(AB)C$ is $\sum_j\big(\sum_k a_{ik}b_{kj}\big)c_{jl}$; entry $(i,l)$ of $A(BC)$ is $\sum_k a_{ik}\big(\sum_j b_{kj}c_{jl}\big)$. Both equal the double sum $\sum_{j,k}a_{ik}b_{kj}c_{jl}$.

2. The distributive laws follow from $\sum_k a_{ik}(b_{kj}+c_{kj})=\sum_ka_{ik}b_{kj}+\sum_ka_{ik}c_{kj}$, and similarly on the other side.

3. For a counterexample to commutativity take $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$, $B=\begin{bmatrix}0&0\\1&0\end{bmatrix}$: $AB=\begin{bmatrix}1&0\\0&0\end{bmatrix}$ but $BA=\begin{bmatrix}0&0\\0&1\end{bmatrix}$.

:::

Associativity is what lets us collect elimination steps: $E_{32}(E_{31}(E_{21}A))=(E_{32}E_{31}E_{21})A$, one matrix $E$ with $EA=U$.

::: {#prp-block-multiplication .proposition name="Block multiplication"}

If $A$ and $B$ are cut into blocks whose sizes are compatible, for example
$$A=\begin{bmatrix}A_1&A_2\\A_3&A_4\end{bmatrix},\qquad B=\begin{bmatrix}B_1&B_2\\B_3&B_4\end{bmatrix},$$
then $AB$ is computed by the usual rule with blocks in place of numbers:
$$AB=\begin{bmatrix}A_1B_1+A_2B_3&A_1B_2+A_2B_4\\A_3B_1+A_4B_3&A_3B_2+A_4B_4\end{bmatrix}.$$

:::

::: {.proof}

1. Split the sum $\sum_k a_{ik}b_{kj}$ into the $k$ in the first block of columns of $A$ (first block of rows of $B$) and the remaining $k$.

2. For $(i,j)$ in the top-left block, the first part is entry $(i,j)$ of $A_1B_1$ and the second is the entry of $A_2B_3$. The other three blocks are the same computation.

:::

::: {#fig-matrix-multiplication-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.0,0.0) rectangle (0.7,-0.7);
\node[lab] at (0.35,-0.35) {$A_1$};
\draw[hl cell] (0.7,0.0) rectangle (1.4,-0.7);
\node[lab] at (1.05,-0.35) {$A_2$};
\draw[cell frame] (0.0,-0.7) rectangle (0.7,-1.4);
\node[lab] at (0.35,-1.05) {$A_3$};
\draw[cell frame] (0.7,-0.7) rectangle (1.4,-1.4);
\node[lab] at (1.05,-1.05) {$A_4$};
\draw[hl cell] (1.8,0.0) rectangle (2.5,-0.7);
\node[lab] at (2.15,-0.35) {$B_1$};
\draw[cell frame] (2.5,0.0) rectangle (3.2,-0.7);
\node[lab] at (2.85,-0.35) {$B_2$};
\draw[hl cell] (1.8,-0.7) rectangle (2.5,-1.4);
\node[lab] at (2.15,-1.05) {$B_3$};
\draw[cell frame] (2.5,-0.7) rectangle (3.2,-1.4);
\node[lab] at (2.85,-1.05) {$B_4$};
\node[lab] at (3.5,-0.7) {$=$};
\draw[cell frame] (3.9,0) rectangle (8.7,-1.4); \draw[faint] (6.3,0) -- (6.3,-1.4); \draw[faint] (3.9,-0.7) -- (8.7,-0.7);
\draw[hl cell] (3.9,0) rectangle (6.3,-0.7);
\node[lab] at (5.1,-0.35) {$A_1B_1+A_2B_3$}; \node[lab] at (7.5,-0.35) {$A_1B_2+A_2B_4$};
\node[lab] at (5.1,-1.05) {$A_3B_1+A_4B_3$}; \node[lab] at (7.5,-1.05) {$A_3B_2+A_4B_4$};
\end{tikzpicture}
\end{center}
```

Block multiplication follows the entry rule: the top-left block of $AB$ is the first block row of $A$ times the first block column of $B$ (highlighted), with matrix products in place of number products. The order $A_1B_1$, not $B_1A_1$, matters.

:::

::: {#exm-columns-times-rows .example name="Columns times rows"}

$$\begin{bmatrix}1&2\\3&4\end{bmatrix}\begin{bmatrix}5&6\\7&8\end{bmatrix}
=\begin{bmatrix}1\\3\end{bmatrix}\begin{bmatrix}5&6\end{bmatrix}+\begin{bmatrix}2\\4\end{bmatrix}\begin{bmatrix}7&8\end{bmatrix}
=\begin{bmatrix}5&6\\15&18\end{bmatrix}+\begin{bmatrix}14&16\\28&32\end{bmatrix}
=\begin{bmatrix}19&22\\43&50\end{bmatrix}.$$

:::

::: {#fig-matrix-multiplication-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$1$};
\draw[cell, fill=primaryLight] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$3$};
\draw[cell, fill=primaryLight] (0.700,0.550) rectangle (1.250,1.100);
\node[lab] at (0.975,0.825) {$5$};
\draw[cell, fill=primaryLight] (1.250,0.550) rectangle (1.800,1.100);
\node[lab] at (1.525,0.825) {$6$};
\node[lab] at (2.15,0.55) {$+$};
\draw[hl cell] (2.500,0.550) rectangle (3.050,1.100);
\node[lab] at (2.775,0.825) {$2$};
\draw[hl cell] (2.500,0.000) rectangle (3.050,0.550);
\node[lab] at (2.775,0.275) {$4$};
\draw[hl cell] (3.200,0.550) rectangle (3.750,1.100);
\node[lab] at (3.475,0.825) {$7$};
\draw[hl cell] (3.750,0.550) rectangle (4.300,1.100);
\node[lab] at (4.025,0.825) {$8$};
\node[lab] at (4.65,0.55) {$=$};
\draw[cell, fill=primaryLight] (5.000,0.550) rectangle (5.550,1.100);
\node[lab] at (5.275,0.825) {$5$};
\draw[cell, fill=primaryLight] (5.550,0.550) rectangle (6.100,1.100);
\node[lab] at (5.825,0.825) {$6$};
\draw[cell, fill=primaryLight] (5.000,0.000) rectangle (5.550,0.550);
\node[lab] at (5.275,0.275) {$15$};
\draw[cell, fill=primaryLight] (5.550,0.000) rectangle (6.100,0.550);
\node[lab] at (5.825,0.275) {$18$};
\node[lab] at (6.4,0.55) {$+$};
\draw[hl cell] (6.750,0.550) rectangle (7.300,1.100);
\node[lab] at (7.025,0.825) {$14$};
\draw[hl cell] (7.300,0.550) rectangle (7.850,1.100);
\node[lab] at (7.575,0.825) {$16$};
\draw[hl cell] (6.750,0.000) rectangle (7.300,0.550);
\node[lab] at (7.025,0.275) {$28$};
\draw[hl cell] (7.300,0.000) rectangle (7.850,0.550);
\node[lab] at (7.575,0.275) {$32$};
\node[lab] at (8.15,0.55) {$=$};
\draw[cell frame] (8.450,0.550) rectangle (9.000,1.100);
\node[lab] at (8.725,0.825) {$19$};
\draw[cell frame] (9.000,0.550) rectangle (9.550,1.100);
\node[lab] at (9.275,0.825) {$22$};
\draw[cell frame] (8.450,0.000) rectangle (9.000,0.550);
\node[lab] at (8.725,0.275) {$43$};
\draw[cell frame] (9.000,0.000) rectangle (9.550,0.550);
\node[lab] at (9.275,0.275) {$50$};
\end{tikzpicture}
\end{center}
```

@exm-columns-times-rows as two layers: column $k$ of $A$ times row $k$ of $B$ is a full $2\times2$ matrix of rank one, and $AB$ is the sum of these layers.

:::
