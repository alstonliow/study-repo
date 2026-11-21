<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-3-q1" status="draft"}
The feasible set is the unbounded polyhedron in the first quadrant above both lines $2x_1+x_2=1$ and $x_1+3x_2=1$. Its boundary runs from $(0,\infty)$ down the $x_2$-axis to $(0,1)$, along $2x_1+x_2=1$ to the corner $(\frac25,\frac15)$ where the two lines cross, along $x_1+3x_2=1$ to $(1,0)$, and then along the $x_1$-axis.

(a) A linear objective with positive coefficients is minimized at a vertex: $x_1+x_2$ equals $1$ at $(0,1)$ and $(1,0)$ and $\frac35$ at $(\frac25,\frac15)$. Check optimality there: adding $\frac25$ times the first constraint and $\frac15$ times the second gives $x_1+x_2\ge\frac35$ for every feasible point. Optimal set $\{(\frac25,\frac15)\}$, $p^\star=\frac35$.

(b) The feasible set contains $(t,t)$ for all $t\ge1$, on which $-x_1-x_2=-2t\to-\infty$. So $p^\star=-\infty$ and the optimal set is empty.

(c) $x_1\ge0$ always, and $x_1=0$ is feasible exactly when $x_2\ge1$. Optimal set $\{(0,x_2)\mid x_2\ge1\}$, $p^\star=0$.

(d) If $\max\{x_1,x_2\}=t$ then $1\le2x_1+x_2\le3t$, so $t\ge\frac13$; the point $(\frac13,\frac13)$ is feasible ($2x_1+x_2=1$, $x_1+3x_2=\frac43$) and attains $\frac13$. Any optimal point needs $x_1,x_2\le\frac13$ and $2x_1+x_2\ge1$, which forces $x_1=x_2=\frac13$. Optimal set $\{(\frac13,\frac13)\}$, $p^\star=\frac13$.

(e) Try the second constraint alone: minimizing $x_1^2+9x_2^2$ subject to $x_1+3x_2=1$ gives, from $\nabla f_0=(2x_1,18x_2)=\lambda(1,3)$, the point $x=(\frac12,\frac16)$. It satisfies $2x_1+x_2=\frac76>1$ and $x\succeq0$, so it is feasible, and $\nabla f_0(x)=(1,3)$ is a nonnegative multiple of the normal of the only active constraint, so the optimality criterion (@thm-convex-optimality-criterion) holds. Optimal set $\{(\frac12,\frac16)\}$, $p^\star=\frac14+\frac14=\frac12$.
:::
