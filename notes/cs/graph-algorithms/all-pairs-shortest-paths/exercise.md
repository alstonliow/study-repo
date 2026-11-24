::: {.problem #prob-mit6006s20-6-q6 origin="external" source="mit6006s20-6-q6"}
**Johnson's Algorithm**

In this problem, you will implement Johnson's Algorithm to compute all-pairs shortest-path weights in a general weighted directed graph $G$, as described in Lecture 14. The input to your algorithm will be: a positive integer $n$ representing the number of vertices of your graph identified by consecutive integers $0$ to $n-1$, and a tuple $S$ of triples, where each triple $(u,v,w)$ corresponds to a directed edge from vertex $u$ to $v$ of weight $w$. Your output should be a length-$n$ tuple $D$ of length-$n$ tuples where $D[u][v]=\delta(u,v)$ for all $u,v\in\{0,\dots,n-1\}$, except when the input graph contains a negative-weight cycle when you should return `None`.

Please implement the `johnson(n, S)` function in the template code provided. Your code template contains working implementations of Bellman–Ford and Dijkstra (using a binary heap as a priority queue) modified from the recitation notes. Note that you will have to construct your own adjacency list and weight function if you would like to use this code. You can download the code template and some test cases from the website.
:::

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

::: {.problem #prob-mit6046-11-q1 origin="external" source="mit6046-11-q1"}
Bellman-Ford consult any system of difference constraints (or report that it is unsolvable) in $O(VE)$ time where $V$ = variables and $E$ = constraints. An exercise is to prove the Bellman-Ford minimizes $\max_i x_i-\min_i x_i$.

*Note (these notes):* A system of difference constraints asks for reals $x_1,\dots,x_n$ with $x_j-x_i\le b_{ij}$ for given pairs $(i,j)$. Build a graph with a vertex per variable and an edge $i\to j$ of weight $b_{ij}$ per constraint. Add a new vertex $s$ with an edge of weight $0$ to every variable, as in Johnson's algorithm (@def-johnson). Run Bellman–Ford (@thm-bellman-ford) from $s$: a negative cycle means no solution, and otherwise $x_i=\delta(s,i)$ is a solution.
:::
