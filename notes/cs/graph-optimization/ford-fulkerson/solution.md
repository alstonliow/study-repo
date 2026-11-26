<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-7-q1" status="draft"}
(a) By max-flow min-cut (@thm-max-flow-min-cut) the maximum flow equals the minimum cut capacity. Changing $c(u,v)$ by $k$ changes the capacity of every cut by $0$ or by exactly $k$ (depending on whether $(u,v)$ crosses it), in the same direction. So the minimum over all cuts changes by at most $k$ in that direction. Statements 1 and 3 are the case $k=1$.

(b) $f$ is still a feasible flow. Starting from it, run Ford–Fulkerson (@def-ford-fulkerson): search for an augmenting path by BFS in $O(V+E)$ and push $1$ unit (capacities are integers). By (a) the maximum grew by at most $k$, so after at most $k$ augmentations no augmenting path exists, and the flow is maximum. Time $O(k(V+E))$, plus one final search.

(c) If $f(u,v)\le r$, then $f$ is feasible for $c'$, and since the maximum cannot grow, it is still maximum. Otherwise let $d=f(u,v)-r\le k$. Repeat $d$ times: in the graph of edges carrying positive flow, find a path from $s$ to $u$ and a path from $v$ to $t$ (they exist by flow conservation, and are found by DFS in $O(V+E)$); decrease the flow by $1$ along $s\to u$, $(u,v)$ and $v\to t$. (If the flow through $(u,v)$ is on a cycle, cancel the cycle instead.) The result is feasible for $c'$ with value $|f|-d$. Then run at most $d$ augmentations as in (b) to restore maximality; the new maximum is at least $|f|-k$ by (a) and at most $|f|$. Time $O(k(V+E))$.
:::

::: {.solution for="prob-mit6854ps-1-q3" status="draft"}
Let $\delta(v)$ be the BFS distance from $s$ in $G_f$ and call a residual edge $(u,v)$ *forward* if $\delta(v)=\delta(u)+1$. Shortest $s$–$t$ paths use only forward edges.

*(a)* Augmenting along a shortest path removes some forward edges and adds reverse edges $(v,u)$ of path edges $(u,v)$, which go from level $\delta(u)+1$ down to $\delta(u)$. Every residual edge, old or new, still goes up by at most one level, so every $s$–$v$ path in the new residual graph has at least $\delta(v)$ edges: no distance decreases, in particular not $\delta(t)$.

*(b)* Suppose $\delta(t)=L$ stays the same for a while. An $s$–$t$ path of length $L$ must climb one level per edge, so it uses only edges that go up exactly one level; by (a) the levels never decrease, and new edges go downwards, so such paths use only edges that were forward edges of the residual graph when the length first became $L$. Each augmentation saturates (deletes) at least one of them, and none comes back while the length is $L$ (a reappearing edge would be the reverse of a path edge, going down). An edge of $G$ and its reverse cannot both go up one level, so there are at most $m$ such edges, and after at most $m$ augmentations no path of length $L$ remains: the length increases.

*(c)* The length lies between $1$ and $n-1$ and increases at least every $m$ augmentations, so there are $O(nm)$ augmentations.

*(d)* Each augmentation is one BFS plus a pass along the path, $O(m)$. Total $O(nm^2)$. (This is @thm-edmonds-karp.)
:::

::: {.solution for="prob-mit6854ps-1-q4" status="draft"}
*(a)* By max-flow min-cut (@thm-max-flow-min-cut) the maximum flow value is the minimum cut capacity. Raising some capacities by $1$ raises the capacity of every cut by at most the number of its edges, at most $m$; so the minimum cut, and the maximum flow, grow by at most $m$. Starting Ford–Fulkerson from $f$ (still feasible), every augmentation adds at least $1$ (integral data), so at most $m$ augmentations of $O(m)$ each: $O(m^2)$ time.

*(b)*

1. Solve the instance $j=k$ from $f=0$: capacities are $0$ or $1$, the maximum flow is at most $m$, so $O(m)$ augmentations, $O(m^2)$ time.

2. Given a maximum flow $f_j$ for $u_j$, note $u_{j-1}=2u_j$ or $2u_j+1$ on each edge. The flow $2f_j$ is feasible for $2u_j$ and maximum there (all cut capacities double, so the minimum cut does too). The capacities $u_{j-1}$ are $2u_j$ plus $1$ on some edges, so by (a) $O(m)$ augmentations starting from $2f_j$ give a maximum flow $f_{j-1}$ for $u_{j-1}$.

3. Continue down to $j=0$, the original instance. There are $k+1=O(\log U)$ phases of $O(m)$ augmentations each, each $O(m)$: total $O(m^2\log U)$, polynomial.
:::

::: {.solution for="prob-mit6854ps-2-q1" status="draft"}
Call $\min_{e\in P}l(e)$ the *width* of $P$; removing a cycle from a walk never lowers its width, so the best walk width equals the best simple path width.

*(a)* Keep labels $b(v)$, with $b(s)=+\infty$ and $b(v)=-\infty$ otherwise. Repeatedly extract an unprocessed vertex $v$ of largest $b(v)$, mark it processed, and for each edge $(v,w)$ set $b(w)\gets\max\big(b(w),\min(b(v),l(v,w))\big)$, remembering $v$ as $w$'s parent when the label improves. The parents give the path.

1. Every label is the width of some path from $s$, so $b(v)\le\beta(v)$, the optimum.

2. Suppose some $v$ is extracted with $b(v)<\beta(v)$, the first such. Take an optimal path to $v$, and on it the first unprocessed vertex $y$ with predecessor $x$ (processed, so $b(x)=\beta(x)\ge\beta(v)$ by the choice of $v$, and widths only shrink along a path). When $x$ was processed, $b(y)$ became at least $\min(b(x),l(x,y))\ge\beta(v)>b(v)$.

3. But $v$ was extracted before $y$, so $b(v)\ge b(y)$: a contradiction. Hence every extracted label is optimal.

*(b)* Labels other than $\pm\infty$ are edge lengths, integers in $1..m$. Keep an array of $m$ buckets (doubly linked lists) indexed by label, plus a pointer $j$. The extracted labels never increase (a new label $\min(b(v),l)$ is at most the label just extracted), so to extract a maximum, move $j$ downwards to the next non-empty bucket. Raising a label moves a vertex between buckets in $O(1)$. The pointer moves at most $m$ times in all, each edge is relaxed once, and each vertex extracted once: $O(m+n)$, which is $O(m)$ when every vertex is reachable.
:::

::: {.solution for="prob-mit6854ps-2-q2" status="draft"}
*(a)* The width of a path depends only on the *order* of the capacities, not their values. Replace each residual capacity by its rank $1,\dots,m'$ in the given order ($m'\le2m$ residual edges, equal capacities get equal ranks). A path of largest minimum rank is a fattest path, and by part (b) of the previous problem it is found in $O(m)$ with bucket lists.

*(b)* Pushing $\delta$ along the path $P$:

1. residual capacities of the edges of $P$ drop by $\delta$ (some become $0$ and leave);
2. those of the reverse edges of $P$ grow by $\delta$ (some appear);
3. all others are unchanged.

Within each group the order is preserved, since all members change by the same amount. So the new order is the merge of three sorted lists: the unchanged edges (the old order with $P$ and its reverses deleted), the edges of $P$ shifted down, and the reverse edges shifted up. Deleting and merging take $O(m)$.

*(c)* Sort once, $O(m\log m)$. By @thm-fattest-augmenting-path there are $O(m\log(nU))$ augmentations, each $O(m)$: total $O(m^2\log(nU))$.
:::
