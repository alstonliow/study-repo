::: {.problem #prob-camii-sms-3-q6 origin="external" source="camii-sms-3-q6"}
Suppose $\mu\sim\pi(\cdot)$ where $\pi(\cdot)$ is an unknown density function on $\mathbb R$. Suppose $Y\mid\mu\sim N(\mu,\sigma^2)$ and $\sigma^2$ is known. Derive Tweedie's formula
$$\mathbb E(\mu\mid Y)=Y+\sigma^2\cdot\frac{f'(Y)}{f(Y)},$$
where $f(y)=\int\pi(\mu)f(y;\mu,\sigma^2)\,d\mu$ is the marginal density of $Y$, and $f(y;\mu,\sigma^2)$ is the density of $N(\mu,\sigma^2)$. Hint: The posterior distribution of $\theta$ given $Y$ is an exponential family.
:::
