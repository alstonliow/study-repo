---
title: "Iterated Expectations and Random Sums"
sources: [mit6041-12]
requires: [math/probability/continuous/transforms]
status: draft
---

<!-- Added 2026-11-20 from MIT 6.041 (Fall 2010), Lecture 12, in our own wording; proofs written out in steps. -->

The conditional expectation given an event (@def-conditional-expectation) becomes a random variable once the event is "$Y$ takes its observed value".

::: {#def-conditional-expectation-random-variable .definition name="Conditional expectation and variance given a random variable"}

For random variables $X$ and $Y$ let $g(y)=E[X\mid Y=y]$. The *conditional expectation of $X$ given $Y$* is the random variable
$$E[X\mid Y]=g(Y).$$
Likewise $\mathrm{Var}(X\mid Y)$ is the random variable $v(Y)$, where $v(y)=E\bigl[(X-g(y))^2\mid Y=y\bigr]$.

:::

::: {#thm-iterated-expectations .theorem name="Law of iterated expectations" generalizes="thm-total-expectation"}

$$E\bigl[E[X\mid Y]\bigr]=E[X].$$

:::

::: {.proof}

1. For discrete $Y$, $E[g(Y)]=\sum_yg(y)\,p_Y(y)=\sum_yE[X\mid Y=y]\Pr(Y=y)$.

2. The events $\{Y=y\}$ partition the sample space, so the law of total expectation (@thm-total-expectation) gives $E[X]$.

3. For continuous $Y$ the same computation with integrals reads $\int E[X\mid Y=y]f_Y(y)\,dy=\iint xf_{X\mid Y}(x\mid y)f_Y(y)\,dx\,dy=\iint xf_{X,Y}(x,y)\,dx\,dy=E[X]$.

:::

::: {#thm-total-variance .theorem name="Law of total variance"}

$$\mathrm{Var}(X)=E\bigl[\mathrm{Var}(X\mid Y)\bigr]+\mathrm{Var}\bigl(E[X\mid Y]\bigr).$$

:::

::: {.proof}

1. Given $Y=y$, $\mathrm{Var}(X\mid Y=y)=E[X^2\mid Y=y]-g(y)^2$, so $\mathrm{Var}(X\mid Y)=E[X^2\mid Y]-g(Y)^2$.

2. Take expectations and use @thm-iterated-expectations: $E[\mathrm{Var}(X\mid Y)]=E[X^2]-E[g(Y)^2]$.

3. Also $\mathrm{Var}(g(Y))=E[g(Y)^2]-(E[g(Y)])^2=E[g(Y)^2]-(E[X])^2$.

4. Adding the two lines, $E[g(Y)^2]$ cancels and the sum is $E[X^2]-(E[X])^2=\mathrm{Var}(X)$.

:::

In words: total spread = average spread within the groups $\{Y=y\}$ + spread of the group means.

::: {#exm-stick-breaking .example name="Breaking a stick twice"}

Break a stick of length $\ell$ at a uniform point $Y$, keep the piece $[0,Y]$, and break it again at a uniform point $X$ of $[0,Y]$. Given $Y$, $X$ is uniform on $[0,Y]$, so $E[X\mid Y]=Y/2$ and $\mathrm{Var}(X\mid Y)=Y^2/12$. Hence
$$E[X]=E[Y]/2=\ell/4,\qquad\mathrm{Var}(X)=\frac{E[Y^2]}{12}+\frac{\mathrm{Var}(Y)}4=\frac{\ell^2}{36}+\frac{\ell^2}{48}=\frac{7\ell^2}{144}.$$

:::

::: {#thm-random-sum .theorem name="Sum of a random number of random variables"}

Let $X_1,X_2,\dots$ be independent and identically distributed with mean $\mu$, variance $\sigma^2$ and transform $M_X$, and let $N$ be a nonnegative integer random variable independent of them. Then $Y=X_1+\dots+X_N$ satisfies
$$E[Y]=E[N]\,\mu,\qquad\mathrm{Var}(Y)=E[N]\,\sigma^2+\mu^2\,\mathrm{Var}(N),\qquad M_Y(s)=E\bigl[M_X(s)^N\bigr].$$

:::

::: {.proof}

1. Given $N=n$, $Y$ is a sum of $n$ fixed independent terms, so $E[Y\mid N]=N\mu$, $\mathrm{Var}(Y\mid N)=N\sigma^2$ and $E[e^{sY}\mid N]=M_X(s)^N$ (@thm-transform-properties).

2. Iterated expectations (@thm-iterated-expectations) give $E[Y]=E[N\mu]=E[N]\mu$ and $M_Y(s)=E[M_X(s)^N]$.

3. Total variance (@thm-total-variance) gives $\mathrm{Var}(Y)=E[N\sigma^2]+\mathrm{Var}(N\mu)=E[N]\sigma^2+\mu^2\mathrm{Var}(N)$.

:::

The transform is the transform of $N$ with $e^s$ replaced by $M_X(s)$: write $M_N(s)=E[e^{sN}]$; then $M_Y(s)=M_N(\ln M_X(s))$.

::: {#exm-geometric-sum-of-exponentials .example name="A geometric number of exponentials"}

Let $N\sim\mathrm{Geom}(p)$ and $X_i\sim\operatorname{Exp}(\lambda)$. Then $E[z^N]=\frac{pz}{1-(1-p)z}$ and $M_X(s)=\frac{\lambda}{\lambda-s}$ for $s<\lambda$, so
$$M_Y(s)=\frac{p\lambda/(\lambda-s)}{1-(1-p)\lambda/(\lambda-s)}=\frac{p\lambda}{p\lambda-s},$$
the transform of $\operatorname{Exp}(p\lambda)$. A geometric number of exponential waits is again exponential, with mean $\frac1p\cdot\frac1\lambda$.

:::
