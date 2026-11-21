::: {.problem #prob-mit18650f16-8-q3 origin="external" source="mit18650f16-8-q3"}
Logistic regression

Consider independent random pairs $(\mathbf X_1,Y_1),\dots,(\mathbf X_n,Y_n)$, such that:

- $Y_i\in\{0,1\}$ is a binary variable,
- $\mathbf X_i\in\mathbb{R}^p$,
- $\ln\dfrac{P[Y_i=1\mid\mathbf X_i]}{P[Y_i=0\mid\mathbf X_i]}=\mathbf X_i'\beta$, for some $\beta\in\mathbb{R}^p$.

For the sake of simplicity, we assume that $\mathbf X_1$ has a density, that is unknown. We denote it by $f$.

1. Compute $P[Y_i=1\mid\mathbf X_i]$ (for $i=1,\dots,n$).

2. Write the likelihood of the model in terms of $\beta$ and $f$.

3. Show that the maximum likelihood estimator of $\beta$ does not depend on the unknown density $f$.

Remark: In practice, there is no closed form for the maximum likelihood estimator, but there are some algorithms that allow to approach it.
:::

::: {.problem #prob-mit18650f16-11-q3 origin="external" source="mit18650f16-11-q3"}
Linear model with latent variables

Consider the linear regression
$$Y=X'\beta+\varepsilon,$$
where $\beta\in\mathbb{R}^p$ is the unknown parameter, $X\in\mathbb{R}^p$ is the vector or explanatory variables and, $Y\in\mathbb{R}$ is the response variable and $\varepsilon\in\mathbb{R}$ is the error term. Assume that $\varepsilon$ and $X$ are independent and let $F$ be the cdf of $\varepsilon$.

Let $(X_1,Y_1),\dots,(X_n,Y_n)$ be a sample of i.i.d. copies of $(X,Y)$. Assume that for each observation, $X_i$ is observed but $Y_i$ is not observed. Instead, what is observed is
$$Z_i=\mathbf 1_{Y_i\ge0} .$$
The random variables $Y_i$ are called latent variables because they are not observed and the observed sample is $(X_1,Z_1),\dots,(X_n,Z_n)$.

1. Conditional on $X_1$, what is the distribution of $Z_1$ ?

2. Write the link function in terms of $F$.

3. If $\varepsilon$ is standard Gaussian, prove that the link function is $\Phi^{-1}$, where $\Phi$ is the cdf of $N(0,1)$. What is the name of the model in that case ?

4. Assume that the density of $\varepsilon$ is the logistic function:
$$f(t)=\frac{e^{-t}}{(1+e^{-t})^2},\quad t\in\mathbb{R} .$$

   a) Compute $F(t)$, for $t\in\mathbb{R}$.

   b) Compute the link function.

   c) What is the name of the model in that case ?

*Note (these notes):* The handout says that an earlier version had a typo in the logistic function of Question 4; the density here is the posted one. In Question 3, "$e$" in the handout stands for the error $\varepsilon$.
:::
