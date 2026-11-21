<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-1-q2" status="draft"}
1. Both norms are nonnegative, so the inequality is equivalent to $\lVert x-a\rVert_2^2\le\lVert x-b\rVert_2^2$.

2. Expanding, $x^Tx-2a^Tx+a^Ta\le x^Tx-2b^Tx+b^Tb$, that is,
$$2(b-a)^Tx\le b^Tb-a^Ta.$$
So $c=2(b-a)\ne0$ and $d=\lVert b\rVert_2^2-\lVert a\rVert_2^2$: a halfspace.

3. Picture: the boundary hyperplane passes through the midpoint $\frac12(a+b)$ (check: $2(b-a)^T\frac{a+b}2=b^Tb-a^Ta$) and is perpendicular to $b-a$; the halfspace is the side containing $a$ (@exm-separating-voronoi).
:::
