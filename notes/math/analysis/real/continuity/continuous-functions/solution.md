<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-2-q2" status="draft"}
The set is $\{1/2\}$.

1. At $a = 1/2$: for every $x$, $|f(x) - \frac12|$ equals $|x - \frac12|$ (if $x$ is rational) or $|\frac12 - x|$ (if not). So $|f(x) - f(\frac12)| = |x - \frac12|$, and $\delta = \varepsilon$ works.

2. At $a \ne 1/2$: take rationals $q_n \to a$ and irrationals $r_n \to a$ (both sets are dense). Then $f(q_n) = q_n \to a$ and $f(r_n) = 1 - r_n \to 1 - a \ne a$. The two limits differ, so $f$ is not sequentially continuous at $a$, hence not continuous there.
:::

::: {.solution for="prob-cama1s-2-q4" status="draft"}
(a) For real $u, v$, $\max\{u,v\} = \frac12(u + v + |u - v|)$. Sums, scalar multiples and absolute values of continuous functions are continuous, so $\max\{u, v\}$ of two continuous functions is continuous. Since $h_1 = f_1$ and $h_{n+1} = \max\{h_n, f_{n+1}\}$, induction gives that every $h_n$ is continuous.

(b) No. Let $f_n(x) = \min\{1, nx\}$, which is continuous from $[0,1]$ to $[0,1]$. Then $h(0) = 0$ and, for $x > 0$, $f_n(x) = 1$ once $n \ge 1/x$, so $h(x) = 1$. So $h$ is discontinuous at $0$.
:::

::: {.solution for="prob-cama1s-2-q5" status="draft"}
1. Let $|f| \le M$. Fix $x_0 \in (a,b)$ and $\delta > 0$ with $[x_0 - \delta, x_0 + \delta] \subset [a,b]$. Put $g(h) = f(x_0 + h) - f(x_0)$ for $|h| \le \delta$; then $|g| \le 2M$.

2. $x_0 + h$ is the midpoint of $x_0$ and $x_0 + 2h$, so $f(x_0 + h) \le \frac12(f(x_0) + f(x_0 + 2h))$, that is, $g(h) \le \frac12 g(2h)$ when $|2h| \le \delta$. By induction, $g(h) \le 2^{-n}g(2^nh) \le 2^{1-n}M$ whenever $|h| \le 2^{-n}\delta$.

3. $x_0$ is the midpoint of $x_0 + h$ and $x_0 - h$, so $2f(x_0) \le f(x_0 + h) + f(x_0 - h)$, that is, $g(h) \ge -g(-h)$. With step 2 applied to $-h$: $g(h) \ge -2^{1-n}M$ for $|h| \le 2^{-n}\delta$.

4. So $|f(x_0 + h) - f(x_0)| \le 2^{1-n}M$ whenever $|h| \le 2^{-n}\delta$. Given $\varepsilon > 0$, choose $n$ with $2^{1-n}M < \varepsilon$; this proves continuity at $x_0$.

5. Not necessarily at the endpoints. Let $f(a) = 1$ and $f(x) = 0$ for $a < x \le b$. If $x \ne y$ or $x = y \ne a$, the midpoint lies in $(a,b]$, so the left side is $0$ and the right side is $\ge 0$; if $x = y = a$ both sides are $1$. So $f$ is bounded and satisfies the inequality, but it is discontinuous at $a$.
:::
