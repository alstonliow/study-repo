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

::: {#def-dot-product .definition name="Dot product and length"}

The *dot product* of $\mathbf{v},\mathbf{w}\in\mathbb{R}^n$ is
$$\mathbf{v}\cdot\mathbf{w}=v_1w_1+v_2w_2+\dots+v_nw_n=\mathbf{v}^{\mathsf T}\mathbf{w}.$$
The *length* of $\mathbf{v}$ is $\lVert\mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot\mathbf{v}}$. A *unit vector* has length $1$; $\mathbf{v}/\lVert\mathbf{v}\rVert$ is the unit vector in the direction of $\mathbf{v}\neq\mathbf{0}$. Two vectors are *perpendicular* (orthogonal) when $\mathbf{v}\cdot\mathbf{w}=0$.

:::

The dot product is symmetric, $\mathbf{v}\cdot\mathbf{w}=\mathbf{w}\cdot\mathbf{v}$, and linear in each argument: $(c\mathbf{u}+d\mathbf{v})\cdot\mathbf{w}=c\,\mathbf{u}\cdot\mathbf{w}+d\,\mathbf{v}\cdot\mathbf{w}$.

::: {#thm-cauchy-schwarz .theorem name="Cauchy–Schwarz and triangle inequalities"}

For all $\mathbf{v},\mathbf{w}\in\mathbb{R}^n$,
$$\lvert\mathbf{v}\cdot\mathbf{w}\rvert\le\lVert\mathbf{v}\rVert\,\lVert\mathbf{w}\rVert
\qquad\text{and}\qquad
\lVert\mathbf{v}+\mathbf{w}\rVert\le\lVert\mathbf{v}\rVert+\lVert\mathbf{w}\rVert.$$

:::

::: {.proof}

1. If $\mathbf{w}=\mathbf{0}$ both sides of the first inequality are $0$. Otherwise, for every real $t$,
   $$0\le\lVert\mathbf{v}-t\mathbf{w}\rVert^2=\lVert\mathbf{v}\rVert^2-2t\,\mathbf{v}\cdot\mathbf{w}+t^2\lVert\mathbf{w}\rVert^2.$$

2. Choose $t=\mathbf{v}\cdot\mathbf{w}/\lVert\mathbf{w}\rVert^2$. The right side becomes $\lVert\mathbf{v}\rVert^2-(\mathbf{v}\cdot\mathbf{w})^2/\lVert\mathbf{w}\rVert^2\ge0$, which rearranges to $(\mathbf{v}\cdot\mathbf{w})^2\le\lVert\mathbf{v}\rVert^2\lVert\mathbf{w}\rVert^2$.

3. For the triangle inequality, expand and apply step 2:
   $$\lVert\mathbf{v}+\mathbf{w}\rVert^2=\lVert\mathbf{v}\rVert^2+2\,\mathbf{v}\cdot\mathbf{w}+\lVert\mathbf{w}\rVert^2\le\lVert\mathbf{v}\rVert^2+2\lVert\mathbf{v}\rVert\lVert\mathbf{w}\rVert+\lVert\mathbf{w}\rVert^2=(\lVert\mathbf{v}\rVert+\lVert\mathbf{w}\rVert)^2.$$

:::

::: {#def-angle-between-vectors .definition name="Angle between vectors"}

For nonzero $\mathbf{v},\mathbf{w}$ the *angle* $\theta\in[0,\pi]$ between them is defined by
$$\cos\theta=\frac{\mathbf{v}\cdot\mathbf{w}}{\lVert\mathbf{v}\rVert\,\lVert\mathbf{w}\rVert}.$$
By @thm-cauchy-schwarz the right side lies in $[-1,1]$, so $\theta$ exists. In $\mathbb{R}^2$ it agrees with the usual angle, by the formula $\cos(\beta-\alpha)=\cos\beta\cos\alpha+\sin\beta\sin\alpha$.

:::

::: {#exm-angle-between-vectors .example name="An angle"}

For $\mathbf{v}=(1,1,0)$ and $\mathbf{w}=(1,0,1)$: $\mathbf{v}\cdot\mathbf{w}=1$ and $\lVert\mathbf{v}\rVert=\lVert\mathbf{w}\rVert=\sqrt2$, so $\cos\theta=\frac12$ and $\theta=\frac\pi3$. The sign of $\mathbf{v}\cdot\mathbf{w}$ tells the type of angle: positive for acute, zero for right, negative for obtuse.

:::
