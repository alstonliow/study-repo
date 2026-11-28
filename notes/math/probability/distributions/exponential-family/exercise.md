::: {.problem #prob-mit18650f16-11-q1 origin="external" source="mit18650f16-11-q1"}
Exponential families

For each of the following families of distributions, tell whether it is an exponential family:

- $\operatorname{Ber}(p)$, $p\in(0,1)$;
- $N(\mu,1)$, $\mu\in\mathbb{R}$;
- $N(\mu,\sigma^2)$, $\mu\in\mathbb{R}$, $\sigma^2>0$;
- $\operatorname{Exp}(\lambda)$, $\lambda>0$;
- $\mathcal U([0,\vartheta])$, $\vartheta>0$;
- $\Gamma(\alpha,\beta)$, $\alpha>0$, $\beta>0$;
- $\operatorname{Poiss}(\lambda)$, $\lambda>0$.

Recall that the Gamma distribution with parameters $\alpha,\beta>0$ has density
$$f(x)=\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x},\quad x>0,$$
where $\Gamma$ is the Gamma function.
:::

::: {.problem #prob-mit18650f16-11-q2 origin="external" source="mit18650f16-11-q2"}
One parameter canonical Exponential families

Let $\Theta\subseteq\mathbb{R}$ and consider the family of densities $f_\theta$, $\theta\in\Theta$ defined on a subset $\mathcal X$ of $\mathbb{R}$ (called sample space) by
$$f_\theta(x)=a(x)\exp(-\theta x+b(\theta)),\quad x\in\mathcal X,$$
where $a$ is a positive function defined on $\mathcal X$ and $b$ is a function defined on the space $\Theta$ (called parameter space).

Let $\ell(\theta)=\ln f_\theta(X)$, $\theta\in\Theta$, be the log-likelihood function, where $X$ is a random variable on $\mathcal X$.

1. In the rest of the problem, if $\theta\in\Theta$ and $g$ is a function defined on $\mathbb{R}$, denote by $E_\theta[g(X)]$ (resp. $\operatorname{Var}_\theta[g(X)]$) the expectation (resp. variance) of $g(X)$ under the assumption that $X$ has density $f_\theta$.

   a) Why is it true that
   $$\int_{\mathbb{R}}f_\theta(x)\,dx=1,\quad\forall\theta\in\Theta\ ?$$

   b) Assuming that you can switch expectations and derivatives with respect to $\theta$, prove the following identities:

      1. $E_\theta[\ell'(\theta)]=0$;
      2. $\operatorname{Var}_\theta[\ell'(\theta)]=-E_\theta[\ell''(\theta)]$.

   c) What is the name of the last quantity in the previous question ?

2. Compute $\ell'(\theta)$ and $\ell''(\theta)$ in terms of the functions $a$ and $b$.

3. Using the previous functions, compute $E_\theta[X]$ and $\operatorname{Var}_\theta[X]$, for all $\theta\in\Theta$.

4. Example: Assume that $\Theta=(0,\infty)$ and for $\theta>0$, $f_\theta$ is the density of the Gamma distribution with parameters $\alpha$ and $\theta$, where $\alpha$ is a fixed number.

   a) What is the sample space $\mathcal X$ ?

   b) What are the functions $a$ and $b$ ?

   c) Using the previous questions, compute the expectation and the variance of the Gamma distribution with parameters $\alpha,\beta>0$.
:::

::: {.problem #prob-camii-sms-3-q4 origin="external" source="camii-sms-3-q4"}
Show the following families of distributions are (possibly multi-parameter) exponential families; all parameters are unknown unless noted otherwise. Then find the corresponding natural parameters, sufficient statistics, and cumulant functions.

(a) The normal distribution, $N(\mu,\sigma^2)$:
$$f(y;\mu,\sigma^2)=\frac1{\sqrt{2\pi\sigma^2}}e^{-\frac{(y-\mu)^2}{2\sigma^2}},\quad y\in\mathbb R.$$

(b) The negative binomial distribution (number of failures until $k$ successes are reached in Bernoulli trials), $\mathrm{NegBin}(k,p)$ with fixed $k$:
$$f(y;p)=\binom{y+k-1}{y}p^k(1-p)^y,\quad y=0,1,2,\dots$$
:::

::: {.problem #prob-camii-sms-3-q5 origin="external" source="camii-sms-3-q5"}
Let $Y$ be a real-valued random variable whose moment generating function is finite on an open interval containing zero. Show that the first three cumulants are $\kappa_1=\mathbb E(Y)$, $\kappa_2=\operatorname{Var}(Y)$, $\kappa_3=\mathbb E(Y-\kappa_1)^3$, respectively. Use these to find the mean and variance of the negative binomial distribution $\mathrm{NegBin}(k,p)$ (in terms of $k$ and $p$).
:::

::: {.problem #prob-camii-sms-3-q9 origin="external" source="camii-sms-3-q9"}
The probability density function of the Gamma distribution with shape parameter $\alpha>0$ and rate parameter $\beta>0$ is given by
$$f(y;\alpha,\beta)=\frac{\beta^\alpha y^{\alpha-1}e^{-\beta y}}{\Gamma(\alpha)}.$$
Show that this is an exponential dispersion family by finding the natural and dispersion parameters. Hint: It may be useful to know that the mean and variance of the Gamma distribution are $\alpha/\beta$ and $\alpha/\beta^2$, respectively.
:::
