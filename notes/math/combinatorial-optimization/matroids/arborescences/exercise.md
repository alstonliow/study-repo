::: {.problem #prob-mit18433ps-6-q2 origin="external" source="mit18433ps-6-q2"}
Consider the minimum cost arborescence problem we discussed in lecture. Given a digraph $D=(V,A)$, a root vertex $r\in V$, costs $c:A\to\mathbb R_+$, the problem is to find an $r$-arborescence of minimum total cost, where an $r$-arborescence is a spanning tree (when the directions of the arcs are discarded) in which all vertices are reachable from $r$ by a directed path. Consider the following greedy algorithm (generalizing the undirected setting):

$\quad$ Let $F=\emptyset$, $S=V\setminus\{r\}$\
$\quad$ **while** $S\ne\emptyset$ **do**\
$\qquad$ Among all arcs in $\bigcup_{v\in S}\delta^-(v)$ whose addition to $F$ does not create a directed circuit, let $(u,v)$ be the one of minimum cost\
$\qquad$ $F=F\cup\{a\}$\
$\qquad$ $S=S\setminus\{v\}$\
$\quad$ **end while**\
$\quad$ Return $F$

Show that this greedy type algorithm does not necessarily return the optimum arborescence.
:::

::: {.problem #prob-mit18433ps-6-q3 origin="external" source="mit18433ps-6-q3"}
In lecture and in the notes, we have seen an algorithm to compute the minimum cost $r$-arborescence for a given vertex $r$ (in a directed graoh $D$ with costs $c$). Suppose we would like to find the minimum cost $r$-arborescence for every vertex $r\in V$. We could use the algorithm seen in class $|V|$ times, but show how to modify it to be able to return a minimum cost $r$-arborescence for every $r$ (in time much less than running the algorithm $|V|$ times).

Hint: The modified algorithm should first construct a strongly connected graph $F$ (independently of $r$) such that it contains an optimum $r$-arborescence for every $r$ and such that this optimum $r$-arborescence can be obtained by a reverse delete procedure (as in the original algorithm).
:::
