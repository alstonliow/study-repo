---
title: "Simply Connected Regions and the Extended Green's Theorem"
sources: [mit1802-24, mit1802n-V5, mit1802n-V6]
requires: [math/calculus/multivariable/line-integrals/flux-and-normal-form-of-greens-theorem]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 24 and Supplementary Notes V5, V6, in our own wording. Numbers checked in Python (sympy). -->

::: {#exm-vortex-field .example name="A field with a hole"}

$\mathbf{F}=\dfrac{-y\,\mathbf{i}+x\,\mathbf{j}}{x^2+y^2}$, defined everywhere except the origin. Its curl is
$$\frac{\partial}{\partial x}\frac{x}{x^2+y^2}-\frac{\partial}{\partial y}\frac{-y}{x^2+y^2}=\frac{y^2-x^2}{(x^2+y^2)^2}+\frac{x^2-y^2}{(x^2+y^2)^2}=0,$$
but on the circle of radius $a$, counterclockwise, $\mathbf{F}=\hat{\mathbf{T}}/a$, so the work is $\frac1a\cdot2\pi a=2\pi$. Green's theorem would give $0$; it does not apply, because the disk contains the origin, where $\mathbf{F}$ is undefined.

:::

::: {#fig-simply-connected-regions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) circle (1.3); \draw[emph, ->] (0.8,0) arc (0:350:0.8); \node[lab] at (0,-1.6) {simply connected};
\begin{scope}[xshift=4cm]
\fill[tintA, even odd rule] (0,0) circle (1.3) (0,0) circle (0.35);
\draw[emph] (0,0) circle (0.35); \draw[hl, ->] (0.8,0) arc (0:350:0.8);
\node[lab] at (0,-1.6) {not simply connected};
\end{scope}
\end{tikzpicture}
\end{center}
```

A loop in a disk can be shrunk to a point inside the region; a loop around the hole of an annulus cannot.

:::

::: {#def-simply-connected-plane .definition name="Simply connected region"}

A region $D$ of the plane is **simply connected** if the interior of every closed curve lying in $D$ is also contained in $D$ (informally: $D$ has no holes).

:::

The plane, a disk, a half-plane are simply connected; the plane without the origin and an annulus are not.

::: {#thm-green-simply-connected .theorem name="Green's theorem in a simply connected region"}

If $\mathbf{F}$ is continuously differentiable in a simply connected region $D$, then Green's theorem (in both forms) holds for every positively oriented simple closed curve $C$ in $D$. In particular, if $\operatorname{curl}\mathbf{F}=0$ in $D$, then $\mathbf{F}$ is conservative in $D$, hence a gradient field there.

:::

::: {.proof}

1. The interior $R$ of $C$ lies in $D$, so $\mathbf{F}$ is continuously differentiable on all of $R$ and @thm-greens-theorem applies.

2. If the curl is $0$ the double integral is $0$, so $\oint_C\mathbf{F}\cdot d\mathbf{r}=0$ for every simple closed curve, and the argument of @cor-criterion-from-green gives a potential.

:::

::: {#thm-extended-green .theorem name="Extended Green's theorem"}

Let $R$ be a region whose boundary consists of an outer curve $C_1$ and inner curves $C_2,\dots,C_n$ around holes. If all the boundary curves are oriented so that $R$ is on their left (outer curve counterclockwise, inner ones clockwise) and $\mathbf{F}$ is continuously differentiable on $R$, then
$$\oint_{C_1}\mathbf{F}\cdot d\mathbf{r}+\dots+\oint_{C_n}\mathbf{F}\cdot d\mathbf{r}=\iint_R\operatorname{curl}\mathbf{F}\,dA .$$

:::

::: {.proof}

1. Make cuts from the outer curve to each inner curve. The cut region is bounded by a single closed curve which runs along every $C_i$ (with $R$ on its left) and along each cut twice, in opposite directions.

2. Apply Green's theorem to the cut region. The integrals along the cuts cancel, leaving the sum of the integrals over the $C_i$.

:::

::: {#cor-curves-around-hole .corollary name="All loops around the hole give the same work"}

If $\operatorname{curl}\mathbf{F}=0$ in the plane minus the origin, then $\oint_C\mathbf{F}\cdot d\mathbf{r}$ has the same value for every simple closed curve $C$ going once counterclockwise around the origin. For the field of @exm-vortex-field this value is $2\pi$.

:::

::: {.proof}

1. Let $C'$ be a small circle around the origin inside $C$. Apply @thm-extended-green to the region between them, with $C$ counterclockwise and $C'$ clockwise: $\oint_C-\oint_{C'\text{ (ccw)}}=\iint0\,dA=0$.

:::
