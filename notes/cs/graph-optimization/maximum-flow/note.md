---
title: "Maximum Flow and Minimum Cut"
sources: [mit6046-13, mit6046-14, mit6046r-7]
requires: []
aliases: [cs/graph-algorithms/maximum-flow]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lectures 13-14 and Recitation 7, in our own wording; example our own (checked by computation); proofs written out in steps. On 2026-11-25 the Ford–Fulkerson method moved to its own note (one algorithm per note, SPEC §8.6); this note is the overview. -->

## Flows and cuts

::: {#def-flow-network .definition name="Flow network, flow"}

A *flow network* is a directed graph $G=(V,E)$ with a *source* $s$, a *sink* $t$, and a non-negative *capacity* $c(u,v)$ on each edge ($c(u,v)=0$ for non-edges). A *flow* is a function $f:V\times V\to\mathbb R$ with

1. *capacity constraint:* $f(u,v)\le c(u,v)$;
2. *skew symmetry:* $f(u,v)=-f(v,u)$ (flow from $v$ to $u$ counts negatively);
3. *conservation:* $\sum_vf(u,v)=0$ for every $u\ne s,t$ (what enters leaves).

Its *value* is $|f|=\sum_vf(s,v)$, the net flow out of $s$. The *maximum-flow problem* asks for a flow of largest value.

:::

::: {#def-st-cut .definition name="$s$-$t$ cut"}

An *$s$-$t$ cut* $(S,T)$ splits $V$ into $S\ni s$ and $T=V\setminus S\ni t$. Its *capacity* is $c(S,T)=\sum_{u\in S,v\in T}c(u,v)$, and the net flow across it is $f(S,T)=\sum_{u\in S,v\in T}f(u,v)$.

:::

::: {#lem-flow-across-cut .lemma name="Flow across any cut"}

For every flow $f$ and every $s$-$t$ cut $(S,T)$, $f(S,T)=|f|\le c(S,T)$.

:::

::: {.proof}

1. Summing conservation over the vertices of $S$ other than $s$, and adding the definition of $|f|$: $\sum_{u\in S}\sum_{v\in V}f(u,v)=|f|$.

2. The terms with both ends in $S$ cancel in pairs by skew symmetry, leaving $f(S,T)=|f|$.

3. Each term $f(u,v)\le c(u,v)$, so $f(S,T)\le c(S,T)$.

:::

## Residual networks and augmenting paths

::: {#def-residual-network .definition name="Residual network, augmenting path"}

The *residual capacity* of a pair is $c_f(u,v)=c(u,v)-f(u,v)$: how much more flow can be pushed from $u$ to $v$ (including by cancelling flow from $v$ to $u$). The *residual network* $G_f$ has an edge $(u,v)$ wherever $c_f(u,v)>0$. An *augmenting path* is a path from $s$ to $t$ in $G_f$; its residual capacity $c_f(p)$ is the smallest $c_f$ on it.

:::

Pushing $c_f(p)$ units along an augmenting path $p$ (adding to $f(u,v)$ and subtracting from $f(v,u)$ on each edge of $p$) gives a flow of value $|f|+c_f(p)$.

::: {#thm-max-flow-min-cut .theorem name="Max-flow min-cut"}

For a flow $f$ the following are equivalent:

1. $|f|=c(S,T)$ for some cut $(S,T)$;
2. $f$ is a maximum flow;
3. $G_f$ has no augmenting path.

In particular the maximum flow value equals the minimum cut capacity.

:::

::: {.proof}

1. *(1) ⇒ (2).* Every flow has value at most $c(S,T)$ by @lem-flow-across-cut, and $f$ reaches it.

2. *(2) ⇒ (3).* An augmenting path would give a larger flow.

3. *(3) ⇒ (1).* Let $S$ be the vertices reachable from $s$ in $G_f$ and $T$ the rest; $t\in T$ since there is no augmenting path. For $u\in S$, $v\in T$ we have $c_f(u,v)=0$ (else $v$ would be reachable), that is $f(u,v)=c(u,v)$. Summing, $|f|=f(S,T)=c(S,T)$.

:::

::: {#exm-max-flow-small .example name="A small network"}

Edges $s\to a$ ($3$), $s\to b$ ($2$), $a\to b$ ($1$), $a\to t$ ($2$), $b\to t$ ($3$). The augmenting paths $s,a,t$ ($2$ units), $s,b,t$ ($2$ units) and $s,a,b,t$ ($1$ unit) give a flow of value $5$. The cut $S=\{s\}$ has capacity $3+2=5$, so the flow is maximum.

:::

::: {#fig-maximum-flow-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s) at (0,0) {$s$};
\node[small vertex] (a) at (2,1) {$a$};
\node[small vertex] (b) at (2,-1) {$b$};
\node[small vertex] (t) at (4,0) {$t$};
\draw[->, emph] (s) -- node[edge label] {$3/3$} (a);
\draw[->, emph] (s) -- node[edge label] {$2/2$} (b);
\draw[->, emph] (a) -- node[edge label] {$1/1$} (b);
\draw[->, emph] (a) -- node[edge label] {$2/2$} (t);
\draw[->, emph] (b) -- node[edge label] {$3/3$} (t);
\draw[hl, dashed] (0.55,1.5) -- (0.55,-1.5);
\node[lab,tick] at (0.55,1.75) {cut $S=\{s\}$: capacity $5$};
\end{tikzpicture}
\end{center}
```

A maximum flow of value $5$ (labels are flow/capacity). The cut separating $s$ from the rest has capacity $3+2=5$, so no flow can be larger: max-flow equals min-cut.

:::

## The algorithms

The Ford–Fulkerson method (@sec-cs-graph-optimization-ford-fulkerson) has its own note, with Edmonds–Karp, its choice of shortest augmenting paths.

| algorithm | augmenting path | augmentations | time $O(\cdot)$ |
|---|---|---|---|
| Ford–Fulkerson (@cor-integral-flow) | any; integer capacities | at most $\lvert f^*\rvert$ | $\lvert E\rvert\cdot\lvert f^*\rvert$ |
| Edmonds–Karp (@thm-edmonds-karp) | shortest, by BFS | $\lvert V\rvert\cdot\lvert E\rvert$ | $\lvert V\rvert\cdot\lvert E\rvert^2$ |
