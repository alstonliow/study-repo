---
title: "Affine and Convex Sets"
sources: [ee364a-2, mit18065-21]
requires: [math/linear-algebra/vector-spaces/solving-ax-b]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex sets, in our own wording; proofs written out in steps. -->
<!-- Merged 2026-11-21 (owner approval): def-convex-set moved here from @sec-ai-machine-learning-convex-optimization (MIT 18.065, Lecture 21); wording from 18.065, display form and notation of this part from EE364A. -->

Convex optimization studies sets and functions that behave well under averaging. This note fixes the three basic kinds of set: affine sets (closed under lines), convex sets (closed under segments) and convex cones (closed under nonnegative combinations).

::: {#def-affine-set .definition name="Affine set, affine hull"}

A set $C\subseteq\mathbb{R}^n$ is *affine* if it contains the whole line through any two of its points:
$$x_1,x_2\in C,\ \theta\in\mathbb{R}\ \Longrightarrow\ \theta x_1+(1-\theta)x_2\in C.$$
An *affine combination* of $x_1,\dots,x_k$ is $\sum_i\theta_ix_i$ with $\sum_i\theta_i=1$. The *affine hull* $\operatorname{aff}C$ is the set of all affine combinations of points of $C$.

:::

::: {#prp-affine-set-subspace .proposition name="Affine sets are shifted subspaces"}

A nonempty set $C$ is affine if and only if, for one (equivalently every) $x_0\in C$, the set $V=C-x_0=\{x-x_0\mid x\in C\}$ is a subspace. Every affine set is the solution set $\{x\mid Ax=b\}$ of a system of linear equations, and conversely.

:::

::: {.proof}

1. Suppose $C$ is affine and $x_0\in C$. For $v_1=x_1-x_0$, $v_2=x_2-x_0$ in $V$ and scalars $\alpha,\beta$, the point $\alpha x_1+\beta x_2+(1-\alpha-\beta)x_0$ is an affine combination of three points of $C$.

2. An affine set contains every affine combination of its points: induct on the number of points, writing $\sum_{i\le k}\theta_ix_i=\theta_kx_k+(1-\theta_k)\sum_{i<k}\frac{\theta_i}{1-\theta_k}x_i$ when $\theta_k\ne1$ (some $\theta_i\ne1$ exists if $k\ge2$, so reorder).

3. Hence $\alpha v_1+\beta v_2=\big(\alpha x_1+\beta x_2+(1-\alpha-\beta)x_0\big)-x_0\in V$, so $V$ is a subspace. Conversely, if $V$ is a subspace then $\theta x_1+(1-\theta)x_2=x_0+\theta v_1+(1-\theta)v_2\in C$.

4. Choose a matrix $A$ whose null space is $V$ and put $b=Ax_0$. Then $Ax=b$ iff $x-x_0\in V$ iff $x\in C$. Conversely, the solution set of $Ax=b$ is $x_0+\operatorname{null}A$ for any solution $x_0$, a shifted subspace.

:::

::: {#def-convex-set .definition name="Convex set"}

A set $C\subseteq\mathbb{R}^n$ is *convex* if it contains the segment between any two of its points:
$$x_1,x_2\in C,\ 0\le\theta\le1\ \Longrightarrow\ \theta x_1+(1-\theta)x_2\in C.$$

:::

::: {#def-convex-combination .definition name="Convex combination, convex hull"}

A *convex combination* of $x_1,\dots,x_k$ is a point
$$\theta_1x_1+\cdots+\theta_kx_k,\qquad \theta_i\ge0,\quad \theta_1+\cdots+\theta_k=1.$$
The *convex hull* $\operatorname{conv}C$ of a set $C$ is the set of all convex combinations of points of $C$.

:::

::: {#prp-convex-hull-smallest .proposition name="The convex hull is the smallest convex superset"}

A set is convex (@def-convex-set) if and only if it contains every convex combination of its points. Consequently $\operatorname{conv}C$ is convex, and it is contained in every convex set that contains $C$.

:::

::: {.proof}

1. If a set contains all convex combinations of its points, it contains those with two points, so it is convex.

2. Conversely let $C$ be convex; induct on $k$. For $k=2$ this is the definition. For $k>2$ and $\theta_k<1$ write
$$\sum_{i=1}^k\theta_ix_i=(1-\theta_k)\,y+\theta_kx_k,\qquad y=\sum_{i<k}\frac{\theta_i}{1-\theta_k}x_i,$$
where $y\in C$ by induction (its weights are nonnegative and sum to $1$); then the two-point case applies. If $\theta_k=1$ the combination is $x_k$.

3. A convex combination of two convex combinations of points of $C$ is again a convex combination of points of $C$, so $\operatorname{conv}C$ is convex. Any convex $D\supseteq C$ contains all convex combinations of points of $C$ by step 2, so $D\supseteq\operatorname{conv}C$.

:::

::: {#def-convex-cone .definition name="Cone, convex cone, conic hull"}

A set $C$ is a *cone* if $x\in C$ and $\theta\ge0$ imply $\theta x\in C$. It is a *convex cone* if it is convex and a cone, equivalently if
$$x_1,x_2\in C,\ \theta_1,\theta_2\ge0\ \Longrightarrow\ \theta_1x_1+\theta_2x_2\in C.$$
A *conic combination* is $\sum_i\theta_ix_i$ with all $\theta_i\ge0$; the *conic hull* of $C$ is the set of all conic combinations of its points.

:::

::: {.proof}

1. The two descriptions agree. If $C$ is a convex cone and $\theta_1+\theta_2>0$, then $\theta_1x_1+\theta_2x_2=(\theta_1+\theta_2)\big(\tfrac{\theta_1}{\theta_1+\theta_2}x_1+\tfrac{\theta_2}{\theta_1+\theta_2}x_2\big)$ is a nonnegative multiple of a point of $C$; if $\theta_1=\theta_2=0$ it is $0=0\cdot x_1\in C$.

2. Conversely the displayed property with $\theta_2=0$ gives the cone property, and with $\theta_1+\theta_2=1$ gives convexity.

:::

::: {#exm-hulls-in-plane .example name="Three hulls of two points"}

For $x_1=(1,0)$ and $x_2=(0,1)$ in $\mathbb{R}^2$: the affine hull is the line $u+v=1$; the convex hull is the segment between them; the conic hull is the quadrant $u,v\ge0$. Adding the origin as a third point makes the convex hull the triangle with vertices $0,x_1,x_2$ and leaves the conic hull unchanged.

:::

::: {#rmk-affine-and-convex-sets-1 .remark name="Each kind contains the next"}

Every subspace is an affine set and a convex cone; every affine set and every convex cone is convex. A set is a subspace exactly when it is both affine and a cone.

:::
