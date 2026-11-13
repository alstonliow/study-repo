---
title: "Sets and Elements"
sources: [fit1058-cn-1.1, fit1058-cn-1.2]
requires: [math/discrete/sets/cardinality-and-standard-sets]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Sets and elements; Specifying sets. -->

## Sets and elements

::: {.remark name="Naive set theory"}

We work within *naive set theory*: a set is a primitive, undefined notion, and any well-specified collection of objects is assumed to form a set. This suffices for ordinary practice, but unrestricted set formation is inconsistent in general – *Russell’s paradox* considers $R = \{x : x \notin x\}$, for which $R \in R \leftrightarrow R \notin R$, a contradiction. Axiomatic set theory (e.g. ZFC) resolves this by restricting which collections may form sets.

:::

::: {#def-set .definition name="Set"}

A set $A$ is an unordered collection of distinct objects, called *elements* (or *members*) of $A$.

:::

::: {#def-membership .definition name="Membership"}

$$a \in A \iff a \text{ is an element of } A, \qquad
a \notin A \iff \neg(a \in A).$$

:::

::: {#def-set-equality .definition name="Set equality"}

$$A = B \iff \forall x\, (x \in A \leftrightarrow x \in B).$$

:::

::: {#def-empty-set .definition name="Empty set"}

$\emptyset = \{\}$ is the unique set satisfying $\forall x\, (x \notin \emptyset)$.

:::

::: {#def-singleton-unordered-pair .definition name="Singleton, unordered pair"}

$\{a\}$ has the sole element $a$; $\{a,b\}$ has elements $a,b$, with $\{a,b\} = \{b,a\}$.

:::

::: {#def-standard-number-sets .definition name="Standard number sets"}

$$\begin{aligned}
\mathbb{N}&= \{0,1,2,3,\dots\} & \text{(natural numbers)}\\
\mathbb{Z}&= \{\dots,-2,-1,0,1,2,\dots\} & \text{(integers)}\\
\mathbb{Z}^+ &= \{1,2,3,\dots\} & \text{(positive integers)}\\
\mathbb{Q}&= \{p/q : p \in \mathbb{Z},\ q \in \mathbb{Z},\ q \neq 0\} & \text{(rationals)}\\
\mathbb{R}&&\text{(reals)}\\
\mathbb{C}&&\text{(complex numbers)}
\end{aligned}$$

:::

::: {.remark}

Rosen takes $0 \in \mathbb{N}$; confirm this matches CN @sec-math-discrete-sets-cardinality-and-standard-sets before relying on it elsewhere.

:::

::: {#def-universal-set .definition name="Universal set"}

The *universal set* $U$ is the set containing all objects under discussion in a given context; every set considered is implicitly $A \subseteq U$.

:::

::: {.remark name="Venn diagram"}

A *Venn diagram* represents sets as regions enclosed by curves inside a rectangle representing $U$; overlapping regions represent intersections, non-overlapping regions represent disjointness.

:::

## Specifying sets

::: {#def-roster-method .definition name="Roster method"}

$A = \{a_1, a_2, \dots, a_n\}$. Order and repetition do not matter: $\{1,2,3\} = \{3,2,1\} = \{1,1,2,3\}$.

:::

::: {.remark name="Ellipsis notation"}

$\{1,2,3,\dots\}$, or bounded: $\{1,2,\dots,100\}$.

:::

::: {#def-set-builder-notation .definition name="Set-builder notation"}

$A = \{x \in U : P(x)\}$, equivalently $\{x \mid P(x)\}$, where $P$ is a predicate.

:::

::: {#exm-sets-and-elements-1 .example}

$\{x \in \mathbb{Z}: x^2 < 9\} = \{-2,-1,0,1,2\}$.

:::

::: {#def-interval-notation .definition name="Interval notation, $a,b \in \mathbb{R}$, $a<b$"}

$$[a,b] = \{x \in \mathbb{R}: a \le x \le b\}, \qquad
(a,b) = \{x \in \mathbb{R}: a < x < b\},$$
$$[a,b) = \{x \in \mathbb{R}: a \le x < b\}, \qquad
(a,b] = \{x \in \mathbb{R}: a < x \le b\}.$$

:::

```{=latex}
\begin{picture}(10,1.5)
\thicklines
\put(0,0.7){\line(1,0){10}}
\multiput(0,0.4)(1,0){11}{\line(0,1){0.6}}
\put(2,0.7){\circle*{0.15}}
\put(7,0.7){\circle{0.15}}
\put(1.85,0){$a$}
\put(6.85,0){$b$}
\end{picture}
\end{center}
```

$[a,b)$: filled dot at $a$ (included), open circle at $b$ (excluded)
