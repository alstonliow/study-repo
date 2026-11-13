---
title: "Combining binary relations"
sources: [fit1058-cn-2.15]
requires: [math/discrete/functions/composition]
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Combining binary relations. -->

::: {#def-union-and-intersection-of-relations .definition name="Union and intersection of relations"}

For $R,S \subseteq A \times B$:
$$R \cup S = \{(x,y) : xRy \text{ or } xSy\}, \qquad
R \cap S = \{(x,y) : xRy \text{ and } xSy\}.$$

:::

::: {#def-composition-of-relations .definition name="Composition of relations"}

For $R \subseteq A \times B$ and $S \subseteq B \times C$, the *composition* $S \circ R \subseteq A \times C$ is
$$S \circ R = \{(x,z) : \exists y \in B \text{ such that } xRy \text{ and } ySz\}.$$

:::

::: {.remark}

When $R,S$ happen to be functions, this is exactly function composition (@sec-math-discrete-functions-composition). Relation composition generalizes it: no uniqueness of the intermediate $y$ is required, and there may be several, or none.

:::

::: {#prp-composing-with-its-inverse .proposition name="Composing $R$ with its inverse"}

For $R \subseteq A \times B$:
$$(x,z) \in R^{-1} \circ R \iff \exists y \in B \text{ such that } xRy \text{ and } zRy.$$

:::

::: {.proof}

$$(x,z) \in R^{-1}\circ R \iff \exists y,\ xRy \wedge yR^{-1}z \iff \exists y,\ xRy \wedge zRy$$
using the defining property $yR^{-1}z \iff zRy$.

:::

::: {.remark}

So $R^{-1}\circ R$ relates $x,z \in A$ exactly when they share a common $R$-image in $B$; symmetrically, $R \circ R^{-1}$ relates elements of $B$ that share a common preimage in $A$.

:::

::: {#def-iterated-composition-of-a-relation .definition name="Iterated composition of a relation with itself"}

For $R$ on $A$ and $n \in \mathbb{Z}^+$:
$$R^{(n)} = \underbrace{R \circ R \circ \cdots \circ R}_{n \text{ copies}}.$$

:::

::: {#exm-six-degrees-of-separation .example name="“Six degrees of separation”"}

For the relation $\mathrm{knows}$ on the set of all people, $\mathrm{knows}^{(2)}$ relates two people with a mutual acquaintance; $\mathrm{knows}^{(6)}$ is (under this popular hypothesis) the complete relation on all people.

:::

::: {#def-transitive-closure .definition name="Transitive closure"}

The *transitive closure* of $R$ on $A$ is the unique relation $R^+$ on $A$ such that, for all $x,y,z \in A$:

(i) $xRy \implies xR^+y$;

(ii) $xR^+y \wedge yRz \implies xR^+z$;

(iii) $xRy \wedge yR^+z \implies xR^+z$.

:::

::: {.remark}

Condition (i) is essential (it seeds the closure); either (ii) or (iii) alone suffices together with (i) – both are not simultaneously required.

:::

::: {#thm-combining-1 .theorem}

$$R^+ = \bigcup_{i=1}^{\infty} R^{(i)}.$$
$R^+$ is always transitive.

:::

::: {.proof name="Proof sketch"}

Each $R^{(i)}$ is contained in $R^+$: $R^{(1)}=R \subseteq R^+$ by (i), and if $R^{(i)} \subseteq R^+$, then $(x,z)\in R^{(i+1)}$ means $\exists y,\ (x,y)\in R^{(i)} \subseteq R^+$ and $yRz$, so $(x,z) \in R^+$ by (ii); induction gives $R^{(i)}\subseteq R^+$ for all $i$, hence $\bigcup_i R^{(i)} \subseteq R^+$. Conversely, $\bigcup_i R^{(i)}$ satisfies (i)-(iii) itself, and $R^+$ is the *unique* relation satisfying them, so equality follows. Transitivity of $R^+$ is then immediate: any finite chain of $R^+$-steps is absorbed into some $R^{(i)} \subseteq R^+$.

:::

::: {#def-closure-general .definition name="Closure, general"}

The *closure* of $R$ under a property $P$ is the smallest relation $R'\supseteq R$ with property $P$ (if it exists).

:::

::: {#def-reflexive-closure .definition name="Reflexive closure"}

$$r(R) = R \cup \Delta_A, \qquad \Delta_A = \{(a,a):a\in A\} \text{ (the diagonal relation)}.$$

:::

::: {#def-symmetric-closure .definition name="Symmetric closure"}

$$s(R) = R \cup R^{-1}.$$

:::

::: {.remark}

Transitive closure $R^+$ was already defined above: $R^+=\bigcup_{i=1}^\infty R^{(i)}$.

:::
