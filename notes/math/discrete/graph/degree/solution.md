<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-graph-1-03" status="draft"}
Let $G$ have $n\ge2$ vertices. Every degree lies in $\{0,1,\dots,n-1\}$.

1. *Case 1: $G$ has an isolated vertex $u$.* Then no vertex $v$ has degree
   $n-1$, because such a $v$ would be adjacent to every other vertex,
   including $u$. So all $n$ degrees lie in $\{0,\dots,n-2\}$.

2. *Case 2: $G$ has no isolated vertex.* Then every degree is at least $1$,
   so all $n$ degrees lie in $\{1,\dots,n-1\}$.

3. In both cases, $n$ degrees take at most $n-1$ different values. By the
   pigeonhole principle, two vertices have the same degree.
:::

::: {.solution for="prob-graph-1-04" status="draft"}
Caffeine has $8$ carbon, $10$ hydrogen, $4$ nitrogen and $2$ oxygen atoms, so
$24$ vertices. The degree sum is
$$8\cdot4 + 10\cdot1 + 4\cdot3 + 2\cdot2 = 32 + 10 + 12 + 4 = 58.$$

(a) By the Handshaking Lemma, the number of edges is $58/2 = 29$.

(b) The average degree is $58/24 = 29/12\approx 2.42$.
:::

::: {.solution for="prob-graph-2-13" status="draft"}
(a) $K_4$, with $4$ vertices. A 3-regular graph needs at least $4$ vertices,
    and $K_4$ is planar (Exercise 10(c)).

(b) The cube $Q_3$, with $8$ vertices. In a 3-regular bipartite graph with parts
    $X$ and $Y$, counting edges from each side gives $3|X| = m = 3|Y|$, so the
    parts have equal size, and each part has at least $3$ vertices. With parts of size $3$ the graph is $K_{3,3}$,
    which is not planar. With parts of size $4$, $Q_3$ works.

(c) $K_{3,3}$, with $6$ vertices. A 3-regular graph has an even number of
    vertices. The only one with $4$ vertices is $K_4$, which is planar.

(d) The *antiprisms*. For $n\ge3$, take two $n$-cycles $u_0\cdots u_{n-1}$
    and $l_0\cdots l_{n-1}$, and join $u_i$ to $l_i$ and to $l_{i+1}$
    (indices mod $n$). Each vertex has $2$ cycle neighbours and $2$ others,
    so the graph is 4-regular and connected. Drawing one cycle inside the
    other, with the zigzag of edges between them, shows it is planar.
    ($n = 3$ gives the octahedron.)

(e) $12$. A 5-regular graph has $m = 5n/2$ edges. Planarity requires
    $m\le3n-6$, so $5n/2\le 3n-6$, which gives $n\ge12$. The icosahedron is
    5-regular, planar and has $12$ vertices.

(f) No. A 6-regular graph has $m = 3n > 3n-6$ edges, which violates
    $m\le 3n-6$. Equivalently, its average degree is $6$, contradicting
    Exercise 11(a).
:::
