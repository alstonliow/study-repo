---
title: "Coprimality"
sources: [fit1058-cn-7.9]
requires: [math/discrete/number-theory/divisibility-and-primes, math/discrete/number-theory/extended-euclidean-algorithm]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: Coprimality. -->

::: {#def-coprime .definition name="Coprime"}

$a,b\in\mathbb{Z}$ are *coprime* (*relatively prime*) if $\gcd(a,b)=1$.

:::

::: {.remark name="Coprime is not prime"}

$21$ and $25$ are coprime, but neither is prime. Coprimality is easy to test (run the EA), whereas primality testing is a genuinely different and harder problem.

:::

::: {#cor-coprimebezout .corollary name="Bézout characterisation of coprimality"}

$m,n\in\mathbb{Z}$ are coprime if and only if $xm+yn=1$ for some $x,y\in\mathbb{Z}$.

:::

::: {.proof}

By @thm-bezout, $\gcd(m,n)$ is the least positive element of $m\mathbb{Z}+n\mathbb{Z}$. No positive integer is smaller than $1$, so this least element is $1$ if and only if $1\in m\mathbb{Z}+n\mathbb{Z}$.

:::

::: {#exm-coprimality-1 .example}

$21$ and $25$ are coprime, and indeed $6\cdot21-5\cdot25=126-125=1$.

:::

::: {#lem-coprimeprod .lemma name="Products preserve coprimality"}

If $\gcd(a,c)=\gcd(b,c)=1$, then $\gcd(ab,c)=1$.

:::

::: {.proof}

By @cor-coprimebezout, write $xa+uc=1$ and $yb+vc=1$. Multiplying these gives $1=(xy)\,ab+(xav+uyb+uvc)\,c$, so $\gcd(ab,c)=1$ by @cor-coprimebezout again.

:::

::: {#thm-euclidlemma .theorem name="Euclid's lemma"}

Let $p$ be prime and $a,b\in\mathbb{Z}$. If $p\mid ab$, then $p\mid a$ or $p\mid b$.

:::

::: {.proof}

Assume $p\mid ab$ and $p\nmid a$; we show $p\mid b$. Since $p$ is prime and $p\nmid a$, $\gcd(p,a)=1$, so by @cor-coprimebezout there are $x,y\in\mathbb{Z}$ with $xp+ya=1$. Multiplying by $b$ gives $xpb+yab=b$. The first term is a multiple of $p$, and the second is a multiple of $ab$, hence of $p$. So $p\mid b$.

:::

::: {.remark name="Primality is needed"}

$3\mid(8\times9)$ forces $3\mid8$ or $3\mid9$ (here $3\mid9$). But for non-prime divisors this fails: $6\mid(3\times4)$, yet $6\nmid3$ and $6\nmid4$.

:::

::: {#prp-coprimedivides .proposition name="Coprime divisor rule"}

If $a\mid n$, $b\mid n$ and $\gcd(a,b)=1$, then $ab\mid n$.

:::

::: {.proof}

Write $xa+yb=1$ (@cor-coprimebezout) and $n=a\alpha=b\beta$. Then
$$n = n(xa+yb) = xa(b\beta)+yb(a\alpha) = ab(x\beta+y\alpha).$$

:::

::: {#thm-fta .theorem name="Fundamental Theorem of Arithmetic"}

Every positive integer has a factorisation into primes that is unique up to order.

:::

::: {.proof}

Existence is @thm-primefactexists. For uniqueness, suppose, for contradiction, that some integer has two different prime factorisations, and let $n$ be the smallest such. Over the primes $p_1,\dots,p_k$ appearing in either factorisation, write $n=p_1^{e_1}\cdots p_k^{e_k}=p_1^{f_1}\cdots p_k^{f_k}$, with $e_i\ne f_i$ for some $i$.

If some prime $p_j$ appears in both factorisations, divide both by $p_j^{\min(e_j,f_j)}$. The results are still two different factorisations, of the smaller number $n/p_j^{\min(e_j,f_j)}$, contradicting the minimality of $n$.

So the two factorisations share no prime. Let $p$ occur in the first. Then $p\mid n$, while $n$ is also a product of primes $q_1,\dots,q_l$, none equal to $p$. Applying @thm-euclidlemma repeatedly gives $p\mid q_t$ for some $t$, so $p=q_t$, a contradiction.

:::
