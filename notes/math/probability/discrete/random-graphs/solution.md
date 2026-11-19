<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-10-q1" status="draft"}
The MLE is $\hat p=\frac{D}{n-1}\approx\frac Dn$.

1. Each edge adds $2$ to the total degree, so $D=\frac{2E}{n}$, where $E\sim\text{Bin}(\binom n2,p)$ is the number of edges (@def-erdos-renyi-graph). Observing $D$ is the same as observing $E=e$.
2. Approximating $E$ by $\text{Poisson}(\binom n2p)$, the log-likelihood is $-\binom n2p+e\ln p+\text{const}$, maximised where $-\binom n2+\frac ep=0$.
3. So $\hat p=\frac{e}{\binom n2}=\frac{nD/2}{n(n-1)/2}=\frac{D}{n-1}$. The exact binomial likelihood $p^e(1-p)^{\binom n2-e}$ gives the same maximiser.
:::

::: {.solution for="prob-eecs126d-2-q3" status="draft"}
The answer is $p$.

1. Condition on the set $F$ of friends of $i$, with $|F|=k\ge2$. A triangle at $i$ is a pair in $F$ that are friends with each other, so $T(i)$ counts the edges among $F$.
2. Those $\binom k2$ edges are independent of the edges at $i$ (@def-erdos-renyi-graph), so given $F$, $T(i)\sim\text{Bin}(\binom k2,p)$ and $E[C(i)\mid F]=p$.
3. This does not depend on $F$, so averaging over all $F$ with $|F|\ge2$ gives $E[C(i)\mid N(i)\ge2]=p$. (In $G(n,p)$ a friend of a friend is no more likely to be a friend than anyone else.)
:::
