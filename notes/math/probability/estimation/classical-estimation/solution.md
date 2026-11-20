<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6041f10-11-q1" status="draft"}
1. The log-likelihood of $\lambda$ is $\sum_i\bigl(x_i\ln\lambda-\lambda-\ln x_i!\bigr)$, with derivative $\frac{\sum_ix_i}\lambda-n$.

2. It vanishes at $\hat\lambda_n=\frac1n\sum_ix_i$, the sample mean, and the log-likelihood is concave in $\lambda$, so this is the maximum (if all $x_i=0$ the maximum is at $\lambda=0$, which the formula also gives).

3. $E[\hat\Lambda_n]=\lambda$, so it is unbiased; $\mathrm{Var}(\hat\Lambda_n)=\lambda/n\to0$, so it is consistent by the weak law of large numbers (@exm-sample-mean-estimator).
:::

::: {.solution for="prob-mit6041f10-11-q3" status="draft"}
(a) The likelihood is $\prod_iq(1-q)^{t_i-1}=q^k(1-q)^{s-k}$ with $s=t_1+\dots+t_k$, maximised at $\hat q_k=\frac ks$. It is the MAP estimate under the uniform prior of problem set 10, as noted after @def-maximum-likelihood.

(b) $\frac1{\hat Q_k}=\frac{T_1+\dots+T_k}k$ is the sample mean of independent $\mathrm{Geom}(q^*)$ variables with mean $\frac1{q^*}$ and finite variance, so it converges to $\frac1{q^*}$ in probability by the weak law of large numbers.

(c) $\mathrm{Var}(T_i)=\frac{1-q^*}{(q^*)^2}$, which for $q^*\in[0.5,1]$ is at most $2$ (its value at $q^*=0.5$). Chebyshev's inequality gives
$$\Pr\Bigl(\Bigl|\frac1{\hat Q_k}-\frac1{q^*}\Bigr|>0.1\Bigr)\le\frac{2}{k\cdot0.01}=\frac{200}k,$$
which is at most $0.05$ once $k\ge4000$. (A normal approximation would suggest about $1.96^2\cdot2/0.01\approx769$, but it is not a guarantee.)
:::

::: {.solution for="prob-mit6041f10-11-q4" status="draft"}
Write $r=e^{-1/\theta}\in(0,1)$, so $p_K(k;\theta)=r^k/Z(\theta)$: $K$ counts failures before the first success in trials with success probability $1-r$.

(a) $Z(\theta)=\sum_{k\ge0}r^k=\frac1{1-e^{-1/\theta}}$.

(b) $\mu_K=\frac r{1-r}=\frac1{e^{1/\theta}-1}$ and $\sigma_K^2=\frac r{(1-r)^2}=\frac{e^{1/\theta}}{(e^{1/\theta}-1)^2}$.

(c) The log-likelihood is $-\frac{ns_n}\theta+n\ln\bigl(1-e^{-1/\theta}\bigr)$. Its derivative in $\theta$ is $\frac n{\theta^2}\bigl(s_n-\frac1{e^{1/\theta}-1}\bigr)$, which vanishes when $\mu_K(\theta)=s_n$:
$$\hat\theta_n=\frac1{\ln(1+1/s_n)}\approx s_n\quad(\theta\gg1).$$

(d) $\frac{\sigma_{\hat K}}{\mu_{\hat K}}=\frac{\sigma_K}{\sqrt n\,\mu_K}=\frac1{\sqrt{nr}}\approx\frac1{\sqrt n}$ for $\theta\gg1$. This equals $0.01$ for $n\approx10^4$ (exactly $n=10^4e^{1/\theta}$).

(e) By the central limit theorem $\hat K$ is approximately normal with standard deviation $\sigma_{\hat K}=0.01\,\mu_K$. Estimating $\mu_K$ by $\hat K$, an approximate $95\%$ interval is
$$\bigl[\hat K(1-0.0196),\ \hat K(1+0.0196)\bigr].$$
:::

::: {.solution for="prob-mit6041f10-11-q5" status="draft"}
(a) The sample mean is $2340/1000=2.34$ and its standard deviation is at most $2/\sqrt{1000}\approx0.063$. As in @exm-confidence-interval-mean, an approximate $95\%$ interval is $2.34\pm1.96\cdot0.063$, that is $[2.216,\,2.464]$.

(b) By @exm-ml-exponential, $\hat\theta=\frac n{\sum_iw_i}=\frac{1000}{2340}\approx0.427$. Only the total weight is needed.
:::

::: {.solution for="prob-mit6041f10-11-q6" status="draft"}
With independent normal noise of fixed variance, the log-likelihood is a constant minus $\frac1{2\sigma^2}\sum_i(y_i-\text{model}_i)^2$, so the ML estimates are the least squares estimates (@thm-least-squares-normal-equations): for a model $y\approx a+bz$, $\hat b=\frac{\sum_i(z_i-\bar z)(y_i-\bar y)}{\sum_i(z_i-\bar z)^2}$ and $\hat a=\bar y-\hat b\bar z$.

(a) With $z_i=x_i$: $\bar x=4.94$, $\bar y=134.38$, giving $\hat\theta_1\approx40.53$ and $\hat\theta_0\approx-65.86$.

(b) With $z_i=x_i^2$: $\hat\beta_1\approx4.091$ and $\hat\beta_0\approx-3.07$. The quadratic model fits these data far better.
:::

::: {.solution for="prob-mit1805s22-6-q1" status="draft"}
1. With $S=\sum x_i$ and $P=\prod x_i$, the likelihood is $\dfrac{a^{5m}}{(4!)^m}P^4e^{-aS}$, and the log-likelihood is $5m\ln a-aS+\text{const}$.

2. Its derivative $\frac{5m}a-S$ vanishes at $a=\frac{5m}S$; the second derivative $-\frac{5m}{a^2}$ is negative, so this is the maximum.

3. $\hat a=\dfrac{5m}{x_1+\dots+x_m}=\dfrac5{\bar x}$.
:::

::: {.solution for="prob-mit1805s22-6-q3" status="draft"}
(b) first. The likelihood is $\prod_i\frac1{b-a}=(b-a)^{-n}$ if every $x_i\in[a,b]$, and $0$ otherwise. It is positive only when $a\le\min_ix_i$ and $b\ge\max_ix_i$, and there it increases as $b-a$ shrinks. So it is largest at
$$\hat a=\min_ix_i,\qquad\hat b=\max_ix_i .$$

(a) Hence $\hat a=1.2$ and $\hat b=10.5$.
:::
