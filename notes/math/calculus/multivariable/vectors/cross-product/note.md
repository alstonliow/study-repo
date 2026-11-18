---
title: "Determinants, the Cross Product and the Triple Product"
sources: [mit1802-2, mit1802-3, mit1802n-D]
requires: [math/linear-algebra/determinants/cramers-rule-and-volume]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 2-3 and Supplementary Notes D, in our own wording. Numbers checked in Python. -->

Vectors in the plane and in space are written $\mathbf{A}=\langle a_1,a_2,a_3\rangle=a_1\mathbf{i}+a_2\mathbf{j}+a_3\mathbf{k}$, with length $\lvert\mathbf{A}\rvert$ and direction $\operatorname{dir}\mathbf{A}=\mathbf{A}/\lvert\mathbf{A}\rvert$ (@sec-math-linear-algebra-systems-vectors-and-dot-products gives the dot product, lengths and angles). The dot product $\mathbf{A}\cdot\hat{\mathbf{u}}=\lvert\mathbf{A}\rvert\cos\theta$ with a unit vector $\hat{\mathbf{u}}$ is the component of $\mathbf{A}$ along $\hat{\mathbf{u}}$.

::: {#def-determinant-two-three .definition name="Determinants of order 2 and 3"}

$$\begin{vmatrix}a_1&a_2\\b_1&b_2\end{vmatrix}=a_1b_2-a_2b_1,\qquad
\begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}
=a_1\begin{vmatrix}b_2&b_3\\c_2&c_3\end{vmatrix}-a_2\begin{vmatrix}b_1&b_3\\c_1&c_3\end{vmatrix}+a_3\begin{vmatrix}b_1&b_2\\c_1&c_2\end{vmatrix}.$$
We write $\det(\mathbf{A},\mathbf{B})$ and $\det(\mathbf{A},\mathbf{B},\mathbf{C})$ for the determinants whose rows are the given vectors.

:::

The $3\times3$ formula is the cofactor expansion along the first row (@thm-cofactor-expansion).

::: {#thm-plane-determinant-area .theorem name="Area of a parallelogram in the plane"}

For plane vectors $\mathbf{A}=\langle a_1,a_2\rangle$ and $\mathbf{B}=\langle b_1,b_2\rangle$,
$$\det(\mathbf{A},\mathbf{B})=\pm\,\text{area of the parallelogram with sides }\mathbf{A},\mathbf{B},$$
with sign $+$ when $\mathbf{B}$ is counterclockwise from $\mathbf{A}$ (turning by less than $\pi$).

:::

::: {.proof}

1. Let $\theta$ be the angle from $\mathbf{A}$ to $\mathbf{B}$. The area is $\lvert\mathbf{A}\rvert\lvert\mathbf{B}\rvert\lvert\sin\theta\rvert$ (base times height).

2. Rotate $\mathbf{A}$ by $90^\circ$ counterclockwise: $\mathbf{A}'=\langle -a_2,a_1\rangle$, with $\lvert\mathbf{A}'\rvert=\lvert\mathbf{A}\rvert$. The angle between $\mathbf{A}'$ and $\mathbf{B}$ is $\pi/2-\theta$, so $\mathbf{A}'\cdot\mathbf{B}=\lvert\mathbf{A}\rvert\lvert\mathbf{B}\rvert\cos(\pi/2-\theta)=\lvert\mathbf{A}\rvert\lvert\mathbf{B}\rvert\sin\theta$.

3. But $\mathbf{A}'\cdot\mathbf{B}=-a_2b_1+a_1b_2=\det(\mathbf{A},\mathbf{B})$. So the determinant is the area with the sign of $\sin\theta$.

:::

::: {#fig-cross-product-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.3,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,3.5) node[lab, above] {$y$};
\fill[tintA] (0,0) -- (3,1) -- (4,3) -- (1,2) -- cycle;
\draw[->, emph] (0,0) -- (3,1) node[lab, below right] {$\mathbf{A}=\langle3,1\rangle$};
\draw[->, emph] (0,0) -- (1,2) node[lab, above left] {$\mathbf{B}=\langle1,2\rangle$};
\draw[faint, dashed] (3,1) -- (4,3) -- (1,2);
\draw[->, hl] (0,0) -- (-1,3) node[lab, left] {$\mathbf{A}'$};
\end{tikzpicture}
\end{center}
```

The parallelogram spanned by $\mathbf{A}=\langle3,1\rangle$ and $\mathbf{B}=\langle1,2\rangle$ has area $\det(\mathbf{A},\mathbf{B})=3\cdot2-1\cdot1=5$, which equals $\mathbf{A}'\cdot\mathbf{B}$ for $\mathbf{A}'=\langle-1,3\rangle$, the vector $\mathbf{A}$ turned $90^\circ$.

:::

In space, $\lvert\det(\mathbf{A},\mathbf{B},\mathbf{C})\rvert$ is the volume of the parallelepiped with edges $\mathbf{A},\mathbf{B},\mathbf{C}$ (@thm-determinant-volume); the triple product below gives a second proof.

::: {#def-cross-product .definition name="Cross product"}

For $\mathbf{A},\mathbf{B}$ in space,
$$\mathbf{A}\times\mathbf{B}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\a_1&a_2&a_3\\b_1&b_2&b_3\end{vmatrix}
=\langle a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1\rangle .$$
The determinant is a memory aid: it means its expansion along the first row.

:::

::: {#thm-cross-product-geometry .theorem name="Geometric meaning of the cross product"}

1. $\mathbf{A}\times\mathbf{B}$ is perpendicular to both $\mathbf{A}$ and $\mathbf{B}$.
2. $\lvert\mathbf{A}\times\mathbf{B}\rvert=\lvert\mathbf{A}\rvert\lvert\mathbf{B}\rvert\sin\theta$, the area of the parallelogram with sides $\mathbf{A},\mathbf{B}$.
3. $\mathbf{A},\mathbf{B},\mathbf{A}\times\mathbf{B}$ form a right-handed system (right-hand rule: fingers from $\mathbf{A}$ curling towards $\mathbf{B}$, thumb along $\mathbf{A}\times\mathbf{B}$).

:::

::: {.proof}

1. $\mathbf{A}\cdot(\mathbf{A}\times\mathbf{B})=a_1(a_2b_3-a_3b_2)+a_2(a_3b_1-a_1b_3)+a_3(a_1b_2-a_2b_1)=0$, since the six terms cancel in pairs. The same computation gives $\mathbf{B}\cdot(\mathbf{A}\times\mathbf{B})=0$.

2. Expanding both sides gives Lagrange's identity
$$\lvert\mathbf{A}\times\mathbf{B}\rvert^2=\lvert\mathbf{A}\rvert^2\lvert\mathbf{B}\rvert^2-(\mathbf{A}\cdot\mathbf{B})^2 .$$
With $\mathbf{A}\cdot\mathbf{B}=\lvert\mathbf{A}\rvert\lvert\mathbf{B}\rvert\cos\theta$ the right side is $\lvert\mathbf{A}\rvert^2\lvert\mathbf{B}\rvert^2\sin^2\theta$; take square roots ($\sin\theta\ge0$ for $0\le\theta\le\pi$).

3. The orientation is checked on $\mathbf{i}\times\mathbf{j}=\mathbf{k}$; moving $\mathbf{A},\mathbf{B}$ continuously without making them parallel never changes it, because $\mathbf{A}\times\mathbf{B}$ never vanishes on the way. (This step is a sketch.)

:::

::: {#prp-cross-product-rules .proposition name="Rules for the cross product"}

$\mathbf{B}\times\mathbf{A}=-\mathbf{A}\times\mathbf{B}$, $\mathbf{A}\times\mathbf{A}=\mathbf{0}$, the product is linear in each factor, and
$$\mathbf{i}\times\mathbf{j}=\mathbf{k},\qquad\mathbf{j}\times\mathbf{k}=\mathbf{i},\qquad\mathbf{k}\times\mathbf{i}=\mathbf{j}.$$
The cross product is not associative: $(\mathbf{i}\times\mathbf{i})\times\mathbf{j}=\mathbf{0}$ but $\mathbf{i}\times(\mathbf{i}\times\mathbf{j})=-\mathbf{j}$.

:::

::: {#thm-triple-product .theorem name="Triple product and volume"}

$$\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=\det(\mathbf{A},\mathbf{B},\mathbf{C}),$$
and its absolute value is the volume of the parallelepiped with edges $\mathbf{A},\mathbf{B},\mathbf{C}$.

:::

::: {.proof}

1. Dotting $\mathbf{A}$ with the first-row expansion of $\mathbf{B}\times\mathbf{C}$ replaces $\mathbf{i},\mathbf{j},\mathbf{k}$ by $a_1,a_2,a_3$, which is the expansion of $\det(\mathbf{A},\mathbf{B},\mathbf{C})$ along its first row.

2. Take the face with sides $\mathbf{B},\mathbf{C}$ as base: its area is $\lvert\mathbf{B}\times\mathbf{C}\rvert$ and its unit normal is $\hat{\mathbf{n}}=(\mathbf{B}\times\mathbf{C})/\lvert\mathbf{B}\times\mathbf{C}\rvert$.

3. The height is the component of $\mathbf{A}$ along the normal, $\lvert\mathbf{A}\cdot\hat{\mathbf{n}}\rvert$. Volume $=$ base $\times$ height $=\lvert\mathbf{B}\times\mathbf{C}\rvert\,\lvert\mathbf{A}\cdot\hat{\mathbf{n}}\rvert=\lvert\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})\rvert$.

:::

::: {#exm-space-triangle .example name="A triangle in space"}

For $P=(1,0,0)$, $Q=(0,1,0)$, $R=(0,0,2)$: $\overrightarrow{PQ}=\langle-1,1,0\rangle$, $\overrightarrow{PR}=\langle-1,0,2\rangle$.

- The angle at $P$: $\cos\theta=\dfrac{1}{\sqrt2\sqrt5}=\dfrac1{\sqrt{10}}$, so $\theta\approx71.6^\circ$.
- $\overrightarrow{PQ}\times\overrightarrow{PR}=\langle2,2,1\rangle$, of length $3$, so the triangle has area $\tfrac32$.
- $\langle2,2,1\rangle$ is normal to the plane through $P,Q,R$, which is therefore $2x+2y+z=2$.

:::

::: {#rmk-cross-product-1 .remark name="Plane through three points"}

A point $P$ lies in the plane through $P_1,P_2,P_3$ exactly when the box with edges $\overrightarrow{P_1P},\overrightarrow{P_1P_2},\overrightarrow{P_1P_3}$ is flat, i.e. $\det(\overrightarrow{P_1P},\overrightarrow{P_1P_2},\overrightarrow{P_1P_3})=0$. By @thm-triple-product this is the same equation as $\overrightarrow{P_1P}\cdot\mathbf{N}=0$ with $\mathbf{N}=\overrightarrow{P_1P_2}\times\overrightarrow{P_1P_3}$.

:::
