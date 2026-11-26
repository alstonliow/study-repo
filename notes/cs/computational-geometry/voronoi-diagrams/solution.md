<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-6-q2" status="draft"}
1. Compute the Voronoi diagram of $Q$ in $O(n\log n)$ (@thm-fortune-sweep) and the point-location structure on it in $O(n)$.

2. For each $p_i$, locate its cell: the cell of $q_j$ contains $p_i$ exactly when $q_j$ is a nearest point of $Q$ to $p_i$, so $\min_j\lVert p_i-q_j\rVert=\lVert p_i-q_j\rVert$ is found in $O(\log n)$. This gives the first inner maximum in $O(n\log n)$.

3. Do the same with the roles of $P$ and $Q$ exchanged for the second, and return the larger. Total $O(n\log n)$.
:::

::: {.solution for="prob-mit6854ps-6-q4" status="draft"}
*(a)* This is part 2 of @lem-voronoi-empty-circle: part of the bisector is a Voronoi edge iff some circle centred on it is empty with exactly $p_i,p_j$ on its boundary, and every empty circle through exactly $p_i,p_j$ is centred on their bisector.

*(b)*

1. Let $p_ip_j\in T$. Removing it splits $T$ into two parts; $p_ip_j$ is a shortest edge between them (otherwise exchanging it for a shorter crossing edge gives a cheaper spanning tree).

2. Let $\Delta$ be the closed disc with diameter $p_ip_j$, and suppose some other point $p_k\in\Delta$. The angle $p_ip_kp_j$ is at least $90^\circ$, so $\lVert p_k-p_i\rVert$ and $\lVert p_k-p_j\rVert$ are both less than $\lVert p_i-p_j\rVert$. Whichever part contains $p_k$, one of the edges $p_kp_i$, $p_kp_j$ crosses between the parts and is shorter than $p_ip_j$: a contradiction with step 1.

3. So the circle with diameter $p_ip_j$ is empty and has only $p_i,p_j$ on it; by (a), $p_ip_j\in E$.

*(c)* Compute the Voronoi diagram in $O(n\log n)$ (@thm-fortune-sweep) and read off $D(P)$, which has at most $3n-6$ edges (@thm-voronoi-size). By (b) a minimum spanning tree of $D(P)$ is a Euclidean minimum spanning tree; Kruskal or Prim takes $O(n\log n)$. Total $O(n\log n)$, which is optimal (sorting reduces to it).

*(d)* Let $\Delta_1$ be an empty disc with only $p_i,p_j$ on its boundary circle and $\Delta_2$ one with only $p_k,p_l$ ($\{i,j\}\cap\{k,l\}=\varnothing$). For a disc with centre $c$ and radius $\rho$ let $\pi(x)=\lVert x-c\rVert^2-\rho^2$ (negative inside, $0$ on the circle, positive outside), and put $g=\pi_1-\pi_2$. The quadratic terms cancel, so $g$ is affine.

1. $p_i,p_j$ lie on circle 1 and strictly outside $\Delta_2$: $g(p_i),g(p_j)<0$. Likewise $g(p_k),g(p_l)>0$.

2. As $g$ is affine, $g<0$ on the whole segment $p_ip_j$ and $g>0$ on $p_kp_l$, so the segments are disjoint. If the edges share an endpoint, two segments from a common point meet only there unless collinear and overlapping, which would put a third point on a segment through an empty circle's chord, inside the disc: impossible.
:::
