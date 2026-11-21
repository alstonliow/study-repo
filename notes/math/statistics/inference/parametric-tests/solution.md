<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-5-q1" status="draft"}
1. Let $q=q_{\alpha/2}$ be the $(1-\alpha/2)$-quantile of $N(0,1)$. By the central limit theorem $\sqrt n(\bar X_n-\lambda)/\sqrt\lambda\to N(0,1)$, and $\bar X_n\to\lambda$ in probability, so by Slutsky's theorem $\sqrt n(\bar X_n-\lambda)/\sqrt{\bar X_n}\to N(0,1)$ (on the event $\bar X_n>0$, whose probability tends to $1$). Hence
$$I=\Bigl[\bar X_n-q\sqrt{\bar X_n/n},\ \bar X_n+q\sqrt{\bar X_n/n}\Bigr]$$
satisfies $\Pr_\lambda(\lambda\in I)\to\Pr(|Z|\le q)=1-\alpha$ for every $\lambda>0$ (@prp-three-asymptotic-intervals, part 3).

2. Reject $H_0$ when $\lambda_0\notin I$: $\psi=\mathbf 1\{\lambda_0\notin I\}$. Under $H_0$, $\Pr_{\lambda_0}(\psi=1)=1-\Pr_{\lambda_0}(\lambda_0\in I)\to\alpha$, so $\psi$ has asymptotic level $\alpha$ (the duality of @thm-interval-test-duality). Equivalently, $\psi=\mathbf 1\{\sqrt n|\bar X_n-\lambda_0|/\sqrt{\bar X_n}>q\}$, which is Wald's test (@thm-wald-test) since $I(\lambda)=1/\lambda$.
:::

::: {.solution for="prob-mit18650f16-5-q2" status="draft"}
1. $\hat\mu_1=\bar X$, $\hat\sigma_1^2=\frac1{n_1}\sum_i(X_i-\bar X)^2$, and likewise $\hat\mu_2=\bar Y$, $\hat\sigma_2^2=\frac1{n_2}\sum_j(Y_j-\bar Y)^2$ (@exm-ml-normal).

2. By Cochran's theorem (@thm-normal-sample-theory, with $n\hat\sigma^2=(n-1)S^2$), $n_1\hat\sigma_1^2/\sigma_1^2\sim\chi^2_{n_1-1}$ and $n_2\hat\sigma_2^2/\sigma_2^2\sim\chi^2_{n_2-1}$.

3. The two are independent (they come from independent samples), and a sum of independent chi-squares has as degrees of freedom the sum: $\chi^2_{n_1+n_2-2}$.

4. $\hat\mu_1\sim N(\mu_1,\sigma_1^2/n_1)$ and $\hat\mu_2\sim N(\mu_2,\sigma_2^2/n_2)$ are independent, so $\Delta\sim N\bigl(\mu_1-\mu_2,\ \sigma_1^2/n_1+\sigma_2^2/n_2\bigr)$.

5. Let $\sigma^2$ be the common variance. Under $H_0$, $Z=\Delta/\bigl(\sigma\sqrt{1/n_1+1/n_2}\bigr)\sim N(0,1)$, and $V=(n_1\hat\sigma_1^2+n_2\hat\sigma_2^2)/\sigma^2\sim\chi^2_{n_1+n_2-2}$ by part 3. $Z$ is a function of the sample means and $V$ of the sample variances, which are independent (@thm-normal-sample-theory, for each sample). So
$$T=\frac{Z}{\sqrt{V/(n_1+n_2-2)}}=\frac{\hat\mu_1-\hat\mu_2}{\sqrt{\dfrac{n_1\hat\sigma_1^2+n_2\hat\sigma_2^2}{n_1+n_2-2}\Bigl(\dfrac1{n_1}+\dfrac1{n_2}\Bigr)}}\sim t_{n_1+n_2-2}$$
does not involve $\sigma$, and $\psi=\mathbf 1\{|T|>q_{\alpha/2}(t_{n_1+n_2-2})\}$ has level exactly $\alpha$. This is the pooled two-sample $t$-test (@def-two-sample-t-test).

6. Take the sample variances to be the MLEs $\hat\sigma_1^2=0.22$, $\hat\sigma_2^2=0.17$ (the course's convention). Then the pooled variance is $(2.2+1.7)/18\approx0.2167$, the standard error is $\sqrt{0.2167\cdot0.2}\approx0.208$, and $T=0.36/0.208\approx1.73$, against $q_{0.025}(t_{18})\approx2.10$. We do not reject $H_0$; the p-value is $\Pr(|t_{18}|>1.73)\approx0.10$. (With the unbiased convention, variances $0.22$ and $0.17$ with divisor $9$, $T\approx1.82$ and the p-value is $\approx0.085$; the conclusion is the same.) Note that not rejecting does not show that the calibrations are identical: the test only finds no significant evidence of a difference.
:::

::: {.solution for="prob-mit18650f16-5-q3" status="draft"}
1. Let $\theta=(\mu,\sigma^2)$ with MLE $\hat\theta=(\bar X_n,\hat\sigma^2)$. By @thm-mle-asymptotic-normality and the Fisher information of the Gaussian model, $\sqrt n(\hat\theta-\theta)\to N_2\bigl(0,\operatorname{diag}(\sigma^2,2\sigma^4)\bigr)$.

2. Let $g(\mu,\sigma^2)=\mu-\sqrt{\sigma^2}$, so $H_0$ is $g(\theta)>0$. Its gradient is $(1,-1/(2\sigma))$, and by the delta method (@thm-multivariate-delta-method) $\sqrt n(g(\hat\theta)-g(\theta))\to N(0,\Gamma)$ with
$$\Gamma=\sigma^2+\frac{2\sigma^4}{4\sigma^2}=\frac32\sigma^2 .$$

3. Let $T_n=\sqrt n\,\dfrac{\bar X_n-\hat\sigma}{\sqrt{3\hat\sigma^2/2}}$ and reject $H_0$ when $T_n<-1.645$, the $5\%$ quantile of $N(0,1)$. If $\mu>\sigma$, then $T_n\to+\infty$ in probability and the rejection probability tends to $0$; on the boundary $\mu=\sigma$ it tends to $0.05$ by Slutsky's theorem. So the test has asymptotic level $5\%$, and its p-value is $\Phi(T_n)$.

4. *First sample:* $\hat\sigma=\sqrt{5.20}\approx2.280$, $T_n=10\cdot(2.41-2.280)/\sqrt{7.80}\approx0.46$, p-value $\Phi(0.46)\approx0.68$: no evidence against $H_0$.

5. *Second sample:* $\hat\sigma=\sqrt{15.95}\approx3.994$, $T_n=10\cdot(3.28-3.994)/\sqrt{23.93}\approx-1.46$, p-value $\Phi(-1.46)\approx0.072$. We do not reject $H_0$ at level $5\%$ but do reject it at level $10\%$.

(The "sample variance" is taken as the MLE; with divisor $n-1$ the numbers change in the third decimal only.)
:::

::: {.solution for="prob-mit18650f16-6-q1" status="draft"}
The MLE is $\hat\lambda=1/\bar X_n$, with $\sqrt n(\hat\lambda-\lambda)\to N(0,\lambda^2)$ (@exm-delta-method-exponential), so $T_n(\lambda_0)=\sqrt n(\hat\lambda-\lambda_0)/\hat\lambda\to N(0,1)$ under $\lambda=\lambda_0$, by Slutsky's theorem.

1. $\psi=\mathbf 1\{|T_n(\lambda_0)|>q_{\alpha/2}\}$, the Wald test (@thm-wald-test, since $I(\lambda)=1/\lambda^2$), has asymptotic level $\alpha$.

2. $\psi=\mathbf 1\{T_n(\lambda_0)>q_\alpha\}$. If $\lambda=\lambda_0$, the rejection probability tends to $\alpha$. If $\lambda<\lambda_0$, write $T_n(\lambda_0)=\sqrt n(\hat\lambda-\lambda)/\hat\lambda-\sqrt n(\lambda_0-\lambda)/\hat\lambda$; the first term converges in distribution and the second tends to $+\infty$ in probability, so the rejection probability tends to $0$. Hence $\limsup_n\Pr_\lambda(\psi=1)\le\alpha$ for every $\lambda\le\lambda_0$.

3. a) $\hat\lambda=1/0.98\approx1.0204$ and $T_{50}(1)=\sqrt{50}\,(0.0204)/1.0204\approx0.141$, far below $q_{0.05}=1.645$ (or $q_{0.01}$, $q_{0.1}$): do not reject $H_0$. The data do not show that $\lambda>1$.

   b) p-value $=\Pr(Z>0.141)\approx0.44$.
:::

::: {.solution for="prob-mit18650f16-6-q2" status="draft"}
1. $\hat\mu=\bar X_n$ and $\hat\sigma^2=\frac1n\sum_i(X_i-\bar X_n)^2$.

2. Let $Z=\sqrt n(\hat\mu-\mu)/\sigma\sim N(0,1)$ and $V=n\hat\sigma^2/\sigma^2\sim\chi^2_{n-1}$; by @thm-normal-sample-theory they are independent. Then
$$\frac Z{\sqrt{V/(n-1)}}=\frac{\sqrt n(\hat\mu-\mu)/\sigma}{\sqrt{n\hat\sigma^2/((n-1)\sigma^2)}}=\sqrt{n-1}\,\frac{\hat\mu-\mu}{\hat\sigma}=S,$$
so $S\sim t_{n-1}$ (@def-t-distribution).

3. Let $q=q_\alpha(t_{n-1})$ and $T=\sqrt{n-1}\,\hat\mu/\hat\sigma$; reject $H_0$ when $T<-q$. For any $\mu>0$, $T=S+\sqrt{n-1}\,\mu/\hat\sigma>S$, so
$$\Pr_{\mu,\sigma^2}(T<-q)\le\Pr(S<-q)=\alpha$$
by symmetry of $t_{n-1}$. So the test has level $\alpha$ for every $n$; the bound is approached as $\mu\downarrow0$, so the level cannot be improved.
:::

::: {.solution for="prob-mit18650f16-6-q3" status="draft"}
1. Independence of two Bernoulli variables means that all four cells factor. If $X\perp Y$ then $r=pq$. Conversely, if $r=pq$: $\Pr(X=1,Y=0)=p-r=p(1-q)$, $\Pr(X=0,Y=1)=q-r=(1-p)q$, and $\Pr(X=0,Y=0)=1-p-q+r=(1-p)(1-q)$, so all four cells factor.

2. a) Each is a sample mean of i.i.d. bounded variables with means $p$, $q$ and $E[XY]=r$; the strong law gives almost sure, hence consistent, convergence.

   b) $(\hat p,\hat q,\hat r)$ is the mean of the i.i.d. vectors $(X_i,Y_i,X_iY_i)$, so by the multivariate central limit theorem (@thm-multivariate-clt) $\sqrt n\bigl((\hat p,\hat q,\hat r)-(p,q,r)\bigr)\to N_3(0,\Sigma)$ with (using $X^2=X$, $Y^2=Y$, $(XY)^2=XY$, $X\cdot XY=XY$)
   $$\Sigma=\begin{pmatrix}p(1-p)&r-pq&r(1-p)\\ r-pq&q(1-q)&r(1-q)\\ r(1-p)&r(1-q)&r(1-r)\end{pmatrix}.$$

   c) Apply the delta method (@thm-multivariate-delta-method) to $g(p,q,r)=r-pq$, with gradient $\nabla g=(-q,-p,1)$:
   $$V=\nabla g^{\mathsf T}\Sigma\nabla g=q^2p(1-p)+p^2q(1-q)+r(1-r)+2pq(r-pq)-2qr(1-p)-2pr(1-q).$$

   d) Put $r=pq$: the term $2pq(r-pq)$ vanishes and
   $$V=pq\bigl[q(1-p)+p(1-q)+1-pq-2q(1-p)-2p(1-q)\bigr]=pq\bigl[1-p-q+pq\bigr]=pq(1-p)(1-q).$$
   By continuous mapping $\hat V=\hat p\hat q(1-\hat p)(1-\hat q)$ is consistent.

   e) Under $H_0$, $r-pq=0$ and by Slutsky's theorem $T_n=\sqrt n(\hat r-\hat p\hat q)/\sqrt{\hat V}\to N(0,1)$. The test $\mathbf 1\{|T_n|>q_{\alpha/2}\}$ has asymptotic level $\alpha$.

3. With $X$ = "in a relationship" and $Y$ = "happy": $\hat p=506/1000=0.506$, $\hat q=384/1000=0.384$, $\hat r=0.205$. Then $\hat r-\hat p\hat q\approx0.0107$, $\hat V\approx0.0591$, and $T_n=\sqrt{1000}\cdot0.0107/\sqrt{0.0591}\approx1.39<1.96$. We do not reject independence at level $5\%$; the p-value is $\Pr(|Z|>1.39)\approx0.16$. (Here $T_n^2\approx1.93$ equals Pearson's chi-square statistic for the $2\times2$ table, @def-goodness-of-fit with one degree of freedom.)
:::
