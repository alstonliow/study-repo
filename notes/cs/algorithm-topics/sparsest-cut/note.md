---
title: "Sparsest Cut, Multicommodity Flow and Metric Embeddings"
sources: [mit6854-19]
requires: [cs/graph-optimization/maximum-flow, math/combinatorial-optimization/polyhedra/lp-duality]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 19 (Sections 4-6), in our own wording; proofs written out in steps. The lectures that prove the O(log k) bound are not in the course's published notes; the theorem of Linial, London and Rabinovich and Bourgain's embedding are stated without proof. -->

A cut is *sparse* if it is small compared with the demand it separates. Finding the sparsest cut is NP-hard and has no known constant-factor approximation, but a linear program, the maximum concurrent flow, approximates it within $O(\log k)$. The proof goes through finite metric spaces.

## Cuts and flows with many commodities

::: {#def-multicommodity-cut .definition name="Multicommodity cut, sparsest cut"}

Let $G=(V,E)$ be an undirected graph with capacities $u_e\ge0$ and $k$ commodities, commodity $i$ having a source $s_i$, a sink $t_i$ and a demand $d_i>0$. For $\varnothing\ne S\subsetneq V$ let $D(S)$ be the total demand of the commodities separated by $S$. The *multicommodity cut* problem asks for
$$\beta^*=\min_S\frac{u(\delta(S))}{D(S)}.$$
*Sparsest cut* is the case with one commodity of demand $1$ for every pair of vertices, so $D(S)=|S|\,|V\setminus S|$; with $k=1$ the problem is the minimum $s$–$t$ cut.

:::

::: {#def-concurrent-flow .definition name="Maximum concurrent flow"}

The *maximum concurrent flow* $\alpha^*$ is the largest $\alpha$ such that $\alpha d_i$ units of every commodity $i$ can be routed from $s_i$ to $t_i$ at the same time, with total flow at most $u_e$ on every edge. It is a linear program (one flow per commodity, shared capacities).

:::

::: {#prp-concurrent-flow-weak-duality .proposition name="Flow bounds cut"}

$\alpha^*\le\beta^*$, with equality when $k=1$.

:::

::: {.proof}

1. Take a concurrent flow with value $\alpha$ and any $S$. Each commodity separated by $S$ sends $\alpha d_i$ units across $\delta(S)$, so $u(\delta(S))\ge\alpha D(S)$.

2. For $k=1$ this is the max-flow min-cut theorem (@thm-max-flow-min-cut) for the undirected graph, each edge replaced by two opposite arcs of capacity $u_e$.

:::

For several commodities the inequality can be strict.

::: {#exm-flow-cut-gap .example name="A gap with four commodities"}

Take $K_{2,3}$ with sides $\{a,b\}$ and $\{x,y,z\}$, all six capacities $1$, and four commodities of demand $1$: $ab$, $xy$, $yz$, $xz$. Every cut has $u(\delta(S))\ge D(S)$ (checked over all $15$ cuts), and $S=\{a\}$ gives $3/3$, so $\beta^*=1$. But each commodity joins two vertices at distance $2$, so routing $\alpha$ units of all four uses at least $4\cdot2\alpha$ units of capacity, while only $6$ exist: $\alpha^*\le\tfrac34<\beta^*$.

:::

::: {#fig-sparsest-cut-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (ka) at (0,1.2) {$a$};
\node[small vertex] (kb) at (0,-1.2) {$b$};
\node[small vertex] (kx) at (2.4,1.6) {$x$};
\node[small vertex] (ky) at (2.4,0) {$y$};
\node[small vertex] (kz) at (2.4,-1.6) {$z$};
\draw[emph] (ka)--(kx);
\draw[emph] (ka)--(ky);
\draw[emph] (ka)--(kz);
\draw[emph] (kb)--(kx);
\draw[emph] (kb)--(ky);
\draw[emph] (kb)--(kz);
\draw[hl, dashed] (ka) to[bend right=40] (kb);
\draw[hl, dashed] (kx) to[bend left=40] (ky);
\draw[hl, dashed] (ky) to[bend left=40] (kz);
\draw[hl, dashed] (kx) to[bend left=70] (kz);
\end{tikzpicture}
\end{center}
```

$K_{2,3}$ with unit capacities (solid) and four unit demands (dashed). Every cut separates at most as much demand as its capacity, so $\beta^*=1$, but each demand needs a path of two edges, so $\alpha^*\le\tfrac34$.

:::

## Finite metric spaces

::: {#def-metric-embedding .definition name="Embedding with distortion"}

A metric space $(X,d)$ *embeds* into $(Y,\ell)$ *with distortion* $c\ge1$ if some map $\varphi:X\to Y$ has $d(x,y)\le\ell(\varphi(x),\varphi(y))\le c\,d(x,y)$ for all $x,y$; with $c=1$ the embedding is *isometric*. Write $\ell_p^n$ for $\mathbb R^n$ with $\lVert x-y\rVert_p$, and $\ell_p$ for the union over $n$.

:::

::: {#prp-frechet-embedding .proposition name="Every finite metric embeds in $\ell_\infty$"}

A metric $d$ on $V=\{1,\dots,n\}$ embeds isometrically into $\ell_\infty^n$ by $\varphi(v)=\big(d(1,v),\dots,d(n,v)\big)$.

:::

::: {.proof}

1. By the triangle inequality, $|d(i,u)-d(i,v)|\le d(u,v)$ for every coordinate $i$, so $\lVert\varphi(u)-\varphi(v)\rVert_\infty\le d(u,v)$.

2. The coordinate $i=u$ gives $|d(u,u)-d(u,v)|=d(u,v)$, so equality holds.

:::

The metrics that embed isometrically in $\ell_1$ are exactly the non-negative combinations of *cut metrics* $\delta_S(x,y)=[\,|\{x,y\}\cap S|=1\,]$, and $\ell_2$-embeddable finite metrics are $\ell_1$-embeddable.

::: {#thm-flow-cut-metrics .theorem name="Flow and cut as minima over metrics"}

Write $\Phi(\ell)=\dfrac{\sum_{e=xy\in E}u_e\,\ell(x,y)}{\sum_id_i\,\ell(s_i,t_i)}$ for a metric $\ell$ on $V$. Then
$$\alpha^*=\min_{\ell\text{ a metric}}\Phi(\ell),\qquad\beta^*=\min_{\ell\ \ell_1\text{-embeddable}}\Phi(\ell).$$
Since every metric embeds in $\ell_\infty$, the two formulas differ only in the class of metrics allowed.

:::

::: {.proof}

1. *$\beta^*$.* A cut metric $\delta_S$ gives $\Phi(\delta_S)=u(\delta(S))/D(S)$, so the minimum over $\ell_1$ metrics is at most $\beta^*$. Conversely an $\ell_1$ metric is $\ell=\sum_S\lambda_S\delta_S$ with $\lambda\ge0$, and $\Phi(\ell)$ is a ratio of sums $\sum\lambda_S\,u(\delta(S))$ over $\sum\lambda_SD(S)$, which is at least the smallest of the ratios, $\beta^*$.

2. *$\alpha^*$.* Write the concurrent flow with path variables. Its LP dual has a length $\ell_e\ge0$ on each edge and a value $z_i$ for each commodity, minimising $\sum_eu_e\ell_e$ subject to $\sum_id_iz_i\ge1$ and every $s_i$–$t_i$ path having length at least $z_i$. At an optimum $z_i$ is the shortest-path distance $\ell(s_i,t_i)$ for the lengths $\ell_e$, which is a metric; scaling removes the normalisation $\sum_id_i\ell(s_i,t_i)=1$. By LP duality (@thm-strong-duality) the optimal values agree.

3. Shortest-path distances never exceed the edge lengths, and replacing $\ell_e$ by the distance $\ell(x,y)$ can only lower the numerator, so the minimum over all metrics equals the minimum over shortest-path metrics.

:::

::: {#thm-llr .theorem name="Linial–London–Rabinovich, Aumann–Rabani"}

$\beta^*\le O(\log k)\,\alpha^*$, and a cut achieving this ratio can be found in polynomial time.

:::

The proof (not given in the course's published notes) solves the LP for $\alpha^*$, takes its optimal metric, and embeds it into $\ell_1$ with distortion $O(\log k)$ on the terminals by *Bourgain's theorem* (every $n$-point metric embeds in $\ell_1$ with distortion $O(\log n)$); since the $\ell_1$ metric is a combination of cut metrics, one of those cuts is good. The bound is tight for flows: on constant-degree expanders the gap is $\Theta(\log n)$. Using a semidefinite relaxation instead, Arora, Rao and Vazirani get $O(\sqrt{\log n})$ for sparsest cut.
