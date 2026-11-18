<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-3-q5" status="draft"}
a) With $f(x)=x^3-9$, @def-newtons-method gives
$$x_{k+1}=x_k-\frac{x_k^3-9}{3x_k^2}=\frac13\Big(2x_k+\frac9{x_k^2}\Big).$$
In double precision (16 digits):

| $k$ | $x_k$ |
|---|---|
| 0 | 2 |
| 1 | 2.083333333333333 |
| 2 | 2.080088888888889 |
| 3 | 2.080083823064241 |
| 4 | 2.080083823051904 |
| 5 | 2.080083823051904 |

To 6 significant figures $9^{1/3}=2.08008$ (already from $k=2$). At $k=4$ the value no longer changes: the method has reached the full accuracy of the computer.

b) $x_0=2$ is smaller than $9^{1/3}$; every later $x_k$ ($k\ge1$) is larger than $9^{1/3}$. $x_1>x_0$, and from then on $x_k<x_{k-1}$ (decreasing towards the root). Reason: $f$ is increasing and concave up for $x>0$. A tangent line of a concave-up graph lies below the graph, so its zero is to the right of the true root whatever the starting point; hence $x_1,x_2,\ldots$ all lie to the right of the root. For $x_k$ to the right of the root, $f(x_k)>0$ and $f'(x_k)>0$, so the step $-f(x_k)/f'(x_k)$ is negative: the iterates decrease (but stay to the right).

c) $9^{1/3}=2(1+\frac18)^{1/3}$, and $(1+x)^{1/3}\approx1+\frac x3-\frac{x^2}9$, so
$$9^{1/3}\approx2\Big(1+\frac1{24}-\frac1{576}\Big)=2.079861.$$
The exact value is $2.080084$, so the difference is about $2.2\times10^{-4}$. A good estimate of it is the next term of the series, $2\cdot\frac{(1/3)(-2/3)(-5/3)}{6}\Big(\frac18\Big)^3=2\cdot\frac{5}{81}\cdot\frac1{512}\approx2.4\times10^{-4}$.
:::
