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
