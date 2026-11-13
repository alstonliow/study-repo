---
title: Unordered Selection with Replacement
sources: [fit1058-cn-8.9]
requires: [math/discrete/counting/combinations, math/discrete/counting/selection, math/discrete/counting/sum-and-product-rules]
level: core
status: draft
---

<!-- Migrated from 1058note 08-counting-combinatorics.tex, §8.9. -->

::: {#def-multiset .definition name="Multiset"}
A *multiset* is a collection in which elements may repeat and order is irrelevant, e.g. $\{1,1,3,5\}$. A size-$r$ multiset drawn from $\{1,\dots,n\}$ is determined by its multiplicities $x_1,\dots,x_n\ge0$, where $x_1+\cdots+x_n=r$.
:::

::: {.remark name="Multisets and stars and bars"}
Hence the number of size-$r$ multisets from an $n$-set equals the stars-and-bars count below. This is exactly "unordered selection with replacement".
:::

::: {#exm-division-rule-fails .example name="Why the division rule fails here"}
Choose $r=5$ pieces of fruit from $n=3$ kinds (apple $=1$, banana $=2$, orange $=3$). There are $3^5=243$ ordered selections (@sec-math-discrete-counting-selection). Grouping them by the resulting multiset:

| multiset | \# ordered selections |
|:--|:-:|
| $\{2,2,2,2,2\}$ | $1$ |
| $\{1,2,2,2,2\}$ | $5$ |
| $\{1,1,2,2,3\}$ | $\dfrac{5!}{2!\,2!\,1!}=30$ |

The number of preimages is not constant, so @thm-division-rule does not apply. Indeed the answer turns out to be $21$, and $243/21$ is not an integer.
:::

::: {#thm-stars-and-bars .theorem name="Stars and bars"}
The number of $(x_1,\dots,x_n)$ with each $x_i\ge0$ integer and $x_1+\cdots+x_n=r$ is
$$
\binom{r+n-1}{n-1} = \binom{r+n-1}{r}.
$$
:::

::: {.proof}
Substitute $y_i=x_i+1\ge1$, so $\sum y_i = r+n$. Represent $r+n$ as $r+n$ ones in a row; the values $y_1,\dots,y_n$ correspond to $n-1$ barrier positions splitting them into $n$ groups, each barrier placed in one of the $r+n-1$ gaps *between* consecutive ones (no barrier before the first or after the last, since each $y_i\ge1$), with at most one barrier per gap (since each $y_i\ge1$, not $\ge0$).

This is exactly choosing $n-1$ of the $r+n-1$ gap-positions, without replacement, unordered (@sec-math-discrete-counting-combinations):
$$
\binom{r+n-1}{n-1}.
$$
:::

::: {.proof name="Alternative proof: $0/1$ strings"}
Encode $(x_1,\dots,x_n)$ as the string
$$
\underbrace{0\cdots0}_{x_1}\;1\;\underbrace{0\cdots0}_{x_2}\;1\;\cdots\;1\;\underbrace{0\cdots0}_{x_n}:
$$
each unit is a $0$, and the $n-1$ separators between consecutive "bins" are $1$s.

**Bijection**: onto the strings of length $r+n-1$ with exactly $r$ zeros.

- Every encoding has $r$ zeros and $n-1$ ones.
- Conversely, the $n-1$ ones cut any such string into $n$ (possibly empty) blocks of zeros, and the block lengths recover $(x_1,\dots,x_n)$.
- These two maps are mutually inverse.

**Counting the strings**: A string is determined by which $r$ of its $r+n-1$ positions hold $0$, an unordered selection without replacement (@sec-math-discrete-counting-combinations). By @thm-bijection-rule,
$$
\#\{(x_1,\dots,x_n)\} = \binom{r+n-1}{r}.
$$
:::

::: {#exm-stars-and-bars-encoding .example}
$n=5$, $r=4$: the ones split $00110110$ into the blocks $00$, (empty), $0$, (empty), $0$. So $(x_1,\dots,x_5)=(2,0,1,0,1)$, i.e. the multiset $\{1,1,3,5\}$. The length is $8=r+n-1$.
:::

::: {#exm-fruit-salad .example name="Fruit salad"}
$n=3$, $r=5$: there are $\binom{3+5-1}{5}=\binom75=21$ possible salads.
:::

::: {.remark name="Four different counts"}
All four answer "choose $r$ from $n$" differing only in order-matters and replacement-allowed -- yet the formulas look structurally unrelated at first glance. The stars-and-bars bijection above is what connects the fourth case back to ordinary binomial coefficients.
:::
