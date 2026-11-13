---
title: "Finding Proofs"
sources: [fit1058-cn-3.3, fit1058-cn-3.4, fit1058-cn-3.5]
requires: [math/discrete/proof/contradiction, math/discrete/proof/induction, math/discrete/proof/techniques, math/discrete/proof/theorems-and-proofs, math/discrete/sets/subsets]
status: draft
---

<!-- Migrated from 1058note notes/chapters/03-proofs.tex: Proofs of existential and universal statements; Finding proofs; Types of proofs. -->

## Proofs of existential and universal statements

::: {#def-existential-statement .definition name="Existential statement"}

An *existential statement* asserts $\exists x \in D,\ P(x)$ for some domain $D$ and predicate $P$: that *something* with the stated property exists. It may be true or false.

:::

::: {#exm-finding-proofs-1 .example}

English has a palindrome.

:::

::: {.proof}

‘rotator’ is an English word, and it reads the same forwards and backwards.

:::

::: {.remark name="Proving $\exists x,\ P(x)$"}

A single *witness* suffices: exhibit one $x \in D$ and verify $P(x)$ holds. No need to search further once found.

:::

::: {#def-universal-statement .definition name="Universal statement"}

A *universal statement* asserts $\forall x \in D,\ P(x)$: *everything* in $D$ has the property.

:::

## Finding proofs

::: {.remark name="No algorithm for finding proofs"}

There is no systematic method for discovering proofs.

:::

::: {.remark name="Strategy: proving $A \subseteq B$"}

1.  Name a general member: “Let $x \in A$.”

2.  Unpack what the definition of $A$ tells you about $x$.

3.  Follow the logical consequences.

4.  Aim to conclude $x$ satisfies the definition of $B$.

:::

::: {.remark name="Strategy: proving $A = B$ (sets)"}

Prove $A \subseteq B$ and $A \supseteq B$ separately (@sec-math-discrete-sets-subsets). Each direction uses the subset strategy above.

:::

::: {.remark name="Strategy: proving $A = B$ (numbers)"}

If direct symbolic manipulation (algebraic rules) can transform expression $A$ into expression $B$, use that. Otherwise, prove $A \le B$ and $A \ge B$ separately – the numerical analogue of the double-inclusion technique.

:::

::: {.remark name="Without loss of generality (WLOG)"}

When a proof is symmetric in two variables (swapping them leaves the claim unchanged), it suffices to prove one case and invoke the symmetry for the other – written “WLOG, assume $x\le y$” etc. Using WLOG when the situation is *not* actually symmetric is a common error – check the symmetry claim carefully before invoking it.

:::

::: {.remark name="Forward vs.\ backward reasoning"}

*Forward*: start from known facts/assumptions, derive consequences, until reaching the goal. *Backward*: start from the goal, ask “what would suffice to prove this?”, and work backward to something already known. Backward reasoning is often how a proof is *discovered*; it is then usually rewritten forward for presentation.

:::

## Types of proofs

::: {.remark name="Proof types"}

- *Direct proof / proof by symbolic manipulation* (@sec-math-discrete-proof-techniques): assume $P$, derive $Q$ via a direct chain of implications or equations.

- *Proof by construction* (@sec-math-discrete-proof-techniques, also called *proof by example*): exhibit a specific object and verify it works – a *constructive* existence proof, producing an explicit witness (contrast: *nonconstructive* existence proofs establish that something exists, e.g. via contradiction or a counting argument, without exhibiting it).

- *Proof by cases* (@sec-math-discrete-proof-techniques): split the domain into exhaustive cases, prove the claim in each.

- *Proof by contradiction* (@sec-math-discrete-proof-contradiction): assume the negation of the claim, derive a contradiction (some statement and its negation both true).

- *Proof by contraposition*: to prove $P \implies Q$, instead prove the equivalent $\neg Q \implies \neg P$ (@sec-math-discrete-proof-theorems-and-proofs’s contrapositive theorem) – useful when $\neg Q$ gives more to work with than $P$ does.

- *Vacuous / trivial proof*: prove $P \implies Q$ by showing $P$ is always false (vacuous) or $Q$ is always true (trivial).

- *Proof by (mathematical) induction* (@sec-math-discrete-proof-induction).

- *Uniqueness proofs*: show existence, then show any two witnesses must coincide.

This list is not exhaustive, and real proofs frequently mix several of these – e.g. a proof by cases where one case is handled by contradiction and another by direct construction.

:::

::: {#exm-vacuous-proof .example name="Vacuous proof"}

“For all $x\in\emptyset$, $x^2<0$.” True vacuously: $\emptyset$ has no members, so the implication “$x\in\emptyset \implies x^2<0$” is never tested against an actual counterexample.

:::
