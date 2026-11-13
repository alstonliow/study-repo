---
title: "Modular Exponentiation"
sources: [fit1058-cn-7.13, fit1058-cn-7.14]
requires: [math/discrete/number-theory/coprimality, math/discrete/number-theory/euler-totient, math/discrete/number-theory/modular-arithmetic]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: Fast exponentiation; Modular exponentiation. -->

## Fast exponentiation

::: {#def-binary-square-and-multiply-exponentiation .definition name="Binary (square-and-multiply) exponentiation"}

Write $m=\sum_{i}b_i2^i$ in binary. Then $a^m=\prod_{i \,:\, b_i=1}a^{2^i}$, where the powers $a^{2^i}$ are obtained by repeated squaring: $a^{2^{i+1}}=\bigl(a^{2^i}\bigr)^2$.

:::

::: {#prp-fastexpcost .proposition name="Cost"}

For $m\ge1$, binary exponentiation computes $a^m$ using at most $2\lfloor\log_2 m\rfloor$ multiplications.

:::

::: {.proof}

Producing $a^2,a^4,\dots,a^{2^{\lfloor\log_2m\rfloor}}$ takes $\lfloor\log_2m\rfloor$ squarings. The binary expansion of $m$ has $\lfloor\log_2m\rfloor+1$ digits, so at most that many ones, and combining the corresponding powers takes at most $\lfloor\log_2m\rfloor$ further multiplications.

:::

::: {#exm-square-and-multiply .example name="Square-and-multiply"}

Compute $3^{36}$. Since $36=100100_2=2^5+2^2$, we have $3^{36}=3^{32}\cdot3^4$. Squaring repeatedly gives $3^2=9$, $3^4=81$, $3^8=6561$, $3^{16}=43046721$, $3^{32}=1853020188851841$, and one final multiplication by $3^4=81$ gives $3^{36}$. That is six multiplications, versus $35$ for the naive method.

:::

## Modular exponentiation

::: {.remark name="Two savings"}

Modular exponentiation is exponentiation in $\mathbb{Z}_n$. Two separate savings apply: reduce each intermediate product mod $n$ (@thm-congarith), and, when $\gcd(a,n)=1$, reduce the *exponent* mod $\varphi(n)$ (@cor-expred below).

:::

::: {#thm-euler .theorem name="Euler"}

If $\gcd(x,n)=1$, then $x^{\varphi(n)}\equiv1\pmod n$.

:::

::: {.proof}

Let $\mathbb{Z}_n^*=\{y_1,\dots,y_{\varphi(n)}\}$ and consider $xy_1,\dots,xy_{\varphi(n)}$. These lie in $\mathbb{Z}_n^*$ by @lem-coprimeprod. They are also distinct mod $n$: if $xy_i\equiv xy_j$, multiplying by $x^{-1}$ (which exists by @thm-inverse) gives $y_i=y_j$. So multiplying by $x$ just permutes $\mathbb{Z}_n^*$, and the two lists have the same product:
$$y_1y_2\cdots y_{\varphi(n)} \equiv (xy_1)(xy_2)\cdots(xy_{\varphi(n)}) = x^{\varphi(n)}\,y_1y_2\cdots y_{\varphi(n)} \pmod n.$$
The product $y_1\cdots y_{\varphi(n)}$ lies in $\mathbb{Z}_n^*$, so it has an inverse; multiplying both sides by it gives $x^{\varphi(n)}\equiv1\pmod n$.

:::

::: {#cor-flt .corollary name="Fermat's Little Theorem"}

If $p$ is prime and $p\nmid x$, then $x^{p-1}\equiv1\pmod p$.

:::

::: {.proof}

Take $n=p$ in @thm-euler, and use $\varphi(p)=p-1$ (@prp-totientpp).

:::

::: {#cor-expred .corollary name="Exponent reduction"}

If $\gcd(a,n)=1$ and $x\equiv y\pmod{\varphi(n)}$ with $x,y\ge0$, then $a^x\equiv a^y\pmod n$.

:::

::: {.proof}

Taking $x\ge y$, write $x=y+k\varphi(n)$. Then $a^x=a^y\bigl(a^{\varphi(n)}\bigr)^k\equiv a^y\cdot1^k=a^y\pmod n$ by @thm-euler.

:::

::: {.remark name="The coprimality hypothesis is essential"}

For $n=4$: $\varphi(4)=2$ and $3\equiv1\pmod2$, yet $2^3=8\equiv0$ while $2^1=2\pmod4$.

:::

::: {#exm-modular-exponentiation-1 .example}

Simplify $2^9\bmod7$. Since $\varphi(7)=6$, the exponent reduces mod $6$: $9\bmod6=3$. So $2^9\equiv2^3=8\equiv1\pmod7$.

:::

::: {#exm-exponent-reduction .example name="Exponent reduction"}

Compute $3^{36}\bmod25$. Here $\varphi(25)=20$ and $\gcd(3,25)=1$, so $3^{36}\equiv3^{36\bmod20}=3^{16}\pmod{25}$. Squaring repeatedly mod $25$: $3^2=9$, $3^4=81\equiv6$, $3^8\equiv6^2=36\equiv11$, $3^{16}\equiv11^2=121\equiv21$. So $3^{36}\equiv21\pmod{25}$, using four multiplications and no number larger than $121$.

:::
