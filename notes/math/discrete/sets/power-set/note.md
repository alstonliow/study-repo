---
title: "The Power Set"
sources: [fit1058-cn-1.8, fit1058-cn-1.9, fit1058-cn-1.10]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Counting all subsets; The power set of a set; Counting subsets by size using binomial coefficients. -->

## Counting all subsets

::: {#thm-power-set-1 .theorem}

For finite $B$ with $|B| = n$, the number of subsets of $B$ is $2^n$.

:::

::: {.proof}

A subset is determined by choosing, independently for each of the $n$ elements, whether to include it (2 options per element). By the product rule, the number of independent choice-sequences is $\underbrace{2 \times 2 \times \cdots \times 2}_{n} = 2^n$, and each choice-sequence corresponds to exactly one subset.

:::

## The power set of a set

::: {#def-power-set .definition name="Power set"}

$\mathcal{P}(A) = \{S : S \subseteq A\}$.

:::

::: {#cor-power-set-1 .corollary}

$|A| = n \Rightarrow |\mathcal{P}(A)| = 2^n$.

:::

::: {.proof}

Immediate from @sec-math-discrete-sets-power-set: $\mathcal{P}(A)$ is exactly the set of subsets of $A$, and there are $2^n$ of them.

:::

::: {.remark}

Holds even for $A = \emptyset$: $n=0$ gives $2^0 = 1$, consistent with $\emptyset$ having exactly one subset, itself. $\mathcal{P}(A)$ is also written $2^A$.

:::

::: {#exm-power-set-1 .example}

$\emptyset$ has exactly one subset, itself, so $\mathcal{P}(\emptyset) = \{\emptyset\}$. The set $\{\emptyset\}$ has exactly two subsets, $\emptyset$ and $\{\emptyset\}$ itself, so $\mathcal{P}(\{\emptyset\}) = \{\emptyset, \{\emptyset\}\}$.

:::

## Counting subsets by size using binomial coefficients

::: {#def-binomial-coefficient .definition name="Binomial coefficient"}

For $0 \le k \le n$, $\dbinom{n}{k}$ (“$n$ choose $k$”) is the number of $k$-element subsets of an $n$-element set.

:::

::: {#prp-sum-over .proposition name="Sum over $k$"}

$$\sum_{k=0}^{n} \binom{n}{k} = 2^n.$$

:::

::: {.proof}

The binomial coefficients $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}$ partition the subsets of an $n$-set by size, so they sum to the total subset count, $2^n$ (@sec-math-discrete-sets-power-set).

:::

::: {#exm-power-set-1-2 .example name="$n=3$"}

Identify each subset of $\{1,2,3\}$ with its indicator vector (@sec-math-discrete-sets-power-set):

| subset | $\varnothing$ | $\{1\}$ | $\{2\}$ | $\{3\}$ | $\{1,2\}$ | $\{1,3\}$ | $\{2,3\}$ | $\{1,2,3\}$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| vector | $000$ | $100$ | $010$ | $001$ | $110$ | $101$ | $011$ | $111$ |

Grouped by size: $1+3+3+1=8=2^3$.

:::

::: {#prp-symmetry .proposition name="Symmetry"}

$$\binom{n}{k} = \binom{n}{n-k}.$$

:::

::: {.proof}

Choosing $k$ elements to include determines which $n-k$ elements are excluded, and vice versa; this is a bijection between $k$-subsets and $(n-k)$-subsets.

:::

::: {#thm-closed-form .theorem name="Closed form"}

$$\binom{n}{k} = \frac{n(n-1)(n-2)\cdots(n-k+1)}{k!} = \frac{n!}{k!(n-k)!}.$$

:::

::: {.proof}

Count *ordered* choices of $k$ distinct elements from $n$: $n$ options for the first, $n-1$ for the second, …, $n-k+1$ for the $k$-th, giving $n(n-1)\cdots(n-k+1) = n!/(n-k)!$ ordered sequences. Each $k$-subset is counted once for every ordering of its $k$ elements, i.e. $k!$ times, so
$$\binom{n}{k} = \frac{1}{k!} \cdot \frac{n!}{(n-k)!} = \frac{n!}{k!(n-k)!}.$$

:::
