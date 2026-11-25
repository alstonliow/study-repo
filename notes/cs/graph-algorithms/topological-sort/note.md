---
title: "Topological Sort and Cycle Detection"
sources: [mit6006-10, mit6006r-10]
requires: [cs/graph-algorithms/depth-first-search]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 10 and Recitation 10, in our own wording; proofs written out in steps. Split from cs/graph-algorithms/depth-first-search on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Recall that a DAG is a digraph with no directed cycle (@def-dag), and a *topological order* lists the vertices so that every edge goes forward (@thm-topological-sort). The *finishing order* of Full-DFS is the order in which the visits finish.

::: {#thm-dfs-topological-sort .theorem name="Topological sort by DFS"}

If $G$ is a DAG, the reverse of a finishing order of Full-DFS is a topological order. So a topological order can be found in $O(|V|+|E|)$ time.

:::

::: {.proof}

We show that for every edge $(u,v)$, the visit of $v$ finishes before the visit of $u$.

1. If $u$ is visited before $v$: while visiting $u$, the edge $(u,v)$ is examined, so $v$ is visited during the visit of $u$ (now or earlier in that visit) and therefore finishes before $u$ does.

2. If $v$ is visited before $u$: $u$ is not reachable from $v$, since otherwise the walk from $v$ to $u$ plus the edge $(u,v)$ would give a closed walk and hence a cycle. So $u$ is not visited during the visit of $v$, which finishes before $u$ is visited at all.

:::

```{=latex}
\begin{algorithm}
\caption{Topological sort by DFS}
\begin{algorithmic}
\INPUT DAG $G=(V,E)$ as adjacency lists
\OUTPUT The vertices in a topological order
\STATE run Full-DFS on $G$, recording the finishing order $F$
\RETURN $F$ reversed
\end{algorithmic}
\end{algorithm}
```

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

```{=latex}
\begin{algorithm}
\caption{Cycle detection: $\mathrm{visit}(u)$ in Full-DFS}
\begin{algorithmic}
\INPUT Digraph $G=(V,E)$ as adjacency lists, a vertex $u$; the set $A$ of vertices whose visit is in progress
\COMMENT{Full-DFS calls this visit; if it never returns a cycle, $G$ has none}
\STATE add $u$ to $A$
\FOR{$v\in\operatorname{Adj}(u)$}
    \IF{$v\in A$}
        \RETURN the cycle: parent pointers from $u$ back to $v$, reversed, then the edge $(u,v)$
    \ELSIF{$P(v)$ is not set}
        \STATE $P(v)\gets u$; $\mathrm{visit}(v)$
    \ENDIF
\ENDFOR
\STATE remove $u$ from $A$ \COMMENT{the visit of $u$ finishes}
\end{algorithmic}
\end{algorithm}
```

::: {#fig-depth-first-search-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight, draw=accent] (a) at (0.00,0.80) {$a$};
\node[small vertex, fill=accentLight, draw=accent] (b) at (1.50,0.80) {$b$};
\node[small vertex, fill=accentLight, draw=accent] (c) at (3.00,0.80) {$c$};
\node[small vertex] (d) at (0.00,-0.80) {$d$};
\node[small vertex] (e) at (1.50,-0.80) {$e$};
\node[small vertex, fill=accentLight, draw=accent] (f) at (3.00,-0.80) {$f$};
\draw[->, hl] (a) -- (b);
\draw[->, faint] (a) -- (d);
\draw[->, hl] (b) -- (c);
\draw[->, faint] (b) -- (e);
\draw[->, faint] (d) -- (e);
\draw[->, faint] (e) -- (f);
\draw[->, hl] (c) -- (f);
\draw[->, hl, dashed] (f) -- (b);
\end{tikzpicture}
\end{center}
```

The DAG of @fig-depth-first-search-1 with an extra edge $f\to b$. Full-DFS from $a$ (alphabetical) is visiting $a,b,c,f$ (highlighted, the set $A$) when it examines $f\to b$ (dashed). Since $b\in A$, the tree path $b,c,f$ and the edge $f\to b$ form the cycle $b,c,f,b$.

:::
