::: {.problem #prob-cs70-10-q2 origin="external" source="cs70-10.6-q2"}
Using (3) and the boundary conditions $D_1 = 0$ and $D_2 = 1$, derive (4). [Hint: For $n \ge 2$, define $Q_n = D_n - nD_{n-1}$ and obtain a recursion for $Q_n$.]

*Note (these notes):* (3) is the recurrence $D_n=(n-1)(D_{n-1}+D_{n-2})$ (@prp-derangement-recurrence) and (4) is the formula $D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}$ (@thm-derangement-count).
:::
