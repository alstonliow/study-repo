---
title: "Vectors, Orientation and Areas"
sources: [cs97si-2, cs97si-9]
requires: []
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 2 (geometry part) and Lecture 9 (cross product), in our own wording; proofs written out in steps. The examples and figures are our own. -->

Contest geometry works with points of $\mathbb{R}^2$ as vectors and reduces almost every test to the sign of one number, the two-dimensional cross product. With integer coordinates that number is an exact integer, so the tests have no rounding error.

::: {#def-cross-product-2d .definition name="Dot and cross product in the plane"}

For $u=(u_x,u_y)$ and $v=(v_x,v_y)$ in $\mathbb{R}^2$,

$$
u\cdot v=u_xv_x+u_yv_y,\qquad u\times v=u_xv_y-u_yv_x .
$$

For points $a,b,c$, the *orientation* is $\operatorname{ccw}(a,b,c)=(b-a)\times(c-a)$.

:::

::: {#prp-cross-product-2d .proposition name="Meaning of the cross product"}

If $\theta$ is the angle that turns $u$ to $v$ counter-clockwise, then

$$
u\times v=|u|\,|v|\sin\theta .
$$

So $\operatorname{ccw}(a,b,c)>0$ when $a\to b\to c$ turns left, $<0$ when it turns right, and $=0$ exactly when $a,b,c$ are collinear. The triangle $abc$ has area $\tfrac12\lvert\operatorname{ccw}(a,b,c)\rvert$.

:::

::: {.proof}

1. Write $u=|u|(\cos\alpha,\sin\alpha)$ and $v=|v|(\cos\beta,\sin\beta)$, so $\theta=\beta-\alpha$.

2. Then $u\times v=|u||v|(\cos\alpha\sin\beta-\sin\alpha\cos\beta)=|u||v|\sin(\beta-\alpha)$.

3. With $u=b-a$ and $v=c-a$, the sign of $\sin\theta$ tells whether $c$ lies to the left ($0<\theta<\pi$) or to the right of the directed line $ab$, and $\sin\theta=0$ means $c$ is on that line.

4. The triangle has base $|u|$ and height $|v|\,\lvert\sin\theta\rvert$, so its area is $\tfrac12|u||v|\lvert\sin\theta\rvert=\tfrac12\lvert u\times v\rvert$.

:::

::: {#exm-vector-geometry-triangle .example name="A left turn"}

For $a=(0,0)$, $b=(4,1)$, $c=(1,3)$: $\operatorname{ccw}(a,b,c)=4\cdot3-1\cdot1=11>0$, so $a\to b\to c$ turns left and the triangle has area $11/2$.

:::

::: {#fig-vector-geometry-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\draw[gridline] (-0.5,-0.5) grid (4.5,3.5);
\fill[tintA] (0,0) -- (4,1) -- (1,3) -- cycle;
\draw[emph,->] (0,0) -- (4,1) node[lab,right] {$b$};
\draw[emph,->] (0,0) -- (1,3) node[lab,above] {$c$};
\draw[faint] (4,1) -- (1,3);
\node[lab,below left] at (0,0) {$a$};
\draw[->,hl] (1.2,0.3) arc[start angle=14, end angle=71, radius=1.24];
\node[lab,note] at (2.2,1.5) {area $\tfrac{11}{2}$};
\end{tikzpicture}
\end{center}
```

$\operatorname{ccw}(a,b,c)=11>0$: turning $b-a$ towards $c-a$ is counter-clockwise, and the shaded triangle has half that area.

:::

## Polygons and circles

::: {#thm-shoelace .theorem name="Area of a simple polygon"}

If $p_0,p_1,\dots,p_{n-1}$ are the vertices of a simple polygon in counter-clockwise order and $p_n=p_0$, its area is

$$
A=\frac12\sum_{i=0}^{n-1}p_i\times p_{i+1}.
$$

In clockwise order the sum is $-2A$.

:::

::: {.proof}

1. Fix the origin $o$. The term $\tfrac12\,p_i\times p_{i+1}$ is the signed area of the triangle $o\,p_i\,p_{i+1}$ (@prp-cross-product-2d): positive when the edge $p_ip_{i+1}$ goes counter-clockwise around $o$, negative otherwise.

2. Take a point $x$ not on any edge and not on any ray from $o$ through a vertex. The ray from $o$ through $x$ crosses the boundary at finitely many points beyond $o$; between $o$ and $x$ the crossings alternate between edges going counter-clockwise and clockwise around $o$, ending with a counter-clockwise one exactly when $x$ is inside (the boundary is traversed counter-clockwise).

3. So $x$ lies in the signed triangles with total weight $1$ if $x$ is inside the polygon and $0$ if outside. Integrating over the plane, the sum of the signed areas equals the area of the polygon.

4. Reversing the order negates every term.

:::

::: {#exm-vector-geometry-shoelace .example name="A pentagon"}

For $(0,0),(4,0),(4,3),(2,5),(0,3)$ the terms $p_i\times p_{i+1}$ are $0,12,14,6,0$, so the area is $32/2=16$: a $4\times3$ rectangle plus a triangle of base $4$ and height $2$.

:::

::: {#fig-vector-geometry-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.6]
\draw[gridline] (-0.5,-0.5) grid (4.5,5.5);
\fill[tintB] (0,0) -- (4,0) -- (4,3) -- cycle; \fill[tintB] (0,0) -- (4,3) -- (2,5) -- cycle; \fill[tintB] (0,0) -- (2,5) -- (0,3) -- cycle;
\draw[emph] (0,0) -- (4,0) -- (4,3) -- (2,5) -- (0,3) -- cycle;
\draw[faint] (0,0) -- (4,3); \draw[faint] (0,0) -- (2,5);
\foreach \x/\y in {0/0,4/0,4/3,2/5,0/3} \node[dot] at (\x,\y) {};
\node[lab,below left] at (0,0) {$p_0$}; \node[lab,below right] at (4,0) {$p_1$};
\node[lab,right] at (4,3) {$p_2$}; \node[lab,above] at (2,5) {$p_3$}; \node[lab,left] at (0,3) {$p_4$};
\node[lab,note,anchor=west] at (5,2.5) {$\tfrac12(0+12+14+6+0)=16$};
\end{tikzpicture}
\end{center}
```

The shoelace sum with the origin at $p_0$: the polygon splits into the triangles $p_0p_1p_2$, $p_0p_2p_3$ and $p_0p_3p_4$ of areas $6$, $7$ and $3$.

:::

::: {#prp-line-intersection .proposition name="Intersection of two lines"}

The lines $p+t\,r$ and $q+s\,w$ ($t,s\in\mathbb{R}$) meet in exactly one point if and only if $r\times w\ne0$, and then the point is $p+t\,r$ with

$$
t=\frac{(q-p)\times w}{r\times w}.
$$

:::

::: {.proof}

1. A common point satisfies $p+t\,r=q+s\,w$, that is $t\,r-s\,w=q-p$.

2. Take the cross product of both sides with $w$. Since $w\times w=0$, this gives $t\,(r\times w)=(q-p)\times w$.

3. If $r\times w\ne0$ this fixes $t$, and crossing with $r$ fixes $s$ the same way, so the point is unique. If $r\times w=0$ the directions are parallel and the lines are either disjoint or equal.

:::

::: {#exm-vector-geometry-lines .example name="Two lines"}

The line through $(0,0)$ with direction $(4,2)$ and the line through $(1,3)$ with direction $(2,-2)$: $r\times w=-8-4=-12$ and $(q-p)\times w=-2-6=-8$, so $t=2/3$ and the lines meet at $(8/3,4/3)$.

:::

::: {#prp-circumcircle .proposition name="Circumcircle of a triangle"}

The circle through three non-collinear points $a,b,c$ has its centre where the perpendicular bisectors of $ab$ and $ac$ meet: the line through $\tfrac12(a+b)$ with direction $(b-a)$ turned by $90^\circ$, and likewise for $ac$. Its radius is the distance from the centre to $a$.

:::

::: {.proof}

1. A point is equidistant from $a$ and $b$ if and only if it lies on the perpendicular bisector of $ab$; the same holds for $a$ and $c$.

2. Turning $u=(u_x,u_y)$ by $90^\circ$ gives $(-u_y,u_x)$. The two bisector directions are $b-a$ and $c-a$ turned by $90^\circ$, and their cross product equals $(b-a)\times(c-a)=\operatorname{ccw}(a,b,c)\ne0$, so the bisectors meet in one point by @prp-line-intersection.

3. That point is equidistant from $a$, $b$ and $c$, so it is the centre, and the radius is its distance to any of them.

:::

For $a=(0,0)$, $b=(4,0)$, $c=(0,3)$ the centre is $(2,3/2)$, the midpoint of the hypotenuse, and the radius is $5/2$.

::: {#rmk-vector-geometry-1 .remark name="Exact arithmetic"}

Keep coordinates integral as long as possible: orientation tests and doubled areas are then exact. Divide only at the end (a line intersection is a quotient), and compare floating-point results with a tolerance $\varepsilon$ rather than with $=$.

:::
