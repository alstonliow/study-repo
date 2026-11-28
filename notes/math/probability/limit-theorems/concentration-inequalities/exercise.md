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

::: {.problem #prob-mit6042f10-12-q4 origin="external" source="mit6042f10-12-q4"}
We have two coins: one is a fair coin and the other is a coin that produces heads with probability 3/4. One of the two coins is picked, and this coin is tossed $n$ times. Explain how to calculate the number of tosses to make us 95% confident which coin was chosen. You do not have to calculate the minimum value of $n$, though we'd be pleased if you did.
:::

::: {#prob-run-of-heads-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-simulation"}
Let $T$ be the number of tosses of a fair coin until $k$ heads in a row first appear. Write `mean_flips_until_run(k, trials, rng)`. It simulates $T$ independently `trials` times and returns the sample mean, an estimate of $E[T]$ (@thm-law-of-large-numbers). Draw each toss as `rng.random() < 0.5` (heads), where `rng` is a `random.Random`, so a fixed seed gives a fixed result.

The tests compare with the exact value $E[T]=2^{k+1}-2$ and allow five standard errors (@prp-sample-mean).

```{.python .starter}
import random


def mean_flips_until_run(k, trials, rng):
    """Monte Carlo estimate of the expected number of fair coin flips until
    k heads in a row first appear. rng is a random.Random; use rng.random()."""
    ...
```

```{.python .tests}
import random


def exact(k):
    return 2 ** (k + 1) - 2


def test_one_head():
    # geometric(1/2): mean 2, standard deviation sqrt(2); 5 standard errors is 0.07
    est = mean_flips_until_run(1, 10_000, random.Random(1))
    assert abs(est - exact(1)) < 0.07, est


def test_three_heads():
    # the waiting time has standard deviation about 11.9; 5 standard errors is 0.42
    est = mean_flips_until_run(3, 20_000, random.Random(2))
    assert abs(est - exact(3)) < 0.42, est


def test_no_heads_needed():
    assert mean_flips_until_run(0, 100, random.Random(3)) == 0


def test_uses_the_generator():
    a = mean_flips_until_run(2, 500, random.Random(4))
    b = mean_flips_until_run(2, 500, random.Random(4))
    assert a == b, "the same seed must give the same estimate"
```
:::

::: {.problem #prob-mit6041f10-9-q2 origin="external" source="mit6041f10-9-q2"}
Demonstrate that the Chebyshev inequality is tight, that is, for every $\mu$, $\sigma > 0$, and $c \geq \sigma$, construct a random variable $X$ with mean $\mu$ and standard deviation $\sigma$ such that
$$\mathbf{P}(|X - \mu| \geq c) = \frac{\sigma^2}{c^2}.$$
Hint: You should be able to do this with a discrete random variable that takes on only 3 distinct values with nonzero probability.
:::

::: {.problem #prob-mit18065ps-20-q10 origin="external" source="mit18065ps-20-q10"}
Computer experiment : Find the average $A_{1000000}$ of a million random 0-1 samples ! What is your value of the standardized variable $X=\big(A_N-\frac12\big)/2\sqrt N$ ?
:::

::: {.problem #prob-mit18065ps-20-q3 origin="external" source="mit18065ps-20-q3"}
A fair coin flip has outcomes $X=0$ and $X=1$ with probabilities $\frac12$ and $\frac12$. What is the probability that $X\ge2\overline X$ ? Show that Markov's inequality gives the exact probability $\overline X/2$ in this case.
:::

::: {.problem #prob-eecs126-1-q1 origin="external" source="eecs126-1-q1"}
Come up with examples of random variables $X_1,\dots,X_n$ in which (1) and (2) are tight.

*Note (these notes):* The notes state, for $S_n=X_1+\dots+X_n$, the first moment bound (1) $P(|S_n|\ge\lambda)\le\frac1\lambda\sum_{i=1}^nE|X_i|$ (Markov's inequality, @thm-markov-inequality) and the second moment bound (2) $P(|S_n|\ge\lambda)\le\frac1{\lambda^2}\sum_{i=1}^n\mathrm{Var}(X_i)$ (Chebyshev's inequality, @thm-chebyshev-s-inequality), for pairwise independent $X_i$ (and mean zero, implicitly).
:::
