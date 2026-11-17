---
title: "The Chinese Remainder Theorem"
sources: [cs70-6.6]
requires: [math/discrete/number-theory/modular-arithmetic]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 6 §6 (cs70-6.6), in our own wording; proofs written out in steps. -->

::: {#thm-crt-two .theorem name="Chinese Remainder Theorem, two moduli"}

Let $m,n\ge1$ with $\gcd(m,n)=1$. For all integers $a,b$ there is exactly one $x\in\{0,1,\dots,mn-1\}$ with
$$x\equiv a\pmod n\qquad\text{and}\qquad x\equiv b\pmod m.$$

:::

::: {.proof}

1. Since $\gcd(m,n)=1$, $m$ has an inverse $m^{-1}$ modulo $n$, and $n$ has an inverse $n^{-1}$ modulo $m$ (@thm-inverse).

2. Let $u=m\cdot(m^{-1}\bmod n)$ and $v=n\cdot(n^{-1}\bmod m)$. Then $u\equiv1\pmod n$ and $u\equiv0\pmod m$, while $v\equiv0\pmod n$ and $v\equiv1\pmod m$.

3. **Existence.** Let $x=(au+bv)\bmod mn$. Modulo $n$, $x\equiv a\cdot1+b\cdot0=a$; modulo $m$, $x\equiv a\cdot0+b\cdot1=b$.

4. **Uniqueness.** If $x$ and $y$ in $\{0,\dots,mn-1\}$ are both solutions, then $n\mid x-y$ and $m\mid x-y$, so $mn\mid x-y$ (@prp-coprimedivides). But $|x-y|<mn$, so $x-y=0$.

:::

::: {#thm-crt .theorem name="Chinese Remainder Theorem"}

Let $n_1,\dots,n_k\ge1$ be pairwise coprime and $N=n_1n_2\cdots n_k$. For all integers $a_1,\dots,a_k$ there is exactly one $x\in\{0,\dots,N-1\}$ with $x\equiv a_i\pmod{n_i}$ for every $i$. It is
$$x=\Bigl(\sum_{i=1}^{k}a_ib_i\Bigr)\bmod N,\qquad b_i=\frac N{n_i}\Bigl(\Bigl(\frac N{n_i}\Bigr)^{-1}\bmod n_i\Bigr).$$

:::

::: {.proof}

1. $\frac N{n_i}$ is a product of moduli coprime to $n_i$, so it is coprime to $n_i$ and has an inverse modulo $n_i$; hence $b_i$ is defined.

2. $b_i\equiv1\pmod{n_i}$, and $b_i\equiv0\pmod{n_j}$ for $j\ne i$, because $n_j$ divides $\frac N{n_i}$.

3. So modulo $n_j$, every term of $\sum_ia_ib_i$ vanishes except $a_jb_j\equiv a_j$: $x$ is a solution.

4. If $x$ and $y$ are solutions in $\{0,\dots,N-1\}$, every $n_i$ divides $x-y$. Applying @prp-coprimedivides repeatedly, $N\mid x-y$, and as before $x=y$.

:::

::: {#rmk-crt-vector-view .remark name="Arithmetic in pieces"}

The theorem gives a bijection between $\{0,\dots,mn-1\}$ and pairs $(x\bmod n,\ x\bmod m)$, and it respects arithmetic: the pair of $x+y$ is the sum of the pairs, and likewise for products (@thm-congarith). So working modulo $mn$ is the same as working modulo $n$ and modulo $m$ side by side. The numbers $b_i$ behave like basis vectors: $b_i$ is the number whose pair has $1$ in place $i$ and $0$ elsewhere.

:::
