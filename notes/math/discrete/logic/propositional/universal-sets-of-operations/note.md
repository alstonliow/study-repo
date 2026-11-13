---
title: "Universal sets of operations"
sources: [fit1058-cn-4.20]
requires: [math/discrete/logic/propositional/normal-forms]
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: Universal sets of operations. -->

::: {#def-universal-set-of-operations .definition name="Universal set of operations"}

$X$ is *universal* if every logical expression is equivalent to one using only operations from $X$.

:::

::: {#prp-universal-sets-of-operations-1 .proposition}

$\{\wedge,\vee,\neg\}$ is universal (immediate from DNF/CNF, @sec-math-discrete-logic-propositional-normal-forms).

:::

::: {#cor-universal-sets-of-operations-1 .corollary}

$\{\wedge,\neg\}$ and $\{\vee,\neg\}$ are each universal.

:::

::: {.proof}

De Morgan’s laws express $\vee$ in terms of $\wedge,\neg$ (and vice versa), so either can be dropped while keeping $\neg$.

:::

::: {.remark name="$\{\wedge,\vee\}$ is not universal"}

Without $\neg$, every expression built from $\wedge,\vee$ is *monotone*: increasing any input from $F$ to $T$ can never make the output go from $T$ to $F$. Since $\neg P$ itself is not monotone, it cannot be expressed – so $\{\wedge,\vee\}$ fails to be universal.

:::

::: {#def-sheffer-stroke-nand-extra .definition name="Sheffer stroke (NAND) (extra)"}

$$P \mid Q = \neg(P\wedge Q).$$

:::

::: {#prp-alone-is-universal-extra .proposition name="$\{\mid\}$ alone is universal (extra)"}

$$\neg P = P\mid P, \qquad P\wedge Q = (P\mid Q)\mid(P\mid Q), \qquad P\vee Q = (P\mid P)\mid(Q\mid Q).$$

:::

::: {.proof}

Check each directly by truth table, or: $P\mid P = \neg(P\wedge P) = \neg P$; then $(P\mid Q)\mid(P\mid Q) = \neg(P\mid Q) = \neg\neg(P\wedge Q) = P\wedge Q$; and $(P\mid P)\mid(Q\mid Q) = \neg P \mid \neg Q = \neg(\neg P\wedge\neg Q) = P\vee Q$ (De Morgan’s). Since $\{\wedge,\vee,\neg\}$ is universal and all three are expressible via $\mid$ alone, $\{\mid\}$ is universal.

:::

::: {.remark}

This is why NAND gates alone suffice to build any digital circuit – a genuinely important fact in computer engineering, well beyond what CN’s syllabus covers here.

:::
