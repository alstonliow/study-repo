---
title: "Exponential Families"
sources: [cs229-3]
requires: [math/probability/continuous/standard-distributions]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 3 (the exponential family: Bernoulli and Gaussian examples), in our own wording. The Poisson example and the moment proposition with its proof are our own additions. -->

Many standard distributions share one algebraic form, in which the parameter enters only through a linear term in the exponent. This form is what makes generalized linear models (@sec-ai-machine-learning-generalized-linear-models) work.

::: {#def-exponential-family .definition name="Exponential family"}

A family of distributions of a random variable $Y$ (discrete or continuous) is an *exponential family* if its probability mass or density functions have the form

$$
p(y;\boldsymbol\eta)=b(y)\exp\bigl(\boldsymbol\eta^{\mathsf T}T(y)-a(\boldsymbol\eta)\bigr),
$$

where $\boldsymbol\eta$ is the *natural parameter*, $T(y)$ the *sufficient statistic* (often $T(y)=y$), $b(y)\ge0$ the *base measure* and $a(\boldsymbol\eta)$ the *log partition function*. The function $a$ is fixed by normalization:

$$
a(\boldsymbol\eta)=\log\int b(y)\exp\bigl(\boldsymbol\eta^{\mathsf T}T(y)\bigr)\,dy
$$

(a sum for discrete $Y$). Fixing $T$, $a$ and $b$ and letting $\boldsymbol\eta$ vary gives the family.

:::

::: {#exm-exponential-family-members .example name="Bernoulli, Gaussian and Poisson"}

1. *Bernoulli with mean $\phi$.* For $y\in\{0,1\}$,

   $$
   \phi^y(1-\phi)^{1-y}=\exp\Bigl(y\log\frac{\phi}{1-\phi}+\log(1-\phi)\Bigr),
   $$

   so $\eta=\log\dfrac{\phi}{1-\phi}$, $T(y)=y$, $b(y)=1$ and, since $\phi=\dfrac{1}{1+e^{-\eta}}$ is the logistic function of $\eta$ (@def-logistic-function), $a(\eta)=-\log(1-\phi)=\log(1+e^\eta)$.

2. *Gaussian with mean $\mu$ and variance $1$.*

   $$
   \frac1{\sqrt{2\pi}}e^{-(y-\mu)^2/2}=\frac1{\sqrt{2\pi}}e^{-y^2/2}\exp\Bigl(\mu y-\frac{\mu^2}2\Bigr),
   $$

   so $\eta=\mu$, $T(y)=y$, $a(\eta)=\eta^2/2$ and $b(y)=e^{-y^2/2}/\sqrt{2\pi}$. (A known variance other than $1$ changes only $b$ and a scale.)

3. *Poisson with mean $\lambda$.* For $y=0,1,2,\dots$,

   $$
   \frac{e^{-\lambda}\lambda^y}{y!}=\frac1{y!}\exp\bigl(y\log\lambda-\lambda\bigr),
   $$

   so $\eta=\log\lambda$, $T(y)=y$, $a(\eta)=e^\eta$ and $b(y)=1/y!$.

The multinomial, exponential, gamma, beta and Dirichlet families have the same form.

:::

::: {#prp-exponential-family-moments .proposition name="The log partition function generates the moments"}

For a one-parameter exponential family with $T(y)=y$, at every $\eta$ in the interior of the set where $a(\eta)$ is finite,

$$
E[Y]=a'(\eta),\qquad \operatorname{Var}(Y)=a''(\eta).
$$

In particular $a$ is convex. (For a vector parameter, $E[T(Y)]=\nabla a(\boldsymbol\eta)$ and the covariance matrix of $T(Y)$ is the Hessian $\nabla^2a(\boldsymbol\eta)$, which is positive semidefinite.)

:::

::: {.proof}

1. Write $Z(\eta)=e^{a(\eta)}=\int b(y)e^{\eta y}\,dy$. Inside the interior of its domain, $Z$ can be differentiated under the integral sign (it is a two-sided Laplace transform of $b$), so $Z'(\eta)=\int y\,b(y)e^{\eta y}\,dy$ and $Z''(\eta)=\int y^2b(y)e^{\eta y}\,dy$.

2. Dividing by $Z(\eta)$ and using $p(y;\eta)=b(y)e^{\eta y}/Z(\eta)$ gives $Z'/Z=E[Y]$ and $Z''/Z=E[Y^2]$.

3. Now $a=\log Z$, so $a'=Z'/Z=E[Y]$.

4. Differentiating again, $a''=Z''/Z-(Z'/Z)^2=E[Y^2]-E[Y]^2=\operatorname{Var}(Y)\ge0$, so $a$ is convex.

:::

::: {#exm-exponential-family-moments .example name="Checking the moments"}

For the Bernoulli, $a'(\eta)=\dfrac{e^\eta}{1+e^\eta}=\phi$ and $a''(\eta)=\phi(1-\phi)$. For the unit-variance Gaussian, $a'(\eta)=\eta=\mu$ and $a''=1$. For the Poisson, $a'(\eta)=a''(\eta)=e^\eta=\lambda$: the mean and the variance of a Poisson variable are both $\lambda$.

:::
