---
title: "Convex Hull by Graham Scan"
sources: [cs97si-9]
requires: [cs/computational-geometry/vector-geometry, cs/data-structures/stacks-and-queues]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 9, in our own wording; proofs written out in steps. The example is our own. -->

The convex hull (@def-convex-hull) of $n$ points can be found by divide and conquer (@sec-cs-computational-geometry-convex-hull). The Graham scan is the version usually written in contests: one sort and one pass with a stack.

::: {#prp-hull-edge-test .proposition name="Hull edges by orientation"}

Assume no three of the points are collinear. The directed segment $AB$ between two of the points is an edge of the hull traversed counter-clockwise if and only if $\operatorname{ccw}(A,B,C)>0$ for every other point $C$.

:::

::: {.proof}

1. If all other points lie strictly to the left of the line $AB$, the closed half-plane to the left of $AB$ is convex and contains every point, so it contains the hull, and $AB$ lies on the hull's boundary.

2. Conversely, if $AB$ is a counter-clockwise hull edge, the hull lies to its left; no other point is on the line $AB$, so every other point is strictly to the left.

:::

Testing all pairs this way costs $O(n^3)$. The Graham scan does better.

::: {#def-graham-scan .definition name="Graham scan"}

Let $o$ be the point with the smallest $x$ (the smallest $y$ among ties). Sort the other points by the angle of $p-o$, increasing from $-\pi/2$ to $\pi/2$; for points with $p_x>o_x$ this is the order of the slope $(p_y-o_y)/(p_x-o_x)$, and it is decided by $\operatorname{ccw}(o,p,q)>0$ without division. Then scan the points in this order with a stack that starts as $(o)$: before pushing a point $p$, pop the top while the last two stack entries $s,t$ and $p$ do not make a left turn, $\operatorname{ccw}(s,t,p)\le0$.

:::

```{=latex}
\begin{algorithm}
\caption{Graham scan}
\begin{algorithmic}
\INPUT Points $P$, $|P|=n\ge3$, no three collinear
\OUTPUT The hull vertices in counter-clockwise order
\STATE $o\gets$ the leftmost point (lowest among ties)
\STATE sort $P\setminus\{o\}$ by angle around $o$ into $q_1,\dots,q_{n-1}$
\STATE $S\gets(o)$
\FOR{$i=1$ \TO $n-1$}
    \WHILE{$|S|\ge2$ \AND $\operatorname{ccw}(S_{-2},S_{-1},q_i)\le0$}
        \STATE pop $S$ \COMMENT{$S_{-1}$ would make a right turn}
    \ENDWHILE
    \STATE push $q_i$ onto $S$
\ENDFOR
\RETURN $S$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-graham-scan .theorem name="Graham scan"}

The Graham scan returns the vertices of the convex hull in counter-clockwise order in $O(n\log n)$ time.

:::

::: {.proof}

1. *Invariant.* After $q_i$ is pushed, the stack holds, in order, the hull vertices of $\{o,q_1,\dots,q_i\}$, ending with $q_i$. For $i=1$ the stack is $(o,q_1)$, which is right.

2. *The new point is on the hull.* The points $q_1,\dots,q_i$ lie in the angular sector at $o$ that ends with the ray through $q_i$, so $q_i$ is extreme in its direction from $o$, and $o$ and $q_i$ are hull vertices of the first $i+1$ points.

3. *Pops remove exactly the dead vertices.* A stack entry $t$ with predecessor $s$ for which $\operatorname{ccw}(s,t,q_i)\le0$ lies inside the triangle $o\,s\,q_i$ (or on its boundary), so it is not a hull vertex any more. Once $\operatorname{ccw}(s,t,q_i)>0$, the chain $o,\dots,s,t,q_i$ turns left at every vertex; together with the closing edge $q_i\to o$ (all points lie to its left, since $q_i$ has the largest angle) it is a convex polygon containing all the points, so all its vertices stay.

4. By induction the final stack is the hull of all points, counter-clockwise from $o$.

5. *Time.* Sorting costs $O(n\log n)$. Every point is pushed once and popped at most once, so the scan costs $O(n)$ in total.

:::

::: {#exm-graham-scan-1 .example name="Nine points"}

For the points $(0,2),(2,0),(3,3),(5,1),(4,4),(1,4),(2,2),(6,3),(3,6)$, $o=(0,2)$ and the angular order is

$$
(2,0),\ (5,1),\ (2,2),\ (6,3),\ (3,3),\ (4,4),\ (3,6),\ (1,4).
$$

The scan pops $(2,2)$ when $(6,3)$ arrives, $(3,3)$ when $(4,4)$ arrives and $(4,4)$ when $(3,6)$ arrives. The hull is $(0,2),(2,0),(5,1),(6,3),(3,6),(1,4)$.

:::

::: {#fig-graham-scan-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.62]
\draw[gridline] (-0.5,-0.5) grid (6.5,6.5);
\foreach \p in {(2,0),(5,1),(2,2),(6,3),(3,3),(4,4),(3,6),(1,4)} \draw[faint] (0,2) -- \p;
\fill[tintA] (0,2) -- (2,0) -- (5,1) -- (6,3) -- (3,6) -- (1,4) -- cycle;
\draw[hl] (0,2) -- (2,0) -- (5,1) -- (6,3) -- (3,6) -- (1,4) -- cycle;
\foreach \p/\n/\a in {(2,0)/1/below,(5,1)/2/below right,(2,2)/3/below,(6,3)/4/right,(3,3)/5/below right,(4,4)/6/right,(3,6)/7/above,(1,4)/8/above left}
  \node[dot,label={[lab,tick]\a:$q_{\n}$}] at \p {};
\node[hl dot,label={[lab]left:$o$}] at (0,2) {};
\end{tikzpicture}
\end{center}
```

@exm-graham-scan-1: the points are numbered in angular order around $o$. The interior points $q_3$, $q_5$ and $q_6$ are pushed and later popped; the highlighted polygon is the hull.

:::

::: {#rmk-graham-scan-1 .remark name="Collinear points and the monotone chain"}

With collinear points, break angle ties by distance from $o$ and decide whether points on hull edges are kept (pop on $\le0$ or only on $<0$). A common variant, Andrew's monotone chain, sorts by $(x,y)$ instead of by angle and builds the lower and upper hulls with the same stack rule; it avoids angle comparisons altogether.

:::
