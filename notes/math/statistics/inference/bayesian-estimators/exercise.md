::: {.problem #prob-mit18650f16-10-q1 origin="external" source="mit18650f16-10-q1"}
Bayesian Estimation

Let $X_1,\dots,X_n\overset{i.i.d.}{\sim}N(0,\theta)$, for some unknown positive number $\theta$.

1. Compute the maximum likelihood estimator of $\theta$.

2. Prove that the MLE is asymptotically normal and find its asymptotic variance.

3. In a Bayesian approach:

   a) Compute Jeffreys prior ? Is it proper ?

   b) Use Bayes' formula in order to compute the posterior distribution. Is it well defined ?

   c) Compute the Bayesian estimator of $\theta$ associated with Jeffreys prior.

Recall that the inverse Gamma distribution with parameters $\alpha>1$, $\beta>0$ has density
$$f(x)=\frac{\beta^\alpha e^{-\beta/x}}{\Gamma(\alpha)\,x^{\alpha+1}},\quad x>0 .$$
Its expectation is given by $\dfrac\beta{\alpha-1}$.
:::

::: {.problem #prob-mit18650f16-10-q2 origin="external" source="mit18650f16-10-q2"}
Bayesian Estimation and Linear Regression

Let $X_1,\dots,X_n$ be $n$ deterministic vectors in $\mathbb{R}^p$ and let $\mathbb X$ be the $n\times p$ matrix whose rows are $X_1',\dots,X_n'$. Consider a sample $Y_1,\dots,Y_n$, such that conditionally on some $p$ dimensional random vector $\beta$, $Y_1,\dots,Y_n$ are independent and for each $i=1,\dots,n$,
$$Y_i-X_i'\beta\sim N(0,\sigma^2),$$
where $\sigma^2$ is a given positive number. Denote by $Y=(Y_1,\dots,Y_n)'$.

1. Conditionally on $\beta$, what is the distribution of $Y$ ?

2. Assume that the prior distribution on $\beta$ is $N_p(0,\tau^2I_p)$, where $\tau^2$ is a fixed positive number.

   a) Prove that the posterior distribution of $\beta$ (i.e., the distribution of $\beta$ conditional on $Y$) has a density proportional to $\exp\Bigl(-\dfrac1{2\sigma^2}\bigl(\|Y-\mathbb X\beta\|^2+\lambda\|\beta\|^2\bigr)\Bigr)$, for some $\lambda$ to be determined.

   b) Conclude that the posterior distribution of $\beta$ is Gaussian and determine the corresponding parameters.

   Hint: The density of the Gaussian distribution with mean vector $\mu$ and covariance matrix $\Sigma$ is given by
   $$g(\beta)=\frac1{(2\pi)^{p/2}\sqrt{\det\Sigma}}\exp\Bigl(-\frac12(\beta-\mu)'\Sigma^{-1}(\beta-\mu)\Bigr).$$

   c) What is the posterior mean of $\beta$ ?

3. Consider a frequentist approach: Assume that the linear regression of $Y_i$ on $X_i$ is $Y_i=X_i'\beta+\varepsilon_i$, for some unknown vector $\beta\in\mathbb{R}^p$, where $\varepsilon_1,\dots,\varepsilon_n$ are i.i.d. $N(0,\sigma^2)$, for some $\sigma^2>0$. The Ridge estimator of $\beta$ is defined as:
$$\hat\beta^{(R)}\in\operatorname*{argmin}_{t\in\mathbb{R}^p}\|Y-\mathbb Xt\|_2^2+\lambda\|t\|_2^2,$$
where $\lambda$ is a tuning parameter, i.e., a given number chosen by the statistician. Note that similarly to the BIC or the Lasso estimators, the Ridge estimator minimizes a penalized version of the sum of squared errors.

   a) Compute the Ridge estimator.

   b) Using the previous questions, prove that there exists a value of $\tau^2$ such that $\hat\beta^{(R)}$ is equal to the Bayesian estimator with prior distribution $N_p(0,\tau^2I_p)$.

   c) What is the distribution of $\hat\beta^{(R)}$ ?

   d) Compute the quadratic risk of $\hat\beta^{(R)}$ in terms of the matrix $\mathbb X$, $\lambda$ and $\beta$.

*Note (these notes):* The handout writes the minimisation over $t\in\mathbb{R}^S$; the minimisation is over $\mathbb{R}^p$.
:::

::: {.problem #prob-camib-sts-1-q9 origin="external" source="camib-sts-1-q9"}
Let $X_1,\dots,X_n$ be independent and identically distributed with conditional probability density function $f(x\mid\theta)=\theta x^{\theta-1}\mathbf 1_{\{0\le x\le1\}}$ for some $\theta>0$. Suppose the prior distribution for $\theta$ is $\Gamma(\alpha,\lambda)$. Find the posterior distribution of $\theta$ given $X=(X_1,\dots,X_n)$ and the Bayesian point estimator of $\theta$ under the quadratic loss function.
:::
