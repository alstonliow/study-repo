<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-11"}
This is the coupon collector problem with $n = 365$ coupons.

1. When $i$ different birthdays have been seen, each new person has a new
   birthday with probability $\frac{365-i}{365}$. So the number of people
   until the next new birthday is geometric with mean $\frac{365}{365-i}$.

2. By linearity of expectation, the expected total is
   $$\sum_{i=0}^{364}\frac{365}{365-i} = 365\sum_{k=1}^{365}\frac1k = 365\,H_{365}\approx 365\cdot 6.4785\approx 2365.$$

3. So about $2{,}365$ people are expected, roughly $6.5$ times the number of
   days. Compare this with the birthday paradox, where $23$ people already
   make a repeat more likely than not.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-2-q5" status="draft"}
(a) $X\ge0$, so by Markov's inequality (@thm-markov-inequality) $P(X>2nH_n)\le\frac{nH_n}{2nH_n}=\frac12$.

(b) $X=\sum_{i=1}^{n}G_i$ with independent $G_i\sim\operatorname{Geom}(p_i)$, $p_i=\frac{n-i+1}{n}$. Then $\operatorname{var}(X)=\sum_i\frac{1-p_i}{p_i^2}\le\sum_{j=1}^{n}\frac{n^2}{j^2}\le\frac{\pi^2n^2}{6}$. By Chebyshev's inequality,
$$P(X>2nH_n)\le P(|X-nH_n|\ge nH_n)\le\frac{\pi^2n^2/6}{n^2H_n^2}\le\frac{\pi^2}{6(\ln n)^2}.$$

(c) Let $A_i$ be the event that coupon type $i$ is missing from the first $2nH_n$ boxes (round down; the bound only improves). Then $X>2nH_n$ implies some $A_i$, and
$$P(A_i)=\Bigl(1-\frac1n\Bigr)^{2nH_n}\le e^{-2H_n}\le e^{-2\ln n}=\frac1{n^2},$$
using $(1-1/n)^n\le1/e$. By the union bound, $P(X>2nH_n)\le n\cdot\frac1{n^2}=\frac1n$.
:::
