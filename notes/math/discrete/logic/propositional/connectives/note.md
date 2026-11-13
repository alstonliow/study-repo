---
title: "Negation, Conjunction and Disjunction"
sources: [fit1058-cn-4.5, fit1058-cn-4.6, fit1058-cn-4.7]
requires: [math/discrete/logic/propositional/implication-and-equivalence, math/discrete/sets/set-operations]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: Negation; Conjunction; Disjunction. -->

## Negation

::: {#def-negation .definition name="Negation"}

For proposition $P$, $\neg P$ is true iff $P$ is false.
$$\begin{array}{c|c}
P & \neg P \\ \hline
F & T \\
T & F
\end{array}$$

:::

::: {#prp-double-negation .proposition name="Double negation"}

$$\neg\neg P = P.$$

:::

::: {.remark name="Analogy with set complement"}

Negation mirrors complementation (@sec-math-discrete-sets-set-operations): both give the “completely opposite” outcome, and applying either twice returns the original. If $P$ is the proposition $x \in A$, then $\neg P$ is $x \in \overline{A}$: e.g. $\neg(\sqrt2 \in \mathbb{Q})$ is the same as $\sqrt2 \in \overline{\mathbb{Q}}$ (equivalently $\sqrt2 \notin \mathbb{Q}$).

:::

## Conjunction

::: {#def-conjunction .definition name="Conjunction"}

For propositions $P,Q$: $P \wedge Q$ (“$P$ and $Q$”) is true iff *both* $P$ and $Q$ are true.
$$\begin{array}{cc|c}
P & Q & P \wedge Q \\ \hline
F & F & F \\
F & T & F \\
T & F & F \\
T & T & T
\end{array}$$

:::

::: {.remark name="Analogy with set intersection"}

For object $x$ and sets $A,B$:
$$(x \in A) \wedge (x \in B) \iff x \in A \cap B, \qquad A \cap B = \{x : x\in A \wedge x \in B\}$$
(restating @sec-math-discrete-sets-set-operations’s definition using $\wedge$).

:::

::: {#def-generalized-n-ary-conjunction .definition name="Generalized (n-ary) conjunction"}

For propositions $P_1,\dots,P_n$:
$$P_1 \wedge P_2 \wedge \cdots \wedge P_n$$
is true iff *every* $P_i$ is true.

:::

::: {#exm-translating-english-and .example name="Translating English “and”"}

“You can access the internet from campus only if you are a computer science major or you are not a freshman” involves nested connectives; more simply, “It is below freezing and snowing” translates directly as $P \wedge Q$ for $P=$“it is below freezing”, $Q=$“it is snowing”. Care is needed when English sentences bury an implicit “and” inside a single clause (e.g. “$x$ is between $2$ and $5$” is really $(x>2)\wedge(x<5)$).

:::

## Disjunction

::: {#def-disjunction .definition name="Disjunction"}

For propositions $P,Q$: $P \vee Q$ (“$P$ or $Q$”) is true iff *at least one* of $P,Q$ is true.
$$\begin{array}{cc|c}
P & Q & P \vee Q \\ \hline
F & F & F \\
F & T & T \\
T & F & T \\
T & T & T
\end{array}$$

:::

::: {.remark name="Inclusive, not exclusive"}

This is the *inclusive-or*: true even when *both* $P,Q$ are true. Contrast with *exclusive-or* (@sec-math-discrete-logic-propositional-implication-and-equivalence), true precisely when *exactly one* holds.

:::

::: {#exm-english-or-is-ambiguous .example name="English “or” is ambiguous"}

“Students who have taken CS100 or CS200 may take this class” – inclusive: having taken both still qualifies. “Soup or salad comes with this entree” – exclusive in ordinary restaurant use: you get one, not both, even though the sentence uses the same word “or.” Mathematical $\vee$ always means *inclusive*-or unless stated otherwise; natural language is not reliable here.

:::

::: {.remark name="Analogy with set union"}

For object $x$ and sets $A,B$:
$$(x \in A) \vee (x \in B) \iff x \in A \cup B, \qquad A \cup B = \{x : x\in A \vee x \in B\}$$
(restating @sec-math-discrete-sets-set-operations’s definition using $\vee$).

:::

::: {.remark name="Operator precedence so far"}

Among the connectives introduced up to this point, precedence (highest to lowest) is:
$$\neg \ > \ \wedge \ > \ \vee.$$
So $\neg P \vee Q$ means $(\neg P) \vee Q$, and $P \wedge Q \vee R$ means $(P \wedge Q) \vee R$ – parenthesize explicitly whenever there’s any doubt.

:::
