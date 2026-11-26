---
title: "Applications of Maximum Flow"
sources: [mit6046-14, mit6046r-7, mit18433-4]
requires: [cs/graph-optimization/ford-fulkerson]
aliases: [cs/graph-algorithms/flow-applications]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 14 and Recitation 7, in our own wording; example our own (checked by computation); proofs written out in steps. On 2026-11-25 bipartite matching moved to its own note (one algorithm per note, SPEC §8.6). -->

Many problems reduce to maximum flow: build a network whose integral flows correspond to the objects wanted, and use integrality (@cor-integral-flow).

Maximum bipartite matching (@sec-cs-graph-optimization-bipartite-matching) has its own note.

## Baseball elimination

::: {#exm-baseball-elimination .example name="Is a team eliminated?"}

In a league, team $i$ has $w_i$ wins and $g_{ij}$ games left against team $j$. Team $x$ is *eliminated* if it cannot finish with the most wins (ties allowed) however the remaining games turn out.

Assume $x$ wins all its remaining games, reaching $W=w_x+\sum_jg_{xj}$. Build a network with a node for each pair $\{i,j\}$ of other teams and a node for each other team $i$: an edge $s\to\{i,j\}$ of capacity $g_{ij}$ (the games to be played), edges $\{i,j\}\to i$ and $\{i,j\}\to j$ of capacity $\infty$ (who wins them), and an edge $i\to t$ of capacity $W-w_i$ (how many more wins $i$ may get without passing $x$). If some $W-w_i<0$, $x$ is eliminated at once.

Then $x$ is *not* eliminated exactly when the maximum flow saturates every edge out of $s$, that is, has value $\sum_{\{i,j\}}g_{ij}$. Indeed, an integral flow assigns the winner of every remaining game so that no team passes $W$. If the flow is smaller, the minimum cut names a set $R$ of teams whose wins plus games among themselves force some team of $R$ above $W$: $\frac{\sum_{i\in R}w_i+\sum_{i,j\in R}g_{ij}}{|R|}>W$.

For example, with three other teams on $70,69,68$ wins and $2$ games left between each pair of them, a team with $68$ wins and $4$ games left reaches $W=72$; the three others must share $6$ more wins among $207$, an average of $71$, so they can all stay at or below $72$ and the team is not eliminated. With $W=70$ it would be, because $\frac{207+6}{3}=71>70$.

:::

```{=latex}
\begin{algorithm}
\caption{Baseball elimination}
\begin{algorithmic}
\INPUT Wins $w_i$, remaining games $g_{ij}$, a team $x$
\OUTPUT Whether $x$ is eliminated
\STATE $W\gets w_x+\sum_jg_{xj}$
\IF{$w_i>W$ for some team $i$}
    \RETURN eliminated
\ENDIF
\STATE build a network: $s\to\{i,j\}$ of capacity $g_{ij}$, $\{i,j\}\to i$ and $\{i,j\}\to j$ of capacity $\infty$, $i\to t$ of capacity $W-w_i$ (teams $i,j\ne x$)
\STATE $f\gets$ a maximum flow
\IF{$|f|=\sum_{\{i,j\}}g_{ij}$}
    \RETURN not eliminated
\ENDIF
\RETURN eliminated
\end{algorithmic}
\end{algorithm}
```

::: {#fig-flow-applications-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s) at (0.00,0.00) {$s$};
\node[small vertex] (t) at (5.60,0.00) {$t$};
\node[box] (p12) at (1.80,1.10) {$1,2$};
\node[box] (p13) at (1.80,0.00) {$1,3$};
\node[box] (p23) at (1.80,-1.10) {$2,3$};
\node[small vertex] (v1) at (3.80,1.10) {$1$};
\node[small vertex] (v2) at (3.80,0.00) {$2$};
\node[small vertex] (v3) at (3.80,-1.10) {$3$};
\draw[->, emph] (s) -- node[edge label, pos=0.5] {$2/2$} (p12);
\draw[->] (p12) -- node[edge label, pos=0.3] {$1$} (v1);
\draw[->] (p12) -- node[edge label, pos=0.3] {$1$} (v2);
\draw[->, emph] (s) -- node[edge label, pos=0.5] {$2/2$} (p13);
\draw[->] (p13) -- node[edge label, pos=0.3] {$1$} (v1);
\draw[->] (p13) -- node[edge label, pos=0.3] {$1$} (v3);
\draw[->, emph] (s) -- node[edge label, pos=0.5] {$2/2$} (p23);
\draw[->] (p23) -- node[edge label, pos=0.3] {$1$} (v2);
\draw[->] (p23) -- node[edge label, pos=0.3] {$1$} (v3);
\draw[->] (v1) -- node[edge label, pos=0.5] {$2/2$} (t);
\draw[->] (v2) -- node[edge label, pos=0.5] {$2/3$} (t);
\draw[->] (v3) -- node[edge label, pos=0.5] {$2/4$} (t);
\end{tikzpicture}
\end{center}
```

The network for the example with $W=72$ (labels are flow/capacity; the middle edges have capacity $\infty$ and show their flow). The other teams have $70$, $69$ and $68$ wins, each pair of them has $2$ games left, and team $i$ may win at most $72-w_i$ more. The flow shown saturates every edge out of $s$ (value $6$): each of the three teams wins $2$ of the remaining games and ends at or below $72$, so the team is not eliminated.

:::

## Other uses

Edge-disjoint paths from $s$ to $t$ (all capacities $1$; the maximum number equals the minimum number of edges whose removal separates $t$ from $s$, which is Menger's theorem), assigning people to tasks with capacities, and image segmentation by minimum cuts all follow the same pattern.

## Arc-disjoint paths

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on flows and cuts (Sections 4.1.1 and 4.2.1), in our own wording; proof written out in steps. It makes the remark on Menger's theorem above precise. -->

::: {#thm-menger-arc-disjoint .theorem name="Menger's theorem (arc version)"}

A directed graph has $k$ pairwise arc-disjoint paths from $s$ to $t$ if and only if $|\delta^+(S)|\ge k$ for every set $S$ with $s\in S$, $t\notin S$.

:::

::: {.proof}

1. *Necessity.* Each path from $s$ to $t$ leaves every such $S$ through an arc of $\delta^+(S)$, and disjoint paths use different arcs.

2. *Sufficiency.* Give every arc capacity $1$. Every $s$–$t$ cut has capacity at least $k$, so by @thm-max-flow-min-cut and @cor-integral-flow there is an integral flow $f$ of value at least $k$, with $f\in\{0,1\}$ on each arc.

3. *Flow decomposition.* While the value is positive, leave $s$ along an arc carrying flow; at every vertex $v\ne t$ that is entered, conservation provides an unused outgoing arc with flow (also when the walk returns to $s$). The walk ends at $t$. Shortcut repeated vertices to get a simple path, and remove the flow on the arcs of the walk; conservation is kept and the value drops by $1$.

4. Repeating $k$ times gives $k$ paths that use disjoint sets of arcs.

:::

The same network argument, with infinite capacity on the edges of a bipartite graph directed from $A$ to $B$, shows that a minimum cut corresponds to a vertex cover $(A\setminus S)\cup(B\cap S)$, which rederives König's theorem (@thm-konig).

