---
title: "Truth Values and Propositions"
sources: [fit1058-cn-4.1, fit1058-cn-4.2, fit1058-cn-4.3, fit1058-cn-4.4]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: Truth values; Boolean variables; Propositions; Logical operations. -->

## Truth values

::: {#def-truth-values .definition name="Truth values"}

Logic (classical, two-valued) is built on two *truth values*: *True* ($T$) and *False* ($F$).

:::

::: {.remark}

Physically, truth values may correspond to presence/absence of electrical current, magnetisation, a switch’s on/off state, etc. – the abstraction lets us reason about logic independently of implementation. The *bit* (0 or 1) is a closely related abstraction: $F \leftrightarrow 0$, $T \leftrightarrow 1$.

:::

## Boolean variables

::: {#def-boolean-propositional-variable .definition name="Boolean / propositional variable"}

A *Boolean variable* (or *propositional variable*) is a variable whose value is $T$ or $F$.

:::

## Propositions

::: {#def-proposition .definition name="Proposition"}

A *proposition* is a declarative sentence that is either true or false, but not both.

:::

::: {#exm-propositions .example name="Propositions"}

$1+1=2$ (true); “The earth is flat.” (false); “It will rain tomorrow.” (a proposition – has a definite truth value, even if unknown to us right now).

:::

::: {#exm-not-propositions .example name="Not propositions"}

Questions (“Come and work for us!”), nonsensical or non-declarative sentences (Lewis Carroll’s “’Twas brillig...”), and self-referential sentences with no consistent truth value (“This statement is false.”) are not propositions.

:::

::: {.remark name="Naming a proposition"}

A proposition may be named by a Boolean variable, e.g. let $X$ be the proposition $1+1=2$; then $X$’s truth value is $T$.

:::

## Logical operations

::: {.remark name="The basic connectives"}

|             |            |
|:------------|:-----------|
| Not         | $\neg$     |
| And         | $\wedge$   |
| Or          | $\vee$     |
| Implies     | $\implies$ |
| Equivalence | $\iff$     |

Logical operations combining propositions are also called *connectives*; in hardware they are implemented as *logic gates*.

:::
