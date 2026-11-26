---
title: "Segment Intersection"
sources: [cs97si-9]
requires: [cs/computational-geometry/vector-geometry]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 9, in our own wording; proofs written out in steps. The special cases and examples are our own. -->

Whether two segments cross is decided by four orientation tests (@def-cross-product-2d), with no division at all.

::: {#def-segment-intersection .definition name="Proper intersection, segment intersection test"}

Segments $AB$ and $CD$ *intersect properly* if they meet in a single point that is interior to both. The *segment intersection test*: let

$$
d_1=\operatorname{ccw}(A,B,C),\quad d_2=\operatorname{ccw}(A,B,D),\quad d_3=\operatorname{ccw}(C,D,A),\quad d_4=\operatorname{ccw}(C,D,B).
$$

Report a proper intersection when $d_1d_2<0$ and $d_3d_4<0$. Otherwise, if some $d_i=0$, check whether the corresponding point lies on the other segment (for $d_1=0$: whether $C$ lies on $AB$); report an intersection if one does.

:::

```{=latex}
\begin{algorithm}
\caption{Segment intersection test}
\begin{algorithmic}
\INPUT Points $A,B,C,D$ with integer coordinates
\OUTPUT Whether the closed segments $AB$ and $CD$ share a point
\STATE $d_1\gets\operatorname{ccw}(A,B,C)$; $d_2\gets\operatorname{ccw}(A,B,D)$; $d_3\gets\operatorname{ccw}(C,D,A)$; $d_4\gets\operatorname{ccw}(C,D,B)$
\IF{$d_1d_2<0$ \AND $d_3d_4<0$}
    \RETURN true \COMMENT{proper crossing}
\ENDIF
\IF{($d_1=0$ \AND $C\in AB$) \OR ($d_2=0$ \AND $D\in AB$) \OR ($d_3=0$ \AND $A\in CD$) \OR ($d_4=0$ \AND $B\in CD$)}
    \RETURN true \COMMENT{touching or overlapping}
\ENDIF
\RETURN false
\end{algorithmic}
\end{algorithm}
```

Here a point $P$ collinear with $AB$ lies on $AB$ exactly when $\min(A_x,B_x)\le P_x\le\max(A_x,B_x)$ and the same holds for $y$.

::: {#thm-segment-intersection .theorem name="Correctness of the test"}

The segment intersection test reports an intersection if and only if the closed segments $AB$ and $CD$ have a common point, and it reports a proper intersection exactly in the case $d_1d_2<0$, $d_3d_4<0$. It uses $O(1)$ integer operations.

:::

::: {.proof}

1. *Proper case.* $d_1d_2<0$ means $C$ and $D$ lie strictly on opposite sides of the line $AB$, so the segment $CD$ crosses that line in a single point $X$ interior to $CD$. Likewise $d_3d_4<0$ means $AB$ crosses the line $CD$ in a single point $Y$ interior to $AB$. Both $X$ and $Y$ are the unique common point of the two lines (they are not parallel, since $C,D$ are on opposite sides of $AB$), so $X=Y$ is interior to both segments.

2. *Conversely*, if the segments meet in one point interior to both and no endpoint is collinear with the other segment, the endpoints of each segment lie strictly on opposite sides of the other line, so $d_1d_2<0$ and $d_3d_4<0$.

3. *No zero, not both products negative.* If all $d_i\ne0$ and, say, $d_1d_2>0$, then $C$ and $D$ lie strictly on the same side of the line $AB$, so $CD$ does not even meet that line, and the segments are disjoint. The case $d_3d_4>0$ is symmetric.

4. *Some $d_i=0$.* If the segments share a point and are not in the proper case, that point is an endpoint of one segment lying on the other (or the segments overlap along a line, when again some endpoint lies on the other segment). That endpoint is collinear with the other segment, so its $d_i$ is $0$ and the bounding-box check finds it. Conversely, a check that succeeds exhibits a common point.

5. Each $d_i$ is two products and a subtraction, and the box checks are comparisons.

:::

::: {#exm-segment-intersection-1 .example name="Three cases"}

1. $A=(0,0)$, $B=(4,2)$, $C=(1,3)$, $D=(3,-1)$: $d_1=10$, $d_2=-10$, $d_3=-10$, $d_4=10$, a proper crossing (at $(2,1)$).
2. $A=(0,0)$, $B=(2,2)$, $C=(3,3)$, $D=(5,5)$: all four $d_i$ are $0$; no endpoint lies in the other segment's box, so the collinear segments are disjoint.
3. $A=(0,0)$, $B=(4,0)$, $C=(2,0)$, $D=(2,3)$: $d_1=0$ and $C$ lies on $AB$, so the segments touch at $C$ without crossing properly.

:::

::: {#fig-segment-intersection-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.62]
\begin{scope}
\draw[emph] (0,0) node[dot]{} node[lab,below left]{$A$} -- (4,2) node[dot]{} node[lab,right]{$B$};
\draw[emph] (1,3) node[dot]{} node[lab,above]{$C$} -- (3,-1) node[dot]{} node[lab,below]{$D$};
\node[hl dot] at (2,1) {};
\node[lab,note] at (2,-2.2) {proper};
\end{scope}
\begin{scope}[xshift=6.5cm]
\draw[emph] (0,0) node[dot]{} node[lab,below left]{$A$} -- (2,2) node[dot]{} node[lab,left]{$B$};
\draw[emph] (3,3) node[dot]{} node[lab,right]{$C$} -- (5,5) node[dot]{} node[lab,right]{$D$};
\draw[faint,dashed] (2,2) -- (3,3);
\node[lab,note] at (2.5,-2.2) {collinear, disjoint};
\end{scope}
\begin{scope}[xshift=14cm]
\draw[emph] (0,0) node[dot]{} node[lab,below left]{$A$} -- (4,0) node[dot]{} node[lab,below right]{$B$};
\draw[emph] (2,3) node[dot]{} node[lab,above]{$D$} -- (2,0);
\node[hl dot] at (2,0) {}; \node[lab,below] at (2,0) {$C$};
\node[lab,note] at (2,-2.2) {touching};
\end{scope}
\end{tikzpicture}
\end{center}
```

The three cases of @exm-segment-intersection-1. Only the first passes the sign test; the other two are settled by the collinear checks.

:::

::: {#rmk-segment-intersection-1 .remark name="Special cases decide the bugs"}

Most wrong answers come from the degenerate cases: collinear overlapping segments, a segment of length zero, and endpoints touching. Decide first whether touching counts as intersecting in the problem at hand, and keep the test in integers.

:::
