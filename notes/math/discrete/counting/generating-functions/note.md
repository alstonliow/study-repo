---
title: "Generating Functions"
sources: [mcs-15.1, mcs-15.2, mcs-15.3, mcs-15.4, mcs-15.5]
requires: [math/discrete/counting/stars-and-bars, math/discrete/sequences/solving-recurrences]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Chapter 15, in our own wording; examples our own, checked by computation; proofs written out in steps. Extends @def-generating-function-extra. -->

## Sequences as power series

::: {#def-ordinary-generating-function .definition name="Generating function"}

The *(ordinary) generating function* of a sequence $(g_0,g_1,g_2,\dots)$ is the power series
$$G(x)=g_0+g_1x+g_2x^2+\dots=\sum_{n\ge0}g_nx^n.$$
We write $(g_0,g_1,g_2,\dots)\longleftrightarrow G(x)$, and $[x^n]G(x)=g_n$ for the coefficient of $x^n$. We treat $G(x)$ as a *formal* power series: an algebraic object added and multiplied like a polynomial, whatever the convergence (see the remark at the end of this note).

:::

The basic example is the geometric series
$$\frac1{1-x}=1+x+x^2+\cdots\longleftrightarrow(1,1,1,\dots),\qquad\frac1{1-ax}\longleftrightarrow(1,a,a^2,\dots).$$

::: {#prp-generating-function-operations .proposition name="Operations on generating functions"}

Let $(f_n)\leftrightarrow F(x)$ and $(g_n)\leftrightarrow G(x)$. Then

1. *Scaling and adding:* $(af_n+bg_n)\leftrightarrow aF(x)+bG(x)$.
2. *Right shift:* $(\underbrace{0,\dots,0}_k,f_0,f_1,\dots)\leftrightarrow x^kF(x)$.
3. *Differentiation:* $(f_1,2f_2,3f_3,\dots)\leftrightarrow F'(x)$.
4. *Product:* $F(x)G(x)\leftrightarrow(h_n)$ with $h_n=\sum_{k=0}^nf_kg_{n-k}$ (the *convolution*).

:::

::: {.proof}

1–2. Compare coefficients of $x^n$.

3. $\frac d{dx}\sum_nf_nx^n=\sum_{n\ge1}nf_nx^{n-1}$, whose coefficient of $x^{n}$ is $(n+1)f_{n+1}$.

4. Multiplying out $\bigl(\sum_kf_kx^k\bigr)\bigl(\sum_jg_jx^j\bigr)$, the terms with $k+j=n$ contribute $f_kg_jx^n$; collecting them gives $h_n$.

:::

For instance, differentiating $\frac1{1-x}$ gives $\frac1{(1-x)^2}\leftrightarrow(1,2,3,\dots)$, and $\frac x{(1-x)^2}\leftrightarrow(0,1,2,3,\dots)$.

## Counting with generating functions

::: {#thm-convolution-rule .theorem name="Convolution rule"}

Suppose there are $a_n$ ways to choose $n$ items of one kind and $b_n$ ways to choose $n$ items of another kind, with generating functions $A(x)$ and $B(x)$. Then the number of ways to choose $n$ items in total, some of each kind, has generating function $A(x)B(x)$.

:::

::: {.proof}

A choice of $n$ items in total consists of a choice of $k$ items of the first kind and $n-k$ of the second, for some $k$. By the sum and product rules (@sec-math-discrete-counting-sum-and-product-rules) there are $\sum_{k=0}^na_kb_{n-k}$ such choices, which is the convolution in @prp-generating-function-operations.

:::

::: {#prp-multiset-generating-function .proposition name="Choosing with repetition"}

The number of ways to choose $n$ items from $k$ kinds, with repetition allowed, is $[x^n]\dfrac1{(1-x)^k}=\dbinom{n+k-1}{n}$.

:::

::: {.proof}

1. For one kind, there is exactly one way to choose $n$ items for every $n$: generating function $\frac1{1-x}$. By @thm-convolution-rule, $k$ kinds give $\frac1{(1-x)^k}$.

2. The coefficient is the number of multisets of size $n$ from $k$ kinds, which is $\binom{n+k-1}n$ by stars and bars (@thm-stars-and-bars).

:::

::: {#exm-generating-function-coins .example name="Fruit baskets with restrictions"}

How many baskets of $n$ fruits are there with an even number of apples, at most $2$ bananas, and any number of cherries?

1. Apples: $1+x^2+x^4+\cdots=\frac1{1-x^2}$. Bananas: $1+x+x^2=\frac{1-x^3}{1-x}$. Cherries: $\frac1{1-x}$.

2. The product is $\frac{1-x^3}{(1-x^2)(1-x)^2}=\frac{1+x+x^2}{(1+x)(1-x)^2}$.

3. Partial fractions (below) give $\frac{1+x+x^2}{(1+x)(1-x)^2}=\frac{1/4}{1+x}+\frac{-3/4}{1-x}+\frac{3/2}{(1-x)^2}$, so the number of baskets is
   $$\tfrac14(-1)^n-\tfrac34+\tfrac32(n+1)=\frac{6n+3+(-1)^n}4.$$
   For $n=2$: $\frac{16}4=4$, namely AA, BB, BC, CC.

:::

## Partial fractions and linear recurrences

A rational generating function $\frac{P(x)}{Q(x)}$ with $\deg P<\deg Q$ and $Q$ a product of factors $(1-\alpha x)$ splits into a sum of terms $\frac c{(1-\alpha x)^j}$, each with a known coefficient formula: $[x^n]\frac1{(1-\alpha x)^j}=\binom{n+j-1}{j-1}\alpha^n$. This turns generating functions into closed forms.

::: {#thm-fibonacci-generating-function .theorem name="Fibonacci numbers by generating functions"}

The Fibonacci numbers ($f_0=0$, $f_1=1$, $f_n=f_{n-1}+f_{n-2}$) have generating function $F(x)=\dfrac x{1-x-x^2}$, and
$$f_n=\frac1{\sqrt5}\bigl(\varphi^n-\psi^n\bigr),\qquad\varphi=\frac{1+\sqrt5}2,\ \psi=\frac{1-\sqrt5}2.$$

:::

::: {.proof}

1. By the recurrence and @prp-generating-function-operations, $F(x)-xF(x)-x^2F(x)$ has coefficient $f_n-f_{n-1}-f_{n-2}=0$ for $n\ge2$, coefficient $f_1-f_0=1$ for $n=1$, and $f_0=0$ for $n=0$. So $(1-x-x^2)F(x)=x$.

2. $1-x-x^2=(1-\varphi x)(1-\psi x)$, since $\varphi+\psi=1$ and $\varphi\psi=-1$. Partial fractions give $\frac x{(1-\varphi x)(1-\psi x)}=\frac1{\varphi-\psi}\Bigl(\frac1{1-\varphi x}-\frac1{1-\psi x}\Bigr)$, which one checks by putting the right side over a common denominator.

3. With $\varphi-\psi=\sqrt5$ and $\frac1{1-\alpha x}\leftrightarrow(\alpha^n)$, the coefficient of $x^n$ is $\frac{\varphi^n-\psi^n}{\sqrt5}$.

:::

The same three steps solve every linear recurrence with constant coefficients: multiply the recurrence by $x^n$ and sum to get a rational $G(x)$, factor the denominator, and expand by partial fractions. Repeated roots give the terms $\binom{n+j-1}{j-1}\alpha^n$, which explains the factors $n^{j-1}$ in the general solution (@thm-distinct-roots and its repeated-root version).

::: {#rmk-generating-functions-formal .remark name="Formal power series"}

All manipulations above are identities between formal power series: sequences with the addition and the convolution product of @prp-generating-function-operations. A series $G$ has a multiplicative inverse exactly when $g_0\ne0$; for example $(1-x)\cdot(1+x+x^2+\cdots)=1$ holds formally, whether or not the series converges for a given $x$. So no question of convergence arises when we use generating functions only to read off coefficients.

:::
