<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-4-q2" status="draft"}
Write $\hat m_1=\bar X_n$ and $\hat m_2=\frac1n\sum_iX_i^2$, and $\hat s^2=\hat m_2-\hat m_1^2$ (the empirical variance).

1. Bernoulli: $m_1=p$, so $\hat p=\bar X_n$.

2. Poisson: $m_1=\lambda$, so $\hat\lambda=\bar X_n$.

3. Exponential: $m_1=1/\lambda$, so $\hat\lambda=1/\bar X_n$.

4. Gaussian: $m_1=\mu$, $m_2=\sigma^2+\mu^2$, so $\hat\mu=\bar X_n$ and $\hat\sigma^2=\hat s^2$.

5. Shifted exponential: $m_1=a+1/\lambda$ and the variance is $1/\lambda^2$, so $\hat\lambda=1/\hat s$ and $\hat a=\bar X_n-\hat s$.

6. Log-normal: $m_1=e^{\mu+\sigma^2/2}$ and $m_2=e^{2\mu+2\sigma^2}$, so $\ln m_2-2\ln m_1=\sigma^2$. Hence $\hat\sigma^2=\ln\hat m_2-2\ln\hat m_1$ and $\hat\mu=\ln\hat m_1-\hat\sigma^2/2=2\ln\hat m_1-\frac12\ln\hat m_2$.

In parts 1–4 the moment estimators coincide with the MLEs; in parts 5 and 6 they differ.
:::
