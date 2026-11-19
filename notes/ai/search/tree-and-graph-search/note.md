---
title: "Tree Search, Graph Search and Uninformed Strategies"
sources: [cs188-2, cs188-3]
requires: [ai/search/search-problems]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 2 (agents, state space graphs and search trees, tree search, DFS, BFS, iterative deepening) and Lecture 3 (greedy search, graph search), in our own wording; proofs written out in steps; the example was checked by a short Python simulation. -->

A *reflex agent* chooses each action from the current percept alone; a *planning agent* asks what would happen if it took a sequence of actions, which needs a model of the world, here a search problem (@def-search-problem). This note describes the general scheme by which a planning agent explores possible plans and the strategies that use no knowledge beyond the problem itself.

::: {#def-search-tree .definition name="State space graph, search tree"}

The *state space graph* of a search problem has one vertex per state and an edge $s\to\text{Succ}(s,a)$ for every action $a\in\text{Actions}(s)$. Each state appears in it once.

The *search tree* has the start state at its root, and the children of a node for state $s$ are nodes for the states $\text{Succ}(s,a)$, $a\in\text{Actions}(s)$. A node of the search tree stands for the whole path (plan) from the root to it, so a state may appear at many nodes, and the tree is infinite when the graph has a cycle reachable from the start.

:::

Neither structure is built in full; search algorithms build as little of the search tree as they can.

::: {#def-tree-search .definition name="Tree search, fringe, strategy"}

*Tree search* keeps a *fringe* of unexpanded nodes of the search tree, which starts as the root. It repeatedly removes a node from the fringe; if its state is an end state it returns the node's plan, and otherwise it *expands* the node, adding its children to the fringe. If the fringe becomes empty there is no solution. The rule deciding which node to remove is the *strategy*.

*Graph search* is tree search that also keeps the set of states already expanded (the *closed set*) and skips a removed node whose state is in it, so that no state is expanded twice.

:::

```{=latex}
\begin{algorithm}
\caption{Tree search and graph search}
\begin{algorithmic}
\INPUT Search problem, strategy
\OUTPUT A solution, or none
\STATE $\mathit{fringe}\gets\{\text{node}(s_{\text{start}})\}$; $\mathit{closed}\gets\emptyset$
\WHILE{$\mathit{fringe}$ is not empty}
    \STATE $n\gets$ node chosen by the strategy, removed from $\mathit{fringe}$
    \IF{$\text{IsEnd}(n.\mathit{state})$}
        \RETURN $n.\mathit{plan}$
    \ENDIF
    \IF{graph search and $n.\mathit{state}\in\mathit{closed}$}
        \STATE \textbf{continue}
    \ENDIF
    \STATE $\mathit{closed}\gets\mathit{closed}\cup\{n.\mathit{state}\}$
    \FOR{$a\in\text{Actions}(n.\mathit{state})$}
        \STATE add the child node for $\text{Succ}(n.\mathit{state},a)$ to $\mathit{fringe}$
    \ENDFOR
\ENDWHILE
\RETURN none
\end{algorithmic}
\end{algorithm}
```

The end test is made when a node is removed, not when it is added; for the cost-sensitive strategies this is what makes the returned plan optimal.

::: {#def-uninformed-strategies .definition name="Depth-first, breadth-first and iterative deepening search"}

All strategies can be seen as one fringe ordered by a priority.

- *Depth-first search* (DFS) removes the deepest node: the fringe is a stack (last in, first out).
- *Breadth-first search* (BFS) removes the shallowest node: the fringe is a queue (first in, first out).
- *Iterative deepening search* (IDS) runs DFS that does not expand nodes at depth $\ell$, for $\ell=0,1,2,\dots$ in turn, until one run finds a solution.
- *Uniform cost search* removes the node of least path cost $g(n)$ (@def-uniform-cost-search).

These strategies use only the problem's definition and are called *uninformed*.

:::

To compare them, let $b$ be the *branching factor* (the maximum number of actions in a state), $m$ the maximum depth of the search tree (possibly $\infty$), and $s$ the depth of the shallowest end node. A strategy is *complete* if it returns a solution whenever one exists, and *optimal* if the solution it returns has minimum cost. A tree with branching factor $b$ has at most $1+b+\dots+b^{k}=O(b^{k})$ nodes up to depth $k$ when $b\ge2$.

::: {#thm-uninformed-search-properties .theorem name="Properties of DFS, BFS and IDS"}

For tree search with $b\ge2$:

$$
\begin{array}{lcccc}
 & \text{time} & \text{space} & \text{complete} & \text{optimal}\\
\text{DFS} & O(b^{m}) & O(bm) & \text{if } m<\infty & \text{no}\\
\text{BFS} & O(b^{s}) & O(b^{s}) & \text{yes} & \text{if all costs are equal}\\
\text{IDS} & O(b^{s}) & O(bs) & \text{yes} & \text{if all costs are equal}
\end{array}
$$

Time counts nodes generated and space the largest size of the fringe.

:::

::: {.proof}

1. DFS. The fringe holds, for each node on the current path, its unexpanded siblings, at most $b$ per level and at most $m$ levels, so $O(bm)$ nodes. In the worst case DFS generates the whole tree, $O(b^{m})$ nodes. If $m<\infty$ the tree is finite and DFS, which removes every node it adds, eventually reaches every end node, so it is complete; if $m=\infty$ it can follow an infinite branch forever. It returns the first end node in left-to-right order, which need not be cheapest: in @exm-uninformed-search, if the children of $A$ were generated in the order $G,C$, DFS would return $S,A,G$ of cost $10$ although $S,A,C,D,G$ costs $5$.
2. BFS. BFS removes all nodes of depth $d$ before any of depth $d+1$. So it removes an end node at depth $s$ after generating at most all nodes up to depth $s+1$ — $O(b^{s+1})$, and $O(b^{s})$ if the end test is made when a node is generated, as is usual for BFS — and the fringe at that time holds at most one level, $O(b^{s})$ nodes. Since depth $s$ is finite, BFS is complete. If every action costs the same $c>0$, the cost of a plan is $c$ times its depth, and the shallowest end node is a cheapest one.
3. IDS. The run with limit $\ell<s$ finds nothing and the run with $\ell=s$ finds the shallowest end node (it explores the whole tree up to depth $s$ in DFS order), so IDS is complete, and optimal for equal costs as BFS is. Each run is a DFS of depth at most $s$, so the fringe holds $O(bs)$ nodes.
4. IDS time. The run with limit $\ell$ generates at most $\sum_{k=0}^{\ell}b^{k}\le\frac{b^{\ell+1}}{b-1}$ nodes, so all runs together generate at most
$$
\sum_{\ell=0}^{s}\frac{b^{\ell+1}}{b-1}\le\frac{b^{s+2}}{(b-1)^{2}}=O(b^{s})\cdot\frac{b^{2}}{(b-1)^{2}},
$$
and $\frac{b^{2}}{(b-1)^{2}}\le4$ for $b\ge2$. Repeating the shallow levels thus costs only a constant factor.

:::

IDS combines the small fringe of DFS with the completeness and shallowest-first behaviour of BFS, which is why it is the usual uninformed choice when the search tree is large. None of DFS, BFS or IDS looks at costs; UCS (@thm-uniform-cost-search) is the cost-sensitive uninformed strategy.

::: {#def-greedy-search .definition name="Greedy search"}

Given a heuristic $h$ estimating the cost from a state to the nearest end state, *greedy (best-first) search* is tree search that removes the node whose state has the least $h$.

:::

Greedy search heads straight for what looks closest to an end state. It ignores the cost already paid, so it is not optimal, and with a misleading heuristic it can behave like a badly guided DFS. A\* search (@def-a-star-search) orders the fringe by $g(n)+h(n)$ and combines both.

::: {#exm-uninformed-search .example name="Five strategies on one graph"}

Take states $S,A,B,C,D,G$ with start $S$, end state $G$ and actions with costs
$$
S\xrightarrow{1}A,\quad S\xrightarrow{4}B,\quad A\xrightarrow{1}C,\quad A\xrightarrow{9}G,\quad B\xrightarrow{3}G,\quad C\xrightarrow{1}D,\quad D\xrightarrow{2}G,
$$
and the heuristic $h(S,A,B,C,D,G)=(5,4,2,3,2,0)$. Children are generated in alphabetical order and ties are broken first in, first out. Tree search gives:

| strategy | states removed, in order | plan returned | cost |
|---|---|---|---|
| DFS | $S,A,C,D,G$ | $S,A,C,D,G$ | $5$ |
| BFS | $S,A,B,C,G$ | $S,A,G$ | $10$ |
| IDS ($\ell=2$ run) | $S,A,C,G$ | $S,A,G$ | $10$ |
| UCS | $S,A,C,D,B,G$ | $S,A,C,D,G$ | $5$ |
| greedy | $S,B,G$ | $S,B,G$ | $7$ |

BFS and IDS return the plan with fewest actions, greedy search the one that looks shortest from $S$ (its first step goes to $B$, with the least $h$), and UCS the cheapest. DFS finds the cheapest plan here only because $C$ comes before $G$ among the children of $A$.

:::

::: {#fig-tree-and-graph-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[small vertex, fill=accentLight, draw=accent] (S) at (0,0) {$S$};
\node[lab, tick] at (0,0.45) {$h=5$};
\node[small vertex, fill=accentLight, draw=accent] (A) at (1.6,0.9) {$A$};
\node[lab, tick] at (1.6,1.35) {$h=4$};
\node[small vertex] (B) at (1.6,-0.9) {$B$};
\node[lab, tick] at (1.6,-0.45) {$h=2$};
\node[small vertex, fill=accentLight, draw=accent] (C) at (3.2,0.9) {$C$};
\node[lab, tick] at (3.2,1.35) {$h=3$};
\node[small vertex, fill=accentLight, draw=accent] (D) at (4.8,0.9) {$D$};
\node[lab, tick] at (4.8,1.35) {$h=2$};
\node[small vertex, fill=accentLight, draw=accent] (G) at (4.8,-0.9) {$G$};
\node[lab, tick] at (4.8,-0.45) {$h=0$};
\draw[->, hl] (S) -- node[edge label] {1} (A);
\draw[->] (S) -- node[edge label] {4} (B);
\draw[->, hl] (A) -- node[edge label] {1} (C);
\draw[->] (A) -- node[edge label] {9} (G);
\draw[->] (B) -- node[edge label] {3} (G);
\draw[->, hl] (C) -- node[edge label] {1} (D);
\draw[->, hl] (D) -- node[edge label] {2} (G);
\end{tikzpicture}
\end{center}
```

The graph of @exm-uninformed-search with action costs on the edges and heuristic values above the states. The highlighted path $S,A,C,D,G$ of cost $5$ is the one UCS returns; BFS and IDS return $S,A,G$ (cost $10$) and greedy search $S,B,G$ (cost $7$).

:::
