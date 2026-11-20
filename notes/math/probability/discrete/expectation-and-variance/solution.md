<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-05" status="draft"}
- **Expectation:** $E(W) = 0\cdot\frac12 + 1\cdot\frac13 + 2\cdot\frac16 = \frac23$.
- **Median:** $m$ is a median when $\Pr(W\le m)\ge\frac12$ and
  $\Pr(W\ge m)\ge\frac12$. Both $m = 0$ ($\Pr(W\le0) = \frac12$,
  $\Pr(W\ge0) = 1$) and $m = 1$ ($\Pr(W\le1) = \frac56$,
  $\Pr(W\ge1) = \frac12$) qualify, as does every $m$ in between.
- **Mode:** $0$, the value with the largest probability.
- **Variance:** $E(W^2) = 0 + \frac13 + 4\cdot\frac16 = 1$, so
  $$\mathrm{Var}(W) = E(W^2) - E(W)^2 = 1 - \tfrac49 = \tfrac59.$$
- **Standard deviation:** $\sqrt{5}/3\approx 0.745$.
:::

::: {.solution for="prob-probability-2-06" status="draft"}
1. For one die $X$: $E(X) = \frac72$ and $E(X^2) = \frac{91}6$, so
   $\mathrm{Var}(X) = \frac{91}6 - \frac{49}4 = \frac{35}{12}$.

2. The dice are independent, so the sum $S$ has
   $$\mathrm{Var}(S) = 2\cdot\tfrac{35}{12} = \tfrac{35}6\approx 5.83,$$
   with standard deviation $\sigma\approx 2.415$ and mean $7$.

3. $|S-7|\ge 2\sigma\approx 4.83$ means $|S-7|\ge5$, so $S\in\{2,12\}$:
   $$\Pr(|S-7|\ge2\sigma) = \tfrac2{36} = \tfrac1{18}\approx 0.056.$$

4. Chebyshev's Inequality only guarantees
   $\Pr(|S-7|\ge2\sigma)\le\frac1{2^2} = \frac14$. The bound holds, but it is
   far from the true value, because it applies to every distribution.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-12-q1" status="draft"}
(a) You end with $2N$ or $0$, each with probability $\frac12$: $E=N$ and $\mathrm{Var}=E[X^2]-E[X]^2=\frac{(2N)^2}2-N^2=N^2$.

(b) One share of each of the $N$ stocks: $X=\sum_{i=1}^N2B_i$ with independent $B_i\sim\mathrm{Bernoulli}(\frac12)$. Then $E[X]=N$ and, by @thm-variance-of-an-independent-sum, $\mathrm{Var}(X)=N\cdot4\cdot\frac14=N$.

(c) Diversify: both strategies have the same expected value, but diversifying reduces the variance from $N^2$ to $N$ (and the chance of losing everything from $\frac12$ to $2^{-N}$).

(d) $E=\frac72$ and $\mathrm{Var}=\frac{91}6-\frac{49}4=\frac{35}{12}$.

(e) $E[X^3]=\frac{1+8+27+64+125+216}6=\frac{441}6=73.5$, $E[X^6]=\frac{1+64+729+4096+15625+46656}6=\frac{67171}6$, so $\mathrm{Var}(X^3)=\frac{67171}6-\Bigl(\frac{441}6\Bigr)^2=\frac{69515}{12}\approx5792.9$.
:::

::: {.solution for="prob-mit6006s20-0-q2" status="draft"}
(a) $X$ is the sum of three indicator variables, each with expectation $\frac12$, so $E[X]=\frac32$ by linearity.

(b) $Y=D_1D_2$ with independent dice, $E[D_i]=\frac72$, so $E[Y]=E[D_1]E[D_2]=\frac{49}4=12.25$ (@thm-expectation-of-product).

(c) By linearity, $E[X+Y]=\frac32+\frac{49}4=\frac{55}4=13.75$ (no independence of $X$ and $Y$ is needed).
:::

::: {.solution for="prob-mit6041f10-3-q3" status="draft"}
(a)

1. Write $\Pr(X\ge k)=\sum_{j\ge k}\Pr(X=j)$, so $\sum_{k\ge1}\Pr(X\ge k)=\sum_{k\ge1}\sum_{j\ge k}\Pr(X=j)$.

2. All terms are nonnegative, so the order of summation may be swapped. For fixed $j$ the index $k$ runs over $1,\dots,j$, giving $\sum_{j\ge1}j\Pr(X=j)$.

3. Adding the term $j=0$, which is $0$, this is $E[X]$.

(b) For $k\le a$, $\Pr(Y\ge k)=1$; for $a<k\le b$, $\Pr(Y\ge k)=\frac{b-k+1}{b-a+1}$; for $k>b$ it is $0$. Hence
$$E[Y]=a+\frac{1}{b-a+1}\sum_{k=a+1}^b(b-k+1)=a+\frac{(b-a)(b-a+1)/2}{b-a+1}=\frac{a+b}2.$$
:::

::: {.solution for="prob-mit1805s22-3-q3" status="draft"}
(a) A fair $n$-sided die has variance $\frac{n^2-1}{12}$. So $\mathrm{Var}(X)=\frac{15}{12}=\frac54$, $\sigma_X\approx1.118$, and $\mathrm{Var}(Y)=\frac{35}{12}$, $\sigma_Y\approx1.708$. By independence $\mathrm{Var}(Z)=\frac14\bigl(\frac54+\frac{35}{12}\bigr)=\frac{25}{24}$, so $\sigma_Z\approx1.021$.

(b) The $24$ pairs $(X,Y)$ are equally likely. Counting pairs with each average:

| $z$ | $1$ | $1.5$ | $2$ | $2.5$ | $3$ | $3.5$ | $4$ | $4.5$ | $5$ |
|---|---|---|---|---|---|---|---|---|---|
| $24\,p(z)$ | $1$ | $2$ | $3$ | $4$ | $4$ | $4$ | $3$ | $2$ | $1$ |
| $24\,F(z)$ | $1$ | $3$ | $6$ | $10$ | $14$ | $18$ | $21$ | $23$ | $24$ |

The pmf is a symmetric trapezoid of spikes about $z=3$; the cdf is a step function, constant between these points, jumping by $p(z)$ at each.

(c) Let $W$ be the winnings of one game. $X>Y$ happens for $(x,y)$ with $y<x$: $x=2,3,4$ give $1,2,3$ pairs, winning $4,6,8$ dollars; the other $18$ pairs lose $1$. So $E[W]=\frac{4+12+24-18}{24}=\frac{11}{12}$, and by linearity the expected total over $60$ games is $60\cdot\frac{11}{12}=55$ dollars, a gain.
:::
