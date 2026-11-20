::: {.problem #prob-mit1805s22-10-q2 origin="external" source="mit1805s22-10-q2"}
(Soda)
Consider a machine that is known to fill soda cans with amounts that follow a normal distribution with (unknown) mean $\mu$ and standard deviation $\sigma = 3$ mL. We measure the volume of soda in a sample of bottles and obtain the following data (in mL):

$$352,\ 351,\ 361,\ 353,\ 352,\ 358,\ 360,\ 358,\ 359$$

For this problem, you will probably want to use R to make the calculations.

(a) Construct a precise 95% confidence interval for the mean $\mu$.

(b) Now construct a 98% confidence interval for the mean $\mu$.

(c) Suppose now that $\sigma$ is not known. Redo parts (a) and (b), and compare your answers to those above.
:::

::: {.problem #prob-mit1805s22-10-q3 origin="external" source="mit1805s22-10-q3"}
(Cholesterol)
In a study on cholesterol levels a sample of 12 men and women was chosen. The plasma cholesterol levels (mmol/L) of the subjects were as follows:

$$6.0,\ 6.4,\ 7.0,\ 5.8,\ 6.0,\ 5.8,\ 5.9,\ 6.7,\ 6.1,\ 6.5,\ 6.3,\ 5.8.$$

(a) Estimate the variance of the plasma cholesterol levels with a 95% confidence interval.

(b) What assumptions did you make about the sample in order to make your estimate?
:::

::: {.problem #prob-mit1805s22-10-q4 origin="external" source="mit1805s22-10-q4"}
(Candy)
A candy manufacturer produces packs of candy targeted to weigh 52 grams. A quality control manager was concerned that the variation in the actual weights was larger than acceptable. That is, They were concerned that some packs weighed significantly less than 52-grams and some weighed significantly more than 52 grams. In order to estimate $\sigma$, the standard deviation of the weights of the nominal 52-gram packs, they took a random sample of n = 10 packs off of the factory line. The random sample yielded a sample variance of 4.2 grams$^2$.

(a) Use the random sample to derive a 95% confidence interval for $\sigma$. Note: the interval is for $\sigma$ not $\sigma^2$.

(b) What assumptions did you make about the sample in order to make your estimate.
:::

::: {.problem #prob-mit1805s22-10-q5 origin="external" source="mit1805s22-10-q5"}
Probabilities for hypotheses
When given a 95% confidence interval many people often mistake this to mean that there is a 95% probablility that the true value of the parameter is in the confidence interval. This violates the maxim that frequentists don't give probabilities for hypotheses, but the reasoning is subtle. This problem is aimed at understanding the subtlety.

(a) What 95% does mean. Imagine running the following experiment.

- Pick a value $\mu$.
- Draw a sample of size $n$ from a $N(\mu, 5^2)$ distribution.
- Compute the 95% $z$-confidence interval for $\mu$.
- Check if $\mu$ is in the confidence interval.
- Record the result.

If you repeat this experiment many times, what percentage of the time will the chosen $\mu$ be in the confidence interval? (Hint, this is not a question about the probability of hypothesized values of $\mu$. It's about the probability of random intervals.)

(b) What 95% doesn't mean. Now let's modify this a bit. Suppose we have the following choices and prior probabilities for $\mu$

| $\mu$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $p(\mu)$ | 0.94 | 0.02 | 0.02 | 0.02 |

Suppose I pick a random $\mu$ from this prior distribution and draw a sample of size 64 from a $N(\mu, 5)$ distribution. I do not tell you the value of $\mu$, but I do tell you that the sample mean is $\bar x = 1.6$.

We both know the sample size ($n = 64$) and the variance used in drawing the sample ($\sigma^2 = 5^2$). So we both know that the 95% confidence interval for $\mu$ is
$$\bar x \pm z_{0.025} \cdot \frac{\sigma}{\sqrt{n}} \approx 1.6 \pm 1.96 \cdot \frac{5}{8} \approx [0.375, 2.825].$$

(i) Compute the prior probability that $\mu$ is in the above confidence interval.

(ii) Update the probabilities for $\mu$ based on the data and compute the posterior probability that $\mu$ is in the above confidence interval.

Are either of these probabilities close to 95%? Why is this not surprising?

(c) A medical study shows that patients receiving a new cancer treatment survived an average of 15 months longer than patients receiving the conventional treatment. The study also found that the 95% confidence interval for this average was 10 to 20 months.

Say whether each of the following statements is true or false. False means that the statement does not follow logically from the confidence-interval result.

(i) There is a 95% probability that the true increase in survival time lies between 10 and 20 months.

(ii) The probability that the new treatment increases survival time is at least 95%.

(iii) The confidence interval provides an estimate of the true value of the average increase in survival time.

(iv) The null hypothesis that there is no change in survival time due to the new treatment is likely to be incorrect.

(v) If we ran the same study 100 times, then in approximately 95 of the studies the 95% confidence intervals would contain the true value of the change in survival time.

(vi) We would reject the null hypothesis of no improvement in survival time at the 5% significance level.

*Note (these notes):* Part (b) writes $N(\mu, 5)$ but the text that follows uses $\sigma^2 = 5^2$; the solution uses standard deviation $5$.
:::

::: {.problem #prob-mit1805s22-11-q1 origin="external" source="mit1805s22-11-q1"}
(Height)
Suppose $\mu$ is the average height of a college male. You measure the heights (in inches) of twenty college men, getting data $x_1, \ldots, x_{20}$, with sample mean $\bar x = 69.55$ in. and sample variance $s^2 = 14.26$ in$^2$. Suppose that the $x_i$ are drawn from a normal distribution with unknown mean $\mu$ and unknown variance $\sigma^2$.

(a) Using $\bar x$ and $s^2$, construct a 90% $t$-confidence interval for $\mu$.

(b) Now suppose you are told that the height of a college male is normally distributed with standard deviation 3.77 in. Using the same data as in part (a), construct a 90% $z$-confidence interval for $\mu$.

(c) In (b), how many people in total would you need to measure to bring the width of the 90% $z$-confidence interval down to 1 inch?
:::

::: {.problem #prob-mit1805s22-11-q2 origin="external" source="mit1805s22-11-q2"}
Confidence intervals from standardized statistics
The Beta distribution arises in a surprising way: draw a sample of size $n$ from a uniform(0,1) distribution and let $w_2$ be the second smallest value. Then it turns out that
$$w_2 \sim \mathrm{Beta}(2, n - 1).$$
Now suppose you draw a sample of size $n$ from a uniform$(0, a)$ distribution, where $a$ is unknown. If we let $y_2$ be the second smallest data value then the standardized order statistic
$$y_2/a \sim \mathrm{Beta}(2, n - 1).$$
Use $y_2$ and qbeta in R, to define a 95% confidence interval for $a$. (Because $n$ and $y_2$ are not given this will be a general formula not numbers.)

Finally, supposing $n = 9$ and $y_2 = 1.5$, give the 95% confidence interval for $a$.
:::

::: {.problem #prob-mit1805s22-11-q3 origin="external" source="mit1805s22-11-q3"}
Various variances
Consider a sample of size $n$ drawn from a Bernoulli($\theta$) distribution. (That is, a draw from a binomial$(n, \theta)$ distribution.) In constructing a confidence interval the conservative estimate is that the variance of the underlying Bernoulli distribution is $\sigma^2 = 1/4$ --this is conservative because for any $\theta$ we know that $\sigma^2 \leq 1/4$.

(a) In this problem we want to compare how well normal distribution using the conservative estimate matches the one using the true variance

(i) Let $\theta = 0.5$ and $n = 250$. Make a plot that includes

- the pmf $p(x\mid\theta)$ of the binomial$(n, \theta)$ distribution.
- the pdf of the normal distribution with the same mean and variance as the binomial$(n, \theta)$ distribution
- the normal distribution with the same mean (as the binomial distribution) and conservative variance to your plot.

Note: The conservative variance for a Bernoulli($\theta$) distribution is 1/4. So the conservative variance for a binomial$(n, \theta)$ is $n/4$.

Note. It is not reasonable to compare the probabilities in a pmf to the densities in a pdf. In order to make them comparable, but also to make the graphs readable, you should plot the pmf as points, but think of them as the top of a density histogram with bin width 1 and breaks on the half integers.

(ii) Make a similar plot for $\theta = 0.3$ and $n = 250$.

(iii) Make a similar plot for $\theta = 0.1$ and $n = 250$.

In each case, how close are each of the normal distributions to the binomial distribution? How do the two normal distributions differ? Based on your plots, for what range of $\theta$ do you think the conservative normal distribution is a reasonable approximation for binomial$(n, \theta)$ with large $n$?

(b) Suppose $\theta$ is the probability of success, and that the result of an experiment was 140 successes out of 250 trials. Find 80% and 95% confidence intervals for $\theta$ using the conservative variance. (For the 95% interval use the rule-of-thumb that $z_{0.025} = 2$.)

(c) Using the same data as in part (b), find an 80% posterior probability interval for $\theta$ using a flat prior, i.e. Beta(1, 1). Center your interval between the 0.1 and 0.9 quantiles. Compare this with the 80% confidence interval in part (b).

Hint: Use qbeta(p, a, b) to do the computation.
:::
