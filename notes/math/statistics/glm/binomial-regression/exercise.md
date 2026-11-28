::: {.problem #prob-camii-sms-4-q1 origin="external" source="camii-sms-4-q1"}
Show that the log-likelihood for binomial regression with data $(y_1,x_1),\dots,(y_n,x_n)\in\{0,1\}\times\mathbb R^p$ when the response is binary and the canonical link function is used can be written as
$$-\sum_{i=1}^n\log\bigl(1+\exp(-\tilde Y_iX_i^{\mathsf T}\beta)\bigr),$$
where $\tilde Y_i=2Y_i-1$.
:::

::: {.problem #prob-camii-sms-4-q4 origin="external" source="camii-sms-4-q4"}
Suppose that for some strictly increasing function $f$, we have
$$Y_i^*=f(X_i^{\mathsf T}\beta^*+\varepsilon_i),\qquad i=1,\dots,n,$$
where $\varepsilon\sim N_n(0,\sigma^2I)$, and the $X_i$ are covariates in $\mathbb R^p$ with first component equal to 1. Suppose that for some constant $c$, we observe
$$Y_i:=\mathbf 1_{\{Y_i^*>c\}}.$$
Show that $Y_1,\dots,Y_n$ are independent and
$$\mathbb E(Y_i)=\Phi(X_i^{\mathsf T}\beta)$$
for some $\beta$ that you should specify, where $\Phi$ is the c.d.f. of the standard normal distribution. This is often called the probit regression model.
:::

::: {.problem #prob-camii-sms-4-q7 origin="external" source="camii-sms-4-q7"}
You see below the results of using `glm` to analyse data from Agresti (1996) on tennis matches between 5 top women tennis players (1989–90). We let $Y_{ij}$ be the number of wins of player $i$ against player $j$, and let $n_{ij}$ be the total number of matches of $i$ against $j$, for $1\le i<j\le5$. Thus we have 10 observations, which we will assume are realisations of independent binomial random variables $Y_{ij}$ with
$$Y_{ij}\sim\mathrm{Bin}(n_{ij},\mu_{ij})$$
and
$$\log\Bigl(\frac{\mu_{ij}}{1-\mu_{ij}}\Bigr)=\alpha_i-\alpha_j.$$
This is known as the Bradley–Terry model and the parameter $\alpha_i$ represents the quality of player $i$. The data are tabulated in R as follows

```
  wins tot sel graf saba navr sanc
     2   5   1   -1    0    0    0
     1   1   1    0   -1    0    0
     3   6   1    0    0   -1    0
     2   2   1    0    0    0   -1
     6   9   0    1   -1    0    0
     3   3   0    1    0   -1    0
     7   8   0    1    0    0   -1
     1   3   0    0    1   -1    0
     3   5   0    0    1    0   -1
     3   4   0    0    0    1   -1
```

Thus for example, the first row tells us that Seles played Graf five times and won on two occasions. We perform the following R commands (the output has been slightly abbreviated).

```
> fit <- glm(wins/tot ~ sel + graf + saba + navr - 1, binomial, weights=tot)
> summary(fit, correlation=TRUE)
Coefficients:
     Estimate Std. Error z value Pr(>|z|)
sel    1.5331     0.7871   1.948  0.05142 .
graf   1.9328     0.6784   2.849  0.00438 **
saba   0.7309     0.6771   1.079  0.28042
navr   1.0875     0.7237   1.503  0.13289
---
    Null deviance: 16.1882  on 10  degrees of freedom
Residual deviance:  4.6493  on  6  degrees of freedom
Correlation of Coefficients:
     sel  graf saba
graf 0.59
saba 0.46 0.60
navr 0.63 0.54 0.49
```

(a) What is the meaning of the `-1` in the model formula and why do you think it was included?

(b) Why is Sánchez (`sanc`) not included in the model formula?

(c) Can we confidently (at the $5\%$ level) say that Graf is better than Sánchez?

(d) Can we confidently (at the $5\%$ level) say that Graf is better than Seles? [Use the correlation matrix and a calculator or R, writing out your calculations. $\mathbb P(Z\le1.64)\approx0.95$ when $Z\sim N(0,1)$.]

(e) What is your estimate of the probability that Sabatini (`saba`) beats Sánchez, in a single match? Give a $95\%$ confidence interval for this probability. [Use a calculator or R. $\mathbb P(Z\le1.96)\approx0.975$ when $Z\sim N(0,1)$.]
:::

::: {.problem #prob-camii-sms-4-q9 origin="external" source="camii-sms-4-q9"}
We wish to study how various explanatory variables may contribute to the development of asthma in children. One way to do this would be to randomly select $n$ newborn babies and then study them for the first 5 years, measuring the values of the relevant covariates and noting down whether they develop asthma or not within the study period. However, this sort of experiment may be too expensive to carry out, and instead, we acquire the medical records of some children who developed asthma within the first five years of their life, and some children who did not. Luckily the medical records contain all the covariates we intended to measure.

We can imagine that the records we obtain are a sample from a large collection of data
$$(Y_1,X_1),\dots,(Y_N,X_N)\in\{0,1\}\times\mathbb R^p,$$
where each $Y_i$ indicates the development of asthma and can be considered as a realisation of a Bernoulli random variable $Y_i$ with $\pi_i:=\mathbb P(Y_i=1)\in(0,1)$,
$$\log\Bigl(\frac{\pi_i}{1-\pi_i}\Bigr)=\alpha+X_i^{\mathsf T}\beta,$$
and all the $Y_i$ are independent. Let $Z_i$ indicate whether $(Y_i,X_i)$ is in our sample: 1 if it is, 0 if not. Suppose that for all $i=1,\dots,N$,
$$\mathbb P(Z_i=1\mid Y_i=1)=p_1,\qquad\text{and}\qquad\mathbb P(Z_i=1\mid Y_i=0)=p_0,$$
where $p_1,p_0>0$ are unknown, and further that the $(Y_i,Z_i)$ are all independent. Show that
$$\frac{\mathbb P(Y_i=1\mid Z_i=1)}{1-\mathbb P(Y_i=1\mid Z_i=1)}=\frac{p_1}{p_0}\exp(\alpha+X_i^{\mathsf T}\beta).$$
Conclude that it is possible to estimate $\beta$ from our medical records data, but not $\alpha$.
:::
