<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-13" status="draft"}
1. Run the Euclidean algorithm on $99$ and $86$:
   $$\begin{aligned}
   99 &= 1\cdot 86 + 13\\
   86 &= 6\cdot 13 + 8\\
   13 &= 1\cdot 8 + 5\\
   8 &= 1\cdot 5 + 3\\
   5 &= 1\cdot 3 + 2\\
   3 &= 1\cdot 2 + 1\\
   2 &= 2\cdot 1
   \end{aligned}$$
   The last nonzero remainder is $1$, so $\gcd(99,86) = 1$: they are coprime.

2. Express each remainder as a combination of $99$ and $86$, working down:
   $$\begin{aligned}
   13 &= 99 - 86\\
   8 &= 86 - 6\cdot 13 = 7\cdot 86 - 6\cdot 99\\
   5 &= 13 - 8 = 7\cdot 99 - 8\cdot 86\\
   3 &= 8 - 5 = 15\cdot 86 - 13\cdot 99\\
   2 &= 5 - 3 = 20\cdot 99 - 23\cdot 86\\
   1 &= 3 - 2 = 38\cdot 86 - 33\cdot 99
   \end{aligned}$$

3. So $1 = 38\cdot 86 - 33\cdot 99$. Reducing mod $99$ gives
   $38\cdot 86\equiv 1$, so the inverse of $86$ in $\mathbb Z_{99}$ is
   $38$. Check: $38\cdot 86 = 3268 = 33\cdot 99 + 1$.
:::
