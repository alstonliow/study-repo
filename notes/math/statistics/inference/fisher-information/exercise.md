::: {.problem #prob-mit18650f16-4-q1 origin="external" source="mit18650f16-4-q1"}
Maximum likelihood and Fisher information

For each of the following distributions, compute the maximum likelihood estimator for the unknown (one or two dimensional) parameter, based on a sample of $n$ i.i.d. random variables with that distribution. In each case, is the Fisher information well defined ? If yes, compute it.

1. $\operatorname{Ber}(p)$, $0<p<1$;

2. Poisson with parameter $\lambda>0$:
$$P_\lambda[X=k]=e^{-\lambda}\frac{\lambda^k}{k!},\quad\forall k\in\mathbb{N};$$

3. Exponential with parameter $\lambda>0$, with density
$$f_\lambda(x)=\lambda e^{-\lambda x},\quad\forall x>0;$$

4. Gaussian with parameters $\mu\in\mathbb{R}$, $\sigma^2>0$ (recall that the second parameter is $\sigma^2$, not $\sigma$);

5. Shifted exponential distribution with parameters $a\in\mathbb{R}$, $\lambda>0$ with density
$$f_{a,\lambda}(x)=\lambda e^{-\lambda(x-a)}\mathbf 1_{x\ge a},\quad\forall x\in\mathbb{R};$$

6. Log-normal distribution with parameters $\mu\in\mathbb{R}$ and $\sigma^2>0$, with density
$$f_{\mu,\sigma^2}(x)=\frac1{x\sqrt{2\pi\sigma^2}}e^{-\frac1{2\sigma^2}(\ln x-\mu)^2},\quad\forall x>0 .$$

*Note (these notes):* The handout notes a typo in its first version of the log-normal density; the corrected density is given here.
:::

::: {.problem #prob-mit18650f16-4-q3 origin="external" source="mit18650f16-4-q3"}
Censored data

In a given population, $n$ individuals are sampled randomly, with replacement, and each sampled individual is asked whether his/her salary is greater than some fixed threshold $z$. Assume that the salary of a randomly chosen individual has the exponential distribution with unknown parameter $\lambda$. Asking whether the salary overcomes a given threshold rathen than directly asking for the salary increases the number people that are willing to answer and decreases the number of mistakes in the collected answers. Denote by $X_1,\dots,X_n$ the binary responses ($X_i\in\{0,1\}$, $i=1,\dots,n$) of the $n$ sampled individuals.

1. What is the distribution of the $X_i$'s ?

2. Let $\bar X_n$ be the proportion of sampled individuals whose response was 1 (corresponding to Yes). Prove that $\bar X_n$ is asymptotically normal and compute the asymptotic variance.

3. Find a function $f$ such that $f(\bar X_n)$ is a consistent estimator of $\lambda$.

4. Prove that $f(\bar X_n)$ is asymptotically normal and compute the asymptotic variance.

5. What equation must $z$ satisfy in order to minimize the asymptotic variance computed in Question 4 ? Write this equation in the form $g_\lambda(z)=z$, where $g_\lambda$ is a function that depends on the unknown parameter $\lambda$.

6. Let $Y_1,\dots,Y_n$ be the salaries of the $n$ sampled people.

   a) If one could actually observe $Y_1,\dots,Y_n$, what would be the statistical model ?

   b) In that case, what would be the Fisher information (as a function of the unknown parameter $\lambda$ ? Denote it by $I_Y(\lambda)$.

   c) In the model where only the $X_i$'s are observed (with fixed threshold $z$), what is the Fisher information ? Denote it by $I_X(\lambda)$.

   d) Compare $I_Y(\lambda)$ and $I_X(\lambda)$: Which one is the largest ? How do you interpret this fact ?
:::

::: {.problem #prob-camii-sms-2-q7 origin="external" source="camii-sms-2-q7"}
Let $Y$ be a random variable with density $f(y;\theta)$ for $y\in\mathcal Y\subseteq\mathbb R^n$ and some $\theta\in\Theta\subseteq\mathbb R^d$, and write $\ell(\theta;Y)$ and $U(\theta;Y)$ for the corresponding log-likelihood and score functions.

(a) Assume that the order of differentiation with respect to a component of $\theta$ and integration over $\mathcal Y$ may be interchanged where necessary. Show that, for $r,s=1,\dots,d$,
$$\operatorname{Cov}_\theta\{U_r(\theta;Y),U_s(\theta;Y)\}=-\mathbb E_\theta\Bigl\{\frac{\partial^2}{\partial\theta_r\partial\theta_s}\ell(\theta;Y)\Bigr\}.$$

(b) Let $I(\theta)$ denote the Fisher information matrix with $(r,s)$-entry given by the above expression. Let $\hat\theta$ be the maximum likelihood estimator of $\theta$ using an i.i.d. sample $Y_1,\dots,Y_n\sim f(y;\theta)$. By using the Taylor expansion for $U(\hat\theta;Y)$ at $\hat\theta=\theta$, sketch an argument that shows
$$\sqrt n(\hat\theta-\theta)\xrightarrow{d}N(0,I(\theta)^{-1})\quad\text{as }n\to\infty.$$
:::

::: {.problem #prob-camii-sms-2-q8 origin="external" source="camii-sms-2-q8"}
In the normal linear model, find the Fisher information matrix for the parameters $(\beta,\sigma^2)$. Assume $X^{\mathsf T}X/n\to\Sigma$. Use the result in the last Question to obtain the asymptotic covariance matrix of $(\hat\beta,\hat\sigma^2)$ and show that it is indeed the limit of the exact covariance matrix of $(\hat\beta,\hat\sigma^2)$.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::

::: {.problem #prob-camii-sms-3-q3 origin="external" source="camii-sms-3-q3"}
Suppose $Y_1,\dots,Y_n$ is an i.i.d. sample from $N(\mu,1)$. What is the asymptotic distribution of the maximum likelihood estimator of $\mathbb P(Y_1<0)$?
:::
