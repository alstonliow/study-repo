::: {.problem #prob-mit18433-2-q2 origin="external" source="mit18433-2-q2"}
Let $G=(V,E)$ be any graph. Given a set $S\subseteq V$, suppose that there exists a matching $M$ covering $S$ (i.e. $S$ is a subset of the matched vertices in $M$). Prove that there exists a maximum matching $M^*$ covering $S$ as well.
:::

::: {.problem #prob-mit18433-2-q3 origin="external" source="mit18433-2-q3"}
Let $U$ be any minimizer in the Tutte-Berge formula. Let $K_1,\cdots,K_k$ be the connected components of $G\setminus U$. Show that, for any maximum matching $M$, we must have that

1. $M$ contains exactly $\lfloor\frac{|K_i|}2\rfloor$ edges from $G[K_i]$ (the subgraph of $G$ induced by the vertices in $K_i$), i.e. $G[K_i]$ is perfectly matched for the even components $K_i$ and near-perfectly matched for the odd components.
2. Each vertex $u\in U$ is matched to a vertex $v$ in an odd component $K_i$ of $G\setminus U$.
3. the only unmatched vertices must be in odd components $K_i$ of $G\setminus U$.
:::

::: {.problem #prob-mit18433-2-q4 origin="external" source="mit18433-2-q4"}
Could there be several minimizers $U$ in the Tutte-Berge formula? Either give an example with several sets $U$ achieving the minimum, or prove that the set $U$ is unique.
:::

::: {.problem #prob-mit18433-2-q5 origin="external" source="mit18433-2-q5"}
Given a graph $G=(V,E)$, an inessential vertex is a vertex $v$ such that there exists a maximum matching of $G$ not covering $v$. Let $B$ be the set of all inessential vertices in $G$ (e.g., if $G$ has a perfect matching then $B=\emptyset$). Let $C$ denote the set of vertices not in $B$ but adjacent to at least one vertex in $B$ (thus, if $B=\emptyset$ then $C=\emptyset$). Let $D=V\setminus(B\cup C)$. The triple $\{B,C,D\}$ is called the Edmonds-Gallai partition of $G$. Show that $U=C$ is a minimizer in the Tutte-Berge formula. (In particular, this means that in the Tutte-Berge formula we can assume that $U$ is such that the union of the odd connected components of $G\setminus U$ is precisely the set of inessential vertices.)
:::

::: {.problem #prob-mit18433-2-q6 origin="external" source="mit18433-2-q6"}
Show that any 3-regular 2-edge-connected graph $G=(V,E)$ (not necessarily bipartite) has a perfect matching. (A 2-edge-connected graph has at least 2 edges in every cutset; a cutset being the edges between $S$ and $V\setminus S$ for some vertex set $S$.)
:::

::: {.problem #prob-mit18433-2-q7 origin="external" source="mit18433-2-q7"}
A graph $G=(V,E)$ is said to be factor-critical if, for all $v\in V$, we have that $G\setminus\{v\}$ contains a perfect matching. In parts (a) and (b) below, $G$ is a factor-critical graph.

1. Let $U$ be any minimizer in the Tutte-Berge formula for $G$. Prove that $U=\emptyset$. (Hint: see Exercise 2-3.)
2. Deduce that when Edmonds algorithm terminates the final graph (obtained from $G$ by shrinking flowers) must be a single vertex.
3. Given a graph $H=(V,E)$, an ear is a path $v_0-v_1-v_2-\cdots-v_k$ whose endpoints ($v_0$ and $v_k$) are in $V$ and whose internal vertices ($v_i$ for $1\le i\le k-1$) are not in $V$. We allow that $v_0$ be equal to $v_k$, in which case the path would reduce to a cycle. Adding the ear to $H$ creates a new graph on $V\cup\{v_1,\cdots,v_{k-1}\}$. The trivial case when $k=1$ (a 'trivial' ear) simply means adding an edge to $H$. An ear is called odd if $k$ is odd, and even otherwise; for example, a trivial ear is odd.
   (a) Let $G$ be a graph that can be constructed by starting from an odd cycle and repeatedly adding odd ears. Prove that $G$ is factor-critical.
   (b) Prove the converse that any factor-critical graph can be built by starting from an odd cycle and repeatedly adding odd ears.
:::
