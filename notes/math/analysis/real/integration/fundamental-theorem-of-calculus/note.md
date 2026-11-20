---
title: "The Fundamental Theorem of Calculus, Rigorously"
sources: [cama1-7]
requires: [math/analysis/real/integration/integrable-functions, math/analysis/real/differentiability/taylors-theorem, math/calculus/single-variable/integrals/fundamental-theorem]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 7.1 (end), in our own wording; proofs written out in steps. The two fundamental theorems and substitution are in @sec-math-calculus-single-variable-integrals-fundamental-theorem, proved there with the Riemann-sum integral; here they rest on @def-riemann-integral-darboux, and the second needs only an integrable derivative. Substitution is not repeated: its proof there carries over once the theorems below are in place. The integral test (@thm-integral-test) and improper integrals (@def-improper-integral) likewise carry over, using @thm-monotone-integrable. -->

## Differentiating an integral

::: {#thm-ftc-continuous-integrand .theorem name="Fundamental theorem of calculus, part 1" related="thm-ftc-2"}

Let $f:[a,b]\to\mathbb R$ be continuous and $F(x)=\int_a^xf(t)\,dt$. Then $F$ is differentiable on $[a,b]$ (one-sided at the ends) and
$$F'(x)=f(x).$$

:::

::: {.proof}

1. $F$ is defined because $f$ is integrable on every $[a,x]$ (@thm-continuous-integrable). By @thm-integral-additive, for $h\ne0$ with $x+h\in[a,b]$,
$$\frac{F(x+h)-F(x)}h-f(x)=\frac1h\int_x^{x+h}\bigl(f(t)-f(x)\bigr)\,dt.$$

2. Let $\varepsilon>0$. By continuity at $x$ there is $\delta>0$ with $|f(t)-f(x)|<\varepsilon$ whenever $|t-x|<\delta$.

3. If $0<|h|<\delta$, every $t$ between $x$ and $x+h$ satisfies this, so by @prp-integral-monotone the right side of step 1 has modulus at most $\frac1{|h|}\cdot\varepsilon|h|=\varepsilon$.

:::

Without continuity this can fail: for the step function $f=0$ on $[-1,0]$ and $f=1$ on $(0,1]$, $F(x)=\max(x,0)$ is not differentiable at $0$.

## Integrating a derivative

::: {#thm-ftc-integrable-derivative .theorem name="Fundamental theorem of calculus, part 2" related="thm-ftc-1"}

Let $f$ be differentiable on $[a,b]$ with $f'$ Riemann integrable. Then
$$\int_a^bf'(t)\,dt=f(b)-f(a).$$

:::

::: {.proof}

1. Let $D:a=x_0<\cdots<x_n=b$ be any dissection. Telescoping, $f(b)-f(a)=\sum_{i=1}^n\bigl(f(x_i)-f(x_{i-1})\bigr)$.

2. By the mean value theorem (@thm-mean-value), $f(x_i)-f(x_{i-1})=(x_i-x_{i-1})f'(u_i)$ for some $u_i\in(x_{i-1},x_i)$.

3. Since $m_i(f')\le f'(u_i)\le M_i(f')$, summing gives $L_D(f')\le f(b)-f(a)\le U_D(f')$.

4. This holds for every $D$, so $\underline\int f'\le f(b)-f(a)\le\overline\int f'$. As $f'$ is integrable, both ends equal $\int_a^bf'$.

:::

This does not assume $f'$ continuous, only integrable. The hypothesis cannot be dropped altogether: there are differentiable functions whose derivative is unbounded on $[a,b]$, hence not Riemann integrable. When $f'$ is continuous, part 1 gives a second proof: $G(x)=\int_a^xf'$ and $f$ have the same derivative, so they differ by a constant (@cor-sign-of-derivative), which is $-f(a)$.

::: {#thm-integration-by-parts-proof .theorem name="Integration by parts"}

If $f,g$ are differentiable on $[a,b]$ with $f',g'$ integrable, then
$$\int_a^bf(x)g'(x)\,dx=f(b)g(b)-f(a)g(a)-\int_a^bf'(x)g(x)\,dx.$$

:::

::: {.proof}

1. $f,g$ are continuous (@thm-differentiable-continuous), hence integrable, so $f'g$ and $fg'$ are integrable (@prp-integral-product) and so is their sum $(fg)'$ (@thm-integral-linear).

2. By @thm-ftc-integrable-derivative and linearity, $\int_a^bfg'+\int_a^bf'g=\int_a^b(fg)'=f(b)g(b)-f(a)g(a)$. Rearrange.

:::

Integration by parts is the product rule integrated; substitution (@thm-substitution-definite) is the chain rule integrated.

## Taylor's theorem with integral remainder

::: {#thm-taylor-integral-remainder .theorem name="Taylor's theorem with integral remainder"}

Let $f$ be $n+1$ times differentiable on $[a,b]$ with $f^{(n+1)}$ continuous. Then
$$f(b)=\sum_{k=0}^n\frac{(b-a)^k}{k!}f^{(k)}(a)+\int_a^b\frac{(b-t)^n}{n!}f^{(n+1)}(t)\,dt.$$

:::

::: {.proof}

1. *Induction on $n$.* For $n=0$ the claim is $f(b)=f(a)+\int_a^bf'$, which is @thm-ftc-integrable-derivative.

2. Assume the claim for $n-1$ (with $f$ now $n+1$ times continuously differentiable); its remainder is $\int_a^b\frac{(b-t)^{n-1}}{(n-1)!}f^{(n)}(t)\,dt$.

3. Integrate by parts (@thm-integration-by-parts-proof) with $u=f^{(n)}$ and $v=-\frac{(b-t)^n}{n!}$, so $v'=\frac{(b-t)^{n-1}}{(n-1)!}$:
$$\int_a^b\frac{(b-t)^{n-1}}{(n-1)!}f^{(n)}(t)\,dt=\Bigl[-\frac{(b-t)^n}{n!}f^{(n)}(t)\Bigr]_a^b+\int_a^b\frac{(b-t)^n}{n!}f^{(n+1)}(t)\,dt.$$

4. The bracket equals $\frac{(b-a)^n}{n!}f^{(n)}(a)$, the next term of the Taylor polynomial. Substituting into the case $n-1$ gives the case $n$.

:::

The form of the remainder is what repeated integration by parts produces, starting from $f(b)=f(a)+\int_a^bf'(t)\,dt$ and always integrating the polynomial factor as a power of $(b-t)$, so that the boundary term at $t=b$ vanishes. Since $\int_a^b\frac{(b-t)^n}{n!}dt=\frac{(b-a)^{n+1}}{(n+1)!}$, bounding $f^{(n+1)}$ between its minimum and maximum on $[a,b]$ and applying the intermediate value theorem to it recovers the Lagrange form (@thm-taylor-lagrange).
