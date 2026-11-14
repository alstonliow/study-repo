<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-03" status="draft"}
(a) A non-leap year has $365 = 52\cdot 7 + 1$ days, so the weekday moves on
    by one:
    $$(d+1)\bmod 7.$$

(b) With a leap day in between there are $366 = 52\cdot 7 + 2$ days:
    $$(d+2)\bmod 7.$$

(c) From one 29 February to the next there are $3\cdot 365 + 366 = 1461$
    days, and $1461 = 208\cdot 7 + 5$:
    $$(d+5)\bmod 7.$$
:::

::: {.solution for="prob-number-theory-08" status="draft"}
With letters identified with $\mathbb Z_{26}$ and key $k\in\mathbb Z_{26}$:
$$e(m_1\cdots m_n, k) = c_1\cdots c_n,\qquad c_i = (m_i + k)\bmod 26,$$
$$d(c_1\cdots c_n, k) = m_1\cdots m_n,\qquad m_i = (c_i - k)\bmod 26.$$
:::

::: {.solution for="prob-number-theory-10" status="draft"}
Write $n = \sum_{i=0}^{D-1} n_i 10^i$ with decimal digits $n_i$, so that
$\mathrm{ds}(n) = \sum_i n_i$.

(a) 1. $10\equiv 1\pmod 3$, so $10^i\equiv 1^i = 1\pmod 3$ for every $i$.

    2. Hence
       $$n = \sum_i n_i 10^i \equiv \sum_i n_i = \mathrm{ds}(n)\pmod 3.$$

    3. Two numbers that are congruent mod $3$ have the same remainder, so
       $n\bmod 3 = \mathrm{ds}(n)\bmod 3$.

(b) The same argument works because $10\equiv 1\pmod 9$ as well, since
    $9\mid 10-1$.

(c) 1. $10\equiv -1\pmod{11}$, so $10^i\equiv(-1)^i\pmod{11}$.

    2. Hence
       $$n\equiv\sum_i (-1)^i n_i = n_0 - n_1 + n_2 - \cdots = \mathrm{ads}(n)\pmod{11},$$
       with a $+$ sign on the rightmost digit $n_0$, as in the definition.

    3. So $n\bmod 11 = \mathrm{ads}(n)\bmod 11$.

(d) In binary, $n = \sum_i b_i 2^i$, and $2\equiv -1\pmod 3$, so
    $2^i\equiv(-1)^i$. Therefore
    $$n\equiv b_0 - b_1 + b_2 - b_3 + \cdots\pmod 3:$$
    take the alternating sum of the bits, starting with $+$ at the right-hand
    end, and reduce mod $3$. For example, $n = 13 = 1101_2$ gives
    $1 - 0 + 1 - 1 = 1$, and indeed $13\bmod 3 = 1$.
:::

::: {.solution for="prob-number-theory-11" status="draft"}
By Exercise 10(b), each number is congruent mod $9$ to its digit sum. For the
left-hand side, $92\equiv 9+2 = 11\equiv 2$ and $31\equiv 3+1 = 4$, so
$92\times 31\equiv 2\cdot 4 = 8\pmod 9$.

(a) $2847$: $2+8+4+7 = 21\equiv 3$. Since $3\ne 8$, the equation is
    **certainly wrong**.

(b) $2852$: $2+8+5+2 = 17\equiv 8$. The remainders agree, so the check
    finds no error. (The equation is in fact correct.)

(c) $2861$: $2+8+6+1 = 17\equiv 8$. The remainders agree, but the equation
    is wrong: $2861 - 2852 = 9$. The check cannot detect errors that are a
    multiple of $9$, such as swapped digits or this kind of slip.

(d) $2718281828$ has digit sum $47\equiv 2$, and $3141592653$ has digit sum
    $39\equiv 3$, so the left side is $\equiv 6$. The right side has digit
    sum $91\equiv 1$. Since $1\ne 6$, the product is **certainly wrong**.
    (The correct product ends in $\dots 9684$.)

In general: if the remainders differ, the equation is false; if they agree,
the equation may or may not be true.
:::

::: {.solution for="prob-number-theory-15" status="draft"}
(a) Encryption must be invertible, so $m\mapsto km\bmod 26$ must be a
    bijection on $\mathbb Z_{26}$. This holds exactly when $k$ has a
    multiplicative inverse mod $26$, that is, when $\gcd(k,26) = 1$. The
    keyspace is
    $$K = \{k\in\mathbb Z_{26} : \gcd(k,26) = 1\} = \{1,3,5,7,9,11,15,17,19,21,23,25\},$$
    which has $\varphi(26) = 12$ keys.

    For example, $k = 2$ fails: $\mathtt a$ ($0$) and $\mathtt n$ ($13$)
    both encrypt to $0$.

(b) Let $k^{-1}$ be the inverse of $k$ in $\mathbb Z_{26}$. Then
    $$m_i = k^{-1}c_i\bmod 26.$$

(c) For an alphabet of size $n$, identify the letters with $\mathbb Z_n$.

    - Keyspace: $K = \{k\in\mathbb Z_n : \gcd(k,n) = 1\}$, with $\varphi(n)$ keys.
    - Encryption: $c_i = k\,m_i\bmod n$.
    - Decryption: $m_i = k^{-1}c_i\bmod n$, where $k^{-1}$ is the inverse of
      $k$ mod $n$ (found with the Extended Euclidean Algorithm).
:::
