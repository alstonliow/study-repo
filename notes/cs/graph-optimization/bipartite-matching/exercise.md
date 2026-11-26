::: {.problem #prob-mit6046r-7-q1 origin="external" source="mit6046r-7-q1"}
**Bipartite Vertex Cover**

Given a bipartite graph $G=(L\cup R,\ E\subseteq L\times R)$, find the set $S$ such that $S$ covers $G$ and $|S|$ is minimal.
:::

::: {.problem #prob-mit6854ps-1-q6 origin="external" source="mit6854ps-1-q6"}
We have seen in lecture that the maximum cardinality matching problem in a bipartite graph $G=(V,E)$ with $V=A\cup B$ can be formulated as a maximum flow problem in a network $H$ with vertex set $V\cup\{s,t\}$ and appropriately defined arcs and capacities. For any matching $M$ in $G$, there is a corresponding $0-1$ flow $f$ (i.e. with all (raw) flow values 0 or 1) in $H$ with $|f|=|M|$, and vice versa.

Use the max-flow min-cut theorem to show that there exists a matching $M$ in $G$ of cardinality $|A|$ (i.e. every vertex in $A$ is incident to an edge of $M$) if and only if for every $S\subseteq A$, we have $|N(S)|\ge|S|$ where $N(S)=\{v\in B:\exists u\in S\text{ with }(u,v)\in E\}$ is the set of neighbors of $S$ (or neighborhood).
:::

::: {.problem #prob-mit6854ps-1-q7 origin="external" source="mit6854ps-1-q7"}
Consider the following 2-player game between Alice and Bob. We are given a bipartite graph $G=(V,E)$ where $V$ is partitioned into $A\cup B$ (thus $A$ and $B$ are disjoint). Alice first chooses a vertex $a_1\in A$. Then Bob selects a vertex $b_1\in B$ which is adjacent to $a_1$. Alice now needs to select a vertex $a_2\in A$ which is adjacent to $b_1$, and different from $a_1$. And we keep alternating between the 2 players. At any stage, a player needs to select a vertex which is (i) adjacent to the last vertex selected by its opponent and (ii) distinct from all previously selected vertices. A player loses as soon as he/she can't select such a vertex.

For example, if the graph is a path $u-v-w-x$ on 4 vertices with $A=\{u,w\}$ and $B=\{v,x\}$ then Bob has a winning strategy. If Alice first plays $u$ then Bob will play $v$ (and then Alice $w$ and Bob $x$), and if she plays $w$, he will play $x$. It is also easy to construct instances where Alice has a winning strategy (e.g. a complete bipartite graph with $|A|>|B|$).

Design a polynomial-time algorithm which given a bipartite graph decides whether Alice or Bob has a winning strategy. And explain what the corresponding winning strategy (for that player) is.
:::
