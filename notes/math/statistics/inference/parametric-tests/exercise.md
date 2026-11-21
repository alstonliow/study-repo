::: {.problem #prob-mit18650f16-5-q1 origin="external" source="mit18650f16-5-q1"}
Hypotheses testing and confidence intervals

Consider a sample $X_1,\dots,X_n\overset{i.i.d.}{\sim}\operatorname{Poiss}(\lambda)$, for some unknown $\lambda>0$.

1. Based on the sample, propose a confidence interval for $\lambda$ with asymptotic level $1-\alpha$, for some fixed $\alpha\in(0,1)$ (prove your answer). Denote by $I$ your confidence interval.

2. Consider the following hypotheses, where $\lambda_0$ is a given positive number:
$$H_0:\ \text{"}\lambda=\lambda_0\text{"}\quad\text{vs.}\quad H_1:\ \text{"}\lambda\ne\lambda_0\text{"}.$$
Using the confidence interval $I$, propose a test with asymptotic level $\alpha$ for these hypotheses.
:::

::: {.problem #prob-mit18650f16-5-q2 origin="external" source="mit18650f16-5-q2"}
Comparing two means

Consider two measuring instruments that are used to measure the intensity of some electromagnetic waves. An engineer wants to check if both instruments are calibrated identically, i.e., if they will produce identical measurements for identical waves. To do so, the engineer does $n_1$ independent measurements of the intensity of a given wave using the first instrument, and $n_2$ measurements on the same wave using the second instrument. The integers $n_1$ and $n_2$ may not be equal because, for instance, one instrument may be more costly than the other one, or may produce measurements more slowly. The measurements are denoted by $X_1,\dots,X_{n_1}$ for the first instrument and by $Y_1,\dots,Y_{n_2}$ for the second one. Intrinsic defects of the instruments will lead to measurement errors, and it is reasonable to assume that $X_1,\dots,X_{n_1}$ are iid Gaussian and so are $Y_1,\dots,Y_{n_2}$. If the two instruments are identically calibrated, the $X_i$'s and the $Y_i$'s should have the same expectation but may not have the same variance, since the two instruments may not have the same precision.

Hence, we assume that $X_1,\dots,X_{n_1}\overset{i.i.d.}{\sim}N(\mu_1,\sigma_1^2)$ and $Y_1,\dots,Y_{n_2}\overset{i.i.d.}{\sim}N(\mu_2,\sigma_2^2)$, where $\mu_1,\mu_2\in\mathbb{R}$ and $\sigma_1^2,\sigma_2^2>0$, and that the two samples are independent of each other. We want to test whether $\mu_1=\mu_2$.

1. Recall the expression of the maximum likelihood estimators for $(\mu_1,\sigma_1^2)$ and for $(\mu_2,\sigma_2^2)$. Denote these estimators by $(\hat\mu_1,\hat\sigma_1^2)$ and $(\hat\mu_2,\hat\sigma_2^2)$.

2. Recall the distribution of $\dfrac{n_1\hat\sigma_1^2}{\sigma_1^2}$ and of $\dfrac{n_2\hat\sigma_2^2}{\sigma_2^2}$.

3. What is the distribution of $\dfrac{n_1\hat\sigma_1^2}{\sigma_1^2}+\dfrac{n_2\hat\sigma_2^2}{\sigma_2^2}$ ?

4. Let $\Delta=\hat\mu_1-\hat\mu_2$. What is the distribution of $\Delta$ ?

5. Consider the following hypotheses:
$$H_0:\ \text{"}\mu_1=\mu_2\text{"}\quad\text{vs.}\quad H_0:\ \text{"}\mu_1\ne\mu_2\text{"}.$$
Here and in the next question we assume that $\sigma_1^2=\sigma_2^2$. Based on the previous questions, propose a test with non asymptotic level $\alpha\in(0,1)$ for $H_0$ against $H_1$.

6. Assume that 10 measurements have been done for both machines. The first instrument measured 8.43 in average with sample variance 0.22 and the second instrument measured 8.07 with sample variance 0.17. Can you conclude that the calibrations of the two machines are significantly identical at level 5% ? What is, approximately, the p-value of your test ?

*Note (these notes):* In question 5 the handout labels the alternative $H_0$ again; it is the alternative $H_1$.
:::

::: {.problem #prob-mit18650f16-5-q3 origin="external" source="mit18650f16-5-q3"}
Implicit hypotheses testing

Based on a sample of i.i.d. Gaussian random variables $X_1,\dots,X_n$ with mean $\mu$ and variance $\sigma^2$, propose a test with asymptotic level 5% for the hypotheses
$$H_0:\ \text{"}\mu>\sigma\text{"}\quad\text{vs.}\quad H_1:\ \text{"}\mu\le\sigma\text{"}.$$
What is the p-value of your test if the sample has size $n=100$, the sample average is 2.41 and the sample variance is 5.20 ? If the sample size is $n=100$, the sample average is 3.28 and the sample variance is 15.95 ? In the latter case, do you reject $H_0$ at level 5% ? At level 10% ?
:::

::: {.problem #prob-mit18650f16-6-q1 origin="external" source="mit18650f16-6-q1"}
Hypotheses testing - Basics

Let $X_1,\dots,X_n\overset{i.i.d.}{\sim}\operatorname{Exp}(\lambda)$, for some unknown parameter $\lambda>0$ and let $\lambda_0$ be a (known) fixed positive number.

1. Consider the following hypotheses:
$$H_0:\ \text{"}\lambda=\lambda_0\text{"}\quad\text{vs.}\quad H_1:\ \text{"}\lambda\ne\lambda_0\text{"}.$$
Give a test with asymptotic level $\alpha$, for any $\alpha\in(0,1)$.

2. Consider the following hypotheses:
$$H_0:\ \text{"}\lambda\le\lambda_0\text{"}\quad\text{vs.}\quad H_1:\ \text{"}\lambda>\lambda_0\text{"}.$$
Give a test with asymptotic level (at most) $\alpha$, for any $\alpha\in(0,1)$.

3. At a call center, the times between two consecutive calls are modeled as i.i.d. exponential random variables, with some unknown parameter $\lambda$. The employer of this center wants to determine whether more employees should be hired. In order to do so, he/she wants to get some information about $\lambda$. The value itself of $\lambda$ is irrelevant, but if $\lambda\ge1$, meaning that the average time between two calls is no larger than 1 (minute), the employer's decision will be to hire more employees.

   To make his/her decision, the employer observes the times between 50 consecutive calls, and finds out that the average these observations is 0.98.

   In statistical words, the employer needs to test the following hypotheses:
   $$H_0:\ \text{"}\lambda\le1\text{"}\quad\text{vs.}\quad H_1:\ \text{"}\lambda>1\text{"}.$$

   a) Based on the observations and using the same test as in the previous question, should the employer reject the null hypothesis ?

   b) What is the p-value of the test ?
:::

::: {.problem #prob-mit18650f16-6-q2 origin="external" source="mit18650f16-6-q2"}
A Student one-sided test

Let $X_1,\dots,X_n\overset{i.i.d.}{\sim}N(\mu,\sigma^2)$, for some unknown parameter $(\mu,\sigma^2)\in\mathbb{R}\times(0,\infty)$. We want to test the following hypotheses at non asymptotic level $\alpha$ (for some fixed $\alpha\in(0,1)$):
$$H_0:\ \text{"}\mu>0\text{"}\quad\text{vs.}\quad H_1:\ \text{"}\mu\le0\text{"}.$$

1. Recall the maximum likelihood estimator $(\hat\mu,\hat\sigma^2)$ of $(\mu,\sigma^2)$.

2. Let $S=\sqrt{n-1}\,\dfrac{\hat\mu-\mu}{\sqrt{\hat\sigma^2}}$. Prove that $S$ is a Student random variable with $n-1$ degrees of freedom.

3. Propose a test with non asymptotic level $\alpha$. Prove your answer.

*Note (these notes):* The handout says that an earlier version had a typo in Question 3; the statement here is the posted version.
:::

::: {.problem #prob-mit18650f16-6-q3 origin="external" source="mit18650f16-6-q3"}
Test of independence for Bernoulli random variables

Let $X,Y$ be two Bernoulli random variables and denote by $p=P[X=1]$, $q=P[Y=1]$ and $r=P[X=1,Y=1]$.

1. Prove that $X$ and $Y$ are independent if and only if $r=pq$.

2. Let $(X_1,Y_1),\dots,(X_n,Y_n)$ be a sample of $n$ i.i.d. copies of $(X,Y)$. Based on this sample, we want to test whether $X$ and $Y$ are independent, i.e., whether $r=pq$.

   a) Define $\hat p=\frac1n\sum_{i=1}^nX_i$, $\hat q=\frac1n\sum_{i=1}^nY_i$ and $\hat r=\frac1n\sum_{i=1}^nX_iY_i$. Prove that these are, respectively, consistent estimators of $p$, $q$ and $r$.

   b) Show that the vector $(\hat p,\hat q,\hat r)$ is asymptotically normal and find the asymptotic covariance matrix.

   c) Using the previous question combined with the Delta-method, prove that
   $$\sqrt n\bigl(\hat r-\hat p\hat q-(r-pq)\bigr)\xrightarrow[n\to\infty]{(d)}N(0,V),$$
   where $V$ depends on $p$, $q$ and $r$.

   d) Consider the following hypotheses:
   $$H_0:\ \text{"}X\text{ and }Y\text{ are independent"}\quad\text{vs.}\quad H_1:\ \text{"}X\text{ and }Y\text{ are not independent"}.$$
   Assuming that $H_0$ is true, show that $V=pq(1-p)(1-q)$ and propose a consistent estimator of $V$.

   e) Using the last two questions, propose a test with asymptotic level $\alpha$, for any $\alpha\in(0,1)$.

We would like to know whether the facts of being happy and being in a relationship are independent of each other. In a given population, 1000 people (aged at least 21 years old) are sampled and asked two questions: "Do you consider yourself as happy ?" and "Are you involved in a relationship ?". The answers are summarized in the following table:

| | Happy | Not happy |
|---|---|---|
| In a relationship | 205 | 301 |
| Not in a relationship | 179 | 315 |

Would you reject independence of being happy and being in a relationship, with asymptotic level 5% ? Compute the p-value of your test.

*Note (these notes):* In question 2a the handout writes $\hat q=\frac1n\sum X_i$; it means $\frac1n\sum Y_i$, as used here.
:::
