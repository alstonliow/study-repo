---
title: "Primitive roots"
sources: [fit1058-cn-7.15]
requires: [math/discrete/number-theory/coprimality, math/discrete/number-theory/diffie-hellman, math/discrete/number-theory/modular-exponentiation]
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: Primitive roots. -->

::: {#def-primitive-root .definition name="Primitive root"}

Let $\gcd(x,n)=1$. Then $x$ is a *primitive root* of $n$ if $x^k\not\equiv1\pmod n$ for all $1\le k<\varphi(n)$, i.e. $\varphi(n)$ is the least positive exponent with $x^{\varphi(n)}\equiv1$. Equivalently, the powers $x,x^2,x^3,\dots$ run through all of $\mathbb{Z}_n^*$; we say $x$ *generates* $\mathbb{Z}_n^*$.

:::

::: {#exm-primitive-root-and-a-non .example name="Primitive root and a non-example"}

For $n=7$, $\varphi(7)=6$ and $\mathbb{Z}_7^*=\{1,\dots,6\}$. The powers of $3$ are
$$\begin{array}{c|cccccc}
k & 1&2&3&4&5&6\\\hline
3^k\bmod7 & 3&2&6&4&5&1
\end{array}$$
All six elements appear, and $1$ is first reached at $k=6$, so $3$ is a primitive root of $7$. By contrast, the powers of $2$ are $2,4,1,\dots$, reaching $1$ at $k=3<6$; so $2$ generates only $\{1,2,4\}$ and is not a primitive root.

:::

::: {.remark name="Primitive roots have the widest range"}

Among the members of $\mathbb{Z}_n^*$, the primitive roots are exactly those whose powers take the greatest possible number of values. This is what makes them useful in cryptography (@sec-math-discrete-number-theory-diffie-hellman).

:::

::: {#thm-primrootexists .theorem name="Which moduli have primitive roots"}

$n$ has a primitive root if and only if $n\in\{1,2,4\}$, or $n=p^k$ or $n=2p^k$ for an odd prime $p$ and $k\in\mathbb{N}$.

:::

::: {#exm-no-primitive-root .example name="No primitive root"}

$8$ has no primitive root. Here $\varphi(8)=4$ and $\mathbb{Z}_8^*=\{1,3,5,7\}$, but $3^2=9$, $5^2=25$ and $7^2=49$ are all $\equiv1\pmod8$, so every element reaches $1$ by exponent $2<4$. Elements outside $\mathbb{Z}_8^*$ cannot help: the powers of $2$ are $2,4,0,0,\dots$ and never reach $1$. This agrees with @thm-primrootexists, since $8=2^3$ is a power of the *even* prime.

:::

::: {#lem-order .lemma name="Order lemma"}

Let $\gcd(x,n)=1$ and let $t\ge1$ be the least positive integer with $x^t\equiv1\pmod n$ (it exists by @thm-euler). Then for every $m\ge0$,  $x^m\equiv1\pmod n$ if and only if $t\mid m$.

:::

::: {.proof}

($\Leftarrow$) If $m=qt$ then $x^m=(x^t)^q\equiv1$.

($\Rightarrow$) Divide: $m=qt+r$ with $0\le r<t$. Then $1\equiv x^m=(x^t)^q\,x^r\equiv x^r\pmod n$. By the minimality of $t$, $r$ cannot be positive, so $r=0$ and $t\mid m$.

:::

::: {#thm-primrootcount .theorem name="Number of primitive roots"}

If $n$ has a primitive root, then it has exactly $\varphi(\varphi(n))$ of them.

:::

::: {.proof}

Let $a$ be a primitive root of $n$ and write $\phi=\varphi(n)$.

**Every element of $\mathbb{Z}_n^*$ is $a^k$ for a unique $k\in\{1,\dots,\phi\}$.** Each $a^k$ lies in $\mathbb{Z}_n^*$ (@lem-coprimeprod). If $a^k\equiv a^l$ with $1\le k<l\le\phi$, multiplying by $(a^{-1})^k$ gives $a^{l-k}\equiv1$ with $1\le l-k<\phi$, contradicting the definition of a primitive root. So $a^1,\dots,a^\phi$ are $\phi=|\mathbb{Z}_n^*|$ distinct elements of $\mathbb{Z}_n^*$, i.e. all of it.

**If $d=\gcd(k,\phi)>1$, then $a^k$ is not a primitive root**, since $(a^k)^{\phi/d}=(a^{\phi})^{k/d}\equiv1$ with $1\le\phi/d<\phi$.

**If $\gcd(k,\phi)=1$, then $a^k$ is a primitive root.** Suppose $(a^k)^j=a^{kj}\equiv1$ with $j\ge1$. Since $\phi$ is the least positive exponent sending $a$ to $1$, @lem-order gives $\phi\mid kj$. Write $x\phi+yk=1$ (@cor-coprimebezout); then $j=x\phi j+y\,kj$ is a sum of multiples of $\phi$, so $\phi\mid j$ and $j\ge\phi$.

So the primitive roots of $n$ correspond one-to-one to the $k\in\{1,\dots,\phi\}$ with $\gcd(k,\phi)=1$, and there are $\varphi(\phi)=\varphi(\varphi(n))$ of these.

:::

::: {#exm-primitive-roots-1 .example}

For $n=7$: $\varphi(\varphi(7))=\varphi(6)=2$. Indeed the primitive roots are $3^1=3$ and $3^5\equiv5$, while $3^2\equiv2$, $3^3\equiv6$, $3^4\equiv4$ are not, as their exponents $2,3,4$ share a factor with $6$.

:::

::: {.remark name="Finding primitive roots is hard"}

No fast algorithm is known for finding a primitive root of a given $n$.

:::
