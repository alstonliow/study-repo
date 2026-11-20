<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-3-q10" status="draft"}
1. Example: $f(\frac12) = 1$ and $f(x) = 0$ otherwise. Every lower sum is $0$. For the dissection $0 < \frac12 - \varepsilon < \frac12 + \varepsilon < 1$ the upper sum is $2\varepsilon$. So $f$ is integrable with $\int_0^1 f = 0$.

2. Now let $f \ge 0$ be continuous with $f(x_0) = c > 0$. By continuity there is an interval $[p,q] \subset [0,1]$ with $p < q$, containing $x_0$, on which $f > c/2$.

3. Take the dissection with points $0, p, q, 1$ (dropping repeats). Its lower sum is at least $(q - p)c/2$, since $f \ge 0$ elsewhere. So $\int_0^1 f \ge (q - p)c/2 > 0$.
:::

::: {.solution for="prob-cama1s-4-q4" status="draft"}
Yes.

1. Suppose $f(x_0) \ne 0$; replacing $f$ by $-f$ we may take $f(x_0) > 0$. By continuity, $f > 0$ on some interval around $x_0$, so there is $[p,q] \subset (a,b)$ with $p < q$ and $f > 0$ on $[p,q]$.

2. Let $g(x) = (x - p)(q - x)$ on $[p,q]$ and $g = 0$ elsewhere. It is continuous and vanishes near $a$ and $b$.

3. $fg$ is continuous, $\ge 0$ on $[a,b]$, and positive at $(p+q)/2$. A non-negative continuous function that is positive at a point has positive integral (sheet 3, question 10). So $\int_a^b fg > 0$, a contradiction.
:::
