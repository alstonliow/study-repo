<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-1-q1" status="draft"}
1. Let $P=v_0v_1\dots v_k$ be augmenting. Its ends lie on different sides, so number it with $v_0\in A$. As $v_0$ is exposed, $v_0v_1\notin M$; the edges then alternate, so $v_{i-1}v_i\notin M$ for odd $i$ and $\in M$ for even $i$. For odd $i$, $v_{i-1}\in A$ and the edge is directed $A\to B$, that is $v_{i-1}\to v_i$; for even $i$, $v_{i-1}\in B$ and the matching edge is directed $B\to A$, again $v_{i-1}\to v_i$. So $P$ is a directed path in $D$ from the exposed $v_0\in A$ to the exposed $v_k\in B$.

2. Conversely, let $Q$ be a directed path in $D$ from an exposed $a\in A$ to an exposed $b\in B$. Arcs leave $A$ only along non-matching edges and leave $B$ only along matching edges, and $Q$ alternates between the sides, so its edges alternate between $E\setminus M$ and $M$. Its vertices are distinct and its ends exposed, so it is an augmenting path in $G$.
:::

::: {.solution for="prob-mit18433-1-q3" status="draft"}
1. Every edge $e$ of $M^*$ has an end covered by $M$: otherwise $M+e$ would be a matching, contradicting maximality of $M$.

2. $M$ covers $2|M|$ vertices, and each covered vertex is an end of at most one edge of $M^*$, because $M^*$ is a matching.

3. So the map sending each edge of $M^*$ to one of its $M$-covered ends is injective into a set of $2|M|$ vertices, and $|M^*|\le2|M|$.
:::

::: {.solution for="prob-mit18433-1-q5" status="draft"}
1. Consider the multigraph $H$ with the edges of $M_A$ and of $M_B$ (an edge in both appears twice). Every vertex has degree at most $2$, so each component of $H$ is a path, an even cycle (alternating between $M_A$ and $M_B$), or a doubled edge. We choose a matching inside each component; together they form a matching of $G$.

2. In a cycle or doubled edge, take its $M_A$ edges: they cover all its vertices.

3. Let a component be a path with ends $x,y$. Each end has a single edge of $H$. If $x\in A_1$, its edge is from $M_A$ (since $M_A$ covers $x$); if $x\in B_1$, its edge is from $M_B$. Every inner vertex has one edge of each kind, so it is covered whichever kind we take.

4. *Odd number of edges.* The two end edges are of the same kind; take all edges of that kind. They cover the whole path.

5. *Even number of edges.* The end edges are of different kinds, say $x$ has an $M_A$ edge and $y$ an $M_B$ edge, and $x,y$ lie on the same side. If both are in $A$, then $y\notin A_1$ (its only edge is not in $M_A$) and $y\notin B_1$; take the $M_A$ edges, which cover all vertices but $y$. If both are in $B$, then $x\notin B_1$ and $x\notin A_1$; take the $M_B$ edges, which cover all vertices but $x$.

6. In every case all vertices of $A_1\cup B_1$ in the component are covered, which proves the claim.
:::

::: {.solution for="prob-mit18433-1-q6" status="draft"}
Fix a perfect matching $M$; for a vertex $z$ let $z'$ be its partner in $M$.

1. *Strategy.* Player 1 starts with any edge of $M$. Afterwards, when player 2 extends the path by an edge $wz$ at an end $w$, the new end $z$ was not on the path; player 1 answers with $zz'$.

2. *Invariant.* After each move of player 1, the vertex set of the path is a union of pairs $\{z,z'\}$. This holds after the first move, and if it holds before player 2 moves, the new vertex $z$ is off the path, so $z'$ is off the path too (the path's vertices are paired among themselves). Then $zz'$ extends the path at $z$ to a longer simple path, and the invariant holds again.

3. So player 1 can always move. The game is finite (each move uses a new edge), so player 2 is the first who cannot move, and loses.
:::
