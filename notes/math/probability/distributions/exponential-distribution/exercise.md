::: {.problem #prob-cs70hw-14-q3 origin="external" source="cs70hw-14-q3"}
**Exponential Distributions: Lightbulbs.** A brand new lightbulb has just been installed in our classroom, and you know the life span of a lightbulb is exponentially distributed with a mean of 50 days.

(a) Suppose an electrician is scheduled to check on the lightbulb in 30 days and replace it if it is broken. What is the probability that the electrician will find the bulb broken?

(b) Suppose the electrician finds the bulb broken and replaces it with a new one. What is the probability that the new bulb will last at least 30 days?

(c) Suppose the electrician finds the bulb in working condition and leaves. What is the probability that the bulb will last at least another 30 days?
:::

::: {.problem #prob-mit1805s22-4-q1 origin="external" source="mit1805s22-4-q1"}
Time to failure
Recall that an exponential random variable $X \sim \exp(\lambda)$ has pdf given by $f(x) = \lambda e^{-\lambda x}$ on $x \geq 0$.

(a) Compute $P(X \geq x)$.

(b) Compute the mean and standard deviation of $X$. You need to set up the necessary integrals, but you can use Wolfram Alpha or another application to do the computation. (Of course, it will be good for you if you compute the integrals by hand!)

(c) Suppose that $X_1$ and $X_2$ are independent $\exp(\lambda)$ random variables. Let $T = \min(X_1, X_2)$. Find the cdf and pdf of $T$. (Hint: first find a formula for $P(T \geq t)$?)

Note: for independent continuous random variables $X_1, X_2$, you can assume the following formula:
$$P(X_1 \geq x_1, X_2 \geq x_2) = P(X_1 \geq x_1)P(X_2 \geq x_2).$$

(d) Suppose we are testing 3 different brands of light bulbs $B_1$, $B_2$, and $B_3$ whose lifetimes are exponential random variables with mean 1/2, 1/3, and 1/5 years, respectively. Assuming that all of the bulbs are independent, what is the expected time before one of the bulb fails. (Hint: part (c) was a warmup for this problem.)
:::
