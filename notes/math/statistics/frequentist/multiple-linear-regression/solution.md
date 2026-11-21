<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-8-q1" status="draft"}
1. With $\Sigma=\sigma^2I_n$ the criterion is $\|Y-\mathbb X\beta\|^2/\sigma^2$, minimised by the same $\beta$ as $\|Y-\mathbb X\beta\|^2$: the LSE.

2. $Y\sim N_n(\mathbb X\beta,\Sigma)$ has density $(2\pi)^{-n/2}(\det\Sigma)^{-1/2}\exp\bigl(-\frac12(Y-\mathbb X\beta)'\Sigma^{-1}(Y-\mathbb X\beta)\bigr)$; the prefactor does not involve $\beta$, so maximising the likelihood is minimising the quadratic form.

3. $\operatorname{rank}\mathbb X=p$. Then $\mathbb X'\Sigma^{-1}\mathbb X$ is positive definite ($v'\mathbb X'\Sigma^{-1}\mathbb Xv=(\mathbb Xv)'\Sigma^{-1}(\mathbb Xv)>0$ for $v\ne0$, as $\mathbb Xv\ne0$ and $\Sigma^{-1}$ is positive definite), so the criterion is strictly convex with a unique minimiser.

4. The gradient $-2\mathbb X'\Sigma^{-1}(Y-\mathbb X\beta)$ vanishes at
$$\hat\beta=(\mathbb X'\Sigma^{-1}\mathbb X)^{-1}\mathbb X'\Sigma^{-1}Y .$$
(Equivalently, with $\Sigma^{-1/2}$ the symmetric inverse square root, this is the LSE for $\Sigma^{-1/2}Y=\Sigma^{-1/2}\mathbb X\beta+\Sigma^{-1/2}\varepsilon$, whose noise is $N_n(0,I_n)$.) As $\hat\beta=\beta+A\varepsilon$ with $A=(\mathbb X'\Sigma^{-1}\mathbb X)^{-1}\mathbb X'\Sigma^{-1}$, it is Gaussian with mean $\beta$ and covariance $A\Sigma A'=(\mathbb X'\Sigma^{-1}\mathbb X)^{-1}$:
$$\hat\beta\sim N_p\bigl(\beta,(\mathbb X'\Sigma^{-1}\mathbb X)^{-1}\bigr).$$

5. The bias is $0$ and the quadratic risk is $E\|\hat\beta-\beta\|^2=\operatorname{tr}\bigl((\mathbb X'\Sigma^{-1}\mathbb X)^{-1}\bigr)$.
:::

::: {.solution for="prob-mit18650f16-8-q2" status="draft"}
1. The pair $(\mathbf X_i,Y_i)$ has density $g(x)\,f_x(y-x'\beta)$ (first $\mathbf X_i=x$, then $\varepsilon_i=y-x'\beta$ given $\mathbf X_i=x$). So
$$L_n(\beta)=\prod_{i=1}^ng(\mathbf X_i)\,f_{\mathbf X_i}(Y_i-\mathbf X_i'\beta).$$

2. $\prod_ig(\mathbf X_i)$ is a positive factor free of $\beta$, so the maximiser of $L_n$ is that of $\prod_if_{\mathbf X_i}(Y_i-\mathbf X_i'\beta)$, which does not involve $g$.

3. a) $f_x(e)=\dfrac1{\sqrt{2\pi\sigma^2}}e^{-e^2/(2\sigma^2)}$ for every $x$.

   b) By part 2 the log-likelihood in $\beta$ is $-\frac1{2\sigma^2}\sum_i(Y_i-\mathbf X_i'\beta)^2+\text{const}$, maximised by the LSE. With the design matrix $\mathbb X$ (rows $\mathbf X_i'$) of rank $p$, $\hat\beta=(\mathbb X'\mathbb X)^{-1}\mathbb X'Y$.

   c) Given the $\mathbf X_i$, the noise is $N_n(0,\sigma^2I_n)$ and @thm-gaussian-linear-model applies: $\hat\beta\sim N_p\bigl(\beta,\sigma^2(\mathbb X'\mathbb X)^{-1}\bigr)$.

   d) $E[\hat\beta\mid\mathbf X_1,\dots,\mathbf X_n]=\beta$, so $E[\hat\beta]=\beta$ by iterated expectations (when $\hat\beta$ is integrable): unbiased.

   e) Maximising over $\sigma^2$ gives $\hat\sigma^2_{\mathrm{MLE}}=\frac1n\|Y-\mathbb X\hat\beta\|^2$.

   f) $\hat\sigma^2=\frac1{n-p}\|Y-\mathbb X\hat\beta\|^2$. Given the $\mathbf X_i$, $(n-p)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p}$ (@thm-gaussian-linear-model); since this conditional law does not depend on the $\mathbf X_i$, $\hat\sigma^2$ is also unconditionally unbiased.

4. a) $\hat b=\dfrac{\overline{XY}-\bar X\bar Y}{\overline{X^2}-\bar X^2}$ and $\hat a=\bar Y-\hat b\bar X$ (@prp-least-squares-slope).

   b) By the law of large numbers the sample moments converge to $E[XY]$, $E[X]$, $E[Y]$, $E[X^2]$, and by continuous mapping $\hat b\to\operatorname{Cov}(X,Y)/\mathrm{Var}(X)=b$, since $\operatorname{Cov}(X,Y)=b\mathrm{Var}(X)+\operatorname{Cov}(X,\varepsilon)=b\mathrm{Var}(X)$ (@prp-regression-characterisation); then $\hat a\to E[Y]-bE[X]=a$.

   c) Write $\mathbf X_i=(1,X_i)'$ and $M=E[\mathbf X_1\mathbf X_1']=\begin{pmatrix}1&\mu_1\\\mu_1&\mu_2\end{pmatrix}$ with $\mu_k=E[X_1^k]$. Then
   $$\sqrt n(\hat\beta-\beta)=\Bigl(\frac1n\sum_i\mathbf X_i\mathbf X_i'\Bigr)^{-1}\frac1{\sqrt n}\sum_i\mathbf X_i\varepsilon_i .$$
   The vectors $\mathbf X_i\varepsilon_i$ are i.i.d. with mean $E[\mathbf X_1]E[\varepsilon_1]=0$ and covariance $E[\varepsilon_1^2]E[\mathbf X_1\mathbf X_1']=\sigma^2M$ (independence), so the second factor tends to $N_2(0,\sigma^2M)$ (@thm-multivariate-clt). The first tends to $M^{-1}$ in probability. By Slutsky's theorem $\sqrt n(\hat\beta-\beta)\to N_2(0,\sigma^2M^{-1}MM^{-1})=N_2(0,\sigma^2M^{-1})$, with
   $$\sigma^2M^{-1}=\frac{\sigma^2}{\mu_2-\mu_1^2}\begin{pmatrix}\mu_2&-\mu_1\\-\mu_1&1\end{pmatrix}.$$
   In particular the asymptotic variance of $\hat b$ is $\sigma^2/\mathrm{Var}(X_1)$.

   d) Estimate $\sigma^2$ by $\hat\sigma^2=\frac1n\sum_i(Y_i-\hat a-\hat bX_i)^2$ and $\mathrm{Var}(X_1)$ by $s_X^2=\overline{X^2}-\bar X^2$; both are consistent. Let $T_n=\sqrt n\,\hat b\,s_X/\hat\sigma$ and reject $H_0$: "$b>0$" when $T_n<-q_\alpha$, $q_\alpha$ the $(1-\alpha)$-quantile of $N(0,1)$. For $b>0$, $T_n=\sqrt n(\hat b-b)s_X/\hat\sigma+\sqrt n\,b\,s_X/\hat\sigma$, where the first term tends to $N(0,1)$ and the second to $+\infty$, so the rejection probability tends to $0\le\alpha$: the test has asymptotic level at most $\alpha$ (and exactly $\alpha$ at the boundary $b=0$).
:::
