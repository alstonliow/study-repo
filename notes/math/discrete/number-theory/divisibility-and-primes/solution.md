<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-01" status="draft"}
(a) $d$ divides $n$ when $n$ is an integer multiple of $d$:
    $$\exists k\in\mathbb Z:\ n = kd.$$

(b) $n$ is prime when $n\ge 2$ and its only positive divisors are $1$ and $n$:
    $$2\le n\ \wedge\ \forall d\in\mathbb N:\ \bigl(d\mid n \to (d = 1 \vee d = n)\bigr).$$

(c) $d$ is a common divisor, and every common divisor is at most $d$:
    $$d\mid m\ \wedge\ d\mid n\ \wedge\ \forall c\in\mathbb Z:\ \bigl((c\mid m\wedge c\mid n)\to c\le d\bigr).$$
:::

::: {.solution for="prob-number-theory-02" status="draft"}
Write $s(n)$ for the sum of the proper divisors of $n$ (the positive divisors
other than $n$).

(a) Computing $s(n)$ for $n = 1,\dots,28$:

    | $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | $s(n)$ | 0 | 1 | 1 | 3 | 1 | **6** | 1 | 7 | 4 | 8 | 1 | 16 | 1 | 10 |

    | $n$ | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | $s(n)$ | 9 | 15 | 1 | 21 | 1 | 22 | 11 | 14 | 1 | 36 | 6 | 16 | 13 | **28** |

    The only $n\le 28$ with $s(n) = n$ are $6 = 1+2+3$ and
    $28 = 1+2+4+7+14$.

(b) $496 = 2^4\cdot 31$, so its proper divisors are
    $1, 2, 4, 8, 16, 31, 62, 124, 248$, and
    $$1+2+4+8+16 + 31+62+124+248 = 31 + 465 = 496.$$
:::

::: {.solution for="prob-number-theory-05" status="draft"}
(a) Every prime with two or more digits is odd and not a multiple of $5$, so
    its last digit is $1$, $3$, $7$ or $9$. Also, the first digit of a
    five-digit number is not $0$.

    So the digits $1,3,7,9$ are more likely to appear in the answer than the
    others, and $0$ is the least likely, since it is excluded from two
    positions. A first guess should use $1,3,7,9$ and avoid $0$.

(b) Primes thin out as numbers grow, so a five-digit prime is more likely to
    start with a small digit. A good first guess therefore uses $1,3,7,9$
    together with one more small nonzero digit, namely $2$.

    The digits $1,2,3,7,9$ in increasing order already form a prime:
    $12379$ is prime (no prime up to $\sqrt{12379} < 112$ divides it).
    This is easy to remember and puts the likely digit $1$ first.

(c) This part is an experiment. Whatever a chatbot suggests, test it before
    using it: check the last digit, the digit sum (for $3$), and trial
    division by the primes up to $\sqrt n\le 316$. Language models often
    propose numbers that look prime but are not, so expect to need several
    attempts.
:::

::: {.solution for="prob-number-theory-09" status="draft"}
Write $n = 10^k q + r$, where $r$ is the number formed by the last $k$
digits of $n$, so $0\le r < 10^k$.

1. **Key fact.** If $d\mid 10^k$, then $d\mid 10^kq$, so
   $n\equiv r \pmod d$. Hence $d\mid n$ if and only if $d\mid r$.

(a) $4\mid 100 = 10^2$. Apply the key fact with $k=2$.

(b) $8\mid 1000 = 10^3$. Apply the key fact with $k=3$.

(c) $25\mid 100 = 10^2$. Apply the key fact with $k=2$.

(d) $2^k\mid 10^k = 2^k5^k$. So $2^k\mid n$ if and only if $2^k$ divides
    the number formed by the last $k$ digits of $n$.

(e) Exactly the divisors of powers of $10$, that is, the numbers
    $d = 2^a5^b$ with $a,b\ge 0$.

    1. If $d = 2^a5^b$, let $k = \max(a,b)$. Then $d\mid 10^k$, and the
       key fact shows that the last $k$ digits decide divisibility.

    2. Conversely, suppose the last $k$ digits always decide divisibility by
       $d$. The numbers $0$ and $10^k$ have the same last $k$ digits (all
       zero), and $d\mid 0$. So $d\mid 10^k$, and hence $d$ has no prime
       factors other than $2$ and $5$.
:::
