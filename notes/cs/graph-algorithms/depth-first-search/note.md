---
title: "Depth-First Search and Connected Components"
sources: [mit6006-10, mit6006r-10]
requires: [cs/graph-algorithms/breadth-first-search]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 10 and Recitation 10, in our own wording; proofs written out in steps. -->

## Depth-first search

::: {#def-dfs .definition name="Depth-first search"}

*Depth-first search* (DFS) from $s$: set $P(s)$ empty and call $\mathrm{visit}(s)$, where $\mathrm{visit}(u)$ does the following: for each $v\in\operatorname{Adj}(u)$ that has no parent yet (and is not $s$), set $P(v)=u$ and call $\mathrm{visit}(v)$. When the loop ends, the visit of $u$ *finishes*.

:::

```{=latex}
\begin{algorithm}
\caption{Depth-first search: $\mathrm{visit}(u)$}
\begin{algorithmic}
\INPUT Graph $G=(V,E)$ as adjacency lists, a vertex $u$; parent table $P$
\COMMENT{DFS from $s$: leave every $P(v)$ unset, set $P(s)\gets$ none and call $\mathrm{visit}(s)$}
\FOR{$v\in\operatorname{Adj}(u)$}
    \IF{$P(v)$ is not set}
        \STATE $P(v)\gets u$
        \STATE $\mathrm{visit}(v)$
    \ENDIF
\ENDFOR
\STATE the visit of $u$ finishes \COMMENT{append $u$ to the finishing order}
\end{algorithmic}
\end{algorithm}
```

DFS follows a walk as far as it can, then backs up to the most recent vertex with an unexplored edge. Unlike BFS its parent tree need not consist of shortest paths, but it reaches the same vertices.

::: {#thm-dfs .theorem name="Depth-first search"}

DFS from $s$ visits exactly the vertices reachable from $s$, and for each such $v\ne s$ the parent pointers lead from $v$ back to $s$. It runs in $O(|E|)$ time, apart from initialising the parent table.

:::

::: {.proof}

1. Only reachable vertices are visited, since each visited $v$ is entered along an edge from a visited vertex; following the parents from $v$ goes back along these edges to $s$.

2. *Every reachable vertex is visited*, by induction on $k=\delta(s,v)$. For $k=0$, $v=s$. If $\delta(s,v)=k+1$, let $u$ be the vertex before $v$ on a shortest walk; $\delta(s,u)=k$, so $u$ is visited by induction. While visiting $u$ the loop examines $v\in\operatorname{Adj}(u)$: either $v$ already has a parent (so it was visited) or it is visited now.

3. *Time.* Each vertex is visited at most once, because it gets a parent before its visit. A visit of $u$ does $O(1)$ work per out-neighbour, so the total is $O\bigl(\sum_u\deg(u)\bigr)=O(|E|)$ (plus $O(1)$ for $s$).

:::

## Exploring the whole graph

To explore every vertex, not only those reachable from one source, use *Full-DFS*: while some vertex is unvisited, pick one, $s$, and run DFS from $s$, keeping the parent table between runs (a vertex visited in an earlier run is not visited again). *Full-BFS* is the same with BFS. Both visit every vertex once and run in $O(|V|+|E|)$ time.

```{=latex}
\begin{algorithm}
\caption{Full-DFS}
\begin{algorithmic}
\INPUT Graph $G=(V,E)$ as adjacency lists
\OUTPUT Parent table $P$ (a DFS forest) and the finishing order
\STATE leave $P(v)$ unset for every $v\in V$
\FOR{$s\in V$}
    \IF{$P(s)$ is not set}
        \STATE $P(s)\gets$ none \COMMENT{$s$ is the root of a new run}
        \STATE $\mathrm{visit}(s)$ \COMMENT{$P$ is kept between runs}
    \ENDIF
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#prp-connected-components-algorithm .proposition name="Connected components in linear time"}

For an undirected graph, Full-DFS (or Full-BFS) finds the connected components (@def-connected-graph-component): the vertices visited in one run form one component. So the components, and whether the graph is connected, can be found in $O(|V|+|E|)$ time.

:::

::: {.proof}

A run from $s$ visits exactly the vertices reachable from $s$ (@thm-dfs), which in an undirected graph is the component of $s$. A vertex visited in an earlier run lies in an earlier component, and a later run starts at an unvisited vertex, so each run produces a new component and every component is produced.

:::

```{=latex}
\begin{algorithm}
\caption{Connected components}
\begin{algorithmic}
\INPUT Undirected graph $G=(V,E)$ as adjacency lists
\OUTPUT A component number $c(v)$ for every vertex
\STATE $k\gets0$; leave $c(v)$ unset for every $v\in V$
\FOR{$s\in V$}
    \IF{$c(s)$ is not set}
        \STATE $k\gets k+1$
        \STATE run DFS (or BFS) from $s$, setting $c(v)\gets k$ for each vertex $v$ it visits
    \ENDIF
\ENDFOR
\RETURN $c$ \COMMENT{$G$ is connected exactly when $k=1$}
\end{algorithmic}
\end{algorithm}
```

::: {#fig-depth-first-search-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (-0.45,-0.85) rectangle (1.45,1.05);
\draw[regionB] (1.95,-0.85) rectangle (3.85,1.05);
\draw[regionC] (4.35,-0.85) rectangle (5.25,1.05);
\node[small vertex] (a) at (0.00,0.60) {$a$};
\node[small vertex] (b) at (1.00,0.60) {$b$};
\node[small vertex] (c) at (0.50,-0.40) {$c$};
\node[small vertex] (d) at (2.40,0.60) {$d$};
\node[small vertex] (e) at (3.40,0.60) {$e$};
\node[small vertex] (f) at (2.40,-0.40) {$f$};
\node[small vertex] (g) at (3.40,-0.40) {$g$};
\node[small vertex] (h) at (4.80,0.10) {$h$};
\draw[emph] (a) -- (b);
\draw[faint] (a) -- (c);
\draw[emph] (b) -- (c);
\draw[emph] (d) -- (e);
\draw[faint] (d) -- (f);
\draw[emph] (e) -- (g);
\draw[emph] (f) -- (g);
\node[lab,tick] at (0.50,1.30) {run 1 from $a$};
\node[lab,tick] at (2.90,1.30) {run 2 from $d$};
\node[lab,tick] at (4.80,1.30) {run 3 from $h$};
\end{tikzpicture}
\end{center}
```

Connected components by Full-DFS, starting runs in alphabetical order. Each run visits one component (shaded), and bold edges are its DFS tree edges. Three runs, so the graph has three components and is not connected.

:::

The finishing order of Full-DFS also gives a topological order of a DAG and detects directed cycles (@sec-cs-graph-algorithms-topological-sort).
