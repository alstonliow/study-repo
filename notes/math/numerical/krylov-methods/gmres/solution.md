<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335ps-4-q1" status="draft"}
1. $x\in\mathcal K_n$ means $x=Q_n\mathbf{y}$ for some $\mathbf{y}\in\mathbb{C}^n$, since the columns of $Q_n$ form a basis of $\mathcal K_n$ (@thm-arnoldi-relation).

2. $b-Ax\perp\mathcal K_n$ means $Q_n^*(b-AQ_n\mathbf{y})=\mathbf{0}$.

3. $Q_n^*AQ_n=H_n$ (@thm-arnoldi-relation), and with $q_1=b/\lVert b\rVert$, $Q_n^*b=\lVert b\rVert\mathbf{e}_1$.

4. So $\mathbf{y}$ solves the $n\times n$ Hessenberg system
$$H_n\mathbf{y}=\lVert b\rVert_2\,\mathbf{e}_1,\qquad x=Q_n\mathbf{y}.$$

This is the *full orthogonalization method* (FOM), a Galerkin method: it imposes orthogonality of the residual instead of minimality. It is the GMRES least squares problem with the last row of $\tilde H_n$ dropped. Its residual norm need not decrease monotonically, and if $H_n$ is singular the iterate does not exist even though GMRES's does; when it exists, its residual is $-h_{n+1,n}y_n\,q_{n+1}$ by the Arnoldi relation, which is cheap to monitor.
:::
