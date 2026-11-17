<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-11" status="draft"}
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
