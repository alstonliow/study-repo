::: {.problem #prob-camii-sms-3-q11 origin="external" source="camii-sms-3-q11"}
Consider a generalised linear model with vector of responses $Y=(Y_1,\dots,Y_n)^{\mathsf T}$ and design matrix $X$ with $i$th row $X_i^{\mathsf T}$. Write $\hat\mu_i=g^{-1}(X_i^{\mathsf T}\hat\beta)$ where $\hat\beta$ is the maximum likelihood estimate of the vector of regression coefficients. Show that if the link function $g$ is the canonical link, the dispersion parameter $\sigma^2=1$, and the weight $w_i=1$, then
$$X^{\mathsf T}Y=X^{\mathsf T}\hat\mu.$$
Conclude that if an intercept term is included in $X$, then
$$\sum_{i=1}^n\hat\mu_i=\sum_{i=1}^nY_i.$$
:::

::: {.problem #prob-camii-sms-4-q2 origin="external" source="camii-sms-4-q2"}
Let $Y_1,\dots,Y_n$ be independent with $Y_i\sim N(\mu_i,\sigma^2)$ and $\mu_i=X_i^{\mathsf T}\beta$, for $i=1,\dots,n$. Show that only one iteration of the Fisher scoring method is required to attain the maximum likelihood estimator $\hat\beta$, regardless of the initial values for the algorithm. What feature of the log-likelihood function ensures that this is the case?
:::

::: {.problem #prob-camii-sms-4-q3 origin="external" source="camii-sms-4-q3"}
Let the design matrix $X$ have $i$th row $X_i^{\mathsf T}$ for $i=1,\dots,n$. Consider the generalized linear model for data $(X_1^{\mathsf T},Y_1),\dots,(X_n^{\mathsf T},Y_n)$ with link function $g(\cdot)$ and dispersion parameter $\sigma_i^2=\sigma^2/w_i$ for observation $i$, where $w_1,\dots,w_n$ are given data weights.

(a) Use the chain rule to show that the score equations for $\beta$ may be written as
$$\sum_{i=1}^n\frac{(Y_i-\mu_i)X_{ir}}{\operatorname{Var}_{\beta,\sigma^2}(Y_i)\cdot g'(\mu_i)}=0,\qquad r=1,\dots,p,$$
where $\operatorname{Var}_{\beta,\sigma^2}(Y_i)$ is the variance of $Y_i$ in the exponential dispersion family with mean parameter $\mu_i=g^{-1}(X_i^{\mathsf T}\beta)$ and dispersion parameter $\sigma_i^2$.

(b) Show that the Fisher information matrix for the parameters $(\beta,\sigma^2)$ takes the block-diagonal form
$$I(\beta,\sigma^2)=\begin{pmatrix}I_{\beta\beta}(\beta,\sigma^2)&0\\0&I_{\sigma^2\sigma^2}(\beta,\sigma^2)\end{pmatrix},$$
where $I_{\beta\beta}(\beta,\sigma^2)$ is a $p\times p$ matrix. Show that $I_{\beta\beta}(\beta,\sigma^2)$ can be expressed as $\sigma^{-2}X^{\mathsf T}WX$ where $W$ is a diagonal matrix in which the $i$-th diagonal entry of $W$ depends on $w_i$ and $\mu_i$. (You need not specify $I_{\sigma^2\sigma^2}(\beta,\sigma^2)$, and you may assume $\partial^2\ell/\partial\beta_j\partial\sigma^2=\partial^2\ell/\partial\sigma^2\partial\beta_j$ for all $j$).

(c) Suppose the link function $g$ is canonical. How do the expressions in (a) and (b) simplify in this case? Show that the observed information matrix of $\beta$ (the $(\beta,\beta)$-block in the Hessian matrix of the log-likelihood function) is non-random given $X$, and use this to conclude that the Newton–Raphson algorithm is equivalent to the Fisher scoring algorithm when the link function is canonical.
:::

::: {.problem #prob-camii-sms-4-q8 origin="external" source="camii-sms-4-q8"}
(Long Tripos 2005/4/13I)

(a) Suppose that $Y_1,\dots,Y_n$ are independent random variables, and that $Y_i$ has probability density function
$$f(y_i\mid\beta,\nu)=\frac{\nu^\nu y_i^{\nu-1}}{\mu_i^\nu\,\Gamma(\nu)}\,e^{-y_i\nu/\mu_i}\qquad\text{for }y_i>0$$
where
$$1/\mu_i=\beta^{\mathsf T}x_i,\qquad\text{for }1\le i\le n,$$
and $x_1,\dots,x_n$ are given $p$-dimensional vectors, and $\nu$ is known. Show that $\mathbb E(Y_i)=\mu_i$ and that $\operatorname{var}(Y_i)=\mu_i^2/\nu$.

(b) Find the score equation for $\hat\beta$, the maximum likelihood estimator of $\beta$, and suggest an iterative scheme for its solution.

(c) If $p=2$, and $x_i=\binom1{z_i}$, find the large-sample distribution of $\hat\beta_2$. Write your answer in terms of $a$, $b$, $c$ and $\nu$, where $a,b,c$ are defined by
$$a=\sum\mu_i^2,\qquad b=\sum z_i\mu_i^2,\qquad c=\sum z_i^2\mu_i^2.$$

*Note (these notes):* The printed sheet says $Y_1$ instead of $Y_i$ in part (a).
:::
