<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-6-q2" status="draft"}
By assumption $\delta(s,v)=\delta_k(s,v)$, the $k$-edge distance (@def-k-edge-distance), for every $v$ (for unreachable $v$ both are $\infty$). So run Bellman–Ford with only $k$ rounds instead of $|V|-1$.

1. Find the vertices reachable from $s$ by BFS in $O(|V|+|E|)$; set $\delta(s,v)=\infty$ for the others and delete them. The remaining graph $G'$ has $|V'|\le|E|+1$.

2. Compute $\delta_0,\delta_1,\dots,\delta_k$ on $G'$ by the recurrence $\delta_j(s,v)=\min\bigl(\{\delta_{j-1}(s,u)+w(u,v):(u,v)\in E\}\cup\{\delta_{j-1}(s,v)\}\bigr)$ (@exm-bellman-ford-dp), keeping only the previous level. Each level costs $O(|V'|+|E|)=O(|E|)$, so $k$ levels cost $O(k|E|)$.

3. Return $\delta_k(s,v)$. Total $O(|V|+k|E|)$.
:::

::: {.solution for="prob-mit6006s20-6-q4" status="draft"}
Let $G$ be the weighted digraph of locations and transitions, and $\bar G$ the same graph with all weights negated. Every cycle has weight $0$ exactly when $G$ has no negative-weight cycle *and* $\bar G$ has no negative-weight cycle (a cycle of positive weight in $G$ is a negative one in $\bar G$). Closed walks are unions of cycles, so it suffices to look at cycles.

To detect a negative-weight cycle anywhere in a graph, add a vertex $x$ with a $0$-weight edge to every location and run Bellman–Ford from $x$ (@thm-bellman-ford): a cycle exists iff some vertex gets weight $-\infty$. Do this for $G$ and for $\bar G$, and answer "conservative" iff neither has one. Each run takes $O(|V|\cdot|E|)=O(n\cdot n)=O(n^2)$ time.
:::
