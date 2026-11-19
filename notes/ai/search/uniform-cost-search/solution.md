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

::: {.solution for="prob-ucs-route-code" status="draft"}
```{.python}
import heapq
from itertools import count


def ucs(start, succ, is_end):
    """Return (cost, path) of a cheapest path from start to an end state,
    or None if no end state is reachable."""
    tie = count()                      # states need not be comparable
    frontier = [(0, next(tie), start)]
    best = {start: 0}                  # lowest priority seen so far
    back = {start: None}               # backpointers
    explored = set()
    while frontier:
        p, _, s = heapq.heappop(frontier)
        if s in explored:              # an outdated entry: s was lowered later
            continue
        explored.add(s)
        if is_end(s):
            path = []
            while s is not None:
                path.append(s)
                s = back[s]
            return p, path[::-1]
        for t, c in succ(s):
            if t not in explored and p + c < best.get(t, float("inf")):
                best[t] = p + c
                back[t] = s
                heapq.heappush(frontier, (p + c, next(tie), t))
    return None
```

1. The frontier is a binary heap of entries (priority, counter, state). Instead of lowering a priority in place, a new entry is pushed and the outdated one is skipped when it is removed; this is the same algorithm as @def-uniform-cost-search.
2. The counter breaks ties, so that states themselves are never compared (two `frozenset`s, for example, do not have a total order).
3. A state is explored when it is first removed; its priority is then its past cost (@thm-uniform-cost-search). The end test happens at removal, not when a state is first reached: stopping at the first push would return the path $A\to B\to D$ of cost $6$ in the small test graph.
4. For waypoints nothing changes in the search: the state records which waypoints have been visited, so reaching the same location with a different set of visited waypoints is a different state.
:::
