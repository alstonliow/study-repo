<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-04"}
"The last $31$ bits" of a number is its remainder on division by $2^{31}$:
$$\mathrm{LCG}(x) = (1103515245\,x + 12345)\bmod 2^{31}.$$
:::

::: {.solution for="prob-number-theory-06"}
$$\forall n\in\mathbb N:\ \Bigl(\mathrm{Leap}(n)\leftrightarrow\bigl((4\mid n\wedge\neg(100\mid n))\vee 400\mid n\bigr)\Bigr).$$

The case "multiple of $400$" needs its own disjunct, because such years are
also multiples of $100$.
:::

::: {.solution for="prob-number-theory-07"}
1. *Odd case.* Let $n$ be odd, so $n = 2k+1$ for some integer $k$.

2. Then
   $$n^2 = 4k^2 + 4k + 1 = 2(2k^2+2k) + 1,$$
   and $2k^2+2k$ is an integer. So $n^2$ is odd.

3. *Even case.* Let $n$ be even, so $n = 2k$ for some integer $k$.

4. Then $n^2 = 4k^2 = 2(2k^2)$, so $n^2$ is even.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-1-q5" status="draft"}
(a)

1. Divide $p$ by $3$: $p=3q+r$ with $r\in\{0,1,2\}$.

2. If $r=0$, then $3\mid p$; since $p$ is prime, $p=3$, contradicting $p>3$.

3. So $p=3q+1$ (take $k=q$) or $p=3q+2=3(q+1)-1$ (take $k=q+1$).

(b)

1. $5$ is in two pairs: $(3,5)$ and $(5,7)$.

2. Suppose a prime $p$ is in two different pairs. Its partners are $p-2$ and $p+2$, so $p-2$, $p$, $p+2$ are all prime.

3. If $p\le3$, then $p-2\le1$ is not prime. So $p>3$.

4. If $p=3k+1$, then $p+2=3(k+1)$ is divisible by $3$ and larger than $3$, so not prime. If $p=3k-1$, then $p-2=3(k-1)$ is divisible by $3$, so it is prime only if $p-2=3$, that is, $p=5$.

5. By part (a) these are the only cases, so $p=5$.
:::
