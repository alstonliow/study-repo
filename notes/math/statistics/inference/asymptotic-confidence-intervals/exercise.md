::: {.problem #prob-mit18650f16-1-q3 origin="external" source="mit18650f16-1-q3"}
A confidence interval for Bernoulli random variables

Let $X_1,\dots,X_n$ be i.i.d. Bernoulli random variables with unknown parameter $p\in(0,1)$ and denote by $\bar X_n$ their empirical average:
$$\bar X_n=\frac1n\sum_{i=1}^nX_i .$$

1. Show that $\sqrt n\dfrac{\bar X_n-p}{\sqrt{p(1-p)}}$ converges in distribution to a standard Gaussian random variable $Z$.

2. Prove that for all $t>0$,
$$\mathbb{P}[|Z|\le t]=2\mathbb{P}[Z\le t]-1 .$$

3. For $t>0$, let $I_t$ be the interval
$$I_t=\Bigl[\bar X_n-\frac{t\sqrt{p(1-p)}}{\sqrt n},\ \bar X_n+\frac{t\sqrt{p(1-p)}}{\sqrt n}\Bigr].$$
Using the previous questions, prove that
$$\mathbb{P}[I_t\ni p]\to2\Phi(t)-1,\quad n\to\infty,$$
where $\Phi$ is the cumulative distribution function of the standard Gaussian distribution.

4. In practice, we would like to be able to define an interval as small as possible, whose expression does not depend on the unknown value of $p$. Using the previous question, find the value of $t$ such that the interval $I_t$ contains $p$ with probability going to 95% as $n$ grows to infinity. Denote by $t_0$ this value.

   Hint: The 97.5%-quantile of the standard Gaussian distribution is 1.96.

In the next questions, we study three ways of updating the interval $I_{t_0}$ in order to obtain intervals that no longer depend on the unknown value of $p$.

5. A conservative method:

   a) Prove that no matter the value of $p$,
   $$p(1-p)\le\frac14 .$$

   b) Using the previous question, find an interval $J_1$ centered around $\bar X_n$ that does not depend on $p$ but that contains $p$ with probability at least 95% when $n$ becomes large.

   c) If it was known a priori that $p\le.3$, could you find an interval smaller than $J_1$, independent of $p$ and that still contains $p$ with probability at least 95% when $n$ becomes large ?

6. Solving an inequality:

   a) Prove that the statement "$p\in I_{t_0}$" is equivalent to a polynomial inequality of degree 2 in $p$.

   b) Solve this inequality in $p$.

   c) Using the previous question, propose a new interval $J_2$ that does not depend on $p$ but contains $p$ with probability going to 95% as $n$ goes to infinity.

7. Show that if you replace $p$ with $\bar X_n$ in the expression of $I_{t_0}$, you obtain an interval $J_3$ that contains $p$ with probability going to 95% as $n$ goes to infinity.

8. In order to forecast the results of the elections, $n$ registered voters are sampled randomly and with replacement and are asked whether they plan to vote for Hillary or Donald at the presidential elections. Denote by $p$ the proportion of American voters who plan to vote for Hillary, within the whole population and by $\hat p$ the proportion of sampled individuals who answer that they plan to vote for Hillary.

   a) Assume that $n=10{,}000$ and $\hat p=.7341$. Compute the intervals $J_1$, $J_2$ and $J_3$ defined in the previous questions and compare their respective lengths.

   b) Find a minimal sample size $n$ that would be required in order to be able to compute an interval of length at most $.05$ that does not depend on the unknown value of $p$ and that contains $p$ with approximate probability at least 95%.
:::

::: {.problem #prob-mit18650f16-2-q3 origin="external" source="mit18650f16-2-q3"}
A confidence interval for Poisson distributions

Let $X_1,\dots,X_n$ be i.i.d. Poisson random variables with parameter $\lambda>0$ and denote by $\bar X_n$ their empirical average:
$$\bar X_n=\frac1n\sum_{i=1}^nX_i .$$

1. Find two sequences $(a_n)_{n\in\mathbb{N}^*}$ and $(b_n)_{n\in\mathbb{N}^*}$ such that $a_n(\bar X_n-b_n)$ converges in distribution to a standard Gaussian random variable $Z\sim N(0,1)$.

2. Prove that for all $t>0$,
$$\mathbb{P}[|Z|\le t]=2\mathbb{P}[Z\le t]-1 .$$

3. Using the previous questions, find an interval $I$ centered around $\bar X_n$ such that
$$\mathbb{P}[I\ni\lambda]\to.95,\quad n\to\infty$$
[Hint: The 97.5%-quantile of the standard Gaussian distribution is 1.96.]

4. Modify the previous interval $I$ in order to get a new interval $J$, not necessarily centered around $\bar X_n$, that does not depend on $\lambda$ and such that
$$\mathbb{P}[J\ni\lambda]\to.95,\quad n\to\infty .$$
:::

::: {.problem #prob-mit18650f16-2-q4 origin="external" source="mit18650f16-2-q4"}
A confidence interval for uniform distributions

Let $X_1,\dots,X_n$ be i.i.d. uniform random variables in $[0,\theta]$, for some $\theta>0$. Denote by
$$M_n=\max_{i=1,\dots,n}X_i .$$

1. Prove that $M_n$ converges in probability to $\theta$.

2. Compute the cumulative distribution function of $n(1-M_n/\theta)$ and prove that $n(1-M_n/\theta)$ converges in distribution to an exponential random variable with parameter 1.

3. Use the previous question to find an interval $I$ of the form $I=[M_n,M_n+c]$, that does not depend on $\theta$ and such that
$$\mathbb{P}[I\ni\theta]\to.95,\quad n\to\infty .$$
[Hint: $\theta\ge M_n$]

4. Is $M_n$ unbiased?
:::
