<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-4-q10" status="draft"}
Write $p = (x_0,y_0)$ and take $(h,k)$ small, so that the points below stay in the ball.

(a)

1. $f(x_0 + h, y_0 + k) - f(p) = [f(x_0 + h, y_0 + k) - f(x_0, y_0 + k)] + [f(x_0, y_0 + k) - f(p)]$.

2. $t \mapsto f(t, y_0 + k)$ is differentiable on the segment, so by the mean value theorem the first bracket is $h\,\partial_1f(x_0 + \theta h, y_0 + k)$ for some $\theta \in (0,1)$. Write it as $h\,\partial_1f(p) + h\,\eta(h,k)$ with $\eta = \partial_1f(x_0 + \theta h, y_0 + k) - \partial_1f(p) \to 0$ as $(h,k) \to 0$, by continuity of $\partial_1f$ at $p$.

3. The second bracket is $k\,\partial_2f(p) + k\,\zeta(k)$ with $\zeta(k) \to 0$, by definition of $\partial_2f(p)$.

4. So $f(p + (h,k)) - f(p) - h\,\partial_1f(p) - k\,\partial_2f(p) = h\eta + k\zeta$, and $|h\eta + k\zeta| \le \|(h,k)\|(|\eta| + |\zeta|) = o(\|(h,k)\|)$. Hence $f$ is differentiable at $p$ with derivative $(h,k) \mapsto h\,\partial_1f(p) + k\,\partial_2f(p)$.

(b) Let $|\partial_1f| \le M$ on the ball. Split as in (a)1. By the mean value theorem the first bracket is at most $M|h|$. The second tends to $0$ as $k \to 0$ by continuity of $y \mapsto f(x_0,y)$. So $f(p + (h,k)) \to f(p)$ as $(h,k) \to 0$.
:::
