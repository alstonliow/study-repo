<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-2-q10" status="draft"}
Assume $|y_0| < b$, so that $y_0$ is an interior value, and put $r = b - |y_0| > 0$ and $M = \sup|f|$.

(a) Not necessarily. Take $f(x,y) = 2\sqrt{|y|}$ and $y_0 = 0$. Both $y = 0$ and $y = x|x|$ (on $|x| \le \min(a, \sqrt b)$) solve the problem: $\frac{d}{dx}(x|x|) = 2|x| = 2\sqrt{|x|x||}$.

(b)

1. By problem 12 (in two variables), there are polynomials $f_k$ with $\sup|f_k - f| < 1/k$ on the rectangle. A polynomial has bounded partial derivatives on the compact rectangle, so by the mean value theorem $f_k$ is Lipschitz in $y$ (indeed in both variables).

2. $\sup|f_k| \le M + 1$. Let $h = \min(a, r/(M+1))$. Picard–Lindelöf on $[0,h]$ with the ball of radius $r$ about $y_0$ (its hypothesis $(M+1)h \le r$ holds) gives a solution of $y_k' = f_k(x,y_k)$, $y_k(0) = y_0$ on $[0,h]$; applying it to $x \mapsto -x$ gives one on $[-h,0]$. Both have derivative $f_k(0,y_0)$ at $0$, so together they solve the problem on $I_k = [-h,h]$, the same interval for every $k$.

3. As $k \to \infty$: the $y_k$ take values in $[y_0 - r, y_0 + r]$ and satisfy $|y_k'| \le M + 1$, so they are uniformly bounded and equicontinuous on $[-h,h]$. They need not converge, but by Arzelà–Ascoli (problem 13(d)) a subsequence converges uniformly. Its limit need not be unique (different subsequences may give different solutions, as (a) allows).

(c)

1. Let $y_{k_j} \to y$ uniformly on $[-h,h]$, and take $\epsilon = h$. Each $y_k$ satisfies $y_k(x) = y_0 + \int_0^x f_k(t, y_k(t))\,dt$.

2. $|f_{k_j}(t,y_{k_j}(t)) - f(t,y(t))| \le \sup|f_{k_j} - f| + |f(t,y_{k_j}(t)) - f(t,y(t))|$. The first term tends to $0$; the second tends to $0$ uniformly in $t$ because $f$ is uniformly continuous on the compact rectangle and $y_{k_j} \to y$ uniformly.

3. Passing to the limit under the integral, $y(x) = y_0 + \int_0^x f(t,y(t))\,dt$ for $|x| \le h$. The integrand is continuous, so by the fundamental theorem of calculus $y' = f(x,y)$ and $y(0) = y_0$. This is Peano's existence theorem. Compared with (b), we get existence along a subsequence, but no uniqueness.
:::
