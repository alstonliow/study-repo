---
title: "Gamma Distribution"
sources: [camib-st-1, camib-sts-1-q2]
requires: [math/probability/joint-distributions/transforms]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 1 (review of the gamma, beta and chi-squared distributions), in our own wording; proofs written out in steps. -->

The exponential distribution models one waiting time. Adding independent waiting times leads to the gamma family, which also contains the chi-squared distributions that appear throughout normal-sampling theory.

::: {#def-gamma-distribution .definition name="Gamma distribution"}

For a *shape* $\alpha>0$ and a *rate* $\lambda>0$, a random variable $X$ has the *gamma distribution* $\mathrm{Gamma}(\alpha,\lambda)$ if it has the density
$$
f(x)=\frac{\lambda^{\alpha}x^{\alpha-1}e^{-\lambda x}}{\Gamma(\alpha)},\qquad x>0,
$$
where $\Gamma(\alpha)=\int_0^\infty x^{\alpha-1}e^{-x}\,dx$ satisfies $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$, $\Gamma(n)=(n-1)!$ for $n\in\mathbb N$, and $\Gamma(\tfrac12)=\sqrt\pi$.

:::

::: {#fig-gamma-distribution-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=3cm]
\draw[->, muted] (0,0) -- (10.5,0) node[lab, right] {$x$};
\draw[->, muted] (0,0) -- (0,1.05);
\foreach \x in {2,4,6,8,10} \node[tick, below] at (\x,0) {$\x$};
\foreach \y in {0.5,1} \node[tick, left] at (0,\y) {$\y$};
\draw[emph, primary, domain=0:10, samples=60] plot (\x,{exp(-\x)});
\draw[emph, secondary, domain=0:10, samples=60] plot (\x,{\x*exp(-\x)});
\draw[emph, accent, domain=0:10, samples=60] plot (\x,{\x*\x*\x*exp(-\x)/6});
\node[lab, primary] at (1.8,0.85) {$\alpha=1$};
\node[lab, secondary] at (2.6,0.5) {$\alpha=2$};
\node[lab, accent] at (6.2,0.3) {$\alpha=4$};
\end{tikzpicture}
\end{center}
```

Gamma densities with rate $\lambda=1$. Shape $1$ is the exponential density; larger shapes move the mass to the right and make the curve more symmetric.

:::

::: {#prp-gamma-properties .proposition name="Moments, scaling and moment generating function"}

Let $X\sim\mathrm{Gamma}(\alpha,\lambda)$. Then

1. $\mathrm{Gamma}(1,\lambda)$ is the exponential distribution with rate $\lambda$;
2. $E(X)=\alpha/\lambda$ and $\mathrm{Var}(X)=\alpha/\lambda^2$;
3. $E(e^{tX})=(1-t/\lambda)^{-\alpha}$ for $t<\lambda$;
4. $cX\sim\mathrm{Gamma}(\alpha,\lambda/c)$ for every $c>0$.

:::

::: {.proof}

1. For $\alpha=1$ the density is $\lambda e^{-\lambda x}$, as $\Gamma(1)=1$.

2. For $t<\lambda$,
$$E(e^{tX})=\int_0^\infty\frac{\lambda^\alpha x^{\alpha-1}e^{-(\lambda-t)x}}{\Gamma(\alpha)}\,dx=\Bigl(\frac{\lambda}{\lambda-t}\Bigr)^{\alpha}\int_0^\infty\frac{(\lambda-t)^\alpha x^{\alpha-1}e^{-(\lambda-t)x}}{\Gamma(\alpha)}\,dx=\Bigl(\frac{\lambda}{\lambda-t}\Bigr)^{\alpha},$$
because the last integrand is the $\mathrm{Gamma}(\alpha,\lambda-t)$ density. This is item 3.

3. Differentiating $M(t)=(1-t/\lambda)^{-\alpha}$ at $t=0$ gives $E(X)=M'(0)=\alpha/\lambda$ and $E(X^2)=M''(0)=\alpha(\alpha+1)/\lambda^2$, so $\mathrm{Var}(X)=\alpha/\lambda^2$.

4. $E(e^{t\,cX})=(1-ct/\lambda)^{-\alpha}$ is the moment generating function of $\mathrm{Gamma}(\alpha,\lambda/c)$, and the moment generating function determines the distribution (@thm-transform-properties).

:::

::: {#thm-gamma-additivity .theorem name="Sums of gamma variables"}

If $X_i\sim\mathrm{Gamma}(\alpha_i,\lambda)$, $i=1,\dots,n$, are independent with the same rate, then
$$
X_1+\dots+X_n\sim\mathrm{Gamma}\Bigl(\sum_{i=1}^n\alpha_i,\ \lambda\Bigr).
$$

:::

::: {.proof}

1. By independence the moment generating function of the sum is the product $\prod_i(1-t/\lambda)^{-\alpha_i}=(1-t/\lambda)^{-\sum_i\alpha_i}$ for $t<\lambda$.

2. This is the moment generating function of $\mathrm{Gamma}(\sum\alpha_i,\lambda)$ (@prp-gamma-properties), and it determines the distribution.

:::

::: {#exm-erlang .example name="The sum of exponential waiting times"}

If $T_1,\dots,T_n$ are independent $\mathrm{Exp}(\lambda)$, then $T_1+\dots+T_n\sim\mathrm{Gamma}(n,\lambda)$ by @thm-gamma-additivity: the time of the $n$-th arrival of a Poisson process of rate $\lambda$ has mean $n/\lambda$ and variance $n/\lambda^2$.

:::

::: {#thm-beta-from-gamma .theorem name="Beta variable from two gamma variables"}

Let $X\sim\mathrm{Gamma}(\alpha,\lambda)$ and $Y\sim\mathrm{Gamma}(\beta,\lambda)$ be independent. Then $U=X+Y\sim\mathrm{Gamma}(\alpha+\beta,\lambda)$ and $V=X/(X+Y)$ has the density
$$
\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\,v^{\alpha-1}(1-v)^{\beta-1},\qquad 0<v<1,
$$
that is, $V\sim\mathrm{Beta}(\alpha,\beta)$ (@def-beta-distribution), and $U$ and $V$ are independent.

:::

::: {.proof}

1. The map $(x,y)\mapsto(u,v)=(x+y,\ x/(x+y))$ is a bijection from $(0,\infty)^2$ onto $(0,\infty)\times(0,1)$ with inverse $x=uv$, $y=u(1-v)$. Its Jacobian determinant is
$$\left|\det\begin{pmatrix}v&u\\1-v&-u\end{pmatrix}\right|=u.$$

2. By independence and the change-of-variables formula (@thm-change-of-variables-density) the joint density of $(U,V)$ is
$$
\frac{\lambda^{\alpha+\beta}(uv)^{\alpha-1}\bigl(u(1-v)\bigr)^{\beta-1}e^{-\lambda u}}{\Gamma(\alpha)\Gamma(\beta)}\,u
=\frac{\lambda^{\alpha+\beta}u^{\alpha+\beta-1}e^{-\lambda u}}{\Gamma(\alpha+\beta)}\cdot\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\,v^{\alpha-1}(1-v)^{\beta-1}.
$$

3. The density factorises into a function of $u$ and a function of $v$, each of them a probability density. Hence $U$ and $V$ are independent with the stated laws.

:::

::: {#prp-chi-square-gamma .proposition name="The chi-squared distribution is a gamma distribution"}

If $Z_1,\dots,Z_k$ are independent $N(0,1)$, then $\chi^2_k=Z_1^2+\dots+Z_k^2\sim\mathrm{Gamma}(k/2,\,1/2)$ (@def-chi-square-distribution). In particular $E(\chi^2_k)=k$ and $\mathrm{Var}(\chi^2_k)=2k$.

:::

::: {.proof}

1. For $t>0$, $P(Z^2\le t)=P(-\sqrt t\le Z\le\sqrt t)$, and differentiating in $t$ gives the density
$$\frac{1}{\sqrt{2\pi}}\,t^{-1/2}e^{-t/2}.$$

2. Since $\Gamma(\tfrac12)=\sqrt\pi$, the $\mathrm{Gamma}(\tfrac12,\tfrac12)$ density is $(1/2)^{1/2}t^{-1/2}e^{-t/2}/\sqrt\pi$, which is the same function. So $Z_1^2\sim\mathrm{Gamma}(\tfrac12,\tfrac12)$.

3. By @thm-gamma-additivity the sum of $k$ independent copies is $\mathrm{Gamma}(k/2,1/2)$; the moments follow from @prp-gamma-properties.

:::
