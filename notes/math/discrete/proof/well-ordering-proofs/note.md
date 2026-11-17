---
title: "Well-Ordering Proofs"
sources: [mcs-2.1, mcs-2.2, mcs-2.4]
requires: [math/discrete/proof/induction]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Chapter 2, in our own wording; proofs written out in steps. The principle itself is @def-well-ordering-property. -->

## A template

The well-ordering property (@def-well-ordering-property) gives a second way, besides induction, to prove that a statement $P(n)$ holds for every $n\in\mathbb N$.

::: {#rmk-well-ordering-proofs-template .remark name="Template for a well-ordering proof"}

1. Let $C=\{n\in\mathbb N:P(n)\text{ is false}\}$, the set of counterexamples.

2. Assume, for contradiction, that $C\ne\emptyset$.

3. By the well-ordering property, $C$ has a least element $m$.

4. Derive a contradiction, usually by showing that $P(m)$ is true after all, or that $C$ has an element smaller than $m$. This is the step that needs ideas.

5. Conclude that $C=\emptyset$: $P(n)$ holds for all $n$.

The same template, applied to the set of steps at which something first goes wrong, proves that a process never reaches a bad state (@sec-math-discrete-proof-state-machines).

:::

::: {#exm-well-ordering-geometric-sum .example name="A geometric sum by well ordering"}

For every real $r\ne1$ and every $n\in\mathbb N$, $\sum_{i=0}^nr^i=\dfrac{r^{n+1}-1}{r-1}$.

:::

::: {.proof}

1. Let $C$ be the set of $n$ for which the formula fails, and suppose $C\ne\emptyset$. Let $m$ be its least element.

2. $m\ne0$, since for $n=0$ both sides are $1$. So $m\ge1$, and $m-1\notin C$ because $m$ is least: $\sum_{i=0}^{m-1}r^i=\frac{r^m-1}{r-1}$.

3. Adding $r^m$ to both sides, $\sum_{i=0}^mr^i=\frac{r^m-1+r^{m+1}-r^m}{r-1}=\frac{r^{m+1}-1}{r-1}$, so the formula holds for $m$, contradicting $m\in C$.

:::

::: {#exm-well-ordering-lowest-terms .example name="Fractions in lowest terms"}

Every positive rational number can be written as $\frac mn$ with $m,n\in\mathbb Z^+$ having no common prime factor.

:::

::: {.proof}

1. Fix a positive rational $q$. The set $C=\{m\in\mathbb Z^+: q=\frac mn\text{ for some }n\in\mathbb Z^+\}$ of possible numerators is non-empty, so it has a least element $m_0$ (@def-well-ordering-property); say $q=\frac{m_0}{n_0}$.

2. Suppose, for contradiction, that some prime $p$ divides both $m_0$ and $n_0$: $m_0=pm_1$, $n_0=pn_1$ with $m_1,n_1\ge1$.

3. Then $q=\frac{m_1}{n_1}$, so $m_1\in C$, and $m_1<m_0$. This contradicts the minimality of $m_0$. So $\frac{m_0}{n_0}$ is in lowest terms.

:::

## Well-ordered sets

::: {#def-well-ordered-set .definition name="Well-ordered set"}

A set $S$ of real numbers is *well ordered* if every non-empty subset of $S$ has a least element. A *lower bound* of $S$ is a number $b$ with $b\le s$ for all $s\in S$; an *upper bound* satisfies $b\ge s$ for all $s\in S$. A bound need not belong to $S$.

:::

So $\mathbb N$ is well ordered, and every subset of a well-ordered set is well ordered. Having a least element is not enough: the non-negative rationals have the least element $0$, but the subset of positive rationals has no least element.

::: {#thm-shifted-well-ordering .theorem name="Integers bounded below are well ordered"}

For every integer $n$, the set $\{k\in\mathbb Z:k\ge n\}$ is well ordered. Hence every set of integers with a lower bound is well ordered, and every non-empty set of integers with an upper bound has a largest element.

:::

::: {.proof}

1. Let $S$ be a non-empty set of integers $\ge n$. Then $S-n=\{s-n:s\in S\}$ is a non-empty subset of $\mathbb N$, with least element $m$ by @def-well-ordering-property. So $m+n$ is the least element of $S$.

2. If a set of integers has a real lower bound $b$, then the integer $\lfloor b\rfloor\le b$ is also a lower bound, so the set lies inside $\{k:k\ge\lfloor b\rfloor\}$, which is well ordered by step 1.

3. If $S\ne\emptyset$ has an upper bound $b$, then $-S=\{-s:s\in S\}$ has the lower bound $-b$, so it has a least element $-s_0$ by step 2. Then $s_0$ is the largest element of $S$.

:::

::: {#exm-well-ordered-fractions .example name="A well-ordered set that is not made of integers"}

$F=\bigl\{\frac n{n+1}:n\in\mathbb N\bigr\}=\{0,\frac12,\frac23,\frac34,\dots\}$ is well ordered. The map $n\mapsto\frac n{n+1}$ is strictly increasing, since $\frac n{n+1}=1-\frac1{n+1}$. So for a non-empty $T\subseteq F$, the least $n$ with $\frac n{n+1}\in T$ (which exists by well ordering of $\mathbb N$) gives the least element of $T$.

:::

::: {#rmk-well-ordering-proofs-termination .remark name="Proving that a computation stops"}

To show that a computation cannot run forever, attach to each step a value from a well-ordered set that strictly decreases from step to step. An infinite run would give a non-empty set of values with no least element. This is the standard termination argument for state machines (@sec-math-discrete-proof-state-machines).

:::
