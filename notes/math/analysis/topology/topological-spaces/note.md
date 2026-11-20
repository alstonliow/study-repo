---
title: "Topological Spaces"
sources: [camib-at-m2]
requires: [math/analysis/metric-spaces/continuous-maps]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Metric and Topological Spaces (Easter 2015 lecture notes), Sections 2.1-2.2, in our own wording; examples ours; proofs written out in steps. -->

In a metric space, convergence and continuity can be described by open sets alone (@prp-convergence-open-sets, @thm-continuity-open-sets), and the open sets have the three properties of @thm-open-sets-metric. A topological space keeps only the open sets and those properties.

::: {#def-topology .definition name="Topology, topological space"}

A *topology* on a set $X$ is a collection $\mathcal U$ of subsets of $X$, called *open sets*, such that

1. $\emptyset\in\mathcal U$ and $X\in\mathcal U$;
2. any union of members of $\mathcal U$ is in $\mathcal U$;
3. the intersection of any two (hence finitely many) members of $\mathcal U$ is in $\mathcal U$.

A *topological space* is a set with a topology. An *open neighbourhood* of $x$ is an open set containing $x$.

:::

::: {#exm-topologies .example name="Topologies"}

1. *Metric topology.* The open sets of a metric space (@def-open-set-metric) form a topology, by @thm-open-sets-metric. A topological space whose topology arises this way is *metrizable*; different metrics may give the same topology (@def-lipschitz-equivalent-metrics).
2. *Discrete topology*: every subset is open. It is the topology of the discrete metric.
3. *Indiscrete topology*: only $\emptyset$ and $X$ are open.
4. *Cofinite topology* on an infinite set $X$: the open sets are $\emptyset$ and the sets with finite complement. A union of such sets has finite complement (contained in each complement), and so does the intersection of two (the union of two finite complements).
5. On $X=\{0,1\}$, $\{\emptyset,\{1\},X\}$ is a topology (the *Sierpiński space*).

:::

## Continuity and homeomorphism

::: {#def-continuous-topological .definition name="Continuous map" generalizes="def-continuity-metric"}

A map $f:X\to Y$ between topological spaces is *continuous* if $f^{-1}(V)$ is open in $X$ for every open $V\subseteq Y$.

:::

By @thm-continuity-open-sets this agrees with the metric definition when $X$ and $Y$ are metric spaces with their metric topologies. If $g:Y\to Z$ is continuous too, then $(g\circ f)^{-1}(W)=f^{-1}(g^{-1}(W))$ shows that $g\circ f$ is continuous.

::: {#def-homeomorphism .definition name="Homeomorphism"}

A *homeomorphism* is a bijection $f:X\to Y$ such that $f$ and $f^{-1}$ are both continuous. Then $X$ and $Y$ are *homeomorphic*, $X\cong Y$. A property preserved by homeomorphisms is a *topological property*.

:::

A homeomorphism is a bijection between points that also matches the open sets: $U$ is open in $X$ if and only if $f(U)$ is open in $Y$. Being homeomorphic is an equivalence relation: identities, inverses and composites of homeomorphisms are homeomorphisms.

::: {#exm-homeomorphisms .example name="Homeomorphic and not"}

1. Every open interval is homeomorphic to $\mathbb R$: $x\mapsto\tan(\pi(x-\frac12))$ maps $(0,1)$ onto $\mathbb R$ with continuous inverse $y\mapsto\frac12+\frac1\pi\arctan y$, and affine maps relate the other intervals. So boundedness and completeness are not topological properties.
2. A continuous bijection need not be a homeomorphism. The map $f:[0,1)\to S^1=\{z\in\mathbb C:|z|=1\}$, $f(t)=e^{2\pi it}$, is a continuous bijection, but $f^{-1}$ is not continuous at $1$: points of $S^1$ just below $1$ have preimages near $1$, not near $0=f^{-1}(1)$. (That $[0,1)\not\cong S^1$ follows from @sec-math-analysis-topology-connectedness.)
3. The identity map from a set with the discrete topology to the same set with the indiscrete topology is continuous, but its inverse is not if the set has two or more points.

:::

## Sequences and the Hausdorff property

::: {#def-convergence-topological .definition name="Convergence in a topological space" generalizes="def-convergence-metric"}

A sequence $(x_n)$ in a topological space *converges* to $x$ if every open neighbourhood of $x$ contains $x_n$ for all sufficiently large $n$.

:::

By @prp-convergence-open-sets this is the old notion in metric spaces. In general limits need not be unique: in the indiscrete topology the only neighbourhood of any point is $X$, so every sequence converges to every point.

::: {#def-hausdorff .definition name="Hausdorff space"}

A topological space $X$ is *Hausdorff* if any two distinct points $x\ne y$ have disjoint open neighbourhoods: there are open $U\ni x$ and $V\ni y$ with $U\cap V=\emptyset$.

:::

Every metric space is Hausdorff: for $x\ne y$ take $r=\frac12d(x,y)$; the balls $B_r(x)$ and $B_r(y)$ are disjoint by the triangle inequality. So a non-Hausdorff topology, such as the indiscrete, cofinite or Sierpiński topology, is not metrizable.

::: {#prp-hausdorff-unique-limits .proposition name="Limits are unique in Hausdorff spaces" generalizes="prp-limit-unique-metric"}

In a Hausdorff space a sequence has at most one limit.

:::

::: {.proof}

1. Suppose $x_n\to x$ and $x_n\to y$ with $x\ne y$. Take disjoint open $U\ni x$ and $V\ni y$.

2. For large $n$, $x_n\in U$ and $x_n\in V$, contradicting $U\cap V=\emptyset$.

:::

::: {#rmk-topological-spaces-sequences .remark name="Sequences are not enough"}

In metric spaces, closedness, continuity and compactness can all be tested with sequences. In general topological spaces they cannot: on an uncountable set with the *cocountable* topology (open sets: $\emptyset$ and complements of countable sets), a sequence converges only if it is eventually constant. So every subset contains the limits of its convergent sequences, yet not every subset is closed (@def-closed-set-topological): a set closed under limits of sequences need not be closed. So the topological definitions are stated with open sets, and sequences are used only where a metric is available.

:::
