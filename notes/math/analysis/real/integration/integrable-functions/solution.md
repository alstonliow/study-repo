<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-3-q9" status="draft"}
Yes.

1. $|f| \le 1$. Let $\varepsilon \in (0,1)$.

2. On $[\varepsilon, 1]$, $f$ is continuous, hence integrable, so there is a dissection $D'$ of $[\varepsilon,1]$ with $U(f,D') - L(f,D') < \varepsilon$.

3. Let $D = \{0\} \cup D'$. The interval $[0,\varepsilon]$ contributes at most $\varepsilon(\sup f - \inf f) \le 2\varepsilon$ to $U(f,D) - L(f,D)$. So $U(f,D) - L(f,D) < 3\varepsilon$.

4. By Riemann's criterion, $f$ is integrable on $[0,1]$.
:::

::: {.solution for="prob-cama1s-3-q11" status="draft"}
In (a) we read $[-1,1]$ as $[a,b]$, the domain of $g$; in (c) we work on an interval $[a,b]$ containing $[0,1]$ (for instance $[-1,1]$).

(a) Since $f_1, f_2$ are increasing,
$$\sum_j |g(x_j) - g(x_{j-1})| \le \sum_j \big(f_1(x_j) - f_1(x_{j-1})\big) + \sum_j \big(f_2(x_j) - f_2(x_{j-1})\big) = f_1(b) - f_1(a) + f_2(b) - f_2(a),$$
so $K = f_1(b) - f_1(a) + f_2(b) - f_2(a)$ works.

(b) Monotone functions are integrable, and a difference of integrable functions is integrable.

(c)

1. $h$ is continuous on $[a,b]$ (at $0$, $|h(x)| \le |x|$), hence integrable.

2. Let $y_k = 1/((k + \frac12)\pi)$ for $k = 1, \dots, N$. Then $h(y_k) = (-1)^k y_k$, so $|h(y_k) - h(y_{k+1})| = y_k + y_{k+1} \ge y_k$.

3. For the partition of $[a,b]$ that contains the points $y_N < \cdots < y_1$ (together with $a$ and $b$), the sum in (a) is at least $\sum_{k=1}^{N-1} y_k = \frac1\pi\sum_{k=1}^{N-1}\frac{1}{k + \frac12}$, which tends to $\infty$ as $N \to \infty$.

4. So no constant $K$ as in (a) exists for $h$, and by (a) $h$ is not a difference of two increasing functions.
:::

::: {.solution for="prob-cama1s-3-q12" status="draft"}
(a)

1. Take $f$ increasing (otherwise use $-f$). At each $x$ the one-sided limits $f(x^-) = \sup_{t<x}f(t)$ and $f(x^+) = \inf_{t>x}f(t)$ exist, and $f(x^-) \le f(x) \le f(x^+)$.

2. $f$ is continuous at $x$ iff $f(x^-) = f(x^+)$. So at each discontinuity $x$ the open interval $J_x = (f(x^-), f(x^+))$ is non-empty; pick a rational $q_x \in J_x$.

3. For $x < y$, $f(x^+) \le f(\frac{x+y}{2}) \le f(y^-)$, so $J_x$ and $J_y$ are disjoint and $q_x \ne q_y$. Hence $x \mapsto q_x$ is an injection of the set of discontinuities into $\mathbb{Q}$, and the set is countable.

(b)

1. $0 \le 2^{-n}f_n(x) \le 2^{-n}$ and $\sum 2^{-n}$ converges, so the series converges for every $x$ by comparison, and $0 \le f \le 1$.

2. Each $f_n$ is increasing, so for $x \le y$ every partial sum satisfies $\sum_{n\le N}2^{-n}f_n(x) \le \sum_{n\le N}2^{-n}f_n(y)$; letting $N \to \infty$, $f(x) \le f(y)$.

3. Fix $m$ and $x \in [0, x_m)$ (non-empty as $x_m > 0$). Every term $2^{-n}(f_n(x_m) - f_n(x))$ is $\ge 0$, and the $m$-th is $2^{-m}$. So $f(x_m) - f(x) \ge 2^{-m}$ for all $x < x_m$, and $f$ is not continuous at $x_m$ (from the left).

4. If the $x_n$ enumerate $\mathbb{Q} \cap (0,1]$, then $f$ is an increasing, hence integrable, function that is discontinuous at every rational of $(0,1]$.
:::
