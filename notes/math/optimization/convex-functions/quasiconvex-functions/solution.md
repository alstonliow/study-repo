<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-2-q3" status="draft"}
(a) $f''(x)=e^x>0$, so $f$ is strictly convex and not concave. It is increasing, so every sublevel and superlevel set is an interval: $f$ is quasiconvex and quasiconcave (quasilinear).

(b) $\nabla^2f=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has eigenvalues $\pm1$, so $f$ is neither convex nor concave. The superlevel sets $\{x_1x_2\ge\alpha\}$ are convex (for $\alpha>0$ the region above the hyperbola $x_2=\alpha/x_1$, which is the epigraph of a convex function; for $\alpha\le0$ all of $\mathbf{R}^2_{++}$), so $f$ is quasiconcave. It is not quasiconvex: $(1,4)$ and $(4,1)$ give $f=4$, their midpoint $(2.5,2.5)$ gives $6.25$.

(c) $\nabla^2f=\frac{1}{x_1x_2}\begin{bmatrix}2/x_1^2&1/(x_1x_2)\\1/(x_1x_2)&2/x_2^2\end{bmatrix}$ has positive diagonal and determinant $\frac{3}{x_1^4x_2^4}>0$, so it is positive definite and $f$ is convex, hence quasiconvex. It is not concave. Its superlevel sets $\{x_1x_2\le1/\alpha\}$ (for $\alpha>0$) are not convex ($(1,4)$, $(4,1)$ satisfy $x_1x_2\le4$, the midpoint does not), so it is not quasiconcave.

(d) $\nabla^2f=\begin{bmatrix}0&-1/x_2^2\\-1/x_2^2&2x_1/x_2^3\end{bmatrix}$ has determinant $-1/x_2^4<0$, so $f$ is neither convex nor concave. It is linear-fractional, so its sublevel and superlevel sets are halfspaces intersected with $\mathbf{R}^2_{++}$: $f$ is quasiconvex and quasiconcave (@exm-quasiconvex).

(e) This is the quadratic-over-linear function, convex (@exm-convex-by-hessian), hence quasiconvex. It is not concave. It is not quasiconcave: $(-1,1)$ and $(1,1)$ give $f=1$, but their midpoint $(0,1)$ gives $0$.

(f) For $0<\alpha<1$,
$$\nabla^2f=\alpha(1-\alpha)x_1^\alpha x_2^{1-\alpha}\begin{bmatrix}-1/x_1^2&1/(x_1x_2)\\1/(x_1x_2)&-1/x_2^2\end{bmatrix}=-\alpha(1-\alpha)f(x)\,vv^T,\quad v=\Big(\frac1{x_1},-\frac1{x_2}\Big),$$
which is negative semidefinite, so $f$ is concave and quasiconcave. It is not convex, and not quasiconvex: $(1,4)$ and $(4,1)$ give $f=4^{1-\alpha}$ and $4^\alpha$, both at most $\max\{4^\alpha,4^{1-\alpha}\}$, while the midpoint gives $2.5>\max\{4^\alpha,4^{1-\alpha}\}$ when, for instance, $\alpha=\frac12$ ($2.5>2$). For $\alpha\in\{0,1\}$, $f$ is linear ($x_2$ or $x_1$): convex, concave, quasiconvex and quasiconcave.
:::
