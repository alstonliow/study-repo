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
