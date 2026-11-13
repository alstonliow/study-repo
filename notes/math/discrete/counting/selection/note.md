---
title: Selection and Ordered Selection
sources: [fit1058-cn-8.5, fit1058-cn-8.6, fit1058-cn-8.7]
requires: [math/discrete/counting/sum-and-product-rules]
status: draft
---

<!-- Migrated from 1058note 08-counting-combinatorics.tex, §8.5–8.7. -->

## Selection

::: {.remark name="Four kinds of selection"}

|  | **order matters** | **order irrelevant** |
|:--|:--|:--|
| **with replacement** | ordered, w/ replacement (@sec-math-discrete-counting-selection) | unordered, w/ replacement (@sec-math-discrete-counting-stars-and-bars) |
| **without replacement** | ordered, w/o replacement (@sec-math-discrete-counting-selection) | unordered, w/o replacement (@sec-math-discrete-counting-combinations) |

:::

## Ordered selection with replacement

::: {#prp-ordered-with-replacement .proposition}
The number of length-$r$ sequences over an $n$-element set $A$ is
$$
|A\times\cdots\times A| = n^r
$$
(@sec-math-discrete-sets-cartesian-product, @sec-math-discrete-sets-cardinality-and-standard-sets for the string special case, @sec-math-discrete-functions-counting for counting functions).
:::

## Ordered selection without replacement

::: {#def-falling-factorial .definition name="Falling factorial, permutations"}
$$
(n)_r = n(n-1)(n-2)\cdots(n-r+1) = \frac{n!}{(n-r)!}, \qquad \text{also written } {}_nP_r \text{ or } P(n,r).
$$
:::

::: {.proof name="Derivation"}
Choice $k$ (for $k=1,\dots,r$) has $n-(k-1)$ options remaining (the $k-1$ prior choices excluded). By the product rule (@sec-math-discrete-counting-sum-and-product-rules):
$$
n\cdot(n-1)\cdots(n-r+1).
$$
:::

::: {.remark name="Counting injections"}
Already the counting-injections theorem of @sec-math-discrete-functions-counting.
:::
