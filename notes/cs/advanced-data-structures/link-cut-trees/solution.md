<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-3-q3" status="draft"}
*1. The argument is wrong.* All edges from $S$ to $\bar S$ are saturated, but edges from $\bar S$ back to $S$ may carry flow, so the net flow across the cut is smaller than its capacity. Example: edges $s\to a$, $a\to b$, $b\to t$, $s\to b$, $a\to t$, all of capacity $1$, and one unit along $s\,a\,b\,t$. Every $s$–$t$ path ($sabt$, $sat$, $sbt$) has a saturated edge, so the flow is blocking, with value $1$; but the maximum flow is $2$ ($sat$ and $sbt$). Here $S=\{s,b\}$, the cut has capacity $2$ and the edge $a\to b$ carries one unit back into $S$.

*2. With dynamic trees* (@def-dynamic-tree-operations). Keep a forest whose tree edges are edges $(v,w)$ of $G$ not yet saturated or discarded, with $w$ the parent of $v$ and cost of $v$ = residual capacity of $(v,w)$.

1. Let $v=$ `find-root(s)`.
2. If $v=t$: $\delta\gets$ `find-cost(find-min(s))`; `add-cost(s, -δ)` pushes $\delta$ along the tree path from $s$ to $t$; then while `find-cost(find-min(s))` is $0$, record that edge as saturated and `cut` it.
3. Else, if $v$ has an unused outgoing edge $(v,w)$: `link(w, v, c(v,w))` (makes $w$ the parent of $v$).
4. Else $v$ is a dead end: if $v=s$ stop; otherwise, for every tree child $x$ of $v$, record the flow $c(x,v)-$`find-cost(x)` and `cut(x)`, and delete $v$ with its incoming edges from the graph.

At the end, read off the flow on the remaining tree edges. Since $G$ is acyclic, linking never closes a cycle. Every edge is linked at most once and then leaves the forest at most once (saturated, or its head deleted), each augmentation saturates an edge, and each step does $O(1)$ tree operations per edge event. So there are $O(m)$ operations of $O(\log n)$ amortized (@thm-link-cut-trees): $O(m\log n)$. When the loop stops every $s$–$t$ path has lost an edge, which was saturated or led to a dead end, so the flow is blocking.
:::
