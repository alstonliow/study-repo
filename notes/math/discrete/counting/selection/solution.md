<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-counting-02" status="draft"}
(a) Each filled ballot is an ordering of the $n$ candidates (the candidate
    numbered $1$, then $2$, and so on), so there are $n!$ ways.

(b) Choose which candidate gets $1$, then $2$, …, then $12$, all different.
    This is ordered selection without replacement:
    $$N(N-1)\cdots(N-11) = \frac{N!}{(N-12)!}\qquad(N\ge 12).$$
:::

::: {.solution for="prob-counting-10" status="draft"}
(a) $10^5 = 100{,}000$.

(b) First digit nonzero: $9\cdot10^4 = 90{,}000$.

(c) $10$, one for each digit.

(d) $10\cdot9\cdot8\cdot7\cdot6 = 30{,}240$.

(e) The first digit is free and each later digit avoids its predecessor:
    $10\cdot9^4 = 65{,}610$.

(f) Choose a set of $5$ distinct digits; its order is forced:
    $\binom{10}5 = 252$.

(g) Choose a multiset of $5$ digits (stars and bars):
    $\binom{10+5-1}5 = \binom{14}5 = 2{,}002$.

(h) Nondecreasing or nonincreasing. By symmetry, $2{,}002$ of each. Both
    happen only for the $10$ constant strings, so
    $2{,}002 + 2{,}002 - 10 = 3{,}994$.

(i) Let the common difference be $d$. Then $d=0$ gives $10$ strings. For
    $d>0$ we need first digit $a$ with $a+4d\le 9$: $d=1$ gives $6$ and
    $d=2$ gives $2$. Negative $d$ gives the reverses, another $8$. In total
    $10 + 8 + 8 = 26$.

(j) A ratio $r\ne1$ with nonzero terms cannot work: $r = 2$ already needs
    last/first $= 16$, $r = \tfrac12$ the reverse, and other ratios are
    worse or give non-integers. So only the $10$ constant strings are
    geometric. (If ratio $0$ is also allowed, the $9$ strings $a0000$ with
    $a\ne0$ are added, giving $19$.)

(k) The digit sum is a multiple of $9$ exactly when the number the string
    represents is (Exercise 7.10). Leading zeros allowed, these numbers are
    $0, 9, 18, \dots, 99{,}999$:
    $$1 + \frac{99{,}999}{9} = 11{,}112.$$

(l) Each position excludes exactly one digit: $9^5 = 59{,}049$.

(m) Let $N_k$ be the number of strings of distinct digits with a given set
    of $k$ positions fixed to their own digit: $N_k = (10-k)!/5!$, i.e.
    $9\cdot8\cdot7\cdot6$, $8\cdot7\cdot6$, $7\cdot6$, $6$, $1$ for $k=1,\dots,5$.
    By inclusion–exclusion,
    $$30{,}240 - 5\cdot3{,}024 + 10\cdot336 - 10\cdot42 + 5\cdot6 - 1 = 18{,}089.$$
:::
