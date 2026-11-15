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

::: {#rmk-equivalence-relations-1 .remark name="Why not antisymmetric too?"}

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

::: {#rmk-equivalence-relations-2 .remark}

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

::: {#fig-equivalence-relations-1}

```{=latex}
\begin{tikzpicture}
  \draw[regionA] (0,0) rectangle (1.6,3);
  \draw[regionB] (1.9,0) rectangle (3.5,3);
  \draw[regionC] (3.8,0) rectangle (5.4,3);
  \foreach \x/\c in {0.8/0, 2.7/1, 4.6/2} {
    \foreach \k in {0,1,2} {
      \pgfmathtruncatemacro{\v}{\c+3*\k}
      \node at (\x, 2.4-0.9*\k) {$\v$};
    }
    \node[below] at (\x,0) {$[\c]$};
  }
\end{tikzpicture}
```

Congruence modulo $3$ on $\{0,1,\dots,8\}$: the equivalence classes $[0]$, $[1]$, $[2]$ partition the set

:::
