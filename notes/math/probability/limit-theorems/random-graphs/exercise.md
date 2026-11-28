::: {.problem #prob-eecs126hw-10-q1 origin="external" source="eecs126hw-10-q1"}
**Random Graph Estimation.** Consider a random graph on $n$ vertices in which each edge appears independently with probability $p$. Let $D$ be the average degree of a vertex in the graph. Compute the maximum likelihood estimator of $p$ given $D$. You may approximate $\text{Binomial}(n,p)=\text{Poisson}(np)$.
:::

::: {.problem #prob-eecs126d-2-q3 origin="external" source="eecs126d-2-q3"}
**Clustering Coefficient.** This problem will explore an important probabilistic concept of clustering that is widely used in machine learning applications today. Consider $n$ students, where $n$ is a positive integer. For each pair of students $i,j\in\{1,\dots,n\}$, $i\ne j$, they are friends with probability $p$, independently of other pairs. We assume that friendship is mutual. We can see that the friendship among the $n$ students can be represented by an undirected graph $G$. Let $N(i)$ be the number of friends of student $i$ and $T(i)$ be the number of triangles attached to student $i$. We define the clustering coefficient $C(i)$ for student $i$ as follows:
$$C(i)=\frac{T(i)}{\binom{N(i)}{2}}.$$
```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (1) at (0,1.2) {$1$};
\node[small vertex] (2) at (1.3,1.6) {$2$};
\node[small vertex] (3) at (1.3,0.3) {$3$};
\node[small vertex] (4) at (2.6,1.2) {$4$};
\node[small vertex] (5) at (1.3,-1.0) {$5$};
\draw (3)--(1);
\draw (3)--(2);
\draw (3)--(4);
\draw (3)--(5);
\draw (1)--(2);
\draw (2)--(4);
\end{tikzpicture}
\end{center}
```

The clustering coefficient is not defined for the students who have no friends. An example is shown in Figure ??. Student 3 has 4 friends (1, 2, 4, 5) and there are two triangles attached to student 3, i.e., triangle 1-2-3 and triangle 2-3-4. Therefore $C(3)=2/\binom42=1/3$.

Find $E[C(i)\mid N(i)\ge2]$.

:::

::: {#prob-gnp-components-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-random-graphs"}
Write two functions for experiments with $G(n,p)$ (@def-erdos-renyi-graph), on vertices $0,\dots,n-1$:

- `gnp(n, p, rng)` samples the graph and returns its edges as pairs `(i, j)` with `i < j`. Use `rng.random()` (a `random.Random`) once for each of the $\binom n2$ possible edges.
- `component_sizes(n, edges)` returns the sizes of the connected components of a graph, largest first.

The tests check the mean number of edges, the giant component for $np=3$, and the isolated vertices below the connectivity threshold (@thm-connectivity-threshold).

```{.python .starter}
import random


def gnp(n, p, rng):
    """Sample G(n, p) on vertices 0..n-1: return its edges as pairs (i, j), i < j.
    Use rng.random() once for each of the n(n-1)/2 possible edges."""
    ...


def component_sizes(n, edges):
    """Sizes of the connected components of the graph on 0..n-1, largest first."""
    ...
```

```{.python .tests}
import math
import random


def test_component_sizes():
    assert component_sizes(5, []) == [1, 1, 1, 1, 1]
    assert component_sizes(6, [(0, 1), (1, 2), (3, 4)]) == [3, 2, 1]
    assert component_sizes(4, [(0, 1), (2, 3), (1, 2), (0, 3)]) == [4]
    assert component_sizes(0, []) == []


def test_extreme_p():
    assert gnp(6, 0, random.Random(0)) == []
    assert sorted(gnp(5, 1, random.Random(0))) == [(i, j) for i in range(5) for j in range(i + 1, 5)]


def test_edges_are_valid():
    edges = gnp(30, 0.3, random.Random(1))
    assert all(0 <= i < j < 30 for i, j in edges)
    assert len(set(edges)) == len(edges)


def test_mean_number_of_edges():
    # E = p * C(n, 2) = 43.5; the mean of 300 graphs has standard error about 0.36
    rng = random.Random(2)
    mean = sum(len(gnp(30, 0.1, rng)) for _ in range(300)) / 300
    assert abs(mean - 43.5) < 1.8, mean


def test_giant_component():
    # np = 3 > 1: one component holds most vertices (about 94% in the limit)
    sizes = component_sizes(400, gnp(400, 3 / 400, random.Random(3)))
    assert sizes[0] > 300 and sizes[1] < 20, sizes[:3]


def test_below_connectivity_threshold():
    # p = 0.5 ln(n) / n: about sqrt(n) isolated vertices, so not connected
    n = 300
    sizes = component_sizes(n, gnp(n, 0.5 * math.log(n) / n, random.Random(4)))
    assert sizes.count(1) >= 5
```
:::

::: {#prob-min-bisection-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-random-graphs"}
In the *stochastic block model*, $n$ vertices (with $n$ even) are split into two hidden communities of $n/2$. Each edge is present independently, with probability $p$ inside a community and $q<p$ between communities. Given the graph, a split into two halves $A$ and $A^c$ with $c$ crossing edges has likelihood proportional to $\bigl(\tfrac{q(1-p)}{p(1-q)}\bigr)^{c}$, and this decreases in $c$. So the maximum-likelihood split is a *minimum bisection*: a split into halves with the fewest crossing edges.

Write `min_bisection(n, edges)`, which returns a minimum bisection as the `frozenset` $A$ of $n/2$ vertices that contains vertex $0$. Search all splits; the tests use $n\le12$.

```{.python .starter}
from itertools import combinations


def min_bisection(n, edges):
    """For an even n, return a frozenset A of n/2 vertices of 0..n-1 that contains
    vertex 0 and minimises the number of edges with one end in A and one outside."""
    ...
```

```{.python .tests}
import random


def cut(edges, A):
    return sum((i in A) != (j in A) for i, j in edges)


def test_two_triangles():
    edges = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (2, 3)]
    assert min_bisection(6, edges) == frozenset({0, 1, 2})


def test_vertex_zero_on_the_other_side():
    edges = [(0, 4), (4, 5), (0, 5), (1, 2), (2, 3), (1, 3), (5, 1)]
    assert min_bisection(6, edges) == frozenset({0, 4, 5})


def test_shape_and_optimality_on_a_cycle():
    edges = [(i, (i + 1) % 8) for i in range(8)]
    A = min_bisection(8, edges)
    assert len(A) == 4 and 0 in A and cut(edges, A) == 2


def test_two_vertices():
    assert min_bisection(2, [(0, 1)]) == frozenset({0})


def sbm(n, p, q, rng):
    """Two communities {0..n/2-1} and {n/2..n-1}; edge probability p inside, q across."""
    half = n // 2
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if rng.random() < (p if (i < half) == (j < half) else q)]


def test_recovers_planted_communities():
    for seed in range(3):
        edges = sbm(12, 0.8, 0.1, random.Random(seed))
        assert min_bisection(12, edges) == frozenset(range(6)), seed
```
:::
