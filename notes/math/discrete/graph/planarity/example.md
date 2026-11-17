<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Section 12.7 (mcs-12.7), in our own wording. -->

::: {#exm-platonic-solids .example name="There are only five regular polyhedra" level="medium"}
A convex polyhedron in which every face is a regular $n$-gon and $m$ faces meet at every vertex ($m,n\ge3$) gives, by projecting it onto a sphere and then the plane, a connected planar graph with $v$ vertices of degree $m$, $e$ edges and $f$ faces of $n$ sides.

1. Counting edge ends at vertices and edge sides along faces, $mv=2e$ and $nf=2e$.

2. Euler's formula (@thm-euler-s-theorem-cn-thm) gives $\frac{2e}m-e+\frac{2e}n=2$, so
   $$\frac1m+\frac1n=\frac12+\frac1e>\frac12.$$

3. With $m,n\ge3$, this leaves only $(m,n)=(3,3),(3,4),(4,3),(3,5),(5,3)$: if both are at least $4$, the left side is at most $\frac12$; if one is $3$, the other must be less than $6$.

4. Solving for $e$ gives the tetrahedron ($e=6$), the cube ($m=3,n=4$, $e=12$), the octahedron ($m=4,n=3$, $e=12$), the dodecahedron ($m=3,n=5$, $e=30$) and the icosahedron ($m=5,n=3$, $e=30$). All five exist.
:::
