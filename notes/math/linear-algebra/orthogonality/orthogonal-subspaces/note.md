---
title: "Orthogonal Vectors and Subspaces"
sources: [mit1806-14]
requires: [math/linear-algebra/vector-spaces/four-fundamental-subspaces]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 14, in our own wording; proofs written out in steps. -->

::: {#prp-pythagoras-orthogonal .proposition name="Orthogonality and Pythagoras"}

$\mathbf{x}\cdot\mathbf{y}=0$ if and only if $\lVert\mathbf{x}\rVert^2+\lVert\mathbf{y}\rVert^2=\lVert\mathbf{x}+\mathbf{y}\rVert^2$.

:::

::: {.proof}

1. $\lVert\mathbf{x}+\mathbf{y}\rVert^2=(\mathbf{x}+\mathbf{y})^{\mathsf T}(\mathbf{x}+\mathbf{y})=\lVert\mathbf{x}\rVert^2+2\,\mathbf{x}^{\mathsf T}\mathbf{y}+\lVert\mathbf{y}\rVert^2$.

2. So the two sides agree exactly when $\mathbf{x}^{\mathsf T}\mathbf{y}=0$.

:::

::: {#fig-orthogonal-subspaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph, primary, ->] (0,0) -- (3,0) node[midway, below, lab] {$\mathbf x$};
\draw[emph, secondary, ->] (3,0) -- (3,2) node[midway, right, lab] {$\mathbf y$};
\draw[emph, accent, ->] (0,0) -- (3,2) node[midway, above left, lab] {$\mathbf x+\mathbf y$};
\draw[muted] (2.75,0) -- (2.75,0.25) -- (3,0.25);
\node[lab, note, anchor=west] at (3.6,1) {$\mathbf x\cdot\mathbf y=0\iff\lVert\mathbf x+\mathbf y\rVert^2=\lVert\mathbf x\rVert^2+\lVert\mathbf y\rVert^2$};
\end{tikzpicture}
\end{center}
```

Pythagoras in any dimension: expanding $\lVert\mathbf x+\mathbf y\rVert^2=\lVert\mathbf x\rVert^2+2\,\mathbf x\cdot\mathbf y+\lVert\mathbf y\rVert^2$ shows that the cross term $2\,\mathbf x\cdot\mathbf y$ vanishes exactly for a right angle.

:::

::: {#def-orthogonal-subspaces .definition name="Orthogonal subspaces and complements"}

Subspaces $S$ and $T$ of $\mathbb{R}^n$ are *orthogonal* if $\mathbf{s}^{\mathsf T}\mathbf{t}=0$ for every $\mathbf{s}\in S$ and $\mathbf{t}\in T$. The *orthogonal complement* of $S$ is
$$S^{\perp}=\{\mathbf{v}\in\mathbb{R}^n:\mathbf{v}^{\mathsf T}\mathbf{s}=0\text{ for all }\mathbf{s}\in S\}.$$

:::

Orthogonal subspaces meet only in $\mathbf{0}$, since a common vector is orthogonal to itself. So two planes in $\mathbb{R}^3$ (the floor and a wall) are never orthogonal subspaces.

::: {#thm-fundamental-theorem-orthogonality .theorem name="Row space and nullspace are orthogonal complements"}

For an $m\times n$ matrix $A$,
$$N(A)=C(A^{\mathsf T})^{\perp}\quad\text{in }\mathbb{R}^n,\qquad N(A^{\mathsf T})=C(A)^{\perp}\quad\text{in }\mathbb{R}^m.$$
Their dimensions add up: $r+(n-r)=n$ and $r+(m-r)=m$.

:::

::: {.proof}

1. $A\mathbf{x}=\mathbf{0}$ says that $\mathbf{x}$ has dot product zero with every row of $A$, and hence with every combination of the rows. So $N(A)\subseteq C(A^{\mathsf T})^{\perp}$, and conversely a vector orthogonal to every row satisfies $A\mathbf{x}=\mathbf{0}$. Thus $N(A)=C(A^{\mathsf T})^{\perp}$.

2. Applying step 1 to $A^{\mathsf T}$ gives $N(A^{\mathsf T})=C(A)^{\perp}$.

3. The dimensions are @thm-fundamental-theorem-dimensions.

:::

::: {#cor-orthogonal-decomposition .corollary name="Every vector splits into row space plus nullspace"}

Every $\mathbf{x}\in\mathbb{R}^n$ is uniquely $\mathbf{x}=\mathbf{x}_r+\mathbf{x}_n$ with $\mathbf{x}_r\in C(A^{\mathsf T})$ and $\mathbf{x}_n\in N(A)$. Then $A\mathbf{x}=A\mathbf{x}_r$, and $A$ maps the row space one-to-one onto the column space.

:::

::: {.proof}

1. A basis of $C(A^{\mathsf T})$ ($r$ vectors) together with a basis of $N(A)$ ($n-r$ vectors) is independent: if a combination vanishes, its row-space part equals minus its nullspace part, a vector lying in both orthogonal subspaces, hence $\mathbf{0}$; each part's coefficients are then zero.

2. These $n$ independent vectors are a basis of $\mathbb{R}^n$ (@cor-basis-from-independent-set), which gives existence; uniqueness follows as in step 1.

3. $A\mathbf{x}=A\mathbf{x}_r+A\mathbf{x}_n=A\mathbf{x}_r$. If two row-space vectors have the same image, their difference is in $C(A^{\mathsf T})\cap N(A)=\{\mathbf{0}\}$. Every $\mathbf{b}=A\mathbf{x}\in C(A)$ is $A\mathbf{x}_r$.

:::

::: {#fig-orthogonal-subspaces-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1]
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-2.30,0) -- (2.40,0);
\draw[->, muted] (0,-2.30) -- (0,2.40);
\draw[emph, primary, faint] (-1.1,-2.2) -- (1.1,2.2); \draw[emph, accent, faint] (-2.2,1.1) -- (2.2,-1.1);
\node[lab, note, primary] at (1.0,2.45) {$C(A^{\mathsf T})$}; \node[lab, note, accent] at (2.55,-1.1) {$N(A)$};
\draw[->, emph, ink] (0,0) -- (1.5,0.5) node[right, lab] {$\mathbf x=(3,1)$};
\draw[->, emph, primary] (0,0) -- (0.5,1) node[left=4pt, lab] {$\mathbf x_r=(1,2)$};
\draw[->, emph, accent] (0,0) -- (1,-0.5) node[below, lab] {$\mathbf x_n=(2,-1)$};
\draw[faint, dashed] (0.5,1) -- (1.5,0.5) -- (1,-0.5);
\end{scope}
\node[lab, note, anchor=west, align=left] at (3.6,0.4) {$A=\begin{bmatrix}1&2\end{bmatrix}$:\\$A\mathbf x=A\mathbf x_r=5$,\quad $A\mathbf x_n=0$};
\end{tikzpicture}
\end{center}
```

Every $\mathbf x$ splits into a row space part and a nullspace part, here for $A=\begin{bmatrix}1&2\end{bmatrix}$ in $\mathbb R^2$ (coordinates drawn at half scale). The nullspace part contributes nothing to $A\mathbf x$.

:::

::: {#fig-orthogonal-subspaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[emph, accent] (0,-1.5) -- (0,0);
\fill[tintA] (-2.2,-0.6) -- (1.4,-0.6) -- (2.4,0.6) -- (-1.2,0.6) -- cycle;
\draw[primary] (-2.2,-0.6) -- (1.4,-0.6) -- (2.4,0.6) -- (-1.2,0.6) -- cycle;
\draw[emph, accent] (0,0) -- (0,2.4) node[lab, above] {$C(A^{\mathsf T})$};
\node[lab, primary] at (2.6,0.2) {$N(A)$};
\draw[faint, dashed] (1.3,0.3) -- (1.3,1.7) -- (0,1.4);
\draw[->, emph] (0,0) -- (1.3,0.3) node[lab, below right] {$\mathbf x_n$};
\draw[->, emph] (0,0) -- (0,1.4) node[lab, left] {$\mathbf x_r$};
\draw[->, hl] (0,0) -- (1.3,1.7) node[lab, above right] {$\mathbf x$};
\draw (0.22,0.05) -- (0.22,0.27) -- (0,0.22);
\end{tikzpicture}
\end{center}
```

Row space and nullspace as orthogonal complements in $\mathbb R^3$, as in @exm-orthogonal-complement-of-a-line: a line and the plane perpendicular to it. Every $\mathbf x$ splits as $\mathbf x_r+\mathbf x_n$ with $\mathbf x_r$ in the row space and $\mathbf x_n$ in the nullspace.

:::

::: {#thm-ata-invertible .theorem name="When A^T A is invertible"}

$N(A^{\mathsf T}A)=N(A)$. Hence $A^{\mathsf T}A$ has the same rank as $A$, and $A^{\mathsf T}A$ is invertible exactly when the columns of $A$ are independent.

:::

::: {.proof}

1. If $A\mathbf{x}=\mathbf{0}$ then $A^{\mathsf T}A\mathbf{x}=\mathbf{0}$.

2. If $A^{\mathsf T}A\mathbf{x}=\mathbf{0}$ then $0=\mathbf{x}^{\mathsf T}A^{\mathsf T}A\mathbf{x}=\lVert A\mathbf{x}\rVert^2$, so $A\mathbf{x}=\mathbf{0}$.

3. Both matrices have $n$ columns and the same nullspace, so the same rank $n-\dim N(A)$. The square matrix $A^{\mathsf T}A$ is invertible iff its nullspace is $\{\mathbf{0}\}$, iff the columns of $A$ are independent (@prp-independence-and-nullspace).

:::

::: {#exm-orthogonal-complement-of-a-line .example name="Complement of a line"}

For $A=\begin{bmatrix}1&2&2\end{bmatrix}$, the row space is the line through $(1,2,2)$ and $N(A)$ is the plane $x+2y+2z=0$. The line and the plane are orthogonal complements in $\mathbb{R}^3$: $1+2=3$.

:::
