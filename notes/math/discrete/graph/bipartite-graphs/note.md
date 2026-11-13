---
title: "Bipartite graphs"
sources: [fit1058-cn-11.10]
requires: [math/discrete/graph/walks-paths-cycles]
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Bipartite graphs. -->

::: {#def-bipartite .definition name="Bipartite"}

$G$ is *bipartite* if $V=A\sqcup B$ such that every edge has one endpoint in $A$ and the other in $B$.

:::

::: {#exm-bipartite-graphs-1 .example}

If $A$ is a set of jobs and $B$ a set of candidates, joining each job to the candidates qualified for it gives a bipartite graph. $K_{m,n}$ is the bipartite graph with *every* possible edge between the two sides.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a1) at (0,1.5) {};
\node (a2) at (0,0.5) {};
\node (a3) at (0,-0.5) {};
\node (b1) at (2.5,1) {};
\node (b2) at (2.5,0) {};
\draw (a1)--(b1) (a1)--(b2) (a2)--(b1) (a3)--(b2);
\node[draw=none,fill=none] at (0,-1.2) {$A$};
\node[draw=none,fill=none] at (2.5,-0.7) {$B$};
\end{tikzpicture}
\end{center}
```

A bipartite graph: every edge crosses between $A$ and $B$

::: {#def-colouring .definition name="$2$-colouring"}

A *$2$-colouring* of $G$ is a function $f:V\to\{\text{Black},\text{White}\}$ such that adjacent vertices get different colours.

:::

::: {#prp-bipartite-graphs-1 .proposition}

$G$ is bipartite if and only if $G$ has a $2$-colouring.

:::

::: {.proof}

($\Rightarrow$) Colour $A$ Black and $B$ White. Every edge goes between $A$ and $B$, so its endpoints get different colours.

($\Leftarrow$) Given a $2$-colouring $f$, let $A=f^{-1}(\text{Black})$ and $B=f^{-1}(\text{White})$. These split $V$ into two parts, and every edge joins differently coloured vertices, i.e. one in $A$ and one in $B$.

:::

::: {#thm-bipartite-graphs-1 .theorem}

$G$ is bipartite if and only if $G$ has no closed walk of odd length.

:::

::: {.proof}

($\Rightarrow$) A walk in a bipartite graph alternates sides $A,B,A,B,\dots$, so it can only return to its starting side after an even number of steps.

($\Leftarrow$) We build a $2$-colouring, one component at a time. In each component fix a vertex $g$, and colour $v$ Black if $d(g,v)$ is even and White if it is odd. Suppose, for contradiction, that some edge $\{v,w\}$ has both ends the same colour, so $d(g,v)$ and $d(g,w)$ have the same parity. Then a shortest path from $g$ to $v$, the edge $\{v,w\}$, and a shortest path from $w$ back to $g$ together form a closed walk of length $d(g,v)+d(g,w)+1$, which is odd. This contradicts the hypothesis, so the colouring is valid.

:::

::: {#cor-bipartite-graphs-1 .corollary}

$G$ is bipartite if and only if $G$ has no cycle of odd length.

:::

::: {.proof}

Combine the previous theorem with @thm-odd-closed-walk.

:::

::: {#exm-bipartite-graphs-2 .example}

$C_n$ is bipartite exactly when $n$ is even. $K_3$ (a triangle) is not bipartite, and neither is any graph containing a triangle.

:::
