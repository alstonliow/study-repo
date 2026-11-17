::: {.problem #prob-cs70hw-11-q4 origin="external" source="cs70hw-11-q4"}
**Graph.** Consider a random graph (undirected, no multi-edges, no self-loops) on $n$ nodes, where each possible edge exists independently with probability $p$. Let $X$ be the number of isolated nodes (nodes with degree 0).

(a) What is $E(X)$? Consider $X$ to be the sum of the indicators $X_i$ that vertex $i$ is isolated. Why isn't $X$ a binomial random variable?

(b) (optional) What is $\mathrm{Var}(X)$?
:::

::: {.problem #prob-cs70hw-11-q5 origin="external" source="cs70hw-11-q5"}
**Triangles in Random Graphs.** Let's say we make a simple and undirected graph $G$ on $n$ vertices by randomly adding $m$ edges, without replacement. In other words, we choose the first edge uniformly from all $\binom{n}{2}$ possible edges, then the second one uniformly from among the remaining $\binom{n}{2} - 1$ edges, etc. What is the expected number of triangles in $G$? (A triangle is a triplet of distinct vertices with all three edges present between them.)
:::

::: {.problem #prob-mit6042f10-12-q2 origin="external" source="mit6042f10-12-q2"}
Here are seven propositions:
$$\begin{array}{ccccc}
x_1 & \lor & x_3 & \lor & \lnot x_7\\
\lnot x_5 & \lor & x_6 & \lor & x_7\\
x_2 & \lor & \lnot x_4 & \lor & x_6\\
\lnot x_4 & \lor & x_5 & \lor & \lnot x_7\\
x_3 & \lor & \lnot x_5 & \lor & \lnot x_8\\
x_9 & \lor & \lnot x_8 & \lor & x_2\\
\lnot x_3 & \lor & x_9 & \lor & x_4
\end{array}$$
Note that:

1. Each proposition is the OR of three terms of the form $x_i$ or the form $\lnot x_i$.
2. The variables in the three terms in each proposition are all different.

Suppose that we assign true/false values to the variables $x_1, \ldots, x_9$ independently and with equal probability.

(a) What is the expected number of true propositions?

(b) Use your answer to prove that there exists an assignment to the variables that makes all of the propositions true.
:::
