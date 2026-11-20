<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-2-q9" status="draft"}
The hypothesis says exactly that $d(f(x),f(y)) < d(x,y)$ whenever $x \ne y$.

(a) If $f(x) = x$ and $f(y) = y$ with $x \ne y$, then $d(x,y) = d(f(x),f(y)) < d(x,y)$, which is impossible.

(b) Neither. Let $X = [1,\infty)$, closed in $\mathbb{R}$ and hence complete, and $f(x) = x + 1/x$, which maps $X$ into $X$.

1. For $x \ne y$ in $X$: $f(x) - f(y) = (x - y)\left(1 - \frac{1}{xy}\right)$ with $0 < 1 - \frac{1}{xy} < 1$ (as $xy > 1$). So $f$ has the property.

2. $f$ is not a contraction: the factor $1 - \frac{1}{xy} \to 1$ as $x, y \to \infty$.

3. $f$ has no fixed point, since $1/x \ne 0$.

(c)

1. $g(x) = d(x,f(x))$ is continuous, so on the compact space $X$ it attains its minimum at some $x_0$.

2. If $f(x_0) \ne x_0$, then $g(f(x_0)) = d(f(x_0), f(f(x_0))) < d(x_0, f(x_0)) = g(x_0)$, contradicting minimality. So $f(x_0) = x_0$, and the fixed point is unique by (a).
:::
