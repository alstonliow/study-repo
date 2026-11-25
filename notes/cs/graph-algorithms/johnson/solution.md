<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-6-q6" status="draft"}
The following self-contained version follows @def-johnson. Starting all potentials at $0$ is the same as running Bellman–Ford from an added vertex $x$ with $0$-weight edges to every vertex, after its first round. Dijkstra uses Python's `heapq` with "lazy deletion" (stale entries are skipped) instead of `decrease_key`, which keeps the $O(|E|\log|V|)$ bound.

```python
import heapq
INF = float('inf')

def johnson(n, S):
    adj = [[] for _ in range(n)]
    for (u, v, w) in S:
        adj[u].append((v, w))
    # Bellman-Ford from a new vertex x joined to every vertex by weight 0:
    # start every h at 0 and relax all edges n times (x adds n + 1 vertices).
    h = [0] * n
    for _ in range(n):
        changed = False
        for u in range(n):
            for v, w in adj[u]:
                if h[u] + w < h[v]:
                    h[v] = h[u] + w
                    changed = True
        if not changed:
            break
    else:
        for u in range(n):                  # one more round: still improving?
            for v, w in adj[u]:
                if h[u] + w < h[v]:
                    return None             # negative-weight cycle
    D = []
    for s in range(n):                      # Dijkstra with w'(u,v) = w + h(u) - h(v) >= 0
        d = [INF] * n
        d[s] = 0
        Q = [(0, s)]
        while Q:
            du, u = heapq.heappop(Q)
            if du > d[u]:
                continue                    # stale queue entry
            for v, w in adj[u]:
                nd = du + w + h[u] - h[v]
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(Q, (nd, v))
        D.append(tuple(d[v] - h[s] + h[v] if d[v] < INF else INF for v in range(n)))
    return tuple(D)
```

It was checked against Floyd–Warshall (@thm-floyd-warshall) on random graphs with negative weights, including graphs with negative-weight cycles.
:::

::: {.solution for="prob-mit6046-11-q1" status="draft"}
Let $x_i=\delta(s,i)$, and let $y$ be any solution of the system.

1. *$x$ is a solution.* For a constraint edge $i\to j$, the triangle inequality gives $\delta(s,j)\le\delta(s,i)+b_{ij}$, that is, $x_j-x_i\le b_{ij}$.

2. *$\max_ix_i\le0$.* The edge $s\to i$ of weight $0$ gives $x_i\le0$.

3. *Shift $y$.* Adding the same constant to all $y_i$ keeps every difference, so we may assume $\max_iy_i=0$.

4. *$y_i\le x_i$ for all $i$.* Put $y_s=0$; then $y_i-y_s\le0$ holds for the edges out of $s$ too. Along any path $s=u_0,u_1,\dots,u_k=i$, summing the constraints of its edges gives $y_i\le$ the weight of the path. Taking a shortest path, $y_i\le\delta(s,i)=x_i$.

5. *Compare spreads.* By step 4, $\min_iy_i\le\min_ix_i$. By steps 2 and 3, $\max_ix_i\le0=\max_iy_i$. Hence $\max_ix_i-\min_ix_i\le\max_iy_i-\min_iy_i$, so the Bellman–Ford solution has the smallest spread of all solutions.
:::
