<!-- Draft solutions (status="draft") written by Claude. CN chapter 12 has no
     sample solutions, so these were not checked against one. Owner to review. -->

::: {.solution for="prob-graph-2-09" status="draft"}
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

::: {.solution for="prob-graph-2-10" status="draft"}
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

::: {.solution for="prob-graph-2-11" status="draft"}
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

::: {.solution for="prob-graph-2-12" status="draft"}
1. If $G$ has at most $2$ vertices, every degree is at most $1$.

2. Otherwise, by Exercise 11(a), the average degree of $G$ is less than $6$.

3. A minimum degree is at most the average, so some vertex has degree less
   than $6$, that is, at most $5$.
:::
