---
title: "Half-Plane Intersection"
sources: [cs97si-9]
requires: [cs/computational-geometry/vector-geometry]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 9, in our own wording; proofs written out in steps. The example is our own. -->

A half-plane is the set $h=\{(x,y):ax+by+c\le0\}$ with $(a,b)\ne(0,0)$, bounded by the line $\ell:ax+by+c=0$. An intersection of half-planes is convex (each half-plane is), so a bounded non-empty intersection with non-empty interior is a convex polygon. The simple algorithm finds its vertices among the pairwise intersections of the boundary lines.

::: {#def-half-plane-intersection-cubic .definition name="Half-plane intersection by checking all vertices"}

Given half-planes $h_1,\dots,h_n$ with boundary lines $\ell_1,\dots,\ell_n$: for every pair $i<j$ with $\ell_i$ and $\ell_j$ not parallel, compute their intersection point $p$ (@prp-line-intersection) and keep $p$ if $a_kp_x+b_kp_y+c_k\le0$ for all $k$. Sort the kept points by angle around their centroid to get the polygon.

:::

```{=latex}
\begin{algorithm}
\caption{Half-plane intersection, $O(n^3)$}
\begin{algorithmic}
\INPUT Half-planes $a_kx+b_ky+c_k\le0$, $k=1,\dots,n$
\OUTPUT The vertices of their intersection, if it is a bounded polygon
\STATE $V\gets\emptyset$
\FOR{each pair $i<j$ with $a_ib_j-a_jb_i\ne0$}
    \STATE $p\gets\ell_i\cap\ell_j$
    \IF{$a_kp_x+b_kp_y+c_k\le\varepsilon$ for all $k$}
        \STATE $V\gets V\cup\{p\}$
    \ENDIF
\ENDFOR
\STATE remove duplicate points of $V$ and sort them by angle around their centroid
\RETURN $V$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-half-plane-intersection-cubic .theorem name="Correctness and cost"}

If $P=h_1\cap\dots\cap h_n$ is a bounded convex polygon with non-empty interior, the kept points are exactly its vertices, and the algorithm runs in $O(n^3)$ time.

:::

::: {.proof}

1. *Every vertex is found.* A vertex $v$ of $P$ is the meeting point of two edges of $P$ that are not parallel. Each edge lies on some boundary line $\ell_i$, so $v=\ell_i\cap\ell_j$ for a non-parallel pair, and $v\in P$ satisfies all $n$ inequalities.

2. *Every kept point is a vertex.* A kept point $p$ lies in $P$ and on two non-parallel lines $\ell_i,\ell_j$ with $P\subseteq h_i\cap h_j$. The set $h_i\cap h_j$ is a wedge with apex $p$, so no segment inside $P$ has $p$ in its relative interior; hence $p$ is an extreme point of $P$, a vertex.

3. *Order.* The centroid of the vertices is an interior point of the convex polygon, and the vertices of a convex polygon appear around an interior point in angular order.

4. *Cost.* There are $O(n^2)$ pairs, and each check costs $O(n)$; the final sort costs $O(n^2\log n)$ at most.

:::

::: {#exm-half-plane-intersection-1 .example name="Four half-planes"}

Take $x\ge0$, $y\ge0$, $x+y\le4$, $y\le3$, written as $-x\le0$, $-y\le0$, $x+y-4\le0$, $y-3\le0$. Of the six pairs, one ($y=0$ and $y=3$) is parallel. The other five intersections are $(0,0)$, $(0,4)$, $(0,3)$, $(4,0)$ and $(1,3)$; the point $(0,4)$ violates $y\le3$. The polygon is $(0,0),(4,0),(1,3),(0,3)$.

:::

::: {#fig-half-plane-intersection-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.75]
\draw[gridline] (-0.5,-0.5) grid (5,4.8);
\fill[tintA] (0,0) -- (4,0) -- (1,3) -- (0,3) -- cycle;
\draw[faint] (0,-0.5) -- (0,4.8); \draw[faint] (-0.5,0) -- (5,0);
\draw[faint] (-0.5,4.5) -- (4.8,-0.8) node[lab,tick,right] {$x+y=4$};
\draw[faint] (-0.5,3) -- (5,3) node[lab,tick,right] {$y=3$};
\draw[hl] (0,0) -- (4,0) -- (1,3) -- (0,3) -- cycle;
\foreach \p in {(0,0),(4,0),(1,3),(0,3)} \node[hl dot] at \p {};
\node[hollow dot] at (0,4) {}; \node[lab,tick,right] at (0,4.15) {$(0,4)$ rejected};
\end{tikzpicture}
\end{center}
```

@exm-half-plane-intersection-1: of the five line intersections, four satisfy every inequality and form the polygon; $(0,4)$ lies outside $y\le3$.

:::

::: {#rmk-half-plane-intersection-1 .remark name="Faster and degenerate cases"}

An $O(n\log n)$ algorithm sorts the half-planes by the angle of their boundary and keeps a deque of useful ones, much like the Graham scan (@def-graham-scan). For the simple algorithm, an unbounded or empty intersection shows up as too few kept points; adding a large bounding box of four half-planes makes the result bounded, and tests need a tolerance $\varepsilon$ when the coordinates are not integers.

:::
