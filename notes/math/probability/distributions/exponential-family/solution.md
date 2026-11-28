<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-11-q1" status="draft"}
We write each density in the form $b(y)\exp(\eta^{\mathsf T}T(y)-a(\eta))$ of @def-exponential-family.

1. $\operatorname{Ber}(p)$: yes, $\eta=\log\frac p{1-p}$, $T(y)=y$ (@exm-exponential-family-members).

2. $N(\mu,1)$: yes, $\eta=\mu$, $T(y)=y$.

3. $N(\mu,\sigma^2)$: yes, a two-parameter family: $\frac1{\sqrt{2\pi\sigma^2}}e^{-(y-\mu)^2/(2\sigma^2)}=\exp\bigl(\frac\mu{\sigma^2}y-\frac1{2\sigma^2}y^2-\frac{\mu^2}{2\sigma^2}-\frac12\log(2\pi\sigma^2)\bigr)$, with $\eta=(\mu/\sigma^2,-1/(2\sigma^2))$ and $T(y)=(y,y^2)$.

4. $\operatorname{Exp}(\lambda)$: yes, $\lambda e^{-\lambda y}=\exp(-\lambda y+\log\lambda)$ on $y>0$: $\eta=-\lambda$, $T(y)=y$, $b(y)=\mathbf 1\{y>0\}$.

5. $\mathcal U([0,\vartheta])$: no. In an exponential family the set $\{y:p(y;\eta)>0\}=\{y:b(y)>0\}$ is the same for every parameter, but the support $[0,\vartheta]$ changes with $\vartheta$.

6. $\Gamma(\alpha,\beta)$: yes, a two-parameter family: $\frac{\beta^\alpha}{\Gamma(\alpha)}y^{\alpha-1}e^{-\beta y}=\exp\bigl((\alpha-1)\log y-\beta y-\log\Gamma(\alpha)+\alpha\log\beta\bigr)$ on $y>0$, with $\eta=(\alpha-1,-\beta)$ and $T(y)=(\log y,y)$. (For fixed $\alpha$ it is a one-parameter family in $\beta$.)

7. $\operatorname{Poiss}(\lambda)$: yes, $\eta=\log\lambda$, $T(y)=y$, $b(y)=1/y!$.
:::

::: {.solution for="prob-mit18650f16-11-q2" status="draft"}
1. a) $f_\theta$ is a probability density (set to $0$ outside $\mathcal X$), so it integrates to $1$ for every $\theta$.

   b) This is @prp-score-identities; for this family directly: since $\ell'=\partial_\theta f_\theta/f_\theta$,
      1. $E_\theta[\ell'(\theta)]=\int\partial_\theta f_\theta\,dx=\frac{d}{d\theta}\int f_\theta\,dx=0$;
      2. $\ell''=\partial^2_\theta f_\theta/f_\theta-(\ell')^2$ and $E_\theta[\partial_\theta^2f_\theta/f_\theta]=\frac{d^2}{d\theta^2}\int f_\theta=0$, so $E_\theta[\ell'']=-E_\theta[(\ell')^2]=-\operatorname{Var}_\theta[\ell']$, using the first identity.

   c) The Fisher information $I(\theta)$ (@def-fisher-information).

2. $\ell(\theta)=\ln a(X)-\theta X+b(\theta)$, so $\ell'(\theta)=-X+b'(\theta)$ and $\ell''(\theta)=b''(\theta)$. (The function $a$ drops out.)

3. From $E_\theta[\ell']=0$: $E_\theta[X]=b'(\theta)$. From the second identity: $\operatorname{Var}_\theta[X]=\operatorname{Var}_\theta[\ell']=-E_\theta[\ell'']=-b''(\theta)$. (Here $-b$ plays the role of the log partition function in @prp-exponential-family-moments, with natural parameter $-\theta$.)

4. a) $\mathcal X=(0,\infty)$.

   b) $f_\theta(x)=\frac{\theta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\theta x}=\frac{x^{\alpha-1}}{\Gamma(\alpha)}\exp(-\theta x+\alpha\ln\theta)$: $a(x)=x^{\alpha-1}/\Gamma(\alpha)$ and $b(\theta)=\alpha\ln\theta$.

   c) $b'(\theta)=\alpha/\theta$ and $b''(\theta)=-\alpha/\theta^2$, so with $\theta=\beta$: $E[X]=\alpha/\beta$ and $\operatorname{Var}(X)=\alpha/\beta^2$.
:::
