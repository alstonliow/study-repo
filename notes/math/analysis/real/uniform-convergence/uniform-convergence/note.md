---
title: "Pointwise and Uniform Convergence"
sources: [camib-at-a1]
requires: [math/analysis/real/sequences/cauchy-sequences, math/analysis/real/continuity/continuous-functions]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 1, in our own wording; examples chosen and checked by us; proofs written out in steps. -->

A sequence of functions can converge at every point and still lose continuity in the limit. Uniform convergence is the stronger notion that keeps it.

::: {#def-pointwise-convergence .definition name="Pointwise convergence"}

Let $E$ be a set and $f_n,f:E\to\mathbb R$. The sequence $(f_n)$ *converges pointwise* to $f$ on $E$ if $f_n(x)\to f(x)$ for every $x\in E$:
$$\forall x\in E\ \forall\varepsilon>0\ \exists N\ \forall n\ge N\quad |f_n(x)-f(x)|<\varepsilon.$$

:::

::: {#exm-pointwise-limit-discontinuous .example name="A pointwise limit that is not continuous"}

Let $f_n(x)=x^n$ on $[0,1]$. For $0\le x<1$, $x^n\to0$, and $f_n(1)=1$ for all $n$. So $f_n\to f$ pointwise, where $f(x)=0$ for $x<1$ and $f(1)=1$. Every $f_n$ is continuous but $f$ is not.

:::

::: {#exm-pointwise-integrals-fail .example name="Integrals need not converge"}

Let $f_n:[0,1]\to\mathbb R$ be the tent of height $n$ on $[0,\frac2n]$: it rises linearly from $0$ at $x=0$ to $n$ at $x=\frac1n$, falls back to $0$ at $x=\frac2n$, and is $0$ after that. Then $f_n(0)=0$, and for $x>0$ we have $f_n(x)=0$ once $\frac2n<x$; so $f_n\to0$ pointwise. But $\int_0^1f_n=\frac12\cdot\frac2n\cdot n=1$ for every $n$, while $\int_0^10=0$.

:::

In the definition $N$ may depend on $x$. Asking for one $N$ for all $x$ at once gives uniform convergence.

::: {#def-uniform-convergence .definition name="Uniform convergence"}

$(f_n)$ *converges uniformly* to $f$ on $E$ if
$$\forall\varepsilon>0\ \exists N\ \forall n\ge N\ \forall x\in E\quad |f_n(x)-f(x)|<\varepsilon.$$
Equivalently, $\sup_{x\in E}|f_n(x)-f(x)|\to0$ as $n\to\infty$ (the supremum may be $+\infty$ for small $n$).

:::

Uniform convergence implies pointwise convergence to the same limit, so when a uniform limit exists it is the pointwise limit.

::: {#exm-uniform-convergence-tests .example name="Checking uniform convergence"}

1. $f_n(x)=x^n$ on $[0,1]$ does not converge uniformly: $\sup_{[0,1]}|f_n-f|\ge\sup_{x<1}x^n=1$.
2. On $[0,a]$ with $a<1$ it does: $\sup_{[0,a]}|x^n|=a^n\to0$.
3. $f_n(x)=\frac xn$ on $\mathbb R$ converges pointwise to $0$, but $\sup_{\mathbb R}|f_n|=\infty$ for every $n$, so not uniformly. On any bounded interval $[-R,R]$ the supremum is $\frac Rn\to0$.

:::

## The uniform Cauchy criterion

::: {#def-uniformly-cauchy .definition name="Uniformly Cauchy sequence"}

$(f_n)$ is *uniformly Cauchy* on $E$ if
$$\forall\varepsilon>0\ \exists N\ \forall m,n\ge N\ \forall x\in E\quad |f_m(x)-f_n(x)|<\varepsilon.$$

:::

::: {#thm-uniform-cauchy-criterion .theorem name="General principle of uniform convergence"}

A sequence $f_n:E\to\mathbb R$ converges uniformly on $E$ if and only if it is uniformly Cauchy.

:::

::: {.proof}

1. *Uniformly convergent implies uniformly Cauchy.* If $f_n\to f$ uniformly, choose $N$ with $|f_n(x)-f(x)|<\frac\varepsilon2$ for all $n\ge N$ and all $x$. For $m,n\ge N$, $|f_m(x)-f_n(x)|\le|f_m(x)-f(x)|+|f(x)-f_n(x)|<\varepsilon$.

2. *Uniformly Cauchy gives a pointwise limit.* For each fixed $x$ the real sequence $(f_n(x))$ is Cauchy, so it converges by @thm-general-principle-of-convergence. Call the limit $f(x)$.

3. *The convergence is uniform.* Let $\varepsilon>0$ and take $N$ from the uniform Cauchy condition. For $m,n\ge N$ and every $x$, $|f_m(x)-f_n(x)|<\varepsilon$. Fix $n\ge N$ and $x$ and let $m\to\infty$: since limits preserve weak inequalities (@lem-limit-preserves-inequality), $|f(x)-f_n(x)|\le\varepsilon$. This holds for every $x$, with $N$ independent of $x$.

:::

The criterion lets us prove uniform convergence without knowing the limit in advance; the Weierstrass M-test (@thm-weierstrass-m-test) is its main application.

## Uniform limits of continuous functions

::: {#thm-uniform-limit-continuous .theorem name="Uniform limits preserve continuity"}

Let $E\subseteq\mathbb R$, $a\in E$, and $f_n\to f$ uniformly on $E$. If every $f_n$ is continuous at $a$, then $f$ is continuous at $a$. In particular a uniform limit of continuous functions is continuous.

:::

::: {.proof}

1. Let $\varepsilon>0$. Choose $N$ with $|f_N(x)-f(x)|<\frac\varepsilon3$ for all $x\in E$; here uniformity is used, since the same $N$ must work at $a$ and at every $x$ near $a$.

2. Since $f_N$ is continuous at $a$, there is $\delta>0$ with $|f_N(x)-f_N(a)|<\frac\varepsilon3$ for $x\in E$, $|x-a|<\delta$.

3. For such $x$,
$$|f(x)-f(a)|\le|f(x)-f_N(x)|+|f_N(x)-f_N(a)|+|f_N(a)-f(a)|<\tfrac\varepsilon3+\tfrac\varepsilon3+\tfrac\varepsilon3=\varepsilon.$$

:::

So @exm-pointwise-limit-discontinuous gives a second proof that $x^n$ does not converge uniformly on $[0,1]$: the limit is discontinuous.

::: {#rmk-uniform-convergence-1 .remark name="Swapping limits"}

The theorem says $\lim_{x\to a}\lim_{n\to\infty}f_n(x)=\lim_{n\to\infty}\lim_{x\to a}f_n(x)$ under uniform convergence. Exchanging two limiting processes always needs a justification of this kind; the next note does the same for integrals and derivatives.

:::
