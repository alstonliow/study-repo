<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-7-q1" status="draft"}
(a) By max-flow min-cut (@thm-max-flow-min-cut) the maximum flow equals the minimum cut capacity. Changing $c(u,v)$ by $k$ changes the capacity of every cut by $0$ or by exactly $k$ (depending on whether $(u,v)$ crosses it), in the same direction. So the minimum over all cuts changes by at most $k$ in that direction. Statements 1 and 3 are the case $k=1$.

(b) $f$ is still a feasible flow. Starting from it, run Ford–Fulkerson (@def-ford-fulkerson): search for an augmenting path by BFS in $O(V+E)$ and push $1$ unit (capacities are integers). By (a) the maximum grew by at most $k$, so after at most $k$ augmentations no augmenting path exists, and the flow is maximum. Time $O(k(V+E))$, plus one final search.

(c) If $f(u,v)\le r$, then $f$ is feasible for $c'$, and since the maximum cannot grow, it is still maximum. Otherwise let $d=f(u,v)-r\le k$. Repeat $d$ times: in the graph of edges carrying positive flow, find a path from $s$ to $u$ and a path from $v$ to $t$ (they exist by flow conservation, and are found by DFS in $O(V+E)$); decrease the flow by $1$ along $s\to u$, $(u,v)$ and $v\to t$. (If the flow through $(u,v)$ is on a cycle, cancel the cycle instead.) The result is feasible for $c'$ with value $|f|-d$. Then run at most $d$ augmentations as in (b) to restore maximality; the new maximum is at least $|f|-k$ by (a) and at most $|f|$. Time $O(k(V+E))$.
:::
