---
title: "Limits of Functions and Differentiability"
sources: [cama1-5]
requires: [math/analysis/real/continuity/extreme-and-intermediate-values, math/calculus/single-variable/differentiation/differentiation-rules]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 5.1, 5.2 and 5.4, in our own wording; proofs written out in steps. The derivative and the rules of differentiation, with proofs, are in @sec-math-calculus-single-variable-differentiation-derivative, @sec-math-calculus-single-variable-differentiation-differentiation-rules and @sec-math-calculus-single-variable-differentiation-chain-rule; this note adds the little-o view of the derivative and the differentiability of inverse functions. -->

## Limits of functions

For $A\subseteq\mathbb R$ and $f:A\to\mathbb R$, $\lim_{x\to a}f(x)=\ell$ is defined as in @def-limit-of-a-function, with $x$ restricted to $A$: for every $\varepsilon>0$ there is $\delta>0$ with $|f(x)-\ell|<\varepsilon$ for all $x\in A$ with $0<|x-a|<\delta$. The condition $0<|x-a|$ means the value at $a$, if there is one, plays no part. For example, if $f(x)=x$ for $x\ne2$ and $f(2)=3$, then $\lim_{x\to2}f(x)=2\ne f(2)$.

Comparing with @def-continuity-epsilon-delta: $f(x)\to\ell$ as $x\to a$ exactly when the function equal to $f$ away from $a$ and to $\ell$ at $a$ is continuous at $a$. So @thm-sequential-continuity gives:

::: {#thm-sequential-limit .theorem name="Limits through sequences"}

$\lim_{x\to a}f(x)=\ell$ if and only if $f(x_n)\to\ell$ for every sequence $(x_n)$ in $A\setminus\{a\}$ with $x_n\to a$.

:::

Consequently the limit laws for functions (@prp-limit-laws-functions) follow from those for sequences.

## The derivative as a linear approximation

::: {#def-little-o .definition name="Little-o notation"}

$o(h)$ denotes any function $\varepsilon(h)\,h$ with $\varepsilon(h)\to0$ as $h\to0$; that is, a quantity $r(h)$ with
$$\frac{r(h)}{h}\to0\quad\text{as }h\to0.$$

:::

::: {#prp-derivative-little-o .proposition name="Derivative as a linear approximation"}

$f$ is differentiable at $x$ with derivative $\lambda$ (@def-derivative) if and only if
$$f(x+h)=f(x)+\lambda h+o(h).$$

:::

::: {.proof}

1. Put $r(h)=f(x+h)-f(x)-\lambda h$ for $h\ne0$. Then $\dfrac{r(h)}{h}=\dfrac{f(x+h)-f(x)}{h}-\lambda$.

2. So $r(h)/h\to0$ exactly when the difference quotient tends to $\lambda$.

:::

The line $f(x)+\lambda h$ is the best linear approximation to $f$ near $x$: any other slope leaves an error that is not $o(h)$. The rules of differentiation become short calculations with the conventions $o(h)+o(h)=o(h)$, $c\cdot o(h)=o(h)$ for a bounded factor $c$, and $h\cdot h=o(h)$. For example, the product rule:
$$f(x+h)g(x+h)=\bigl(f(x)+hf'(x)+o(h)\bigr)\bigl(g(x)+hg'(x)+o(h)\bigr)=f(x)g(x)+h\bigl(f'(x)g(x)+f(x)g'(x)\bigr)+o(h).$$
The same view generalises directly to functions of several variables, where the derivative is a linear map (@sec-math-calculus-multivariable-differentiation-differentials-and-chain-rule).

*Higher derivatives* are defined recursively: $f$ is $(n+1)$ times differentiable if it is $n$ times differentiable and its $n$-th derivative $f^{(n)}$ is differentiable; then $f^{(n+1)}=(f^{(n)})'$.

## Inverse functions

::: {#thm-inverse-differentiable .theorem name="Differentiability of the inverse" related="thm-inverse-function-derivative"}

Let $f:[a,b]\to[c,d]$ be continuous, strictly increasing, with $f(a)=c$, $f(b)=d$, differentiable on $(a,b)$ with $f'$ never $0$ there. Then the inverse $g$ is differentiable at every $y\in(c,d)$, and
$$g'(y)=\frac1{f'(g(y))}.$$

:::

::: {.proof}

1. $g$ exists and is continuous by @thm-continuous-inverse. Fix $y\in(c,d)$, let $x=g(y)$, and for small $k\ne0$ let $h=h(k)=g(y+k)-x$.

2. Since $g$ is injective, $h\ne0$; and $f(x+h)=y+k$, so $k=f(x+h)-f(x)$. Hence
$$\frac{g(y+k)-g(y)}{k}=\frac{h}{f(x+h)-f(x)}=\left(\frac{f(x+h)-f(x)}{h}\right)^{-1}.$$

3. As $k\to0$, $h(k)\to0$ because $g$ is continuous at $y$. So the bracket tends to $f'(x)\ne0$ (@thm-sequential-limit), and its reciprocal to $1/f'(x)$.

:::

Unlike @thm-inverse-function-derivative, this does not assume that $g$ is differentiable; it proves it. For example $x^{1/q}$ is the inverse of $x^q$ on $(0,\infty)$, so its derivative is $\frac{1}{q(x^{1/q})^{q-1}}=\frac1qx^{1/q-1}$; by the chain rule $x^{p/q}=(x^{1/q})^p$ then has derivative $\frac pqx^{p/q-1}$.

## Complex differentiability

::: {#def-complex-differentiable .definition name="Complex differentiability"}

$f:\mathbb C\to\mathbb C$ is *differentiable* at $z$ with derivative $f'(z)$ if
$$\lim_{h\to0}\frac{f(z+h)-f(z)}{h}=f'(z),$$
where now $h$ ranges over non-zero complex numbers; equivalently $f(z+h)=f(z)+hf'(z)+o(h)$.

:::

The sum, product, quotient and chain rules hold with the same proofs, and polynomials have the expected derivatives. But because $h$ may approach $0$ from every direction, the condition is much stronger than in the real case.

::: {#exm-differentiability-1 .example name="Conjugation is not differentiable"}

For $f(z)=\bar z$, $\dfrac{f(z+h)-f(z)}{h}=\dfrac{\bar h}{h}$, which is $1$ for real $h$ and $-1$ for purely imaginary $h$; so the limit does not exist, at any $z$. Geometrically, $z\mapsto\bar z$ is a linear map of $\mathbb R^2$ (a reflection), but the only $\mathbb C$-linear maps are $z\mapsto bz$, which rotate and scale.

Likewise $|z|$ is nowhere complex-differentiable: at $z\ne0$, differentiability of $|z|$ would make $|z|^2/z=\bar z$ differentiable by the product and quotient rules; at $z=0$ it fails already along the real axis.

:::
