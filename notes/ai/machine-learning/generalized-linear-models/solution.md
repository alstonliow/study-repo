<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-8-q3" status="draft"}
1. Let $\pi_i=P[Y_i=1\mid\mathbf X_i]$. Then $\ln\frac{\pi_i}{1-\pi_i}=\mathbf X_i'\beta$, so
$$\pi_i=\frac{e^{\mathbf X_i'\beta}}{1+e^{\mathbf X_i'\beta}}=\frac1{1+e^{-\mathbf X_i'\beta}} .$$

2. The pair $(\mathbf X_i,Y_i)$ has density $f(x)\,\pi(x)^y(1-\pi(x))^{1-y}$ with respect to (Lebesgue $\times$ counting) measure, where $\pi(x)=1/(1+e^{-x'\beta})$. So
$$L_n(\beta)=\prod_{i=1}^nf(\mathbf X_i)\Bigl(\frac{e^{\mathbf X_i'\beta}}{1+e^{\mathbf X_i'\beta}}\Bigr)^{Y_i}\Bigl(\frac1{1+e^{\mathbf X_i'\beta}}\Bigr)^{1-Y_i}.$$

3. The factor $\prod_if(\mathbf X_i)$ is positive and free of $\beta$, so the maximiser is that of the conditional log-likelihood
$$\ell_n(\beta)=\sum_{i=1}^n\Bigl(Y_i\,\mathbf X_i'\beta-\ln\bigl(1+e^{\mathbf X_i'\beta}\bigr)\Bigr),$$
which does not involve $f$. This is the canonical-link GLM log-likelihood; it is concave (@thm-glm-score-information) and is maximised numerically, for example by IRLS (@prp-irls).
:::

::: {.solution for="prob-mit18650f16-11-q3" status="draft"}
Assume $F$ is continuous and strictly increasing (true in both examples).

1. Given $X_1$, $Z_1\in\{0,1\}$ is Bernoulli with
$$\mu(X_1)=\Pr(Y_1\ge0\mid X_1)=\Pr(\varepsilon_1\ge-X_1'\beta\mid X_1)=1-F(-X_1'\beta),$$
using the independence of $\varepsilon_1$ and $X_1$.

2. The link $g$ satisfies $g(\mu(X))=X'\beta$ (@def-link-function). From $\mu=1-F(-X'\beta)$ we get $X'\beta=-F^{-1}(1-\mu)$, so
$$g(\mu)=-F^{-1}(1-\mu).$$
If the distribution of $\varepsilon$ is symmetric about $0$, then $1-F(-t)=F(t)$, hence $\mu=F(X'\beta)$ and $g=F^{-1}$.

3. $N(0,1)$ is symmetric, so $g=\Phi^{-1}$: the *probit* model (@exm-link-functions).

4. a) $F(t)=\int_{-\infty}^tf=\dfrac1{1+e^{-t}}$, since $\frac{d}{dt}(1+e^{-t})^{-1}=e^{-t}(1+e^{-t})^{-2}=f(t)$ and the limit at $-\infty$ is $0$.

   b) $f(-t)=\dfrac{e^t}{(1+e^t)^2}=\dfrac{e^{-t}}{(e^{-t}+1)^2}=f(t)$, so the distribution is symmetric and $g=F^{-1}$: solving $\mu=1/(1+e^{-t})$ gives $g(\mu)=\ln\dfrac\mu{1-\mu}$, the logit.

   c) *Logistic regression* (the canonical-link Bernoulli GLM). So logistic and probit regression are the same latent-variable model with different noise distributions.
:::
