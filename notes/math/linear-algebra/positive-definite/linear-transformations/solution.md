<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-10-q12" status="draft"}
1. $(1)'=0$, $(\cos x)'=-\sin x$, $(\sin x)'=\cos x$, $(\cos2x)'=-2\sin2x$, $(\sin2x)'=2\cos2x$.

2. Column $j$ of the matrix holds the coefficients of the derivative of basis function $j$ (@def-matrix-of-linear-map):
   $$D=\begin{pmatrix}0&0&0&0&0\\0&0&1&0&0\\0&-1&0&0&0\\0&0&0&0&2\\0&0&0&-2&0\end{pmatrix}.$$
   It is skew-symmetric, and its nullspace (the constants) is the kernel of differentiation.
:::
