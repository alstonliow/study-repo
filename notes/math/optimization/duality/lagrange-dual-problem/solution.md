<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-4-q2" status="draft"}
(a) $(x-2)(x-4)\le0$ iff $2\le x\le4$. On $[2,4]$ the increasing function $x^2+1$ is least at $x^\star=2$, so $p^\star=5$.

(b) $L(x,\lambda)=x^2+1+\lambda(x^2-6x+8)=(1+\lambda)x^2-6\lambda x+1+8\lambda$. (Plot: the parabola $x^2+1$ with the interval $[2,4]$ marked and the point $(2,5)$; the Lagrangians for $\lambda=1,2,3$ are parabolas that lie below $x^2+1$ on $[2,4]$, where the constraint term is $\le0$, and above it outside.) For $\lambda>-1$, $L$ is a convex parabola minimized at $x=3\lambda/(1+\lambda)$, so
$$g(\lambda)=1+8\lambda-\frac{9\lambda^2}{1+\lambda}\quad(\lambda>-1),\qquad g(\lambda)=-\infty\quad(\lambda\le-1).$$
For $\lambda\ge0$: $5-g(\lambda)=\frac{(4-8\lambda)(1+\lambda)+9\lambda^2}{1+\lambda}=\frac{(\lambda-2)^2}{1+\lambda}\ge0$, which is the lower bound property, with equality only at $\lambda=2$.

(c) The dual problem is maximize $1+8\lambda-\frac{9\lambda^2}{1+\lambda}$ subject to $\lambda\ge0$. It is a concave maximization: $g''(\lambda)=-\frac{18}{(1+\lambda)^3}<0$ for $\lambda>-1$ (write $\frac{9\lambda^2}{1+\lambda}=9(\lambda-1)+\frac{9}{1+\lambda}$). By (b), $g(\lambda)=5-\frac{(\lambda-2)^2}{1+\lambda}$, maximized at $\lambda^\star=2$ with $d^\star=5=p^\star$. Strong duality holds, as Slater's theorem predicts ($x=3$ is strictly feasible).

(d) $x^2-6x+8\le u$ iff $(x-3)^2\le1+u$. For $u<-1$ the problem is infeasible, $p^\star(u)=\infty$. For $u\ge-1$ the feasible set is $[3-\sqrt{1+u},\,3+\sqrt{1+u}]$. If $3-\sqrt{1+u}\ge0$, i.e. $u\le8$, the optimum is the left end, so $p^\star(u)=(3-\sqrt{1+u})^2+1=11+u-6\sqrt{1+u}$; for $u\ge8$ the interval contains $0$ and $p^\star(u)=1$. (Plot: $p^\star$ decreases from $10$ at $u=-1$ to $1$ at $u=8$ and is constant after.) At $u=0$, $\frac{dp^\star}{du}=1-\frac{3}{\sqrt{1+u}}\Big|_{u=0}=-2=-\lambda^\star$, as in @cor-local-sensitivity.
:::
