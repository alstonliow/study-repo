---
title: "Prim's Algorithm"
sources: [mit6046-12]
requires: [cs/graph-optimization/minimum-spanning-trees, cs/graph-algorithms/dijkstra]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 12, in our own wording; proofs written out in steps. Split from cs/graph-optimization/minimum-spanning-trees on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Prim's algorithm builds an MST (@def-minimum-spanning-tree) as one tree grown from a start vertex, adding the lightest edge that leaves it; each choice is justified by the cut property (@thm-cut-property).

::: {#def-prim .definition name="Prim's algorithm"}

Grow one tree from a start vertex $s$. Keep every vertex $v$ not yet in the tree in a min-priority queue with key $d(v)$, the weight of the lightest edge from $v$ to the tree ($\infty$ if none). Repeatedly remove the vertex $u$ with the smallest key, add it to the tree with its lightest edge, and for each neighbour $v$ still in the queue, lower $d(v)$ to $w(u,v)$ if that is smaller.

:::

```{=latex}
\begin{algorithm}
\caption{Prim's algorithm}
\begin{algorithmic}
\INPUT Connected weighted graph $G=(V,E,w)$, start vertex $s$
\OUTPUT A minimum spanning tree, as parent pointers $P$
\STATE $d(s)\gets0$; $d(v)\gets\infty$ for every $v\ne s$; $P(v)\gets$ none for every $v$
\STATE $Q\gets$ changeable priority queue of $V$ keyed by $d$
\WHILE{$Q$ is not empty}
    \STATE $u\gets Q.\mathrm{delete\_min}()$ \COMMENT{add $u$ and the edge $\{P(u),u\}$ to the tree}
    \FOR{$v\in\operatorname{Adj}(u)$}
        \IF{$v\in Q$ and $w(u,v)<d(v)$}
            \STATE $d(v)\gets w(u,v)$; $P(v)\gets u$
            \STATE $Q.\mathrm{decrease\_key}(v,d(v))$
        \ENDIF
    \ENDFOR
\ENDWHILE
\RETURN $P$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-minimum-spanning-trees-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0.00,1.00) {$a$};
\node[small vertex] (b) at (2.00,1.60) {$b$};
\node[small vertex] (c) at (4.00,1.00) {$c$};
\node[small vertex] (d) at (0.60,-0.60) {$d$};
\node[small vertex] (e) at (2.40,-0.20) {$e$};
\node[small vertex] (f) at (4.00,-0.80) {$f$};
\draw[hl] (a) -- node[edge label, pos=0.5] {$4$} (b);
\draw[hl] (a) -- node[edge label, pos=0.5] {$2$} (d);
\draw[faint] (b) -- node[edge label, pos=0.5] {$6$} (c);
\draw[hl] (b) -- node[edge label, pos=0.5] {$3$} (e);
\draw[faint] (d) -- node[edge label, pos=0.5] {$5$} (e);
\draw[hl] (c) -- node[edge label, pos=0.5] {$4$} (e);
\draw[hl] (c) -- node[edge label, pos=0.5] {$3$} (f);
\draw[faint] (e) -- node[edge label, pos=0.5] {$7$} (f);
\draw[faint] (a) -- node[edge label, pos=0.5] {$8$} (e);
\draw[faint] (b) -- node[edge label, pos=0.5] {$9$} (d);
\node[lab,tick] at (-0.45,1.00) {1};
\node[lab,tick] at (0.15,-0.60) {2};
\node[lab,tick] at (2.00,2.02) {3};
\node[lab,tick] at (2.45,-0.62) {4};
\node[lab,tick] at (4.45,1.00) {5};
\node[lab,tick] at (4.45,-0.80) {6};
\end{tikzpicture}
\end{center}
```

Prim's algorithm from $a$ on the graph of @fig-minimum-spanning-trees-1. Small numbers give the order in which vertices leave the queue, with the key at that moment: $a, d\,(2), b\,(4), e\,(3), c\,(4), f\,(3)$. Each key is the weight of the highlighted edge that joins the vertex to the tree, so the tree is the same as Kruskal's, of weight $16$. The key of $e$ drops from $8$ to $5$ to $3$ before $e$ is removed.

:::

::: {#thm-prim .theorem name="Prim's algorithm"}

Prim's algorithm returns an MST. With a binary heap it runs in $O(|E|\log|V|)$ time, and with a Fibonacci heap (@sec-cs-advanced-data-structures-fibonacci-heaps) in $O(|E|+|V|\log|V|)$.

:::

::: {.proof}

1. At each step, the cut $(T,V\setminus T)$ between the tree's vertices and the rest respects the edges chosen so far, and the edge added is a lightest edge crossing it (that is what the keys record). By @thm-cut-property and induction, the chosen edges always lie in some MST, and after $|V|-1$ steps they form one.

2. The operations are those of Dijkstra's algorithm (@prp-dijkstra-time): $|V|$ `delete_min`s and at most $|E|$ `decrease_key`s.

:::
