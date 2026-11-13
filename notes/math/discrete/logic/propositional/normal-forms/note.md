---
title: "Normal Forms"
sources: [fit1058-cn-4.16, fit1058-cn-4.17]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: Disjunctive Normal Form; Conjunctive Normal Form. -->

## Disjunctive Normal Form

::: {#def-literal .definition name="Literal"}

A logical variable, unnegated or negated once ($X$ or $\neg X$).

:::

::: {#def-dnf .definition name="DNF"}

A disjunction of conjunctions of literals.

:::

::: {.remark name="Constructing DNF from a truth table"}

For each row where the expression is $T$: form the conjunction of literals matching that row ($X$ if $X=T$ in that row, $\neg X$ if $X=F$); disjoin all such conjunctions.

:::

::: {#exm-majority-function-of-3-variables .example name="Majority function of 3 variables"}

$\mathrm{Maj}(X,Y,Z)$ is true iff at least two of $X,Y,Z$ are true.
$$\begin{array}{ccc|c}
X&Y&Z&\mathrm{Maj}\\\hline
F&F&F&F\\ F&F&T&F\\ F&T&F&F\\ F&T&T&T\\
T&F&F&F\\ T&F&T&T\\ T&T&F&T\\ T&T&T&T
\end{array}$$
DNF (four true rows):
$$\mathrm{Maj}(X,Y,Z) = (\neg X\wedge Y\wedge Z)\vee(X\wedge\neg Y\wedge Z)\vee(X\wedge Y\wedge \neg Z)\vee(X\wedge Y\wedge Z).$$

:::

::: {.remark name="Cost of DNF"}

Every expression has an equivalent DNF, but the number of parts can be as large as $2^k$ for $k$ variables – exponential blow-up. DNF makes *satisfiability* easy to certify (any one part gives a satisfying assignment) but gives no efficient way to certify a *tautology*.

:::

## Conjunctive Normal Form

::: {#def-cnf .definition name="CNF"}

A conjunction of *clauses*, each a disjunction of literals.

:::

::: {.remark name="Duality with DNF, via De Morgan's"}

If $P$ is in CNF, $\neg P$ – negation of a conjunction of disjunctions – becomes, via repeated De Morgan’s and double negation, a disjunction of conjunctions of literals: DNF. So CNF and DNF are dual representations.

:::

::: {.remark name="Converting truth table $\to$ CNF"}

Negate the output column; build DNF for $\neg P$; negate that expression; apply De Morgan’s to push the negation inward into CNF form.

:::
