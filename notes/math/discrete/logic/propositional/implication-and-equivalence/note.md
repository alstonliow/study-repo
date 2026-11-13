---
title: "Implication, Equivalence and Exclusive-or"
sources: [fit1058-cn-4.9, fit1058-cn-4.10, fit1058-cn-4.11]
requires: [math/discrete/sets/subsets, math/discrete/sets/symmetric-difference]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/04-propositional-logic.tex: Implication; Equivalence; Exclusive-or. -->

## Implication

::: {#def-implication .definition name="Implication"}

$P \implies Q$ (“if $P$ then $Q$”) is false only when $P$ is true and $Q$ is false.
$$\begin{array}{cc|c}
P & Q & P \implies Q \\ \hline
F & F & T \\
F & T & T \\
T & F & F \\
T & T & T
\end{array}$$

:::

::: {.remark name="Alternative phrasings"}

$P \implies Q$ reads: “if $P$ then $Q$”; “$P$ only if $Q$”; “$P$ is sufficient for $Q$”; “$Q$ is necessary for $P$”; “$Q$ whenever $P$”.

:::

## Equivalence

::: {#def-equivalence-biconditional .definition name="Equivalence / biconditional"}

$P \iff Q$ is true iff $P,Q$ have the same truth value.
$$\begin{array}{cc|c}
P & Q & P \iff Q \\ \hline
F & F & T \\
F & T & F \\
T & F & F \\
T & T & T
\end{array}$$

:::

::: {#prp-implication-and-equivalence-1 .proposition}

$$P \iff Q \quad \equiv \quad (P \implies Q) \wedge (Q \implies P).$$

:::

::: {.remark name="Alternative phrasing"}

$P \iff Q$ reads: “$P$ if and only if $Q$”; “$P$ is necessary and sufficient for $Q$”.

:::

::: {.remark name="Analogy with set equality"}

$x\in A \iff x\in B$ for all $x$ is exactly $A=B$ (@sec-math-discrete-sets-subsets).

:::

## Exclusive-or

::: {#def-exclusive-or .definition name="Exclusive-or"}

$P \oplus Q$ is true iff exactly one of $P,Q$ is true.
$$\begin{array}{cc|c}
P & Q & P \oplus Q \\ \hline
F & F & F \\
F & T & T \\
T & F & T \\
T & T & F
\end{array}$$

:::

::: {#prp-implication-and-equivalence-1-2 .proposition}

$$P \oplus Q = \neg(P \iff Q).$$

:::

::: {#thm-generalized-xor-parity-cn-thm .theorem name="Generalized XOR parity, CN Thm 24"}

For all $n$ and propositions $P_1,\dots,P_n$: $P_1\oplus\cdots\oplus P_n$ is true iff an *odd* number of the $P_i$ are true.

:::

::: {.proof}

Induction on $n$.

**Base case** ($n=1$): $P_1$ alone is true iff exactly $1$ (odd) of it is true.

**Inductive step**: assume the claim for $k$ propositions. Then
$$P_1\oplus\cdots\oplus P_{k+1} = (P_1\oplus\cdots\oplus P_k) \oplus P_{k+1}.$$
By the inductive hypothesis, the first factor is $T$ iff an odd number of $P_1,\dots,P_k$ are true, else $F$. Checking all four combinations of (that factor, $P_{k+1}$) against $\oplus$’s truth table shows the result is $T$ exactly when the *total* count of true propositions among $P_1,\dots,P_{k+1}$ is odd.

By induction, the claim holds for all $n$.

:::

::: {.remark name="Analogy with symmetric difference"}

$x \in A_1 \triangle \cdots \triangle A_n \iff (x\in A_1)\oplus\cdots\oplus(x\in A_n)$ (@sec-math-discrete-sets-symmetric-difference).

:::
