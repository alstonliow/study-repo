---
title: "Equivalence relations"
sources: [fit1058-cn-2.16]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Equivalence relations. -->

::: {#def-equivalence-relation .definition name="Equivalence relation"}

$R$ on $A$ is an *equivalence relation* iff $R$ is reflexive, symmetric, and transitive.

:::

::: {.remark name="Why not antisymmetric too?"}

Equality is reflexive, symmetric, *and* antisymmetric. But requiring antisymmetry of a general equivalence relation would force $xRy \wedge yRx \implies x=y$ – collapsing “equivalent” into “identical,” which defeats the purpose of a looser notion of sameness.

:::

::: {#exm-equivalence-relations-1 .example}

- Congruence modulo $m$: $x \equiv y \pmod{m} \iff m \mid (x-y)$.

- For any $f: A \to B$: $x \sim_f y \iff f(x)=f(y)$ defines an equivalence relation on $A$.

- The transitive closure of any reflexive, symmetric relation is an equivalence relation.

- For any relation $R$: $R \circ R^{-1}$ and $R^{-1} \circ R$ are equivalence relations.

:::

::: {#def-equivalence-class .definition name="Equivalence class"}

For equivalence relation $R$ on $A$, an *equivalence class* is a nonempty $X \subseteq A$ such that:
$$\text{(i) } \forall x,y \in X,\ xRy; \qquad \text{(ii) } \nexists x \in X, z \notin X \text{ such that } xRz.$$
Equivalently, $X$ is a *maximal* subset of $A$ on which $R$ holds between every pair.

:::

::: {.remark}

For $x \in A$, the equivalence class containing $x$ is $[x]_R = \{y \in A : xRy\}$.

:::

::: {#thm-equivalence-relations-1 .theorem}

The equivalence classes of an equivalence relation $R$ on $A$ form a partition of $A$.

:::

::: {.proof}

**(a) Every $x \in A$ lies in some equivalence class.** Let $X = \{y \in A : xRy\} = [x]_R$.

- *$X$ satisfies (i)*: for $y,z \in X$, $xRy$ and $xRz$; by symmetry $yRx$, and with $xRz$ and transitivity, $yRz$.

- *$X$ satisfies (ii)*: suppose $v \in X$, $w \notin X$, $vRw$. Since $v \in X$: $xRv$; combined with $vRw$ and transitivity, $xRw$, so $w \in X$ – contradiction. So no such $v,w$ exist.

- $x \in X$ by reflexivity ($xRx$).

So $X$ is an equivalence class containing $x$.

**(b) Distinct equivalence classes are disjoint.** Suppose $X,Y$ are equivalence classes with $X \cap Y \neq \emptyset$; let $x \in X \cap Y$. We show $X = Y$ by showing $Y \setminus X = \emptyset$ and $X \setminus Y = \emptyset$.

If $y \in Y \setminus X$: since $X$ is an equivalence class and $y \notin X$, $(x,y) \notin R$ (property (ii) for $X$, using $x \in X$). But $x,y \in Y$, and $Y$ is an equivalence class, so property (i) forces $(x,y) \in R$ – contradiction. So $Y \setminus X = \emptyset$; symmetrically $X \setminus Y = \emptyset$. Hence $X = Y$.

So every element of $A$ lies in exactly one equivalence class – the classes are nonempty (by definition), pairwise disjoint (part (b)), and cover $A$ (part (a)): a partition.

:::
