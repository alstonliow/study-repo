<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-10-q1" status="draft"}
Let $S=\sum_iX_i^2$.

1. $\ell_n(\theta)=-\frac n2\ln(2\pi\theta)-\frac S{2\theta}$, $\ell_n'(\theta)=-\frac n{2\theta}+\frac S{2\theta^2}$, so $\hat\theta=S/n$.

2. The $X_i^2$ are i.i.d. with mean $\theta$ and variance $E[X^4]-\theta^2=3\theta^2-\theta^2=2\theta^2$. By the central limit theorem $\sqrt n(\hat\theta-\theta)\to N(0,2\theta^2)$; the asymptotic variance $2\theta^2$ equals $I(\theta)^{-1}$, since $\ell''(\theta)=\frac1{2\theta^2}-\frac{X^2}{\theta^3}$ gives $I(\theta)=\frac1{2\theta^2}$.

3. a) $\pi_J(\theta)\propto\sqrt{I(\theta)}\propto1/\theta$ on $(0,\infty)$ (@def-jeffreys-prior). It is improper: $\int_0^\infty d\theta/\theta=\infty$.

   b) $\pi(\theta\mid X)\propto\frac1\theta\cdot\theta^{-n/2}e^{-S/(2\theta)}=\theta^{-(n/2+1)}e^{-(S/2)/\theta}$, the inverse Gamma density with $\alpha=n/2$, $\beta=S/2$. It is a proper distribution whenever $S>0$ (which holds with probability $1$) and $n\ge1$, so the posterior is well defined although the prior is not.

   c) The posterior mean exists when $\alpha=n/2>1$, i.e. $n\ge3$, and equals
   $$\hat\theta^{(\pi_J)}=\frac{S/2}{n/2-1}=\frac{S}{n-2} .$$
   It differs from the MLE $S/n$ by a factor $n/(n-2)\to1$, so it has the same asymptotic behaviour (compare the Bernstein–von Mises remark in the note).
:::

::: {.solution for="prob-mit18650f16-10-q2" status="draft"}
Throughout let $\lambda>0$ and $A=\mathbb X'\mathbb X+\lambda I_p$, which is positive definite for any $\mathbb X$.

1. $Y\mid\beta\sim N_n(\mathbb X\beta,\sigma^2I_n)$.

2. a) By Bayes' formula the posterior density is proportional to
   $$\exp\Bigl(-\frac{\|Y-\mathbb X\beta\|^2}{2\sigma^2}\Bigr)\exp\Bigl(-\frac{\|\beta\|^2}{2\tau^2}\Bigr)=\exp\Bigl(-\frac1{2\sigma^2}\bigl(\|Y-\mathbb X\beta\|^2+\lambda\|\beta\|^2\bigr)\Bigr),\qquad\lambda=\frac{\sigma^2}{\tau^2}.$$

   b) Expand: $\|Y-\mathbb X\beta\|^2+\lambda\|\beta\|^2=\beta'A\beta-2\beta'\mathbb X'Y+\|Y\|^2=(\beta-m)'A(\beta-m)+\text{const}$ with $m=A^{-1}\mathbb X'Y$. So the posterior density is proportional to $\exp\bigl(-\frac12(\beta-m)'(\sigma^2A^{-1})^{-1}(\beta-m)\bigr)$: by the hint, the posterior is
   $$N_p\bigl(A^{-1}\mathbb X'Y,\ \sigma^2A^{-1}\bigr).$$

   c) The posterior mean is $(\mathbb X'\mathbb X+\lambda I_p)^{-1}\mathbb X'Y$ with $\lambda=\sigma^2/\tau^2$.

3. a) The objective is strictly convex with gradient $-2\mathbb X'(Y-\mathbb Xt)+2\lambda t$, which vanishes at $\hat\beta^{(R)}=(\mathbb X'\mathbb X+\lambda I_p)^{-1}\mathbb X'Y$ (@prp-ridge-closed-form).

   b) Comparing with 2(c), $\hat\beta^{(R)}$ is the Bayes estimator (posterior mean) for the prior $N_p(0,\tau^2I_p)$ with $\tau^2=\sigma^2/\lambda$. (The posterior is Gaussian, so this is also the MAP estimate, @prp-map-ridge.)

   c) $\hat\beta^{(R)}=A^{-1}\mathbb X'Y$ is linear in $Y\sim N_n(\mathbb X\beta,\sigma^2I_n)$, so
   $$\hat\beta^{(R)}\sim N_p\bigl(A^{-1}\mathbb X'\mathbb X\beta,\ \sigma^2A^{-1}\mathbb X'\mathbb XA^{-1}\bigr).$$

   d) The bias is $A^{-1}\mathbb X'\mathbb X\beta-\beta=A^{-1}(\mathbb X'\mathbb X-A)\beta=-\lambda A^{-1}\beta$. Quadratic risk $=\|\text{bias}\|^2+\operatorname{tr}(\text{covariance})$:
   $$E\|\hat\beta^{(R)}-\beta\|^2=\lambda^2\beta'(\mathbb X'\mathbb X+\lambda I_p)^{-2}\beta+\sigma^2\operatorname{tr}\bigl((\mathbb X'\mathbb X+\lambda I_p)^{-1}\mathbb X'\mathbb X(\mathbb X'\mathbb X+\lambda I_p)^{-1}\bigr).$$
   The first term grows and the second shrinks with $\lambda$; for small enough $\lambda>0$ the total is below the LSE risk $\sigma^2\operatorname{tr}((\mathbb X'\mathbb X)^{-1})$ when $\mathbb X$ has rank $p$.
:::
