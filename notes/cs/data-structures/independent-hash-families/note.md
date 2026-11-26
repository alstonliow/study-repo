---
title: "k-Independent Hashing and Simple Tabulation"
sources: [mit6851-10]
requires: [cs/data-structures/perfect-hashing]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 10, in our own wording; proofs written out in steps. Only what the data structures of the next two notes need. -->

A totally random hash function $\{0,\dots,u-1\}\to\{0,\dots,m-1\}$ needs $\Theta(u\log m)$ bits to store, which is no better than storing the keys. Practical analyses therefore assume weaker, cheaply stored families.

::: {#def-k-independent .definition name="k-independent family"}

A family $\mathcal H$ of functions $U\to\{0,\dots,m-1\}$ is *$k$-wise independent* if for all distinct $x_1,\dots,x_k\in U$ and all $t_1,\dots,t_k$, a uniformly random $h\in\mathcal H$ satisfies

$$
\Pr\bigl[h(x_1)=t_1\wedge\dots\wedge h(x_k)=t_k\bigr]=O\!\left(\frac1{m^k}\right).
$$

For $k=2$ this is stronger than universality ($\Pr[h(x)=h(y)]=O(1/m)$, @def-universal-hash-family), and $k$-independence implies $j$-independence for $j<k$.

:::

::: {#prp-polynomial-hash .proposition name="Polynomial hashing"}

Let $p\ge u$ be a prime. For random $a_0,\dots,a_{k-1}\in\{0,\dots,p-1\}$ (with $a_{k-1}\ne0$) the function

$$
h(x)=\Bigl(\sum_{i=0}^{k-1}a_ix^i \bmod p\Bigr)\bmod m
$$

is $k$-wise independent into $\{0,\dots,p-1\}$ before the reduction modulo $m$ (and approximately so after it), and needs $k$ words. For $k=2$ this is the usual $h(x)=((ax+b)\bmod p)\bmod m$.

:::

::: {.proof}

For distinct $x_1,\dots,x_k$ and any target values $t_1,\dots,t_k$ in $\mathbb F_p$, the conditions $\sum_ia_ix_j^i=t_j$ form a linear system with an invertible Vandermonde matrix, so exactly one polynomial of degree $<k$ satisfies them: the probability is $p^{-k}$. The reduction modulo $m$ changes the probabilities by a factor $1\pm O(m/p)$.

:::

::: {#def-simple-tabulation .definition name="Simple tabulation"}

View a key as $c$ characters $x=(x_1,\dots,x_c)$ of $\log_2u/c$ bits each. Store a table $T_i$ of random values for every character position $i$ ($c\,u^{1/c}$ words) and set

$$
h(x)=T_1[x_1]\oplus T_2[x_2]\oplus\dots\oplus T_c[x_c].
$$

Evaluation takes $c$ table lookups. The family is $3$-independent, and not $4$-independent.

:::

::: {#rmk-independent-hash-families-1 .remark name="How much independence is needed"}

For chaining, $O(\log n/\log\log n)$-independence, or simple tabulation, give the longest chain $O(\log n/\log\log n)$ with high probability, the same as for totally random functions. For linear probing (@thm-linear-probing) $5$-independence suffices for $O(1)$ expected time, $2$- and some $4$-independent families can take $\Omega(\log n)$, and simple tabulation behaves like a random function. For cuckoo hashing (@thm-cuckoo-hashing) $O(\log n)$-independence or a random function work, $6$-independence is not enough, and simple tabulation has failure probability $\Theta(n^{-1/3})$ (the statements are quoted from the lecture, not proved here).

:::
