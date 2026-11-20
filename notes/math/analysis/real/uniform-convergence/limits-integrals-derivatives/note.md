---
title: "Uniform Limits, Integrals and Derivatives"
sources: [camib-at-a1, camib-at-a3]
requires: [math/analysis/real/uniform-convergence/uniform-convergence, math/analysis/real/integration/integrable-functions]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Sections 1 and 3.2, in our own wording; the counterexample is ours (checked numerically); proofs written out in steps. -->

Uniform convergence allows limits to be taken inside integrals. For derivatives it is the derivatives that must converge uniformly. The counterexamples in @sec-math-analysis-real-uniform-convergence-uniform-convergence show that pointwise convergence is not enough for either.

## Integrals

::: {#thm-uniform-limit-integral .theorem name="Uniform limits and integrals"}

Let $f_n:[a,b]\to\mathbb R$ be Riemann integrable and $f_n\to f$ uniformly on $[a,b]$. Then $f$ is Riemann integrable and
$$\int_a^bf_n(x)\,dx\to\int_a^bf(x)\,dx.$$

:::

::: {.proof}

1. *$f$ is bounded.* Take $N$ with $|f_N-f|<1$ on $[a,b]$; $f_N$ is bounded, so $f$ is.

2. *$f$ is integrable.* Let $\varepsilon>0$ and put $\eta=\frac{\varepsilon}{3(b-a)}$. Choose $n$ with $|f_n(x)-f(x)|\le\eta$ for all $x$. By @thm-riemann-criterion there is a dissection $D$ with $U_D(f_n)-L_D(f_n)<\frac\varepsilon3$. On each subinterval, $\sup f\le\sup f_n+\eta$ and $\inf f\ge\inf f_n-\eta$, so
$$U_D(f)-L_D(f)\le U_D(f_n)-L_D(f_n)+2\eta(b-a)<\tfrac\varepsilon3+\tfrac{2\varepsilon}3=\varepsilon.$$
By @thm-riemann-criterion again, $f$ is integrable.

3. *The integrals converge.* By linearity and monotonicity (@thm-integral-linear, @prp-integral-monotone),
$$\Bigl|\int_a^bf_n-\int_a^bf\Bigr|\le\int_a^b|f_n-f|\le(b-a)\sup_{[a,b]}|f_n-f|\to0.$$

:::

::: {#cor-uniform-limit-indefinite-integral .corollary name="Indefinite integrals converge uniformly"}

Under the hypotheses of @thm-uniform-limit-integral, $F_n(x)=\int_a^xf_n\to F(x)=\int_a^xf$ uniformly on $[a,b]$.

:::

::: {.proof}

1. For every $x\in[a,b]$, step 3 of the previous proof on $[a,x]$ gives $|F_n(x)-F(x)|\le(x-a)\sup|f_n-f|\le(b-a)\sup|f_n-f|$.

2. The right-hand side does not depend on $x$ and tends to $0$.

:::

## Derivatives

Uniform convergence of $f_n$ says nothing about $f_n'$.

::: {#exm-uniform-limit-derivative-fails .example name="Uniform convergence does not control derivatives"}

Let $f_n(x)=\frac1n\sin(n^2x)$ on $\mathbb R$. Then $|f_n|\le\frac1n$, so $f_n\to0$ uniformly. But $f_n'(x)=n\cos(n^2x)$, and $f_n'(0)=n\to\infty$; the derivatives do not converge to the derivative $0$ of the limit.

:::

::: {#thm-uniform-limit-derivative .theorem name="Differentiating a limit"}

Let $f_n:[a,b]\to\mathbb R$ be differentiable on $[a,b]$ (one-sided at the ends). Suppose

1. $f_n'\to g$ uniformly on $[a,b]$, and
2. $(f_n(c))$ converges for some $c\in[a,b]$.

Then $f_n$ converges uniformly on $[a,b]$ to a differentiable function $f$, and $f'=g$.

:::

::: {.proof}

1. *Key estimate.* For $m,n$ put $h=f_m-f_n$ and $s_{mn}=\sup_{[a,b]}|f_m'-f_n'|$. For $x\ne y$ in $[a,b]$ the mean value theorem (@thm-mean-value) gives a $t$ between them with
$$|h(x)-h(y)|=|h'(t)||x-y|\le s_{mn}|x-y|.\qquad(1)$$
By hypothesis 1 and @thm-uniform-cauchy-criterion, $s_{mn}\to0$ as $m,n\to\infty$.

2. *$(f_n)$ is uniformly Cauchy.* By (1) with $y=c$,
$$|f_m(x)-f_n(x)|\le|f_m(c)-f_n(c)|+s_{mn}(b-a).$$
Both terms are small for large $m,n$, independently of $x$. By @thm-uniform-cauchy-criterion, $f_n\to f$ uniformly for some $f$.

3. *Difference quotients.* Fix $y\in[a,b]$ and define $\varphi_n(x)=\frac{f_n(x)-f_n(y)}{x-y}$ for $x\ne y$ and $\varphi_n(y)=f_n'(y)$. Each $\varphi_n$ is continuous at $y$, by differentiability of $f_n$.

4. *$(\varphi_n)$ is uniformly Cauchy.* For $x\ne y$, (1) gives $|\varphi_m(x)-\varphi_n(x)|=\frac{|h(x)-h(y)|}{|x-y|}\le s_{mn}$; at $x=y$, $|\varphi_m(y)-\varphi_n(y)|=|f_m'(y)-f_n'(y)|\le s_{mn}$. So $\varphi_n$ converges uniformly, and its pointwise limit is $\varphi(x)=\frac{f(x)-f(y)}{x-y}$ for $x\ne y$ and $\varphi(y)=g(y)$.

5. *Conclusion.* By @thm-uniform-limit-continuous, $\varphi$ is continuous at $y$, that is, $\frac{f(x)-f(y)}{x-y}\to g(y)$ as $x\to y$. So $f'(y)=g(y)$.

:::

::: {#rmk-limits-integrals-derivatives-1 .remark name="An easier proof with continuous derivatives"}

If the $f_n'$ are also continuous, the theorem follows from integrals. By @thm-ftc-integrable-derivative, $f_n(x)=f_n(c)+\int_c^xf_n'$; by @cor-uniform-limit-indefinite-integral the right-hand side converges uniformly to $L+\int_c^xg$, where $L=\lim f_n(c)$; and $g$ is continuous by @thm-uniform-limit-continuous, so @thm-ftc-continuous-integrand shows this limit has derivative $g$. The proof above needs no continuity of $f_n'$.

:::
