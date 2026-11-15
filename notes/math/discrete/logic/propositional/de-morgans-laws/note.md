---
title: "De Morgan's Laws"
sources: [fit1058-cn-4.8]
requires: [math/discrete/logic/propositional/connectives, math/discrete/logic/propositional/tautologies, math/discrete/sets/set-operations]
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: De Morgan's Laws. -->

::: {#thm-de-morgan-s-laws-for .theorem name="De Morgan's Laws for propositions"}

$$\neg(P \vee Q) = \neg P \wedge \neg Q, \qquad \neg(P \wedge Q) = \neg P \vee \neg Q.$$

:::

::: {.proof name="Proof of the first law, by truth table"}

$$\begin{array}{cc|c|c|cc|c}
P & Q & P\vee Q & \neg(P\vee Q) & \neg P & \neg Q & \neg P \wedge \neg Q \\ \hline
F & F & F & T & T & T & T \\
F & T & T & F & T & F & F \\
T & F & T & F & F & T & F \\
T & T & T & F & F & F & F
\end{array}$$
The columns for $\neg(P\vee Q)$ and $\neg P \wedge \neg Q$ agree in every row, so the two expressions are *logically equivalent* – true or false together, for every assignment of truth values to $P,Q$.

:::

::: {.remark name="Building the table incrementally"}

The table is constructed left to right, each column using only earlier columns: start with all combinations of $P,Q$; build $P\vee Q$; negate it to get $\neg(P\vee Q)$; separately build $\neg P$ and $\neg Q$; conjoin them to get $\neg P \wedge \neg Q$. Comparing the two target columns (highlighted) completes the proof.

:::

::: {.remark name="Deriving the second law from the first"}

Rather than repeating the truth-table argument, the second law follows from the first by substitution: replace $P,Q$ with $\neg P, \neg Q$ in the first law and simplify using double negation (@sec-math-discrete-logic-propositional-connectives).

:::

::: {#thm-generalized-de-morgan-s-law-2 .theorem name="Generalized De Morgan's law, CN Thm 23"}

For all $n$:
$$\neg(P_1 \vee \cdots \vee P_n) = \neg P_1 \wedge \cdots \wedge \neg P_n.$$

:::

::: {.proof}

$$\begin{aligned}
\text{LHS is true} &\iff P_1 \vee \cdots \vee P_n \text{ is false} \\
&\iff P_1,\dots,P_n \text{ are all false} \\
&\iff \neg P_1,\dots,\neg P_n \text{ are all true} \\
&\iff \text{RHS is true.}
\end{aligned}$$

:::

::: {.remark}

This argument works for *every* $n$ at once – unlike the truth-table method, which would need a separate (and infinite) family of tables, one per $n$.

:::

::: {.remark name="Correspondence with the set-theoretic De Morgan's laws"}

Compare directly with @sec-math-discrete-sets-set-operations’s Theorem (De Morgan’s laws for sets): $\overline{A\cup B} = \overline A \cap \overline B$ and $\overline{A\cap B} = \overline A \cup \overline B$ are exactly the propositional laws above, applied to the propositions $x\in A$ and $x\in B$.

:::

::: {#fig-de-morgans-laws-1}

```{=latex}
\begin{tikzpicture}
  \begin{scope}[xshift=0cm]
    \fill[shade] (-0.4,-1.1) rectangle (3.0,1.1); \fill[white] (0.85,0) circle (0.75); \fill[white] (1.75,0) circle (0.75);
    \draw (-0.4,-1.1) rectangle (3.0,1.1);
    \draw (0.85,0) circle (0.75); \draw (1.75,0) circle (0.75);
    \node at (0.45,0) {$P$}; \node at (2.15,0) {$Q$};
    \node at (1.3,-1.5) {$\neg(P\vee Q)$};
  \end{scope}
  \begin{scope}[xshift=4.4cm]
    \fill[overlapA, even odd rule] (-0.4,-1.1) rectangle (3.0,1.1) (0.85,0) circle (0.75);
    \fill[overlapB, even odd rule] (-0.4,-1.1) rectangle (3.0,1.1) (1.75,0) circle (0.75);
    \draw (-0.4,-1.1) rectangle (3.0,1.1);
    \draw (0.85,0) circle (0.75); \draw (1.75,0) circle (0.75);
    \node at (0.45,0) {$P$}; \node at (2.15,0) {$Q$};
    \node at (1.3,-1.5) {$\neg P\wedge\neg Q$};
  \end{scope}
\end{tikzpicture}
```

Left: $\neg(P\vee Q)$ is the region outside both circles. Right: $\neg P$ (blue) and $\neg Q$ (red) overlap in exactly that region

:::

::: {.remark name="Naming logical equivalence"}

Two compound propositions are *logically equivalent* iff their truth tables are identical in every row – written $P \equiv Q$ or $P \iff Q$ (a *tautology*, true under every assignment; formalized further in @sec-math-discrete-logic-propositional-tautologies).

:::
