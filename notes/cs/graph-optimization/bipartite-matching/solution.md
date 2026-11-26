<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046r-7-q1" status="draft"}
Build a flow network $H$: a source $s$ with a capacity-$1$ edge to every $u\in L$, a capacity-$1$ edge from every $v\in R$ to a sink $t$, and every edge of $E$ directed from $L$ to $R$ with capacity $\infty$. Compute a maximum flow; the vertices $A$ reachable from $s$ in the final residual graph form a minimum cut $(A,B)$. Return
$$S=(L\setminus A)\cup(R\cap A).$$

1. *$S$ is a cover.* The cut $(A,B)$ has finite capacity, so no $\infty$ edge goes from $L\cap A$ to $R\setminus A$. Take an edge $(u,v)$ with $u\in L$, $v\in R$. If $u\notin A$ then $u\in S$. If $u\in A$ then $v\in A$, so $v\in S$.

2. *$|S|$ is the cut capacity.* The only cut edges are $s\to u$ for $u\in L\setminus A$ and $v\to t$ for $v\in R\cap A$, so the capacity is $|L\setminus A|+|R\cap A|=|S|$.

3. *Every cover gives a cut.* For any cover $C$, let $A'=\{s\}\cup(L\setminus C)\cup(R\cap C)$. An edge from $u\in L\setminus C$ must end in $C$, hence in $R\cap C\subseteq A'$, so no $\infty$ edge leaves $A'$, and the capacity of $(A',\,\cdot\,)$ is $|L\cap C|+|R\cap C|=|C|$.

By 2 and 3, $|S|$ equals the minimum cut, which is at most the size of any cover; so $S$ is a minimum vertex cover, and its size equals the maximum flow (König's theorem: in a bipartite graph, minimum vertex cover = maximum matching). Time: one max-flow computation plus a graph search.
:::

::: {.solution for="prob-mit6854ps-1-q6" status="draft"}
$H$ has arcs $s\to a$ ($a\in A$), $a\to b$ ($ab\in E$) and $b\to t$ ($b\in B$), all of capacity $1$.

1. *Necessity.* If $M$ covers $A$, the partners of the vertices of $S$ are $|S|$ distinct vertices of $N(S)$.

2. *Sufficiency.* Assume Hall's condition and take any $s$–$t$ cut $X$ ($s\in X$, $t\notin X$). Let $A_1=A\cap X$ and $B_1=B\cap X$. The arcs leaving $X$ include $s\to a$ for $a\in A\setminus A_1$, $b\to t$ for $b\in B_1$, and, for every $b\in N(A_1)\setminus B_1$, at least one arc $a\to b$ with $a\in A_1$. So
$$\operatorname{cap}(X)\ge|A\setminus A_1|+|B_1|+|N(A_1)\setminus B_1|\ge|A\setminus A_1|+|N(A_1)|\ge|A\setminus A_1|+|A_1|=|A|.$$

3. Every cut has capacity at least $|A|$, and the cut $\{s\}$ has capacity $|A|$, so the maximum flow is $|A|$. By integrality (@cor-integral-flow) there is a $0$–$1$ flow of value $|A|$, i.e. a matching of size $|A|$.
:::

::: {.solution for="prob-mit6854ps-1-q7" status="draft"}
*Claim.* Bob wins if and only if $G$ has a matching covering $A$. So compute a maximum matching $M$ (by maximum flow, @sec-cs-graph-optimization-bipartite-matching) and compare $|M|$ with $|A|$.

1. *If $M$ covers $A$, Bob wins:* whenever Alice plays $a$, Bob answers $M(a)$. This is adjacent to $a$ and unused: the vertices of $B$ used so far are the partners of earlier, distinct vertices of $A$. So Bob can always move, and since the game is finite, Alice eventually cannot.

2. *If $|M|<|A|$, Alice wins:* let $M$ be a maximum matching and $a_1\in A$ a vertex it misses; Alice starts with $a_1$ and answers every $b$ by $M(b)$.

3. This is always possible. After Bob plays $b_i$, the sequence $a_1b_1a_2b_2\dots a_ib_i$ with $a_{j+1}=M(b_j)$ is an $M$-alternating path starting at the uncovered $a_1$; if $b_i$ were uncovered, the path would be augmenting, contradicting maximality (@sec-math-combinatorial-optimization-matching-augmenting-paths). So $M(b_i)$ exists; it differs from $a_1$ (uncovered) and from $a_2,\dots,a_i$ (partners of other $b$'s).

4. Hence Bob is the one who eventually cannot move. In the path example $\{uv,wx\}$ covers $A$ (Bob wins); in $K_{|A|,|B|}$ with $|A|>|B|$ no matching covers $A$ (Alice wins). The algorithm runs in polynomial time, e.g. $O(nm)$ with augmenting paths.
:::
