---
title: "Cartesian product"
sources: [fit1058-cn-1.14]
requires: [math/discrete/sets/cardinality-and-standard-sets]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Cartesian product. -->

::: {#def-ordered-pair .definition name="Ordered pair"}

$(a,b)$ collects $a,b$ in order; $(a,b) = (c,d) \iff a=c \wedge b=d$.

:::

::: {#def-cartesian-product .definition name="Cartesian product"}

$A \times B = \{(a,b) : a \in A,\ b \in B\}$.

:::

::: {#prp-cartesian-product-1 .proposition}

$|A \times B| = |A|\cdot|B|$ for finite $A,B$.

:::

::: {.proof}

There are $|A|$ choices for the first coordinate, and independently $|B|$ choices for the second, so by the product rule there are $|A|\cdot|B|$ pairs.

:::

::: {#def-tuple-generalized-cartesian-product .definition name="$n$-tuple, generalized Cartesian product"}

For sets $A_1,\dots,A_n$:
$$A_1 \times A_2 \times \cdots \times A_n = \{(a_1,\dots,a_n) : a_i \in A_i,\ i=1,\dots,n\},$$
with equality of $n$-tuples componentwise: $(a_1,\dots,a_n)=(b_1,\dots,b_n) \iff a_i=b_i\ \forall i$. If finite, $|A_1\times\cdots\times A_n| = |A_1|\cdots|A_n|$.

:::

::: {#def-power-notation .definition name="Power notation"}

For a set $A$ and $n \in \mathbb{N}$, $A^n = A \times A \times \cdots \times A$ ($n$ factors); $A^0 = \{\emptyset\text{-tuple}\}$ is conventionally treated as a single-element set, $A^1 = A$. If $A$ is finite, $|A^n| = |A|^n$.

:::

::: {.remark}

When $A$ is an alphabet, $A^n$ is identified with strings of length $n$ (@sec-math-discrete-sets-cardinality-and-standard-sets): e.g. $\{0,1\}^3 = \{000,001,\dots,111\}$. Also $\mathbb{R}^n = \mathbb{R}\times\cdots\times\mathbb{R}$ is the set of coordinates in $n$-dimensional space.

:::

::: {#cor-cartesian-product-1 .corollary}

$|A_1 \times \cdots \times A_n| = |A_1| \cdot |A_2| \cdots |A_n|$ for finite $A_i$.

:::
