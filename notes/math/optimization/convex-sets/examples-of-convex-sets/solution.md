<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-1-q1" status="draft"}
1. The line through the origin in the direction of the normal $a$ meets the hyperplane $a^Tx=b_i$ at $x_i=(b_i/\lVert a\rVert_2^2)\,a$, since $a^Tx_i=b_i$.

2. The segment from $x_1$ to $x_2$ is perpendicular to both hyperplanes, so its length is their distance:
$$\lVert x_1-x_2\rVert_2=\frac{\lvert b_1-b_2\rvert}{\lVert a\rVert_2^2}\lVert a\rVert_2=\frac{\lvert b_1-b_2\rvert}{\lVert a\rVert_2}.$$
:::

::: {.solution for="prob-ee364ahw-1-q5" status="draft"}
A symmetric matrix is positive semidefinite iff all its *principal* minors (determinants of submatrices on the same set of rows and columns) are nonnegative. The leading minors alone are not enough: $\operatorname{diag}(0,-1)$ has leading minors $0$ and $0$.

1. $n=1$: $\mathbf{S}^1_+=\{x_1\mid x_1\ge0\}$.

2. $n=2$: $x_1\ge0$, $x_3\ge0$, $x_1x_3-x_2^2\ge0$ (@exm-psd-cone-two-by-two).

3. $n=3$: the diagonal entries $x_1\ge0$, $x_4\ge0$, $x_6\ge0$; the $2\times2$ principal minors
$$x_1x_4-x_2^2\ge0,\qquad x_4x_6-x_5^2\ge0,\qquad x_1x_6-x_3^2\ge0;$$
and the determinant
$$x_1x_4x_6+2x_2x_3x_5-x_1x_5^2-x_4x_3^2-x_6x_2^2\ge0.$$
:::
