<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-2-q3" status="draft"}
Assume every vertex is reachable from $s$ (otherwise add a new source joined to every vertex by edges of length $0$; this creates no cycle). Compute $d_0,\dots,d_n$ by the recurrence ($d_0(s)=0$, $d_0(v)=\infty$ otherwise): $n$ rounds of $O(m)$, so $O(nm)$.

*(a) Karp's formula:*
$$\mu^*=\min_{v}\ \max_{0\le k\le n-1}\frac{d_n(v)-d_k(v)}{n-k}$$
(terms with $d_k(v)=\infty$ are skipped; $v$ with $d_n(v)=\infty$ are skipped). Evaluating it costs $O(n^2)$ after Bellman–Ford.

1. Subtracting $\mu$ from every length lowers $d_k(v)$ by $k\mu$, hence every ratio, and the right side, by exactly $\mu$; it also lowers $\mu^*$ by $\mu$. So we may assume $\mu^*=0$: no negative cycle and some cycle $C$ of length $0$.

2. *Every term of the minimum is $\ge0$.* With no negative cycles, a walk of $n$ edges contains a cycle, so $d_n(v)\ge d(v)=\min_{k\le n-1}d_k(v)$ (shortest paths are simple). So for the $k$ attaining $d(v)$, $d_n(v)-d_k(v)\ge0$.

3. *Some term is $\le0$.* Let $w$ be a vertex of $C$ and $P$ a shortest path to $w$. Extend $P$ around $C$ until the walk has exactly $n$ edges, ending at some $v$. For the part $Q$ of $C$ from $w$ to $v$: $d(v)\le d(w)+l(Q)$, and $d(w)\le d(v)+l(C\setminus Q)=d(v)-l(Q)$ since $l(C)=0$; so the walk has length $d(w)+l(Q)=d(v)$, and $d_n(v)\le d(v)$. Then $d_n(v)-d_k(v)\le d(v)-d_k(v)\le0$ for all $k$, so the maximum for this $v$ is $\le0$.

4. Hence the formula gives $0=\mu^*$.

*(b)* Keep for every $k$ and $v$ the predecessor that attains $d_k(v)$. Let $v$ attain the minimum in (a). Follow predecessors back from $(n,v)$: the $n$-edge walk has $n+1$ vertices, so some vertex repeats; this gives a cycle $C$ on the walk, found in $O(n)$ time with a marker array.

1. Shift so that $\mu^*=0$. By (a), $d_n(v)-d_k(v)\le0$ for all $k$, i.e. $d_k(v)\ge d_n(v)$.

2. Cutting $C$ out of the walk gives a walk to $v$ with $n-|C|$ edges and length $d_n(v)-l(C)\ge d_{n-|C|}(v)\ge d_n(v)$. Hence $l(C)\le0$, and as there are no negative cycles, $l(C)=0$: $C$ is a minimum mean cycle. Total extra time $O(n^2)$ (for evaluating the formula).
:::

::: {.solution for="prob-mit6854ps-2-q4" status="draft"}
*(a)* $\mu^*\ge\mu$ iff the lengths $l-\mu$ have no negative cycle. Compute $l-\mu$ ($m$ additions, adding $-\mu$), run Bellman–Ford for $d_1,\dots,d_n$ (each round, for each edge, one addition and one comparison), form $h_{n-1}$ and test $d_n(v)\ge h_{n-1}(v)$ ($O(n^2)$ comparisons, or $O(n)$ if $h$ is kept as a running minimum). So $A(m,n)=O(nm)$ and $C(m,n)=O(nm)$.

*(b) Parametric search (Megiddo).*

1. Run the algorithm of (a) symbolically with $\mu=\mu^*$, every number stored as $a+b\mu^*$; additions are done coefficientwise.

2. To resolve a comparison of $a_1+b_1\mu^*$ with $a_2+b_2\mu^*$: if $b_1=b_2$ it is decided by $a_1$ versus $a_2$. Otherwise the answer depends only on how $\mu^*$ compares with the critical value $\mu_0=(a_2-a_1)/(b_1-b_2)$. Decide that by running the algorithm of (a) concretely at $\mu_0$ (it says whether $\mu^*<\mu_0$); if $\mu^*\ge\mu_0$, also test whether the graph with lengths $l-\mu_0$ has a zero cycle (compute potentials with $l-\mu_0$, then look for a cycle among edges of reduced length $0$), which tells $\mu^*=\mu_0$ versus $\mu^*>\mu_0$. If $\mu^*=\mu_0$ we have found $\mu^*$ and stop.

3. The symbolic run must meet such an equality. Otherwise every comparison is strict at $\mu^*$ and keeps its outcome for all $\mu$ in a small interval around $\mu^*$, so the algorithm would give the same answer for $\mu$ slightly above $\mu^*$ (where there is a negative cycle) and at $\mu^*$ (where there is none).

4. *Cost.* Each comparison costs one run of (a) plus a zero-cycle test, $O(A+C)$; additions cost $O(1)$. Total $O\big(A+C\cdot(A+C)\big)=O(n^2m^2)$.
:::
