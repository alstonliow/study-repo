::: {.problem #prob-mit1805s22-8-q1 origin="external" source="mit1805s22-8-q1"}
(Confident coin: III)
When spun on edge 250 times a certain coin came up heads 140 times and tails 110. We can make the statement: 'if the coin is unbiased then the probability of getting a result at least this extreme is 7%.'

(a) Let $\theta$ be the probability of coming up heads. Consider the null hypothesis that the coin is fair, $H_0 : \theta = 0.5$. Carefully explain how the 7% figure arises. What term describes this value in NHST? Does it correspond to a one-sided or two-sided test?

(b) Would you reject $H_0$ at a significance level of $\alpha = 0.1$? What about $\alpha = 0.05$? (For this problem assume the test has the same sidedness as the one used to get the 7% $p$-value in part (a).)

(c) How many heads would you need to have observed out of 250 spins to reject at a significance of $\alpha = 0.01$? (Again assume the same sidedness as the test used to get the 7% $p$-value in part (a).)

(d) (i) Fix the significance level at $\alpha = 0.05$. Compute and compare the power of the test for values of the alternative hypothesis $\theta = 0.55$ and $\theta = 0.6$? (Again assume the same sidedeness as in part (a). Here, $H_A$ is composite, so the power is different for different values of the hypothesis.)

(ii) Sketch the pmf of each hypothesis and use it to explain the change in power observed in part (i).

(e) (i) Again fix $\alpha = 0.05$. What is the smallest number of spins necessary for the test to have a power of 0.9 when $H_A : \theta = 0.55$? (Again, use the sidedness from part (a).)

(ii) As in part (d), draw sketches and explain how they illustrate the change in power.

(f) Let $H_A : \theta = 0.55$. Suppose we have only two hypotheses $H_0$ and $H_A$, and a flat prior $P(H_0) = P(H_A) = 0.5$. What is the posterior probability of $H_A$ given the data? (In this part $H_A$ is different from in the previous parts; it consists of one specific value of $\theta$.)

(g) Given the data, what probability would you personally place on the coin being biased toward heads? Why? There is no one right answer, we are simply interested in your thinking.
:::

::: {.problem #prob-mit1805s22-8-q3 origin="external" source="mit1805s22-8-q3"}
z-test
Suppose three radar guns are set up along a stretch of road to catch people driving over the speed limit of 40 miles per hour. Each radar gun is known to have a normal measurement error modeled on $N(0, 5^2)$. For a passing car, let $\bar x$ be the average of the three readings. Our default assumption for a car is that it is not speeding.

(a) Describe the above story in the context of NHST. Are the most natural null and alternative hypotheses simple or composite?

(b) The police would like to set a threshold on $\bar x$ for issuing tickets so that no more than 4% of law abiding, non-speeders are mistakenly given tickets. You should assume this means that they set the threshold conservatively, so that no more 4% of drivers going exactly 40 mph get a ticket.

(i) Use the NHST description in part (a) to help determine what threshold should they set.

(ii) Sketch a graph illustrating your reasoning in part (i).

(iii) What is the probability that a person getting a ticket was not speeding?

(iv) Suppose word gets out about the speed trap and no one speeds along it anymore. What percentage of tickets are given in error?

(c) What is the power of this test with the alternative hypothesis that the car is traveling at 45 miles per hour? How many cameras are needed to achieve a power of 0.9 with $\alpha = 0.04$?
:::

::: {.problem #prob-mit1805s22-8-q4 origin="external" source="mit1805s22-8-q4"}
One generates a number $x$ from a uniform distribution on the interval $[0, \theta]$. One decides to test $H_0 : \theta = 2$ against $H_A : \theta \neq 2$ by rejecting $H_0$ if $x \leq 0.1$ or $x \geq 1.9$.

(a) Compute the probability of a type I error.

(b) Compute the probability of a type II error if the true value of $\theta$ is 2.5.
:::
