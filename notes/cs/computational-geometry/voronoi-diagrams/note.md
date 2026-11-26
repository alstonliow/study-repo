---
title: "Voronoi Diagrams"
sources: [mit6854-23]
requires: [cs/computational-geometry/randomized-incremental-hull]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 23 (Sections 1-2.2), in our own wording; the example is our own (checked by computation); proofs written out in steps. -->

Given $n$ *sites* $P=\{p_1,\dots,p_n\}$ in the plane, the Voronoi diagram divides the plane according to the nearest site. It answers nearest-neighbour queries (with a point-location structure), and from it one gets the Euclidean minimum spanning tree, the largest empty circle and the Delaunay triangulation, all in $O(n\log n)$.

::: {#def-voronoi-diagram .definition name="Voronoi cell, Voronoi diagram"}

The *Voronoi cell* of $p_i$ is
$$V(p_i)=\{x\in\mathbb R^2:\lVert x-p_i\rVert<\lVert x-p_j\rVert\ \text{for all }j\ne i\}=\bigcap_{j\ne i}h(p_i,p_j),$$
where $h(p_i,p_j)$ is the open half-plane on $p_i$'s side of the perpendicular bisector of $p_ip_j$. The *Voronoi diagram* is the subdivision of the plane into the $n$ cells, their *edges* (points equidistant from exactly two nearest sites) and *vertices* (points equidistant from three or more nearest sites).

:::

Each cell is an intersection of $n-1$ half-planes, hence a convex polygon, possibly unbounded, with at most $n-1$ sides; computing every cell this way (@sec-cs-computational-geometry-half-plane-intersection) costs $O(n^2\log n)$ in total. The structure of the diagram is described by empty circles.

::: {#lem-voronoi-empty-circle .lemma name="Vertices and edges by empty circles"}

1. $q$ is a Voronoi vertex if and only if some circle centred at $q$ has no site in its interior and at least three sites on its boundary.
2. Part of the bisector of $p_i$ and $p_j$ is a Voronoi edge if and only if some circle centred on it has no site in its interior and exactly $p_i,p_j$ on its boundary.

:::

::: {.proof}

1. For a point $q$, let $r$ be the distance to its nearest site; the circle of radius $r$ about $q$ is empty and has exactly the nearest sites on its boundary.

2. By definition $q$ is a vertex when it has at least three nearest sites, and lies on an edge between $p_i$ and $p_j$ when these are its only nearest sites. The two statements are the same facts in terms of the circle.

3. For part 2, the points with exactly $p_i,p_j$ nearest form an open set within the bisector (a slight move keeps all other sites farther), so they form a segment, ray or line of the bisector: an edge.

:::

::: {#thm-voronoi-size .theorem name="The diagram has linear size"}

If the sites are not all on a line, the diagram has at most $2n-5$ vertices and at most $3n-6$ edges.

:::

::: {.proof}

1. Add a vertex $q_\infty$ and attach every unbounded edge to it. This gives a connected planar graph with $n_v+1$ vertices, $n_e$ edges and $n$ faces (the cells).

2. Euler's formula gives $(n_v+1)-n_e+n=2$.

3. Every vertex has degree at least $3$ (including $q_\infty$, since non-collinear sites give at least three unbounded edges), so $2n_e\ge3(n_v+1)$.

4. Substituting $n_e=n_v+n-1$ from step 2: $2(n_v+n-1)\ge3n_v+3$, so $n_v\le2n-5$, and then $n_e=n_v+n-1\le3n-6$.

:::

::: {#prp-voronoi-lifting .proposition name="Voronoi diagrams from a three-dimensional polyhedron"}

Lift each site $p=(a,b)$ to $\hat p=(a,b,a^2+b^2)$ on the paraboloid $z=x^2+y^2$, and let $T_p$ be the plane tangent to the paraboloid at $\hat p$, namely $z=2ax+2by-(a^2+b^2)$. The upper envelope $Q=\{(x,y,z):z\ge\max_pT_p(x,y)\}$ is a convex polyhedron, and projecting its facets, edges and vertices vertically onto the plane gives the Voronoi cells, edges and vertices.

:::

::: {.proof}

1. For a point $x=(x,y)$ and site $p=(a,b)$, $\lVert x-p\rVert^2=(x^2+y^2)-T_p(x,y)$.

2. So the site nearest to $x$ is the one whose tangent plane is highest above $x$: the facet of $Q$ above $x$ belongs to the nearest site.

3. Ties between two (three) sites correspond to edges (vertices) of $Q$.

:::

Since $Q$ is an intersection of $n$ half-spaces, which is dual to a convex hull of $n$ points in $\mathbb R^3$, the diagram can be computed in $O(n\log n)$ by a three-dimensional hull algorithm; Fortune's sweep (@def-fortune-sweep) does it directly in the plane. Taking instead the lower convex hull of the lifted points $\hat p$ and projecting it gives the *Delaunay triangulation*, the straight-line dual of the diagram. $\Omega(n\log n)$ is a lower bound: the diagram of the sites $(x_i,\pm1)$ lists the $x_i$ in sorted order.

::: {#exm-voronoi-diagram .example name="Four sites"}

For the sites $(0,0)$, $(4,0)$, $(0,2)$ and $(4,2)$ (a rectangle), the bisectors $x=2$ and $y=1$ divide the plane into four quadrant cells, one per site. All four sites lie on the circle about $(2,1)$ of radius $\sqrt5$, so $(2,1)$ is a single vertex of degree $4$ (a degenerate case); moving $(4,2)$ to $(4,2.4)$ splits it into two vertices of degree $3$ joined by a short edge, with $n_v=2\le2\cdot4-5$ and $n_e=5\le3\cdot4-6$.

:::

::: {#fig-voronoi-diagrams-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\draw[emph] (-1.500,1.000)--(2.000,1.000);
\draw[emph] (1.830,3.900)--(2.100,1.200);
\draw[emph] (2.000,-1.500)--(2.000,1.000);
\draw[emph] (2.000,1.000)--(2.100,1.200);
\draw[emph] (2.100,1.200)--(5.500,1.200);
\node[dot] at (0.0,0.0) {};
\node[lab, below left] at (0.0,0.0) {$p_1$};
\node[dot] at (4.0,0.0) {};
\node[lab, below left] at (4.0,0.0) {$p_2$};
\node[dot] at (0.0,2.0) {};
\node[lab, below left] at (0.0,2.0) {$p_3$};
\node[dot] at (4.0,2.4) {};
\node[lab, below left] at (4.0,2.4) {$p_4$};
\node[hl dot] at (2,1) {};
\node[hl dot] at (2.1,1.2) {};
\end{tikzpicture}
\end{center}
```

The Voronoi diagram of $(0,0)$, $(4,0)$, $(0,2)$ and $(4,2.4)$: 5 edges and two vertices (highlighted), the centres $(2,1)$ and $(2.1,1.2)$ of empty circles through three sites.

:::
