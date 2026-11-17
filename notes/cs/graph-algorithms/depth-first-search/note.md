---
title: "Depth-First Search, Components and Topological Sort"
sources: [mit6006-10, mit6006r-10]
requires: [cs/graph-algorithms/breadth-first-search]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 10 and Recitation 10, in our own wording; proofs written out in steps. -->

## Depth-first search

::: {#def-dfs .definition name="Depth-first search"}

*Depth-first search* (DFS) from $s$: set $P(s)$ empty and call $\mathrm{visit}(s)$, where $\mathrm{visit}(u)$ does the following: for each $v\in\operatorname{Adj}(u)$ that has no parent yet (and is not $s$), set $P(v)=u$ and call $\mathrm{visit}(v)$. When the loop ends, the visit of $u$ *finishes*.

:::

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

::: {#prp-connected-components-algorithm .proposition name="Connected components in linear time"}

For an undirected graph, Full-DFS (or Full-BFS) finds the connected components (@def-connected-graph-component): the vertices visited in one run form one component. So the components, and whether the graph is connected, can be found in $O(|V|+|E|)$ time.

:::

::: {.proof}

A run from $s$ visits exactly the vertices reachable from $s$ (@thm-dfs), which in an undirected graph is the component of $s$. A vertex visited in an earlier run lies in an earlier component, and a later run starts at an unvisited vertex, so each run produces a new component and every component is produced.

:::

## Topological sort and cycle detection

Recall that a DAG is a digraph with no directed cycle (@def-dag), and a *topological order* lists the vertices so that every edge goes forward (@thm-topological-sort). The *finishing order* of Full-DFS is the order in which the visits finish.

::: {#thm-dfs-topological-sort .theorem name="Topological sort by DFS"}

If $G$ is a DAG, the reverse of a finishing order of Full-DFS is a topological order. So a topological order can be found in $O(|V|+|E|)$ time.

:::

::: {.proof}

We show that for every edge $(u,v)$, the visit of $v$ finishes before the visit of $u$.

1. If $u$ is visited before $v$: while visiting $u$, the edge $(u,v)$ is examined, so $v$ is visited during the visit of $u$ (now or earlier in that visit) and therefore finishes before $u$ does.

2. If $v$ is visited before $u$: $u$ is not reachable from $v$, since otherwise the walk from $v$ to $u$ plus the edge $(u,v)$ would give a closed walk and hence a cycle. So $u$ is not visited during the visit of $v$, which finishes before $u$ is visited at all.

:::

::: {#fig-depth-first-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0.00,0.80) {$a$};
\node[small vertex] (b) at (1.50,0.80) {$b$};
\node[small vertex] (c) at (3.00,0.80) {$c$};
\node[small vertex] (d) at (0.00,-0.80) {$d$};
\node[small vertex] (e) at (1.50,-0.80) {$e$};
\node[small vertex] (f) at (3.00,-0.80) {$f$};
\draw[->] (a) --  (b);
\draw[->] (a) --  (d);
\draw[->] (b) --  (c);
\draw[->] (b) --  (e);
\draw[->] (d) --  (e);
\draw[->] (e) --  (f);
\draw[->] (c) --  (f);
\node[lab,tick] at (0.00,1.28) {1/12};
\node[lab,tick] at (1.50,1.28) {2/9};
\node[lab,tick] at (3.00,1.28) {3/6};
\node[lab,tick] at (0.00,-1.28) {10/11};
\node[lab,tick] at (1.50,-1.28) {7/8};
\node[lab,tick] at (3.00,-1.28) {4/5};
\node[small vertex] (ta) at (0.00,-2.6) {$a$};
\node[small vertex] (td) at (1.00,-2.6) {$d$};
\node[small vertex] (tb) at (2.00,-2.6) {$b$};
\node[small vertex] (te) at (3.00,-2.6) {$e$};
\node[small vertex] (tc) at (4.00,-2.6) {$c$};
\node[small vertex] (tf) at (5.00,-2.6) {$f$};
\draw[->] (ta) to[bend left=35] (tb);
\draw[->] (ta) to[bend left=35] (td);
\draw[->] (tb) to[bend left=35] (tc);
\draw[->] (tb) to[bend left=35] (te);
\draw[->] (td) to[bend left=35] (te);
\draw[->] (te) to[bend left=35] (tf);
\draw[->] (tc) to[bend left=35] (tf);
\node[lab, anchor=east] at (-0.5,-2.6) {reverse finish:};
\end{tikzpicture}
\end{center}
```

Full-DFS on a DAG, starting at $a$ and taking neighbours in alphabetical order; each vertex is labelled start/finish time. Listing the vertices by decreasing finish time gives a,d,b,e,c,f, and every edge then points to the right: a topological order.

:::

::: {#thm-dfs-cycle-detection .theorem name="Cycle detection"}

A digraph has a directed cycle if and only if, in the reverse finishing order of Full-DFS, some edge goes backwards. If $G$ has a cycle, Full-DFS examines an edge from a vertex to an ancestor of it in the DFS tree, and this edge with the tree path between them is a cycle. Both can be checked in $O(|V|+|E|)$ time.

:::

::: {.proof}

1. If there is no cycle, @thm-dfs-topological-sort shows that no edge goes backwards. If there is a cycle, no order puts all its edges forward, so some edge goes backwards.

2. Let $C=(v_0,v_1,\dots,v_k,v_0)$ be a cycle, named so that $v_0$ is the first vertex of $C$ that Full-DFS visits. All of $C$ is reachable from $v_0$ and unvisited when the visit of $v_0$ starts, so, as in the proof of @thm-dfs, all of $C$ is visited during the visit of $v_0$; in particular $v_k$ is, and $v_0$ is an ancestor of $v_k$ in the DFS tree.

3. While visiting $v_k$, DFS examines the edge $(v_k,v_0)$, whose head is an ancestor still being visited. Recording which vertices are currently being visited (the current DFS path) detects such an edge in $O(1)$ time, and the parent pointers from $v_k$ up to $v_0$ give the cycle.

:::
