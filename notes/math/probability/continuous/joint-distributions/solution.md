<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-3-q2" status="draft"}
(a) Integrating the joint density $\lambda e^{-\lambda x}\mu e^{-\mu y}$ over $x<y$:
$$P(X<Y)=\int_0^\infty\lambda e^{-\lambda x}e^{-\mu x}\,dx=\frac{\lambda}{\lambda+\mu}.$$

(b) $P(\min_kX_k>t)=\prod_kP(X_k>t)=e^{-(\sum_j\lambda_j)t}$, the tail of an $\text{Exponential}(\sum_j\lambda_j)$ variable.

(c) Let $Y=\min_{k\ne i}X_k$, which is $\text{Exponential}(\sum_{j\ne i}\lambda_j)$ by (b) and independent of $X_i$. Ties have probability $0$, so by (a) $P(X_i=\min_kX_k)=P(X_i<Y)=\lambda_i/\sum_j\lambda_j$. (This is @prp-min-of-exponentials.)
:::

::: {.solution for="prob-eecs126hw-3-q1" status="draft"}
The density is $A$ on $[1,2]\times[1,3]$ and on $[3,4]\times[1,3]$, $2A$ on $[2,3]\times[2,3]$, and $0$ elsewhere.

(a) Total mass $2A+2A+2A=6A=1$, so $A=\frac16$.

- $f_X$: integrating over $y$, each of the three columns gets $\frac13$, so $f_X=\frac13$ on $[1,4]$: $X$ is uniform.
- $f_Y$: for $1<y<2$ only the two outer columns contribute, $f_Y=2A=\frac13$; for $2<y<3$, $f_Y=A+2A+A=\frac23$.
- $\{X+Y\le3\}$ meets the support only in the triangle $1\le x\le2$, $1\le y\le3-x$, of area $\frac12$ and probability $\frac1{12}$. Given that event $(X,Y)$ is uniform on the triangle, so $f_{X\mid X+Y\le3}(x)=2(2-x)$ for $1\le x\le2$, a decreasing ramp.

(b) For $1<y<2$, $X$ is uniform on $[1,2]\cup[3,4]$; for $2<y<3$ the conditional density of $X$ is $1:2:1$ on the three columns. Both are symmetric about $2.5$, so $E[X\mid Y=y]=2.5$. Given $X=x$ in an outer column, $Y$ is uniform on $[1,3]$ and $E[Y\mid X=x]=2$; for $2<x<3$, $Y$ is uniform on $[2,3]$ and $E[Y\mid X=x]=2.5$.

(c) $E[X\mid Y]=2.5=E[X]$ is constant, so $E[XY]=E\bigl[Y\,E[X\mid Y]\bigr]=2.5\,E[Y]=E[X]E[Y]$ and $\operatorname{cov}(X,Y)=0$, although $X$ and $Y$ are not independent (@def-marginal-conditional-density).
:::
