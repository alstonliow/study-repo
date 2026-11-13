---
title: "Multiple Quantifiers"
sources: [fit1058-cn-5.10, fit1058-cn-5.11]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/05-predicate-logic.tex: Multiple quantifiers; Predicate logic expressions. -->

## Multiple quantifiers

::: {.remark name="Same-type quantifiers commute"}

$$\exists X\,\exists Y\, P = \exists Y\,\exists X\, P = \exists(X,Y)\, P, \qquad
\forall X\,\forall Y\, P = \forall Y\,\forall X\, P = \forall(X,Y)\, P.$$

:::

::: {.remark name="Mixed quantifiers do *not* commute"}

$$\exists X\,\forall Y\, P, \quad \forall X\,\exists Y\, P, \quad \exists Y\,\forall X\, P, \quad \forall Y\,\exists X\, P$$
are, in general, four genuinely different statements.

:::

::: {#exm-classic-order-matters-example .example name="Classic order-matters example"}

Let $D(x,y)$ mean “$x$ has dated $y$” on the domain of all people.
$$\exists x\,\forall y\, D(x,y): \text{someone has dated everyone}.$$
$$\forall y\,\exists x\, D(x,y): \text{everyone has been dated by someone.}$$
The first implies the second (that one exceptional dater witnesses every $y$), but not conversely – the second only needs, for each $y$, *some* $x$, possibly different for each $y$.

:::

::: {#prp-general-fact .proposition name="$\exists\forall \implies \forall\exists$, general fact"}

$$\exists x\,\forall y\, P(x,y) \ \implies\ \forall y\,\exists x\, P(x,y).$$
The converse implication does *not* hold in general.

:::

::: {.proof}

Suppose $\exists x\,\forall y\,P(x,y)$: fix such an $x_0$, so $P(x_0,y)$ holds for every $y$. Then for any $y$, taking $x=x_0$ witnesses $\exists x\,P(x,y)$ – so $\forall y\,\exists x\,P(x,y)$ holds. The dating example above (with $D$ not symmetric enough to reverse) shows the converse can fail.

:::

#### Quantifier–connective pitfall.\*\*\*

$\forall$ pairs with
$\Rightarrow$; $\exists$ pairs with $\wedge$ — the other way round
lets a trivial witness make the statement true for the wrong reason.

## Predicate logic expressions

::: {#def-predicate-logic-expression-complete-recursive .definition name="Predicate logic expression, complete recursive grammar"}

- $T,F$ are predicate logic expressions.

- Terms of matching domains plugged into a predicate give a predicate logic expression.

- If $E,F$ are predicate logic expressions: $(E),\ \neg E,\ E\wedge F,\ E\vee F,\ E\implies F,\ E\iff F$.

- If $E$ is a predicate logic expression and $X$ is a free variable of $E$: $\exists X: E$ and $\forall X: E$ are predicate logic expressions, and $X$ is *no longer free* in either.

:::

::: {.remark name="Free variables shrink under quantification"}

If $V$ is the free-variable set of $E$, then $\exists X: E$ and $\forall X: E$ each have free-variable set $V\setminus\{X\}$.

:::
