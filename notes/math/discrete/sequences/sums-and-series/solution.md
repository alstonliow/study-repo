<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sequences-13" status="draft"}
(a) $\underbrace{99\cdots9}_{n} = 9 + 90 + 900 + \cdots + 9\cdot10^{n-1}$, a
    geometric series with $a = 9$, $r = 10$ and $n$ terms. The formula gives
    $$S_n = a\,\frac{r^n - 1}{r - 1} = 9\cdot\frac{10^n - 1}9 = 10^n - 1,$$
    which is correct: for example, $999 = 10^3 - 1$.

(b) $0.999\ldots = \frac9{10} + \frac9{100} + \cdots$, an infinite geometric
    series with $a = \frac9{10}$ and $r = \frac1{10}$. Since $|r|<1$, it
    converges to
    $$\frac a{1-r} = \frac{9/10}{9/10} = 1.$$
    So $0.999\ldots = 1$: it is another decimal expansion of the same number.
:::

::: {.solution for="prob-sequences-14" status="draft"}
(a) For $n\ge1$, $\frac1{2n}\le\frac12$, so
    $H_n\le\log n + \gamma + \frac12\le\log n + 2$, since $\gamma\approx 0.577$.
    For $n\ge 8$ we have $\log n\ge 2$, so $H_n\le 2\log n$. Hence
    $H_n = O(\log n)$, with $c = 2$ and $N = 8$.

(b) $$\frac n1 + \frac n2 + \cdots + \frac nn = n\,H_n\le 2n\log n\quad(n\ge8),$$
    so the sum is $O(n\log n)$.
:::

::: {.solution for="prob-sequences-15" status="draft"}
(a) By Exercise 5 and then (6.47),
    $$g_n\le n\log n - n + H_n\le n\log n - n + \log n + \gamma + \frac1{2n}\le n\log n - n + \log n + c,$$
    with $c = \gamma + \frac12$.

(b) Drop the $-n$. For $n\ge3$, both $\log n\le n\log n$ and
    $c\le n\log n$ hold, since $c = \gamma + \frac12\approx 1.08$ and
    $3\log 3\approx 3.3$. So $g_n\le 3n\log n$ for $n\ge3$, and
    $g_n = O(n\log n)$.

(c) $e^x$ is increasing, so exponentiating (a) gives
    $$e^{g_n}\le e^{n\log n}\,e^{-n}\,e^{\log n}\,e^c = n^n e^{-n}\,n\,e^c = \Bigl(\frac ne\Bigr)^n n\,e^c.$$

(d) $$e^{g_n} = e^{\sum_{i=1}^n\log i} = \prod_{i=1}^n e^{\log i} = \prod_{i=1}^n i = n!.$$

(e) By (c) and (d), $n!\le e^c\bigl(\frac ne\bigr)^n n$ for all $n\ge1$, so
    $$n! = O\Bigl(\Bigl(\frac ne\Bigr)^n n\Bigr)$$
    with constant $e^c$ and $N = 1$.
:::
