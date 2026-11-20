<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-1-q8" status="draft"}
(a) Open (a union of open intervals), not closed ($1 \notin U$ is a limit of $1 - 1/n \in U$).

(b) In $\mathbb{R}$: neither. Every ball about $0$ contains negative numbers, so it is not open; $1 - 1/n \to 1 \notin U$, so it is not closed.

- In $[-1,1]$: neither, for the same two reasons (both witnesses lie in $[-1,1]$).
- In $[0,1)$: $U$ is the whole space, so it is both open and closed.
- In $[0,2]$: open, since $U = [0,2] \cap (-1,1)$; not closed, since $1 \in [0,2]$ is a limit of points of $U$ but not in $U$.

(c) $U = (-\infty, 1)$, which is open and not closed.

1. $\sin n < 1$ for every integer $n$: $\sin n = 1$ would need $n = \pi/2 + 2k\pi$, making $\pi$ rational. So $U \subset (-\infty,1)$.

2. The fractional parts of $n/(2\pi)$ are dense in $[0,1]$ ($1/(2\pi)$ is irrational), so for every $x < 1$ there are arbitrarily large $n$ with $\sin n > x$. For such $n > -x$, $x \in (-n, \sin n)$. So $U = (-\infty,1)$.
:::

::: {.solution for="prob-camib-ats-1-q9" status="draft"}
(a) Open (the ball of radius $y$ about $(x,y)$ stays in it), not closed ($(0,1/n) \to (0,0)$).

(b) Open, as the complement of the closed $x$-axis; not closed (same sequence).

(c) Closed (a limit of points $(x_n,0)$ with $x_n \in [0,1]$ is $(x,0)$ with $x \in [0,1]$); not open (every ball about a point of it contains points with $y \ne 0$).

(d) Neither: not open as in (c); not closed since $(1/n, 0) \to (0,0) \notin$ the set.

(e) Closed, not open.

1. Not open: every ball about $(0,0)$ contains $(\varepsilon, \varepsilon/2)$, with $y/x = 1/2 \notin \mathbb{N}$.

2. Closed: let $(x_n,y_n)$ in the set converge to $(x,y)$. If $x = 0$, the limit is in the set. If $x \ne 0$, then $x_n \ne 0$ for large $n$, and $k_n = y_n/x_n \in \mathbb{N}$ converges to $y/x$. A convergent sequence of integers is eventually constant, so $y/x = k_n \in \mathbb{N}$ for large $n$.

(f) Neither. Not open: any ball about $(1,0)$ contains $(1, \varepsilon\sqrt2)$ with small rational $\varepsilon$, where $y/x \notin \mathbb{Q}$. Not closed: $(1, q_n)$ with rationals $q_n \to \sqrt2$ converges to $(1,\sqrt2)$, which is not in the set.
:::

::: {.solution for="prob-camib-ats-1-q10" status="draft"}
*Uniform metric.* Both sets are closed and not open.

1. $|f(\frac12) - g(\frac12)| \le d(f,g)$ and $|\int f - \int g| \le d(f,g)$, so $f \mapsto f(\frac12)$ and $f \mapsto \int_0^1 f$ are continuous, and each set is the preimage of the closed set $\{0\}$.

2. Neither set is open: for $f$ in the set and any $\varepsilon > 0$, the function $f + \varepsilon/2$ is within $\varepsilon$ of $f$ but outside the set.

*$L^1$ metric.*

3. (b) is unchanged: $|\int f - \int g| \le \int|f - g|$, so it is closed, and $f + \varepsilon/2$ shows it is not open.

4. (a) is no longer closed. Let $t_n$ be the tent of height $1$ centred at $\frac12$ with base of width $2/n$, and $h_n = 1 - t_n$. Then $h_n(\frac12) = 0$ and $\int|h_n - 1| = \int t_n = 1/n \to 0$, but the limit $1$ is not in the set. It is still not open (same example as step 2).
:::
