---
title: "Vectors, Linear Combinations and Dot Products"
sources: [mit1806-1]
requires: []
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 1, and the topics of 18.06 S10 Problem Set 1, in our own wording; proofs written out in steps. -->

A vector in $\mathbb{R}^n$ is a column of $n$ real numbers. Two operations make everything else in linear algebra possible: adding vectors and multiplying them by numbers.

::: {#def-linear-combination .definition name="Linear combination"}

For vectors $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^n$ and scalars $c_1,\dots,c_k\in\mathbb{R}$, the vector
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k$$
is a *linear combination* of $\mathbf{v}_1,\dots,\mathbf{v}_k$. Addition and scalar multiplication act component by component.

:::

::: {#fig-vectors-and-dot-products-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[->] (-0.4,0) -- (4.3,0); \draw[->] (0,-0.4) -- (0,2.9);
\draw[faint, dashed] (3,0.9) -- (3.6,2.5) -- (0.6,1.6);
\draw[->, emph, primary] (0,0) -- (2,0.6) node[lab, below right] {$\mathbf v$};
\draw[->, emph, primary, dashed] (2,0.6) -- (3,0.9);
\node[lab, below] at (2.9,0.85) {$1.5\,\mathbf v$};
\draw[->, emph, accent] (0,0) -- (0.6,1.6) node[lab, left] {$\mathbf w$};
\draw[->, hl] (0,0) -- (3.6,2.5) node[lab, above right] {$1.5\,\mathbf v+\mathbf w$};
\end{tikzpicture}
\end{center}
```

A linear combination $c\mathbf v+d\mathbf w$ with $c=1.5$, $d=1$: scale each vector, then add by the parallelogram rule. Letting $c$ and $d$ range over all real numbers fills the whole plane.

:::

::: {#exm-linear-combinations-of-two-vectors .example name="All combinations of two vectors"}

The combinations $c\,(1,0,1)+d\,(0,1,1)=(c,d,c+d)$ fill a plane through $\mathbf{0}$ in $\mathbb{R}^3$: the plane $z=x+y$. The combinations of a single nonzero vector fill a line; the combinations of three vectors not in one plane fill all of $\mathbb{R}^3$.

:::

::: {#fig-vectors-and-dot-products-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x={(-0.5cm,-0.4cm)}, y={(1cm,0)}, z={(0,1cm)}, scale=1.1]
\draw[->, muted] (0,0,0) -- (2.4,0,0) node[below left, lab, tick] {$x$}; \draw[->, muted] (0,0,0) -- (0,2.4,0) node[right, lab, tick] {$y$}; \draw[->, muted] (0,0,0) -- (0,0,2.6) node[above, lab, tick] {$z$};
\fill[tintA] (-1,-1,-2) -- (1.6,-1,0.6) -- (1.6,1.6,3.2) -- (-1,1.6,0.6) -- cycle;
\draw[->, emph, primary] (0,0,0) -- (1,0,1) node[left, lab] {$\mathbf v=(1,0,1)$};
\draw[->, emph, secondary] (0,0,0) -- (0,1,1) node[right, lab] {$\mathbf w=(0,1,1)$};
\draw[faint, dashed] (1,0,1) -- (1,1,2) -- (0,1,1);
\draw[->, emph, accent] (0,0,0) -- (1,1,2) node[above, lab] {$\mathbf v+\mathbf w$};
\node[lab, note, primary] at (1.5,1.5,3.2) {$z=x+y$};
\end{scope}
\end{tikzpicture}
\end{center}
```

@exm-linear-combinations-of-two-vectors: all combinations $c\mathbf v+d\mathbf w$ of $\mathbf v=(1,0,1)$ and $\mathbf w=(0,1,1)$ fill the shaded plane $z=x+y$ through $\mathbf 0$. The parallelogram shows $c=d=1$.

:::

::: {#def-dot-product .definition name="Dot product and length"}

The *dot product* of $\mathbf{v},\mathbf{w}\in\mathbb{R}^n$ is
$$\mathbf{v}\cdot\mathbf{w}=v_1w_1+v_2w_2+\dots+v_nw_n=\mathbf{v}^{\mathsf T}\mathbf{w}.$$
The *length* of $\mathbf{v}$ is $\lVert\mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot\mathbf{v}}$. A *unit vector* has length $1$; $\mathbf{v}/\lVert\mathbf{v}\rVert$ is the unit vector in the direction of $\mathbf{v}\neq\mathbf{0}$. Two vectors are *perpendicular* (orthogonal) when $\mathbf{v}\cdot\mathbf{w}=0$.

:::

::: {#fig-vectors-and-dot-products-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y={(0,0.75cm)}]
\draw[->, muted] (0,0) -- (4.3,0) node[right, lab, tick] {$x$}; \draw[->, muted] (0,0) -- (0,3.3) node[above, lab, tick] {$y$};
\draw[->, emph, primary] (0,0) -- (3,4*0.75) node[midway, above left, lab] {$\lVert\mathbf v\rVert=5$};
\draw[faint, dashed] (3,0) -- (3,3);
\node[lab, tick, below] at (1.5,0) {$3$}; \node[lab, tick, right] at (3,1.5) {$4$};
\draw[->, bold, accent] (0,0) -- (0.6,0.6) node[right, lab] {$\mathbf u=\mathbf v/5$};
\draw[faint] (0.75,0) arc[start angle=0, end angle=45, radius=0.75];
\end{tikzpicture}
\end{center}
```

Length from the dot product: for $\mathbf v=(3,4)$, $\mathbf v\cdot\mathbf v=9+16=25$, so $\lVert\mathbf v\rVert=5$ by Pythagoras. Dividing by the length gives the unit vector $\mathbf u=(0.6,0.8)$ in the same direction.

:::

The dot product is symmetric, $\mathbf{v}\cdot\mathbf{w}=\mathbf{w}\cdot\mathbf{v}$, and linear in each argument: $(c\mathbf{u}+d\mathbf{v})\cdot\mathbf{w}=c\,\mathbf{u}\cdot\mathbf{w}+d\,\mathbf{v}\cdot\mathbf{w}$.

<!-- Merged 2026-11-20 (owner): the block thm-cauchy-schwarz was removed in favour of thm-cauchy-schwarz-inner-product (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Cauchy–Schwarz and triangle inequalities.** For all $\mathbf{v},\mathbf{w}\in\mathbb{R}^n$,
$$\lvert\mathbf{v}\cdot\mathbf{w}\rvert\le\lVert\mathbf{v}\rVert\,\lVert\mathbf{w}\rVert\qquad\text{and}\qquad\lVert\mathbf{v}+\mathbf{w}\rVert\le\lVert\mathbf{v}\rVert+\lVert\mathbf{w}\rVert.$$
The first follows from $0\le\lVert\mathbf v-t\mathbf w\rVert^2$ with the best $t=\mathbf v\cdot\mathbf w/\lVert\mathbf w\rVert^2$, the second by expanding $\lVert\mathbf v+\mathbf w\rVert^2$. Proofs for every inner product: @thm-cauchy-schwarz-inner-product and @cor-triangle-inequality-inner-product.

::: {#def-angle-between-vectors .definition name="Angle between vectors"}

For nonzero $\mathbf{v},\mathbf{w}$ the *angle* $\theta\in[0,\pi]$ between them is defined by
$$\cos\theta=\frac{\mathbf{v}\cdot\mathbf{w}}{\lVert\mathbf{v}\rVert\,\lVert\mathbf{w}\rVert}.$$
By @thm-cauchy-schwarz-inner-product the right side lies in $[-1,1]$, so $\theta$ exists. In $\mathbb{R}^2$ it agrees with the usual angle, by the formula $\cos(\beta-\alpha)=\cos\beta\cos\alpha+\sin\beta\sin\alpha$.

:::

::: {#fig-vectors-and-dot-products-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, emph, primary] (0,0) -- (1.6,0) node[below, lab] {$\mathbf v$};
\draw[->, emph, secondary] (0,0) -- (1.0,1.0) node[above, lab] {$\mathbf w$};
\node[lab, note] at (0.6,-0.6) {$\mathbf v\cdot\mathbf w>0$: acute};
\end{scope}
\begin{scope}[shift={(3.0,0)}]
\draw[->, emph, primary] (0,0) -- (1.6,0) node[below, lab] {$\mathbf v$};
\draw[->, emph, ink] (0,0) -- (0,1.4) node[above, lab] {$\mathbf w$};
\node[lab, note] at (0.6,-0.6) {$\mathbf v\cdot\mathbf w=0$: right};
\end{scope}
\draw[muted] (3.2,0) -- (3.2,0.2) -- (3.0,0.2);
\begin{scope}[shift={(6.0,0)}]
\draw[->, emph, primary] (0,0) -- (1.6,0) node[below, lab] {$\mathbf v$};
\draw[->, emph, accent] (0,0) -- (-1.0,1.0) node[above, lab] {$\mathbf w$};
\node[lab, note] at (0.6,-0.6) {$\mathbf v\cdot\mathbf w<0$: obtuse};
\end{scope}
\end{tikzpicture}
\end{center}
```

The sign of the dot product gives the type of angle, since $\mathbf v\cdot\mathbf w=\lVert\mathbf v\rVert\lVert\mathbf w\rVert\cos\theta$ and the lengths are positive.

:::

::: {#exm-angle-between-vectors .example name="An angle"}

For $\mathbf{v}=(1,1,0)$ and $\mathbf{w}=(1,0,1)$: $\mathbf{v}\cdot\mathbf{w}=1$ and $\lVert\mathbf{v}\rVert=\lVert\mathbf{w}\rVert=\sqrt2$, so $\cos\theta=\frac12$ and $\theta=\frac\pi3$. The sign of $\mathbf{v}\cdot\mathbf{w}$ tells the type of angle: positive for acute, zero for right, negative for obtuse.

:::
