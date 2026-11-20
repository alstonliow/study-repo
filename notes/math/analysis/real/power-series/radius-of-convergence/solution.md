<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-4-q7" status="draft"}
(i) $3/2$. The ratio of consecutive coefficients is $\frac{2n+4}{3n+4} \to \frac23$, so the radius is $\frac32$.

(ii) $2^{1/3}$. With $w = z^3$ the series is $\sum w^n/(n2^n)$, whose coefficient ratio $\frac{n}{2(n+1)} \to \frac12$, so it converges for $|w| < 2$ and diverges for $|w| > 2$. So the radius in $z$ is $2^{1/3}$.

(iii) $1/e$. The ratio of consecutive coefficients is $\frac{(n+1)^{n+1}}{(n+1)!}\cdot\frac{n!}{n^n} = \left(1 + \frac1n\right)^n \to e$.

(iv) $1$. $|c_n|^{1/n} = n^{1/\sqrt n} = e^{\log n/\sqrt n} \to e^0 = 1$, and the Cauchy–Hadamard formula gives radius $1$.
:::
