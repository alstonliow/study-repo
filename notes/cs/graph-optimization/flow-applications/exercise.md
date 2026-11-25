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

::: {.problem #prob-mit6046r-7-q1 origin="external" source="mit6046r-7-q1"}
**Bipartite Vertex Cover**

Given a bipartite graph $G=(L\cup R,\ E\subseteq L\times R)$, find the set $S$ such that $S$ covers $G$ and $|S|$ is minimal.
:::
