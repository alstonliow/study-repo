::: {.problem #prob-mit6041f10-5-q6 origin="external" source="mit6041f10-5-q6"}
A defective coin minting machine produces coins whose probability of heads is a random variable $P$ with PDF
$$f_P(p) = \begin{cases} 1 + \sin(2\pi p), & \text{if } p \in [0, 1],\\ 0, & \text{otherwise.}\end{cases}$$
In essence, a specific coin produced by this machine will have a fixed probability $P = p$ of giving heads, but you do not know initially what that probability is. A coin produced by this machine is selected and tossed repeatedly, with successive tosses assumed independent.

(a) Find the probability that the first coin toss results in heads.
(b) Given that the first coin toss resulted in heads, find the conditional PDF of $P$.
(c) Given that the first coin toss resulted in heads, find the conditional probability of heads on the second toss.
:::

::: {.problem #prob-mit6041f10-10-q4 origin="external" source="mit6041f10-10-q4"}
Alice has two coins. The probability of heads for the first coin is 1/3; the probability of heads for the second coin is 2/3. Other than this difference in their bias, the coins are indistinguishable through any measurement known to man. Alice chooses one of the coins randomly and sends it to Bob. Let $p$ be the probability that Alice chose the first coin. Bob tries to guess which of the two coins he received by flipping it 3 times in a row and observing the outcome. Assume that all coin flips are independent. Let $Y$ be the number of heads Bob observed.

(a) Given that Bob observed $k$ heads, what is the probability that he received the first coin?
(b) Find values of $k$ for which the probability that Alice sent the first coin increases after Bob observes $k$ heads out of 3 tosses. In other words, for what values of $k$ is the probability that Alice sent the first coin given that Bob observed $k$ heads greater than $p$? If we increase $p$, how does your answer change (goes up, goes down, or stays unchanged)?
(c) Help Bob develop the rule for deciding which coin he received based on the number of heads $k$ he observed in 3 tosses if his goal is to minimize the probability of error.
(d) For this part, assume $p = 2/3$.
  i. Find the probability that Bob will guess the coin correctly using the rule above.
  ii. How does this compare to the probability of guessing correctly if Bob tried to guess which coin he received before flipping it?
(e) If we increase $p$, how does that affect the decision rule?
(f) Find the values of $p$ for which Bob will never guess he received the first coin, regardless of the outcome of the tosses.
(g) Find the values of $p$ for which Bob will always guess he received the first coin, regardless of the outcome of the tosses.
:::

::: {.problem #prob-mit6041f10-10-q5 origin="external" source="mit6041f10-10-q5"}
Consider a Bernoulli process $X_1, X_2, X_3, \ldots$ with unknown probability of success $q$. As usual, define the $k$th inter-arrival time $T_k$ as
$$T_1 = Y_1, \qquad T_k = Y_k - Y_{k-1}, \quad k = 2, 3, \ldots$$
where $Y_k$ is the time of the $k$th success. This problem explores estimation of $q$ from observed inter-arrival times $\{t_1, t_2, t_3, \ldots\}$.

You may find the following integral useful: For any non-negative integers $k$ and $m$,
$$\int_0^1 q^k (1-q)^m \, dq = \frac{k!\, m!}{(k+m+1)!}.$$
Assume $q$ is sampled from the random variable $Q$ which is uniformly distributed over $[0, 1]$.

(a) Compute the PMF of $T_1$, $p_{T_1}(t_1)$.
(b) Compute the least squares estimate (LSE) of $Q$ from the first recording $T_1 = t_1$.
(c) Compute the maximum a posteriori (MAP) estimate of $Q$ given the $k$ recordings, $T_1 = t_1, \ldots, T_k = t_k$.

For this part only assume $q$ is sampled from the random variable $Q$ which is now uniformly distributed over $[0.5, 1]$

(d) Find the linear least squares estimate (LLSE) of the second inter-arrival time ($T_2$), from the observed first arrival time ($T_1 = t_1$).
:::

::: {.problem #prob-mit6041f10-10-q6 origin="external" source="mit6041f10-10-q6"}
The joint PDF of $X$ and $Y$ is defined as follows:
$$f_{X,Y}(x,y) = \begin{cases} cxy & \text{if } 0 < x \leq 1,\ 0 < y \leq 1,\\ 0 & \text{otherwise.}\end{cases}$$

(a) Find the normalization constant $c$.
(b) Compute the conditional expectation estimator of $X$ based on the observed value $Y = y$.
(c) Is this estimate different from what you would have guessed before you saw the value $Y = y$? Explain.
(d) Repeat (b) and (c) for the MAP estimator.
:::

::: {.problem #prob-mit6041f10-11-q2 origin="external" source="mit6041f10-11-q2"}
Caleb builds a particle detector and uses it to measure radiation from far stars. On any given day, the number of particles $Y$ that hit the detector is conditionally distributed according to a Poisson distribution conditioned on parameter $x$. The parameter $x$ is unknown and is modeled as the value of a random variable $X$, exponentially distributed with parameter $\mu$ as follows.
$$f_X(x) = \begin{cases} \mu e^{-\mu x} & x \geq 0\\ 0 & \text{otherwise}\end{cases}$$
Then, the conditional PDF of the number of particles hitting the detector is,
$$p_{Y|X}(y \mid x) = \begin{cases} \dfrac{e^{-x} x^y}{y!} & y = 0, 1, 2, \ldots\\ 0 & \text{otherwise}\end{cases}$$

(a) Find the MAP estimate of $X$ from the observed particle count $y$.
(b) Our goal is to find the conditional expectation estimator for $X$ from the observed particle count $y$.
  i. Show that the posterior probability distribution for $X$ given $Y$ is of the form
  $$f_{X|Y}(x \mid y) = \frac{\lambda^{y+1}}{y!} x^y e^{-\lambda x}, \quad x > 0$$
  and find the parameter $\lambda$. You may find the following equality useful (it is obviously true if the equation above describes a true PDF):
  $$\int_0^\infty a^{y+1} x^y e^{-ax}\,dx = y! \quad \text{for any } a > 0$$
  ii. Find the conditional expectation estimate of $X$ from the observed particle count $y$. Hint: you might want to express $x f_{X|Y}(x \mid y)$ in terms of $f_{X|Y}(x \mid y+1)$.
(c) Compare the two estimators you constructed in part (a) and part (b).
:::
