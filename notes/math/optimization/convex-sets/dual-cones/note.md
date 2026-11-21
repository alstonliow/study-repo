---
title: "Dual Cones"
sources: [ee364a-2]
requires: [math/optimization/convex-sets/generalized-inequalities, math/optimization/convex-sets/separating-hyperplanes]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex sets, in our own wording; proofs written out in steps. -->

The dual cone of $K$ collects the linear functions that are nonnegative on $K$. It describes generalized inequalities by ordinary ones and characterizes minimum and minimal elements by minimizing linear functions.

::: {#def-dual-cone .definition name="Dual cone"}

The *dual cone* of a cone $K$ is
$$K^*=\{y\mid y^{\mathsf T}x\ge0\ \text{for all}\ x\in K\}.$$
For $K\subseteq\mathbb S^n$ the inner product is $\operatorname{tr}(XY)$.

:::

::: {#exm-dual-cones .example name="Self-dual cones and the dual norm cone"}

1. $(\mathbb{R}^n_+)^*=\mathbb{R}^n_+$: if $y\succeq0$ then $y^{\mathsf T}x\ge0$ for $x\succeq0$; conversely $y^{\mathsf T}e_i=y_i\ge0$.

2. $(\mathbb S^n_+)^*=\mathbb S^n_+$: for $Y\succeq0$ and $X=\sum_i\lambda_iq_iq_i^{\mathsf T}\succeq0$, $\operatorname{tr}(XY)=\sum_i\lambda_iq_i^{\mathsf T}Yq_i\ge0$; conversely $\operatorname{tr}(Y\,zz^{\mathsf T})=z^{\mathsf T}Yz\ge0$ for all $z$.

3. For $K=\{(x,t)\mid\lVert x\rVert\le t\}$, $K^*=\{(u,v)\mid\lVert u\rVert_*\le v\}$, with the *dual norm* $\lVert u\rVert_*=\sup\{u^{\mathsf T}x\mid\lVert x\rVert\le1\}$.

4. Enlarging $K$ shrinks $K^*$: in $\mathbb{R}^2$ the dual of the halfplane $\{x\mid x_2\ge0\}$ is the ray $\{(0,v)\mid v\ge0\}$, and the dual of all of $\mathbb{R}^2$ is $\{0\}$.

:::

::: {#prp-dual-cone-properties .proposition name="Properties of dual cones"}

For any cone $K$: $K^*$ is closed and convex; $K_1\subseteq K_2$ implies $K_2^*\subseteq K_1^*$; if $K$ has nonempty interior then $K^*$ contains no line; if $K$ is convex and its closure contains no line then $K^*$ has nonempty interior; $K^{**}$ is the closure of the convex hull of $K$. In particular, if $K$ is proper then so is $K^*$, and $K^{**}=K$.

:::

::: {.proof}

1. $K^*$ is an intersection of the closed halfspaces $\{y\mid y^{\mathsf T}x\ge0\}$, $x\in K$, so it is closed and convex. A larger $K$ gives more halfspaces and a smaller intersection.

2. Contains no line: if $y,-y\in K^*$ then $y^{\mathsf T}x=0$ on $K$; a set with interior is not inside a hyperplane, so $y=0$.

3. $K^{**}\supseteq K$ by definition, and $K^{**}$ is closed and convex, so it contains $\overline{\operatorname{conv}K}$. Conversely let $z\notin\overline{\operatorname{conv}K}$. Strict separation of the point $z$ from this closed convex cone (@def-strict-separation) gives $y$ with $y^{\mathsf T}z<b\le y^{\mathsf T}x$ for $x$ in the cone; as the cone contains $0$ and all positive multiples, $b\le0$ and $y^{\mathsf T}x\ge0$ there, so $y\in K^*$ and $y^{\mathsf T}z<0$, that is, $z\notin K^{**}$.

4. Nonempty interior of $K^*$: if $\operatorname{int}K^*=\emptyset$, $K^*$ lies in a hyperplane $\{y\mid c^{\mathsf T}y=0\}$ with $c\ne0$; then $\pm c\in K^{**}=\overline{\operatorname{conv}K}$, a line in the closure of $K$ (convex, since $K$ is).

:::

::: {#prp-dual-generalized-inequality .proposition name="Generalized inequalities through the dual cone"}

For a proper cone $K$,
$$x\preceq_Ky\iff\lambda^{\mathsf T}x\le\lambda^{\mathsf T}y\ \text{for all}\ \lambda\succeq_{K^*}0,$$
$$x\prec_Ky\iff\lambda^{\mathsf T}x<\lambda^{\mathsf T}y\ \text{for all}\ \lambda\succeq_{K^*}0,\ \lambda\ne0.$$

:::

::: {.proof}

1. The first line is $K=K^{**}$ applied to $y-x$.

2. If $y-x\in\operatorname{int}K$ and $\lambda\in K^*\setminus\{0\}$, then $y-x-\epsilon\lambda\in K$ for small $\epsilon>0$, so $\lambda^{\mathsf T}(y-x)\ge\epsilon\lVert\lambda\rVert_2^2>0$.

3. If $y-x\notin K$, step 1 gives $\lambda\in K^*$ with $\lambda^{\mathsf T}(y-x)<0$. If $y-x\in K\setminus\operatorname{int}K$, it is a boundary point of $K$, and a supporting hyperplane (@thm-supporting-hyperplane) gives $\mu\ne0$ with $\mu^{\mathsf T}u\le\mu^{\mathsf T}(y-x)$ for all $u\in K$.

4. Since $K$ is a cone containing $0$ and $2(y-x)$, this forces $\mu^{\mathsf T}(y-x)=0$ and $\mu^{\mathsf T}u\le0$ on $K$. So $\lambda=-\mu$ is a nonzero element of $K^*$ with $\lambda^{\mathsf T}(y-x)=0$, and the strict inequality fails.

:::

::: {#thm-minimal-via-dual .theorem name="Minimum and minimal elements by linear functions"}

Let $K$ be proper and $S\subseteq\mathbb{R}^n$.

1. $x$ is the minimum element of $S$ if and only if, for every $\lambda\succ_{K^*}0$, $x$ is the unique minimizer of $\lambda^{\mathsf T}z$ over $z\in S$.

2. If $x$ minimizes $\lambda^{\mathsf T}z$ over $S$ for some $\lambda\succ_{K^*}0$, then $x$ is minimal.

3. If $S$ is convex and $x$ is minimal, then $x$ minimizes $\lambda^{\mathsf T}z$ over $S$ for some nonzero $\lambda\succeq_{K^*}0$.

:::

::: {.proof}

1. If $x$ is the minimum, $z-x\in K$ for all $z\in S$, so $\lambda^{\mathsf T}z\ge\lambda^{\mathsf T}x$, with equality only for $z=x$: if $\lambda\in\operatorname{int}K^*$ and $u\in K$, $u\ne0$, then $\lambda-\epsilon u\in K^*$ for small $\epsilon>0$, so $\lambda^{\mathsf T}u\ge\epsilon\lVert u\rVert_2^2>0$.

2. Conversely, if $x$ is the unique minimizer for every $\lambda\succ_{K^*}0$, then by continuity $\lambda^{\mathsf T}(z-x)\ge0$ for every $\lambda\in K^*$, so $z-x\in K^{**}=K$.

3. Statement 2: if some $y\in S$, $y\ne x$, had $y\preceq_Kx$, then $x-y\in K\setminus\{0\}$ and $\lambda^{\mathsf T}(x-y)>0$, so $y$ would give a smaller value.

4. Statement 3: the convex sets $S$ and $x-\operatorname{int}K$ are disjoint, since a point $y\in S$ with $x-y\in\operatorname{int}K$ would be below $x$ and different from it. Separating them (@thm-separating-hyperplane) gives $\lambda\ne0$ with $\lambda^{\mathsf T}z\ge\lambda^{\mathsf T}(x-k)$ for $z\in S$, $k\in\operatorname{int}K$. Letting $k\to0$ gives $\lambda^{\mathsf T}z\ge\lambda^{\mathsf T}x$; letting $k$ grow shows $\lambda^{\mathsf T}k\ge0$ on $K$, so $\lambda\in K^*$.

:::

::: {#exm-production-frontier .example name="Efficient production methods"}

A product can be made by several methods; method $x\in P\subseteq\mathbb{R}^n$ uses $x_i$ units of resource $i$. A method is *efficient* if it is minimal in $P$ for $\mathbb{R}^n_+$: no other method uses at most as much of every resource and less of one. By @thm-minimal-via-dual, every minimizer of a positive price vector $\lambda\succ0$ applied to resource use, $\lambda^{\mathsf T}x$, is efficient, and when $P$ is convex every efficient method arises this way with some $\lambda\succeq0$, $\lambda\ne0$.

:::
