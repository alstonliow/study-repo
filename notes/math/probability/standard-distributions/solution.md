<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-04" status="draft"}
The suggestion does not give a fair die. The number of Heads is
$\mathrm{Bin}(5,\frac12)$, so the probabilities of $1,\dots,6$ are
$$\tfrac1{32},\ \tfrac5{32},\ \tfrac{10}{32},\ \tfrac{10}{32},\ \tfrac5{32},\ \tfrac1{32}.$$
Rolling a $3$ or $4$ is ten times as likely as rolling a $1$ or $6$.

A fair alternative:

1. Toss three coins and read them as a binary number $b\in\{0,\dots,7\}$.
   All eight values are equally likely.

2. If $b\le5$, output $b+1$. If $b\in\{6,7\}$, discard the result and toss
   again.

3. Each accepted round gives each of $1,\dots,6$ with probability $\frac16$.
   A round is accepted with probability $\frac68$, so on average this takes
   $\frac43$ rounds, i.e. $4$ tosses.

With a fixed number of coins this cannot be done exactly: every outcome of
$n$ tosses has probability $2^{-n}$, so every event has probability
$k/2^n$, which is never $\frac16$.
:::

::: {.solution for="prob-probability-2-07" status="draft"}
$E(X) = np = 8$, $\mathrm{Var}(X) = np(1-p) = 4$, and $\sigma = 2$. All
probabilities below are $\binom{16}k/2^{16}$ summed over the relevant $k$.

(a) $\Pr(X = 8) = \binom{16}8/2^{16} = 12{,}870/65{,}536\approx 0.196$. So
    "exactly half" happens less than one time in five.

(b) $|X-8|\ge4$ means $X\le4$ or $X\ge12$:
    $$\Pr = \frac{2(1+16+120+560+1820)}{65{,}536} = \frac{5{,}034}{65{,}536}\approx 0.077.$$

(c) $|X-8|\ge6$ means $X\le2$ or $X\ge14$:
    $$\Pr = \frac{2(1+16+120)}{65{,}536} = \frac{274}{65{,}536}\approx 0.0042.$$

(d) Chebyshev gives at most $\frac14$ for (b) and $\frac19\approx 0.11$ for
    (c). Both bounds hold but are much larger than the exact values: about
    $3$ times too big for (b) and about $27$ times for (c).
:::

::: {.solution for="prob-probability-2-08" status="draft"}
(a) Poisson with mean $\lambda = 0.83$:
    $\Pr(N = k) = e^{-0.83}\,0.83^k/k!$.

(b) $\Pr(N = 0) = e^{-0.83}\approx 0.436$.

(c) In $t$ minutes the count is Poisson with mean $0.83t$, so
    $\Pr(\text{at least one}) = 1 - e^{-0.83t}$. We need
    $$1 - e^{-0.83t}\ge 0.95\iff e^{-0.83t}\le 0.05\iff t\ge\frac{\ln 20}{0.83}\approx 3.61.$$
    So be prepared to wait about $3.6$ minutes.
:::

::: {.solution for="prob-probability-2-09" status="draft"}
(a) Geometric with $p = 0.0125$: the number of balls up to and including
    the dismissal ball, $\Pr(X = k) = (1-p)^{k-1}p$ for $k\ge1$.

(b) $\Pr(X = 1) = p = 0.0125$.

(c) $E(X) = 1/p = 80$ balls.

(d) The geometric distribution is memoryless:
    $$\Pr(X > 200 + k\mid X > 200) = (1-p)^k = \Pr(X > k).$$
    So the remaining number of balls has the same distribution as at the
    start, and we expect $80$ more. (Under this model the batter does not
    "get their eye in".)
:::

::: {.solution for="prob-probability-2-10" status="draft"}
(a) **Uniform** on $\{1,\dots,13\}$: each value has $4$ of the $52$ cards.

(b) **Binomial** $\mathrm{Bin}(n,p)$, where $n$ is the number of days the
    train runs that week and $p$ is the daily probability of being late.

(c) **Poisson**: rare independent events arriving at a constant average rate.

(d) **Geometric**: the number of independent trials until the first success,
    where "success" is the train being on time.

(e) **Geometric**, with success probability $3/n$ if there are $n$
    equally likely coupons. (This is not the full coupon collector problem,
    which waits for all coupons.)

(f) **Binomial** $\mathrm{Bin}(7,q)$, where $q$ is the probability that a
    shell lands aperture-up. Shells are not coins, so $q$ need not be $\frac12$.

(g) $3/7 = 0.\overline{428571}$ has period $6$, and $1{,}002 = 167\cdot6$,
    so each of $1,2,4,5,7,8$ appears exactly $167$ times. **Uniform** on
    $\{1,2,4,5,7,8\}$.

(h) $5/11 = 0.\overline{45}$, so the digits $4$ and $5$ each appear $500$
    times. **Uniform** on $\{4,5\}$.

(i) **Uniform** on $\{0,\dots,9\}$ is the natural model. It is consistent
    with all digit counts of $\pi$ computed so far, but it has not been
    proved (it would follow if $\pi$ were *normal*).
:::
