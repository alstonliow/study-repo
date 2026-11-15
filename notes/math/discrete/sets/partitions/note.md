---
title: "Partitions"
sources: [fit1058-cn-1.15]
requires: [math/discrete/relations/equivalence-relations]
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Partitions. -->

::: {#def-partition .definition name="Partition"}

A *partition* of $A$ is a set of pairwise disjoint, nonempty subsets of $A$ (called *parts*, *blocks*, or *cells*) whose union is $A$.

:::

::: {#rmk-partitions-1 .remark name="Equivalent characterization"}

A collection of nonempty subsets of $A$ is a partition of $A$ iff every element of $A$ belongs to *exactly one* part.

:::

::: {#exm-partitions-1 .example}

For $A = \{a,b,c\}$: $\{\{a,c\},\{b\}\}$ and $\{\{a\},\{b\},\{c\}\}$ are partitions; $\{\{a,b\},\{c\},\emptyset\}$ fails (empty part), $\{\{a,b\},\{b,c\}\}$ fails (not disjoint), $\{\{a\},\{b\}\}$ fails (union $\neq A$, misses $c$).

:::

::: {#fig-partitions-1}

```{=latex}
\begin{tikzpicture}
  \draw[ink, rounded corners] (0,0) rectangle (3,2.3);
  \draw[regionA] (0.25,1.2) rectangle (2.75,2.05);
  \draw[regionB] (1.0,0.25) rectangle (2.0,0.95);
  \node at (0.9,1.62) {$a$}; \node at (2.1,1.62) {$c$}; \node at (1.5,0.6) {$b$};
  \node[lbl] at (1.5,-0.4) {a partition};
  \begin{scope}[xshift=4.2cm]
    \draw[ink, rounded corners] (0,0) rectangle (3,2.3);
    \filldraw[draw=primaryStrong, tintA] (1.05,1.15) ellipse (0.95 and 0.55);
    \filldraw[draw=accentLight, tintB] (1.95,1.15) ellipse (0.95 and 0.55);
    \node at (0.55,1.15) {$a$}; \node at (1.5,1.15) {$b$}; \node at (2.45,1.15) {$c$};
    \node[lbl] at (1.5,-0.4) {not a partition};
  \end{scope}
\end{tikzpicture}
```

$\{\{a,c\},\{b\}\}$ is a partition of $\{a,b,c\}$ (left); $\{\{a,b\},\{b,c\}\}$ is not, because the parts overlap at $b$ (right)

:::

::: {#def-coarsest-and-finest-partitions .definition name="Coarsest and finest partitions"}

For any $A$: the *coarsest* partition is $\{A\}$ (one part, everything together); the *finest* partition is $\{\{a\} : a \in A\}$ (one singleton part per element). If $|A|=1$ these coincide; otherwise they are the two extremes, with every other partition of $A$ intermediate between them.

:::

::: {#rmk-partitions-2 .remark name="Connection to equivalence relations"}

Partitions are closely tied to *equivalence relations* (reflexive, symmetric, transitive relations – @sec-math-discrete-relations-equivalence-relations): every equivalence relation $R$ on $A$ partitions $A$ into *equivalence classes* $[a]_R = \{x \in A : x\,R\,a\}$, and conversely every partition of $A$ arises this way from exactly one equivalence relation (namely, $x\,R\,y \iff x,y$ lie in the same part). We revisit this correspondence formally once binary relations are covered.

:::
