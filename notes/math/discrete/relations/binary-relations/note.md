---
title: "Binary relations"
sources: [fit1058-cn-2.13]
requires: [math/discrete/functions/inverse-functions, math/discrete/functions/special-functions, math/discrete/relations/combining]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Binary relations. -->

::: {#def-binary-relation .definition name="Binary relation"}

A *binary relation* from $A$ to $B$ is a subset $R \subseteq A \times B$. We write $x R y$, $R(x,y)$, or $(x,y) \in R$ interchangeably. A relation *on* $A$ satisfies $R \subseteq A \times A$.

:::

::: {.remark name="Relations as “relaxed functions”"}

A function $f: A \to B$ is exactly a relation $R \subseteq A \times B$ satisfying: for every $a \in A$, there is a *unique* $b \in B$ with $(a,b) \in R$. Dropping the uniqueness (and even the existence) requirement gives a general binary relation – so every function is a relation, but not conversely.

:::

::: {#def-domain-range-codomain-of-a .definition name="Domain, range/codomain of a relation"}

For $R \subseteq A \times B$:
$$\{x \in A : (x,y) \in R \text{ for some } y \in B\} \quad \text{(elements actually related to something)},$$
$$\{y \in B : (x,y) \in R \text{ for some } x \in A\} \quad \text{(elements actually related to)}.$$

:::

::: {#def-cn-notation .definition name="$R(x)$, $R^{-1}(y)$ – CN notation"}

For $x \in A$: $R(x) = \{y \in B : xRy\}$ (a *set*, possibly empty – not a single value, unlike function notation). For $y \in B$: $R^{-1}(y) = \{x \in A : xRy\}$.

:::

::: {#def-inverse-relation .definition name="Inverse relation"}

For $R \subseteq A \times B$, the *inverse relation* $R^{-1} \subseteq B \times A$ is
$$y R^{-1} x \iff x R y.$$

:::

::: {.remark}

When $R$ happens to be a function, this agrees with the inverse function of @sec-math-discrete-functions-inverse-functions – *but only when that function is a bijection*. For a general function $f$, $f^{-1}$ as a *relation* always exists (just reverse the pairs); it is only a *function* in its own right when $f$ is bijective.

:::

::: {#def-zero-one-matrix-of-a .definition name="Zero-one matrix of a relation"}

For finite $A=\{a_1,\dots,a_m\}$, $B=\{b_1,\dots,b_n\}$ and $R\subseteq A\times B$: the matrix $M_R$ is $m\times n$ with
$$(M_R)_{ij} = 1 \iff (a_i,b_j)\in R, \qquad (M_R)_{ij}=0 \text{ otherwise.}$$

:::

::: {.remark name="Properties as matrix conditions, $R$ on $A$"}

Reflexive: diagonal all $1$s. Symmetric: $M_R = M_R^t$. Antisymmetric: $(M_R)_{ij}=1$ and $i\neq j$ $\implies (M_R)_{ji}=0$.

:::

::: {#def-directed-graph-of-a-relation .definition name="Directed graph of a relation"}

For $R$ on $A$: vertices $=A$; a directed edge $a\to b$ exactly when $(a,b)\in R$.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[node distance=2.5cm, every node/.style={draw,circle,inner sep=2pt,minimum size=7mm}, >={Stealth[length=2mm]}]
\node (a) at (0,0) {$a$};
\node (b) at (2.5,0) {$b$};
\node (c) at (1.25,2) {$c$};
\draw[->] (a) -- (b);
\draw[->] (b) -- (c);
\draw[->] (a) to[bend left] (c);
\draw[->] (a) to[out=150,in=210,looseness=8] (a);
\end{tikzpicture}
\end{center}
```

Directed graph of $R=\{(a,a),(a,b),(a,c),(b,c)\}$ – the loop at $a$ shows reflexivity there

::: {.remark name="Properties as graph conditions"}

Reflexive: a loop at every vertex. Symmetric: every edge $a\to b$ has a matching edge $b\to a$. Transitive: whenever $a\to b\to c$, also $a\to c$ directly.

:::

::: {.remark name="Boolean matrix product computes composition"}

If $M_R$, $M_S$ are zero-one matrices of $R\subseteq A\times B$, $S\subseteq B\times C$, then $M_R\odot M_S = M_{S\circ R}$ (Boolean product, @sec-math-discrete-functions-special-functions) – so relation composition (@sec-math-discrete-relations-combining) reduces to matrix multiplication with $\vee,\wedge$ in place of $+,\times$.

:::
