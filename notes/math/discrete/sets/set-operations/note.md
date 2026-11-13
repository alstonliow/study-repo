---
title: "Complement, Difference, Union and Intersection"
sources: [fit1058-cn-1.11, fit1058-cn-1.12]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Complement and set difference; Union and intersection. -->

## Complement and set difference

::: {#def-set-difference-complement-w-r .definition name="Set difference, complement w.r.t.\ $U$"}

$$A - B = \{x : x \in A \wedge x \notin B\}, \qquad
\overline{A} = U - A.$$

:::

::: venndiagram2sets
:::

$A\setminus B$ (shaded)

::: {#thm-de-morgan-s-laws .theorem name="De Morgan's laws"}

$$\overline{A \cup B} = \overline{A} \cap \overline{B}, \qquad
\overline{A \cap B} = \overline{A} \cup \overline{B}.$$

:::

::: {#exm-set-operations-1 .example}

Prove $\overline{A \cap B} = \overline{A} \cup \overline{B}$ using set-builder notation and logical equivalences.
$$\begin{aligned}
\overline{A \cap B} &= \{x : x \notin A \cap B\} \\
&= \{x : \neg(x \in A \cap B)\} \\
&= \{x : \neg(x \in A \wedge x \in B)\} \\
&= \{x : \neg(x \in A) \vee \neg(x \in B)\} &&\text{(De Morgan's law, logic)}\\
&= \{x : x \notin A \vee x \notin B\} \\
&= \{x : x \in \overline{A} \vee x \in \overline{B}\} \\
&= \overline{A} \cup \overline{B}.
\end{aligned}$$

:::

::: {#exm-set-operations-2 .example}

Let $A,B,C$ be sets. Prove $\overline{A \cup (B \cap C)} = (\overline{C} \cup \overline{B}) \cap \overline{A}$ by chaining previously established identities.
$$\begin{aligned}
\overline{A \cup (B \cap C)} &= \overline{A} \cap \overline{(B \cap C)} &&\text{(1st De Morgan's law)}\\
&= \overline{A} \cap (\overline{B} \cup \overline{C}) &&\text{(2nd De Morgan's law)}\\
&= (\overline{B} \cup \overline{C}) \cap \overline{A} &&\text{(commutativity of $\cap$)}\\
&= (\overline{C} \cup \overline{B}) \cap \overline{A}. &&\text{(commutativity of $\cup$)}
\end{aligned}$$

:::

## Union and intersection

::: {#def-union-intersection .definition name="Union, intersection"}

$$A \cup B = \{x : x \in A \vee x \in B\}, \qquad
A \cap B = \{x : x \in A \wedge x \in B\}.$$

:::

::: venndiagram2sets
:::

::: venndiagram2sets
:::

$A\cup B$ (shaded) $A\cap B$ (shaded)

::: {#def-disjoint .definition name="Disjoint"}

$A \cap B = \emptyset$.

:::

::: {#thm-inclusion-exclusion-2 .theorem name="Inclusion–exclusion"}

$|A \cup B| = |A| + |B| - |A \cap B|$.

:::

::: {#exm-set-operations-1-2 .example}

Prove $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ by the element argument.

($\subseteq$) Let $x \in A \cap (B\cup C)$. Then $x \in A$ and ($x \in B$ or $x \in C$). If $x \in B$ then $x \in A\cap B$; if $x \in C$ then $x \in A\cap C$. Either way $x \in (A\cap B)\cup(A\cap C)$.

($\supseteq$) Let $x \in (A\cap B)\cup(A\cap C)$. Then $x \in A\cap B$ or $x \in A\cap C$; either way $x \in A$ and ($x \in B$ or $x \in C$), so $x \in A \cap (B\cup C)$.

Both directions hold, so the sets are equal.

:::

::: {.remark name="Methods for proving set identities"}

(i) *Element argument (double inclusion)*: show LHS $\subseteq$ RHS and RHS $\subseteq$ LHS, as above.

(ii) *Membership table*: tabulate membership ($0/1$) of an arbitrary $x$ in each named set for every combination, and compare the LHS/RHS columns.

(iii) *Using established identities*: rewrite one side into the other via a chain of already-proven identities (the Set Identities table), analogous to proving logical equivalences.

:::

::: {#def-family-of-sets .definition name="Family of sets"}

A *family of sets* indexed by $I$ is a collection $\{A_i\}_{i \in I}$, one set $A_i$ for each $i \in I$; $I$ is the *index set*.

:::

::: {#def-generalized-union-and-intersection-finite .definition name="Generalized union and intersection, finite"}

$$\bigcup_{i=1}^n A_i = A_1 \cup A_2 \cup \cdots \cup A_n = \{x : \exists i \in \{1,\dots,n\},\ x\in A_i\},$$
$$\bigcap_{i=1}^n A_i = A_1 \cap A_2 \cap \cdots \cap A_n = \{x : \forall i \in \{1,\dots,n\},\ x\in A_i\}.$$

:::

::: {#def-generalized-union-and-intersection-arbitrary .definition name="Generalized union and intersection, arbitrary index set"}

For a family $\{A_i\}_{i\in I}$,
$$\bigcup_{i \in I} A_i = \{x : \exists i \in I,\ x \in A_i\}, \qquad
\bigcap_{i \in I} A_i = \{x : \forall i \in I,\ x \in A_i\}.$$
When $I = \mathbb{Z}^+$ one also writes $\displaystyle\bigcup_{i=1}^{\infty} A_i$, $\displaystyle\bigcap_{i=1}^{\infty} A_i$.

:::

::: {#thm-set-identities .theorem name="Set identities"}

For sets $A,B,C$ with universal set $U$:
$$\begin{aligned}
A \cup \emptyset = A,\quad A \cap U = A &\quad\text{(Identity laws)}\\
A \cup U = U,\quad A \cap \emptyset = \emptyset &\quad\text{(Domination laws)}\\
A \cup A = A,\quad A \cap A = A &\quad\text{(Idempotent laws)}\\
\overline{\overline{A}} = A &\quad\text{(Complementation law)}\\
A \cup B = B \cup A,\quad A \cap B = B \cap A &\quad\text{(Commutative laws)}\\
(A\cup B)\cup C = A\cup(B\cup C),\ (A\cap B)\cap C = A\cap(B\cap C) &\quad\text{(Associative laws)}\\
A\cup(B\cap C) = (A\cup B)\cap(A\cup C) &\quad\text{(Distributive law)}\\
A\cap(B\cup C) = (A\cap B)\cup(A\cap C) &\quad\text{(Distributive law)}\\
\overline{A\cup B} = \overline A\cap\overline B,\quad \overline{A\cap B}=\overline A\cup\overline B &\quad\text{(De Morgan's laws)}\\
A\cup(A\cap B) = A,\quad A\cap(A\cup B)=A &\quad\text{(Absorption laws)}\\
A \cup \overline A = U,\quad A \cap \overline A = \emptyset &\quad\text{(Complement laws)}
\end{aligned}$$

:::

::: {#def-bit-string-representation .definition name="Bit-string representation"}

For finite $U = \{a_1,\dots,a_n\}$ with a fixed ordering, $A \subseteq U$ corresponds to the bit string $b_1b_2\cdots b_n$ where $b_i = 1$ iff $a_i \in A$. Then $A\cup B \leftrightarrow$ bitwise OR, $A\cap B \leftrightarrow$ bitwise AND, $\overline{A} \leftrightarrow$ bitwise NOT.

:::
