::: {.problem #prob-mit6046s15-6-q1 origin="external" source="mit6046s15-6-q1"}
**Dynamic and Bounded-Hop All-Pairs Shortest Paths**

This problem explores some extensions of the All-Pairs Shortest Paths (APSP) algorithms covered in lecture and in CLRS. All parts of this problem assume nonnegative real weights. We assume that the vertices are numbered $1,2,\dots,n$.

Weighted directed graphs may be used to model communication networks, and shortest distances (shortest-path weights) between nodes may be used to suggest routes for messages. However, most communication networks are dynamic, i.e., the weights of edges may change over time. So it is useful to have a way of modifying distance estimates to reflect these changes.

(a) Give an efficient algorithm that, given a weighted directed graph $G=(V,E,W)$, a correct distance matrix $D$ for $G$, a corresponding predecessor matrix $\Pi$, and a triple $(i,j,r)$, where $i,j\in V$ and $r$ is a nonnegative real, modifies $D$ and $\Pi$ to reflect the effects of changing $w_{i,j}$ to $r$.

Your algorithm will need to handle three cases: $r=w_{i,j}$, $r<w_{i,j}$, and $r>w_{i,j}$. For each of the cases, analyze your algorithm. (Note: Your worst case running time for one of these cases may not be better than $O(V^3)$.)

(b) Give an example of a weighted directed graph $G=(V,E,W)$, a distance matrix $D$, and a triple $(i,j,r)$ such that any algorithm that modifies $D$ to reflect the effects of changing $w_{i,j}$ to $r$ must take $\Omega(V^2)$ time.

Now suppose that we add a new constraint to the problem — an upper bound of $h$ on the number of hops (edges) in the paths we want to consider. More formally, given a weighted digraph $G=(V,E,W)$ and a positive integer $h$, $0\le h\le n-1$, we would like to produce a distance matrix $D$ giving the shortest distances for at-most-$h$-hop paths.

(c) Adapt the Floyd-Warshall algorithm to solve the bounded-hop APSP problem. Analyze its complexity in terms of graph parameters and $h$.

(d) Adapt the matrix multiplication strategy from Section 25.1 to solve the bounded-hop APSP problem. Analyze its complexity in terms of graph parameters and $h$. Try to get logarithmic dependence on $h$.

(e) Finally, consider a dynamic version of the bounded-hop APSP problem. Design an algorithm that is given the following as input:

1. a weighted directed graph $G=(V,E,W)$;
2. a hop count $h$, $0\le h\le n-1$;
3. a correct distance matrix $D$ yielding shortest at-most-$h$-hop distances, and possibly additional distance information that is useful for solving this problem; and
4. a triple $(i,j,r)$, where $i,j\in V$ and $r$ is a nonnegative real.

Your algorithm should modify $D$ to reflect the effects of changing $w_{i,j}$ to $r$, and should also update any additional distance information that you have added. As for Part (a), your algorithm will need to handle three cases: $r=w_{i,j}$, $r<w_{i,j}$, and $r>w_{i,j}$. For each of the cases, analyze your algorithm's complexity, in terms of graph parameters and $h$.
:::
