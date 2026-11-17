---
title: "Tautologies and Logical Equivalence"
sources: [fit1058-cn-4.12, fit1058-cn-4.13, cs70-1.1]
requires: [math/discrete/logic/propositional/implication-and-equivalence]
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: Tautologies and logical equivalence; History. -->

## Tautologies and logical equivalence

::: {#def-tautology .definition name="Tautology"}

A proposition that is true under every assignment of truth values (every row of its truth table is $T$).

:::

::: {#def-contradiction-propositional .definition name="Contradiction"}

A propositional form that is false for every assignment of truth values is a *contradiction*. $P$ is a contradiction exactly when $\neg P$ is a tautology. For example, $P\wedge\neg P$ is a contradiction.

:::

::: {#rmk-tautologies-excluded-middle .remark name="Law of the excluded middle"}

For every proposition $P$, exactly one of $P$ and $\neg P$ is true. So $P\vee\neg P$ is a tautology and $P\wedge\neg P$ is a contradiction. Proof by contradiction rests on this law (@sec-math-discrete-proof-contradiction).

:::

::: {#def-logical-equivalence .definition name="Logical equivalence"}

$P \equiv Q$ (written $P=Q$) iff their truth tables are identical, iff $P\iff Q$ is a tautology.

:::

::: {#rmk-tautologies-1 .remark name="Key equivalences"}

$$\neg\neg P = P, \qquad \neg(P\vee Q)=\neg P\wedge\neg Q, \qquad \neg(P\wedge Q)=\neg P\vee\neg Q,$$
$$P\implies Q = \neg P \vee Q, \qquad P\iff Q = (P\implies Q)\wedge(Q\implies P),$$
$$P\oplus Q = \neg(P\iff Q) = P \iff \neg Q.$$

:::

::: {#prp-exportation-law .proposition name="Exportation law"}

$$(P \wedge Q) \implies R \ \equiv \ P \implies (Q \implies R).$$

:::

::: {.proof}

Using $X\implies Y = \neg X \vee Y$ repeatedly:
$$\begin{aligned}
(P\wedge Q)\implies R &= \neg(P\wedge Q)\vee R = (\neg P \vee \neg Q)\vee R && \text{(De Morgan's)}\\
&= \neg P \vee (\neg Q \vee R) && \text{(associativity of $\vee$)}\\
&= \neg P \vee (Q \implies R) \\
&= P \implies (Q \implies R).
\end{aligned}$$

:::

## History


