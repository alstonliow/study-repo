::: {.problem #prob-mit6854ps-6-q1 origin="external" source="mit6854ps-6-q1"}
In lecture, we saw a randomized incremental algorithm to find the convex hull of $n$ points in $\mathbb R^d$. The algorithm first selects a random ordering, say $p_1,\cdots,p_n$, of the $n$ points, and then incrementally computes $P_i=conv(\{p_1,\cdots,p_i\})$. When going from $P_{i-1}$ to $P_i$, some of the facets of $P_{i-1}$ disappears (the ones that were visible from $x_i$) and a number of new facets are created. Let $N_i$ be the number of facets created at step $i$. The expected running time of the algorithm can be shown to be $O(n^2+\sum_{i=d+2}^nE[N_i])$. Prove that
$$\sum_{i=d+2}^nE[N_i]=O\left(n^{\lfloor d/2\rfloor}\right).$$
(You can use the fact that the convex hull of $k$ points in $\mathbb R^d$ has $O(k^{\lfloor d/2\rfloor})$ facets.)
:::
