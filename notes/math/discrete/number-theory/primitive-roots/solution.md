<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-17" status="draft"}
(a) $k = \varphi(11) = 10$. By definition, a primitive root $a$ of $11$ has
    $a^k\not\equiv 1$ for $1\le k<10$, and $a^{10}\equiv 1$ by Fermat's
    little theorem.

(b) Multiplying by $2$ and reducing mod $11$ each time:

    | $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    |---|---|---|---|---|---|---|---|---|---|---|
    | $2^i\bmod 11$ | 2 | 4 | 8 | 5 | 10 | 9 | 7 | 3 | 6 | 1 |

    The first power equal to $1$ is $2^{10}$, so $2$ is a primitive root of
    $11$. (All of $1,\dots,10$ appear.)

(c) $\varphi(11) = 10 = 2\cdot 5$. The exponents in $\{1,\dots,10\}$ coprime
    to $10$ are $i = 1, 3, 7, 9$.

(d) If $g$ is a primitive root, then $g^i$ is a primitive root exactly when
    $\gcd(i,\varphi(n)) = 1$. From the table, the primitive roots of $11$ are
    $$2^1 = 2,\quad 2^3 = 8,\quad 2^7 = 7,\quad 2^9 = 6,$$
    that is, $2, 6, 7, 8$.
:::
