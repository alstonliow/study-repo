<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-graph-2-09 origin="external" source="fit1058-cn-12.7-q9"}
Prove that $K_{2,n}$ is planar for all $n$.
:::

::: {.problem #prob-graph-2-10 origin="external" source="fit1058-cn-12.7-q10"}
Check that Euler’s Theorem ($n-m+f=2$) holds for the following graphs:

(a) the cycle $C_n$;

(b) the wheel graph $W_n$, obtained from $C_n$ (the “rim”) by adding
    a new vertex (the “hub”) adjacent (via “spokes”) to every vertex
    of $C_n$;

(c) $K_4$;

(d) the cube $Q_3$ (Exercise 11.11);

(e) the octahedron;

(f) the dodecahedron;

(g) the icosahedron.
:::

::: {.problem #prob-graph-2-11 origin="external" source="fit1058-cn-12.7-q11"}
(a) Give an upper bound on the average degree of a planar graph.

(b) Give an upper bound on the average degree of a planar graph with no
    triangles.

(c) Give an upper bound on the average degree of a bipartite planar
    graph.
:::

::: {.problem #prob-graph-2-12 origin="external" source="fit1058-cn-12.7-q12"}
Prove that every planar graph has a vertex of degree $\le5$.
:::

::: {.problem #prob-cs70hw-3-q4 origin="external" source="cs70hw-3-q4"}
**Planarity.**

(a) Prove that $K_{3,3}$ is nonplanar.

(b) Consider graphs with the property $T$: For every three distinct vertices $v_1, v_2, v_3$ of graph $G$, there are at least two edges among them. Use a proof by contradiction to show that if $G$ is a graph on $\ge 7$ vertices, and $G$ has property $T$, then $G$ is nonplanar.
:::

::: {.problem #prob-cs70hw-3-q5 origin="external" source="cs70hw-3-q5"}
**Always, Sometimes, or Never.** In each part below, you are given some information about the so-called original graph, $OG$. Using only the information in the current part, say whether $OG$ will always be planar, always be non-planar, or could be either. If you think it is always planar or always non-planar, prove it. If you think it could be either, give a planar example and a non-planar example.

(a) $OG$ can be vertex-colored with 4 colors.

(b) $OG$ requires 7 colors to be vertex-colored.

(c) $e \le 3v - 6$, where $e$ is the number of edges of $OG$ and $v$ is the number of vertices of $OG$.

(d) $OG$ is connected, and each vertex in $OG$ has degree at most 2.

(e) Each vertex in $OG$ has degree at most 2.

*Note (these notes):* (b) uses the four colour theorem, which these notes state but do not prove.
:::
