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

::: {#exm-columns-times-rows .example name="Columns times rows"}

$$\begin{bmatrix}1&2\\3&4\end{bmatrix}\begin{bmatrix}5&6\\7&8\end{bmatrix}
=\begin{bmatrix}1\\3\end{bmatrix}\begin{bmatrix}5&6\end{bmatrix}+\begin{bmatrix}2\\4\end{bmatrix}\begin{bmatrix}7&8\end{bmatrix}
=\begin{bmatrix}5&6\\15&18\end{bmatrix}+\begin{bmatrix}14&16\\28&32\end{bmatrix}
=\begin{bmatrix}19&22\\43&50\end{bmatrix}.$$

:::
