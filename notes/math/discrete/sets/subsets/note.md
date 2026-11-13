---
title: "Subsets"
sources: [fit1058-cn-1.6, fit1058-cn-1.7]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Subsets and supersets; Minimal, minimum, maximal, maximum. -->

## Subsets and supersets

::: {#def-subset-superset .definition name="Subset, superset"}

$$A \subseteq B \iff \forall x\,(x \in A \rightarrow x \in B), \qquad
A \supseteq B \iff B \subseteq A.$$

:::

::: {#def-proper-subset .definition name="Proper subset"}

$$A \subsetneq B \iff (A \subseteq B) \wedge (A \neq B).$$

:::

::: {#prp-subsets-1 .proposition}

For every set $A$, $\emptyset \subseteq A$.

:::

::: {.proof}

By definition $\emptyset \subseteq A$ iff $\forall x\,(x \in \emptyset \rightarrow x \in A)$. Since $x \in \emptyset$ is always false, the conditional is vacuously true for every $x$, so the universally quantified statement holds. Hence $\emptyset \subseteq A$.

:::

::: {#prp-subsets-2 .proposition}

$\subseteq$ is reflexive ($A \subseteq A$) and transitive ($A \subseteq B \wedge B \subseteq C \Rightarrow A \subseteq C$).

:::

## Minimal, minimum, maximal, maximum

::: {#exm-motivating-example-cliques .example name="Motivating example: cliques"}

Let $B$ be a set of people, with some pairs acquainted. A *clique* is a subset $A \subseteq B$ such that every two people in $A$ know each other. We want to describe the “biggest” cliques – but “biggest” has two different meanings.

:::

::: {#def-maximum-maximal-w-r-t .definition name="Maximum, maximal, w.r.t.\ a family $\mathcal{F}$ of sets sharing a property"}

Let $\mathcal{F}$ be a family of subsets of some set, all sharing a given property (e.g. “is a clique”), ordered by $\subseteq$.

- $M \in \mathcal{F}$ is a *maximum* if $S \subseteq M$ for every $S \in \mathcal{F}$ (largest possible size).

- $M \in \mathcal{F}$ is *maximal* if $M$ is not a proper subset of any $S \in \mathcal{F}$ (cannot be enlarged while keeping the property).

:::

::: {#prp-subsets-1-2 .proposition}

Every maximum is maximal.

:::

::: {.proof}

If $M$ is a maximum, then $S \subseteq M$ for all $S \in \mathcal{F}$, so no $S \in \mathcal{F}$ can have $M \subsetneq S$ (that would force $M \subsetneq S \subseteq M$, impossible). Hence $M$ is maximal.

:::

::: {.remark}

The converse fails in general: a maximal clique need not be a maximum clique – it just cannot be enlarged, while some other, larger clique may exist elsewhere in $B$.

:::

::: {#def-minimum-minimal-dual-definitions .definition name="Minimum, minimal – dual definitions"}

Dually, for $\mathcal{F}$ ordered by $\subseteq$:

- $m \in \mathcal{F}$ is a *minimum* if $m \subseteq S$ for every $S \in \mathcal{F}$.

- $m \in \mathcal{F}$ is *minimal* if $m$ is not a proper superset of any $S \in \mathcal{F}$ (removing anything from $m$ destroys the property).

Every minimum is minimal; the converse fails in general.

:::

::: {.remark name="Why the distinction matters here but not for $\mathbb{R}$"}

For real numbers, $\le$ is a *total order*: any two reals are comparable, so “cannot be increased” and “is the largest” coincide, and *maximum*/*maximal* are used interchangeably. But $\subseteq$ is only a *partial order*: two sets $A,B$ can be *incomparable* ($A \not\subseteq B$ and $B \not\subseteq A$). This is exactly why a family can have several maximal elements without any single maximum.

:::
