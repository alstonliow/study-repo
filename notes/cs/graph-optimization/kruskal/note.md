---
title: "Kruskal's Algorithm"
sources: [mit6046-12]
requires: [cs/graph-optimization/minimum-spanning-trees, cs/advanced-data-structures/union-find]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 12, in our own wording; proofs written out in steps. This note proves Kruskal's algorithm correct (@thm-cn-thm-70 states it without proof). Split from cs/graph-optimization/minimum-spanning-trees on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Kruskal's algorithm builds an MST (@def-minimum-spanning-tree) as a forest that grows by the lightest edge joining two of its trees; each choice is justified by the cut property (@thm-cut-property).

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
