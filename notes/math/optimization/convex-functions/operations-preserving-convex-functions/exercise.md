::: {.problem #prob-ee364ahw-2-q4 origin="external" source="ee364ahw-2-q4"}
*A general vector composition rule.* Suppose
$$f(x)=h(g_1(x),g_2(x),\ldots,g_k(x))$$
where $h:\mathbf{R}^k\to\mathbf{R}$ is convex, and $g_i:\mathbf{R}^n\to\mathbf{R}$. Suppose that for each $i$, one of the following holds:

- $h$ is nondecreasing in the $i$th argument, and $g_i$ is convex
- $h$ is nonincreasing in the $i$th argument, and $g_i$ is concave
- $g_i$ is affine.

Show that $f$ is convex. (This composition rule subsumes all the ones given in the book, and is the one used in software systems such as CVX.) You can assume that $\mathbf{dom}\,h=\mathbf{R}^k$; the result also holds in the general case when the monotonicity conditions listed above are imposed on $\tilde h$, the extended-valued extension of $h$.
:::
