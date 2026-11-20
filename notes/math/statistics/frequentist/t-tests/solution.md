<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1805s22-4-q6" status="draft"}
(a) $P(\text{IQ}>160)=P(Z>4)=1-\Phi(4)\approx3.17\times10^{-5}$.

(b) Standardizing gives the same event $Z>4$, so again $\approx3.17\times10^{-5}$.

(c) Four standard deviations is $4\sqrt3\approx6.93$, and
$$P(T>4\sqrt3)=\int_{4\sqrt3}^\infty\frac2{\sqrt3\,\pi}\Bigl(1+\frac{x^2}3\Bigr)^{-2}dx\approx0.0031,$$
about $100$ times the normal value.

(d) Numerically:

| | $>20$ | $>40$ | $>200$ |
|---|---|---|---|
| normal, sd $\sqrt3$ | $\approx4\times10^{-31}$ | $\approx3\times10^{-118}$ | $\approx0$ |
| $t_3$ | $\approx1.4\times10^{-4}$ | $\approx1.7\times10^{-5}$ | $\approx1.4\times10^{-7}$ |

The normal tail decays like $e^{-x^2/6}$, the $t_3$ tail only like $x^{-3}$ (the density is of order $x^{-4}$). So with the same mean and standard deviation, extreme values are astronomically more likely under $t_3$: its tail is "fat".
:::
