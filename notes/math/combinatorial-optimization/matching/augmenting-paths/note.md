---
title: "Augmenting Paths"
sources: [mit18433-1]
requires: [math/discrete/graph/bipartite-graphs]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on bipartite matching (Section 1.1, augmenting paths and the cardinality algorithm), in our own wording; example our own (checked by computation); proofs written out in steps. The flow-based algorithm for the same problem is @thm-matching-by-flow. -->

A matching (@def-matching) is a set $M$ of edges no two of which share an end. A vertex not covered by $M$ is *exposed*; $M$ is *perfect* if no vertex is exposed. The *maximum cardinality matching problem* asks for a matching of largest size. Adding edges greedily until none fits gives a *maximal* matching, which need not be maximum; the fix is to change the matching along a path.

::: {#def-augmenting-path .definition name="Alternating and augmenting paths"}

Let $M$ be a matching in a graph $G$. An *alternating path* is a path whose edges lie alternately in $M$ and outside $M$. An *augmenting path* is an alternating path whose two end vertices are both exposed.

:::

An augmenting path $P$ with $k$ edges of $M$ has $k+1$ edges outside $M$, so the symmetric difference $M\triangle P=(M\setminus P)\cup(P\setminus M)$ is again a matching, with one more edge: every inner vertex of $P$ swaps its matching edge, and the two exposed ends become covered. We say we *augment* $M$ along $P$.

::: {#thm-berge-augmenting-path .theorem name="Berge's theorem"}

A matching $M$ in any graph is maximum if and only if there is no augmenting path with respect to $M$.

:::

::: {.proof}

1. If $P$ is an augmenting path, $M\triangle P$ is a larger matching, so $M$ is not maximum.

2. Conversely, suppose $M$ is not maximum and let $M^*$ be a maximum matching, $|M^*|>|M|$. Put $Q=M\triangle M^*$.

3. Every vertex is an end of at most one edge of $M$ and at most one of $M^*$, so it has degree at most $2$ in $Q$. Hence $Q$ is a disjoint union of paths and cycles, whose edges alternate between $M$ and $M^*$.

4. An alternating cycle has even length and as many edges of $M$ as of $M^*$. Since $|M^*\setminus M|>|M\setminus M^*|$, some path component has more edges of $M^*$ than of $M$; it then starts and ends with edges of $M^*$.

5. Its two ends are not covered by $M$ (an $M$-edge at an end would continue the path in $Q$, or would be an edge of $M\cap M^*$, which the end's $M^*$-edge excludes). So this path is augmenting for $M$.

:::

In a bipartite graph with sides $A$ and $B$, an augmenting path has an odd number of edges, so its ends lie on different sides. Searching for one becomes a search in a directed graph.

::: {#prp-augmenting-path-search .proposition name="Finding an augmenting path in a bipartite graph"}

Let $G$ be bipartite with sides $A$, $B$ and let $M$ be a matching. Orient every edge not in $M$ from $A$ to $B$ and every edge of $M$ from $B$ to $A$; call the result $D$. Then $G$ has an augmenting path for $M$ if and only if $D$ has a directed path from an exposed vertex of $A$ to an exposed vertex of $B$. Such a path can be found in $O(|E|)$ time.

:::

The proof is an exercise. For the time bound, add a source joined to all exposed vertices of $A$ and run a depth-first (or breadth-first) search until an exposed vertex of $B$ is reached.

::: {#def-bipartite-augmenting-algorithm .definition name="Augmenting path algorithm for bipartite matching"}

Start with any matching, for example $M=\varnothing$. While the search of @prp-augmenting-path-search finds an augmenting path $P$, replace $M$ by $M\triangle P$. When no path is found, return $M$.

:::

```{=latex}
\begin{algorithm}
\caption{Maximum bipartite matching by augmenting paths}
\begin{algorithmic}
\INPUT bipartite graph $G=(A\cup B,E)$
\OUTPUT a maximum matching $M$
\STATE $M\gets\varnothing$
\LOOP
\STATE orient $E\setminus M$ from $A$ to $B$ and $M$ from $B$ to $A$
\STATE search from the exposed vertices of $A$
\IF{no exposed vertex of $B$ is reached} \RETURN $M$ \ENDIF
\STATE $P\gets$ the path found; $M\gets M\triangle P$
\ENDLOOP
\end{algorithmic}
\end{algorithm}
```

::: {#thm-bipartite-augmenting-algorithm .theorem name="Correctness and running time"}

The algorithm returns a maximum matching after at most $\nu\le|V|/2$ augmentations, where $\nu$ is the maximum size of a matching, so it runs in $O(|V||E|)$ time.

:::

::: {.proof}

1. When the algorithm stops there is no augmenting path (@prp-augmenting-path-search), so $M$ is maximum by @thm-berge-augmenting-path.

2. Each augmentation increases $|M|$ by one and $|M|\le\nu\le|V|/2$; each search takes $O(|E|)$ time.

:::

Augmenting along many shortest augmenting paths at once (Hopcroft–Karp) improves the time to $O(\sqrt{|V|}\,|E|)$.

::: {#exm-augmenting-path-small .example name="One augmentation"}

Let $A=\{1,2,3\}$, $B=\{4,5,6\}$ and $E=\{14,15,24,35,36\}$, with $M=\{14,35\}$. The exposed vertices are $2$ and $6$. In $D$ the path $2\to4\to1\to5\to3\to6$ uses non-matching edges forwards and matching edges backwards, so $2$–$4$–$1$–$5$–$3$–$6$ is augmenting. Augmenting gives $M\triangle P=\{24,15,36\}$, a perfect matching.

:::

::: {#fig-augmenting-paths-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (na1) at (0,1.2) {$1$};
\node[small vertex] (na2) at (0,0.6) {$2$};
\node[small vertex] (na3) at (0,0) {$3$};
\node[small vertex] (na4) at (1.6,1.2) {$4$};
\node[small vertex] (na5) at (1.6,0.6) {$5$};
\node[small vertex] (na6) at (1.6,0) {$6$};
\draw[bold] (na1) -- (na4);
\draw[hl] (na1) -- (na5);
\draw[hl] (na2) -- (na4);
\draw[bold] (na3) -- (na5);
\draw[hl] (na3) -- (na6);
\node[lab] at (0.8,-0.6) {$M$ and path $P$};
\node[small vertex] (nb1) at (3.2,1.2) {$1$};
\node[small vertex] (nb2) at (3.2,0.6) {$2$};
\node[small vertex] (nb3) at (3.2,0) {$3$};
\node[small vertex] (nb4) at (4.80,1.2) {$4$};
\node[small vertex] (nb5) at (4.80,0.6) {$5$};
\node[small vertex] (nb6) at (4.80,0) {$6$};
\draw[faint] (nb1) -- (nb4);
\draw[bold] (nb1) -- (nb5);
\draw[bold] (nb2) -- (nb4);
\draw[faint] (nb3) -- (nb5);
\draw[bold] (nb3) -- (nb6);
\node[lab] at (4.0,-0.6) {$M\triangle P$};
\end{tikzpicture}
\end{center}
```

Left: the matching $M=\{14,35\}$ and the augmenting path $2$–$4$–$1$–$5$–$3$–$6$ (here every edge of the graph; matching edges thick, the others highlighted). Right: after augmenting, the thick edges $\{24,15,36\}$ form a perfect matching.

:::

::: {#rmk-augmenting-paths-1 .remark name="General graphs"}

Berge's theorem holds in every graph, but in a non-bipartite graph the directed search can be fooled by odd cycles: a walk may return to a vertex it has already used. Edmonds' blossom algorithm (@sec-math-combinatorial-optimization-matching-blossom-algorithm) repairs this by shrinking odd cycles.

:::
