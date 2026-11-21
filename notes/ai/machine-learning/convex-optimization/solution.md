<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-21-q1" status="draft"}
1. Discs: the union is convex exactly when one disc contains the other (then the union is that disc).

2. If the boundary circles cross at a point $P$, take points $\mathbf{x}$ on circle 1 and $\mathbf{y}$ on circle 2, both at small distance $\varepsilon$ from $P$ and each outside the other disc. Their midpoint is $P+\frac\varepsilon2(\mathbf{t}_1+\mathbf{t}_2)+O(\varepsilon^2)$, where $\mathbf{t}_k$ is the unit tangent of circle $k$ at $P$ pointing that way. Since $\mathbf{t}_2$ leaves disc 1 transversally, the outward normal $\mathbf{n}_1$ of disc 1 has $\mathbf{n}_1^{\mathsf T}\mathbf{t}_2>0$ (and $\mathbf{n}_1^{\mathsf T}\mathbf{t}_1=0$), so the midpoint is outside disc 1 for small $\varepsilon$; likewise outside disc 2. Not convex.

3. If the discs are disjoint, part of the segment joining the centres lies in neither. If they touch at one point $T$ from outside, points of the two circles at the same small height $\varepsilon$ above $T$ (measured along the common tangent line) have a midpoint in neither disc, because each disc's boundary curves away from the tangent on its own side.

4. Squares: the union is convex when one square contains the other, or when two squares of the same size are placed side by side (overlapping or sharing an edge) with two edges on common lines, so that the union is a rectangle. In every other position the union has a reflex corner where the boundaries meet, and a short segment across that corner leaves the union.
:::

::: {.solution for="prob-mit18065ps-21-q5" status="draft"}
Take $K\ne\emptyset$ and $K\ne\mathbb{R}^n$ (otherwise $F$ is constant, hence convex).

1. $F=1$ on $K$: not convex. Pick $\mathbf{x}\in K$ and $\mathbf{y}\notin K$. If some point $\mathbf{z}=(1-t)\mathbf{x}+t\mathbf{y}$ with $0<t<1$ lies in $K$, then $F(\mathbf{z})=1>1-t=(1-t)F(\mathbf{x})+tF(\mathbf{y})$. Otherwise the segment meets $K$ only at $\mathbf{x}$. Then look at $\mathbf{x}'=2\mathbf{x}-\mathbf{y}$, so that $\mathbf{x}$ is the midpoint of $\mathbf{x}'$ and $\mathbf{y}$: if $\mathbf{x}'\notin K$, then $F(\mathbf{x})=1>0=\frac12F(\mathbf{x}')+\frac12F(\mathbf{y})$; if $\mathbf{x}'\in K$, the first case applies to $\mathbf{x}'$ and $\mathbf{y}$ (the point $\mathbf{x}$ of that segment is in $K$).

2. Reversed ($F=0$ on $K$, $1$ outside): not convex either. Take $\mathbf{x}\in K$, $\mathbf{y}\notin K$, and a point $\mathbf{z}=(1-t)\mathbf{x}+t\mathbf{y}\notin K$ with $t<1$ (points of the segment near $\mathbf{y}$ are outside $K$ when $K$ is closed). Then $F(\mathbf{z})=1>t=(1-t)F(\mathbf{x})+tF(\mathbf{y})$.

3. What is convex is the indicator with values $0$ on $K$ and $+\infty$ outside, which is how constraints are written as convex functions.
:::

::: {.solution for="prob-mit18065ps-22-q1" status="draft"}
$F'(x)=-1/x$ and $F''(x)=1/x^2>0$ for $x>0$, so $F$ is convex by @prp-convex-second-derivative. The graph falls from $+\infty$ near $x=0^+$, crosses zero at $x=1$, and keeps decreasing slowly to $-\infty$, always bending upward (lying above its tangent lines).
:::

::: {.solution for="prob-mit18065ps-23-q5" status="draft"}
1. Let $\mathbf{p},\mathbf{q}$ be the projections of $\mathbf{x},\mathbf{y}$. Closest-point property: the angle at $\mathbf{p}$ between $\mathbf{x}-\mathbf{p}$ and any $\mathbf{z}-\mathbf{p}$ with $\mathbf{z}\in K$ is at least $90^\circ$, i.e. $(\mathbf{z}-\mathbf{p})^{\mathsf T}(\mathbf{x}-\mathbf{p})\le0$; otherwise moving from $\mathbf{p}$ toward $\mathbf{z}$ (allowed, since $K$ is convex) would get closer to $\mathbf{x}$.

2. Use $\mathbf{z}=\mathbf{q}$ at $\mathbf{p}$ and $\mathbf{z}=\mathbf{p}$ at $\mathbf{q}$, and add: $\lVert\mathbf{p}-\mathbf{q}\rVert^2\le(\mathbf{p}-\mathbf{q})^{\mathsf T}(\mathbf{x}-\mathbf{y})\le\lVert\mathbf{p}-\mathbf{q}\rVert\lVert\mathbf{x}-\mathbf{y}\rVert$.

3. Divide by $\lVert\mathbf{p}-\mathbf{q}\rVert$ (if nonzero): $\lVert\mathbf{p}-\mathbf{q}\rVert\le\lVert\mathbf{x}-\mathbf{y}\rVert$. Geometrically, $\mathbf{x}$ and $\mathbf{y}$ lie beyond the two parallel planes through $\mathbf{p}$ and $\mathbf{q}$ perpendicular to $\mathbf{p}-\mathbf{q}$. This is @thm-projection-convex-nonexpansive.
:::
