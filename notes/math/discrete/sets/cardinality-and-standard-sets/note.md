---
title: "Cardinality and Standard Sets"
sources: [fit1058-cn-1.3, fit1058-cn-1.4, fit1058-cn-1.5]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Cardinality; Sets of numbers; Sets of strings. -->

## Cardinality

::: {#def-cardinality .definition name="Cardinality"}

For finite $A$, $|A|$ is the number of distinct elements of $A$. $|\emptyset| = 0$.

:::

::: {#def-finite-infinite-set .definition name="Finite, infinite set"}

$A$ is *finite* if $A = \emptyset$ or there exists $n \in \mathbb{Z}^+$ and a bijection $\{1,2,\dots,n\} \to A$; then $|A| = n$. If no such $n$ exists, $A$ is *infinite*.

:::

## Sets of numbers

::: {#def-signed-subsets .definition name="Signed subsets"}

$$\mathbb{Z}^+ = \{1,2,3,\dots\}, \quad \mathbb{Z}^- = \{-1,-2,-3,\dots\}, \quad
\mathbb{R}^+ = \{x \in \mathbb{R}: x > 0\}, \quad \mathbb{R}^- = \{x \in \mathbb{R}: x < 0\}.$$

:::

::: {.remark}

$\mathbb{N}\subseteq \mathbb{Z}\subseteq \mathbb{Q}\subseteq \mathbb{R}\subseteq \mathbb{C}$.

:::

## Sets of strings

::: {#def-alphabet-string-length .definition name="Alphabet, string, length"}

An *alphabet* $\Sigma$ is a finite nonempty set of symbols. A *string* over $\Sigma$ is a finite sequence of symbols from $\Sigma$. $|w|$ is the length of $w$; $\varepsilon$ is the *empty string*, $|\varepsilon| = 0$.

:::

::: {#def-cardinality-and-standard-sets-1 .definition name="$\Sigma^*$, $\Sigma^n$"}

$$\Sigma^n = \{w : w \text{ over } \Sigma,\ |w| = n\}, \qquad
\Sigma^* = \bigcup_{n=0}^{\infty} \Sigma^n.$$

:::
