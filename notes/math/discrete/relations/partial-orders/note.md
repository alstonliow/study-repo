---
title: "Partial Orders"
sources: [mcs-9.6, mcs-9.7, mcs-9.8, mcs-9.9, mcs-9.11]
requires: [math/discrete/relations/combining]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Sections 9.6-9.9 and 9.11, in our own wording; proofs written out in steps. -->

## Strict and weak partial orders

::: {#def-partial-order .definition name="Partial order"}

A relation $R$ on a set $A$ is a *strict partial order* if it is transitive and asymmetric (@def-transitive, @def-asymmetric). It is a *weak partial order* if it is transitive, antisymmetric and reflexive (@def-antisymmetric, @def-reflexive). A set with a partial order is a *partially ordered set* (poset).

:::

::: {#exm-partial-orders .example name="Familiar partial orders"}

1. $<$ on $\mathbb R$ is strict, and $\le$ is weak.

2. $\subsetneq$ on the subsets of a set is strict, and $\subseteq$ is weak.

3. Divisibility $a\mid b$ on $\mathbb Z^+$ is a weak partial order: $a\mid a$; $a\mid b$ and $b\mid a$ give $a=b$ for positive integers; and $a\mid b\mid c$ gives $a\mid c$.

4. The prerequisite relation between courses, "$x$ must be taken before $y$", is (ideally) a strict partial order.

:::

::: {#prp-strict-weak-orders .proposition name="Strict and weak versions"}

If $R$ is a strict partial order on $A$, then $R\cup\mathrm{Id}_A$ is a weak partial order. If $R$ is a weak partial order, then $R\setminus\mathrm{Id}_A$ is a strict partial order. Here $\mathrm{Id}_A=\{(a,a):a\in A\}$.

:::

::: {.proof}

1. Let $R$ be strict and $W=R\cup\mathrm{Id}_A$. $W$ is reflexive. If $aWb$ and $bWa$ with $a\ne b$, then $aRb$ and $bRa$, contradicting asymmetry; so $W$ is antisymmetric. For transitivity, if $aWb$ and $bWc$: when one of the pairs is in $\mathrm{Id}_A$ the conclusion $aWc$ is the other pair; otherwise $aRb$, $bRc$ give $aRc$.

2. Let $W$ be weak and $R=W\setminus\mathrm{Id}_A$. If $aRb$ and $bRa$, antisymmetry of $W$ gives $a=b$, but $R$ contains no pair $(a,a)$; so $R$ is asymmetric. If $aRb$ and $bRc$, then $aWc$ by transitivity, and $a\ne c$, since $a=c$ would give $aWb$ and $bWa$ with $a\ne b$. So $aRc$.

:::

## Comparing elements

::: {#def-comparable-linear-order .definition name="Comparable, linear order"}

Elements $a,b$ are *comparable* under a partial order $\preceq$ if $a\preceq b$ or $b\preceq a$. A partial order in which every two elements are comparable is a *linear* (or *total*) order. A *chain* is a set of pairwise comparable elements; an *antichain* is a set of pairwise incomparable elements. An element is *minimal* if no other element is below it, and *minimum* if it is below every element.

:::

$\le$ on $\mathbb R$ is linear. $\subseteq$ on the subsets of $\{1,2\}$ is not: $\{1\}$ and $\{2\}$ are incomparable, and they form an antichain. Divisibility on $\{2,3,4,6,12\}$ has two minimal elements, $2$ and $3$, and no minimum.

::: {#def-product-order .definition name="Product order"}

If $\preceq_1$ and $\preceq_2$ are weak partial orders on $A_1$ and $A_2$, the *product order* on $A_1\times A_2$ is $(a_1,a_2)\preceq(b_1,b_2)$ if and only if $a_1\preceq_1b_1$ and $a_2\preceq_2b_2$. It is again a weak partial order (check each property componentwise), but usually not linear even when both factors are: in $\mathbb N\times\mathbb N$, $(1,0)$ and $(0,1)$ are incomparable.

:::

## Every partial order is set containment

::: {#thm-poset-representation .theorem name="Representation by set containment"}

Let $\preceq$ be a weak partial order on $A$, and for $a\in A$ let $D(a)=\{b\in A:b\preceq a\}$. Then for all $a,c\in A$,
$$a\preceq c\iff D(a)\subseteq D(c),$$
and $a\mapsto D(a)$ is injective. So every weak partial order is isomorphic to $\subseteq$ on a collection of sets.

:::

::: {.proof}

1. Suppose $a\preceq c$. If $b\in D(a)$, then $b\preceq a\preceq c$, so $b\preceq c$ by transitivity, and $b\in D(c)$. So $D(a)\subseteq D(c)$.

2. Conversely, suppose $D(a)\subseteq D(c)$. By reflexivity $a\in D(a)$, so $a\in D(c)$, i.e. $a\preceq c$.

3. If $D(a)=D(c)$, then by step 2 $a\preceq c$ and $c\preceq a$, so $a=c$ by antisymmetry. So the map is injective.

:::

For a strict partial order $\prec$, apply the theorem to its weak version: $a\prec c$ if and only if $D(a)\subsetneq D(c)$.

::: {#rmk-partial-orders-summary .remark name="Summary of relational properties"}

| Relation | reflexive | irreflexive | symmetric | antisymmetric | asymmetric | transitive |
|---|---|---|---|---|---|---|
| Strict partial order | | yes | | yes | yes | yes |
| Weak partial order | yes | | | yes | | yes |
| Equivalence relation (@def-equivalence-relation) | yes | | yes | | | yes |

An asymmetric relation is automatically irreflexive and antisymmetric. Partial orders and equivalence relations are the two kinds of relation that appear most often; the only relation on $A$ that is both a weak partial order and an equivalence relation is the identity $\mathrm{Id}_A$.

:::
