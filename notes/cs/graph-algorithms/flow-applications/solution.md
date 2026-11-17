<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-7-q2" status="draft"}
Give every road edge capacity $1$, add a super-source $s$ with an edge $s\to s_i$ of capacity $1$ for each company, and compute a maximum flow from $s$ to $t$ by Ford–Fulkerson. If its value is less than $k$, answer "impossible". Otherwise the flow is integral (@cor-integral-flow) with one unit leaving each $s_i$; follow each unit from $s_i$ along edges with flow $1$ (removing used edges, and dropping any cycles met) to get $k$ paths that share no edge, one from each $s_i$.

*Correctness:* $k$ edge-disjoint paths give a flow of value $k$ (one unit per path), and conversely as above. *Time:* the value is at most $k$, so there are at most $k$ augmentations of $O(V+E)$ each: $O(k(V+E))$, plus $O(E)$ to decompose the flow.
:::

::: {.solution for="prob-mit6046s15-7-q3" status="draft"}
Build a network with a source $s$, a node per customer and per food type, and a sink $t$: edges $s\to a_i$ of capacity $1$, $a_i\to b_j$ of capacity $1$ for each $b_j\in A_i$, and $b_j\to t$ of capacity $q_j$. Compute an integral maximum flow $f$. Customer $a_i$ gets food $b_j$ if one unit flows on $a_i\to b_j$, and a voucher otherwise; the number of vouchers is $n-|f|$.

*Correctness:* integral flows correspond exactly to valid assignments (each customer gets at most one acceptable item, and type $b_j$ is given at most $q_j$ times), with flow value equal to the number of customers fed, as in @thm-matching-by-flow. Maximising the flow minimises the vouchers. *Time:* $|f|\le n$ augmentations, each $O(n+m+\sum_i|A_i|)$ by BFS.
:::
