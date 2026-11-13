---
title: "Doing Logic with Quantifiers"
sources: [fit1058-cn-5.12, fit1058-cn-5.13, fit1058-cn-5.15, fit1058-cn-5.14]
requires: [math/discrete/logic/predicate/multiple-quantifiers, math/discrete/logic/predicate/quantifiers]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/05-predicate-logic.tex: Doing logic with quantifiers; Duality between quantifiers; Some examples; Summary of rules for logic with quantifiers. -->

## Doing logic with quantifiers

::: {.remark name="Instantiation and generalization"}

$$\big(\forall X\, P(X)\big) \implies P(\mathrm{obj}), \qquad P(\mathrm{obj}) \implies \big(\exists X\, P(X)\big)$$
for any specific $\mathrm{obj}$ in $X$’s domain.

:::

::: {#prp-distributes-over-distributes-over .proposition name="$\forall$ distributes over $\wedge$; $\exists$ distributes over $\vee$"}

$$\forall X\,(P(X)\wedge Q(X)) \ \equiv\ (\forall X\, P(X)) \wedge (\forall X\, Q(X)),$$
$$\exists X\,(P(X)\vee Q(X)) \ \equiv\ (\exists X\, P(X)) \vee (\exists X\, Q(X)).$$

:::

::: {.remark name="$\forall$ over $\vee$, and $\exists$ over $\wedge$, only give one-way implications"}

$$(\forall X\, P(X)) \vee (\forall X\, Q(X)) \implies \forall X\,(P(X)\vee Q(X)),$$
$$\exists X\,(P(X)\wedge Q(X)) \implies (\exists X\, P(X)) \wedge (\exists X\, Q(X)),$$
but neither converse holds in general – e.g. every integer is even or odd ($\forall X$, $\mathrm{even}(X)\vee\mathrm{odd}(X)$), yet it is false that every integer is even, or every integer is odd.

:::

::: {#def-scope-of-a-quantified-variable .definition name="Scope of a quantified variable"}

The sub-expression from the quantifier to the end of its innermost enclosing parentheses (or the end of the whole expression, if unparenthesized).

:::

::: {#exm-two-disjoint-scopes-same-variable .example name="Two disjoint scopes, same variable name"}

In $(\forall X\, P(X)) \wedge (\forall X\, Q(X))$, the two $X$’s are entirely independent – like distinct local variables in a program that happen to share a name.

:::

#### At least / at most / exactly $n$ (predicate logic).

At least $n$:
$$\exists x_1\cdots x_n\Big(\bigwedge_{i<j}x_i\neq x_j \wedge \bigwedge_i P(x_i)\Big)$$
At most $n$:
$$\forall x_1\cdots x_{n+1}\Big(\bigwedge_i P(x_i)\Rightarrow \bigvee_{i<j}x_i=x_j\Big)$$
Exactly $n$: conjunction of both.

#### The uniqueness quantifier $\exists!$.

$\exists!\,x\,P(x)$
means “there is a unique $x$ such that $P(x)$.” Without “$!$”:
$$\exists!\,x\,P(x) \;\equiv\; \exists x\,\Big(P(x)\wedge\forall z\big(P(z)\Rightarrow z=x\big)\Big)$$
General template for “exactly one thing satisfies $P$”:
existence ($P(x)$) $\wedge$ uniqueness (anything satisfying $P$
equals $x$). *(CN Ch.5 Problem 4.)*

## Duality between quantifiers

::: {#thm-de-morgan-s-laws-for-2 .theorem name="De Morgan's laws for quantifiers"}

$$\neg\forall X\, P(X) \ \equiv\ \exists X\,\neg P(X), \qquad \neg\exists X\, P(X) \ \equiv\ \forall X\,\neg P(X).$$

:::

::: {#exm-not-all-stars-are-visible .example name="“Not all stars are visible” $=$ “some star is invisible”"}

$$\begin{aligned}
\neg\forall X\,(\mathrm{star}(X)\implies\mathrm{visible}(X))
&= \exists X\,\neg(\mathrm{star}(X)\implies\mathrm{visible}(X)) \\
&= \exists X\,\neg(\neg\mathrm{star}(X)\vee\mathrm{visible}(X)) \\
&= \exists X\,(\mathrm{star}(X)\wedge\neg\mathrm{visible}(X)).
\end{aligned}$$

:::

::: {.remark}

$\neg\forall Y\,\neg = \exists Y$, and $\neg\exists Y\,\neg = \forall Y$ (apply the laws twice, using double negation).

:::

## Some examples

::: {#exm-infinitely-many-primes-in-predicate .example name="“Infinitely many primes”, in predicate logic"}

With $\mathrm{Prime}(n)$ on domain $\mathbb{N}$ and predicate $\le$:
$$\forall b\, \exists n\ \mathrm{Prime}(n) \wedge \neg(n \le b).$$
Read: for every bound $b$, some prime exceeds it – correctly capturing “infinitely many primes” without needing an infinite conjunction.

:::

::: {#exm-swapping-the-quantifiers-gives-a .example name="Swapping the quantifiers gives a different, false, statement"}

$$\exists n\, \forall b\ \mathrm{Prime}(n) \wedge \neg(n \le b).$$

:::

::: {.proof name="Why this is false – step by step"}

Distribute $\forall b$ over the conjunction (@sec-math-discrete-logic-predicate-logic-with-quantifiers):
$$\forall b\ \mathrm{Prime}(n) \wedge \neg(n\le b) \ \equiv\ (\forall b\, \mathrm{Prime}(n)) \wedge (\forall b\, \neg(n\le b)).$$

Since $\mathrm{Prime}(n)$ does not involve $b$, the quantifier is superfluous (@sec-math-discrete-logic-predicate-quantifiers):
$$\forall b\, \mathrm{Prime}(n) \ \equiv\ \mathrm{Prime}(n).$$

Substituting back:
$$\exists n\,\big(\mathrm{Prime}(n) \wedge \forall b\,\neg(n\le b)\big) \ \equiv\ \exists n\in\{\text{primes}\}\ \forall b\ n>b.$$

This asserts a single prime exceeding *every* number – false. So the two quantifier orderings genuinely differ in meaning, one true and one false.

:::

::: {#exm-translating-a-nested-quantifier-english .example name="Translating a nested-quantifier English sentence"}

“Every real number except $0$ has a multiplicative inverse.” With $\mathrm{domain}=\mathbb{R}$:
$$\forall x\,\big(x\neq 0 \implies \exists y\, (xy=1)\big).$$
Note the restricted-$\forall$ pattern from @sec-math-discrete-logic-predicate-quantifiers ($x\neq0 \implies \cdots$) nested with a plain $\exists y$ inside – $y$’s existence is allowed to depend on $x$, which is essential: no single $y$ works for every nonzero $x$.

:::

## Summary of rules for logic with quantifiers

::: {.remark name="Full rule list"}

$$\begin{aligned}
\exists x\in A\, P(x) &\equiv \exists x\,(x\in A \wedge P(x)) & \text{(@sec-math-discrete-logic-predicate-quantifiers)}\\
\forall x\in A\, P(x) &\equiv \forall x\,(x\in A \implies P(x)) & \text{(@sec-math-discrete-logic-predicate-quantifiers)}\\
\exists x\, R &\equiv R, \quad \forall x\, R \equiv R & (x \text{ not free in } R;\ @sec-math-discrete-logic-predicate-quantifiers,5.9)\\
\exists x\exists y\, P(x,y) &\equiv \exists y\exists x\, P(x,y) & \text{(@sec-math-discrete-logic-predicate-multiple-quantifiers)}\\
\forall x\forall y\, P(x,y) &\equiv \forall y\forall x\, P(x,y) & \text{(@sec-math-discrete-logic-predicate-multiple-quantifiers)}\\
\forall x\, P(x) &\implies P(\mathrm{obj}), \quad P(\mathrm{obj}) \implies \exists x\, P(x) & \text{(@sec-math-discrete-logic-predicate-logic-with-quantifiers)}\\
\exists x\,(P(x)\vee Q(x)) &\equiv (\exists x\,P(x))\vee(\exists x\,Q(x)) & \text{(@sec-math-discrete-logic-predicate-logic-with-quantifiers)}\\
\forall x\,(P(x)\wedge Q(x)) &\equiv (\forall x\,P(x))\wedge(\forall x\,Q(x)) & \text{(@sec-math-discrete-logic-predicate-logic-with-quantifiers)}\\
\neg\exists x\, P(x) &\equiv \forall x\,\neg P(x), \quad \neg\forall x\, P(x) \equiv \exists x\,\neg P(x) & \text{(@sec-math-discrete-logic-predicate-logic-with-quantifiers)}
\end{aligned}$$

:::
