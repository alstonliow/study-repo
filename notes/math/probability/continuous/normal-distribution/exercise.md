::: {.problem #prob-cs70hw-14-q7 origin="external" source="cs70hw-14-q7"}
**Sampling a Gaussian With Uniform.** In this question, we will see one way to generate a normal random variable if we have access to a random number generator that outputs numbers between 0 and 1 uniformly at random.

As a general comment, remember that showing two random variables have the same CDF or PDF is sufficient for showing that they have the same distribution.

(a) First, let us see how to generate an exponential random variable with a uniform random variable. Let $U_1 \sim \mathrm{Uniform}(0, 1)$. Prove that $-\ln U_1 \sim \mathrm{Expo}(1)$.

(b) Let $N_1, N_2 \sim \mathcal{N}(0, 1)$, where $N_1$ and $N_2$ are independent. Prove that $N_1^2 + N_2^2 \sim \mathrm{Expo}(1/2)$.

Hint: You may use the fact that over a region $R$, if we convert to polar coordinates $(x, y) \to (r, \theta)$, then the double integral over the region $R$ will be
$$\iint_R f(x, y)\, dx\, dy = \iint_R f(r\cos\theta, r\sin\theta) \cdot r\, dr\, d\theta.$$

(c) Suppose we have two uniform random variables, $U_1$ and $U_2$. How would you transform these two random variables into a normal random variable with mean 0 and variance 1?

Hint: What part (b) tells us is that the point $(N_1, N_2)$ will have a distance from the origin that is distributed as the square root of an exponential distribution. Try to use $U_1$ to sample the radius, and then use $U_2$ to sample the angle.
:::
