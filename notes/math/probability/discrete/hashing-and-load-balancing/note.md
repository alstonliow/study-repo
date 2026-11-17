---
title: "Hashing and Load Balancing"
sources: [cs70-18.1, cs70-18.2]
requires: [math/probability/discrete/indicator-variables]
aliases: [math/probability/hashing-and-load-balancing]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 18 (cs70-18.1, cs70-18.2), in our own wording; bounds proved in steps. The optional tighter load-balancing bound of the source is left out. -->

## The model

::: {#rmk-hashing-and-load-balancing-1 .remark name="Balls and bins again"}

A hash function sends each of $m$ keys to one of $n$ table positions; a simple scheduler sends each of $m$ jobs to one of $n$ processors. Modelling each key or job as going to a uniformly random place, independently of the others, both become $m$ balls thrown into $n$ bins (@exm-balls-and-bins). Two keys in the same position are a *collision*; the *load* of a processor is the number of jobs it receives.

:::

::: {#fig-hashing-and-load-balancing-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \b in {0,...,7} {\draw[emph] (\b+0.1,1.9) -- (\b+0.1,0) -- (\b+0.9,0) -- (\b+0.9,1.9); \node[tick] at (\b+0.5,-0.35) {$\b$};}
\node[ball] at (3.5,0.4) {$1$};
\node[hl ball] at (6.5,0.4) {$2$};
\node[ball] at (1.5,0.4) {$3$};
\node[hl ball] at (6.5,1.1) {$4$};
\node[ball] at (0.5,0.4) {$5$};
\node[ball] at (4.5,0.4) {$6$};
\end{tikzpicture}
\end{center}
```

Hashing $6$ keys into a table of $8$ slots: keys $2$ and $4$ land in the same slot, a collision.

:::

## Hashing without collisions

::: {#prp-collision-union-bound .proposition name="Collision probability, union bound"}

Hash $m$ keys into a table of size $n$. Then
$$\Pr(\text{some collision})\le\frac{m(m-1)}{2n}.$$
In particular the probability is at most $\varepsilon$ when $m\le\sqrt{2\varepsilon n}$.

:::

::: {.proof}

1. Number the $\binom m2$ pairs of keys and let $C_i$ be the event that pair $i$ collides. "Some collision" is the union of the $C_i$.

2. Two given keys land in the same position with probability $\frac1n$: whatever position the first takes, the second matches it with probability $\frac1n$.

3. By the union bound (@thm-union-bound), $\Pr(\bigcup_iC_i)\le\binom m2\frac1n=\frac{m(m-1)}{2n}$.

4. Since $m(m-1)<m^2$, the bound is at most $\varepsilon$ when $m^2\le2\varepsilon n$.

:::

::: {#prp-no-collision-exact .proposition name="No collision, exactly"}

For $m\le n$,
$$\Pr(\text{no collision})=\Bigl(1-\frac1n\Bigr)\Bigl(1-\frac2n\Bigr)\cdots\Bigl(1-\frac{m-1}n\Bigr)\le e^{-m(m-1)/(2n)}.$$

:::

::: {.proof}

1. The outcomes are the $n^m$ equally likely sequences of positions. Those with no collision use $m$ different positions in order: $n(n-1)\cdots(n-m+1)$ of them (@def-falling-factorial). Dividing by $n^m$ gives the product.

2. The same product comes from the chain rule (@thm-chain-rule): given that the first $i$ keys are in different positions, key $i+1$ avoids them with probability $\frac{n-i}n=1-\frac in$.

3. We use the fact from calculus that $1-x\le e^{-x}$ for every real $x$. Applying it to each factor,
   $$\prod_{i=1}^{m-1}\Bigl(1-\frac in\Bigr)\le\prod_{i=1}^{m-1}e^{-i/n}=e^{-\frac1n\sum_{i=1}^{m-1}i}=e^{-m(m-1)/(2n)},$$
   by @thm-sums-and-series-1.

:::

::: {#rmk-hashing-and-load-balancing-2 .remark name="About the square root of the table size"}

For small $x$, $\ln(1-x)\approx-x$, so the bound in @prp-no-collision-exact is also a good approximation: $\Pr(\text{no collision})\approx e^{-m^2/(2n)}$. Setting this equal to $1-\varepsilon$ gives
$$m\approx\sqrt{2\ln\tfrac1{1-\varepsilon}}\cdot\sqrt n,$$
about $1.177\sqrt n$ for $\varepsilon=\frac12$. Both propositions say the same thing: collisions become likely once the number of keys is of order $\sqrt n$, so a collision-free table must be about the square of the number of keys. The birthday paradox is the case $n=365$, where $1.177\sqrt{365}\approx22.5$ against the exact $23$.

:::

## Load balancing

::: {#thm-max-load .theorem name="Maximum load"}

Send $n$ jobs to $n$ processors at random. For every $k\ge1$,
$$\Pr(\text{some processor gets at least }k\text{ jobs})\le\frac{n}{k!}.$$
So if $k!\ge2n$, then with probability at least $\frac12$ every processor gets fewer than $k$ jobs.

:::

::: {.proof}

1. Let $A_k(i)$ be the event that processor $i$ gets at least $k$ jobs. The event in the theorem is $\bigcup_iA_k(i)$, and all the $A_k(i)$ have the same probability by symmetry.

2. If processor $1$ gets at least $k$ jobs, then some set $S$ of exactly $k$ jobs all go to processor $1$. Each such set does so with probability $\frac1{n^k}$, and there are $\binom nk$ sets. By the union bound (@thm-union-bound),
   $$\Pr(A_k(1))\le\binom nk\frac1{n^k}.$$

3. $\binom nk\frac1{n^k}=\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\frac1{k!}\le\frac1{k!}$, since each of the $k$ factors $\frac{n-i}n$ is at most $1$.

4. By the union bound again, over the $n$ processors, the probability is at most $n\cdot\frac1{k!}$.

5. If $k!\ge2n$, this is at most $\frac12$, and the complement has probability at least $\frac12$ (@prp-complement).

:::

::: {#rmk-hashing-and-load-balancing-3 .remark name="How large is the maximum load?"}

The smallest $k$ with $k!\ge2n$ grows very slowly. With the approximation $\ln k!\approx k\ln k-k$ it is about $\frac{\ln n}{\ln\ln n}$. For example, $13!\approx6.2\times10^9$, so if $350$ million letters go to random addresses among $350$ million people, then with probability at least $\frac12$ nobody gets $13$ or more. Random assignment, with no coordination at all, keeps the load within a small factor of the average $1$.

:::
