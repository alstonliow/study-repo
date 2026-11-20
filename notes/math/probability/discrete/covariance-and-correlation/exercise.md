::: {.problem #prob-cs70hw-12-q1 origin="external" source="cs70hw-12-q1"}
**Graph.** Consider a random graph (undirected, no multi-edges, no self-loops) on $n$ nodes, where each possible edge exists independently with probability $p$. Let $X$ be the number of isolated nodes (nodes with degree 0).

(a) What is $\mathrm{Var}(X)$?
:::

::: {.problem #prob-cs70hw-12-q2 origin="external" source="cs70hw-12-q2"}
**Whitening.** Let $X$ and $Y$ be two random variables, with $\mathrm{Var}(X) > 0$, $\mathrm{Var}(Y) > 0$. Show that it is possible to construct $\tilde{X} = aX + bY$ and $\tilde{Y} = cX + dY$, where $a, b, c, d$ are scalars to be chosen subject to the constraint $ad - bc \ne 0$, such that $\mathrm{cov}(\tilde{X}, \tilde{Y}) = 0$.

You may find it unnecessary to transform $Y$, that is, you only need to solve for $a, b$ to get $\mathrm{cov}(\tilde{X}, Y) = 0$.
:::

::: {.problem #prob-mit6041f10-4-q5 origin="external" source="mit6041f10-4-q5"}
Consider a sequence of independent tosses of a biased coin at times $t = 0, 1, 2, \ldots$. On each toss, the probability of a 'head' is $p$, and the probability of a 'tail' is $1 - p$. A reward of one unit is given each time that a 'tail' follows immediately after a 'head.' Let $R$ be the total reward paid in times $1, 2, \ldots, n$. Find $\mathbf{E}[R]$ and $\mathrm{var}(R)$.
:::

::: {.problem #prob-mit6041f10-6-q3 origin="external" source="mit6041f10-6-q3"}
Consider $n$ independent tosses of a $k$-sided fair die. Let $X_i$ be the number of tosses that result in $i$.

(a) Are $X_1$ and $X_2$ uncorrelated, positively correlated, or negatively correlated? Give a one-line justification.
(b) Compute the covariance $\mathrm{cov}(X_1, X_2)$ of $X_1$ and $X_2$.
:::

::: {.problem #prob-mit1805s22-5-q3 origin="external" source="mit1805s22-5-q3"}
Correlation
Suppose $X$ and $Y$ are random variables with
$$P(X = 1) = P(X = -1) = \frac12; \qquad P(Y = 1) = P(Y = -1) = \frac12.$$
Let $c = P(X = 1 \text{ and } Y = 1)$.

(a) Determine the joint distribution of $X$ and $Y$, $\mathrm{Cov}(X, Y)$, and $\mathrm{Cor}(X, Y)$.

(b) For what value(s) of $c$ are $X$ and $Y$ independent? For what value(s) of $c$ are $X$ and $Y$ 100% correlated?
:::

::: {.problem #prob-mit1805s22-5-q5 origin="external" source="mit1805s22-5-q5"}
Overlapping sums
Suppose $X_1, X_2, \ldots$ are independent exponential(2) random variables. Suppose also that $X$ is the sum of the first $n$ and $Y$ is the sum of $X_{n-7}$ to $X_{2n-8}$. Compute $\mathrm{Cov}(X, Y)$ and $\mathrm{Cor}(X, Y)$. You should assume that $n \geq 8$.

Hints: The variance of an exponential($\lambda$) random variable is $1/\lambda^2$. Use the linearity rules for covariance. What is the size of the overlap?
:::
