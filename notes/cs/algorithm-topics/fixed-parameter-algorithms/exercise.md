::: {.problem #prob-mit6046s15-9-q2 origin="external" source="mit6046s15-9-q2"}
**Fixed-Parameter Algorithms**

We consider the Tournament Edge Reversal problem. Define a tournament to be a directed graph $T=(V,E)$ such that, for every pair of vertices $u,v\in V$, exactly one of $(u,v)$ and $(v,u)$ is in $E$. Furthermore, define a cycle cover to be a set $A\subset E$ of directed edges of a tournament $T$ such that, every directed cycle of $T$ contains at least one edge from $A$.

(a) Let a minimal cycle cover of $T$ be a cycle cover with the least number of edges. Prove that reversing all the edges of a minimal cycle cover $A$ turns $T$ into an acyclic tournament. (Hint: Any edge $e\in A$ must be the only edge in $A$ on some directed cycle of $T$.)

In the Tournament Edge Reversal problem, we are given a tournament $T$ and a positive integer $k$, and the objective is to decide whether $T$ has a cycle cover of size at most $k$.

(b) Show that this problem has a kernel with at most $k^2+2k$ vertices. (Hint: Define a triangle to be a directed cycle of length 3. Consider the number of times that a node or an edge appears in different triangles.)

(c) Obtain a FPT algorithm for the Tournament Edge Reversal problem.
:::
