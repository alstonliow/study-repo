<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-graph-1-05 origin="external" source="fit1058-cn-11.12-q5"}
Prove that the shortest walk between two vertices is always a path.
:::

::: {.problem #prob-graph-1-06 origin="external" source="fit1058-cn-11.12-q6"}
Prove that every graph with minimum degree at least 2 has a cycle.
:::

::: {.problem #prob-graph-1-07 origin="external" source="fit1058-cn-11.12-q7"}
Prove that graph distance satisfies the triangle inequality: for all vertices
$u,v,w$ of any graph $G$,
$$d_G(u,w)\le d_G(u,v)+d_G(v,w).$$
:::

::: {.problem #prob-cs70hw-3-q1 origin="external" source="cs70hw-3-q1"}
**Graph Basics.** In the first few parts, you will be answering questions on the following graph $G$.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.6cm,y=1.3cm]
\node[small vertex] (A) at (0,2) {$A$};
\node[small vertex] (B) at (1,2) {$B$};
\node[small vertex] (C) at (2,2) {$C$};
\node[small vertex] (E) at (1,1) {$E$};
\node[small vertex] (D) at (2,1) {$D$};
\node[small vertex] (F) at (0,0) {$F$};
\node[small vertex] (G) at (1,0) {$G$};
\node[small vertex] (H) at (2,0) {$H$};
\draw[->] (A) -- (B); \draw[->] (B) -- (C); \draw[->] (A) -- (F); \draw[->] (B) -- (E);
\draw[->] (C) -- (D); \draw[->] (D) -- (B); \draw[->] (E) -- (D); \draw[->] (D) -- (H);
\draw[->] (H) -- (G); \draw[->] (E) -- (G); \draw[->] (F) -- (E);
\draw[->] (F) to[bend left=25] (G); \draw[->] (G) to[bend left=25] (F);
\end{tikzpicture}
\end{center}
```

(a) What are the vertex and edge sets $V$ and $E$ for graph $G$?

(b) Which vertex has the highest in-degree? Which vertex has the lowest in-degree? Which vertices have the same in-degree and out-degree?

(c) What are the paths from vertex $B$ to $F$, assuming no vertex is visited twice? Which one is the shortest path?

(d) Which of the following are cycles in $G$?

  i. $(B,C), (C,D), (D,B)$
  ii. $(F,G), (G,F)$
  iii. $(A,B), (B,C), (C,D), (D,B)$
  iv. $(B,C), (C,D), (D,H), (H,G), (G,F), (F,E), (E,D), (D,B)$

(e) Which of the following are walks in $G$?

  i. $(E,G)$
  ii. $(E,G), (G,F)$
  iii. $(F,G), (G,F)$
  iv. $(A,B), (B,C), (C,D), (H,G)$
  v. $(E,G), (G,F), (F,G), (G,C)$
  vi. $(E,D), (D,B), (B,E), (E,D), (D,H), (H,G), (G,F)$

(f) Which of the following are tours in $G$?

  i. $(E,G)$
  ii. $(E,G), (G,F)$
  iii. $(F,G), (G,F)$
  iv. $(E,D), (D,B), (B,E), (E,D), (D,H), (H,G), (G,F)$

In the following three parts, let's consider a general undirected graph $G$ with $n$ vertices ($n \ge 3$).

(g) True/False: If each vertex of $G$ has degree at most 1, then $G$ does not have a cycle.

(h) True/False: If each vertex of $G$ has degree at least 2, then $G$ has a cycle.

(i) True/False: If each vertex of $G$ has degree at most 2, then $G$ is not connected.

*Note (these notes):* The figure is redrawn from the original.
:::
