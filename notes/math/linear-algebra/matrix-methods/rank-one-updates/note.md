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

::: {#fig-rank-one-updates-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (0,0) {$(A+\mathbf u\mathbf v^{\mathsf T})^{-1}=A^{-1}-\dfrac{A^{-1}\mathbf u\;\mathbf v^{\mathsf T}A^{-1}}{1+\mathbf v^{\mathsf T}A^{-1}\mathbf u}$};
\draw[cell frame] (-1.2,-0.9) rectangle (-0.95,-1.9); \node[lab, tick] at (-1.075,-2.1) {$A^{-1}\mathbf u$};
\draw[cell frame] (-0.8,-0.9) rectangle (0.2,-1.15); \node[lab, tick] at (-0.3,-1.35) {$\mathbf v^{\mathsf T}A^{-1}$};
\draw[hl cell] (1.6,-1.25) rectangle (1.85,-1.5); \node[lab, tick] at (1.725,-1.75) {a number};
\node[lab, note, anchor=west, align=left] at (2.6,-1.4) {the correction is column times row:\\rank one, cost $O(n^2)$ once $A^{-1}$ is known};
\end{tikzpicture}
\end{center}
```

The shapes in the Sherman–Morrison formula: the change to $A^{-1}$ is a column times a row divided by a single number, which must not be $0$.

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

::: {#fig-rank-one-updates-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (0,0) {$(A+UCV^{\mathsf T})^{-1}=A^{-1}-A^{-1}U\big(C^{-1}+V^{\mathsf T}A^{-1}U\big)^{-1}V^{\mathsf T}A^{-1}$};
\draw[cell frame] (-2.0,-0.8) rectangle (-1.4,-2.4); \node[lab, tick] at (-1.7,-2.6) {$A^{-1}U$: $n\times k$};
\draw[hl cell] (-0.6,-0.8) rectangle (0,-1.4); \node[lab, tick] at (-0.3,-1.65) {$k\times k$};
\draw[cell frame] (0.8,-0.8) rectangle (2.4,-1.4); \node[lab, tick] at (1.6,-1.65) {$V^{\mathsf T}A^{-1}$: $k\times n$};
\node[lab, note, anchor=west] at (2.9,-1.1) {only a small $k\times k$ inverse is new};
\end{tikzpicture}
\end{center}
```

The Woodbury formula for a rank $k$ change $UCV^{\mathsf T}$: the update to the inverse is a thin $n\times k$ matrix, a small $k\times k$ inverse and a wide $k\times n$ matrix. For $k=1$ it is Sherman–Morrison.

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

::: {#fig-rank-one-updates-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(1.2,0)}]
\draw[->, muted] (-0.3,0) -- (2.2,0); \draw[->, muted] (0,-0.3) -- (0,1.4);
\draw[faint] (0,0) rectangle (1,1);
\fill[tintA] (0.000,0.000) -- (1.000,0.000) -- (0.000,1.000) -- (-1.000,1.000) -- cycle;
\draw[primary] (0,0) -- (1,0) -- (0,1) -- (-1,1) -- cycle;
\node[lab, note] at (0.6,-0.5) {$\begin{bmatrix}1&-1\\0&1\end{bmatrix}$: shear left};
\end{scope}
\begin{scope}[shift={(6.2,0)}]
\draw[->, muted] (-0.3,0) -- (2.2,0); \draw[->, muted] (0,-0.3) -- (0,1.4);
\draw[faint] (0,0) rectangle (1,1);
\fill[tintA] (0.000,0.000) -- (1.000,0.000) -- (2.000,1.000) -- (1.000,1.000) -- cycle;
\draw[primary] (0,0) -- (1,0) -- (2,1) -- (1,1) -- cycle;
\node[lab, note] at (0.6,-0.5) {its inverse $\begin{bmatrix}1&1\\0&1\end{bmatrix}$: shear right};
\end{scope}
\end{tikzpicture}
\end{center}
```

@exm-rank-one-update: $I-\mathbf u\mathbf v^{\mathsf T}$ with $\mathbf u=(1,0)$, $\mathbf v=(0,1)$ shears the unit square to the left, and its inverse $I+\mathbf u\mathbf v^{\mathsf T}$ shears it back. Since $\mathbf v^{\mathsf T}\mathbf u=0$ the denominator in Sherman–Morrison is $1$.

:::

::: {#rmk-rank-one-updates-1 .remark name="Updating least squares"}

Adding one new observation (a row $\mathbf{r}^{\mathsf T}$ of $A$ with value $b$) changes $A^{\mathsf T}A$ to $A^{\mathsf T}A+\mathbf{r}\mathbf{r}^{\mathsf T}$, a rank one change. Sherman–Morrison with $\mathbf{u}=-\mathbf{r}$, $\mathbf{v}=\mathbf{r}$ updates $(A^{\mathsf T}A)^{-1}$ in $O(n^2)$ operations; this is the idea behind recursive least squares and the Kalman filter.

:::
