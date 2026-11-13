---
title: "Representing Logical Statements"
sources: [fit1058-cn-4.18, fit1058-cn-4.19]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: Representing logical statements; Statements about how many variables are true. -->

## Representing logical statements

::: {.remark name="Top-down / bottom-up modelling"}

**Top-down**: identify the top-level conjunction of required conditions. **Bottom-up**: identify the atomic Boolean variables (simplest possible true/false assertions) before worrying about their eventual truth values.

:::

::: {#exm-cnf-from-natural-language-rules .example name="CNF from natural-language rules"}

Variables: one Boolean per guest. Rules:
$$(\text{Harry}\vee\text{Ron}\vee\text{Hermione}\vee\text{Ginny})$$
$$\wedge\ (\neg\text{Hagrid}\vee\text{Norberta})$$
$$\wedge\ (\neg\text{Fred}\vee\text{George}) \wedge (\text{Fred}\vee\neg\text{George})$$
$$\wedge\ (\neg\text{Voldemort}\vee\neg\text{Bellatrix})\wedge(\neg\text{Voldemort}\vee\neg\text{Dolores})\wedge(\neg\text{Bellatrix}\vee\neg\text{Dolores}).$$
“At least one of” $\to$ disjunction; “$A$ only if $B$” $\to$ implication $\to \neg A\vee B$; “none or both” $\to$ biconditional $\to$ two implications; “no more than one of a set” $\to$ conjunction of pairwise “not both” clauses.

:::

## Statements about how many variables are true

::: {#def-at-most-of-variables-true .definition name="At most $k$ of $n$ variables true"}

For variables $x_1,\dots,x_n$:
$$\text{``at most } k \text{ true''} \ \equiv\ \bigwedge_{\substack{S\subseteq\{1,\dots,n\} \\ |S|=k+1}} \ \bigvee_{i\in S} \neg x_i.$$

:::

::: {.proof name="Why this is correct"}

“At most $k$ true” fails iff at least $k+1$ variables are true, i.e. iff some set $S$ of size $k+1$ has *all* its variables true, i.e. iff some $S$ has $\bigvee_{i\in S}\neg x_i$ false. So “at most $k$ true” holds iff *every* size-$(k{+}1)$ set $S$ has $\bigvee_{i\in S}\neg x_i$ true – exactly the conjunction above. There are $\binom{n}{k+1}$ such sets $S$.

:::

::: {#def-at-least-of-variables-true .definition name="At least $k$ of $n$ variables true"}

$$\text{``at least } k \text{ true''} \ \equiv\ \bigwedge_{\substack{S\subseteq\{1,\dots,n\} \\ |S|=n-k+1}} \ \bigvee_{i\in S} x_i.$$

:::

::: {.proof name="Why this is correct"}

“At least $k$ true” fails iff at most $k-1$ are true, iff at least $n-k+1$ are false, iff some set $S$ of size $n-k+1$ has *all* its variables false, iff some $S$ has $\bigvee_{i\in S}x_i$ false. So “at least $k$ true” holds iff every size-$(n{-}k{+}1)$ set $S$ has $\bigvee_{i\in S}x_i$ true. There are $\binom{n}{n-k+1}$ such sets.

:::

::: {#def-exactly .definition name="Exactly $k$"}

$$\text{``exactly } k \text{ true''} \ \equiv\ \text{``at least } k\text{''} \ \wedge\ \text{``at most } k\text{''}.$$

:::
