<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-1-q2" status="draft"}
1. *$|R^*|\le|V|-|M^*|$.* Start from a maximum matching $M^*$; it leaves $|V|-2|M^*|$ vertices exposed. Add for each exposed vertex one edge at it (one exists, as there is no isolated vertex). The result is an edge cover with $|M^*|+|V|-2|M^*|=|V|-|M^*|$ edges.

2. *$|R^*|\ge|V|-|M^*|$.* Let $R$ be a minimum edge cover. If an edge $uv\in R$ had both $u$ and $v$ covered by other edges of $R$, deleting it would give a smaller cover. So every edge of $R$ has an end of degree $1$ in $(V,R)$. Hence $(V,R)$ has no cycle and no path with $3$ edges (the middle edge would have both ends of degree $\ge2$): every component is a star.

3. A forest of $c$ stars on the vertex set $V$ has $|V|-c$ edges, and one edge from each star gives a matching of size $c$. So $|M^*|\ge c=|V|-|R|$.

4. *Algorithm.* Find a maximum matching (augmenting paths, @thm-bipartite-augmenting-algorithm, $O(|V||E|)$), then add one edge at each exposed vertex, as in step 1.

5. *Non-bipartite graphs.* Yes: steps 1–3 never used bipartiteness (this is Gallai's identity). The algorithm is the same with a maximum matching found by Edmonds' algorithm (@def-blossom-algorithm).
:::

::: {.solution for="prob-mit18433-1-q4" status="draft"}
1. Make a vertex for each square and an edge for each pair of squares sharing a side. Colour the squares as on a chessboard: a square in row $i$ and column $j$ is *dark* if $i+j$ is even. Adjacent squares have different colours, so the graph is bipartite with the dark and the light squares as sides. A domino covers two adjacent squares, i.e. an edge, and a tiling covers every square exactly once: tilings are exactly the perfect matchings.

2. No tiling exists, although the figure has $21$ dark and $21$ light squares. Consider the $11$ dark squares
$$S=\{(1,3),(2,2),(2,4),(3,1),(3,3),(3,5),(4,2),(4,4),(5,1),(5,3),(6,2)\}$$
(row, column), the dark squares of the upper-left part with $i+j\le8$. Their neighbours in the figure are the $10$ light squares
$$N(S)=\{(1,4),(2,3),(3,2),(3,4),(4,1),(4,3),(4,5),(5,2),(5,4),(6,3)\}.$$
(For instance $(3,5)$ has no square to its right or above it.) Since $|N(S)|<|S|$, the squares of $S$ cannot all be paired with distinct neighbours, so by Hall's condition (@sec-math-discrete-graph-bipartite-graphs) there is no perfect matching. A maximum matching computed by augmenting paths indeed has $20$ edges.
:::

::: {.solution for="prob-mit18433-1-q7" status="draft"}
Hall's condition is necessary, since the vertices of $S$ need $|S|$ distinct partners in $N(S)$. For sufficiency, assume $|N(S)|\ge|S|$ for all $S\subseteq A$.

1. Let $C$ be a minimum vertex cover and $S=A\setminus C$. Every edge at a vertex of $S$ must be covered by its other end, so $N(S)\subseteq C\cap B$.

2. Hence $|C|=|C\cap A|+|C\cap B|\ge(|A|-|S|)+|N(S)|\ge|A|-|S|+|S|=|A|$.

3. By König's theorem (@thm-konig) a maximum matching has $|C|\ge|A|$ edges, so it covers $A$.
:::

::: {.solution for="prob-mit18433-1-q8" status="draft"}
1. *Upper bound.* In any matching, at most $|N(X)|$ vertices of $X$ are matched, so at least $\operatorname{def}(X)$ vertices of $A$ are exposed: $|M|\le|A|-\operatorname{def}(X)$ for every $X$.

2. *Lower bound.* Add $d=\operatorname{def}_{\max}$ new vertices to $B$, each joined to every vertex of $A$. In the new graph every non-empty $X\subseteq A$ has $|N'(X)|=|N(X)|+d\ge|X|$, so by Hall's theorem there is a matching covering $A$. At most $d$ of its edges use new vertices, so $G$ has a matching of size at least $|A|-d$.

3. *Supermodularity.* $|X\cup Y|+|X\cap Y|=|X|+|Y|$. Also $N(X\cup Y)=N(X)\cup N(Y)$ and $N(X\cap Y)\subseteq N(X)\cap N(Y)$, so
$$|N(X\cup Y)|+|N(X\cap Y)|\le|N(X)\cup N(Y)|+|N(X)\cap N(Y)|=|N(X)|+|N(Y)|.$$
Subtracting from the first identity gives $\operatorname{def}(X\cup Y)+\operatorname{def}(X\cap Y)\ge\operatorname{def}(X)+\operatorname{def}(Y)$.
:::

::: {.solution for="prob-mit18433-1-q12" status="draft"}
Assume $k\ge1$. Counting edges from each side, $k|A|=|E|=k|B|$, so $|A|=|B|$.

1. *By König.* A vertex covers exactly $k$ edges, so a vertex cover $C$ covers at most $k|C|$ edges; it must cover all $k|A|$, so $|C|\ge|A|$. By @thm-konig a maximum matching has at least $|A|$ edges, i.e. it is perfect.

2. *By linear programming.* The vector $x_e=\frac1k$ for $e\in E$ (and $0$ on non-edges) satisfies $\sum_jx_{ij}=1$ and $\sum_ix_{ij}=1$, so the polytope (P) of @def-assignment-problem, restricted to $E$, is non-empty. It is bounded, so it has a vertex (@thm-minkowski-polytope), and by @thm-bipartite-perfect-matching-polytope that vertex is a perfect matching of $G$.

3. *Optional.* No: the triangle is $2$-regular with $3$ vertices and has no perfect matching. Even for $k=3$ there are $3$-regular graphs with a bridge and no perfect matching (although by Petersen's theorem every $3$-regular graph without a bridge has one).
:::

::: {.solution for="prob-mit18433-1-q13" status="draft"}
1. Induct on $k$; for $k=0$ there are no edges. For $k\ge1$, exercise 12 gives a perfect matching $M_1$. Deleting it lowers every degree by exactly $1$, so $G-M_1$ is $(k-1)$-regular bipartite and by induction splits into $k-1$ matchings. With $M_1$ this gives $k$.

2. At least $k$ colours are needed, since the $k$ edges at one vertex need different colours. So the edge chromatic number is exactly $k$.

3. *Optional.* No: the triangle is $2$-regular but needs $3$ colours, and the Petersen graph is $3$-regular but needs $4$.
:::

::: {.solution for="prob-mit18433-1-q14" status="draft"}
1. At least $\Delta$ colours are needed at a vertex of degree $\Delta$. For the upper bound, embed $G$ in a $\Delta$-regular bipartite multigraph: first add isolated vertices to the smaller side so that $|A|=|B|$. While some vertex of $A$ has degree less than $\Delta$, so does some vertex of $B$ (the degree sums of the two sides are equal and both sides have the same number of vertices), and we add an edge between them, possibly parallel to an existing one. This ends with a $\Delta$-regular bipartite multigraph.

2. Exercises 12 and 13 hold for multigraphs with the same proofs (the vertex cover count in exercise 12 counts edges with multiplicity). So the multigraph splits into $\Delta$ matchings; restricting them to the edges of $G$ colours $G$ with $\Delta$ colours.

3. The triangle has $\Delta=2$ but its three edges pairwise share an end, so it needs $3$ colours.
:::

::: {.solution for="prob-mit18433ps-1-q4" status="draft"}
(a) 1. A $k$-set $a$ is contained in $n-k$ sets of size $k+1$, and a $(k+1)$-set contains $k+1$ sets of size $k$. So every vertex of $A_k$ has degree $n-k$ and every vertex of $A_{k+1}$ degree $k+1\le n-k$ (as $k<n/2$).

2. For $X\subseteq A_k$, the $|X|(n-k)$ edges leaving $X$ end in $N(X)$, which receives at most $|N(X)|(k+1)\le|N(X)|(n-k)$ edges. So $|N(X)|\ge|X|$, and by Hall's theorem (@sec-math-discrete-graph-bipartite-graphs) there is a matching covering $A_k$, of size $|A_k|=\binom nk$, the largest possible.

(b) 3. Let $m=\lfloor n/2\rfloor$. For each $k<m$, part (a) gives a matching $N_k$ from $A_k$ into $A_{k+1}$ covering $A_k$, with $a\subset b$ on each edge. For each $j>m$ we have $n-j<n/2$, so part (a) for $k=n-j$, applied to complements, gives a matching $N_j'$ from $A_j$ into $A_{j-1}$ covering $A_j$, with $b\supset a$ on each edge.

4. In the union of all these matchings, every set has at most one partner one level up and at most one one level down, so the components are chains $c_1\subset c_2\subset\dots$ through consecutive levels. A set below level $m$ is matched upwards and a set above level $m$ downwards, so every chain contains exactly one set of size $m$. Hence the subsets of $S$ are partitioned into $\binom nm$ chains.

5. A family in which no set contains another meets each chain at most once, so it has at most $\binom nm$ members; the family $A_m$ attains this.
:::
