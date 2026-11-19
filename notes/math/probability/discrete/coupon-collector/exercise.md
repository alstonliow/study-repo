<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-2-11 origin="external" source="fit1058-cn-10.12-q11"}
(Same assumptions as the Birthday Paradox, Exercise 9.7.) You record
birthdays of members of a customer loyalty scheme. How many people do you
expect to have to enrol until their birthdays cover every day of the year?
:::

::: {.problem #prob-eecs126hw-2-q5 origin="external" source="eecs126hw-2-q5"}
**Bounds for the Coupon Collector's Problem.** Recall the coupon collector's problem, where each box contains a single coupon, and there are $n$ different types of coupons. We let $X$ be a random variable which is equal to the number of boxes bought until one of every type of coupon is obtained.

The expected value of $X$ is $nH_n$, where $H_n$ is the harmonic number of order $n$ which is defined as
$$H_n\overset{\Delta}{=}\sum_{i=1}^{n}\frac1i,$$
and satisfies the inequalities
$$\ln n\le H_n\le\ln n+1.$$

(a) Use Markov's inequality in order to show that
$$P(X>2nH_n)\le\frac12.$$

(b) Use Chebyshev's inequality in order to show that
$$P(X>2nH_n)\le\frac{\pi^2}{6(\ln n)^2}.$$
Note: You can use the identity
$$\sum_{i=1}^{\infty}\frac1{i^2}=\frac{\pi^2}{6}.$$

(c) Define appropriate events and use the union bound in order to show that
$$P(X>2nH_n)\le\frac1n.$$
Note: The sequence $a_n=(1-1/n)^n$, for $n=1,2,3,\dots$, is strictly increasing and $\lim_{n\to\infty}a_n=1/e$.
:::
