<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-13-q1" status="draft"}
1. $\partial L/\partial p_i=-a_i^2/p_i^2-\lambda=0$ gives $p_i=a_i/\sqrt{-\lambda}$: each $p_i$ is proportional to $a_i$.

2. The constraint fixes the constant: $p_i=a_i/(a_1+\dots+a_n)$.

3. Then $V=\sum_ia_i^2\cdot\frac{a_1+\dots+a_n}{a_i}=(a_1+\dots+a_n)^2$.

4. It is the minimum: by Cauchy–Schwarz $(\sum a_i)^2=(\sum\frac{a_i}{\sqrt{p_i}}\sqrt{p_i})^2\le V\sum p_i=V$ for every admissible $\mathbf{p}$ (@thm-optimal-sampling-probabilities).
:::
