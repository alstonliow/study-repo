---
title: "Inclusion-Exclusion: Derangements"
sources: [fit1058-cn-8.4]
requires: [math/discrete/counting/inclusion-exclusion, math/discrete/counting/sum-and-product-rules]
status: draft
---

<!-- Migrated from 1058note 08-counting-combinatorics.tex, §8.4. -->

::: {#def-derangement .definition name="Derangement"}
A *derangement* of $\{1,\dots,n\}$ is a permutation $\sigma$ with $\sigma(i)\neq i$ for every $i$ (no fixed points).
:::

::: {#def-fixed-point .definition name="Fixed point"}
For a permutation $\sigma$ of $\{1,\dots,n\}$, $i$ is a *fixed point* if $\sigma(i)=i$. A derangement is a permutation with no fixed points.
:::

::: {#exm-permutations-of-three .example name="Permutations of $\{1,2,3\}$"}
Writing $\sigma$ as $(\sigma(1),\sigma(2),\sigma(3))$:

| $\sigma$ | \# fixed points |
|:-:|:-:|
| $(1,2,3)$ | $3$ |
| $(1,3,2)$ | $1$ |
| $(2,1,3)$ | $1$ |
| $(2,3,1)$ | $0$ |
| $(3,1,2)$ | $0$ |
| $(3,2,1)$ | $1$ |

So $D_3=2$, the derangements being $(2,3,1)$ and $(3,1,2)$.
:::

::: {#thm-derangement-count .theorem name="Derangement count"}
$$
D_n = n!\sum_{k=0}^n \frac{(-1)^k}{k!}.
$$
:::

::: {.proof}
Let $A_i$ = permutations of $\{1,\dots,n\}$ with $\sigma(i)=i$. Then $D_n = n! - |A_1\cup\cdots\cup A_n|$.

For any $k$ indices $i_1<\cdots<i_k$: $|A_{i_1}\cap\cdots\cap A_{i_k}|$ = permutations fixing those $k$ positions, i.e. permutations of the remaining $n-k$ elements: $(n-k)!$. There are $\binom{n}{k}$ such $k$-subsets.

By inclusion-exclusion:
$$
|A_1\cup\cdots\cup A_n| = \sum_{k=1}^n (-1)^{k+1}\binom{n}{k}(n-k)!.
$$
Since $\binom{n}{k}(n-k)! = \dfrac{n!}{k!}$:
$$
D_n = n! - \sum_{k=1}^n (-1)^{k+1}\frac{n!}{k!} = n! + \sum_{k=1}^n (-1)^k\frac{n!}{k!} = n!\sum_{k=0}^n \frac{(-1)^k}{k!}
$$
(the $k=0$ term contributes $n!$ back in).
:::

::: {#prp-derangement-recurrence .proposition name="Recurrence"}
For $n\ge2$,
$$
D_n = (n-1)\big(D_{n-1}+D_{n-2}\big), \qquad D_0=1,\ D_1=0.
$$
:::

::: {.proof}
**Choosing $\sigma(n)$**: In a derangement, $\sigma(n)=j$ for some $j\ne n$, giving $n-1$ choices of $j$. It remains to show that, for each fixed $j$, exactly $D_{n-1}+D_{n-2}$ derangements have $\sigma(n)=j$.

Fix $j$. Positions $1,\dots,n-1$ must be filled with the values $\{1,\dots,n\}\setminus\{j\}$, which include $n$. Split by whether position $j$ receives $n$.

**Case 1** ($\sigma(j)=n$): Then $j$ and $n$ are swapped. The other $n-2$ elements $\{1,\dots,n\}\setminus\{j,n\}$ must fill their own positions with no fixed point: $D_{n-2}$ ways.

**Case 2** ($\sigma(j)\ne n$): The constraints on positions $1,\dots,n-1$ are
$$
\sigma(i)\ne i\quad (i\ne j), \qquad \sigma(j)\ne n,
$$
because the value $j$ is already used at position $n$, so $\sigma(j)\ne j$ holds automatically. Thus the value $n$ plays exactly the role of the value $j$: its only forbidden position is $j$. Define
$$
\Phi:\ (\sigma(1),\dots,\sigma(n-1)) \longmapsto \text{same sequence, with value } n \text{ replaced by } j.
$$

- $\Phi(\sigma)$ is a derangement of $\{1,\dots,n-1\}$: positions $i\ne j$ still avoid $i$, and position $j$ now avoids $j$ because it avoided $n$.
- $\Phi$ is invertible: given a derangement $\tau$ of $\{1,\dots,n-1\}$, replace the value $j$ by $n$ and append $\sigma(n)=j$. Since $\tau(j)\ne j$, the value $n$ does not land in position $j$, so the result lies in Case 2.

By the bijection rule (@thm-bijection-rule), Case 2 contains $D_{n-1}$ derangements.

**Combining**: Cases 1 and 2 are disjoint and exhaustive, so each $j$ contributes $D_{n-1}+D_{n-2}$ (sum rule, @sec-math-discrete-counting-sum-and-product-rules). Over the $n-1$ choices of $j$ (product rule, @sec-math-discrete-counting-sum-and-product-rules) this gives the recurrence.

**Boundary values**: $D_1=0$, since the only permutation $(1)$ fixes $1$. $D_0=1$, since the empty permutation has no fixed point. Check $n=2$: $D_2=1\cdot(D_1+D_0)=1$, matching the single derangement $(2,1)$.
:::

::: {#exm-derangement-cases .example name="The two cases for $n=4$, $j=3$"}
The derangements of $\{1,2,3,4\}$ with $\sigma(4)=3$ are:

| $\sigma$ | $\sigma(3)$ | case |
|:-:|:-:|:--|
| $(2,1,4,3)$ | $4$ | Case 1: $\{1,2\}$ deranged as $(2,1)$ |
| $(2,4,1,3)$ | $1$ | Case 2: $\Phi$ gives $(2,3,1)$ |
| $(4,1,2,3)$ | $2$ | Case 2: $\Phi$ gives $(3,1,2)$ |

Case 2 recovers exactly the $D_3=2$ derangements of $\{1,2,3\}$, so $j=3$ contributes $1+2=3$. Over the $3$ choices of $j$, $D_4=9$.
:::

::: {#exm-derangement-small-values .example name="Small values"}

| $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $D_n$ | $1$ | $0$ | $1$ | $2$ | $9$ | $44$ | $265$ |

With memoization, the recurrence computes $D_n$ using $O(n)$ arithmetic operations. Check against @thm-derangement-count at $n=4$:
$$
24\left(1-1+\frac12-\frac16+\frac1{24}\right)=9.
$$
:::

::: {#cor-derangement-limit .corollary name="Limiting probability"}
$$
\lim_{n\to\infty} \frac{D_n}{n!} = \frac{1}{e}.
$$
:::

::: {.proof}
$$
\frac{D_n}{n!} = \sum_{k=0}^n \frac{(-1)^k}{k!},
$$
the $n$-th partial sum of the Taylor series $e^{-1}=\sum_{k=0}^\infty \dfrac{(-1)^k}{k!}$ (this partial sum converges to $e^{-1}$ as $n\to\infty$).
:::

::: {.remark name="Interpretation"}
The fraction of permutations with *no* fixed point converges rapidly to $1/e\approx0.368$ -- already accurate to $4$ decimal places by $n=7$. This underlies the classic "hat-check problem": the probability nobody gets their own hat back, for $n$ people with hats mixed uniformly at random, is $D_n/n!\to1/e$, essentially independent of $n$ once $n$ is even moderately large.
:::
