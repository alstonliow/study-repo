::: {.problem #prob-mit18650f16-8-q1 origin="external" source="mit18650f16-8-q1"}
Heteroscedastic regression

Let the characteristics $(X_i,y_i)$ of $n$ individuals ($i=1,\dots,n$) be observed, where $y_i\in\mathbb{R}$ is the dependent variable and $X_i\in\mathbb{R}^p$ is the vector of deterministic explanatory variables. Our goal is to estimate the coefficients of $\beta=(\beta_1,\dots,\beta_p)'$ in the linear regression:
$$y_i=X_i'\beta+\varepsilon_i,\quad i=1,\dots,n .$$
We assume that the model is heteroscedastic, i.e., the error terms $\varepsilon_i$ are not i.i.d.. In this exercise, we are interested in the case where the vector $\varepsilon=(\varepsilon_1,\dots,\varepsilon_n)'$ is Gaussian, centered, with known covariance matrix $\Sigma$ and we assume that $\Sigma$ is invertible. We denote by $\mathbb X$ the matrix in $\mathbb{R}^{n\times p}$ whose rows are $X_1',\dots,X_n'$ and by $Y$ the vector with coordinates $y_1,\dots,y_n$.

Consider the estimator $\hat\beta$ that minimises
$$(Y-\mathbb X\beta)'\Sigma^{-1}(Y-\mathbb X\beta),$$
over $\beta\in\mathbb{R}^p$.

1. Show that in the homoscedastic case, i.e., when $\Sigma=\sigma^2I_n$ for some $\sigma^2>0$, $\hat\beta$ reduces the least square error estimator.

2. Prove that $\hat\beta$ is equal to the maximum likelihood estimator.

3. Propose a sufficient condition on the matrix $\mathbb X$ for $\hat\beta$ to be uniquely defined.

4. From now on, we assume that the previous condition is satisfied. Compute $\hat\beta$. What is the distribution of $\hat\beta$ ?

5. Compute the bias and the quadratic risk of $\hat\beta$.
:::

::: {.problem #prob-mit18650f16-8-q2 origin="external" source="mit18650f16-8-q2"}
Linear regression with random design

Consider $n$ i.i.d. pairs of random variables $(\mathbf X_i,Y_i)$, $i=1,\dots,n$, where $\mathbf X_i\in\mathbb{R}^p$ ($p\ge1$) and $Y_i\in\mathbb{R}$. For each $i$, write
$$Y_i=\mathbf X_i'\beta+\varepsilon_i,$$
where $E[\varepsilon_i]=0$, $\operatorname{cov}(\mathbf X_i,\varepsilon_i)=0$ and $\beta\in\mathbb{R}^p$ is an unknown vector, that we want to estimate. In Questions 1,2 and 3, we assume that for all $x\in\mathbb{R}^p$, $\varepsilon_1$ has a conditional density given $\mathbf X_1=x$, denoted by $f_x$ and that $\mathbf X_1$ has a density, which we denote by $g$.

1. Write the likelihood in terms of the unknown parameter $\beta$, $f_x$ and $g$.

2. Show that the maximum likelihood estimator of $\beta$ does not depend on $g$, which may be unknown.

3. Assume that $\varepsilon_1$ is independent of $\mathbf X_1$ and that $\varepsilon_1\sim N(0,\sigma^2)$.

   a) Compute $f_x$, for $x\in\mathbb{R}^p$.

   b) Since the $\mathbf X_i$'s are independent continuous random vectors of size $p$, it is possible to prove that the rank of the family $\{\mathbf X_1,\dots,\mathbf X_n\}$ is equal to $p$ almost surely. Here, we use this result without proving it.

   Show that the maximum likelihood estimator of $\beta$ is equal to the least square error estimator and compute it.

   c) Conditionally on the $\mathbf X_i$'s, what is the distribution of the MLE ?

   d) Is the MLE biased ?

   Hint: First compute its expectation conditionally on the $\mathbf X_i$'s.

   e) What is the maximum likelihood estimator of $\sigma^2$ ?

   f) Propose an unbiased estimator $\hat\sigma^2$ of $\sigma^2$. What is the conditional distribution of $\dfrac{(n-p)\hat\sigma^2}{\sigma^2}$ given the $\mathbf X_i$'s ?

4. Assume that $p=2$ and $\mathbf X_i=(1,X_i)$, $i=1,\dots,n$, where $X_i$ is a random variable with finite, non zero variance. Of course, we no longer assume that $X_1$ has a density. Denote $\beta=(a,b)$, so:
$$Y_i=a+bX_i+\varepsilon_i,\quad i=1,\dots,n .$$

   a) Recall the least square estimator $(\hat a,\hat b)$ of $(a,b)$.

   b) Prove that it is consistent.

   c) Assume that $X_1$ and $\varepsilon$ are independent, and denote by $\sigma^2$ the variance of $\varepsilon_1$. Show that $(\hat a,\hat b)$ is asymptotically normal, and compute its asymptotic covariance matrix in terms of $\sigma^2$ and the moments of $X_1$.

   d) Propose a test with asymptotic level at most $\alpha\in(0,1)$ for the null hypothesis $H_0$: "$b>0$" (the moments of $X_1$ and $\sigma^2$ are not known).
:::

::: {.problem #prob-camii-sms-1-q6 origin="external" source="camii-sms-1-q6"}
Data are available on weights of two groups of three rats at the beginning of a fortnight and at its end. During the fortnight, one group was fed normally, and the other was given a growth inhibitor. The weights of the $k$th rat in the $j$th group before and after the fortnight are $X_{jk}$ and $Y_{jk}$ respectively. It is assumed that $Y_{jk}=\alpha_j+\beta_jX_{jk}+\varepsilon_{jk}$ where $\varepsilon_{jk}$, $j=1,2$, $k=1,2,3$ are independent normally distributed noise with mean $0$ and unknown variance.

(a) Let $W$ be the vector of responses, so $W=(Y_{11},Y_{12},Y_{13},Y_{21},Y_{22},Y_{23})^{\mathsf T}$, and similarly let $\delta$ be the vector of random errors. Write down the model above in the form $W=A\theta+\delta$, giving the design matrix $A$ explicitly and expressing the vector of parameters $\theta$ in terms of the $\alpha_j$ and $\beta_j$.

(b) The model is to be reparametrised in such a way that it can be specialised to (i) two parallel lines for the two groups, (ii) two lines with the same intercept, (iii) one common line for both groups, just by setting parameters to zero. Give one design matrix that can be made to correspond to (i), (ii) and (iii), just by dropping columns, specifying which columns are to be dropped for which cases.
:::

::: {.problem #prob-camii-sms-1-q10 origin="external" source="camii-sms-1-q10"}
Consider the normal linear model with a fixed design matrix $X$. Suppose only the first $p_0$ components of $\beta$ are non-zero. Show that
$$\operatorname{Var}(\hat\beta_{0,j})\le\operatorname{Var}(\hat\beta_j)\quad\text{for }j=1,\dots,p_0.$$
Here $\hat\beta_{0,j}$ denotes the $j$th component of $\hat\beta_0$. Hint: Use the partial regression characterisation of $\hat\beta_j$.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::

::: {.problem #prob-camii-sms-2-q1 origin="external" source="camii-sms-2-q1"}
Suppose we reparametrise the normal linear model $Y=X\beta+\varepsilon$ by letting $\theta=A\beta$ where $A\in\mathbb R^{p\times p}$ is invertible and known, so now we have $Y=XA^{-1}\theta+\varepsilon$ (with $XA^{-1}$ being the new model matrix). Show that the fitted values and predictions based on applying OLS in the reparametrised model will be identical to those in the original model.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::
