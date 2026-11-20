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

::: {#exm-linear-and-not-linear .example name="Linear and not linear"}

Linear: projection onto a line in $\mathbb{R}^2$; rotation by $\theta$; $T(\mathbf{v})=A\mathbf{v}$ for a fixed matrix $A$; differentiation $p\mapsto p'$ on polynomials. Not linear: a shift $T(\mathbf{v})=\mathbf{v}+\mathbf{v}_0$ with $\mathbf{v}_0\neq\mathbf{0}$ (it moves $\mathbf{0}$); $T(\mathbf{v})=\lVert\mathbf{v}\rVert$ (it fails for $c=-1$).

:::

::: {#prp-linear-map-determined-by-basis .proposition name="A linear map is determined by a basis"}

If $\mathbf{v}_1,\dots,\mathbf{v}_n$ is a basis of $V$, then $T$ is determined by $T(\mathbf{v}_1),\dots,T(\mathbf{v}_n)$, and these may be chosen freely in $W$.

:::

::: {.proof}

1. Every $\mathbf{v}$ is uniquely $\sum c_i\mathbf{v}_i$ (@prp-basis-unique-coordinates), so linearity forces $T(\mathbf{v})=\sum c_iT(\mathbf{v}_i)$.

2. Conversely, defining $T(\sum c_i\mathbf{v}_i)=\sum c_i\mathbf{w}_i$ for any chosen $\mathbf{w}_i$ gives a linear map, because the coordinates of $a\mathbf{v}+b\mathbf{v}'$ are $a\mathbf{c}+b\mathbf{c}'$.

:::

::: {#def-matrix-of-linear-transformation .definition name="Matrix of a linear transformation"}

Choose a basis $\mathbf{v}_1,\dots,\mathbf{v}_n$ of $V$ (input) and $\mathbf{w}_1,\dots,\mathbf{w}_m$ of $W$ (output). The *matrix* of $T$ in these bases is the $m\times n$ matrix $A$ whose column $j$ holds the output coordinates of $T(\mathbf{v}_j)$:
$$T(\mathbf{v}_j)=a_{1j}\mathbf{w}_1+\dots+a_{mj}\mathbf{w}_m.$$

:::

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
