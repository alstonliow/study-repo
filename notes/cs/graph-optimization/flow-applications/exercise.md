::: {.problem #prob-mit6046s15-7-q2 origin="external" source="mit6046s15-7-q2"}
**Disjoint Roads**

A number $k$ of trucking companies, $c_1,\dots,c_k$, want to use a common road system, which is modeled as a directed graph, for delivering goods from source locations to a common target location. Each trucking company $c_i$ has its own source location, modeled as a vertex $s_i$ in the graph, and the common target location is another vertex $t$. (All these $k+1$ vertices are distinct.)

The trucking companies want to share the road system for delivering their goods, but they want to avoid getting in each other's way while driving. Thus, they want to find $k$ edge-disjoint paths in the graph, one connecting each source $s_i$ to the target $t$. We assume that there is no problem if trucks of different companies pass through a common vertex.

Design an algorithm for the companies to use to determine $k$ such paths, if possible, and otherwise return "impossible".
:::

::: {.problem #prob-mit6046s15-7-q3 origin="external" source="mit6046s15-7-q3"}
**Food Truck Orders**

The Miso Good food truck produces a large variety of different lunch menu items. Unfortunately, they can only produce their foods in limited quantities, so they often run out of popular items, making customers sad.

To minimize sadness, Miso Good is implementing a sophisticated lunch-ordering system. Customers text in their acceptable choices before lunch time. Then they can use an algorithm to preassign lunches to customers. Customers who do not get one of their choices should receive a \$10 voucher. Miso Good would like to minimize the number of vouchers they give out.

Give an efficient algorithm for Miso Good to assign lunches to customers. In general, suppose that, on a given day, Miso Good has produced $m$ types of food items $b_1,\dots,b_m$, and the quantity of each type of food item $b_j$ is exactly $q_j$. Suppose that $n$ customers $a_1,\dots,a_n$ text in their preferences, where each customer $a_i$ submits a set $A_i$ of one or more acceptable lunch choices. The algorithm should assign each customer either one of his/her choices or a \$10 voucher. It should minimize the number of vouchers.

(Hint: Model this as a max flow problem.)
:::

::: {.problem #prob-mit18433-4-q1 origin="external" source="mit18433-4-q1"}
Suppose you are given an $m\times n$ matrix $A\in\mathbb R^{m\times n}$ with row sums $r_1,\cdots,r_m\in\mathbb Z$ and column sums $c_1,\cdots,c_n\in\mathbb Z$. Some of the entries might not be integral but the row sums and column sums are. Show that there exists a rounded matrix $A'$ with the following properties:

- row sums and column sums of $A$ and $A'$ are identical,
- $a'_{ij}=\lceil a_{ij}\rceil$ or $a'_{ij}=\lfloor a_{ij}\rfloor$ (i.e. $a'_{ij}$ is $a_{ij}$ either rounded up or down.).

By the way, this rounding is useful to the census bureau as they do not want to publish statistics that would give too much information on specific individuals. They want to be able to modify the entries without modifying row and column sums.
:::

::: {.problem #prob-mit18433-4-q2 origin="external" source="mit18433-4-q2"}
At some point during baseball season, each of $n$ teams of the American League has already played several games. Suppose team $i$ has won $w_i$ games so far, and $g_{ij}=g_{ji}$ is the number of games that teams $i$ and $j$ have yet to play. No game ends in a tie, so each game gives one point to either team and 0 to the other. You would like to decide if your favorite team, say team $n$, can still win. In other words, you would like to determine whether there exists an outcome to the games to be played (remember, with no ties) such that team $n$ has at least as many victories as all the other teams (we allow team $n$ to be tied for first place with other teams).

Show that this problem can be solved as a maximum flow problem. Give a necessary and sufficient condition on the $g_{ij}$'s so that team $n$ can still win.
:::

::: {.problem #prob-mit18433-4-q3 origin="external" source="mit18433-4-q3"}
Consider the following orientation problem. We are given an undirected graph $G=(V,E)$ and integer values $p(v)$ for every vertex $v\in V$. we would like to know if we can orient the edges of $G$ such that the directed graph we obtain has at most $p(v)$ arcs incoming to $v$ (the "indegree requirements"). In other words, for each edge $\{u,v\}$, we have to decide whether to orient it as $(u,v)$ or as $(v,u)$, and we would like at most $p(v)$ arcs oriented towards $v$.

1. Show that the problem can be formulated as a maximum flow problem. That is, show how to create a maximum flow problem such that, from its solution, you can decide whether or not the graph can be oriented and if so, it also gives the orientation.
2. Consider the case that the graph cannot be oriented and meet the indegree requirements. Prove from the max-flow min-cut theorem that there must exist a set $S\subseteq V$ such that $|E(S)|>\sum_{v\in S}p(v)$, where as usual $E(S)$ denotes the set of edges with both endpoints within $S$.
:::
