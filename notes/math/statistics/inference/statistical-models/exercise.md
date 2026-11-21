::: {.problem #prob-mit18650f16-2-q1 origin="external" source="mit18650f16-2-q1"}
Biased/unbiased estimation

Let $X_1,\dots,X_n$ be i.i.d. Bernoulli random variables, with unknown parameter $p\in(0,1)$. The aim of this exercise is to estimate the common variance of the $X_i$'s.

1. Show that $\operatorname{var}(X_i)=p(1-p)$

2. Let $\bar X_n$ be the sample average of the $X_i$'s. Prove that $\bar X_n(1-\bar X_n)$ is a consistent estimator of $p(1-p)$.

3. Compute the bias of this estimator.

4. Using the previous question, find an unbiased estimator of $p(1-p)$.
:::

::: {.problem #prob-mit18650f16-2-q2 origin="external" source="mit18650f16-2-q2"}
Statistical models and identifiability

For the following experiments, define a statistical model and check whether the parameter of interest is identified.

1. One observes $n$ i.i.d. Poisson random variables with unknown parameter $\lambda$.

2. One observes $n$ i.i.d. exponential random variables with parameter $\lambda$, which is unknown but a priori known to be no larger than 10.

3. One observes $n$ i.i.d. uniform random variables in the interval $[0,\theta]$, where $\theta$ is unknown.

4. One observes $n$ i.i.d. Gaussian random variables with unknown parameters $\mu,\sigma^2$.

5. One observes the sign of $n$ i.i.d. Gaussian random variables with unknown parameters $\mu,\sigma^2$.

6. StatGen is a statistical procedure to test the relevance of genes. When well calibrated, it outputs the (random) proportion of active genes in a (random) cell. We want to estimate the distribution of this proportion. To that end, we take $n$ iid cells and submit them to StatGen to collect $n$ random variables $X_1,\dots,X_n$ that have uniform distribution on $[0,\theta]$ for some unknown theta.

7. The US Census Bureau is interested in finding out the average commute time of Bostonians. To that end, it randomly selects $n$ individuals, with replacement, among the people who work and live in the Boston area, and asks to each if their commute time is at least 20 minutes. The commute time of a random person is assumed to follow an exponential distribution.

8. Willy Wonka's contains 67 identical machines. Each machine has a lifetime that is modeled as an exponential random variable with some unknown parameter $\lambda$. After a certain time $T=500$ days, one has observed the lifetime of all machines that have stopped working before $T$. The parameter of interest is $\lambda$.
:::
