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

::: {#fig-topological-spaces-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.8) -- (0,1.9) node[lab, above] {$y$};
\draw[emph] (0.150,-1.894) -- (0.173,-1.643) -- (0.195,-1.449) -- (0.218,-1.294) -- (0.240,-1.168) -- (0.262,-1.064) -- (0.285,-0.975) -- (0.307,-0.899) -- (0.330,-0.833) -- (0.352,-0.775) -- (0.375,-0.724) -- (0.398,-0.679) -- (0.420,-0.638) -- (0.443,-0.600) -- (0.465,-0.567) -- (0.487,-0.536) -- (0.510,-0.507) -- (0.532,-0.481) -- (0.555,-0.457) -- (0.578,-0.434) -- (0.600,-0.413) -- (0.623,-0.393) -- (0.645,-0.374) -- (0.667,-0.357) -- (0.690,-0.340) -- (0.712,-0.325) -- (0.735,-0.310) -- (0.758,-0.295) -- (0.780,-0.282) -- (0.802,-0.269) -- (0.825,-0.256) -- (0.847,-0.244) -- (0.870,-0.233) -- (0.892,-0.222) -- (0.915,-0.211) -- (0.937,-0.200) -- (0.960,-0.190) -- (0.982,-0.181) -- (1.005,-0.171) -- (1.027,-0.162) -- (1.050,-0.153) -- (1.073,-0.144) -- (1.095,-0.135) -- (1.117,-0.127) -- (1.140,-0.119) -- (1.162,-0.111) -- (1.185,-0.103) -- (1.208,-0.095) -- (1.230,-0.087) -- (1.252,-0.080) -- (1.275,-0.072) -- (1.297,-0.065) -- (1.320,-0.057) -- (1.342,-0.050) -- (1.365,-0.043) -- (1.387,-0.036) -- (1.410,-0.028) -- (1.432,-0.021) -- (1.455,-0.014) -- (1.477,-0.007) -- (1.500,-0.000) -- (1.522,0.007) -- (1.545,0.014) -- (1.567,0.021) -- (1.590,0.028) -- (1.612,0.036) -- (1.635,0.043) -- (1.657,0.050) -- (1.680,0.057) -- (1.703,0.065) -- (1.725,0.072) -- (1.748,0.080) -- (1.770,0.087) -- (1.792,0.095) -- (1.815,0.103) -- (1.838,0.111) -- (1.860,0.119) -- (1.883,0.127) -- (1.905,0.135) -- (1.927,0.144) -- (1.950,0.153) -- (1.972,0.162) -- (1.995,0.171) -- (2.018,0.181) -- (2.040,0.190) -- (2.062,0.200) -- (2.085,0.211) -- (2.107,0.222) -- (2.130,0.233) -- (2.152,0.244) -- (2.175,0.256) -- (2.197,0.269) -- (2.220,0.282) -- (2.242,0.295) -- (2.265,0.310) -- (2.287,0.325) -- (2.310,0.340) -- (2.333,0.357) -- (2.355,0.374) -- (2.377,0.393) -- (2.400,0.413) -- (2.422,0.434) -- (2.445,0.457) -- (2.467,0.481) -- (2.490,0.507) -- (2.512,0.536) -- (2.535,0.567) -- (2.558,0.600) -- (2.580,0.638) -- (2.603,0.679) -- (2.625,0.724) -- (2.647,0.775) -- (2.670,0.833) -- (2.692,0.899) -- (2.715,0.975) -- (2.737,1.064) -- (2.760,1.168) -- (2.782,1.294) -- (2.805,1.449) -- (2.828,1.643) -- (2.850,1.894);
\draw[faint, dashed] (3,-1.8) -- (3,1.9);\draw[faint] (3.000,-0.06) -- (3.000,0.06); \node[lab, tick, below] at (3.000,-0.05) {$1$};\node[lab, right] at (2.0,1.6) {$\tan(\pi(x-\frac12))$};
\end{tikzpicture}
\end{center}
```

Item 1: $\tan(\pi(x-\frac12))$ stretches $(0,1)$ onto all of $\mathbb R$ continuously and invertibly, so a bounded interval is homeomorphic to an unbounded line.

:::

::: {#fig-topological-spaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,0) -- (2.5,0); \node[dot] at (0,0) {}; \node[hollow dot] at (2.5,0) {};
\node[lab, below] at (0,-0.05) {$0$}; \node[lab, below] at (2.5,-0.05) {$1$};
\draw[hl] (0,0) -- (0.4,0); \draw[hl] (2.1,0) -- (2.5,0);
\draw[map] (2.9,0) -- node[lab, above] {$e^{2\pi it}$} (3.9,0);
\draw[emph] (5.2,0) circle (0.9); \node[dot] at (6.1,0) {}; \node[lab, right] at (6.1,0) {$1$};
\draw[hl] (6.1,0) arc (0:25:0.9); \draw[hl] (6.1,0) arc (0:-25:0.9);
\end{tikzpicture}
\end{center}
```

Item 2: $t\mapsto e^{2\pi it}$ bends $[0,1)$ round the circle. A small arc around $1$ (orange) comes from two far-apart pieces near $0$ and near $1$, so the inverse is not continuous at $1$.

:::

## Sequences and the Hausdorff property

::: {#def-convergence-topological .definition name="Convergence in a topological space" generalizes="def-convergence-metric"}

A sequence $(x_n)$ in a topological space *converges* to $x$ if every open neighbourhood of $x$ contains $x_n$ for all sufficiently large $n$.

:::

By @prp-convergence-open-sets this is the old notion in metric spaces. In general limits need not be unique: in the indiscrete topology the only neighbourhood of any point is $X$, so every sequence converges to every point.

::: {#def-hausdorff .definition name="Hausdorff space"}

A topological space $X$ is *Hausdorff* if any two distinct points $x\ne y$ have disjoint open neighbourhoods: there are open $U\ni x$ and $V\ni y$ with $U\cap V=\emptyset$.

:::

::: {#fig-topological-spaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.5,-1.0) rectangle (4.5,1.2); \node[lab] at (-0.2,0.95) {$X$};
\draw[regionA] (1,0) circle (0.8); \draw[regionB] (3,0) circle (0.8);
\node[dot] at (1,0) {}; \node[lab, below] at (1,0) {$x$}; \node[dot] at (3,0) {}; \node[lab, below] at (3,0) {$y$};
\node[lab] at (1,0.45) {$U$}; \node[lab] at (3,0.45) {$V$};
\end{tikzpicture}
\end{center}
```

Hausdorff: any two distinct points have disjoint open neighbourhoods $U\ni x$ and $V\ni y$. Then a sequence cannot converge to both (@prp-hausdorff-unique-limits).

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
