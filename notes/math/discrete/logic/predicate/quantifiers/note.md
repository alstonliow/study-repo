---
title: "Quantifiers"
sources: [fit1058-cn-5.5, fit1058-cn-5.6, fit1058-cn-5.7, fit1058-cn-5.8, fit1058-cn-5.9]
requires: [math/discrete/logic/propositional/laws-of-boolean-algebra, math/discrete/sets/subsets]
status: draft
---

<!-- Migrated from 1058note notes/chapters/05-predicate-logic.tex: Building logical expressions with predicates; Existential quantifier; Restricting existentially quantified variables; Universal quantifier; Restricting universally quantified variables. -->

## Building logical expressions with predicates

::: {#def-predicate-logic-expression-recursive .definition name="Predicate logic expression, recursive"}

- $T, F$ are predicate logic expressions.

- A predicate applied to terms of matching domains is a predicate logic expression.

- If $E,F$ are predicate logic expressions, so are $(E),\ \neg E,\ E\wedge F,\ E\vee F,\ E\implies F,\ E\iff F$.

:::

::: {.remark name="Free variables propagate"}

A predicate logic expression’s free variables are the union of the free variables of its terms/sub-expressions – combining expressions never removes a free variable (only quantification, @sec-math-discrete-logic-predicate-quantifiers, does that).

:::

::: {#exm-quantifiers-1 .example}

$(1<i)\wedge(i<n)$ has free variables $i,n$. $\mathrm{Parent}(X,Y)\iff\big(Y=\mathrm{MotherOf}(X)\big)\vee\big(Y=\mathrm{FatherOf}(X)\big)$ has free variables $X,Y$.

:::

## Existential quantifier

::: {#def-existential-quantifier .definition name="Existential quantifier"}

For predicate $P(x)$ on domain $D$:
$$\exists x\, P(x)$$
is true iff $P(a)$ is true for *at least one* $a\in D$.

:::

::: {.remark name="Punctuation"}

$\exists x : P(x)$, $\exists x.\, P(x)$, $\exists x\, P(x)$ are all used; the colon/period is read “such that”.

:::

::: {#def-bound-variable .definition name="Bound variable"}

Once quantified, $x$ is *bound*: no longer available to receive a specific value. A fully-quantified expression has no free variables and is a genuine proposition, with a definite truth value.

:::

::: {.remark name="Domain matters"}

$\exists W\in\mathbb{N}:\ W<0$ is false; $\exists W\in\mathbb{Z}:\ W<0$ is true – same predicate, different domain, different truth value.

:::

::: {.remark name="Analogy with disjunction – and where it breaks"}

$\exists x \in D,\ P(x)$ behaves like the disjunction $\bigvee_{a\in D} P(a)$ – true iff at least one disjunct is true. But this is only an analogy: disjunctions must be *finite*, while $D$ may be infinite, so existential quantification genuinely extends what propositional logic alone can express.

:::

::: {.remark name="Vacuous quantification"}

If $x$ does not appear in $P$, $\exists x\, P$ is equivalent to $P$ itself (the quantifier is inert): e.g. $\exists w:\ z<0$ is just $z<0$.

:::

::: {.remark}

Quantifiers apply only to variables, never to constants: $\exists 5$ or $\exists\text{Annie}$ are ill-formed.

:::

## Restricting existentially quantified variables

::: {.remark name="Restricting $\exists$ uses $\wedge$"}

To assert “some $X$ satisfying $R(X)$ also satisfies $P(X)$”:
$$\exists X:\ R(X) \wedge P(X).$$

:::

## Universal quantifier

::: {#def-universal-quantifier .definition name="Universal quantifier"}

For predicate $P(x)$ on domain $D$:
$$\forall x\, P(x)$$
is true iff $P(a)$ is true for *every* $a\in D$.

:::

::: {.remark}

As with $\exists$: the quantified variable becomes bound; an irrelevant quantifier (variable not appearing in the body) can be dropped.

:::

::: {.remark name="Vacuous truth generalizes"}

$\forall x\in\emptyset,\ P(x)$ is vacuously true for *any* $P$, exactly generalizing $\emptyset\subseteq A$ (@sec-math-discrete-sets-subsets Theorem 1) to arbitrary predicates, not just set membership.

:::

## Restricting universally quantified variables

::: {.remark name="Restricting $\forall$ uses $\implies$"}

To assert “every $X$ satisfying $R(X)$ also satisfies $P(X)$”:
$$\forall X:\ R(X) \implies P(X).$$

:::

::: {.remark name="Preview: De Morgan's laws for quantifiers"}

$$\neg\forall x\, P(x) \ \equiv\ \exists x\,\neg P(x), \qquad \neg\exists x\, P(x) \ \equiv\ \forall x\,\neg P(x).$$

:::

::: {.remark}

Consequence: negating $\forall X: R(X)\implies P(X)$ gives $\exists X: R(X)\wedge\neg P(X)$ – exactly matching the $\exists/\wedge$ pairing above, since $\neg(R\implies P) \equiv R\wedge\neg P$ (@sec-math-discrete-logic-propositional-laws-of-boolean-algebra).

:::
