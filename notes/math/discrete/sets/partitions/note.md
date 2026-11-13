---
title: "Partitions"
sources: [fit1058-cn-1.15]
requires: [math/discrete/relations/equivalence-relations]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Partitions. -->

::: {#def-partition .definition name="Partition"}

A *partition* of $A$ is a set of pairwise disjoint, nonempty subsets of $A$ (called *parts*, *blocks*, or *cells*) whose union is $A$.

:::

::: {.remark name="Equivalent characterization"}

A collection of nonempty subsets of $A$ is a partition of $A$ iff every element of $A$ belongs to *exactly one* part.

:::

::: {#exm-partitions-1 .example}

For $A = \{a,b,c\}$: $\{\{a,c\},\{b\}\}$ and $\{\{a\},\{b\},\{c\}\}$ are partitions; $\{\{a,b\},\{c\},\emptyset\}$ fails (empty part), $\{\{a,b\},\{b,c\}\}$ fails (not disjoint), $\{\{a\},\{b\}\}$ fails (union $\neq A$, misses $c$).

:::

::: {#def-coarsest-and-finest-partitions .definition name="Coarsest and finest partitions"}

For any $A$: the *coarsest* partition is $\{A\}$ (one part, everything together); the *finest* partition is $\{\{a\} : a \in A\}$ (one singleton part per element). If $|A|=1$ these coincide; otherwise they are the two extremes, with every other partition of $A$ intermediate between them.

:::

::: {.remark name="Connection to equivalence relations"}

Partitions are closely tied to *equivalence relations* (reflexive, symmetric, transitive relations – @sec-math-discrete-relations-equivalence-relations): every equivalence relation $R$ on $A$ partitions $A$ into *equivalence classes* $[a]_R = \{x \in A : x\,R\,a\}$, and conversely every partition of $A$ arises this way from exactly one equivalence relation (namely, $x\,R\,y \iff x,y$ lie in the same part). We revisit this correspondence formally once binary relations are covered.

:::
