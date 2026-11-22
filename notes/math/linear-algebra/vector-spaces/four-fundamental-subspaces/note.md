---
title: "The Four Fundamental Subspaces"
sources: [mit1806-10]
requires: [math/linear-algebra/vector-spaces/independence-basis-dimension]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 10, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-four-fundamental-subspaces .definition name="The four fundamental subspaces"}

An $m\times n$ matrix $A$ has four subspaces:

1. the *column space* $C(A)\subseteq\mathbb{R}^m$;
2. the *nullspace* $N(A)\subseteq\mathbb{R}^n$;
3. the *row space* $C(A^{\mathsf T})\subseteq\mathbb{R}^n$, all combinations of the rows;
4. the *left nullspace* $N(A^{\mathsf T})\subseteq\mathbb{R}^m$, all $\mathbf{y}$ with $A^{\mathsf T}\mathbf{y}=\mathbf{0}$, equivalently $\mathbf{y}^{\mathsf T}A=\mathbf{0}^{\mathsf T}$.

:::

::: {#fig-four-fundamental-subspaces-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.40,0) -- (1.5,0);
\draw[->, muted] (0,-1.40) -- (0,1.5);
\draw[emph, primary] (-0.6,-1.2) -- (0.6,1.2) node[above, lab, note] {$C(A^{\mathsf T})$};
\draw[emph, accent] (-1.2,0.6) -- (1.2,-0.6) node[below, lab, note] {$N(A)$};
\draw[muted] (0.18,0.36) -- (0.36,0.27) -- (0.18,-0.09);
\node[lab, note] at (0,-1.75) {$\mathbb R^2$ (inputs)};
\end{scope}
\draw[->, emph] (1.7,0.3) -- (2.9,0.3) node[midway, above, lab] {$A$};
\begin{scope}[shift={(4.6,0)}]
\draw[->, muted] (-1.40,0) -- (1.5,0);
\draw[->, muted] (0,-1.40) -- (0,1.5);
\draw[emph, primary] (-0.6,-1.2) -- (0.6,1.2) node[above, lab, note] {$C(A)$};
\draw[emph, accent] (-1.2,0.6) -- (1.2,-0.6) node[below, lab, note] {$N(A^{\mathsf T})$};
\node[lab, note] at (0,-1.75) {$\mathbb R^2$ (outputs)};
\end{scope}
\end{tikzpicture}
\end{center}
```

All four subspaces of the rank one matrix $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$ are lines. Every row and every column is a multiple of $(1,2)$, so the row space and the column space are the line through $(1,2)$; $N(A)$ and $N(A^{\mathsf T})$ are the perpendicular line through $(2,-1)$.

:::

::: {#thm-fundamental-theorem-dimensions .theorem name="Dimensions of the four subspaces"}

If $A$ is $m\times n$ with rank $r$, then
$$\dim C(A)=\dim C(A^{\mathsf T})=r,\qquad \dim N(A)=n-r,\qquad \dim N(A^{\mathsf T})=m-r.$$
In particular row rank equals column rank.

:::

::: {.proof}

1. **Row space.** Elimination $EA=R$ ($E$ invertible) replaces rows by combinations of rows and can be undone, so $C(A^{\mathsf T})=C(R^{\mathsf T})$. The $r$ nonzero rows of $R$ are independent (each has a $1$ in a pivot column where the others have $0$) and span it. So $\dim C(A^{\mathsf T})=r$.

2. **Column space.** The pivot columns of $A$ are a basis of $C(A)$ (@exm-basis-of-column-space): $A\mathbf{x}=\mathbf{0}\iff R\mathbf{x}=\mathbf{0}$, so the same columns are independent in $A$ as in $R$, and every other column is a combination of the pivot columns in both. So $\dim C(A)=r$.

3. **Nullspace.** The $n-r$ special solutions are a basis of $N(A)$ by @thm-special-solutions.

4. **Left nullspace.** Apply step 3 to the $n\times m$ matrix $A^{\mathsf T}$, whose rank is $\dim C(A^{\mathsf T})=r$ by step 1: $\dim N(A^{\mathsf T})=m-r$.

:::

::: {#fig-four-fundamental-subspaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0,0.0) rectangle (0.9,-0.5);
\draw[cell, fill=primaryLight] (0,-0.5) rectangle (0.9,-1.0);
\draw[cell, fill=accentLight] (0,-1.0) rectangle (0.9,-1.5);
\draw[cell, fill=accentLight] (0,-1.5) rectangle (0.9,-2.0);
\node[lab, note, anchor=west] at (1.0,-0.5) {row space $C(A^{\mathsf T})$: $r=2$};
\node[lab, note, anchor=west] at (1.0,-1.5) {nullspace $N(A)$: $n-r=2$};
\node[lab] at (0.45,0.3) {$\mathbb R^4$};
\draw[cell, fill=primaryLight] (6.9,0.0) rectangle (7.80,-0.5);
\draw[cell, fill=primaryLight] (6.9,-0.5) rectangle (7.80,-1.0);
\draw[cell, fill=accentLight] (6.9,-1.0) rectangle (7.80,-1.5);
\node[lab, note, anchor=west] at (7.9,-0.5) {column space $C(A)$: $r=2$};
\node[lab, note, anchor=west] at (7.9,-1.25) {left nullspace $N(A^{\mathsf T})$: $m-r=1$};
\node[lab] at (7.35,0.3) {$\mathbb R^3$};
\draw[->, emph] (5.1,-0.5) -- (6.7,-0.5) node[midway, above, lab] {$A$};
\end{tikzpicture}
\end{center}
```

Dimension count for the $3\times4$ matrix of @exm-four-subspaces, one cell per basis vector. In $\mathbb R^n=\mathbb R^4$ the row space and the nullspace have dimensions $r$ and $n-r$; in $\mathbb R^m=\mathbb R^3$ the column space and the left nullspace have $r$ and $m-r$.

:::

::: {#prp-left-nullspace-from-elimination .proposition name="A basis for the left nullspace"}

If $EA=R$ with $E$ invertible and the last $m-r$ rows of $R$ zero, then the last $m-r$ rows of $E$ are a basis of $N(A^{\mathsf T})$ (as row vectors $\mathbf{y}^{\mathsf T}$ with $\mathbf{y}^{\mathsf T}A=\mathbf{0}^{\mathsf T}$).

:::

::: {.proof}

1. Row $i$ of $EA$ is (row $i$ of $E$)$\,A$. For $i>r$ this is a zero row of $R$.

2. These $m-r$ rows of the invertible $E$ are independent, and $\dim N(A^{\mathsf T})=m-r$, so they form a basis (@cor-basis-from-independent-set).

:::

::: {#fig-four-fundamental-subspaces-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$2$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[cell frame] (1.650,1.100) rectangle (2.200,1.650);
\node[lab] at (1.925,1.375) {$1$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$4$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$1$};
\draw[cell frame] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$4$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$3$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$6$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\draw[cell frame] (1.650,-0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$5$};
\draw[cell frame] (2.300,1.100) rectangle (2.850,1.650);
\node[lab] at (2.575,1.375) {$1$};
\draw[cell frame] (2.850,1.100) rectangle (3.400,1.650);
\node[lab] at (3.125,1.375) {$0$};
\draw[cell frame] (3.400,1.100) rectangle (3.950,1.650);
\node[lab] at (3.675,1.375) {$0$};
\draw[cell frame] (2.300,0.550) rectangle (2.850,1.100);
\node[lab] at (2.575,0.825) {$0$};
\draw[cell frame] (2.850,0.550) rectangle (3.400,1.100);
\node[lab] at (3.125,0.825) {$1$};
\draw[cell frame] (3.400,0.550) rectangle (3.950,1.100);
\node[lab] at (3.675,0.825) {$0$};
\draw[cell frame] (2.300,-0.000) rectangle (2.850,0.550);
\node[lab] at (2.575,0.275) {$0$};
\draw[cell frame] (2.850,-0.000) rectangle (3.400,0.550);
\node[lab] at (3.125,0.275) {$0$};
\draw[cell frame] (3.400,-0.000) rectangle (3.950,0.550);
\node[lab] at (3.675,0.275) {$1$};
\draw[bold, ink] (2.25,1.7) -- (2.25,-0.05);
\node[lab, note] at (1.75,-0.35) {$[A\ \ I]$};
\draw[->] (4.1,0.825) -- (5.6,0.825) node[midway, above, lab, tick] {elimination};
\draw[cell frame] (5.800,1.100) rectangle (6.350,1.650);
\node[lab] at (6.075,1.375) {$1$};
\draw[cell frame] (6.350,1.100) rectangle (6.900,1.650);
\node[lab] at (6.625,1.375) {$2$};
\draw[cell frame] (6.900,1.100) rectangle (7.450,1.650);
\node[lab] at (7.175,1.375) {$0$};
\draw[cell frame] (7.450,1.100) rectangle (8.000,1.650);
\node[lab] at (7.725,1.375) {$1$};
\draw[cell frame] (5.800,0.550) rectangle (6.350,1.100);
\node[lab] at (6.075,0.825) {$0$};
\draw[cell frame] (6.350,0.550) rectangle (6.900,1.100);
\node[lab] at (6.625,0.825) {$0$};
\draw[cell frame] (6.900,0.550) rectangle (7.450,1.100);
\node[lab] at (7.175,0.825) {$1$};
\draw[cell frame] (7.450,0.550) rectangle (8.000,1.100);
\node[lab] at (7.725,0.825) {$2$};
\draw[hl cell] (5.800,-0.000) rectangle (6.350,0.550);
\node[lab] at (6.075,0.275) {$0$};
\draw[hl cell] (6.350,-0.000) rectangle (6.900,0.550);
\node[lab] at (6.625,0.275) {$0$};
\draw[hl cell] (6.900,-0.000) rectangle (7.450,0.550);
\node[lab] at (7.175,0.275) {$0$};
\draw[hl cell] (7.450,-0.000) rectangle (8.000,0.550);
\node[lab] at (7.725,0.275) {$0$};
\draw[cell frame] (8.100,1.100) rectangle (8.650,1.650);
\node[lab] at (8.375,1.375) {$1$};
\draw[cell frame] (8.650,1.100) rectangle (9.200,1.650);
\node[lab] at (8.925,1.375) {$0$};
\draw[cell frame] (9.200,1.100) rectangle (9.750,1.650);
\node[lab] at (9.475,1.375) {$0$};
\draw[cell frame] (8.100,0.550) rectangle (8.650,1.100);
\node[lab] at (8.375,0.825) {$-2$};
\draw[cell frame] (8.650,0.550) rectangle (9.200,1.100);
\node[lab] at (8.925,0.825) {$1$};
\draw[cell frame] (9.200,0.550) rectangle (9.750,1.100);
\node[lab] at (9.475,0.825) {$0$};
\draw[hl cell] (8.100,-0.000) rectangle (8.650,0.550);
\node[lab] at (8.375,0.275) {$-1$};
\draw[hl cell] (8.650,-0.000) rectangle (9.200,0.550);
\node[lab] at (8.925,0.275) {$-1$};
\draw[hl cell] (9.200,-0.000) rectangle (9.750,0.550);
\node[lab] at (9.475,0.275) {$1$};
\draw[bold, ink] (8.05,1.7) -- (8.05,-0.05);
\node[lab, note] at (7.55,-0.35) {$[R\ \ E]$, $EA=R$};
\end{tikzpicture}
\end{center}
```

Elimination on $[A\ \ I]$ for the matrix of @exm-four-subspaces records the row operations in $E$. A zero row of $R=EA$ (highlighted) comes from a row of $E$ whose combination of the rows of $A$ is zero, so that row, $(-1,-1,1)$, lies in $N(A^{\mathsf T})$.

:::

::: {#exm-four-subspaces .example name="The four subspaces of a 3 by 4 matrix"}

For $A=\begin{bmatrix}1&2&0&1\\2&4&1&4\\3&6&1&5\end{bmatrix}$ (rank $2$, @exm-nullspace-three-by-four):

| subspace | dimension | basis |
|---|---|---|
| $C(A)\subseteq\mathbb{R}^3$ | $2$ | $(1,2,3)$, $(0,1,1)$ |
| $C(A^{\mathsf T})\subseteq\mathbb{R}^4$ | $2$ | $(1,2,0,1)$, $(0,0,1,2)$ |
| $N(A)\subseteq\mathbb{R}^4$ | $2$ | $(-2,1,0,0)$, $(-1,0,-2,1)$ |
| $N(A^{\mathsf T})\subseteq\mathbb{R}^3$ | $1$ | $(-1,-1,1)$ |

The left nullspace vector records the dependence among the rows: $-(\text{row }1)-(\text{row }2)+(\text{row }3)=\mathbf{0}$.

:::

::: {#fig-four-fundamental-subspaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0.9) rectangle (3,2.6);
\draw[regionB] (0,-0.9) rectangle (3,0.7);
\draw[regionA] (5.2,0.9) rectangle (8.2,2.6);
\draw[regionB] (5.2,-0.9) rectangle (8.2,0.7);
\node[lab, align=center] at (1.5,1.75) {row space $C(A^{\mathsf T})$\\ $\dim r$};
\node[lab, align=center] at (1.5,-0.1) {nullspace $N(A)$\\ $\dim n-r$};
\node[lab, align=center] at (6.7,1.75) {column space $C(A)$\\ $\dim r$};
\node[lab, align=center] at (6.7,-0.1) {left nullspace $N(A^{\mathsf T})$\\ $\dim m-r$};
\node[lab] at (1.5,3.0) {$\mathbb{R}^n$};
\node[lab] at (6.7,3.0) {$\mathbb{R}^m$};
\draw[->, emph] (3.1,1.9) -- node[lab, above] {$A\mathbf{x}_r=\mathbf b$} (5.1,1.9);
\draw[->, emph] (3.1,-0.1) -- node[lab, above] {$A\mathbf{x}_n=\mathbf 0$} (5.1,1.3);
\end{tikzpicture}
\end{center}
```

The four subspaces of an $m\times n$ matrix of rank $r$. $A$ maps the row space onto the column space and the nullspace to $\mathbf 0$; each pair is orthogonal.

:::

::: {#rmk-four-fundamental-subspaces-1 .remark name="The big picture"}

$\mathbb{R}^n$ holds the row space ($r$) and the nullspace ($n-r$); $\mathbb{R}^m$ holds the column space ($r$) and the left nullspace ($m-r$). The note @sec-math-linear-algebra-orthogonality-orthogonal-subspaces shows that each pair is orthogonal and fills its space.

:::
