<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-4-q2" status="draft"}
1. Splitting the integral at $t = x$,
$$g(x) = (x-1)\int_0^x tf(t)\,dt + x\int_x^1 (t-1)f(t)\,dt.$$

2. The integrands $tf(t)$ and $(t-1)f(t)$ are continuous, so by the fundamental theorem of calculus and the product rule
$$g'(x) = \int_0^x tf(t)\,dt + (x-1)xf(x) + \int_x^1 (t-1)f(t)\,dt - x(x-1)f(x) = \int_0^x tf(t)\,dt + \int_x^1 (t-1)f(t)\,dt.$$

3. Again by the fundamental theorem of calculus, $g''(x) = xf(x) - (x-1)f(x) = f(x)$.
:::

::: {.solution for="prob-cama1s-4-q3" status="draft"}
(a)

1. Let $H(y) = h(y)$ for $y > 0$ and $H(y) = 0$ for $y \le 0$. On $y > 0$ and on $y < 0$, $H$ is infinitely differentiable. At $0$, sheet 3 showed that all derivatives of $h$ from the right are $0$ and tend to $0$; from the left $H$ is $0$. So $H$ is infinitely differentiable with all derivatives $0$ at $0$, and $H(y) > 0$ exactly when $y > 0$.

2. Let $g(x) = H(x - a)H(b - x)$. It is infinitely differentiable as a product, and $g(x) > 0$ iff $x - a > 0$ and $b - x > 0$, that is, iff $x \in (a,b)$.

(b)

1. Let $g_1$ be the function of (a) for the interval $(-2,-1)$ and $c = \int_{-2}^{-1}g_1 > 0$. Let $k(x) = \frac1c\int_{-2}^x g_1(t)\,dt$. By the fundamental theorem of calculus, $k' = g_1/c$, so $k$ is infinitely differentiable. Also $k = 0$ on $(-\infty,-2]$, $k = 1$ on $[-1,\infty)$, and $0 \le k \le 1$.

2. Let $F(x) = k(x)k(-x)$. For $|x| \le 1$ both factors are $1$, so $F = 1$ on $[-1,1]$. For $x \ge 2$, $k(-x) = 0$; for $x \le -2$, $k(x) = 0$. So $F = 0$ outside $(-2,2)$, and $F$ is infinitely differentiable.

(c)

1. Let $F$ be as in (b) and $S(x) = \sum_{n\in\mathbb{Z}}F(x - n)$. Near any point only finitely many terms (at most $5$) are non-zero, so $S$ is infinitely differentiable. Each $x$ is within $\frac12$ of some integer $n$, and then $F(x - n) = 1$; all terms are $\ge 0$, so $S \ge 1$. Clearly $S(x - m) = S(x)$ for every integer $m$.

2. Let $\psi = F/S$. It is infinitely differentiable, non-negative, and $0$ outside $(-2,2)$. Using the periodicity of $S$,
$$\sum_n \psi(x - n) = \sum_n \frac{F(x - n)}{S(x - n)} = \frac{1}{S(x)}\sum_n F(x - n) = 1.$$
:::

::: {.solution for="prob-cama1s-4-q13" status="draft"}
Take $\theta \ne 0$.

1. *Recurrence.* Let $u(x) = (1 - x^2)^n$. For $n \ge 2$, $u$ and $u'$ vanish at $\pm1$. Integrating by parts twice (the boundary terms vanish),
$$I_n = -\frac1\theta\int_{-1}^1 u'(x)\sin(\theta x)\,dx = -\frac{1}{\theta^2}\int_{-1}^1 u''(x)\cos(\theta x)\,dx.$$

2. $u'' = -2n(1-x^2)^{n-1} + 4n(n-1)x^2(1-x^2)^{n-2}$. Writing $x^2 = 1 - (1 - x^2)$ gives $u'' = -2n(2n-1)(1-x^2)^{n-1} + 4n(n-1)(1-x^2)^{n-2}$. So $\theta^2I_n = 2n(2n-1)I_{n-1} - 4n(n-1)I_{n-2}$.

3. *Polynomials.* Let $J_n = \theta^{2n+1}I_n$. Direct integration gives $I_0 = 2\sin\theta/\theta$ and $I_1 = 4\sin\theta/\theta^3 - 4\cos\theta/\theta^2$, so $J_0 = 2\sin\theta$ and $J_1 = 4\sin\theta - 4\theta\cos\theta$. Take $P_0 = 2$, $Q_0 = 0$, $P_1 = 4$, $Q_1 = -4\theta$.

4. Multiplying the recurrence by $\theta^{2n-1}$: $J_n = 2n(2n-1)J_{n-1} - 4n(n-1)\theta^2J_{n-2}$. If $J_k = k!(P_k\sin\theta + Q_k\cos\theta)$ for $k = n-1, n-2$, then $J_n = n!(P_n\sin\theta + Q_n\cos\theta)$ with
$$P_n = 2(2n-1)P_{n-1} - 4\theta^2P_{n-2}, \qquad Q_n = 2(2n-1)Q_{n-1} - 4\theta^2Q_{n-2}.$$
These have integer coefficients and degree at most $2n - 2 \le 2n$, by induction.

5. *Irrationality.* Suppose $\pi/2 = a/b$ with positive integers $a, b$. At $\theta = \pi/2$ we have $\sin\theta = 1$ and $\cos\theta = 0$, so
$$\frac{a^{2n+1}}{n!}I_n(\pi/2) = b^{2n+1}P_n(a/b).$$
The right side is an integer, since $\deg P_n \le 2n$.

6. The integrand of $I_n(\pi/2)$ is positive on $(-1,1)$, so $I_n(\pi/2) > 0$, and $I_n(\pi/2) \le 2$. So the integer $a^{2n+1}I_n(\pi/2)/n!$ lies in $(0, 2a^{2n+1}/n!]$. But $a^{2n+1}/n! \to 0$, so for large $n$ it lies strictly between $0$ and $1$, a contradiction. Hence $\pi/2$, and so $\pi$, is irrational.
:::
