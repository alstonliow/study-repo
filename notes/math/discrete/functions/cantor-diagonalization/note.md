---
title: "Uncountable Sets and Diagonalization"
sources: [cs70-11]
requires: [math/discrete/functions/countable-sets, math/discrete/sets/power-set]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 11 (cs70-11), in our own wording; proofs written out in steps. -->

## The real numbers

::: {#thm-reals-uncountable .theorem name="The reals are uncountable"}

The interval $[0,1]$, and hence $\mathbb R$, is uncountable.

:::

::: {.proof}

1. Write each $x\in[0,1]$ as an infinite decimal $0.d_1d_2d_3\ldots$ that does not end in an infinite run of $0$s; for example $1=0.999\ldots$ and $0.5=0.4999\ldots$. This representation is unique.

2. Suppose, for contradiction, that $f:\mathbb N\to[0,1]$ is a bijection, and list $f(0),f(1),f(2),\dots$ with their decimals.

3. Let $r_n$ be digit $n+1$ of $f(n)$ (the *diagonal*), and let $s=0.s_1s_2s_3\ldots$ with $s_{n+1}=(r_n+2)\bmod10$. Then $s$ is a real number in $[0,1]$.

4. For every $n$, $s$ differs from $f(n)$ in digit $n+1$ by at least $2$ (mod $10$). Two decimals that differ by at least $2$ in some digit, with the earlier digits arbitrary, cannot be equal even allowing the two expansions $0.\ldots d999\ldots=0.\ldots(d+1)000\ldots$, which differ by only $1$ in a digit. So $s\ne f(n)$ for every $n$.

5. So $s$ is not in the range of $f$, contradicting that $f$ is a bijection. If $\mathbb R$ were countable, so would be its subset $[0,1]$; hence $\mathbb R$ is uncountable too.

:::

::: {#rmk-cantor-diagonalization-rationals .remark name="Why the argument fails for the rationals"}

Applying the same construction to a list of the rationals in $[0,1]$ produces a number $s$ that is not on the list, but $s$ need not be rational (its decimal need not repeat), so there is no contradiction. This is consistent with @cor-rationals-countable.

:::

## The Cantor set

::: {#def-cantor-set .definition name="Cantor set"}

Start with $[0,1]$, remove the open middle third $(\frac13,\frac23)$, then the open middle third of each remaining interval, and so on forever. The *Cantor set* $C$ is the set of points never removed.

:::

::: {#prp-cantor-set .proposition name="The Cantor set is small and large"}

1. The total length removed is $1$.

2. $C$ is the set of $x\in[0,1]$ that have a base-$3$ expansion using only the digits $0$ and $2$.

3. $C$ is uncountable.

:::

::: {.proof}

1. Step $k$ keeps $\frac23$ of what is left, so after $k$ steps the remaining length is $\bigl(\frac23\bigr)^k\to0$.

2. Step $1$ removes exactly the numbers whose base-$3$ expansion must start $0.1\ldots$; the endpoints $\frac13=0.0222\ldots_3$ and $\frac23=0.2_3$ have expansions avoiding the digit $1$ there and stay. In the same way step $k$ removes the numbers whose $k$-th ternary digit must be $1$. What remains are the numbers with an expansion of $0$s and $2$s only.

3. Map $x=0.t_1t_2\ldots_3\in C$ (digits $t_i\in\{0,2\}$) to the binary number $0.\frac{t_1}2\frac{t_2}2\ldots_2$. Every binary expansion arises, by doubling its digits, so this map is onto $[0,1]$. If $C$ were countable, $[0,1]$ would be countable by @prp-injection-into-countable, contradicting @thm-reals-uncountable.

:::

## Power sets

::: {#thm-power-set-uncountable .theorem name="Cantor's theorem for the natural numbers"}

There is no bijection $\mathbb N\to\mathcal P(\mathbb N)$ (@def-power-set): $\mathcal P(\mathbb N)$ is uncountable.

:::

::: {.proof}

1. Suppose, for contradiction, that $f:\mathbb N\to\mathcal P(\mathbb N)$ is a bijection.

2. Let $D=\{n\in\mathbb N: n\notin f(n)\}$: flip the diagonal of the table whose row $n$ records which numbers belong to $f(n)$.

3. $D\subseteq\mathbb N$, so $D=f(m)$ for some $m$. If $m\in D$, then by the definition of $D$, $m\notin f(m)=D$; if $m\notin D$, then $m\in f(m)=D$. Both are impossible.

:::

::: {#rmk-cantor-diagonalization-infinities .remark name="Orders of infinity"}

So infinite sets come in different sizes. The size of $\mathbb N$ is written $\aleph_0$ and that of $\mathcal P(\mathbb N)$ is written $2^{\aleph_0}$; it equals the size of $\mathbb R$, the *continuum*. The *continuum hypothesis*, that no set is strictly between $\mathbb N$ and $\mathbb R$ in size, is a famous question of set theory. For a finite set of size $k$, by contrast, $|\mathcal P(S)|=2^k$.

:::
