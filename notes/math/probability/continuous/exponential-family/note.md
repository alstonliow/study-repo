---
title: "Exponential Families"
sources: [cs229-3, mit18650-10]
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

If the family is indexed by another parameter $\theta$ and $\boldsymbol\eta=\boldsymbol\eta(\theta)\in\mathbb{R}^k$, the density reads

$$
p_\theta(y)=b(y)\exp\Bigl(\sum_{i=1}^k\eta_i(\theta)\,T_i(y)-B(\theta)\Bigr),\qquad B(\theta)=a\bigl(\boldsymbol\eta(\theta)\bigr),
$$

a *$k$-parameter exponential family*.

<!-- Merge (owner approved 2026-11-21): the theta-indexed k-parameter form is MIT 18.650 Chapter 10; the rest of the definition is from Stanford CS229 Chapter 3. -->

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

::: {#fig-exponential-family-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[faint] (0,0) -- (2.2,0);
\path[bar] (0.525,0) rectangle (0.875,0.480);
\path[bar] (1.325,0) rectangle (1.675,1.120);
\node[tick, below] at (1.1,0) {Bernoulli: $\eta=\log\frac p{1-p}$};
\end{scope}
\begin{scope}[shift={(3.2,0)}]
\draw[faint] (0,0) -- (2.2,0);
\path[bar] (0.075,0) rectangle (0.225,0.224);
\path[bar] (0.315,0) rectangle (0.465,0.672);
\path[bar] (0.555,0) rectangle (0.705,1.008);
\path[bar] (0.795,0) rectangle (0.945,1.008);
\path[bar] (1.035,0) rectangle (1.185,0.756);
\path[bar] (1.275,0) rectangle (1.425,0.454);
\path[bar] (1.515,0) rectangle (1.665,0.227);
\path[bar] (1.755,0) rectangle (1.905,0.097);
\path[bar] (1.995,0) rectangle (2.145,0.036);
\node[tick, below] at (1.1,0) {Poisson: $\eta=\log\mu$};
\end{scope}
\begin{scope}[shift={(6.4,0)}]
\draw[faint] (0,0) -- (2.2,0);
\draw[emph, domain=0:2.2, samples=80, smooth, variable=\x] plot ({\x}, {0.9*exp(-((\x-1.1)^2)/(2*0.4^2))/(0.4*sqrt(2*pi))});
\node[tick, below] at (1.1,0) {normal: $\eta=\mu/\sigma^2$};
\end{scope}
\begin{scope}[shift={(9.6,0)}]
\draw[faint] (0,0) -- (2.2,0);
\draw[emph, domain=0.05:2.2, samples=80, smooth, variable=\x] plot ({\x}, {1.1*exp(-1.6*\x)});
\node[tick, below] at (1.1,0) {exponential: $\eta=-\lambda$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Four members of the exponential family with their natural parameters $\eta$ (the normal with known $\sigma^2$)

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

::: {#fig-exponential-family-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.4,0) -- (5.6,0) node[lab, right] {$\eta$};
\draw[->] (0,0) -- (0,3.0) node[lab, above] {$a(\eta)$};
\draw[emph, domain=-0.3:3.2, samples=80, smooth, variable=\x] plot ({\x}, {0.35*exp(\x*0.8)});
\draw[hl] (0.8,0.069) -- (3.0,3.120);
\node[hl dot] at (2.0,1.734) {};
\draw (2.0,0) -- (2.0,-0.08) node[tick, below] {$\eta_0$};
\node[tick, text=accent, right] at (2.4,1.93) {slope $a'(\eta_0)=E[T(Y)]$};
\end{tikzpicture}
\end{center}
```

The log-partition function $a(\eta)$ is convex. Its slope at $\eta_0$ is the mean of $T(Y)$ and its curvature the variance; for the Poisson family $a(\eta)=e^\eta$, so both equal $e^{\eta_0}$

:::

::: {#exm-exponential-family-moments .example name="Checking the moments"}

For the Bernoulli, $a'(\eta)=\dfrac{e^\eta}{1+e^\eta}=\phi$ and $a''(\eta)=\phi(1-\phi)$. For the unit-variance Gaussian, $a'(\eta)=\eta=\mu$ and $a''=1$. For the Poisson, $a'(\eta)=a''(\eta)=e^\eta=\lambda$: the mean and the variance of a Poisson variable are both $\lambda$.

:::

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 10 (the one-parameter canonical exponential family with a dispersion parameter, its mean and variance, the table of b functions and canonical links), in our own wording; the proof and the Gamma computation are our own. MIT 18.650 also writes a k-parameter family as exp(sum_i eta_i(theta) T_i(x) - B(theta)) h(x), now stated in def-exponential-family (merged 2026-11-21, owner approved). -->

Generalized linear models use a variant of the one-parameter family that separates the location of the distribution from its spread.

::: {#def-exponential-dispersion-family .definition name="Canonical exponential family with dispersion" generalizes="def-exponential-family"}

A family of mass or density functions on $\mathbb{R}$ is a *canonical exponential family with dispersion parameter $\phi>0$* if

$$
f_\theta(y)=\exp\Bigl(\frac{y\theta-b(\theta)}{\phi}+c(y,\phi)\Bigr)
$$

for known functions $b$ and $c$. The parameter $\theta$ is the *canonical parameter* and $\phi$ the *dispersion parameter*. For fixed known $\phi$ this is an exponential family in the sense of @def-exponential-family with natural parameter $\eta=\theta/\phi$, $T(y)=y$, log partition function $a(\eta)=b(\phi\eta)/\phi$ and base measure $e^{c(y,\phi)}$.

:::

::: {#fig-exponential-family-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.6,0) node[lab, right] {$y$};
\draw[hl, domain=0.4:6.2, samples=80, smooth, variable=\x] plot ({\x}, {2.0*exp(-((\x-3.2)^2)/(2*0.5^2))/(0.5*sqrt(2*pi))});
\draw[emph, domain=0.2:6.2, samples=80, smooth, variable=\x] plot ({\x}, {2.0*exp(-((\x-3.2)^2)/(2*1.0^2))/(1.0*sqrt(2*pi))});
\draw[faint, domain=0:6.2, samples=80, smooth, variable=\x] plot ({\x}, {2.0*exp(-((\x-3.2)^2)/(2*1.6^2))/(1.6*sqrt(2*pi))});
\draw (3.2,0) -- (3.2,-0.08) node[tick, below] {$b'(\theta)$};
\node[tick, text=accent] at (4.1,1.5) {small $\phi$};
\node[tick] at (5.4,0.4) {large $\phi$};
\end{tikzpicture}
\end{center}
```

Normal members of a dispersion family with the same $\theta$ (hence the same mean $b'(\theta)$) and different $\phi$: the variance $\phi\,b''(\theta)$ grows with the dispersion

:::

::: {#prp-dispersion-family-moments .proposition name="Mean and variance in a dispersion family" generalizes="prp-exponential-family-moments"}

If $Y$ has density $f_\theta$ as above, with $\theta$ in the interior of the parameter set, then

$$
\mu=E[Y]=b'(\theta),\qquad \mathrm{Var}(Y)=\phi\,b''(\theta).
$$

In particular $b''>0$ whenever $Y$ is not almost surely constant, so $b'$ is strictly increasing.

:::

::: {.proof}

1. With $\eta=\theta/\phi$ and $a(\eta)=b(\phi\eta)/\phi$ as in the definition, @prp-exponential-family-moments gives $E[Y]=a'(\eta)$ and $\mathrm{Var}(Y)=a''(\eta)$.

2. By the chain rule, $a'(\eta)=b'(\phi\eta)=b'(\theta)$ and $a''(\eta)=\phi\,b''(\phi\eta)=\phi\,b''(\theta)$.

3. A variance is positive unless the variable is constant, so $b''(\theta)>0$ in that case.

:::

The function $V(\mu)=b''\bigl((b')^{-1}(\mu)\bigr)$, the variance per unit dispersion written as a function of the mean, is the *variance function*.

::: {#exm-dispersion-families .example name="Four dispersion families"}

| Distribution | $\theta$ | $b(\theta)$ | $\phi$ | $\mu=b'(\theta)$ | $V(\mu)$ |
|---|---|---|---|---|---|
| $N(\mu,\sigma^2)$ | $\mu$ | $\theta^2/2$ | $\sigma^2$ | $\theta$ | $1$ |
| $\operatorname{Poisson}(\mu)$ | $\log\mu$ | $e^\theta$ | $1$ | $e^\theta$ | $\mu$ |
| $\operatorname{Ber}(\mu)$ | $\log\frac\mu{1-\mu}$ | $\log(1+e^\theta)$ | $1$ | $\frac{e^\theta}{1+e^\theta}$ | $\mu(1-\mu)$ |
| $\operatorname{Gamma}$, mean $\mu$, shape $\nu$ | $-1/\mu$ | $-\log(-\theta)$ | $1/\nu$ | $-1/\theta$ | $\mu^2$ |

For the normal, $\frac1{\sqrt{2\pi\sigma^2}}e^{-(y-\mu)^2/(2\sigma^2)}=\exp\bigl(\frac{y\mu-\mu^2/2}{\sigma^2}-\frac12(\frac{y^2}{\sigma^2}+\log(2\pi\sigma^2))\bigr)$. For the Gamma with shape $\nu$ and mean $\mu$ (scale $\mu/\nu$), the density $\frac1{\Gamma(\nu)}\bigl(\frac\nu\mu\bigr)^\nu y^{\nu-1}e^{-\nu y/\mu}$ equals $\exp\bigl(\nu\,(y\theta+\log(-\theta))+c(y,\phi)\bigr)$ with $\theta=-1/\mu$ and $c(y,\phi)=\nu\log\nu+(\nu-1)\log y-\log\Gamma(\nu)$; then $\mathrm{Var}(Y)=\phi\,b''(\theta)=\frac1\nu\cdot\frac1{\theta^2}=\mu^2/\nu$, the known Gamma variance.

:::

