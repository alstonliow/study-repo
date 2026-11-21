<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-4-q1" status="draft"}
1. $\hat p=\bar X_n$ (@exm-mle-bernoulli-poisson); $I(p)=\dfrac1{p(1-p)}$ (@exm-fisher-information-bernoulli).

2. $\hat\lambda=\bar X_n$. $\ell(\lambda)=-\lambda+X\log\lambda-\log X!$, $\ell''=-X/\lambda^2$, so $I(\lambda)=E[X]/\lambda^2=1/\lambda$.

3. $\ell_n=n\log\lambda-\lambda\sum_iX_i$ gives $\hat\lambda=1/\bar X_n$. $\ell''(\lambda)=-1/\lambda^2$, so $I(\lambda)=1/\lambda^2$.

4. $\hat\mu=\bar X_n$, $\hat\sigma^2=\frac1n\sum_i(X_i-\bar X_n)^2$ (@exm-ml-normal). With $v=\sigma^2$, $\ell=-\frac12\log(2\pi v)-\frac{(X-\mu)^2}{2v}$:
$$\partial^2_\mu\ell=-\frac1v,\qquad\partial_\mu\partial_v\ell=-\frac{X-\mu}{v^2},\qquad\partial_v^2\ell=\frac1{2v^2}-\frac{(X-\mu)^2}{v^3}.$$
Taking $-E[\cdot]$: $I(\mu,\sigma^2)=\begin{pmatrix}1/\sigma^2&0\\0&1/(2\sigma^4)\end{pmatrix}$.

5. The likelihood is $\lambda^ne^{-\lambda\sum_i(X_i-a)}$ if $a\le\min_iX_i$ and $0$ otherwise. For fixed $\lambda$ it increases in $a$, so $\hat a=\min_iX_i$; then maximising $n\log\lambda-\lambda\sum_i(X_i-\hat a)$ gives $\hat\lambda=1/(\bar X_n-\min_iX_i)$. The Fisher information is not defined in the usual sense: the support $[a,\infty)$ depends on $a$, the log-density is not differentiable in $a$ at $x=a$ (and is $-\infty$ for $a>x$), and the score identities fail. For $\lambda$ alone (with $a$ known) $I(\lambda)=1/\lambda^2$ as in part 3.

6. $\ln X_i\sim N(\mu,\sigma^2)$, and the log-likelihood is $-\sum_i\ln X_i$ plus the Gaussian log-likelihood of the $\ln X_i$. So $\hat\mu=\frac1n\sum_i\ln X_i$, $\hat\sigma^2=\frac1n\sum_i(\ln X_i-\hat\mu)^2$, and the derivatives in $(\mu,\sigma^2)$ are those of part 4 with $\ln X$ in place of $X$: $I(\mu,\sigma^2)=\operatorname{diag}\bigl(1/\sigma^2,\ 1/(2\sigma^4)\bigr)$.
:::

::: {.solution for="prob-mit18650f16-4-q3" status="draft"}
Write $q=q(\lambda)=e^{-\lambda z}$.

1. $X_i=\mathbf 1\{Y_i>z\}$ with $Y_i\sim\operatorname{Exp}(\lambda)$, so $X_i\sim\operatorname{Ber}(q)$, $q=\Pr(Y_i>z)=e^{-\lambda z}$, independently.

2. By the central limit theorem $\sqrt n(\bar X_n-q)\to N\bigl(0,q(1-q)\bigr)$: asymptotic variance $e^{-\lambda z}(1-e^{-\lambda z})$.

3. $\lambda=-\ln(q)/z$, so take $f(x)=-\ln(x)/z$. Since $\bar X_n\to q\in(0,1)$ almost surely and $f$ is continuous there, $f(\bar X_n)\to\lambda$ almost surely. (On the event $\bar X_n=0$, whose probability $(1-q)^n$ tends to $0$, $f$ is infinite; this does not affect consistency.)

4. $f'(q)=-1/(zq)$. By the delta method (@thm-delta-method),
$$\sqrt n\bigl(f(\bar X_n)-\lambda\bigr)\to N\Bigl(0,\ \frac{q(1-q)}{z^2q^2}\Bigr)=N\Bigl(0,\ \frac{e^{\lambda z}-1}{z^2}\Bigr).$$

5. Minimise $v(z)=(e^{\lambda z}-1)/z^2$ over $z>0$. Then $v'(z)=\bigl(\lambda z\,e^{\lambda z}-2(e^{\lambda z}-1)\bigr)/z^3$, which vanishes when $\lambda ze^{\lambda z}=2(e^{\lambda z}-1)$, i.e.
$$z=g_\lambda(z),\qquad g_\lambda(z)=\frac2\lambda\bigl(1-e^{-\lambda z}\bigr).$$
(With $u=\lambda z$ this is $u=2(1-e^{-u})$, whose positive root is $u\approx1.594$; $v\to\infty$ as $z\to0$ or $z\to\infty$, so this is the minimum. The best threshold is about $1.59$ times the mean salary $1/\lambda$.)

6. a) $\bigl((0,\infty),(\operatorname{Exp}(\lambda))_{\lambda>0}\bigr)$.

   b) $I_Y(\lambda)=1/\lambda^2$ (Problem 1, part 3).

   c) For $X\sim\operatorname{Ber}(q(\lambda))$, $\ell(\lambda)=X\ln q+(1-X)\ln(1-q)$ and $\ell'=q'(\lambda)\bigl(\frac Xq-\frac{1-X}{1-q}\bigr)$, so $I_X(\lambda)=\mathrm{Var}(\ell')=\dfrac{q'(\lambda)^2}{q(1-q)}$. With $q'=-zq$,
   $$I_X(\lambda)=\frac{z^2q}{1-q}=\frac{z^2}{e^{\lambda z}-1} .$$
   Its inverse is the asymptotic variance of part 4, as it should be: $f(\bar X_n)$ is the MLE of $\lambda$ from the $X_i$.

   d) With $u=\lambda z>0$, $I_X\le I_Y$ is equivalent to $u^2\le e^u-1$. The function $e^u-1-u^2$ is $0$ at $0$ and has derivative $e^u-2u>0$ (since $e^u\ge eu>2u$), so $I_X(\lambda)<I_Y(\lambda)$. Recording only whether the salary exceeds $z$ throws information away: each answer is worth less than an exact salary, and the estimator from the binary answers has a larger asymptotic variance than the MLE $1/\bar Y_n$ from full data. The questionnaire trades this loss of precision for more and more reliable answers.
:::
