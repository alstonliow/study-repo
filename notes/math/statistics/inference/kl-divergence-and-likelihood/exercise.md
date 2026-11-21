::: {.problem #prob-mit18650f16-3-q1 origin="external" source="mit18650f16-3-q1"}
Maximum likelihood estimator

Let $X_1,\dots,X_n$ be $n$ i.i.d. random variables with density $f_\theta$ with respect to the Lebesgue measure. For each case below find the MLE of $\theta$.

1. $f_\theta(x)=\theta\tau^\theta x^{-(\theta+1)}\mathbf 1(x\ge\tau)$, $\theta>0$, where $\tau>0$ is a known constant.

2. $f_\theta(x)=\tau\theta^\tau x^{-(\tau+1)}\mathbf 1(x\ge\theta)$, $\theta>0$, where $\tau>0$ is a known constant.

3. $f_\theta(x)=\sqrt\theta\,x^{\sqrt\theta-1}\mathbf 1(0\le x\le1)$, $\theta>0$

4. $f_\theta(x)=(x/\theta^2)\exp(-x^2/2\theta^2)\mathbf 1(x\ge0)$, $\theta>0$

5. $f_\theta(x)=\theta\tau x^{\tau-1}\exp(-\theta x^\tau)\mathbf 1(x\ge0)$, $\theta>0$, where $\tau>0$ is a known constant.
:::

::: {.problem #prob-mit18650f16-3-q2 origin="external" source="mit18650f16-3-q2"}
Consistency of the maximum likelihood estimator

Let $X_1,\dots,X_n$ be $n$ i.i.d. random variables with distribution $N(\theta,\theta)$, for some unknown $\theta>0$. Compute the maximum likelihood estimator of $\theta$ and show that it is consistent.
:::

::: {.problem #prob-mit18650f16-3-q3 origin="external" source="mit18650f16-3-q3"}
Kullback-Leibler divergence

1. Compute the Kullback-Leibler divergence between $P=N(a,\sigma^2)$ and $Q=N(b,\sigma^2)$ for $a,b\in\mathbb{R}$, $\sigma^2>0$.

2. Compute the Kullback-Leibler divergence between the Bernoulli distributions $P=\operatorname{Ber}(a)$ and $Q=\operatorname{Ber}(b)$ for $a,b\in(0,1)$.
:::

::: {.problem #prob-mit18650f16-3-q4 origin="external" source="mit18650f16-3-q4"}
Total variation distance

1. Compute the total variation between the uniform probability measures on the intervals $[0,s]$ and $[0,t]$, for some given real numbers $s,t$, with $0<s\le t$.

2. If $p$ and $q$ are two numbers in $[0,1]$, compute the total variation distance between $\operatorname{Ber}(p)$ and $\operatorname{Ber}(q)$.

3. If $X_1,\dots,X_n$ are $n$ i.i.d. Bernoulli random variables with some parameter $p\in[0,1]$ and $\bar X_n$ is their empirical average, show that the total variation distance between $\operatorname{Ber}(\bar X_n)$ and $\operatorname{Ber}(p)$ converges to zero in probability.

4. Show that the Poisson distribution with parameter $1/n$ converges in total variation distance to the Dirac distribution at zero (i.e., the distribution of the random variable that is always equal to zero).
:::
