<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-14" status="draft"}
(a)

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $\varphi(n)$ | 1 | 1 | 2 | 2 | 4 | 2 | 6 | 4 | 6 | 4 |

| $n$ | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| $\varphi(n)$ | 10 | 4 | 12 | 6 | 8 | 8 | 16 | 6 | 18 | 8 |

For a prime $p$, $\varphi(p) = p-1$. The other values follow from
$\varphi(p^k) = p^k - p^{k-1}$ and $\varphi(mn) = \varphi(m)\varphi(n)$ for
coprime $m,n$; e.g. $\varphi(18) = \varphi(2)\varphi(9) = 1\cdot 6 = 6$.

(b) $a$ is a primitive root of $n$ when $\gcd(a,n)=1$ and the smallest
    $k\ge1$ with $a^k\equiv 1\pmod n$ is $k = \varphi(n)$. Some examples:

| $n$ | primitive roots in $\{1,\dots,n-1\}$ |
|---|---|
| 5 | 2, 3 |
| 7 | 3, 5 |
| 9 | 2, 5 |
| 10 | 3, 7 |
| 11 | 2, 6, 7, 8 |
| 13 | 2, 6, 7, 11 |
| 18 | 5, 11 |
| 8, 12 | none |

For example, $3$ is a primitive root of $7$: its powers mod $7$ are
$3, 2, 6, 4, 5, 1$, and $1$ first appears at the $6$th power. Mod $8$
every odd $a$ has $a^2\equiv1$, so nothing reaches order $\varphi(8)=4$.
:::
