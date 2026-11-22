---
title: "Projections onto Subspaces"
sources: [mit1806-15, mit1806-16]
requires: [math/linear-algebra/orthogonality/orthogonal-subspaces]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lectures 15 and 16, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

## Projection onto a line

::: {#thm-projection-onto-line .theorem name="Projection onto a line"}

Let $\mathbf{a}\neq\mathbf{0}$ in $\mathbb{R}^m$. The point on the line through $\mathbf{a}$ closest to $\mathbf{b}$ is
$$\mathbf{p}=\frac{\mathbf{a}^{\mathsf T}\mathbf{b}}{\mathbf{a}^{\mathsf T}\mathbf{a}}\,\mathbf{a}=P\mathbf{b},\qquad P=\frac{\mathbf{a}\mathbf{a}^{\mathsf T}}{\mathbf{a}^{\mathsf T}\mathbf{a}}.$$
The error $\mathbf{e}=\mathbf{b}-\mathbf{p}$ is perpendicular to $\mathbf{a}$.

:::

::: {.proof}

1. Write $\mathbf{p}=\hat x\,\mathbf{a}$. Requiring $\mathbf{a}^{\mathsf T}(\mathbf{b}-\hat x\mathbf{a})=0$ gives $\hat x=\mathbf{a}^{\mathsf T}\mathbf{b}/\mathbf{a}^{\mathsf T}\mathbf{a}$.

2. For any other point $c\,\mathbf{a}$ on the line, $\mathbf{b}-c\mathbf{a}=\mathbf{e}+(\hat x-c)\mathbf{a}$ with $\mathbf{e}\perp\mathbf{a}$, so by @prp-pythagoras-orthogonal $\lVert\mathbf{b}-c\mathbf{a}\rVert^2=\lVert\mathbf{e}\rVert^2+(\hat x-c)^2\lVert\mathbf{a}\rVert^2\ge\lVert\mathbf{e}\rVert^2$, with equality only at $c=\hat x$.

3. $\hat x\,\mathbf{a}=\mathbf{a}\hat x=\mathbf{a}\,\frac{\mathbf{a}^{\mathsf T}\mathbf{b}}{\mathbf{a}^{\mathsf T}\mathbf{a}}=P\mathbf{b}$.

:::

::: {#fig-projections-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.3,-0.1) -- (3.6,1.2);
\draw[->, emph] (0.000,0.000) -- (3.000,1.000);
\node[lab, below right] at (3.000,1.000) {$\mathbf a$};
\draw[->, emph] (0.000,0.000) -- (1.600,2.400);
\node[lab, above left] at (1.600,2.400) {$\mathbf b$};
\draw[->, hl] (0.000,0.000) -- (2.160,0.720);
\node[lab, below right] at (2.160,0.720) {$\mathbf p=\hat x\mathbf a$};
\draw[dashed] (2.160,0.720) -- node[lab, right] {$\mathbf e=\mathbf b-\mathbf p$} (1.600,2.400);
\draw[faint] (1.989,0.663) -- (1.932,0.834) -- (2.103,0.891);
\end{tikzpicture}
\end{center}
```

Projecting $\mathbf b$ onto the line through $\mathbf a$: the error $\mathbf e$ is perpendicular to $\mathbf a$.

:::

::: {#exm-projection-onto-line .example name="Projecting onto a line"}

Project $\mathbf{b}=(1,1,1)$ onto $\mathbf{a}=(1,2,2)$: $\mathbf{a}^{\mathsf T}\mathbf{b}=5$, $\mathbf{a}^{\mathsf T}\mathbf{a}=9$, so $\mathbf{p}=\frac59(1,2,2)$ and $\mathbf{e}=\frac19(4,-1,-1)$, which is indeed perpendicular to $\mathbf{a}$. The projection matrix is
$$P=\frac19\begin{bmatrix}1&2&2\\2&4&4\\2&4&4\end{bmatrix},$$
of rank $1$, with $P^{\mathsf T}=P$ and $P^2=P$.

:::

## Projection onto a subspace

::: {#thm-projection-onto-subspace .theorem name="Projection onto a column space"}

Let $A$ be $m\times n$ with independent columns. The point of $C(A)$ closest to $\mathbf{b}\in\mathbb{R}^m$ is $\mathbf{p}=A\hat{\mathbf{x}}$, where $\hat{\mathbf{x}}$ solves the *normal equations*
$$A^{\mathsf T}A\,\hat{\mathbf{x}}=A^{\mathsf T}\mathbf{b}.$$
So $\mathbf{p}=P\mathbf{b}$ with
$$P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}.$$

:::

::: {.proof}

1. The error $\mathbf{e}=\mathbf{b}-A\hat{\mathbf{x}}$ should be perpendicular to every column of $A$: $A^{\mathsf T}(\mathbf{b}-A\hat{\mathbf{x}})=\mathbf{0}$, which is the normal equations. $A^{\mathsf T}A$ is invertible by @thm-ata-invertible, so $\hat{\mathbf{x}}$ is unique.

2. Then $\mathbf{e}\in N(A^{\mathsf T})=C(A)^{\perp}$ (@thm-fundamental-theorem-orthogonality). For any $A\mathbf{x}\in C(A)$, $\mathbf{b}-A\mathbf{x}=\mathbf{e}+A(\hat{\mathbf{x}}-\mathbf{x})$ is a sum of orthogonal vectors, so $\lVert\mathbf{b}-A\mathbf{x}\rVert^2=\lVert\mathbf{e}\rVert^2+\lVert A(\hat{\mathbf{x}}-\mathbf{x})\rVert^2\ge\lVert\mathbf{e}\rVert^2$.

3. Substituting $\hat{\mathbf{x}}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}\mathbf{b}$ gives the formula for $P$.

:::

::: {#fig-projections-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\fill[tintA] (-1.6,-0.7) -- (2.6,-0.7) -- (3.6,0.9) -- (-0.6,0.9) -- cycle;
\draw[faint] (-1.6,-0.7) -- (2.6,-0.7) -- (3.6,0.9) -- (-0.6,0.9) -- cycle;
\node[lab, note, primary] at (3.0,-0.45) {$C(A)$};
\fill[ink] (0,0) circle[pt] node[below left, lab, tick] {$\mathbf 0$};
\draw[->, emph, ink] (0,0) -- (2,2.1) node[above, lab] {$\mathbf b$};
\draw[->, emph, primary] (0,0) -- (2,0.3) node[below right, lab] {$\mathbf p=A\hat{\mathbf x}$};
\draw[->, emph, accent] (2,0.3) -- (2,2.1) node[midway, right, lab] {$\mathbf e$};
\draw[muted] (2,0.5) -- (1.82,0.47) -- (1.82,0.27);
\end{scope}
\node[lab, note, anchor=west, align=left] at (4.2,1.0) {$A^{\mathsf T}\mathbf e=\mathbf 0$ gives\\$\hat{\mathbf x}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}\mathbf b$,\\$P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$};
\end{tikzpicture}
\end{center}
```

Projection onto the column space of $A$: $\mathbf p$ is a combination $A\hat{\mathbf x}$ of the columns, and the error $\mathbf e=\mathbf b-A\hat{\mathbf x}$ is perpendicular to each column.

:::

::: {#prp-projection-matrix-properties .proposition name="Properties of projection matrices"}

The matrix $P$ of @thm-projection-onto-subspace satisfies
$$P^{\mathsf T}=P,\qquad P^2=P.$$
$I-P$ is the projection onto $N(A^{\mathsf T})$, and $\mathbf{b}=P\mathbf{b}+(I-P)\mathbf{b}$ splits $\mathbf{b}$ into its parts in $C(A)$ and $C(A)^{\perp}$.

:::

::: {.proof}

1. $P^{\mathsf T}=A\big((A^{\mathsf T}A)^{-1}\big)^{\mathsf T}A^{\mathsf T}=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$, because $A^{\mathsf T}A$ is symmetric and so is its inverse (@prp-transpose-rules).

2. $P^2=A(A^{\mathsf T}A)^{-1}(A^{\mathsf T}A)(A^{\mathsf T}A)^{-1}A^{\mathsf T}=P$.

3. $(I-P)\mathbf{b}=\mathbf{e}\in C(A)^{\perp}$ and $(I-P)^2=I-2P+P^2=I-P$; if $\mathbf{b}\in C(A)^{\perp}$ then $A^{\mathsf T}\mathbf{b}=\mathbf{0}$ so $P\mathbf{b}=\mathbf{0}$ and $(I-P)\mathbf{b}=\mathbf{b}$.

:::

::: {#fig-projections-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\fill[tintA] (-1.6,-0.7) -- (2.6,-0.7) -- (3.6,0.9) -- (-0.6,0.9) -- cycle;
\draw[faint] (-1.6,-0.7) -- (2.6,-0.7) -- (3.6,0.9) -- (-0.6,0.9) -- cycle;
\node[lab, note, primary] at (3.0,-0.45) {$C(A)$};
\fill[ink] (0,0) circle[pt] node[below left, lab, tick] {$\mathbf 0$};
\draw[->, emph, ink] (0,0) -- (2,2.1) node[above, lab] {$\mathbf b$};
\draw[->, emph, primary] (0,0) -- (2,0.3) node[below right, lab] {$\mathbf p=P\mathbf b$};
\draw[->, emph, accent] (2,0.3) -- (2,2.1) node[midway, right, lab] {$\mathbf e$};
\draw[muted] (2,0.5) -- (1.82,0.47) -- (1.82,0.27);
\end{scope}
\node[lab, note, anchor=west, align=left] at (4.2,1.0) {$P\mathbf b$ is already in $C(A)$,\\so projecting again\\changes nothing: $P^2=P$};
\end{tikzpicture}
\end{center}
```

Projecting twice is the same as projecting once. The error $\mathbf e=(I-P)\mathbf b$ is the projection onto the orthogonal complement, so $P$ and $I-P$ split $\mathbf b$ into two perpendicular parts.

:::

::: {#rmk-projections-1 .remark name="Two extreme cases"}

If $\mathbf{b}\in C(A)$ then $P\mathbf{b}=\mathbf{b}$; if $\mathbf{b}\perp C(A)$ then $P\mathbf{b}=\mathbf{0}$. When $A$ is square and invertible, $C(A)=\mathbb{R}^m$ and the formula collapses to $P=AA^{-1}(A^{\mathsf T})^{-1}A^{\mathsf T}=I$; the formula cannot be split like that when $A$ is rectangular.

:::

::: {#fig-projections-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}
\fill[tintA] (-1.2,-0.5) -- (1.6,-0.5) -- (2.2,0.6) -- (-0.6,0.6) -- cycle;
\fill[ink] (0,0) circle[pt];
\draw[->, emph, primary] (0,0) -- (1.3,0.3) node[above, lab] {$\mathbf b=\mathbf p$};
\node[lab, note] at (0.5,-1.0) {$\mathbf b\in C(A)$: $P\mathbf b=\mathbf b$};
\end{scope}
\begin{scope}[shift={(5,0)}]
\fill[tintA] (-1.2,-0.5) -- (1.6,-0.5) -- (2.2,0.6) -- (-0.6,0.6) -- cycle;
\fill[primary] (0,0) circle[pt] node[below right, lab, tick] {$\mathbf p=\mathbf 0$};
\draw[->, emph, accent] (0,0) -- (0,1.5) node[above, lab] {$\mathbf b=\mathbf e$};
\draw[muted] (0.2,0.04) -- (0.2,0.24) -- (0,0.2);
\node[lab, note] at (0.5,-1.0) {$\mathbf b\perp C(A)$: $P\mathbf b=\mathbf 0$};
\end{scope}
\end{tikzpicture}
\end{center}
```

The two extreme cases of a projection. A vector already in the column space is its own projection; a vector perpendicular to it projects to $\mathbf 0$ and is all error.

:::
