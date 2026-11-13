---
title: "Laws of Boolean Algebra"
sources: [fit1058-cn-4.14, fit1058-cn-4.15]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: Distributive Laws; Laws of Boolean algebra. -->

## Distributive Laws

::: {#thm-distributive-laws .theorem name="Distributive laws"}

$$P \wedge (Q\vee R) = (P\wedge Q)\vee(P\wedge R), \qquad P \vee (Q\wedge R) = (P\vee Q)\wedge(P\vee R).$$

:::

::: {#prp-absorption-laws .proposition name="Absorption laws"}

$$P \vee (P\wedge Q) = P, \qquad P \wedge (P\vee Q) = P.$$

:::

::: {.proof}

$$\begin{aligned}
P \vee (P\wedge Q) &= (P\wedge T)\vee(P\wedge Q) && \text{(identity: $P = P\wedge T$)}\\
&= P \wedge (T \vee Q) && \text{(distributive law)}\\
&= P \wedge T && \text{(domination: $T\vee Q=T$)}\\
&= P.
\end{aligned}$$
The second identity is the dual (swap $\wedge \leftrightarrow \vee$, $T \leftrightarrow F$ throughout).

:::

## Laws of Boolean algebra

::: {.remark name="Full table, dual pairs"}

$$\neg\neg P = P$$
$$\neg T = F, \quad \neg F = T$$
$$P\wedge Q = Q\wedge P, \qquad P\vee Q = Q\vee P \quad \text{(commutative)}$$
$$(P\wedge Q)\wedge R = P\wedge(Q\wedge R), \qquad (P\vee Q)\vee R = P\vee(Q\vee R) \quad \text{(associative)}$$
$$P\wedge P = P, \qquad P\vee P = P \quad \text{(idempotent)}$$
$$P\wedge\neg P = F, \qquad P\vee\neg P = T \quad \text{(complement)}$$
$$P\wedge T = P, \qquad P\vee F = P \quad \text{(identity)}$$
$$P\wedge F = F, \qquad P\vee T = T \quad \text{(domination)}$$
$$P\wedge(Q\vee R)=(P\wedge Q)\vee(P\wedge R), \qquad P\vee(Q\wedge R)=(P\vee Q)\wedge(P\vee R) \quad \text{(distributive)}$$
$$\neg(P\vee Q)=\neg P\wedge\neg Q, \qquad \neg(P\wedge Q)=\neg P\vee\neg Q \quad \text{(De Morgan's)}$$

:::

::: {#exm-algebraic-proof .example name="Algebraic proof"}

Show $\neg(P\implies Q) \equiv P \wedge \neg Q$.
$$\begin{aligned}
\neg(P\implies Q) &= \neg(\neg P \vee Q) \\
&= \neg\neg P \wedge \neg Q && \text{(De Morgan's)}\\
&= P \wedge \neg Q && \text{(double negation)}.
\end{aligned}$$

:::
