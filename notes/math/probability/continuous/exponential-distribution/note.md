---
title: "Exponential Distribution"
sources: [cs70-20.3]
requires: [math/probability/continuous/continuous-random-variables, math/probability/discrete/geometric-distribution]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 20 (cs70-20.3), in our own wording; proofs written out in steps. -->

::: {#def-exponential-distribution .definition name="Exponential distribution"}

For $\lambda>0$, $X$ is *exponential* with rate $\lambda$, written $X\sim\mathrm{Exp}(\lambda)$, if it has density
$$f(x)=\begin{cases}\lambda e^{-\lambda x}&x\ge0,\\0&x<0.\end{cases}$$
It models a waiting time in continuous time: until a component fails, a request arrives, an apple falls.

:::

::: {#prp-exponential-tail .proposition name="Tail of the exponential distribution"}

If $X\sim\mathrm{Exp}(\lambda)$, then $f$ is a density and $\Pr(X>t)=e^{-\lambda t}$ for all $t\ge0$.

:::

::: {.proof}

1. $f\ge0$. For $t\ge0$, an antiderivative of $\lambda e^{-\lambda x}$ is $-e^{-\lambda x}$, so
   $$\Pr(X>t)=\int_t^\infty\lambda e^{-\lambda x}\,dx=\Bigl[-e^{-\lambda x}\Bigr]_t^\infty=0-(-e^{-\lambda t})=e^{-\lambda t}.$$

2. With $t=0$, the total integral is $1$, so $f$ is a density.

:::

::: {#thm-exponential-mean-variance .theorem name="Mean and variance of the exponential distribution"}

If $X\sim\mathrm{Exp}(\lambda)$, then $E[X]=\dfrac1\lambda$ and $\mathrm{Var}(X)=\dfrac1{\lambda^2}$.

:::

::: {.proof}

1. Integrate by parts with $u=x$, $dv=\lambda e^{-\lambda x}dx$, $v=-e^{-\lambda x}$:
   $$E[X]=\int_0^\infty x\lambda e^{-\lambda x}\,dx=\Bigl[-xe^{-\lambda x}\Bigr]_0^\infty+\int_0^\infty e^{-\lambda x}\,dx=0+\frac1\lambda.$$
   The boundary term is $0$ because $xe^{-\lambda x}\to0$ as $x\to\infty$.

2. In the same way, with $u=x^2$:
   $$E[X^2]=\int_0^\infty x^2\lambda e^{-\lambda x}\,dx=\Bigl[-x^2e^{-\lambda x}\Bigr]_0^\infty+\int_0^\infty 2xe^{-\lambda x}\,dx=0+\frac2\lambda E[X]=\frac2{\lambda^2}.$$

3. So $\mathrm{Var}(X)=E[X^2]-E[X]^2=\frac2{\lambda^2}-\frac1{\lambda^2}=\frac1{\lambda^2}$.

:::

::: {#prp-exponential-memoryless .proposition name="Memorylessness"}

If $X\sim\mathrm{Exp}(\lambda)$ and $s,t\ge0$, then $\Pr(X>s+t\mid X>s)=\Pr(X>t)$.

:::

::: {.proof}

1. The event $X>s+t$ is contained in $X>s$, so by @def-conditional-probability and @prp-exponential-tail,
   $$\Pr(X>s+t\mid X>s)=\frac{\Pr(X>s+t)}{\Pr(X>s)}=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}=\Pr(X>t).$$

:::

Having waited $s$ units of time without the event, the remaining wait has the same distribution as at the start.

## A limit of geometric distributions

::: {#prp-exponential-geometric-limit .proposition name="Exponential as a limit of geometric"}

Fix $\lambda>0$. For small $\delta>0$, perform one trial every $\delta$ time units, each succeeding with probability $p=\lambda\delta$, and let $Y_\delta$ be the time of the first success. Then for every $t>0$,
$$\Pr(Y_\delta>t)\to e^{-\lambda t}\qquad\text{as }\delta\to0.$$

:::

::: {.proof}

1. $Y_\delta=\delta N$ where $N\sim\mathrm{Geom}(\lambda\delta)$ (@def-geometric-distribution) is the number of the first successful trial.

2. $Y_\delta>t$ means $N>t/\delta$, that is, the first $k=\lfloor t/\delta\rfloor$ trials all fail. So $\Pr(Y_\delta>t)=(1-\lambda\delta)^{k}$.

3. Take logarithms: $k\ln(1-\lambda\delta)$. As $\delta\to0$, $\ln(1-\lambda\delta)=-\lambda\delta+O(\delta^2)$ and $k\delta\to t$, so $k\ln(1-\lambda\delta)\to-\lambda t$.

4. Since $\exp$ is continuous, $(1-\lambda\delta)^k\to e^{-\lambda t}$, which is $\Pr(X>t)$ for $X\sim\mathrm{Exp}(\lambda)$ (@prp-exponential-tail).

:::

::: {#rmk-exponential-rate}

So the exponential distribution is the continuous-time version of the geometric distribution. The rate $\lambda$ (successes per unit time) plays the role of $p$, but it can be larger than $1$. The means match too: $E[Y_\delta]=\delta\cdot\frac1{\lambda\delta}=\frac1\lambda$.

:::
