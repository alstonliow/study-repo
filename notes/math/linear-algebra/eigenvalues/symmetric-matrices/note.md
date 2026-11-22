---
title: "Symmetric Matrices and the Spectral Theorem"
sources: [mit1806-25]
requires: [math/linear-algebra/eigenvalues/diagonalization, math/linear-algebra/orthogonality/orthonormal-bases-and-gram-schmidt]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 25 (first half), in our own wording; proofs written out in steps. The second half of the lecture (positive definiteness) is in the note on positive definite matrices. -->

Symmetric matrices ($S^{\mathsf T}=S$, @def-symmetric-matrix) are the most important matrices in applications, and their eigenvalues and eigenvectors are as good as possible.

<!-- Merged 2026-11-20 (owner): the block thm-symmetric-real-eigenvalues was removed in favour of lem-self-adjoint-eigenvalues (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Real eigenvalues, orthogonal eigenvectors.** A real symmetric matrix $S$ has only real eigenvalues, and eigenvectors for different eigenvalues are orthogonal. In short: $\bar{\mathbf x}^{\mathsf T}S\mathbf x$ equals both $\lambda\lVert\mathbf x\rVert^2$ and $\bar\lambda\lVert\mathbf x\rVert^2$. See @lem-self-adjoint-eigenvalues, which proves it for every self-adjoint map.

<!-- Merged 2026-11-20 (owner): the block thm-spectral-theorem was removed in favour of cor-real-symmetric-orthogonally-diagonalisable (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Spectral theorem.** Every real symmetric matrix can be factored as
$$S=Q\Lambda Q^{\mathsf T}=\lambda_1\mathbf{q}_1\mathbf{q}_1^{\mathsf T}+\dots+\lambda_n\mathbf{q}_n\mathbf{q}_n^{\mathsf T},$$
with $Q$ orthogonal (@def-orthogonal-matrix), $\Lambda$ real diagonal, and the columns $\mathbf q_i$ orthonormal eigenvectors. The proof splits off one real unit eigenvector at a time: @cor-real-symmetric-orthogonally-diagonalisable and @thm-spectral-theorem-self-adjoint.

Each $\mathbf{q}_i\mathbf{q}_i^{\mathsf T}$ is the projection onto the line through $\mathbf{q}_i$ (@prp-projection-with-orthonormal-columns). So every symmetric matrix is a combination of perpendicular projections, weighted by its eigenvalues.

::: {#exm-spectral-two-by-two .example name="A 2 by 2 symmetric matrix"}

$S=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ has $\lambda=3$ with $\mathbf{q}_1=\frac1{\sqrt2}(1,1)$ and $\lambda=1$ with $\mathbf{q}_2=\frac1{\sqrt2}(1,-1)$:
$$S=3\cdot\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}+1\cdot\frac12\begin{bmatrix}1&-1\\-1&1\end{bmatrix}.$$

:::

::: {#fig-symmetric-matrices-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$1$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\node[lab, note] at (0.550,-0.350) {$S$};
\node[lab] at (1.35,0.55) {$=3$};
\draw[cell, fill=primaryLight] (1.700,0.550) rectangle (2.250,1.100);
\node[lab] at (1.975,0.825) {$\frac12$};
\draw[cell, fill=primaryLight] (2.250,0.550) rectangle (2.800,1.100);
\node[lab] at (2.525,0.825) {$\frac12$};
\draw[cell, fill=primaryLight] (1.700,0.000) rectangle (2.250,0.550);
\node[lab] at (1.975,0.275) {$\frac12$};
\draw[cell, fill=primaryLight] (2.250,0.000) rectangle (2.800,0.550);
\node[lab] at (2.525,0.275) {$\frac12$};
\node[lab, note] at (2.250,-0.350) {$\mathbf q_1\mathbf q_1^{\mathsf T}$};
\node[lab] at (3.05,0.55) {$+\,1$};
\draw[hl cell] (3.400,0.550) rectangle (3.950,1.100);
\node[lab] at (3.675,0.825) {$\frac12$};
\draw[hl cell] (3.950,0.550) rectangle (4.500,1.100);
\node[lab] at (4.225,0.825) {$-\frac12$};
\draw[hl cell] (3.400,0.000) rectangle (3.950,0.550);
\node[lab] at (3.675,0.275) {$-\frac12$};
\draw[hl cell] (3.950,0.000) rectangle (4.500,0.550);
\node[lab] at (4.225,0.275) {$\frac12$};
\node[lab, note] at (3.950,-0.350) {$\mathbf q_2\mathbf q_2^{\mathsf T}$};
\begin{scope}[shift={(6.6,0.4)}]
\draw[->, muted] (-1.0,0) -- (1.1,0);
\draw[->, muted] (0,-1.0) -- (0,1.1);
\draw[->, emph, primary] (0,0) -- (0.6,0.6) node[right, lab] {$\mathbf q_1$};
\draw[->, emph, accent] (0,0) -- (0.6,-0.6) node[right, lab] {$\mathbf q_2$};
\draw[muted] (0.14,0.14) -- (0.28,0) -- (0.14,-0.14);
\end{scope}
\end{tikzpicture}
\end{center}
```

@exm-spectral-two-by-two: $S$ is a sum of projections onto its perpendicular eigenvector lines, each weighted by its eigenvalue. The two projection matrices add to $I$ and multiply to $0$.

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

2. As $t$ goes from $1$ to $0$, the eigenvalues of $S_t$ move continuously and are real (@lem-self-adjoint-eigenvalues); none can cross $0$, because $\det S_t\ne0$.

3. At $t=0$, $S_0=D$, whose eigenvalues are the pivots. So the sign pattern of the eigenvalues of $S=S_1$ matches the pivots.

:::

::: {#fig-symmetric-matrices-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$1$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$3$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$3$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$1$};
\node[lab, note] at (0.550,-0.350) {$S$};
\draw[->] (1.3,0.55) -- (2.3,0.55) node[midway, above, lab, tick] {eliminate};
\draw[hl cell] (2.500,0.550) rectangle (3.050,1.100);
\node[lab] at (2.775,0.825) {$1$};
\draw[cell frame] (3.050,0.550) rectangle (3.600,1.100);
\node[lab] at (3.325,0.825) {$3$};
\draw[cell frame] (2.500,0.000) rectangle (3.050,0.550);
\node[lab] at (2.775,0.275) {$0$};
\draw[hl cell] (3.050,0.000) rectangle (3.600,0.550);
\node[lab] at (3.325,0.275) {$-8$};
\node[lab, note] at (3.050,-0.350) {pivots $1,-8$};
\node[lab, anchor=west, align=left] at (4.1,0.55) {eigenvalues $4,-2$:\\one positive, one negative,\\like the pivots};
\end{tikzpicture}
\end{center}
```

For a symmetric matrix the pivots and the eigenvalues have the same signs, counted with multiplicity, though not the same values. Here $\det S=-8$ is both $1\cdot(-8)$ and $4\cdot(-2)$.

:::
