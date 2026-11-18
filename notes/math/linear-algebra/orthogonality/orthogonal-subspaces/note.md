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
