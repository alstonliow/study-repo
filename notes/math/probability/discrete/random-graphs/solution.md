<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-10-q1" status="draft"}
The MLE is $\hat p=\frac{D}{n-1}\approx\frac Dn$.

1. Each edge adds $2$ to the total degree, so $D=\frac{2E}{n}$, where $E\sim\text{Bin}(\binom n2,p)$ is the number of edges (@def-erdos-renyi-graph). Observing $D$ is the same as observing $E=e$.
2. Approximating $E$ by $\text{Poisson}(\binom n2p)$, the log-likelihood is $-\binom n2p+e\ln p+\text{const}$, maximised where $-\binom n2+\frac ep=0$.
3. So $\hat p=\frac{e}{\binom n2}=\frac{nD/2}{n(n-1)/2}=\frac{D}{n-1}$. The exact binomial likelihood $p^e(1-p)^{\binom n2-e}$ gives the same maximiser.
:::

::: {.solution for="prob-eecs126d-2-q3" status="draft"}
The answer is $p$.

1. Condition on the set $F$ of friends of $i$, with $|F|=k\ge2$. A triangle at $i$ is a pair in $F$ that are friends with each other, so $T(i)$ counts the edges among $F$.
2. Those $\binom k2$ edges are independent of the edges at $i$ (@def-erdos-renyi-graph), so given $F$, $T(i)\sim\text{Bin}(\binom k2,p)$ and $E[C(i)\mid F]=p$.
3. This does not depend on $F$, so averaging over all $F$ with $|F|\ge2$ gives $E[C(i)\mid N(i)\ge2]=p$. (In $G(n,p)$ a friend of a friend is no more likely to be a friend than anyone else.)
:::

::: {.solution for="prob-gnp-components-code" status="draft"}
```{.python}
import random


def gnp(n, p, rng):
    """Sample G(n, p) on vertices 0..n-1: return its edges as pairs (i, j), i < j.
    Use rng.random() once for each of the n(n-1)/2 possible edges."""
    return [(i, j) for i in range(n) for j in range(i + 1, n) if rng.random() < p]


def component_sizes(n, edges):
    """Sizes of the connected components of the graph on 0..n-1, largest first."""
    parent = list(range(n))                     # union-find
    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for i, j in edges:
        parent[find(i)] = find(j)
    sizes = {}
    for v in range(n):
        r = find(v)
        sizes[r] = sizes.get(r, 0) + 1
    return sorted(sizes.values(), reverse=True)
```

1. Sampling: one independent Bernoulli($p$) trial per pair $i<j$, in a fixed order, so a seed fixes the graph.
2. Components: a union–find structure. Each vertex points to a parent; `find` follows the pointers to the root of its component, halving the path on the way, and each edge joins the two roots.
3. Count the vertices under each root and sort the counts in decreasing order. The work is almost linear in $n$ plus the number of edges.
:::

::: {.solution for="prob-min-bisection-code" status="draft"}
```{.python}
from itertools import combinations


def min_bisection(n, edges):
    """For an even n, return a frozenset A of n/2 vertices of 0..n-1 that contains
    vertex 0 and minimises the number of edges with one end in A and one outside."""
    best, best_cut = None, None
    for rest in combinations(range(1, n), n // 2 - 1):   # fixing 0 in A halves the work
        A = frozenset((0,) + rest)
        cut = sum((i in A) != (j in A) for i, j in edges)
        if best_cut is None or cut < best_cut:
            best, best_cut = A, cut
    return best
```

1. Fixing vertex $0$ in $A$ counts each split once: choose the other $n/2-1$ members of $A$ from $1,\dots,n-1$, which gives $\binom{n-1}{n/2-1}$ splits ($462$ for $n=12$).
2. For each split, count the edges with exactly one end in $A$ and keep the smallest count; ties keep the first split found.
3. The likelihood claim: the number of edges inside the communities is $e-c$, where $e$ is fixed by the graph, and there are $2\binom{n/2}{2}$ pairs inside and $(n/2)^2$ across, whatever the split. So the likelihood is $p^{e-c}(1-p)^{2\binom{n/2}2-e+c}q^{c}(1-q)^{(n/2)^2-c}$, which is a constant times $\bigl(\tfrac{q(1-p)}{p(1-q)}\bigr)^{c}$.
:::
