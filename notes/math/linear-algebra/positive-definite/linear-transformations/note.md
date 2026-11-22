---
title: "Linear Transformations and Their Matrices"
sources: [mit1806-30]
requires: [math/linear-algebra/positive-definite/singular-value-decomposition]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 30, in our own wording; proofs written out in steps. -->

::: {#def-linear-transformation .definition name="Linear transformation"}

A function $T:V\to W$ between vector spaces is a *linear transformation* if
$$T(c\mathbf{v}+d\mathbf{w})=c\,T(\mathbf{v})+d\,T(\mathbf{w})\qquad\text{for all }\mathbf{v},\mathbf{w}\in V,\ c,d\in\mathbb{R}.$$
In particular $T(\mathbf{0})=\mathbf{0}$.

:::

::: {#fig-linear-transformations-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-0.2,0) -- (2.4,0); \draw[->, muted] (0,-0.2) -- (0,1.9);
\draw[->, emph, primary] (0,0) -- (1,0.2) node[below, lab] {$\mathbf v$};
\draw[->, emph, secondary] (0,0) -- (0.3,1) node[left, lab] {$\mathbf w$};
\draw[faint, dashed] (1,0.2) -- (1.3,1.2) -- (0.3,1);
\draw[->, emph, accent] (0,0) -- (1.3,1.2) node[above, lab] {$\mathbf v+\mathbf w$};
\end{scope}
\draw[->] (2.6,0.8) -- (3.6,0.8) node[midway, above, lab, note] {$T$};
\begin{scope}[shift={(4,0)}]
\draw[->, muted] (-0.2,0) -- (2.4,0); \draw[->, muted] (0,-0.2) -- (0,1.9);
\draw[->, emph, primary] (0,0) -- (1.1,0.2) node[below, lab] {$T\mathbf v$};
\draw[->, emph, secondary] (0,0) -- (0.8,1) node[left, lab] {$T\mathbf w$};
\draw[faint, dashed] (1.1,0.2) -- (1.9,1.2) -- (0.8,1);
\draw[->, emph, accent] (0,0) -- (1.9,1.2) node[above, lab] {$T(\mathbf v+\mathbf w)$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Linearity in a picture, for the shear $T(x,y)=(x+\frac12y,\,y)$: the image of the parallelogram on $\mathbf v,\mathbf w$ is the parallelogram on $T\mathbf v,T\mathbf w$, so $T(\mathbf v+\mathbf w)=T\mathbf v+T\mathbf w$.

:::

::: {#exm-linear-and-not-linear .example name="Linear and not linear"}

Linear: projection onto a line in $\mathbb{R}^2$; rotation by $\theta$; $T(\mathbf{v})=A\mathbf{v}$ for a fixed matrix $A$; differentiation $p\mapsto p'$ on polynomials. Not linear: a shift $T(\mathbf{v})=\mathbf{v}+\mathbf{v}_0$ with $\mathbf{v}_0\neq\mathbf{0}$ (it moves $\mathbf{0}$); $T(\mathbf{v})=\lVert\mathbf{v}\rVert$ (it fails for $c=-1$).

:::

::: {#fig-linear-transformations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.3,0) -- (1.5,0); \draw[->, muted] (0,-1.3) -- (0,1.5);
\draw[faint, primary] (-1.000,-1.000) -- (-1.000,1.000); \draw[faint, primary] (-1.000,-1.000) -- (1.000,-1.000);
\draw[faint, primary] (-0.500,-1.000) -- (-0.500,1.000); \draw[faint, primary] (-1.000,-0.500) -- (1.000,-0.500);
\draw[faint, primary] (0.500,-1.000) -- (0.500,1.000); \draw[faint, primary] (-1.000,0.500) -- (1.000,0.500);
\draw[faint, primary] (1.000,-1.000) -- (1.000,1.000); \draw[faint, primary] (-1.000,1.000) -- (1.000,1.000);
\fill[accent] (0.000,0.000) circle[pt];
\node[lab, note, align=center] at (0.1,-1.75) {the grid};
\end{scope}
\begin{scope}[shift={(3.6,0)}]
\draw[->, muted] (-1.3,0) -- (1.5,0); \draw[->, muted] (0,-1.3) -- (0,1.5);
\draw[faint, primary] (-0.366,-1.366) -- (-1.366,0.366); \draw[faint, primary] (-0.366,-1.366) -- (1.366,-0.366);
\draw[faint, primary] (0.067,-1.116) -- (-0.933,0.616); \draw[faint, primary] (-0.616,-0.933) -- (1.116,0.067);
\draw[faint, primary] (0.933,-0.616) -- (-0.067,1.116); \draw[faint, primary] (-1.116,-0.067) -- (0.616,0.933);
\draw[faint, primary] (1.366,-0.366) -- (0.366,1.366); \draw[faint, primary] (-1.366,0.366) -- (0.366,1.366);
\fill[accent] (0.000,0.000) circle[pt];
\node[lab, note, align=center] at (0.1,-1.75) {rotation: linear\\($\mathbf 0$ stays, lines stay evenly spaced)};
\end{scope}
\begin{scope}[shift={(7.4,0)}]
\draw[->, muted] (-1.3,0) -- (1.5,0); \draw[->, muted] (0,-1.3) -- (0,1.5);
\draw[faint, primary] (-0.600,-0.700) -- (-0.600,1.300); \draw[faint, primary] (-0.600,-0.700) -- (1.400,-0.700);
\draw[faint, primary] (-0.100,-0.700) -- (-0.100,1.300); \draw[faint, primary] (-0.600,-0.200) -- (1.400,-0.200);
\draw[faint, primary] (0.900,-0.700) -- (0.900,1.300); \draw[faint, primary] (-0.600,0.800) -- (1.400,0.800);
\draw[faint, primary] (1.400,-0.700) -- (1.400,1.300); \draw[faint, primary] (-0.600,1.300) -- (1.400,1.300);
\fill[accent] (0.400,0.300) circle[pt];
\node[lab, note, align=center] at (0.1,-1.75) {shift by $\mathbf v_0$: not linear\\($\mathbf 0$ moves)};
\end{scope}
\end{tikzpicture}
\end{center}
```

A linear transformation keeps the origin fixed and takes evenly spaced parallel lines to evenly spaced parallel lines (or collapses them). A shift moves the origin, so $T(\mathbf 0)\ne\mathbf 0$ and it is not linear.

:::

<!-- Merged 2026-11-20 (owner): the block prp-linear-map-determined-by-basis was removed in favour of thm-linear-map-from-basis (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**A linear map is determined by a basis.** If $\mathbf{v}_1,\dots,\mathbf{v}_n$ is a basis of $V$, then $T$ is determined by $T(\mathbf{v}_1),\dots,T(\mathbf{v}_n)$, and these may be chosen freely in $W$: linearity forces $T(\sum c_i\mathbf v_i)=\sum c_iT(\mathbf v_i)$. See @thm-linear-map-from-basis.

<!-- Merged 2026-11-20 (owner): the block def-matrix-of-linear-transformation was removed in favour of def-matrix-of-linear-map (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**The matrix of $T$.** Choose a basis $\mathbf{v}_1,\dots,\mathbf{v}_n$ of $V$ (input) and $\mathbf{w}_1,\dots,\mathbf{w}_m$ of $W$ (output). The *matrix* of $T$ in these bases is the $m\times n$ matrix $A$ whose column $j$ holds the output coordinates of $T(\mathbf{v}_j)$, that is, $T(\mathbf{v}_j)=a_{1j}\mathbf{w}_1+\dots+a_{mj}\mathbf{w}_m$ (@def-matrix-of-linear-map).

::: {#thm-matrix-represents-transformation .theorem name="Coordinates transform by the matrix"}

If $\mathbf{v}$ has input coordinates $\mathbf{c}$, then $T(\mathbf{v})$ has output coordinates $A\mathbf{c}$. If $S:W\to Z$ has matrix $B$ (in the same basis of $W$), then $S\circ T$ has matrix $BA$.

:::

::: {.proof}

1. $T(\sum_jc_j\mathbf{v}_j)=\sum_jc_j\sum_ia_{ij}\mathbf{w}_i=\sum_i(A\mathbf{c})_i\mathbf{w}_i$.

2. Applying step 1 twice, the coordinates of $S(T(\mathbf{v}))$ are $B(A\mathbf{c})=(BA)\mathbf{c}$ by associativity (@prp-matrix-product-laws). This is why matrices are multiplied the way they are.

:::

::: {#exm-matrix-of-projection .example name="A good basis gives a diagonal matrix"}

Let $T$ project $\mathbb{R}^2$ onto the line through $\mathbf{q}_1=\frac1{\sqrt2}(1,1)$. In the standard basis its matrix is $\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}$ (@thm-projection-onto-line). In the basis $\mathbf{q}_1,\mathbf{q}_2=\frac1{\sqrt2}(-1,1)$ of eigenvectors, $T(\mathbf{q}_1)=\mathbf{q}_1$ and $T(\mathbf{q}_2)=\mathbf{0}$, so the matrix is $\begin{bmatrix}1&0\\0&0\end{bmatrix}$.

:::

::: {#fig-linear-transformations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.3]
\draw[->] (-1.4,0) -- (2.4,0); \draw[->] (0,-0.6) -- (0,2.2);
\draw[emph, primary] (-0.6,-0.6) -- (2.1,2.1);
\draw[faint, dashed] (0.4,1.8) -- (1.1,1.1);
\draw[->, emph] (0,0) -- (0.4,1.8) node[lab, above] {$\mathbf v$};
\draw[->, hl] (0,0) -- (1.1,1.1) node[lab, right] {$T(\mathbf v)$};
\draw[->, emph, accent] (0,0) -- (-0.707,0.707) node[lab, above left] {$\mathbf q_2\mapsto\mathbf 0$};
\draw[->, emph, primary] (0,0) -- (0.707,0.707);
\node[lab, primary, below right] at (0.6,0.6) {$\mathbf q_1\mapsto\mathbf q_1$};
\end{tikzpicture}
\end{center}
```

Projection onto the line through $\mathbf q_1$ (@exm-matrix-of-projection). In the basis $\mathbf q_1,\mathbf q_2$ the map keeps the first coordinate and sends the second to zero, so its matrix is $\begin{bmatrix}1&0\\0&0\end{bmatrix}$.

:::

::: {#exm-matrix-of-derivative .example name="Matrix of the derivative"}

On polynomials of degree $\le2$ with basis $1,x,x^2$ (input) and $1,x$ (output), $\frac{d}{dx}$ sends $1\mapsto0$, $x\mapsto1$, $x^2\mapsto2x$. Its matrix is
$$A=\begin{bmatrix}0&1&0\\0&0&2\end{bmatrix},$$
and $A(c_0,c_1,c_2)=(c_1,2c_2)$ are the coefficients of $c_1+2c_2x$. The nullspace (constants) and column space (all of the output space) match the calculus.

:::

::: {#fig-linear-transformations-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.600,0.500) rectangle (1.200,1.100);
\node[lab] at (0.900,0.800) {$0$};
\draw[hl cell] (1.200,0.500) rectangle (1.800,1.100);
\node[lab] at (1.500,0.800) {$1$};
\draw[cell frame] (1.800,0.500) rectangle (2.400,1.100);
\node[lab] at (2.100,0.800) {$0$};
\draw[cell frame] (0.600,-0.100) rectangle (1.200,0.500);
\node[lab] at (0.900,0.200) {$0$};
\draw[cell frame] (1.200,-0.100) rectangle (1.800,0.500);
\node[lab] at (1.500,0.200) {$0$};
\draw[hl cell] (1.800,-0.100) rectangle (2.400,0.500);
\node[lab] at (2.100,0.200) {$2$};
\node[lab, tick] at (0.9,1.3) {$1$}; \node[lab, tick] at (1.5,1.3) {$x$}; \node[lab, tick] at (2.1,1.3) {$x^2$};
\node[lab, tick] at (0.35,0.8) {$1$}; \node[lab, tick] at (0.35,0.2) {$x$};
\node[lab, note, anchor=west, align=left] at (2.8,0.5) {column $j$: the derivative of input basis $j$\\$1\mapsto0$, $x\mapsto1$, $x^2\mapsto2x$};
\end{tikzpicture}
\end{center}
```

The matrix of $\frac{d}{dx}$ from polynomials of degree $\le2$ (columns, basis $1,x,x^2$) to degree $\le1$ (rows, basis $1,x$). The first column is zero because constants differentiate to $0$.

:::
