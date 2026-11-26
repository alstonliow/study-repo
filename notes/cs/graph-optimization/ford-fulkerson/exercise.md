::: {.problem #prob-mit6046s15-7-q1 origin="external" source="mit6046s15-7-q1"}
**Maximum Flow in a Dynamic Network**

In this problem, you will design an algorithm that takes the following inputs:

- A flow network $F=(G,c)$, where $G=(V,E)$ is a graph with source vertex $s$ and target vertex $t$, and $c$ is a capacity function mapping each directed edge of $G$ to a nonnegative integer;
- A maximum flow $f$ for $F$; and
- A triple $(u,v,r)$, where $u$ and $v$ are vertices of $G$ and $r$ is a nonnegative integer $\ne c(u,v)$.

The algorithm should produce a maximum flow for flow network $F'=(G,c')$, where $c'$ is identical to $c$ except that $c'(u,v)=r$. The algorithm should run in time $O(k\cdot(V+E))$, where $|c(u,v)-r|=k$. The algorithm should behave differently depending on whether $r>c(u,v)$ or $r<c(u,v)$.

(a) Start by proving the following basic, general results about flow networks:

1. Increasing the capacity of a single edge $(u,v)$ by 1 can result in an increase of at most 1 in the max flow.
2. Increasing the capacity of a single edge $(u,v)$ by a positive integer $k$ can result in an increase of at most $k$ in the max flow.
3. Decreasing the capacity of a single edge $(u,v)$ by 1 can result in a decrease of at most 1 in the max flow.
4. Decreasing the capacity of a single edge $(u,v)$ by a positive integer $k$ can result in a decrease of at most $k$ in the max flow.

(b) Suppose that $r>c(u,v)$. Describe your algorithm for this case in detail, prove that it works correctly, and analyze its time complexity (in terms of $V$, $E$, and $k$).

(c) Suppose that $r<c(u,v)$. Describe your algorithm for this case in detail, prove that it works correctly, and analyze its time complexity.
:::

::: {.problem #prob-mit6854ps-1-q3 origin="external" source="mit6854ps-1-q3"}
Consider the Ford-Fulkerson augmenting path algorithm for the maximum flow problem seen in lecture, and assume that at every iteration the shortest (in terms of number of edges) augmenting path in the residual graph is selected (recall that the algorithm first finds the shortest path in the residual graph corresponding to the current flow, then pushes as much flow on it so as not to violate the capacity constraints, and then repeats until there is no augmenting path in the residual graph).

(a) Show that the length of the shortest path in the residual graph does not decrease from one iteration to the next.

(b) Show that the length of the shortest path in the residual graph must increase at least every $m$ iterations, where $m$ is the number of edges in the graph.

(c) Deduce that the total number of augmentations must be $O(nm)$ where $n$ is the number of vertices.

(d) Deduce that the total running time of the algorithm is $O(nm^2)$.
:::

::: {.problem #prob-mit6854ps-1-q4 origin="external" source="mit6854ps-1-q4"}
Consider a maximum $s-t$ flow problem with *integer* capacities $u$. We saw in lecture that the Ford and Fulkerson generic algorithm could take $O(mU)$ iterations, where $U$ is the maximum capacity of any edge, and this is not polynomial. In this problem, you will show that the algorithm can be made polynomial through a simple technique known as *scaling*.

(a) Suppose we have a maximum flow $f$ for our capacitated network, and we increase the capacity of some of the edges by 1 unit. $f$ may not remain optimal. Prove that the maximum flow value increases by at most $m$, where $m$ is the number of edges. What is the running time of Ford and Fulkerson if we start from our given flow $f$?

(b) Let $k=\lfloor\log_2U\rfloor$ and consider $k+1$ maximum flow instances. In the $j$th one where $j=0,1,\cdots,k$, the capacities $u(v,w)$ are replaced by
$$u_j(v,w)=\left\lfloor\frac{u(v,w)}{2^j}\right\rfloor.$$
When $j=0$, the problem is our original maximum flow instance. When $j=k$, all capacities are either 0 or 1. Describe how we can efficiently solve the maximum flow problem for the original capacities by solving the problem with the capacities $u_j$ for $j$ from $k$ down to 1. What is the running time of the resulting algorithm?
:::

::: {.problem #prob-mit6854ps-2-q1 origin="external" source="mit6854ps-2-q1"}
Given a directed graph $G=(V,E)$, a source $s\in V$, a sink $t\in V$ and a length function $l:E\to\mathbb R$, the fattest path problem is to find a simple path $P$ from $s$ to $t$ which maximizes $\min_{(v,w)\in P}l(v,w)$.

(a) Give a modification of Dijkstra's algorithm for the shortest path problem which solves the fattest path problem. Argue correctness of your algorithm.

(b) Suppose that all arcs lengths are integer-valued between 1 and $m$ where $m=|E|$. Can you provide an implementation of your algorithm that runs in $O(m)$ time? (Hint: Do not use any fancy priority queue.)
:::

::: {.problem #prob-mit6854ps-2-q2 origin="external" source="mit6854ps-2-q2"}
In this problem, you will show that the fattest augmenting path algorithm for the maximum flow problem can be implemented to run in $O(m)$ time per iteration after some basic preprocessing. Remember that in the fattest augmenting path algorithm, the augmenting path with largest minimum residual capacity is chosen at every iteration.

(a) Show that if we have a total ordering of the residual capacities then the fattest augmenting path can be found in $O(m)$ time.

(b) Show that, this total ordering of the residual capacities can be maintained in $O(m)$ time after pushing flow along one augmenting path (how do the residual capacities change)?

(c) What is the running time of the resulting implementation of the fattest augmenting path algorithm?
:::
