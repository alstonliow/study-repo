<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-01"}
Count the $36$ equally likely pairs $(x,y)$ by $|x-y|$:

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\Pr(\lvert X-Y\rvert = k)$ | $\frac6{36}$ | $\frac{10}{36}$ | $\frac8{36}$ | $\frac6{36}$ | $\frac4{36}$ | $\frac2{36}$ |

For $k\ge1$ there are $6-k$ pairs with $x - y = k$ and as many with
$y - x = k$, giving $2(6-k)$.
:::

::: {.solution for="prob-probability-2-02"}
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

::: {.solution for="prob-probability-2-03"}
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

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-11-q1" status="draft"}
(a) Sum the rows and columns (@def-joint-distribution): $\Pr(X=0,1,2)=\frac23,\frac19,\frac29$ and $\Pr(Y=0,1,2)=\frac49,\frac29,\frac13$.

(b) $E[X]=\frac19+2\cdot\frac29=\frac59$ and $E[Y]=\frac29+2\cdot\frac13=\frac89$.

(c) $E[X^2]=\frac19+4\cdot\frac29=1$, so $\mathrm{Var}(X)=1-\frac{25}{81}=\frac{56}{81}$. $E[Y^2]=\frac29+4\cdot\frac13=\frac{14}9$, so $\mathrm{Var}(Y)=\frac{14}9-\frac{64}{81}=\frac{62}{81}$.

(d) $E[I]=\Pr(X=1)=\frac19$, $E[J]=\Pr(Y=1)=\frac29$, and $E[IJ]=\Pr(X=1,Y=1)=\frac19$.

(e) $I_AI_B=I_{A\cap B}$, so $E[I_AI_B]=\Pr(A\cap B)$ (@prp-expectation-of-indicator).
:::

::: {.solution for="prob-cs70hw-11-q2" status="draft"}
(a) No. Condition (1) says $X_i=-X_j$ with probability $1$ for each pair. Then with probability $1$ all three of $X_1=-X_2$, $X_2=-X_3$, $X_1=-X_3$ hold (an intersection of three events of probability $1$). But the first two give $X_1=X_3$, which together with the third forces $X_1=-X_1$, impossible for values $\pm1$.

(b) Exactly the even $n$. The condition says $X_i=-X_{i-1}$ with probability $1$ around the cycle $1,2,\dots,n,1$. Going once around, $X_1=(-1)^nX_1$, which is impossible for odd $n$. For even $n$ take: with probability $\frac12$, $(X_1,\dots,X_n)=(1,-1,1,-1,\dots,1,-1)$, and with probability $\frac12$ the negative of this. Then each consecutive pair (including $X_n,X_1$) is $(1,-1)$ or $(-1,1)$ with probability $\frac12$ each, as required.
:::
