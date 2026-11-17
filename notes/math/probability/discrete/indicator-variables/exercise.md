::: {.problem #prob-cs70hw-11-q4 origin="external" source="cs70hw-11-q4"}
**Graph.** Consider a random graph (undirected, no multi-edges, no self-loops) on $n$ nodes, where each possible edge exists independently with probability $p$. Let $X$ be the number of isolated nodes (nodes with degree 0).

(a) What is $E(X)$? Consider $X$ to be the sum of the indicators $X_i$ that vertex $i$ is isolated. Why isn't $X$ a binomial random variable?

(b) (optional) What is $\mathrm{Var}(X)$?
:::

::: {.problem #prob-cs70hw-11-q5 origin="external" source="cs70hw-11-q5"}
**Triangles in Random Graphs.** Let's say we make a simple and undirected graph $G$ on $n$ vertices by randomly adding $m$ edges, without replacement. In other words, we choose the first edge uniformly from all $\binom{n}{2}$ possible edges, then the second one uniformly from among the remaining $\binom{n}{2} - 1$ edges, etc. What is the expected number of triangles in $G$? (A triangle is a triplet of distinct vertices with all three edges present between them.)
:::
