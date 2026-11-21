<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-2-q1" status="draft"}
1. $X_i^2=X_i$, so $E[X_i^2]=p$ and $\operatorname{var}(X_i)=p-p^2=p(1-p)$.

2. $\bar X_n\to p$ almost surely by the strong law, and $x\mapsto x(1-x)$ is continuous, so $\bar X_n(1-\bar X_n)\to p(1-p)$ almost surely (@thm-continuous-mapping); in particular it is (strongly) consistent.

3. $E[\bar X_n]=p$ and $E[\bar X_n^2]=\operatorname{var}(\bar X_n)+p^2=\frac{p(1-p)}n+p^2$. Hence
$$E[\bar X_n(1-\bar X_n)]=p-p^2-\frac{p(1-p)}n=\Bigl(1-\frac1n\Bigr)p(1-p),$$
and the bias is $-p(1-p)/n$.

4. For $n\ge2$, $\dfrac n{n-1}\bar X_n(1-\bar X_n)$ is unbiased. (It is the sample variance with divisor $n-1$, since $\frac1n\sum_i(X_i-\bar X_n)^2=\bar X_n-\bar X_n^2$ for $0/1$ data.)
:::

::: {.solution for="prob-mit18650f16-2-q2" status="draft"}
In each case the observations are i.i.d. and we give $(E,(\Pr_\theta)_{\theta\in\Theta})$ for one observation.

1. $\bigl(\{0,1,2,\dots\},(\operatorname{Poisson}(\lambda))_{\lambda>0}\bigr)$. Identified: $\lambda$ is the mean, so different $\lambda$ give different laws.

2. $\bigl((0,\infty),(\operatorname{Exp}(\lambda))_{\lambda\in(0,10]}\bigr)$. Identified (the mean is $1/\lambda$).

3. $\bigl([0,\infty),(U[0,\theta])_{\theta>0}\bigr)$. Identified: $\theta$ is the right end of the support.

4. $\bigl(\mathbb{R},(N(\mu,\sigma^2))_{(\mu,\sigma^2)\in\mathbb{R}\times(0,\infty)}\bigr)$. Identified: the mean and the variance determine $(\mu,\sigma^2)$.

5. Observing $X_i=\mathbf 1\{Y_i\ge0\}$ gives $\bigl(\{0,1\},(\operatorname{Ber}(\Phi(\mu/\sigma)))_{(\mu,\sigma^2)}\bigr)$. $(\mu,\sigma^2)$ is not identified, since only $\mu/\sigma$ enters; $\mu/\sigma$ is identified because $\Phi$ is strictly increasing (@exm-identifiability-signs). (The sign of $0$ has probability $0$, so recording $-1/+1$ instead changes nothing.)

6. A proportion lies in $[0,1]$, so the model $\bigl([0,1],(U[0,\theta])_{\theta\in(0,1]}\bigr)$; identified as in 3.

7. Let $T_i\sim\operatorname{Exp}(\lambda)$ be the commute time (in minutes) and $X_i=\mathbf 1\{T_i\ge20\}$. Then $X_i\sim\operatorname{Ber}(e^{-20\lambda})$: the model is $\bigl(\{0,1\},(\operatorname{Ber}(e^{-20\lambda}))_{\lambda>0}\bigr)$. The parameter of interest, the mean commute time $1/\lambda$, is identified because $\lambda\mapsto e^{-20\lambda}$ is one to one.

8. For each machine we observe $Y_i=\min(T_i,T)$ and whether it failed, $\delta_i=\mathbf 1\{T_i<T\}$, with $T_i\sim\operatorname{Exp}(\lambda)$. The law of $(Y_i,\delta_i)$ has density $\lambda e^{-\lambda y}$ for $y<T$, $\delta=1$, and an atom of mass $e^{-\lambda T}$ at $(T,0)$. So $E=([0,T)\times\{1\})\cup\{(T,0)\}$ and $\lambda>0$. Identified, since already $\Pr(\delta=0)=e^{-500\lambda}$ is one to one in $\lambda$. (If only the failed machines' lifetimes are recorded with the number $67$ known, the same model applies.)
:::
