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

::: {.solution for="prob-mit6006r-12-q1" status="draft"}
1. *Graph.* Intersections are vertices; each road gives a directed edge per direction of travel, with weight equal to *minus* its fun in that direction. Maximizing fun is now minimizing weight, and a loop of ever-increasing fun is a negative-weight cycle.

2. Run Bellman–Ford from each of the three homes $a,b,c$. Every road is reachable from every home, so a fun loop exists if and only if Bellman–Ford reports a negative cycle (one run already suffices to detect it). If so, report the loop.

3. Otherwise all distances $\delta(a,v),\delta(b,v),\delta(c,v)$ are finite. Choose the meeting point $v$ minimizing $\delta(a,v)+\delta(b,v)+\delta(c,v)$; its total fun is minus that sum.

Three Bellman–Ford runs and one $O(|V|)$ scan: $O(|V|\,|E|)$ time.
:::

::: {.solution for="prob-mit6006-12-q1" status="draft"}
Treat each undirected edge $\{u,v\}$ as the two directed edges $(u,v)$ and $(v,u)$ of the same weight; this is how shortest paths in an undirected graph are defined.

1. If some edge has weight $w(u,v)<0$, then $u\to v\to u$ is a cycle of weight $2w(u,v)<0$.

2. If there is a negative-weight cycle, at least one of its edges has negative weight.

3. So the answer is Yes exactly when some edge has negative weight. Scanning the edges takes $O(|E|)$ time. This is why negative weights are only interesting in directed graphs.
:::

::: {.solution for="prob-mit6006-12-q2" status="draft"}
1. Run BFS (or DFS) from $s$ in $O(|V|+|E|)$ time to find the set $V'$ of vertices reachable from $s$. Set $\delta(s,v)=\infty$ for $v\notin V'$.

2. Let $G'$ be the subgraph induced on $V'$, with edge set $E'$. Every path from $s$ stays inside $V'$, so the distances from $s$ in $G'$ are the same as in $G$. Run $A$ on $G'$.

3. Every vertex of $V'$ other than $s$ is entered by some edge of $E'$ (the last edge of a path from $s$), so $|V'|\le|E'|+1$. Hence $A$ takes $O(|V'|(|V'|+|E'|))=O(|V'|(|E'|+1))$ time, which is $O(|V||E|)$ when $|E|\ge1$. If $E=\emptyset$, only $s$ is reachable and the answer is immediate.

4. Steps 1 and 3 together take $O(|V||E|)$ time.
:::
