<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-2-q2" status="draft"}
By the template of @sec-math-discrete-proof-well-ordering-proofs:

1. Let $C$ be the set of $n\ge0$ for which (1) fails, and suppose $C\ne\emptyset$, with least element $m$.

2. $m\ne0$, since both sides are $0$ for $n=0$. So $m-1\ge0$ satisfies (1): $\sum_{i=0}^{m-1}i^3=\frac{(m-1)^2m^2}4$.

3. Then $\sum_{i=0}^mi^3=\frac{(m-1)^2m^2}4+m^3=\frac{m^2\bigl((m-1)^2+4m\bigr)}4=\frac{m^2(m+1)^2}4$, so (1) holds for $m$, a contradiction.
:::
