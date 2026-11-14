<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-04" status="draft"}
"The last $31$ bits" of a number is its remainder on division by $2^{31}$:
$$\mathrm{LCG}(x) = (1103515245\,x + 12345)\bmod 2^{31}.$$
:::

::: {.solution for="prob-number-theory-06" status="draft"}
$$\forall n\in\mathbb N:\ \Bigl(\mathrm{Leap}(n)\leftrightarrow\bigl((4\mid n\wedge\neg(100\mid n))\vee 400\mid n\bigr)\Bigr).$$

The case "multiple of $400$" needs its own disjunct, because such years are
also multiples of $100$.
:::

::: {.solution for="prob-number-theory-07" status="draft"}
1. *Odd case.* Let $n$ be odd, so $n = 2k+1$ for some integer $k$.

2. Then
   $$n^2 = 4k^2 + 4k + 1 = 2(2k^2+2k) + 1,$$
   and $2k^2+2k$ is an integer. So $n^2$ is odd.

3. *Even case.* Let $n$ be even, so $n = 2k$ for some integer $k$.

4. Then $n^2 = 4k^2 = 2(2k^2)$, so $n^2$ is even.
:::
