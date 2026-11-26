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

::: {.solution for="prob-mit18433-4-q1" status="draft"}
1. Write $a_{ij}=\lfloor a_{ij}\rfloor+f_{ij}$ with $0\le f_{ij}<1$. The row sums $r_i'=\sum_jf_{ij}=r_i-\sum_j\lfloor a_{ij}\rfloor$ and column sums $c_j'=\sum_if_{ij}$ of $f$ are integers. It suffices to find $\varepsilon_{ij}\in\{0,1\}$, with $\varepsilon_{ij}=0$ whenever $f_{ij}=0$, having the same row sums $r'$ and column sums $c'$; then $a'_{ij}=\lfloor a_{ij}\rfloor+\varepsilon_{ij}$ works.

2. Build a network: source $s$, a node $R_i$ per row, a node $C_j$ per column, sink $t$; arcs $s\to R_i$ of capacity $r'_i$, $R_i\to C_j$ of capacity $1$ if $f_{ij}>0$, and $C_j\to t$ of capacity $c'_j$.

3. Sending $f_{ij}$ along $R_i\to C_j$ (and $r'_i$, $c'_j$ on the outer arcs) is a feasible flow saturating all arcs out of $s$, so the maximum flow value is $\sum_ir'_i$.

4. All capacities are integers, so there is an integral maximum flow (@cor-integral-flow). It saturates the arcs out of $s$ and into $t$ (same total), so $\varepsilon_{ij}=$ its value on $R_i\to C_j$ is $0$ or $1$, is $0$ where $f_{ij}=0$, and has row sums $r'$ and column sums $c'$.
:::

::: {.solution for="prob-mit18433-4-q2" status="draft"}
1. It is best for team $n$ to win all its remaining games, reaching $W=w_n+\sum_jg_{nj}$; team $n$ can still win iff the games among teams $1,\dots,n-1$ can be decided so that every team $i<n$ ends with at most $W$ wins. (This is the setting of @exm-baseball-elimination.)

2. *Network.* Source $s$; a node for each pair $\{i,j\}$, $i<j<n$, with an arc $s\to\{i,j\}$ of capacity $g_{ij}$; arcs $\{i,j\}\to i$ and $\{i,j\}\to j$ of infinite capacity; a node per team $i<n$ with an arc $i\to t$ of capacity $W-w_i$ (if some $W-w_i<0$, team $n$ is already out). An integral flow saturating all source arcs assigns every game a winner (the team receiving its unit) without any team exceeding $W$, and conversely. So team $n$ can win iff the maximum flow equals $G=\sum_{i<j<n}g_{ij}$; integrality is @cor-integral-flow.

3. *Condition.* Consider a cut with $s$-side containing the team set $T$ and some game nodes. Infinite arcs force every game node on the $s$-side to have both teams in $T$, and including all games inside $T$ only lowers the capacity. The minimum cut for a given $T$ therefore has capacity $G-g(T)+\sum_{i\in T}(W-w_i)$, where $g(T)=\sum_{i<j,\ i,j\in T}g_{ij}$. By max-flow min-cut (@thm-max-flow-min-cut), team $n$ can still win iff for every $T\subseteq\{1,\dots,n-1\}$
$$\sum_{i\in T}w_i+\sum_{i<j,\ i,j\in T}g_{ij}\ \le\ |T|\Big(w_n+\sum_{j}g_{nj}\Big),$$
i.e. no group of teams must win, on average, more than $W$ games in total.
:::

::: {.solution for="prob-mit18433-4-q3" status="draft"}
1. Network: source $s$, a node per edge $e$ and per vertex $v$, sink $t$; arcs $s\to e$ of capacity $1$, $e\to u$ and $e\to v$ of capacity $1$ for $e=\{u,v\}$, and $v\to t$ of capacity $p(v)$. An integral flow of value $|E|$ sends each edge's unit to one of its ends; orienting $e$ towards that end gives indegree at most $p(v)$ at every $v$. Conversely an orientation gives such a flow. So an orientation exists iff the maximum flow is $|E|$, and an integral maximum flow (@cor-integral-flow) gives it.

2. Suppose the maximum flow is less than $|E|$, and take a minimum cut with $s$-side $\{s\}\cup E'\cup S$ ($E'$ edge nodes, $S\subseteq V$). Its capacity is $|E\setminus E'|+\sum_{e\in E'}|e\setminus S|+p(S)$. Moving an edge node with an end outside $S$ to the sink side does not increase this (it adds $1$ and removes at least $1$), and an edge of $E(S)$ on the sink side may be moved to the source side, saving $1$. So the minimum is attained with $E'=E(S)$, of capacity $|E|-|E(S)|+p(S)$. By max-flow min-cut (@thm-max-flow-min-cut) this is less than $|E|$, so $|E(S)|>\sum_{v\in S}p(v)$.
:::
