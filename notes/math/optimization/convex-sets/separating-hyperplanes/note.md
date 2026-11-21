---
title: "Separating and Supporting Hyperplanes"
sources: [ee364a-2]
requires: [math/optimization/convex-sets/examples-of-convex-sets]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex sets, in our own wording; proofs written out in steps. The proof of separation follows the closest-point argument. -->

Two disjoint convex sets can be split by a hyperplane, and a convex set can be touched at each boundary point by a hyperplane. These two theorems are the geometric source of duality (@sec-math-optimization-duality-lagrange-dual-problem).

::: {#thm-separating-hyperplane .theorem name="Separating hyperplane theorem"}

If $C$ and $D$ are nonempty disjoint convex subsets of $\mathbb{R}^n$, there are $a\ne0$ and $b$ with
$$a^{\mathsf T}x\le b\ \text{for}\ x\in C,\qquad a^{\mathsf T}x\ge b\ \text{for}\ x\in D.$$

:::

::: {.proof}

We prove the case where $C$ and $D$ are closed and one of them, say $D$, is bounded; the general case follows by approximating with such sets and taking a limit of normalized normals.

1. The distance $\operatorname{dist}(C,D)=\inf\{\lVert c-d\rVert_2\mid c\in C,d\in D\}$ is attained at some $c\in C$, $d\in D$: minimize the continuous function $d'\mapsto\operatorname{dist}(d',C)$ over the compact set $D$, and the nearest point of the closed set $C$ exists. Since $C\cap D=\emptyset$, $c\ne d$.

2. Put $a=d-c\ne0$ and $b=\frac12\big(\lVert d\rVert_2^2-\lVert c\rVert_2^2\big)$. The hyperplane $a^{\mathsf T}x=b$ is the perpendicular bisector of the segment $cd$.

3. Suppose some $u\in D$ had $a^{\mathsf T}u<b$. Consider $g(t)=\lVert d+t(u-d)-c\rVert_2^2$. Its derivative at $0$ is $2(d-c)^{\mathsf T}(u-d)=2(a^{\mathsf T}u-a^{\mathsf T}d)$.

4. Now $a^{\mathsf T}d-b=\frac12\lVert d-c\rVert_2^2>0$, so $a^{\mathsf T}u<b<a^{\mathsf T}d$ and $g'(0)<0$. For small $t>0$ the point $d+t(u-d)$ lies in $D$ (convexity) and is closer to $c$ than $d$, contradicting step 1. Hence $a^{\mathsf T}x\ge b$ on $D$.

5. The same argument with the roles of $C$ and $D$ exchanged gives $a^{\mathsf T}x\le b$ on $C$.

:::

::: {#def-strict-separation .definition name="Strict separation"}

$C$ and $D$ are *strictly separated* if $a^{\mathsf T}x<b$ on $C$ and $a^{\mathsf T}x>b$ on $D$. The proof of @thm-separating-hyperplane gives strict separation when $C$ is closed and $D$ is compact. Disjoint convex sets need not be strictly separable: $\{(u,v)\mid v\le0\}$ and $\{(u,v)\mid u>0,\ v\ge1/u\}$ are closed and disjoint, but no hyperplane separates them strictly.

:::

::: {#thm-supporting-hyperplane .theorem name="Supporting hyperplane theorem"}

Let $C$ be convex and $x_0$ a boundary point of $C$. There is $a\ne0$ with $a^{\mathsf T}x\le a^{\mathsf T}x_0$ for all $x\in C$; the hyperplane $\{x\mid a^{\mathsf T}x=a^{\mathsf T}x_0\}$ *supports* $C$ at $x_0$.

:::

::: {.proof}

1. If $\operatorname{int}C$ is empty, $C$ lies in an affine set of lower dimension (its affine hull), and any hyperplane containing that affine set works.

2. Otherwise $\operatorname{int}C$ is a nonempty convex set not containing $x_0$. Apply @thm-separating-hyperplane to $\operatorname{int}C$ and $\{x_0\}$: there is $a\ne0$ with $a^{\mathsf T}x\le a^{\mathsf T}x_0$ for $x\in\operatorname{int}C$.

3. A convex set with nonempty interior lies in the closure of its interior, so by continuity the inequality holds on all of $C$.

:::

::: {#exm-separating-voronoi .example name="Points closer to $a$ than to $b$"}

For distinct $a,b\in\mathbb{R}^n$, $\{x\mid\lVert x-a\rVert_2\le\lVert x-b\rVert_2\}$ is the halfspace $(b-a)^{\mathsf T}x\le\frac12(\lVert b\rVert_2^2-\lVert a\rVert_2^2)$: square both sides and cancel $\lVert x\rVert_2^2$. Its boundary is the perpendicular bisector used in step 2 of the separation proof.

:::

::: {#rmk-separating-hyperplanes-1 .remark name="A converse"}

A closed convex set with nonempty interior whose every boundary point has a supporting hyperplane is the intersection of the halfspaces of those hyperplanes. Conversely, a closed set with nonempty interior that has a supporting hyperplane at every boundary point is convex.

:::
