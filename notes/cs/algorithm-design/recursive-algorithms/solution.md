<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-7-q1" status="draft"}
Campaigning on day $i$ gains $g_i=d_i-z_i>0$ delegates, and campaign days must be at least $3$ apart. Rep. Torr can win iff the largest possible total gain $G$ satisfies $\sum_iz_i+G\ge\lfloor D/2\rfloor+1$.

1. *Subproblems:* $x(i)$, the largest total gain using only days $i,\dots,n$, for $1\le i\le n+3$.
2. *Relation:* either do not campaign on day $i$, or campaign and skip the next two days: $x(i)=\max\{x(i+1),\ g_i+x(i+3)\}$.
3. *Order:* decreasing $i$; $x(i)$ depends only on larger indices.
4. *Base:* $x(n+1)=x(n+2)=x(n+3)=0$.
5. *Original:* $G=x(1)$; compare as above (computing $D$ and $\sum z_i$ in $O(n)$).
6. *Time:* $O(n)$ subproblems with $O(1)$ work: $O(n)$.
:::

::: {.solution for="prob-mit6006s20-7-q3" status="draft"}
Expand the subproblems with the parity of the weight so far.

1. *Subproblems:* $x(v,p)$, the number of paths from $s$ to $v$ whose weight has parity $p\in\{0,1\}$, for $v\in V$.
2. *Relation:* guess the last edge $(u,v)$: $x(v,p)=\sum_{u\in\operatorname{Adj}^-(v)}x\bigl(u,(p-w(u,v))\bmod2\bigr)$ for $v\ne s$.
3. *Order:* a topological order of $G$ (@thm-dfs-topological-sort); every edge goes forward, so the relation is acyclic.
4. *Base:* $x(s,0)=1$ (the path of length $0$) and $x(s,1)=0$; since $G$ is acyclic no path returns to $s$.
5. *Original:* $x(t,1)$.
6. *Time:* $\sum_vO(1+\deg^-(v))=O(|V|+|E|)$, plus the topological sort.
:::
