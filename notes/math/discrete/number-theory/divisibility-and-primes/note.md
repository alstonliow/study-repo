---
title: "Divisibility and Primes"
sources: [fit1058-cn-7.1, fit1058-cn-7.2]
requires: [math/discrete/number-theory/coprimality, math/discrete/number-theory/diffie-hellman]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: Multiples and divisors; Prime numbers. -->

## Multiples and divisors

::: {#def-divisibility .definition name="Divisibility"}

For $d\in\mathbb{Z}\setminus\{0\}$ and $n\in\mathbb{Z}$, $d$ *divides* $n$, written $d\mid n$, if $n=qd$ for some $q\in\mathbb{Z}$. Then $d$ is a *divisor* (or *factor*) of $n$, and $n$ is a *multiple* of $d$; otherwise we write $d\nmid n$. The set of all multiples of $d$ is
$$d\mathbb{Z}=\{kd : k\in\mathbb{Z}\}.$$
A divisor of $n$ is *proper* if it is neither $1$ nor $n$.

:::

::: {#exm-divisibility-and-primes-1 .example}

$2\mathbb{Z}$ is the set of even integers, and $10\mathbb{Z}=\{\dots,-20,-10,0,10,20,\dots\}$.

:::

::: {.remark name="Zero is a special case"}

Every $d\ne0$ divides $0$, since $0=0\cdot d$. So whenever divisors are involved, $0$ often needs separate treatment.

:::

::: {#prp-divlinear .proposition name="Linearity of divisibility"}

For all $d,m,n,x,y\in\mathbb{Z}$ with $d\ne0$,
$$d\mid m \ \wedge\ d\mid n \quad\Longrightarrow\quad d\mid (xm+yn).$$
In particular $d\mid(m+n)$ and $d\mid(m-n)$.

:::

::: {.proof}

Write $m=q_1d$ and $n=q_2d$. Then $xm+yn=(xq_1+yq_2)d$, and $xq_1+yq_2\in\mathbb{Z}$, so $d\mid(xm+yn)$.

:::

::: {.remark name="The converse fails"}

$2\mid(3+5)$, but $2\nmid3$ and $2\nmid5$. Knowing that $d$ divides a sum tells you nothing about the individual terms.

:::

::: {.remark name="Divisibility tests from the last digits"}

Some divisors can be detected from the decimal representation alone:

- $10\mid n$ iff $n$ ends in $0$;

- $5\mid n$ iff $n$ ends in $0$ or $5$;

- $2\mid n$ iff $n$ ends in one of $0,2,4,6,8$;

- $4\mid n$ iff the last two digits of $n$ form a multiple of $4$.

Only a fixed number of digits at the end matter, however large $n$ is (Exercise 7.9).

:::

## Prime numbers

::: {#def-prime-composite .definition name="Prime, composite"}

An integer $p>1$ is *prime* if it has no proper divisors. An integer $n>1$ that is not prime is *composite*.

:::

::: {.remark name="$1$ is neither"}

$1$ is neither prime nor composite. Excluding it is what makes prime factorisations unique (@thm-fta): otherwise $6=2\cdot3=1\cdot2\cdot3=1\cdot1\cdot2\cdot3=\cdots$.

:::

::: {#thm-primefactexists .theorem name="Existence of prime factorisation"}

Every integer $n\ge2$ is a product of primes.

:::

::: {.proof}

We use strong induction on $n$.

**Base case** ($n=2$): $2$ is prime, so it is a product of one prime.

**Inductive step**: Let $n\ge2$ and assume every $k$ with $2\le k\le n$ is a product of primes. If $n+1$ is prime, it is a product of one prime. Otherwise $n+1$ has a proper divisor $a$, so $n+1=ab$ with $1<a,b<n+1$ (if $b$ were $1$ or $n+1$, then $a$ would be $n+1$ or $1$). Since $a,b\le n$, the inductive hypothesis makes each of them a product of primes, and hence so is $n+1=ab$.

By the Principle of Strong Induction, the claim holds for all $n\ge2$.

:::

::: {#thm-infprimes .theorem name="Infinitude of primes, Euclid"}

There are infinitely many primes.

:::

::: {.proof}

Suppose, for contradiction, that the primes are exactly $p_1,\dots,p_k$, and let $N=p_1p_2\cdots p_k+1$. By @thm-primefactexists, $N$ has a prime divisor, which must be some $p_i$. But $p_i$ also divides $p_1\cdots p_k$, so by @prp-divlinear it divides $N-p_1\cdots p_k=1$, which is impossible for a prime. So no finite list contains all the primes.

:::

::: {#prp-sqrtbound .proposition name="Trial division bound"}

If $n>1$ is composite, then $n$ has a prime divisor $p\le\sqrt n$.

:::

::: {.proof}

Write $n=ab$ with $1<a\le b<n$. Then $a^2\le ab=n$, so $a\le\sqrt n$. By @thm-primefactexists, $a$ has a prime divisor $p$, and $p\le a\le\sqrt n$ with $p\mid a\mid n$.

:::

::: {.remark name="Using the bound"}

To test whether $n$ is prime, it is enough to try dividing by the primes up to $\sqrt n$. For example, $97$ is prime because none of $2,3,5,7$ divides it, and $11^2=121>97$.

:::

::: {.remark name="Density of primes (extra)"}

The Prime Number Theorem says that $\pi(x)$, the number of primes $\le x$, satisfies $\pi(x)\sim x/\ln x$. So primes thin out, but only slowly: an integer near $x$ is prime with probability about $1/\ln x$. This is why searching randomly for large primes (as needed in @sec-math-discrete-number-theory-diffie-hellman) is practical.

:::
