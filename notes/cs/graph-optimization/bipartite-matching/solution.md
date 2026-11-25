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
