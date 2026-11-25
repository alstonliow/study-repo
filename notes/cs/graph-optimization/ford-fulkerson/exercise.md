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
