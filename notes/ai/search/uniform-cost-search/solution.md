<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-3-q1" status="draft"}
**(a)** The minimum cost is
$$n+\frac{m(m+1)}{2}.$$

1. Lower bound, east moves: the path must cross from $x=j$ to $x=j+1$ at least once for each $j=0,\dots,m-1$, and that east move costs $1+j$. Together these cost at least $\sum_{j=0}^{m-1}(1+j)=m(m+1)/2$.
2. Lower bound, north moves: the path needs at least $n$ vertical moves, each costing at least $1$.
3. The path that goes north $n$ times at $x=0$ (cost $1$ each) and then east $m$ times (costs $1,2,\dots,m$) meets both bounds.
4. Uniqueness: equality forces no west or south moves and every vertical move to cost exactly $1$, i.e. to be made at $x=0$, before the first east move. So this path is the unique minimum-cost path.

**(b)**

1. False. Costs are at least $1$, so only finitely many states have past cost below the optimum and UCS reaches the end state after finitely many steps.
2. False. UCS also explores cheap locations outside the rectangle, for example $(-1,0)$ or $(0,-1)$, each of past cost $1$.
3. True. UCS returns a minimum-cost path, and it pops states in order of past cost, so every state it explores has past cost at most that of $(m,n)$.

**(c)**

1. True. Every path of the old graph still exists, so the minimum cannot increase.
2. False. The action may lie on no path from the start to the end, and with a negative cost UCS is no longer guaranteed to be correct at all.
3. False. Adding $1$ to every action adds the number of steps to each path's cost, which favours paths with fewer edges. Example: a path of two edges of cost $1$ (total $2$) beats a single edge of cost $3$, but after the change they cost $4$ and $4$, and with a single edge of cost $2.5$ instead, the single edge wins ($3.5<4$).
:::
