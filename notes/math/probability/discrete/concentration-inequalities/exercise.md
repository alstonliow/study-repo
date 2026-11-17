::: {.problem #prob-cs70hw-12-q3 origin="external" source="cs70hw-12-q3"}
**Probabilistic Bounds.** A random variable $X$ has variance $\mathrm{Var}(X) = 9$ and expectation $E[X] = 2$. Furthermore, the value of $X$ is never greater than 10. Given this information, provide either a proof or a counterexample for the following statements.

(a) $E[X^2] = 13$.

(b) $P[X = 2] > 0$.

(c) $P[X \ge 2] = P[X \le 2]$.

(d) $P[X \le 1] \le 8/9$.

(e) $P[X \ge 6] \le 9/16$.
:::

::: {.problem #prob-cs70hw-12-q4 origin="external" source="cs70hw-12-q4"}
**Subset Card Game.** Jonathan and Yiming are playing a card game. Jonathan has $k > 2$ cards, and each card has a real number written on it. Jonathan tells Yiming (truthfully), that the sum of the card values is 0, and that the sum of squares of the values on the cards is 1. Specifically, if the card values are $c_1, c_2, \ldots, c_k$, then we have $\sum_{i=1}^k c_i = 0$ and $\sum_{i=1}^k c_i^2 = 1$. Jonathan and Yiming also agree on a positive target value of $\alpha$.

The cards are then going to be dealt randomly in the following fashion: for each card in the deck, a fair coin is flipped. If the coin lands heads, then the card goes to Yiming, and if the coin lands tails, the card goes to Jonathan. Note that it is possible for either player to end up with no cards/all the cards.

A player wins the game if the sum of the card values in their hand is at least $\alpha$, otherwise it is a tie.

(a) Prove that the probability that Yiming wins is at most $\frac{1}{8\alpha^2}$.

(b) Find a deck of $k$ cards and target value $\alpha$ where the probability that Yiming wins is exactly $\frac{1}{8\alpha^2}$.
:::

::: {.problem #prob-cs70hw-12-q5 origin="external" source="cs70hw-12-q5"}
**Just One Tail, Please.** Let $X$ be some random variable with finite mean and variance which is not necessarily non-negative. The extended version of Markov's Inequality states that for a non-negative function $\varphi(x)$ which is monotonically increasing for $x > 0$ and some constant $\alpha > 0$,
$$P(X \ge \alpha) \le \frac{E[\varphi(X)]}{\varphi(\alpha)}$$
Suppose $E[X] = 0$, $\mathrm{Var}(X) = \sigma^2 < \infty$, and $\alpha > 0$.

(a) Use the extended version of Markov's Inequality stated above with $\varphi(x) = (x + c)^2$, where $c$ is some positive constant, to show that:
$$P(X \ge \alpha) \le \frac{\sigma^2 + c^2}{(\alpha + c)^2}$$

(b) Note that the above bound applies for all positive $c$, so we can choose a value of $c$ to minimize the expression, yielding the best possible bound. Find the value for $c$ which will minimize the RHS expression (you may assume that the expression has a unique minimum). Plug in the minimizing value of $c$ to prove the following bound:
$$P(X \ge \alpha) \le \frac{\sigma^2}{\alpha^2 + \sigma^2}.$$

(c) Recall that Chebyshev's inequality provides a two-sided bound. That is, it provides a bound on $P(|X - E[X]| \ge \alpha) = P(X \ge E[X] + \alpha) + P(X \le E[X] - \alpha)$. If we only wanted to bound the probability of one of the tails, e.g. if we wanted to bound $P(X \ge E[X] + \alpha)$, it is tempting to just divide the bound we get from Chebyshev's by two. Why is this not always correct in general? Provide an example of a random variable $X$ (does not have to be zero-mean) and a constant $\alpha$ such that using this method (dividing by two to bound one tail) is not correct, that is, $P(X \ge E[X] + \alpha) > \frac{\mathrm{Var}(X)}{2\alpha^2}$ or $P(X \le E[X] - \alpha) > \frac{\mathrm{Var}(X)}{2\alpha^2}$.

Now we see the use of the bound proven in part (b) - it allows us to bound just one tail while still taking variance into account, and does not require us to assume any property of the random variable. Note that the bound is also always guaranteed to be less than 1 (and therefore at least somewhat useful), unlike Markov's and Chebyshev's inequality!

(d) Let's try out our new bound on a simple example. Suppose $X$ is a positively-valued random variable with $E[X] = 3$ and $\mathrm{Var}(X) = 2$. What bound would Markov's inequality give for $P[X \ge 5]$? What bound would Chebyshev's inequality give for $P[X \ge 5]$? What about for the bound we proved in part (b)? (Note: Recall that the bound from part (b) only applies for zero-mean random variables.)
:::
