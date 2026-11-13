---
title: "The GCD and the Euclidean Algorithm"
sources: [fit1058-cn-7.5, fit1058-cn-7.6]
requires: [math/discrete/number-theory/coprimality, math/discrete/number-theory/divisibility-and-primes]
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: The greatest common divisor; The Euclidean algorithm. -->

## The greatest common divisor

::: {#def-gcd-lcm .definition name="gcd, lcm"}

For $a,b\in\mathbb{Z}$ not both $0$, $\gcd(a,b)$ is the greatest $d$ with $d\mid a$ and $d\mid b$. For $a,b\in\mathbb{N}$, $\operatorname{lcm}(a,b)$ is the least positive common multiple of $a$ and $b$.

:::

::: {#exm-gcd-and-euclidean-algorithm-1 .example}

The positive divisors of $12$ are $1,2,3,4,6,12$ and those of $20$ are $1,2,4,5,10,20$. The common ones are $1,2,4$, so $\gcd(12,20)=4$.

:::

::: {.remark name="Why the gcd exists"}

The set of common divisors contains $1$, and is bounded above because $d\mid n\ne0$ implies $d\le|n|$; so it has a greatest element. If $a=b=0$, every integer is a common divisor, which is why $\gcd(0,0)$ is undefined.

:::

::: {#prp-gcdsub .proposition name="Subtraction invariance"}

For $a,b\in\mathbb{Z}$ not both $0$,  $\gcd(a,b)=\gcd(b,a-b)$.

:::

::: {.proof}

We show that $(a,b)$ and $(b,a-b)$ have exactly the same common divisors; then their greatest common divisors are equal.

If $d\mid a$ and $d\mid b$, then $d\mid(a-b)$ by @prp-divlinear, so $d$ is a common divisor of $b$ and $a-b$. Conversely, if $d\mid b$ and $d\mid(a-b)$, then $d\mid\bigl((a-b)+b\bigr)=a$, so $d$ is a common divisor of $a$ and $b$.

:::

::: {.remark name="Repeated subtraction"}

Applying @prp-gcdsub repeatedly, always subtracting the smaller number from the larger, computes the gcd: $\gcd(20,12)=\gcd(12,8)=\gcd(8,4)=\gcd(4,4)=\gcd(4,0)=4$. The Euclidean algorithm (@sec-math-discrete-number-theory-gcd-and-euclidean-algorithm) speeds this up.

:::

::: {#prp-gcdlcm .proposition name="gcd–lcm identity (extra)"}

For $a,b\in\mathbb{N}$,  $\gcd(a,b)\cdot\operatorname{lcm}(a,b)=ab$.

:::

::: {.proof}

Write $a=\prod_i p_i^{e_i}$ and $b=\prod_i p_i^{f_i}$ over a common list of primes (@thm-fta). Then $\gcd(a,b)=\prod_i p_i^{\min(e_i,f_i)}$ and $\operatorname{lcm}(a,b)=\prod_i p_i^{\max(e_i,f_i)}$, and $\min(e_i,f_i)+\max(e_i,f_i)=e_i+f_i$ for each $i$.

:::

## The Euclidean algorithm

::: {#lem-div-comb .lemma name="Divisibility of integer combinations"}

Let $d,u,v \in \mathbb{Z}$. If $d \mid u$ and $d \mid v$, then $d \mid (su + tv)$ for all $s,t \in \mathbb{Z}$.

:::

::: {.proof}

Write $u = dk_1$ and $v = dk_2$. Then $su + tv = d(sk_1 + tk_2)$, and $sk_1 + tk_2 \in \mathbb{Z}$.

:::

::: {#lem-euclid-step .lemma name="Euclid's Lemma for the gcd"}

Let $a \in \mathbb{Z}$ and $b \in \mathbb{N}$, and write $a = qb + r$ with $q = \lfloor a/b \rfloor$ and $0 \le r < b$. Then $\gcd(a,b) = \gcd(b,r)$.

:::

::: {.proof}

As in @prp-gcdsub, we show that $(a,b)$ and $(b,r)$ have the same common divisors.

If $d\mid a$ and $d\mid b$, then $d$ divides $r = 1\cdot a + (-q)\cdot b$ by @lem-div-comb, so $d$ is a common divisor of $b$ and $r$. Conversely, if $d\mid b$ and $d\mid r$, then $d$ divides $a = q\cdot b + 1\cdot r$, so $d$ is a common divisor of $a$ and $b$.

The two sets of common divisors are equal, and nonempty and bounded above since $b>0$, so their greatest elements are equal: $\gcd(a,b)=\gcd(b,r)$.

:::

::: {#def-euclidean-algorithm-ea .definition name="Euclidean Algorithm (EA)"}

To find $\gcd(a,b)$:

1.  Input $a,b\in\mathbb{N}$; if $a<b$, swap them so that $a\ge b$.

2.  If $b\mid a$, output $b$.

3.  Otherwise output $\gcd(b,\,a\bmod b)$, computed by the same method.

:::

::: {.remark name="Division replaces repeated subtraction"}

Subtracting $b$ from $a$ until the result drops below $b$ is exactly division with remainder. So one EA step does in one go what @prp-gcdsub would do with many subtractions.

:::

::: {#exm-gcd-and-euclidean-algorithm-1-2 .example}

$\gcd(1180,482)$:  $1180=2\cdot482+216$,  $482=2\cdot216+50$,  $216=4\cdot50+16$,  $50=3\cdot16+2$,  $16=8\cdot2+0$. So $\gcd(1180,482)=2$.

:::

::: {#exm-worst-case-of-the-ea .example name="Worst case of the EA"}

Consecutive Fibonacci numbers are the worst case: every quotient is $1$, so each remainder is only the previous Fibonacci number. For $(55,34)$:
$$55=1\cdot34+21,\quad 34=1\cdot21+13,\quad 21=1\cdot13+8,\quad 13=1\cdot8+5,$$
$$8=1\cdot5+3,\quad 5=1\cdot3+2,\quad 3=1\cdot2+1,\quad 2=2\cdot1.$$
So $\gcd(55,34)=1$. In the same way, consecutive Fibonacci numbers are always coprime (Exercise 7.12).

:::
