---
title: "Subspaces, Products and Quotients"
sources: [camib-at-m2]
requires: [math/analysis/topology/closure-and-interior, math/discrete/relations/equivalence-relations]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Metric and Topological Spaces (Easter 2015 lecture notes), Section 2.5, in our own wording; examples ours; proofs written out in steps. -->

Three constructions make new spaces from old: restricting to a subset, forming products, and gluing points together. Each topology is chosen so that the natural maps are continuous and maps into or out of the new space can be tested on the old one.

## Subspace topology

::: {#def-subspace-topology .definition name="Subspace topology" generalizes="def-metric-subspace"}

Let $X$ be a topological space and $Y\subseteq X$. The *subspace topology* on $Y$ consists of the sets $V\cap Y$ with $V$ open in $X$.

:::

The axioms hold because $\bigcup(V_\alpha\cap Y)=(\bigcup V_\alpha)\cap Y$ and $(V_1\cap Y)\cap(V_2\cap Y)=(V_1\cap V_2)\cap Y$. For a metric space this is the topology of the metric subspace: a ball of $Y$ is $B^Y_r(y)=B_r(y)\cap Y$, and an open set of $Y$ is a union of such balls. For example $[0,\frac12)$ is open in $Y=[0,1]$, being $(-1,\frac12)\cap Y$, although it is not open in $\mathbb R$.

::: {#prp-subspace-continuity .proposition name="Maps into a subspace"}

Let $Y\subseteq X$ have the subspace topology and $\iota:Y\to X$ be the inclusion. Then $\iota$ is continuous, and a map $f:Z\to Y$ is continuous if and only if $\iota\circ f:Z\to X$ is. In particular the restriction $g|_Y$ of a continuous $g:X\to W$ is continuous.

:::

::: {.proof}

1. $\iota^{-1}(V)=V\cap Y$ is open in $Y$ for $V$ open in $X$, so $\iota$ is continuous, and so is $\iota\circ f$ if $f$ is.

2. Conversely, every open set of $Y$ is $V\cap Y=\iota^{-1}(V)$, and $f^{-1}(V\cap Y)=(\iota\circ f)^{-1}(V)$, which is open if $\iota\circ f$ is continuous.

3. $g|_Y=g\circ\iota$ is a composite of continuous maps.

:::

## Product topology

::: {#def-topological-basis .definition name="Basis of a topology"}

A collection $\mathcal B$ of open sets of $X$ is a *basis* of the topology if every open set is a union of members of $\mathcal B$. Equivalently, for every open $U$ and $x\in U$ there is $B\in\mathcal B$ with $x\in B\subseteq U$.

:::

For a metric space the open balls form a basis.

::: {#def-product-topology .definition name="Product topology"}

The *product topology* on $X\times Y$ has as open sets all unions of *open boxes* $U\times V$ with $U$ open in $X$ and $V$ open in $Y$.

:::

The open boxes form a basis: the union condition is built in, and $(U_1\times V_1)\cap(U_2\times V_2)=(U_1\cap U_2)\times(V_1\cap V_2)$ is again a box, so finite intersections of unions of boxes are unions of boxes.

::: {#prp-product-topology-properties .proposition name="Properties of the product topology"}

1. The projections $\pi_X(x,y)=x$ and $\pi_Y(x,y)=y$ are continuous.
2. A map $f=(f_1,f_2):Z\to X\times Y$ is continuous if and only if $f_1=\pi_X\circ f$ and $f_2=\pi_Y\circ f$ are.
3. The product topology on $\mathbb R\times\mathbb R$ is the metric topology of $\mathbb R^2$. More generally, for metric spaces $X,Y$ it is the topology of the metric $d((x,y),(x',y'))=\max\{d_X(x,x'),d_Y(y,y')\}$.

:::

::: {.proof}

1. $\pi_X^{-1}(U)=U\times Y$ is an open box.

2. If $f$ is continuous, so are its composites with the projections. Conversely, $f^{-1}(U\times V)=f_1^{-1}(U)\cap f_2^{-1}(V)$ is open, and preimages respect unions, so $f^{-1}$ of every open set is open.

3. In the max metric, $B_r((x,y))=B_r(x)\times B_r(y)$ is an open box, so every metric-open set is product-open. Conversely, if $(x,y)\in U\times V$, choose $r$ with $B_r(x)\subseteq U$ and $B_r(y)\subseteq V$; then $B_r((x,y))\subseteq U\times V$, so open boxes are metric-open. For $\mathbb R^2$, the max metric $d_\infty$ is Lipschitz equivalent to $d_2$, so the topologies agree.

:::

## Quotient topology

::: {#def-quotient-topology .definition name="Quotient topology"}

Let $\sim$ be an equivalence relation on a topological space $X$, let $X/{\sim}$ be the set of equivalence classes and $q:X\to X/{\sim}$, $q(x)=[x]$. The *quotient topology* on $X/{\sim}$ declares $V$ open if and only if $q^{-1}(V)$ is open in $X$.

:::

Since $q^{-1}$ preserves unions and intersections, this is a topology, and it is the largest topology making $q$ continuous.

::: {#prp-quotient-maps-out .proposition name="Maps out of a quotient"}

A map $g:X/{\sim}\to Y$ is continuous if and only if $g\circ q:X\to Y$ is continuous. So a continuous $f:X\to Y$ that is constant on each equivalence class induces a continuous map $\bar f:X/{\sim}\to Y$, $\bar f([x])=f(x)$.

:::

::: {.proof}

1. If $g$ is continuous, so is $g\circ q$, since $q$ is continuous.

2. Conversely, for $W$ open in $Y$, $q^{-1}(g^{-1}(W))=(g\circ q)^{-1}(W)$ is open in $X$, which by definition means $g^{-1}(W)$ is open in $X/{\sim}$.

3. If $f$ is constant on classes, $\bar f$ is well defined with $\bar f\circ q=f$, so it is continuous by step 2.

:::

::: {#exm-quotient-spaces .example name="Gluing"}

1. *The circle.* On $[0,1]$ let $0\sim1$ and no other points be identified. The map $t\mapsto e^{2\pi it}$ is constant on classes and induces a continuous bijection $[0,1]/{\sim}\to S^1$; it is a homeomorphism by @prp-compact-hausdorff-homeomorphism. Similarly $\mathbb R/{\sim}$ with $x\sim y\iff x-y\in\mathbb Z$ is a circle, and gluing opposite sides of a square gives a torus.
2. *A non-Hausdorff quotient.* On $\mathbb R$ let $x\sim y\iff x-y\in\mathbb Q$. If $V\ne\emptyset$ is open in the quotient, $U=q^{-1}(V)$ is open, non-empty and satisfies $U+r=U$ for every rational $r$. It contains an interval $(c-\delta,c+\delta)$, so it contains all its rational translates, which cover $\mathbb R$. So the only open sets are $\emptyset$ and the whole space: the quotient is indiscrete, although $\mathbb R$ is a metric space.

:::
