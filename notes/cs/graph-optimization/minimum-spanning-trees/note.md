---
title: "Minimum Spanning Trees: Prim and Kruskal"
sources: [mit6046-12]
requires: [cs/graph-algorithms/dijkstra, cs/advanced-data-structures/union-find, math/discrete/graph/forests-and-spanning-trees]
aliases: [cs/graph-algorithms/minimum-spanning-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 12, in our own wording; proofs written out in steps. The definition is @def-minimum-spanning-tree; this note proves Kruskal's algorithm correct (@thm-cn-thm-70 states it without proof) and adds Prim's. -->

Let $G=(V,E)$ be a connected undirected graph with edge weights $w$. A *minimum spanning tree* (MST) is a spanning tree (@def-spanning-tree) of least total weight (@def-minimum-spanning-tree). Both classical algorithms are greedy, and both are justified by one property of cuts.

::: {#def-cut-respect .definition name="Cut, crossing edge"}

A *cut* $(S,V\setminus S)$ is a split of the vertices into two non-empty parts. An edge *crosses* the cut if it has one end in each part. A cut *respects* a set $A$ of edges if no edge of $A$ crosses it.

:::

::: {#thm-cut-property .theorem name="Cut property"}

Let $A$ be a set of edges contained in some MST, let $(S,V\setminus S)$ be a cut that respects $A$, and let $e$ be a lightest edge crossing the cut. Then $A\cup\{e\}$ is contained in some MST.

:::

::: {.proof}

1. Let $T$ be an MST containing $A$. If $e\in T$ we are done; otherwise add $e=\{u,v\}$ to $T$, which creates exactly one cycle (@sec-math-discrete-graph-trees).

2. The cycle crosses the cut at $e$, and since it returns to its start it crosses the cut again at some other edge $e'$ of $T$. As the cut respects $A$, $e'\notin A$.

3. $T'=T-e'+e$ is again a spanning tree (removing $e'$ breaks the only cycle), it contains $A\cup\{e\}$, and $w(T')=w(T)-w(e')+w(e)\le w(T)$ because $e$ is a lightest crossing edge.

4. So $T'$ is an MST containing $A\cup\{e\}$.

:::

## Prim's algorithm

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

## Kruskal's algorithm

::: {#def-kruskal .definition name="Kruskal's algorithm"}

Sort the edges by weight. Start with every vertex in its own component (a union-find structure, @def-union-find). For each edge $\{u,v\}$ in order: if `find(u)` $\ne$ `find(v)`, add the edge and `union(u, v)`; otherwise skip it (it would close a cycle).

:::

```{=latex}
\begin{algorithm}
\caption{Kruskal's algorithm}
\begin{algorithmic}
\INPUT Connected weighted graph $G=(V,E,w)$
\OUTPUT A minimum spanning tree $T$
\STATE sort $E$ by weight
\STATE $T\gets\emptyset$; make a union-find structure with each vertex in its own set
\FOR{$\{u,v\}\in E$ in order of weight}
    \IF{$\mathrm{find}(u)\ne\mathrm{find}(v)$}
        \STATE $T\gets T\cup\{\{u,v\}\}$
        \STATE $\mathrm{union}(u,v)$
    \ENDIF
\ENDFOR
\RETURN $T$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-kruskal .theorem name="Kruskal's algorithm" related="thm-cn-thm-70"}

Kruskal's algorithm returns an MST in $O(|E|\log|V|)$ time.

:::

::: {.proof}

1. When an edge $e=\{u,v\}$ is added, let $S$ be the component of $u$ in the forest built so far. The cut $(S,V\setminus S)$ respects the chosen edges, and $e$ crosses it. Every lighter edge was already examined and either added or skipped, and neither kind crosses this cut (added edges lie inside components; a skipped edge joined two vertices of one component). So $e$ is a lightest crossing edge, and @thm-cut-property applies.

2. By induction the chosen edges always lie in some MST; at the end they connect $G$, so they form an MST.

3. Sorting takes $O(|E|\log|E|)=O(|E|\log|V|)$, and the $O(|E|)$ union-find operations take $O(|E|\,\alpha(|V|))$ (@thm-union-find-ackermann).

:::

::: {#fig-minimum-spanning-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0,1) {$a$};
\node[small vertex] (b) at (2,1.6) {$b$};
\node[small vertex] (c) at (4,1) {$c$};
\node[small vertex] (d) at (0.6,-0.6) {$d$};
\node[small vertex] (e) at (2.4,-0.2) {$e$};
\node[small vertex] (f) at (4,-0.8) {$f$};
\draw[hl] (a) -- node[edge label] {$4$} (b);
\draw[hl] (a) -- node[edge label] {$2$} (d);
\draw[faint] (b) -- node[edge label] {$6$} (c);
\draw[hl] (b) -- node[edge label] {$3$} (e);
\draw[faint] (d) -- node[edge label] {$5$} (e);
\draw[hl] (c) -- node[edge label] {$4$} (e);
\draw[hl] (c) -- node[edge label] {$3$} (f);
\draw[faint] (e) -- node[edge label] {$7$} (f);
\draw[faint] (a) -- node[edge label] {$8$} (e);
\draw[faint] (b) -- node[edge label] {$9$} (d);
\end{tikzpicture}
\end{center}
```

Kruskal's algorithm takes the edges in order of weight, $2,3,3,4,4,\dots$, and keeps an edge unless its ends are already connected. The highlighted edges form the minimum spanning tree, of weight $16$; the edge of weight $5$ is skipped because $d$ and $e$ are already joined through $a$ and $b$.

:::

::: {#rmk-minimum-spanning-trees-greedy .remark name="Greedy choice and optimal substructure"}

The cut property is the "greedy choice" property, and contracting the chosen edge leaves a smaller MST problem ("optimal substructure"). The same structure, a *matroid*, is what makes greedy algorithms work in general. With negative weights nothing changes: only the order of the weights matters.

:::
