::: {.problem #prob-camii-sms-4-q6 origin="external" source="camii-sms-4-q6"}
For an exponential family of distributions $\{f(\cdot;\theta)\mid\theta\in\Theta\subseteq\mathbb R\}$, the deviance of $\theta_1\in\Theta$ from $\theta_2\in\Theta$ is defined as $D(\theta_1,\theta_2)=2\mathbb E_{\theta_1}\{\log f(Y;\theta_1)-\log f(Y;\theta_2)\}$, where $\mathbb E_{\theta_1}$ means the expectation is taken over $Y\sim f(\cdot;\theta_1)$. With an abuse of notation, we often use the mean value parametrisation $\mu_1=\mathbb E_{\theta_1}(Y)$, $\mu_2=\mathbb E_{\theta_2}(Y)$ and write $D(\theta_1,\theta_2)$ as $D(\mu_1,\mu_2)$.

(a) Show that $D(\theta_1,\theta_2)=2\{(\theta_1-\theta_2)\mu_1-K(\theta_1)+K(\theta_2)\}$, where $K(\cdot)$ is the cumulant function of the exponential family. How does this formula change when we include a dispersion parameter in the distribution?

(b) When $\mu=(\mu_1,\dots,\mu_n)$ and $\tilde\mu=(\tilde\mu_1,\dots,\tilde\mu_n)$ are vectors, the total deviance of $\mu$ from $\tilde\mu$ is defined as $D^{(n)}(\mu,\tilde\mu)=\sum_{i=1}^nD(\mu_i,\tilde\mu_i)$. Consider the normal linear model: let $Y_1,\dots,Y_n$ be independent with $Y_i\sim N(\mu_i,1)$ and $\mu_i=X_i^{\mathsf T}\beta$, for $i=1,\dots,n$. Show that the total deviance of $Y$ from the maximum likelihood estimator of $\mu$ is equal to the residual sum of squares.

(c) Consider a generalized linear model as set up in Question 3 with the canonical link function. Show that the maximum likelihood estimator of $\beta$ is given by $\hat\beta=\operatorname*{arg\,min}_\beta D^{(n)}(Y,\mu)$ where $\mu_i$ is the mean parameter corresponding to the natural parameter $\theta_i=X_i^{\mathsf T}\beta$.

(d) In the same setting, consider a partitioning $X=(X_0,X_1)$, $\beta=(\beta_0^{\mathsf T},\beta_1^{\mathsf T})^{\mathsf T}$ where $X_0\in\mathbb R^{n\times p_0}$, $X_1\in\mathbb R^{n\times(p-p_0)}$, $\beta_0\in\mathbb R^{p_0}$, and $\beta_1\in\mathbb R^{p-p_0}$. Let $\hat\mu$ and $\hat\mu_0$ be the maximum likelihood estimator of $\mu$ under the model $\theta=X\beta$ and $\theta=X_0\beta$. Show that $D^+(Y,\hat\mu_0)=D^+(Y,\hat\mu)+D^+(\hat\mu,\hat\mu_0)$. Hint: By using the score equation for $\hat\beta$, show that $D^+(\hat\mu,\hat\mu_0)=2\{\ell(\hat\mu)-\ell(\hat\mu_0)\}$ where $\ell(\mu)$ is the log-likelihood function for mean $\mu$. Then consider a special choice of $X$.

(e) Do the conclusions in (c) and (d) still hold if we use a non-canonical link function?

*Note (these notes):* Question 3 of the sheet is the set-up of a GLM with link $g$ and weights $w_i$ (see question 3 of sheet 4 in the notes); $D^+$ denotes the total deviance $D^{(n)}$.
:::
