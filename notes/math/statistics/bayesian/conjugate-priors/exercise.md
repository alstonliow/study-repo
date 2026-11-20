::: {.problem #prob-mit1805s22-7-q6 origin="external" source="mit1805s22-7-q6"}
(Normal is the new normal)
Your friend transmits an unknown value $\theta$ to you over a noisy channel. The noise is normally distributed with mean 0 and a known variance 4, so the value $x$ that you receive is modeled by $x \sim N(\theta, 2^2)$. Based on previous communications, your prior on $\theta$ is $N(6, 3^2)$.

(a) Suppose your friend transmits a value to you that you receive as $x = 5$. Use the formulas for normal-normal updating (given in the reading), to find the posterior pdf for $\theta$.

(b) Suppose your friend transmits the same value $\theta$ to you 8 times. You receive these signals plus noise as $x_1, \ldots, x_8$ with sample mean $\bar x = 5$. Using the same prior and know variance $\sigma^2$ as in part (a), show that the posterior on $\theta$ is $N(5.05, 0.47)$. Plot the prior and posterior on the same graph. Describe how the data changes your belief about the true value of $\theta$.

(c) IQ in the general population follows a $N(100, 15^2)$ distribution. An IQ test is unbiased with a known normal variance of $10^2$; that is, if the same person is tested multiple times, their measured IQ will differ from their true IQ according to a normal distribution with mean 0 and variance 100.

(i) Randall Vard scored an 80 on the test. What is the posterior expected value of their true IQ?

(ii) Mary I. Taft scored a 150 on the test. What is the posterior expected value of their true IQ?
:::
