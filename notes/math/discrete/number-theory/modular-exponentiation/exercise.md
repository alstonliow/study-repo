<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-number-theory-16 origin="external" source="fit1058-cn-7.19-q16"}
Compute by hand, showing your working,
$$1752^{31415926535897932384626433832795028841971693993751058209749445923078164}
        \bmod 125.$$
(The exponent is $\lfloor10^{70}\pi\rfloor$.)
:::

::: {.problem #prob-cs70hw-4-q5 origin="external" source="cs70hw-4-q5"}
**Fermat's Little Theorem.** Fermat's Little Theorem states that for any prime $p$ and any $a \in \{1, 2, \ldots, p - 1\}$, we have $a^{p-1} \equiv 1 \pmod p$. Without using induction, prove that $\forall n \in \mathbb{N}$, $n^7 - n$ is divisible by 42.
:::

::: {.problem #prob-mit6042f10-3-q1 origin="external" source="mit6042f10-3-q1"}
**Warmup Exercises.** For the following parts, a correct numerical answer will only earn credit if accompanied by it's derivation. Show your work.

(a) Use the Pulverizer to find integers $s$ and $t$ such that $135s + 59t = \gcd(135, 59)$.

(b) Use the previous part to find the inverse of 59 modulo 135 in the range $\{1, \ldots, 134\}$.

(c) Use Euler's theorem to find the inverse of 17 modulo 31 in the range $\{1, \ldots, 30\}$.

(d) Find the remainder of $3^{482248}$ divided by 83. (Hint: Euler's theorem.)
:::

::: {.problem #prob-mit6042f10-3-q3 origin="external" source="mit6042f10-3-q3"}
In this problem, we will investigate numbers which are squares modulo a prime number $p$.

(a) An integer $n$ is a *square modulo $p$* if there exists another integer $x$ such that $n \equiv x^2 \pmod p$. Prove that $x^2 \equiv y^2 \pmod p$ if and only if $x \equiv y \pmod p$ or $x \equiv -y \pmod p$. (Hint: $x^2 - y^2 = (x + y)(x - y)$)

(b) There is a simple test we can perform to see if a number $n$ is a square modulo $p$. It states that

**Theorem 1 (Euler's Criterion).**

1. If $n$ is a square modulo $p$ then $n^{\frac{p-1}{2}} \equiv 1 \pmod p$.
2. If $n$ is not a square modulo $p$ then $n^{\frac{p-1}{2}} \equiv -1 \pmod p$.

Prove the first part of Euler's Criterion. (Hint: Use Fermat's theorem.)

(c) Assume that $p \equiv 3 \pmod 4$ and $n \equiv x^2 \pmod p$. Given $n$ and $p$, find one possible value of $x$. (Hint: Write $p$ as $p = 4k + 3$ and use Euler's Criterion. You might have to multiply two sides of an equation by $n$ at one point.)
:::
