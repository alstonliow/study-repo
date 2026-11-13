---
title: "Symmetric difference"
sources: [fit1058-cn-1.13]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/01-sets.tex: Symmetric difference. -->

::: {#def-symmetric-difference .definition name="Symmetric difference"}

$A \triangle B = \{x : x \in A \text{ or } x \in B \text{ but not both}\}$ (exclusive or).

:::

::: venndiagram2sets
:::

$A\triangle B$ (shaded)

::: {#prp-equivalent-forms .proposition name="Equivalent forms"}

$$A \triangle B = (A \setminus B) \cup (B \setminus A) = (A \cap \overline{B}) \cup (\overline{A} \cap B) = (A \cup B) \setminus (A \cap B).$$

:::

::: {.remark}

$A \triangle A = \emptyset$, and this is the only case where a symmetric difference is empty.

:::

::: {#prp-symmetric-difference-1 .proposition}

$A = B \iff A \triangle B = \emptyset$.

:::

::: {.proof}

$$A = B \iff A \subseteq B \text{ and } B \subseteq A \iff A\setminus B = \emptyset \text{ and } B\setminus A = \emptyset \iff (A\setminus B)\cup(B\setminus A) = \emptyset \iff A \triangle B = \emptyset.$$

:::

::: {#prp-symmetric-difference-2 .proposition}

$\overline{A \triangle B} = \overline{A} \triangle \overline{B}$.

:::

::: {.proof}

$$\overline{A \triangle B} = \overline{(A \cap \overline{B}) \cup (\overline{A} \cap B)} = \overline{(A \cap \overline{B})} \cap \overline{(\overline{A} \cap B)} = (\overline{A} \cup B) \cap (A \cup \overline{B}).$$
Expanding and simplifying (using distributivity and $A \cap \overline{A} = \emptyset$) gives $(A \cap \overline{B}) \cup (\overline{A} \cap B) = A \triangle B$, so the complement identity holds by the same characterization applied to $\overline{A}, \overline{B}$: $\overline{A}\triangle\overline{B} = (\overline{A}\cap B)\cup(A\cap\overline{B}) = A \triangle B = \overline{A \triangle B}$.

:::
