<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sequences-08" status="draft"}
(a) There are two errors.

    1. Step 2 uses the recurrence for $t_1$, but $t_1 = 1$ is given
       directly. The correct basis is simply $t_1 = 1\le\frac52$.

    2. Step 7 uses the hypothesis $t_k\le\frac52$ in the wrong direction.
       Since $t_k$ is subtracted, an *upper* bound on $t_k$ gives a *lower*
       bound on $3 - \frac12t_k$: from $t_k\le\frac52$ we only get
       $t_{k+1}\ge\frac74$. To bound $t_{k+1}$ from above we need a lower
       bound on $t_k$, which $S(k)$ does not provide.

(b) (i) Let $T(n)$ be the statement $1\le t_n\le\frac52$.

    1. *Basis.* $t_1 = 1$, so $T(1)$ holds.

    2. *Inductive step.* Assume $T(k)$. Since $-\frac12t_k$ lies between
       $-\frac54$ and $-\frac12$,
       $$\tfrac74 = 3 - \tfrac54\ \le\ t_{k+1}\ \le\ 3 - \tfrac12 = \tfrac52.$$
       In particular $1\le t_{k+1}\le\frac52$, which is $T(k+1)$.

    3. By induction $T(n)$ holds for all $n$, and so does $S(n)$.

    (ii) Applying the recurrence twice,
    $$t_{n+2} = 3 - \tfrac12\bigl(3 - \tfrac12t_n\bigr) = \tfrac32 + \tfrac14t_n.$$
    Here the coefficient of $t_n$ is positive, so an upper bound on $t_n$
    does give an upper bound on $t_{n+2}$.

    1. *Bases.* $t_1 = 1\le\frac52$ and $t_2 = 3 - \frac12 = \frac52$.

    2. *Step.* If $t_n\le\frac52$, then
       $t_{n+2}\le\frac32 + \frac58 = \frac{17}8\le\frac52$.

    3. Induction from $n = 1$ in steps of $2$ covers all odd $n$, and from
       $n = 2$ covers all even $n$.
:::

::: {.solution for="prob-sequences-09" status="draft"}
(a) The terms are ratios of consecutive Fibonacci numbers,
    $\varphi_n = f_{n+1}/f_n$:

    | $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    |---|---|---|---|---|---|---|---|---|---|---|
    | $\varphi_n$ | 1 | 2 | 1.5 | 1.666667 | 1.6 | 1.625 | 1.615385 | 1.619048 | 1.617647 | 1.618182 |

    | $n$ | 11 | 12 | 13 | 14 | 15 | 16–20 |
    |---|---|---|---|---|---|---|
    | $\varphi_n$ | 1.617978 | 1.618056 | 1.618026 | 1.618037 | 1.618033 | 1.618034 |

    The terms alternate above and below the limit.

(b) About $1.618034$.

(c) $\varphi = 1 + \frac1\varphi$ gives $\varphi^2 - \varphi - 1 = 0$. The
    terms are positive, so take the positive root:
    $$\varphi = \frac{1+\sqrt5}2\approx 1.6180340.$$

(d) $N = 9$. $|\varphi_8 - \varphi|\approx 0.00101$, but
    $|\varphi_9 - \varphi| = |\tfrac{55}{34} - \varphi|\approx 0.00039$, and
    by (h) all later terms stay within $0.001$.

Write $\delta = 0.001$. All terms are at least $1$, so they are positive.

(e) 1. Assume $\varphi_n < \varphi + \delta$. Then
       $$\varphi_{n+1} = 1 + \frac1{\varphi_n} > 1 + \frac1{\varphi+\delta} = 1 + \frac1\varphi\cdot\frac1{1 + \delta/\varphi}.$$

    2. By the hint with $x = \delta/\varphi > 0$,
       $\frac1{1+x} > 1 - x$. So
       $$\varphi_{n+1} > 1 + \frac1\varphi - \frac\delta{\varphi^2} = \varphi - \frac\delta{\varphi^2},$$
       using $1 + \frac1\varphi = \varphi$.

    3. $\varphi^2 = \varphi + 1 > 1$, so $\frac\delta{\varphi^2} < \delta$
       and $\varphi_{n+1} > \varphi - \delta$.

(f) 1. Assume $\varphi_n > \varphi - \delta$ (which is positive). Then
       $$\varphi_{n+1} < 1 + \frac1{\varphi - \delta} = 1 + \frac1\varphi\cdot\frac1{1 - \delta/\varphi}.$$

    2. $x = \delta/\varphi < \frac13$, so by the hint
       $\frac1{1-x} < 1 + \frac32x$, and
       $$\varphi_{n+1} < 1 + \frac1\varphi + \frac{3\delta}{2\varphi^2} = \varphi + \frac{3}{2\varphi^2}\,\delta.$$

    3. $\varphi^2\approx 2.618 > \frac32$, so $\frac3{2\varphi^2} < 1$ and
       $\varphi_{n+1} < \varphi + \delta$.

(g) If $\varphi - \delta < \varphi_n < \varphi + \delta$, then (e) gives
    $\varphi_{n+1} > \varphi - \delta$, and (f) gives
    $\varphi_{n+1} < \varphi + \delta$.

(h) Let $P(n)$ be the statement $\varphi - \delta < \varphi_n < \varphi + \delta$.
    $P(N)$ holds for $N = 9$ by (d), and $P(n)\Rightarrow P(n+1)$ by (g). By
    induction, $P(n)$ holds for all $n\ge N$.
:::

::: {.solution for="prob-sequences-10" status="draft"}
(a) No. With $a = \frac12$ and $\varepsilon = \frac14$, Lim wins only if
    $\frac14 < a_n < \frac34$. For $n\ge3$, $|a_n|\le\frac13$, so every
    choice of $n\ge3$ wins for Una.

(b) No. Every term with $n\ge2$ satisfies $|a_n|\le\frac12$, and only $a_1 = 1$
    is far away. Whatever $N$ Lim picks, Una can pick a large $n$ with
    $|a_n| < \frac14$, so $|a_n - \frac12| > \frac14$.

(c) Not all choices are equally good. Against $a = \frac12$, Una wins with
    any $\varepsilon\le\frac12$: she then picks a large $n$, where
    $a_n\approx 0$. If she chooses $\varepsilon > \frac12$, Lim can win by
    taking $N$ with $\frac1N < \varepsilon - \frac12$, because then every
    $n\ge N$ has $|a_n - \frac12|\le\frac12 + \frac1n < \varepsilon$. Advice: choose $\varepsilon$ smaller than
    the distance between Lim's $a$ and the true limit $0$.

(d) $a = 0$, the actual limit. Then, whatever $\varepsilon$ Una picks, Lim
    chooses $N > 1/\varepsilon$, and every $n\ge N$ has
    $|a_n| = \frac1n < \varepsilon$.

(e) (Play it.)

(f) Lim has a winning strategy exactly when the sequence converges: there is
    an $a$ such that for every $\varepsilon>0$ there is an $N$ with
    $|a_n - a| < \varepsilon$ for all $n\ge N$. Lim plays that $a$, and then
    the $N$ that goes with Una's $\varepsilon$.

(g) $a_n = (-1)^n$. Whatever $a$ Lim proposes, Una takes $\varepsilon = 1$.
    For every $n$, $|a_n - a|\ge1$ or $|a_{n+1} - a|\ge1$, because $a_n$ and
    $a_{n+1}$ are $2$ apart. So for any $N$, Una can find $n\ge N$ with
    $|a_n - a|\ge 1$.

(h) Una has a winning strategy exactly when the sequence does not converge:
    for every $a$ there is an $\varepsilon>0$ such that for every $N$ some
    $n\ge N$ has $|a_n - a|\ge\varepsilon$. This is the negation of (f).
:::
