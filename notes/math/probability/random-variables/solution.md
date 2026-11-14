<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-01" status="draft"}
Count the $36$ equally likely pairs $(x,y)$ by $|x-y|$:

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\Pr(\lvert X-Y\rvert = k)$ | $\frac6{36}$ | $\frac{10}{36}$ | $\frac8{36}$ | $\frac6{36}$ | $\frac4{36}$ | $\frac2{36}$ |

For $k\ge1$ there are $6-k$ pairs with $x - y = k$ and as many with
$y - x = k$, giving $2(6-k)$.
:::

::: {.solution for="prob-probability-2-02" status="draft"}
$X\oplus Y$ is uniform on $\{0,1\}$, whatever the distribution of $Y$.

1. Let $q = \Pr(Y = 0)$. $X\oplus Y = 0$ exactly when $X = Y$. By
   independence,
   $$\Pr(X\oplus Y = 0) = \Pr(X=0)\Pr(Y=0) + \Pr(X=1)\Pr(Y=1) = \tfrac12 q + \tfrac12(1-q) = \tfrac12.$$

2. So $\Pr(X\oplus Y = 1) = \frac12$ too.

3. The same calculation conditional on $Y = y$ gives
   $\Pr(X\oplus Y = 0\mid Y = y) = \frac12$, so $X\oplus Y$ is even
   independent of $Y$. This is why a one-time pad hides the message
   completely.
:::

::: {.solution for="prob-probability-2-03" status="draft"}
Each of the four strings has probability $\frac14$. Note that in each string
$z = x\oplus y$.

(a) Each bit is $0$ in exactly two of the four strings, so each of $X,Y,Z$
    is uniform on $\{0,1\}$.

    1. The pairs $(x,y)$ in the four strings are $00, 01, 10, 11$: each
       occurs once. So $\Pr(X=a, Y=b) = \frac14 = \Pr(X=a)\Pr(Y=b)$ for all
       $a,b$, and $X$, $Y$ are independent.

    2. The same holds for the pairs $(x,z)$: $00, 01, 11, 10$.

    3. And for the pairs $(y,z)$: $00, 11, 01, 10$.

(b) $Z$ is not independent of $(X,Y)$, because $Z$ is determined by them:
    $$\Pr(Z = 0\mid X=0,Y=1) = 0 \ne \tfrac12 = \Pr(Z = 0).$$

(c) Likewise $Y = X\oplus Z$ and $X = Y\oplus Z$, so each bit is determined
    by the other two. Neither $Y$ nor $X$ is independent of the other two.
    The three variables are pairwise independent but not mutually
    independent.
:::
