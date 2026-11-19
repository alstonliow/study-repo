<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-3-q2" status="draft"}
(a) Integrating the joint density $\lambda e^{-\lambda x}\mu e^{-\mu y}$ over $x<y$:
$$P(X<Y)=\int_0^\infty\lambda e^{-\lambda x}e^{-\mu x}\,dx=\frac{\lambda}{\lambda+\mu}.$$

(b) $P(\min_kX_k>t)=\prod_kP(X_k>t)=e^{-(\sum_j\lambda_j)t}$, the tail of an $\text{Exponential}(\sum_j\lambda_j)$ variable.

(c) Let $Y=\min_{k\ne i}X_k$, which is $\text{Exponential}(\sum_{j\ne i}\lambda_j)$ by (b) and independent of $X_i$. Ties have probability $0$, so by (a) $P(X_i=\min_kX_k)=P(X_i<Y)=\lambda_i/\sum_j\lambda_j$. (This is @prp-min-of-exponentials.)
:::
