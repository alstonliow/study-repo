---
title: "Power Series and Taylor Series"
sources: [mit1801-37]
requires: [math/calculus/single-variable/series/infinite-series, math/calculus/single-variable/applications-of-derivatives/linear-and-quadratic-approximation]
aliases: [math/calculus/series/taylor-series]   # old ids (moved)
relations:
  related: [math/discrete/counting/generating-functions]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 37, in our own wording; proofs written out in steps. Numbers checked in Python. -->

::: {#def-power-series .definition name="Power series, radius of convergence"}

A power series is $\sum_{n=0}^\infty a_nx^n$. There is $R\in[0,\infty]$, the radius of convergence, such that the series converges for $\lvert x\rvert<R$ and diverges for $\lvert x\rvert>R$; at $x=\pm R$ anything can happen.

:::

The geometric series $\sum x^n=\frac1{1-x}$ has $R=1$. Inside the radius of convergence, power series can be added, multiplied, substituted into, and differentiated and integrated term by term, like polynomials (we use this without proof).

::: {#exm-series-from-geometric .example name="Series from the geometric series"}

- Substitute $x=-u$: $\frac1{1+u}=1-u+u^2-\cdots$.
- Integrate from $0$ to $x$: $\ln(1+x)=x-\frac{x^2}2+\frac{x^3}3-\cdots$ for $\lvert x\rvert<1$.
- Substitute $x=-v^2$ and integrate: $\tan^{-1}x=x-\frac{x^3}3+\frac{x^5}5-\cdots$.

:::

::: {#thm-taylor-coefficients .theorem name="Taylor coefficients"}

If $f(x)=\sum_{n=0}^\infty a_nx^n$ for $\lvert x\rvert<R$, then
$$a_n=\frac{f^{(n)}(0)}{n!} .$$

:::

::: {.proof}

1. Differentiating term by term $n$ times, the terms with $k<n$ vanish and the term $a_nx^n$ becomes $n!\,a_n$ (@prp-nth-derivative-power).

2. The terms with $k>n$ still contain a factor $x$, so at $x=0$ they vanish: $f^{(n)}(0)=n!\,a_n$.

:::

::: {#def-taylor-series .definition name="Taylor series"}

The Taylor series of $f$ at $a$ is
$$\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x-a)^n .$$

:::

The partial sums are the best polynomial approximations of each degree; the first two are the linear and quadratic approximations (@def-quadratic-approximation).

::: {#prp-standard-taylor-series .proposition name="Standard series"}

For all real $x$,
$$e^x=\sum_{n=0}^\infty\frac{x^n}{n!},\qquad \sin x=\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{(2n+1)!},\qquad \cos x=\sum_{n=0}^\infty\frac{(-1)^nx^{2n}}{(2n)!} ,$$
and for $\lvert x\rvert<1$, $(1+x)^r=1+rx+\frac{r(r-1)}{2!}x^2+\frac{r(r-1)(r-2)}{3!}x^3+\cdots$.

:::

::: {#thm-taylor-remainder .theorem name="Taylor's formula with remainder"}

If $f^{(n+1)}$ is continuous between $a$ and $x$, then
$$f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x),\qquad R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$
for some $c$ between $a$ and $x$.

:::

We use the remainder formula without proof (it follows from repeated use of the mean value theorem). It shows the series for $e^x$, $\sin x$, $\cos x$ converge to the functions: the remainders are at most $\frac{M\lvert x\rvert^{n+1}}{(n+1)!}\to0$.

::: {#exm-compute-e .example name="Computing $e$"}

$e=\sum\frac1{n!}$. Summing to $n=10$ gives $2.718281801$, and the remainder is at most $\frac{e}{11!}<7\times10^{-8}$; indeed $e=2.718281828\ldots$

:::
