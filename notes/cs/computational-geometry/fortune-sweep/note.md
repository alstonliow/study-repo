---
title: "Fortune's Sweep-Line Algorithm for Voronoi Diagrams"
sources: [mit6854-23]
requires: [cs/computational-geometry/voronoi-diagrams, cs/computational-geometry/sweep-line]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 23 (Section 2.3), in our own wording; the example is our own (checked by computation); proofs written out in steps. -->

A sweep line (@sec-cs-computational-geometry-sweep-line) cannot simply report the Voronoi diagram above it: a cell above the line may still be cut by a site below it. Fortune's idea (1986) is to finalise only the part of the plane that is closer to some site above the line than to the line itself. That part is bounded by a curve of parabolic arcs, the *beach line*, which changes only at two kinds of discrete events.

Sweep a horizontal line $\ell$ downwards, at height $y=t$ decreasing.

::: {#def-beach-line .definition name="Beach line, breakpoint"}

For a site $p$ above $\ell$, the points equidistant from $p$ and $\ell$ form a parabola $C_p$ opening upwards. The *beach line* is the lower envelope of the parabolas $C_p$ of the sites above $\ell$: a sequence of parabolic arcs, each belonging to one site (a site may own several arcs). A *breakpoint* is a point where two consecutive arcs meet.

:::

::: {#prp-beach-line .proposition name="What the beach line tells"}

1. Every point strictly above the beach line is closer to some site above $\ell$ than to $\ell$, so its nearest site is already known: the Voronoi diagram above the beach line is final.
2. A breakpoint between arcs of $p_i$ and $p_j$ is equidistant from $p_i$, $p_j$ and $\ell$, with no site closer, so it lies on the Voronoi edge of $p_i,p_j$. As $\ell$ moves, the breakpoints trace out the Voronoi edges.

:::

::: {.proof}

1. If $x$ lies above the beach line, it is closer to some site $p$ above $\ell$ than to $\ell$; every site below $\ell$ is farther from $x$ than $\ell$ is. So the nearest site of $x$ is a site above $\ell$, and these are all known.

2. A breakpoint $q$ is at distance $r=\operatorname{dist}(q,\ell)$ from both $p_i$ and $p_j$ and no site above $\ell$ is closer (they define the lower envelope), nor any site below $\ell$ (they are farther than $\ell$). The empty circle of radius $r$ about $q$ has exactly $p_i,p_j$ on its boundary, so by @lem-voronoi-empty-circle $q$ is on their Voronoi edge.

:::

::: {#def-fortune-events .definition name="Site and circle events"}

The sequence of arcs changes only at two kinds of events:

1. *Site event:* $\ell$ reaches a new site $p_l$. A degenerate arc of $p_l$ appears, splitting the arc of the site $p_j$ directly above it: $\dots p_ip_jp_k\dots\to\dots p_ip_jp_lp_jp_k\dots$. Two new breakpoints start tracing the bisector of $p_j,p_l$.
2. *Circle event:* an arc of $p_j$ between arcs of $p_i$ and $p_k$ shrinks to a point: $\dots p_ip_jp_k\dots\to\dots p_ip_k\dots$. This happens when $\ell$ touches from below the circle through $p_i,p_j,p_k$, and its centre is then a Voronoi vertex.

:::

Each site event creates one arc and splits one into two, so the beach line has at most $2n-1$ arcs. A circle event is detected for every three consecutive arcs whose breakpoints converge; when arcs change, at most two such triples disappear (their pending events are *false alarms* and are deleted) and at most two appear.

::: {#def-fortune-sweep .definition name="Fortune's algorithm"}

Keep

1. an *event queue*: a priority queue of events keyed by height, initially the $n$ sites; a circle event's key is the lowest point of its circle;
2. the *beach line*: a balanced search tree of the arcs in left-to-right order, with the breakpoints as internal keys (a breakpoint's position is computed from its two sites and the current $t$);
3. the *diagram*: a doubly connected edge list (half-edges with twin, next and previous pointers).

Repeatedly remove the highest event. For a site event, locate the arc above the site in the tree, split it, start a new edge, delete the false alarm of the split arc and insert the new circle events. For a circle event, delete the vanishing arc, record the vertex, finish the two edges, start the new one, and update the circle events of the neighbours. Finally, unbounded edges are clipped to a box.

:::

```{=latex}
\begin{algorithm}
\caption{Fortune's sweep}
\begin{algorithmic}
\INPUT sites $p_1,\dots,p_n$ in the plane
\OUTPUT the Voronoi diagram as a doubly connected edge list
\STATE $Q\gets$ priority queue of all site events; $T\gets$ empty beach line
\WHILE{$Q$ is not empty}
\STATE $e\gets$ highest event of $Q$
\IF{$e$ is a site event at $p$}
\STATE find the arc of $T$ above $p$; split it around a new arc of $p$
\STATE delete its pending circle event; add circle events of the new triples
\ELSE
\STATE remove the vanishing arc from $T$; record the circle centre as a vertex
\STATE update the pending circle events of the neighbouring triples
\ENDIF
\ENDWHILE
\RETURN the edge list, with unbounded edges clipped
\end{algorithmic}
\end{algorithm}
```

::: {#thm-fortune-sweep .theorem name="Fortune's algorithm runs in $O(n\log n)$"}

The algorithm computes the Voronoi diagram of $n$ sites in $O(n\log n)$ time and $O(n)$ space.

:::

::: {.proof}

1. There are $n$ site events and at most $2n-5$ real circle events, one per Voronoi vertex (@thm-voronoi-size).

2. Each event inserts and deletes $O(1)$ circle events (false alarms included), so the queue sees $O(n)$ operations of $O(\log n)$ each.

3. Each event makes $O(1)$ operations on the beach-line tree, which has $O(n)$ arcs, at $O(\log n)$ each; the diagram is updated in $O(1)$ per event.

4. Correctness follows from @prp-beach-line once one knows that arcs appear only at site events and disappear only at circle events, which we accept without proof.

:::

::: {#exm-fortune-sweep .example name="Three sites"}

Sites $a=(0,4)$, $b=(4,3)$, $c=(1,0)$. At $t=4$ the beach line is one degenerate arc of $a$. At $t=3$ the site event of $b$ splits it: arcs $a\,b\,a$. The triple $a\,b\,a$ has a repeated site, so no circle event. At $t=0$ the site event of $c$ falls below the left arc of $a$ (the breakpoints of $a$ and $b$ are then at $x\approx1.72$ and $x\approx30.3$): arcs $a\,c\,a\,b\,a$, and the triple $c\,a\,b$ gets a circle event. The circle through $a,b,c$ has centre $(1.7,2.3)$ and radius $\sqrt{5.78}\approx2.40$, so the event fires at $t\approx2.3-2.40=-0.10$, when the middle arc of $a$ vanishes and the single Voronoi vertex is created.

:::

::: {#fig-fortune-sweep-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.7]
\draw[hl] (-2.500,3.542) -- (-2.450,3.500) -- (-2.400,3.460) -- (-2.350,3.420) -- (-2.300,3.382) -- (-2.250,3.344) -- (-2.200,3.307) -- (-2.150,3.270) -- (-2.100,3.235) -- (-2.050,3.200) -- (-2.000,3.167) -- (-1.950,3.134) -- (-1.900,3.102) -- (-1.850,3.070) -- (-1.800,3.040) -- (-1.750,3.010) -- (-1.700,2.982) -- (-1.650,2.954) -- (-1.600,2.927) -- (-1.550,2.900) -- (-1.500,2.875) -- (-1.450,2.850) -- (-1.400,2.827) -- (-1.350,2.804) -- (-1.300,2.782) -- (-1.250,2.760) -- (-1.200,2.740) -- (-1.150,2.720) -- (-1.100,2.702) -- (-1.050,2.684) -- (-1.000,2.667) -- (-0.950,2.650) -- (-0.900,2.635) -- (-0.850,2.620) -- (-0.800,2.607) -- (-0.750,2.594) -- (-0.700,2.582) -- (-0.650,2.570) -- (-0.600,2.560) -- (-0.550,2.550) -- (-0.500,2.542) -- (-0.450,2.534) -- (-0.400,2.527) -- (-0.350,2.520) -- (-0.300,2.515) -- (-0.250,2.510) -- (-0.200,2.507) -- (-0.150,2.504) -- (-0.100,2.502) -- (-0.050,2.500) -- (0.000,2.500) -- (0.050,2.500) -- (0.100,2.502) -- (0.150,2.504) -- (0.200,2.507) -- (0.250,2.510) -- (0.300,2.515) -- (0.350,2.520) -- (0.400,2.527) -- (0.450,2.534) -- (0.500,2.542) -- (0.550,2.550) -- (0.600,2.560) -- (0.650,2.570) -- (0.700,2.582) -- (0.750,2.594) -- (0.800,2.607) -- (0.850,2.620) -- (0.900,2.635) -- (0.950,2.650) -- (1.000,2.667) -- (1.050,2.684) -- (1.100,2.702) -- (1.150,2.720) -- (1.200,2.740) -- (1.250,2.760) -- (1.300,2.782) -- (1.350,2.804) -- (1.400,2.827) -- (1.450,2.850) -- (1.500,2.875) -- (1.550,2.900) -- (1.600,2.927) -- (1.650,2.954) -- (1.700,2.982) -- (1.750,3.010) -- (1.800,3.040) -- (1.850,3.070) -- (1.900,3.102) -- (1.950,3.051) -- (2.000,3.000) -- (2.050,2.951) -- (2.100,2.902) -- (2.150,2.856) -- (2.200,2.810) -- (2.250,2.766) -- (2.300,2.722) -- (2.350,2.681) -- (2.400,2.640) -- (2.450,2.601) -- (2.500,2.562) -- (2.550,2.526) -- (2.600,2.490) -- (2.650,2.456) -- (2.700,2.422) -- (2.750,2.391) -- (2.800,2.360) -- (2.850,2.331) -- (2.900,2.302) -- (2.950,2.276) -- (3.000,2.250) -- (3.050,2.226) -- (3.100,2.202) -- (3.150,2.181) -- (3.200,2.160) -- (3.250,2.141) -- (3.300,2.122) -- (3.350,2.106) -- (3.400,2.090) -- (3.450,2.076) -- (3.500,2.062) -- (3.550,2.051) -- (3.600,2.040) -- (3.650,2.031) -- (3.700,2.022) -- (3.750,2.016) -- (3.800,2.010) -- (3.850,2.006) -- (3.900,2.002) -- (3.950,2.001) -- (4.000,2.000) -- (4.050,2.001) -- (4.100,2.002) -- (4.150,2.006) -- (4.200,2.010) -- (4.250,2.016) -- (4.300,2.022) -- (4.350,2.031) -- (4.400,2.040) -- (4.450,2.051) -- (4.500,2.062) -- (4.550,2.076) -- (4.600,2.090) -- (4.650,2.106) -- (4.700,2.123) -- (4.750,2.141) -- (4.800,2.160) -- (4.850,2.181) -- (4.900,2.203) -- (4.950,2.226) -- (5.000,2.250) -- (5.050,2.276) -- (5.100,2.303) -- (5.150,2.331) -- (5.200,2.360) -- (5.250,2.391) -- (5.300,2.423) -- (5.350,2.456) -- (5.400,2.490) -- (5.450,2.526) -- (5.500,2.562) -- (5.550,2.601) -- (5.600,2.640) -- (5.650,2.681) -- (5.700,2.723) -- (5.750,2.766) -- (5.800,2.810) -- (5.850,2.856) -- (5.900,2.903) -- (5.950,2.951) -- (6.000,3.000) -- (6.050,3.051) -- (6.100,3.102) -- (6.150,3.156) -- (6.200,3.210) -- (6.250,3.266) -- (6.300,3.323) -- (6.350,3.381) -- (6.400,3.440) -- (6.450,3.501) -- (6.500,3.562);
\draw[faint, dashed] (-2.5,1)--(6.5,1) node[lab, right] {$\ell$};
\node[dot] at (0,4) {};
\node[lab, above] at (0,4) {$a$};
\node[dot] at (4,3) {};
\node[lab, above] at (4,3) {$b$};
\node[dot] at (1,0) {};
\node[lab, above] at (1,0) {$c$};
\node[hollow dot] at (1.900,3.102) {};
\end{tikzpicture}
\end{center}
```

The beach line (highlighted) for the sites $a,b$ when the sweep line $\ell$ is at $y=1$: the lower envelope of their parabolas, arcs $a\,b\,a$ (the second breakpoint lies far to the right). The breakpoints lie on the bisector of $a$ and $b$; the site $c$ is still below $\ell$.

:::
