<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-graph-1-05" status="draft"}
1. Let $W = v_0v_1\cdots v_k$ be a shortest walk from $u = v_0$ to $w = v_k$,
   and suppose it is not a path. Then some vertex repeats: $v_i = v_j$ with
   $i<j$.

2. Remove the closed section between the two occurrences:
   $$W' = v_0\cdots v_i v_{j+1}\cdots v_k.$$
   This is still a walk from $u$ to $w$, because $v_i = v_j$ is adjacent to
   $v_{j+1}$.

3. $W'$ has length $k - (j-i) < k$, contradicting the choice of $W$. So $W$
   is a path.
:::

::: {.solution for="prob-graph-1-06" status="draft"}
Let $G$ be a finite graph with minimum degree at least $2$.

1. Let $P = v_0v_1\cdots v_k$ be a longest path in $G$. It exists because $G$
   is finite and has at least one edge.

2. Every neighbour of $v_0$ lies on $P$. Otherwise we could add that
   neighbour in front of $v_0$ and get a longer path.

3. $v_0$ has at least two neighbours, so it has a neighbour $v_i$ other than
   $v_1$, with $i\ge2$.

4. Then $v_0v_1\cdots v_iv_0$ is a cycle, of length $i+1\ge3$.
:::

::: {.solution for="prob-graph-1-07" status="draft"}
If $u$ and $v$, or $v$ and $w$, are in different components, the right-hand
side is $\infty$ and there is nothing to prove. Otherwise:

1. Take a shortest walk from $u$ to $v$, of length $d_G(u,v)$, and a shortest
   walk from $v$ to $w$, of length $d_G(v,w)$.

2. Following one and then the other is a walk from $u$ to $w$ of length
   $d_G(u,v) + d_G(v,w)$.

3. $d_G(u,w)$ is the length of a shortest walk from $u$ to $w$, so it is at
   most this length.
:::
