---
title: "Induction: more examples"
sources: [fit1058-cn-3.11]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/03-proofs.tex: Induction: more examples. -->

::: {#exm-bernoulli-s-inequality-extra .example name="Bernoulli's inequality (extra)"}

For all $x \ge -1$ and all integers $n \ge 0$:
$$(1+x)^n \ge 1 + nx.$$

:::

::: {.proof}

**Base case** ($n=0$): $(1+x)^0 = 1 = 1+0\cdot x$.

**Inductive step**: assume $(1+x)^k \ge 1+kx$ for some $k \ge 0$. Since $x \ge -1$, we have $1+x \ge 0$, so multiplying both sides of the inductive hypothesis by $(1+x)$ preserves the inequality:
$$(1+x)^{k+1} = (1+x)^k(1+x) \ge (1+kx)(1+x) = 1 + kx + x + kx^2 = 1 + (k+1)x + kx^2.$$
Since $kx^2 \ge 0$:
$$(1+x)^{k+1} \ge 1 + (k+1)x.$$

By induction, the inequality holds for all $n \ge 0$.

:::

::: {.remark}

The condition $x\ge-1$ is exactly what’s needed for $1+x\ge0$, which is what allows multiplying an inequality through by $(1+x)$ without flipping its direction.

:::

::: {#exm-harmonic-numbers .example name="Harmonic numbers"}

Let $H_m = 1+\tfrac12+\tfrac13+\cdots+\tfrac1m$. Then for every $n\ge0$:
$$H_{2^n} \ge 1+\frac{n}{2}.$$

:::

::: {.proof}

**Base case** ($n=0$): $H_{2^0}=H_1=1 \ge 1+0$.

**Inductive step**: assume $H_{2^k}\ge1+\frac{k}{2}$ for some $k\ge0$. Then
$$H_{2^{k+1}} = H_{2^k} + \frac{1}{2^k+1}+\frac{1}{2^k+2}+\cdots+\frac{1}{2^{k+1}}.$$
There are $2^k$ terms in this added block, each $\ge \frac{1}{2^{k+1}}$, so the block sums to at least $2^k\cdot\frac{1}{2^{k+1}}=\frac12$. Hence
$$H_{2^{k+1}} \ge \left(1+\frac{k}{2}\right)+\frac12 = 1+\frac{k+1}{2}.$$

By induction, $H_{2^n}\ge1+\frac{n}{2}$ for all $n\ge0$.

:::

::: {.remark}

Since $1+n/2 \to \infty$ as $n\to\infty$, this proves the harmonic series diverges.

:::

::: {#def-depth-of-a-set-of .definition name="Depth of a set of intervals"}

For lectures given as time intervals, the *depth* is the maximum number that mutually overlap at any single instant.

:::

::: {#exm-existence-of-prime-factorisation .example name="Existence of prime factorisation"}

Every integer $n\ge2$ can be written as a product of one or more primes.

:::

::: {.proof}

**Base case** ($n=2$): $2$ itself is prime.

**Inductive step**: let $k\ge2$, and suppose every integer from $2$ to $k$ has a prime factorization. Consider $n=k+1$.

**Case 1**: $n$ is prime. Then $n$ itself is its factorization.

**Case 2**: $n$ is composite, so $n=ab$ for integers $2\le a,b\le n-1=k$. By the strong inductive hypothesis, both $a$ and $b$ have prime factorizations; concatenating them gives a prime factorization of $n=ab$.

Either way, $n$ has a prime factorization.

By strong induction, every $n\ge2$ has one.

:::

::: {.remark}

This needs *strong* induction: the factors $a,b$ of composite $n$ can be much smaller than $n-1$, so the hypothesis must cover *all* smaller values.

:::

::: {#exm-division-algorithm-existence-via-well .example name="Division algorithm: existence via well-ordering"}

For $a\in\mathbb{Z},\ d\in\mathbb{Z}^+$, there exist $q,r\in\mathbb{Z}$ with $a=dq+r$ and $0\le r<d$.

:::

::: {.proof}

Consider $S = \{a-dq : q\in\mathbb{Z},\ a-dq\ge0\}$. $S\subseteq\mathbb{N}$ and $S\neq\emptyset$. By well-ordering, $S$ has a least element $r=a-dq_0$.

We claim $r<d$. If not, $r-d = a-d(q_0+1) \in S$, but $r-d<r$, contradicting minimality of $r$.

So $r<d$, and $q=q_0$ gives $a=dq+r$ with $0\le r<d$.

:::

::: {#def-simple-polygon-diagonal .definition name="Simple polygon, diagonal"}

A *simple polygon* is a polygon whose sides do not cross. A *diagonal* is a line segment connecting two non-adjacent vertices that lies entirely inside the polygon.

:::

::: {#lem-every-simple-polygon-with-sides .lemma name="Every simple polygon with $\ge4$ sides has a diagonal"}

:::

::: {.proof name="Proof sketch"}

Take the leftmost vertex $v$ and its two neighbors $u,w$. If segment $uw$ lies inside the polygon, it is a diagonal. Otherwise, some vertex lies inside triangle $uvw$; take the one farthest from line $uw$ – the segment from $v$ to that vertex is a diagonal.

:::

::: {#exm-round-robin-tournament-ranking .example name="Round-robin tournament ranking"}

In a round-robin tournament with $n$ players, the players can be labeled $p_1,\dots,p_n$ such that $p_i$ beats $p_{i+1}$ for every $i$.

:::

::: {.proof}

**Base case** ($n=1$): trivial.

**Inductive step**: let $k\ge1$, suppose the claim holds for at most $k$ players. Consider $k+1$ players. Pick any player $x$; let $B$ = players who beat $x$, $L$ = players $x$ beats, so $|B|,|L|\le k$.

By the inductive hypothesis, $B$ has a chain ordering $b_1,\dots,b_{|B|}$, and $L$ has $\ell_1,\dots,\ell_{|L|}$. Concatenate:
$$b_1,\dots,b_{|B|},\ x,\ \ell_1,\dots,\ell_{|L|}.$$
The joins $b_{|B|}\to x$ and $x\to\ell_1$ hold by definition of $B,L$.

By strong induction, the claim holds for all $n\ge1$.

:::
