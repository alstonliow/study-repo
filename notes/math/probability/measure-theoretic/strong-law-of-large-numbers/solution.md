<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-3-q4" status="draft"}
1. $X=\sum_{n\ge1}\mathbf 1_{\{X\ge n\}}$ pointwise (an integer $k\ge0$ is the number of $n\ge1$ with $n\le k$). Integrate term by term (@cor-series-nonnegative-integral).

2. For a non-negative real random variable $W$: $\sum_{n\ge1}\Pr(W\ge n)=\sum_{n\ge1}\Pr(\lfloor W\rfloor\ge n)=E\lfloor W\rfloor\ge E[W]-1$.

3. Let $E[X]=\infty$ and $K\ge1$. By step 2 with $W=X/K$, $\sum_n\Pr(X_n\ge Kn)=\sum_n\Pr(X/K\ge n)=\infty$. The events $\{X_n\ge Kn\}$ are independent, so by the second Borel–Cantelli lemma (@lem-borel-cantelli) they occur infinitely often a.s., giving $\limsup_nX_n/n\ge K$ a.s. ($K=1$ is the first claim). Intersecting over $K\in\mathbb N$, $\limsup_nX_n/n=\infty$ a.s.

4. For i.i.d. $Y_n$ with $E|Y_1|=\infty$, apply step 3's argument to $|Y_n|$ (step 2 does not need integer values): $\limsup_n|Y_n|/n=\infty$ a.s.

5. Let $S_n=Y_1+\dots+Y_n$. If $|S_n|/n\le C$ for all large $n$, then $|Y_n|=|S_n-S_{n-1}|\le Cn+C(n-1)\le2Cn$ for large $n$, contradicting step 4. So $\limsup_n|S_n|/n=\infty$ a.s.
:::

::: {.solution for="prob-camii-pms-10-q1" status="draft"}
1. Let $Z_i=X_iX_{i+1}$. Then $E[Z_i]=\mu^2$ and $E[Z_i^4]=E[X_i^4]E[X_{i+1}^4]\le M^2$ by independence.

2. The odd-indexed terms $Z_1,Z_3,Z_5,\dots$ are independent, since they are functions of the disjoint blocks $(X_1,X_2),(X_3,X_4),\dots$ (@cor-independence-grouping). So are the even-indexed terms $Z_2,Z_4,\dots$.

3. By @thm-slln-fourth-moment applied to each family, $\frac1m\sum_{j\le m}Z_{2j-1}\to\mu^2$ and $\frac1m\sum_{j\le m}Z_{2j}\to\mu^2$ a.s.

4. $P_n$ is the sum of the first $\lceil(n-1)/2\rceil$ odd-indexed and the first $\lfloor(n-1)/2\rfloor$ even-indexed terms. Both counts divided by $n$ tend to $\frac12$, so $\frac{P_n}n\to\frac12\mu^2+\frac12\mu^2=\mu^2$ almost surely.
:::

::: {.solution for="prob-camii-pms-10-q3" status="draft"}
1. *Derivatives.* Fix $\lambda_0>0$. For $\lambda>\lambda_0$, the $k$th $\lambda$-derivative of $e^{-\lambda x}f(x)$ is $(-x)^ke^{-\lambda x}f(x)$, bounded by $\|f\|_\infty x^ke^{-\lambda_0x}$, integrable on $(0,\infty)$. By @thm-differentiation-under-integral and induction, $\hat f^{(k)}(\lambda)=\int_0^\infty(-x)^ke^{-\lambda x}f(x)\,dx$ on $(\lambda_0,\infty)$, for every $\lambda_0$.

2. *Gamma density.* $S_n$ has density $\frac{\lambda^nx^{n-1}e^{-\lambda x}}{(n-1)!}$ on $(0,\infty)$: by induction, the convolution of this density with $\lambda e^{-\lambda x}$ is $\int_0^x\frac{\lambda^ny^{n-1}e^{-\lambda y}}{(n-1)!}\lambda e^{-\lambda(x-y)}dy=\frac{\lambda^{n+1}x^ne^{-\lambda x}}{n!}$.

3. Hence $\hat f^{(n-1)}(\lambda)=(-1)^{n-1}\frac{(n-1)!}{\lambda^n}E[f(S_n)]$, i.e. $C(\lambda,n)=(-1)^{n-1}(n-1)!\,\lambda^{-n}\neq0$.

4. *Uniqueness.* Suppose $\hat f\equiv0$. Then $E[f(S_n)]=0$ for every $n$ and $\lambda$. Fix $x>0$ and take $\lambda=n/x$. Then $E[S_n]=n/\lambda=x$ and $\operatorname{Var}(S_n)=n/\lambda^2=x^2/n$, so by Chebyshev $S_n\to x$ in probability as $n\to\infty$.

5. $f$ is continuous at $x$, so $f(S_n)\to f(x)$ in probability, and $|f(S_n)|\le\|f\|_\infty$. By @thm-bounded-convergence-probability, $0=E[f(S_n)]\to f(x)$. So $f(x)=0$.
:::
