---
title: "Low-Rank Changes in A and Its Inverse"
sources: [mit18065-14]
requires: [math/linear-algebra/systems/inverse-matrices]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lecture 14 (video lecture and problem set; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->

When $A$ changes by a matrix of low rank, its inverse also changes by a matrix of low rank. This lets us update a solution, a factorisation or a least squares fit when one row or column of data changes, without starting again.

::: {#thm-sherman-morrison .theorem name="Sherman–Morrison formula"}

If $A$ is invertible and $1-\mathbf{v}^{\mathsf T}A^{-1}\mathbf{u}\ne0$, then $A-\mathbf{u}\mathbf{v}^{\mathsf T}$ is invertible and
$$(A-\mathbf{u}\mathbf{v}^{\mathsf T})^{-1}=A^{-1}+\frac{A^{-1}\mathbf{u}\,\mathbf{v}^{\mathsf T}A^{-1}}{1-\mathbf{v}^{\mathsf T}A^{-1}\mathbf{u}} .$$
For $A=I$: $(I-\mathbf{u}\mathbf{v}^{\mathsf T})^{-1}=I+\dfrac{\mathbf{u}\mathbf{v}^{\mathsf T}}{1-\mathbf{v}^{\mathsf T}\mathbf{u}}$.

:::

::: {.proof}

1. Write $\mathbf{z}=A^{-1}\mathbf{u}$ and $D=1-\mathbf{v}^{\mathsf T}\mathbf{z}$. The claimed inverse is $N=A^{-1}+\mathbf{z}\mathbf{v}^{\mathsf T}A^{-1}/D$.

2. Multiply: $(A-\mathbf{u}\mathbf{v}^{\mathsf T})N=I-\mathbf{u}\mathbf{v}^{\mathsf T}A^{-1}+\dfrac{\mathbf{u}\mathbf{v}^{\mathsf T}A^{-1}-\mathbf{u}(\mathbf{v}^{\mathsf T}\mathbf{z})\mathbf{v}^{\mathsf T}A^{-1}}{D}$, using $A\mathbf{z}=\mathbf{u}$.

3. The fraction is $\mathbf{u}\mathbf{v}^{\mathsf T}A^{-1}\,(1-\mathbf{v}^{\mathsf T}\mathbf{z})/D=\mathbf{u}\mathbf{v}^{\mathsf T}A^{-1}$, which cancels the middle term. So the product is $I$.

4. The column space of $A-\mathbf{u}\mathbf{v}^{\mathsf T}$ therefore contains every column of $I$, so this square matrix has rank $n$, is invertible, and its inverse is $N$.

:::

::: {#fig-rank-one-updates-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\draw[cell frame] (0,0) rectangle (1.6,1.6); \node[lab] at (0.8,0.8) {$A$};
\node[lab] at (2.0,0.8) {$+$};
\draw[hl cell] (2.4,0) rectangle (2.7,1.6); \node[lab, below] at (2.55,0) {$\mathbf u$};
\draw[hl cell] (2.9,1.3) rectangle (4.5,1.6); \node[lab, below] at (3.7,1.3) {$\mathbf v^{\mathsf T}$};
\node[lab] at (5.1,0.8) {$\Longrightarrow$};
\draw[cell frame] (5.7,0) rectangle (7.3,1.6); \node[lab] at (6.5,0.8) {$A^{-1}$};
\node[lab] at (7.7,0.8) {$-$};
\draw[hl cell] (8.1,0) rectangle (8.4,1.6);
\draw[hl cell] (8.6,1.3) rectangle (10.2,1.6);
\node[lab, below] at (9.15,-0.2) {$\dfrac{(A^{-1}\mathbf u)(\mathbf v^{\mathsf T}A^{-1})}{1+\mathbf v^{\mathsf T}A^{-1}\mathbf u}$};
\end{tikzpicture}
\end{center}
```

A rank one change of $A$ (a column times a row) changes $A^{-1}$ by another rank one matrix, so the new inverse costs a few matrix–vector products instead of a fresh inversion.

:::

::: {#thm-woodbury .theorem name="Woodbury formula"}

Let $A$ ($n\times n$) be invertible, $U$ be $n\times k$, $V$ be $n\times k$, and suppose $I_k-V^{\mathsf T}A^{-1}U$ is invertible. Then
$$(A-UV^{\mathsf T})^{-1}=A^{-1}+A^{-1}U\,(I_k-V^{\mathsf T}A^{-1}U)^{-1}\,V^{\mathsf T}A^{-1}.$$
A change of rank $k$ in $A$ costs one $k\times k$ inverse instead of a new $n\times n$ inverse.

:::

::: {.proof}

1. Let $Z=A^{-1}U$ and $K=I_k-V^{\mathsf T}Z$. Then $(A-UV^{\mathsf T})(A^{-1}+ZK^{-1}V^{\mathsf T}A^{-1})=I-UV^{\mathsf T}A^{-1}+U K^{-1}V^{\mathsf T}A^{-1}-U(V^{\mathsf T}Z)K^{-1}V^{\mathsf T}A^{-1}$.

2. The last two terms are $U(I_k-V^{\mathsf T}Z)K^{-1}V^{\mathsf T}A^{-1}=UV^{\mathsf T}A^{-1}$, which cancels the second term.

3. So the product is $I$, as in @thm-sherman-morrison with $k=1$.

:::

::: {#prp-solve-after-rank-one-update .proposition name="Solving after a rank one change"}

To solve $(A-\mathbf{u}\mathbf{v}^{\mathsf T})\mathbf{y}=\mathbf{b}$ using only solves with $A$: solve $A\mathbf{x}=\mathbf{b}$ and $A\mathbf{z}=\mathbf{u}$, then
$$\mathbf{y}=\mathbf{x}+\frac{\mathbf{v}^{\mathsf T}\mathbf{x}}{1-\mathbf{v}^{\mathsf T}\mathbf{z}}\,\mathbf{z}.$$
With a factorisation $A=LU$ already computed, the cost is two triangular solve pairs, $O(n^2)$, instead of a new $O(n^3)$ elimination.

:::

::: {.proof}

Multiply @thm-sherman-morrison by $\mathbf{b}$: $A^{-1}\mathbf{b}=\mathbf{x}$ and $A^{-1}\mathbf{u}\,\mathbf{v}^{\mathsf T}A^{-1}\mathbf{b}=\mathbf{z}\,(\mathbf{v}^{\mathsf T}\mathbf{x})$.

:::

::: {#exm-rank-one-update .example name="A shear"}

With $A=I$, $\mathbf{u}=(1,0)$, $\mathbf{v}=(0,1)$: $\mathbf{v}^{\mathsf T}\mathbf{u}=0$, so
$$\begin{bmatrix}1&-1\\0&1\end{bmatrix}^{-1}=I+\mathbf{u}\mathbf{v}^{\mathsf T}=\begin{bmatrix}1&1\\0&1\end{bmatrix}.$$
If instead $\mathbf{v}=(1,0)$, then $\mathbf{v}^{\mathsf T}\mathbf{u}=1$ and $I-\mathbf{u}\mathbf{v}^{\mathsf T}=\operatorname{diag}(0,1)$ is singular, as the formula warns.

:::

::: {#rmk-rank-one-updates-1 .remark name="Updating least squares"}

Adding one new observation (a row $\mathbf{r}^{\mathsf T}$ of $A$ with value $b$) changes $A^{\mathsf T}A$ to $A^{\mathsf T}A+\mathbf{r}\mathbf{r}^{\mathsf T}$, a rank one change. Sherman–Morrison with $\mathbf{u}=-\mathbf{r}$, $\mathbf{v}=\mathbf{r}$ updates $(A^{\mathsf T}A)^{-1}$ in $O(n^2)$ operations; this is the idea behind recursive least squares and the Kalman filter.

:::
