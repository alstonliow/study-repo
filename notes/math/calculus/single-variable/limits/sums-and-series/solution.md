<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sequences-13"}
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

::: {.solution for="prob-sequences-14"}
(a) For $n\ge1$, $\frac1{2n}\le\frac12$, so
    $H_n\le\log n + \gamma + \frac12\le\log n + 2$, since $\gamma\approx 0.577$.
    For $n\ge 8$ we have $\log n\ge 2$, so $H_n\le 2\log n$. Hence
    $H_n = O(\log n)$, with $c = 2$ and $N = 8$.

(b) $$\frac n1 + \frac n2 + \cdots + \frac nn = n\,H_n\le 2n\log n\quad(n\ge8),$$
    so the sum is $O(n\log n)$.
:::

::: {.solution for="prob-sequences-15"}
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

<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-7-q1" status="draft"}
For $x\ne1$,
$$\sum_{i=0}^ni^2x^i=\frac{x(1+x)-x^{n+1}\bigl((n+1)^2-(2n^2+2n-1)x+n^2x^2\bigr)}{(1-x)^3},$$
and for $x=1$ the sum is $\frac{n(n+1)(2n+1)}6$.

1. Start from $\sum_{i=0}^nx^i=\frac{1-x^{n+1}}{1-x}$ and apply the operator $x\frac d{dx}$, which turns $\sum c_ix^i$ into $\sum ic_ix^i$.

2. Once: $\sum_{i=0}^nix^i=\frac{x-(n+1)x^{n+1}+nx^{n+2}}{(1-x)^2}$.

3. Twice, after simplifying, gives the formula above. One can check it for small $n$; for example $n=1$ gives $\frac{x(1+x)-x^2(4-3x+x^2)}{(1-x)^3}=\frac{x(1-x)^3}{(1-x)^3}=x$.
:::

::: {.solution for="prob-mit6042f10-7-q2" status="draft"}
(a) $\prod_{k=1}^n2^{2k-1}=2^{\sum_{k=1}^n(2k-1)}=2^{n^2}$, since the first $n$ odd numbers sum to $n^2$.

(b) The double sum factors: $\Bigl(\sum_{i=0}^n3^i\Bigr)\Bigl(\sum_{j=0}^m3^j\Bigr)=\frac{(3^{n+1}-1)(3^{m+1}-1)}4$.

(c) $\sum_i\sum_j(i+j)=\sum_i\bigl(ni+\frac{n(n+1)}2\bigr)=n\cdot\frac{n(n+1)}2+n\cdot\frac{n(n+1)}2=n^2(n+1)$.

(d) $\Bigl(\sum_{i=1}^n2^i\Bigr)\Bigl(\sum_{j=1}^n3^j\Bigr)=(2^{n+1}-2)\cdot\frac{3^{n+1}-3}2=(2^n-1)(3^{n+1}-3)$.
:::
