<!-- Draft solutions (status="draft") written by Claude. CN chapter 12 has no
     sample solutions, so these were not checked against one. Owner to review. -->

::: {.solution for="prob-graph-2-09"}
Draw $K_{2,n}$ with straight edges as follows.

1. Put the two vertices of the first part at $(0,1)$ and $(0,-1)$, and the
   $n$ vertices of the second part at $(1,0),(2,0),\dots,(n,0)$.

2. Join $(0,1)$ and $(0,-1)$ to every $(i,0)$ by straight segments.

3. A segment from $(0,1)$ lies in the upper half-plane $y\ge0$, and one from
   $(0,-1)$ lies in $y\le0$. So two such segments can only meet on the
   $x$-axis, that is, at a shared endpoint $(i,0)$.

4. Two segments from the same point $(0,\pm1)$ to different points on the
   axis meet only at $(0,\pm1)$.

5. So no two edges cross, and $K_{2,n}$ is planar.
:::

::: {.solution for="prob-graph-2-10"}
In each case $n - m + f = 2$, where $f$ counts the outer face:

| graph | $n$ | $m$ | $f$ | $n-m+f$ |
|---|---|---|---|---|
| $C_n$ | $n$ | $n$ | $2$ (inside, outside) | $2$ |
| $W_n$ | $n+1$ | $2n$ | $n+1$ ($n$ triangles, outside) | $2$ |
| $K_4$ | $4$ | $6$ | $4$ | $2$ |
| $Q_3$ | $8$ | $12$ | $6$ | $2$ |
| octahedron | $6$ | $12$ | $8$ | $2$ |
| dodecahedron | $20$ | $30$ | $12$ | $2$ |
| icosahedron | $12$ | $30$ | $20$ | $2$ |

For the solids, the faces of the plane drawing are the faces of the solid (one
of them becomes the outer face).
:::

::: {.solution for="prob-graph-2-11"}
Let $G$ be planar with $n\ge3$ vertices and $m$ edges; the average degree is
$2m/n$.

(a) Every face of a plane drawing is bounded by at least $3$ edges, so
    $m\le3n-6$. Hence
    $$\frac{2m}{n}\le 6 - \frac{12}n < 6.$$

(b) With no triangles, every face is bounded by at least $4$ edges, so
    $m\le 2n-4$ and
    $$\frac{2m}{n}\le 4 - \frac8n < 4.$$

(c) A bipartite graph has no odd cycles, in particular no triangles, so the
    bound $< 4$ from (b) applies.
:::

::: {.solution for="prob-graph-2-12"}
1. If $G$ has at most $2$ vertices, every degree is at most $1$.

2. Otherwise, by Exercise 11(a), the average degree of $G$ is less than $6$.

3. A minimum degree is at most the average, so some vertex has degree less
   than $6$, that is, at most $5$.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-3-q4" status="draft"}
(a)

1. Suppose $K_{3,3}$ ($v=6$, $e=9$) had a plane drawing, with $f$ faces. By Euler's formula, $f=2-v+e=5$.

2. $K_{3,3}$ is bipartite, so it has no odd cycles, in particular no triangles; every face is bounded by at least $4$ edges. Each edge borders at most $2$ faces, so $4f\le2e$, that is, $20\le18$. Contradiction.

(b)

1. Suppose $G$ has $n\ge7$ vertices, property $T$, and is planar.

2. Property $T$ says that among any three vertices at most one pair is a non-edge. So no vertex has two non-neighbours: if $u$ had non-neighbours $w_1,w_2$, the triple $u,w_1,w_2$ would have at most one edge. Hence every vertex has degree at least $n-2$.

3. So $e\ge\frac{n(n-2)}2$. A planar graph with $n\ge3$ vertices has $e\le3n-6$ (@sec-math-discrete-graph-planarity). Then $n(n-2)\le6n-12$, i.e. $(n-2)(n-6)\le0$, so $n\le6$. This contradicts $n\ge7$.
:::

::: {.solution for="prob-cs70hw-3-q5" status="draft"}
(a) Either. $K_4$ is planar and $4$-colourable; $K_{3,3}$ is $2$-colourable (it is bipartite) but non-planar.

(b) Always non-planar. By the four colour theorem every planar graph can be coloured with $4$ colours, so a graph needing $7$ colours is not planar.

(c) Either. A triangle has $e=3\le3$ and is planar. $K_{3,3}$ has $e=9\le12$ and is non-planar.

(d) Always planar. A connected graph with all degrees at most $2$ is a single vertex, a path or a cycle, and each can be drawn in the plane without crossings.

(e) Always planar. Each connected component is as in (d); draw the components side by side.
:::
