---
title: "Symmetric Matrices and the Spectral Theorem"
sources: [mit1806-25]
requires: [math/linear-algebra/eigenvalues/diagonalization, math/linear-algebra/orthogonality/orthonormal-bases-and-gram-schmidt]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 25 (first half), in our own wording; proofs written out in steps. The second half of the lecture (positive definiteness) is in the note on positive definite matrices. -->

Symmetric matrices ($S^{\mathsf T}=S$, @def-symmetric-matrix) are the most important matrices in applications, and their eigenvalues and eigenvectors are as good as possible.

::: {#thm-symmetric-real-eigenvalues .theorem name="Real eigenvalues, orthogonal eigenvectors"}

Let $S$ be a real symmetric matrix.

1. Every eigenvalue of $S$ is real.
2. Eigenvectors for different eigenvalues are orthogonal.

:::

::: {.proof}

1. Let $S\mathbf{x}=\lambda\mathbf{x}$ with $\mathbf{x}\in\mathbb{C}^n$ nonzero. Take complex conjugates: $S\bar{\mathbf{x}}=\bar\lambda\bar{\mathbf{x}}$, since $S$ is real.

2. Compute $\bar{\mathbf{x}}^{\mathsf T}S\mathbf{x}$ in two ways: it equals $\lambda\,\bar{\mathbf{x}}^{\mathsf T}\mathbf{x}$, and, using $S^{\mathsf T}=S$, it equals $(S\bar{\mathbf{x}})^{\mathsf T}\mathbf{x}=\bar\lambda\,\bar{\mathbf{x}}^{\mathsf T}\mathbf{x}$.

3. $\bar{\mathbf{x}}^{\mathsf T}\mathbf{x}=\sum\lvert x_i\rvert^2>0$, so $\lambda=\bar\lambda$ is real.

4. If $S\mathbf{x}=\lambda\mathbf{x}$ and $S\mathbf{y}=\mu\mathbf{y}$ with $\lambda\neq\mu$, then $\lambda\,\mathbf{y}^{\mathsf T}\mathbf{x}=\mathbf{y}^{\mathsf T}S\mathbf{x}=(S\mathbf{y})^{\mathsf T}\mathbf{x}=\mu\,\mathbf{y}^{\mathsf T}\mathbf{x}$, so $(\lambda-\mu)\mathbf{y}^{\mathsf T}\mathbf{x}=0$ and $\mathbf{y}^{\mathsf T}\mathbf{x}=0$.

:::

::: {#thm-spectral-theorem .theorem name="Spectral theorem"}

Every real symmetric matrix can be factored as
$$S=Q\Lambda Q^{\mathsf T}=\lambda_1\mathbf{q}_1\mathbf{q}_1^{\mathsf T}+\dots+\lambda_n\mathbf{q}_n\mathbf{q}_n^{\mathsf T},$$
with $Q$ orthogonal (@def-orthogonal-matrix) and $\Lambda$ real diagonal. The columns $\mathbf{q}_i$ are orthonormal eigenvectors.

:::

::: {.proof}

1. Induction on $n$; $n=1$ is clear. Take a real eigenvalue $\lambda_1$ (@thm-symmetric-real-eigenvalues) and a real unit eigenvector $\mathbf{q}_1$ (solve $(S-\lambda_1I)\mathbf{x}=\mathbf{0}$ over $\mathbb{R}$ and normalise).

2. Extend $\mathbf{q}_1$ to an orthonormal basis $\mathbf{q}_1,\dots,\mathbf{q}_n$ of $\mathbb{R}^n$ (Gram–Schmidt, @thm-gram-schmidt) and let $Q_1$ have these columns. Then $Q_1^{\mathsf T}SQ_1$ is symmetric, and its first column is $Q_1^{\mathsf T}S\mathbf{q}_1=\lambda_1Q_1^{\mathsf T}\mathbf{q}_1=\lambda_1\mathbf{e}_1$. By symmetry its first row is $\lambda_1\mathbf{e}_1^{\mathsf T}$:
   $$Q_1^{\mathsf T}SQ_1=\begin{bmatrix}\lambda_1&\mathbf{0}^{\mathsf T}\\\mathbf{0}&S'\end{bmatrix}.$$

3. $S'$ is symmetric of size $n-1$; by induction $S'=Q'\Lambda'Q'^{\mathsf T}$. Then $Q=Q_1\begin{bmatrix}1&0\\0&Q'\end{bmatrix}$ is orthogonal (a product of orthogonal matrices) and $Q^{\mathsf T}SQ=\operatorname{diag}(\lambda_1,\Lambda')$.

4. The second form is columns times rows (@thm-four-ways-to-multiply) applied to $(Q\Lambda)Q^{\mathsf T}$.

:::

Each $\mathbf{q}_i\mathbf{q}_i^{\mathsf T}$ is the projection onto the line through $\mathbf{q}_i$ (@prp-projection-with-orthonormal-columns). So every symmetric matrix is a combination of perpendicular projections, weighted by its eigenvalues.

::: {#exm-spectral-two-by-two .example name="A 2 by 2 symmetric matrix"}

$S=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ has $\lambda=3$ with $\mathbf{q}_1=\frac1{\sqrt2}(1,1)$ and $\lambda=1$ with $\mathbf{q}_2=\frac1{\sqrt2}(1,-1)$:
$$S=3\cdot\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}+1\cdot\frac12\begin{bmatrix}1&-1\\-1&1\end{bmatrix}.$$

:::

::: {#fig-symmetric-matrices-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\draw[->] (-3.3,0) -- (3.4,0) node[lab, right] {$x_1$};
\draw[->] (0,-2.6) -- (0,2.8) node[lab, above] {$x_2$};
\draw[faint] (0,0) circle (1);
\draw[emph, primary, rotate=45] (0,0) ellipse (3 and 1);
\draw[->, hl] (0,0) -- (45:3) node[lab, above right] {$S\mathbf q_1=3\mathbf q_1$};
\draw[->, emph] (0,0) -- (45:1);
\node[lab, above left] at (45:0.8) {$\mathbf q_1$};
\draw[->, emph, accent] (0,0) -- (-45:1) node[lab, below right] {$S\mathbf q_2=\mathbf q_2$};
\end{tikzpicture}
\end{center}
```

$S=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ maps the unit circle (faint) to an ellipse. Its axes lie along the orthonormal eigenvectors $\mathbf q_1,\mathbf q_2$ and are stretched by the eigenvalues $3$ and $1$.

:::

::: {#prp-signs-of-pivots-and-eigenvalues .proposition name="Signs of pivots and eigenvalues"}

For a symmetric matrix with nonzero pivots (no row exchanges needed), the number of positive pivots equals the number of positive eigenvalues.

:::

::: {.proof}

1. Write $S=LDL^{\mathsf T}$ (@prp-symmetric-ldlt) and consider $S_t=L_tDL_t^{\mathsf T}$, where $L_t$ has the off-diagonal entries of $L$ multiplied by $t\in[0,1]$. Each $S_t$ is symmetric with pivots $D$, so $\det S_t=\det D\neq0$.

2. As $t$ goes from $1$ to $0$, the eigenvalues of $S_t$ move continuously and are real (@thm-symmetric-real-eigenvalues); none can cross $0$, because $\det S_t\ne0$.

3. At $t=0$, $S_0=D$, whose eigenvalues are the pivots. So the sign pattern of the eigenvalues of $S=S_1$ matches the pivots.

:::
