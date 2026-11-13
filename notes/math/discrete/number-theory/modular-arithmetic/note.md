---
title: "Modular Arithmetic and Inverses"
sources: [fit1058-cn-7.10, fit1058-cn-7.11]
requires: [math/discrete/number-theory/coprimality, math/discrete/number-theory/modular-exponentiation]
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: Modular arithmetic; Modular inverses. -->

## Modular arithmetic

::: {.remark name="Where remainders arise"}

Often only remainders matter. Days of the week are remainders mod $7$ of the number of days since a reference date; hours in 24-hour time are remainders mod $24$; the state of a toggle switch ($0$ off, $1$ on) is the number of presses mod $2$.

:::

::: {#def-congruence .definition name="Congruence"}

For $n\in\mathbb{N}$ and $a,b\in\mathbb{Z}$, $a$ is *congruent to $b$ modulo $n$*, written $a\equiv b\pmod n$, if $n\mid(a-b)$.

:::

::: {#prp-congremainder .proposition}

$a\equiv b\pmod n$ if and only if $a\bmod n=b\bmod n$.

:::

::: {.proof}

Write $a=q_an+r_a$ and $b=q_bn+r_b$ with $0\le r_a,r_b\le n-1$. Then $a-b=(q_a-q_b)n+(r_a-r_b)$, so $n\mid(a-b)$ if and only if $n\mid(r_a-r_b)$. Since $|r_a-r_b|\le n-1<n$, this holds if and only if $r_a=r_b$.

:::

::: {#prp-congequiv .proposition}

For every $n\in\mathbb{N}$, congruence modulo $n$ is an equivalence relation on $\mathbb{Z}$.

:::

::: {.proof}

**Reflexive**: $a-a=0=0\cdot n$.  **Symmetric**: if $a-b=kn$ then $b-a=(-k)n$.  **Transitive**: if $a-b=kn$ and $b-c=ln$ then $a-c=(k+l)n$.

:::

::: {#def-residue-classes-and .definition name="Residue classes and $\mathbb{Z}_n$"}

The equivalence classes of congruence mod $n$ are the *residue classes* $[a]=a+n\mathbb{Z}=\{a+kn : k\in\mathbb{Z}\}$. There are exactly $n$ of them: $[0],[1],\dots,[n-1]$. We write $\mathbb{Z}_n$ for $\{0,1,\dots,n-1\}$ with $+,-,\times$ followed by reduction mod $n$.

:::

::: {.remark name="Equation in $\mathbb{Z}_n$ vs.\ congruence"}

In $\mathbb{Z}_4$, $2+3=1$, since $5\bmod4=1$. This is different from the congruence $2+3\equiv1\pmod4$: the congruence only says that $2+3$ and $1$ lie in the same class, so $2+3\equiv37\pmod4$ is also true, while “$2+3=37$ in $\mathbb{Z}_4$” makes no sense ($37\notin\mathbb{Z}_4$).

:::

::: {#thm-congarith .theorem name="Congruences respect arithmetic"}

If $a\equiv b\pmod n$ and $c\equiv d\pmod n$, then
$$a+c\equiv b+d, \qquad a-c\equiv b-d, \qquad ac\equiv bd \pmod n.$$

:::

::: {.proof}

Write $a-b=kn$ and $c-d=ln$. Then $(a+c)-(b+d)=(k+l)n$ and $(a-c)-(b-d)=(k-l)n$. For the product, $ac-bd = c(a-b)+b(c-d) = (ck+bl)n$.

:::

::: {.remark name="Reduce as you go"}

By @thm-congarith, in any calculation using only $+,-,\times$, you can reduce mod $n$ at *every* step instead of only at the end. Division and exponentiation need separate treatment (@sec-math-discrete-number-theory-modular-arithmetic, @sec-math-discrete-number-theory-modular-exponentiation).

:::

::: {#exm-checking-a-product-mod-9 .example name="Checking a product mod 9"}

Is $84\times32=2678$? Since $10\equiv1\pmod9$, a number is congruent mod $9$ to its digit sum. So $84\equiv12\equiv3$ and $32\equiv5$, giving $84\times32\equiv15\equiv6$; but $2678\equiv23\equiv5$. The two sides differ mod $9$, so the calculation is wrong (in fact $84\times32=2688$). The check is one-sided: agreement mod $9$ would not prove the answer correct.

:::

## Modular inverses

::: {#def-modular-inverse .definition name="Modular inverse, $\mathbb{Z}_n^*$"}

$x^{-1}\in\mathbb{Z}_n$ is a *multiplicative inverse* of $x\in\mathbb{Z}_n$ if $xx^{-1}\equiv1\pmod n$. We write $\mathbb{Z}_n^*$ for the set of elements of $\mathbb{Z}_n$ that have an inverse.

:::

::: {#exm-modular-arithmetic-1 .example}

In $\mathbb{Z}_7$: $2^{-1}=4$ (since $2\cdot4=8\equiv1$), and $1^{-1}=1$, $3^{-1}=5$, $4^{-1}=2$, $5^{-1}=3$, $6^{-1}=6$. Every nonzero element has an inverse, so $\mathbb{Z}_7^*=\{1,2,3,4,5,6\}$.

In $\mathbb{Z}_6$, $2$ has no inverse: $2z$ is always even, so it is never $1,7,13,\dots$. Similarly $3$ and $4$ have none, while $5\cdot5=25\equiv1$. So $\mathbb{Z}_6^*=\{1,5\}$.

:::

::: {#thm-inverse .theorem name="Existence of inverses"}

$x\in\mathbb{Z}_n$ has an inverse in $\mathbb{Z}_n$ if and only if $\gcd(x,n)=1$.

:::

::: {.proof}

($\Rightarrow$) If $xx^{-1}\equiv1\pmod n$, then $xx^{-1}+kn=1$ for some $k\in\mathbb{Z}$, so $x$ and $n$ are coprime by @cor-coprimebezout.

($\Leftarrow$) If $\gcd(x,n)=1$, @cor-coprimebezout gives $y,z\in\mathbb{Z}$ with $yx+zn=1$. Let $y'=y\bmod n$, so $y=ln+y'$. Then $y'x+(lx+z)n=1$, so $y'x\equiv1\pmod n$ with $y'\in\mathbb{Z}_n$.

:::

::: {.remark name="Finding inverses with the EEA"}

The proof is constructive: run the EEA on $(x,n)$ to get $yx+zn=1$; then $x^{-1}=y\bmod n$. This is the main practical use of the EEA.

:::

::: {#exm-inverse-computation .example name="Inverse computation"}

Find $17^{-1}$ in $\mathbb{Z}_{101}$. Rows $(t,x,y)$ satisfy $t=101x+17y$:
$$\begin{array}{rrrl}
101 & 1 & 0 &\\
17 & 0 & 1 &\\
16 & 1 & -5 & (q=5)\\
1 & -1 & 6 & (q=1)
\end{array}$$
So $1=-1\cdot101+6\cdot17$, giving $17^{-1}=6$ in $\mathbb{Z}_{101}$. Check: $6\cdot17=102\equiv1\pmod{101}$.

:::
