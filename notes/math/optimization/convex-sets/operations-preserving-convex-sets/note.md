---
title: "Operations that Preserve Convexity of Sets"
sources: [ee364a-2]
requires: [math/optimization/convex-sets/examples-of-convex-sets]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex sets, in our own wording; proofs written out in steps. -->

To show a set is convex one rarely uses the definition. Instead one builds the set from simple convex sets by intersections, affine maps, perspective maps and linear-fractional maps, which all preserve convexity.

::: {#prp-intersection-convex .proposition name="Intersections of convex sets"}

Any intersection (finite or infinite) of convex sets is convex. For example
$$S=\{x\in\mathbb{R}^m\mid\ \lvert p(t)\rvert\le1\ \text{for}\ \lvert t\rvert\le\pi/3\},\qquad p(t)=\textstyle\sum_{k=1}^m x_k\cos kt,$$
is convex, being the intersection over $t$ of the slabs $\{x\mid -1\le(\cos t,\dots,\cos mt)\,x\le1\}$.

:::

::: {.proof}

1. If $x_1,x_2$ lie in every set $C_\alpha$, then so does each point of the segment between them, since each $C_\alpha$ is convex.

:::

::: {#prp-affine-image-convex .proposition name="Images and preimages under affine maps"}

Let $f(x)=Ax+b$. If $S\subseteq\mathbb{R}^n$ is convex then $f(S)$ is convex, and if $T\subseteq\mathbb{R}^m$ is convex then $f^{-1}(T)=\{x\mid f(x)\in T\}$ is convex. Examples: scaling, translation, projection onto some coordinates, the sum $S_1+S_2$, and the solution set $\{x\mid x_1A_1+\cdots+x_mA_m\preceq B\}$ of a linear matrix inequality (the preimage of $\mathbb S^p_+$ under $x\mapsto B-\sum_ix_iA_i$).

:::

::: {.proof}

1. Affine maps preserve convex combinations: $f(\theta x_1+(1-\theta)x_2)=\theta f(x_1)+(1-\theta)f(x_2)$.

2. Image: two points of $f(S)$ are $f(x_1),f(x_2)$ with $x_i\in S$; their combination is $f$ of a point of $S$.

3. Preimage: if $f(x_1),f(x_2)\in T$ then $f(\theta x_1+(1-\theta)x_2)$ is a convex combination of them, hence in $T$.

4. The sum $S_1+S_2$ is the image of the convex set $S_1\times S_2$ under $(x,y)\mapsto x+y$.

:::

::: {#def-perspective-function .definition name="Perspective and linear-fractional functions"}

The *perspective* $P:\mathbb{R}^{n+1}\to\mathbb{R}^n$ is
$$P(x,t)=x/t,\qquad\operatorname{dom}P=\{(x,t)\mid t>0\}.$$
A *linear-fractional* function is $f(x)=\dfrac{Ax+b}{c^{\mathsf T}x+d}$ with $\operatorname{dom}f=\{x\mid c^{\mathsf T}x+d>0\}$, the perspective composed with an affine map.

:::

::: {#prp-perspective-preserves-convexity .proposition name="Perspective and linear-fractional maps preserve convexity"}

If $C\subseteq\operatorname{dom}P$ is convex, then $P(C)$ is convex; if $D$ is convex, so is $P^{-1}(D)$. The same holds for linear-fractional functions.

:::

::: {.proof}

1. The perspective maps segments to segments. Take $(x_1,t_1),(x_2,t_2)$ with $t_i>0$ and $0\le\theta\le1$. Then
$$P\big(\theta(x_1,t_1)+(1-\theta)(x_2,t_2)\big)=\frac{\theta x_1+(1-\theta)x_2}{\theta t_1+(1-\theta)t_2}=\mu\frac{x_1}{t_1}+(1-\mu)\frac{x_2}{t_2},$$
$$\mu=\frac{\theta t_1}{\theta t_1+(1-\theta)t_2}\in[0,1].$$

2. As $\theta$ runs over $[0,1]$, $\mu$ runs over $[0,1]$ (it is continuous and increasing, with $\mu(0)=0$, $\mu(1)=1$). So the image of the segment is the segment between the images.

3. Image: two points of $P(C)$ come from two points of $C$; the segment between those lies in $C$ and maps onto the segment between the images, so $P(C)$ is convex.

4. Preimage: if $P(x_1,t_1),P(x_2,t_2)\in D$, step 1 shows $P$ of every point between them lies on the segment between these images, hence in $D$.

5. A linear-fractional function is $P$ after the affine map $x\mapsto(Ax+b,c^{\mathsf T}x+d)$, so the affine case (@prp-affine-image-convex) finishes the proof.

:::

::: {#exm-linear-fractional-probability .example name="Conditional probabilities"}

Let $u,v$ be random variables with values in $\{1,\dots,n\}$ and $\{1,\dots,m\}$ and $p_{ij}=\operatorname{P}(u=i,v=j)$. The conditional probability $f_{ij}=\operatorname{P}(u=i\mid v=j)=p_{ij}/\sum_kp_{kj}$ is a linear-fractional function of $p$. Hence if the joint distribution $p$ ranges over a convex set, the conditional distribution ranges over a convex set too.

:::

::: {#rmk-operations-preserving-convex-sets-1 .remark name="Recipe for proving convexity"}

Two routes: apply the definition directly, or express the set as obtained from known convex sets by the operations above. The second is almost always shorter.

:::
