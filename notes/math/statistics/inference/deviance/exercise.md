::: {.problem #prob-camii-sms-3-q7 origin="external" source="camii-sms-3-q7"}
Suppose $Y_1,\dots,Y_n$ is an i.i.d. sample from a regular exponential family with natural parameter $\theta\in\Theta\subseteq\mathbb R$ (regular means $\Theta$ is open), sufficient statistic $T(y)=y$, cumulant function $K(\theta)$, mean parameter $\mu=\mu(\theta)$, and variance $V(\theta)>0$.

(a) Show that the distribution of $\bar Y=\sum_{i=1}^nY_i/n$ is in an exponential family with natural parameter $\theta^{(n)}=n\theta$ and cumulant function $K^{(n)}(\theta^{(n)})=nK(\theta^{(n)}/n)$. What is the mean and variance of $\bar Y$? Hint: What is the joint density of $Y_1,\dots,Y_n$?

(b) The deviance of $\theta_1$ from $\theta_2$ is defined as
$$D(\theta_1,\theta_2)=2\mathbb E_{\theta_1}\Bigl\{\log\frac{f(Y;\theta_1)}{f(Y;\theta_2)}\Bigr\}.$$
Show that the deviance in the exponential family for $\bar Y$ of natural parameter $\theta_1^{(n)}=n\theta_1$ from $\theta_2^{(n)}=n\theta_2$ is $nD(\theta_1,\theta_2)$. Denote this as $D^{(n)}(\theta_1,\theta_2)$.

(c) Show likelihood ratio statistic for testing $H_0:\theta=\theta_0$ versus $H_1:\theta\neq\theta_0$, after a monotone transformation, is given by $D^{(n)}(\hat\theta,\theta_0)$. What is the limiting distribution of this statistic when $n\to\infty$? Justify your answer using the approximation $D(\theta_1,\theta_2)\approx I^{(1)}(\theta_2)(\theta_1-\theta_2)^2$ when $\theta_1\approx\theta_2$, where $I^{(1)}(\theta_2)$ is the Fisher information of one observation from the distribution $f(\cdot;\theta_2)$.

(d) With an abuse of notation, we also denote $D(\theta_1,\theta_2)$ as $D(\mu_1,\mu_2)$ where $\mu_1$ and $\mu_2$ are the mean parameters corresponding to $\theta_1$ and $\theta_2$ in the exponential family. Similarly, $D^{(n)}(\mu_1,\mu_2)=nD(\mu_1,\mu_2)$. The deviance residual is defined as
$$R=\operatorname{sign}(\bar Y-\mu)\cdot\sqrt{D^{(n)}(\bar Y,\mu)}.$$
What is the limiting distribution of $R$ when $n\to\infty$?
:::
