::: {.problem #prob-mit6042f10-4-q4 origin="external" source="mit6042f10-4-q4"}
Recall that a *coloring* of a simple graph is an assignment of a color to each vertex such that no two adjacent vertices have the same color. A *$k$-coloring* is a coloring that uses at most $k$ colors.

**False Claim.** *Let $G$ be a (simple) graph with maximum degree at most $k$. If $G$ also has a vertex of degree less than $k$, then $G$ is $k$-colorable.*

(a) Give a counterexample to the False Claim when $k = 2$.

(b) Consider the following proof of the False Claim:

*Proof.* Proof by induction on the number $n$ of vertices:

*Induction hypothesis:* $P(n)$ is defined to be: Let $G$ be a graph with $n$ vertices and maximum degree a most $k$. If $G$ also has a vertex of degree less than $k$, then $G$ is $k$-colorable.

*Base case:* ($n=1$) $G$ has only one vertex and so is 1-colorable. So $P(1)$ holds.

*Inductive step:*

We may assume $P(n)$. To prove $P(n + 1)$, let $G_{n+1}$ be a graph with $n + 1$ vertices and maximum degree at most $k$. Also, suppose $G_{n+1}$ has a vertex, $v$, of degree less than $k$. We need only prove that $G_{n+1}$ is $k$-colorable.

To do this, first remove the vertex $v$ to produce a graph, $G_n$, with $n$ vertices. Removing $v$ reduces the degree of all vertices adjacent to $v$ by 1. So in $G_n$, each of these vertices has degree less than $k$. Also the maximum degree of $G_n$ remains at most $k$. So $G_n$ satisfies the conditions of the induction hypothesis $P(n)$. We conclude that $G_n$ is $k$-colorable.

Now a $k$-coloring of $G_n$ gives a coloring of all the vertices of $G_{n+1}$, except for $v$. Since $v$ has degree less than $k$, there will be fewer than $k$ colors assigned to the nodes adjacent to $v$. So among the $k$ possible colors, there will be a color not used to color these adjacent nodes, and this color can be assigned to $v$ to form a $k$-coloring of $G_{n+1}$.

Identify the exact sentence where the proof goes wrong.
:::

::: {.problem #prob-mit6042f10-4-q6 origin="external" source="mit6042f10-4-q6"}
Let $(s_1, s_2, \ldots, s_n)$ be an arbitrarily distributed sequence of the number $1, 2, \ldots, n - 1, n$. For instance, for $n = 5$, one arbitrary sequence could be $(5, 3, 4, 2, 1)$.

Define the graph $G=(V,E)$ as follows:

1. $V = \{v_1, v_2, \ldots, v_n\}$
2. $e = (v_i, v_j) \in E$ if either:
   (a) $j = i + 1$, for $1 \le i \le n - 1$
   (b) $i = s_k$, and $j = s_{k+1}$ for $1 \le k \le n - 1$

(a) Prove that this graph is 4-colorable for any $(s_1, s_2, \ldots, s_n)$.

Hint: First show that a line graph is 2-colorable. Note that a line graph is defined as follows: The $n$-node graph containing $n - 1$ edges in sequence is known as the line graph $L_n$.

(b) Suppose $(s_1, s_2, \ldots, s_n) = (1, a_1, 3, a_2, 5, a_3, \ldots)$ where $a_1, a_2, \ldots$ is an arbitrary distributed sequence of the even numbers in $1, \ldots, n - 1$. Prove that the resulting graph is 2-colorable.
:::
