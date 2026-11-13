---
title: "The Euler totient function"
sources: [fit1058-cn-7.12]
requires: [math/discrete/number-theory/modular-arithmetic]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: The Euler totient function. -->

::: {#def-totient .definition name="Euler totient function"}

For $n\in\mathbb{N}$, $\varphi(n)$ is the number of integers $x$ with $1\le x\le n$ and $\gcd(x,n)=1$. By @thm-inverse, $\varphi(n)=|\mathbb{Z}_n^*|$.

:::

::: {#exm-euler-totient-1 .example}

$\varphi(6)=|\{1,5\}|=2$ and $\varphi(7)=|\{1,\dots,6\}|=6$.

:::

::: {.remark name="Range of $x$"}

For $n\ge2$ this agrees with CN’s range $0<x<n$, since $\gcd(n,n)=n>1$. Including $x=n$ gives $\varphi(1)=1$, which keeps multiplicativity valid when one factor is $1$.

:::

::: {#prp-totientpp .proposition name="Totient of a prime power"}

For $p$ prime and $m\in\mathbb{N}$,  $\varphi(p^m)=p^{m-1}(p-1)$. In particular $\varphi(p)=p-1$.

:::

::: {.proof}

An integer $x$ with $1\le x\le p^m$ fails to be coprime to $p^m$ exactly when $p\mid x$. The multiples of $p$ in this range are $p,2p,\dots,p^{m-1}\cdot p$, so there are $p^{m-1}$ of them. Hence $\varphi(p^m)=p^m-p^{m-1}=p^{m-1}(p-1)$.

:::

::: {#thm-totientmult .theorem name="Multiplicativity"}

If $\gcd(a,b)=1$ then $\varphi(ab)=\varphi(a)\varphi(b)$.

:::

::: {#thm-totientformula .theorem name="General formula"}

If $n=p_1^{m_1}\cdots p_k^{m_k}$ with distinct primes $p_i$, then
$$\varphi(n)=\prod_{i=1}^{k}p_i^{m_i-1}(p_i-1) = n\prod_{i=1}^{k}\left(1-\frac1{p_i}\right).$$
In particular, for distinct primes $p,q$,  $\varphi(pq)=(p-1)(q-1)$.

:::

::: {.proof}

Powers of distinct primes are coprime, so @thm-totientmult splits $\varphi(n)$ into a product of the $\varphi(p_i^{m_i})$, each given by @prp-totientpp. The second form follows from $p_i^{m_i-1}(p_i-1)=p_i^{m_i}(1-1/p_i)$.

:::

::: {#exm-euler-totient-2 .example}

$\varphi(12)=\varphi(4)\varphi(3)=2\cdot2=4$; indeed the integers in $[1,12]$ coprime to $12$ are $1,5,7,11$. And $\varphi(25)=5\cdot4=20$.

:::

::: {.remark name="Needs the factorisation"}

The formula needs the prime factorisation of $n$, and no essentially easier way to compute $\varphi(n)$ is known. The RSA cryptosystem relies on this.

:::
