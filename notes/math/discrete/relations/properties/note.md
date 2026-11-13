---
title: "Properties of binary relations"
sources: [fit1058-cn-2.14]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Properties of binary relations. -->

::: {#def-reflexive .definition name="Reflexive"}

$R$ on $A$ is *reflexive* iff
$$\forall a \in A,\quad (a,a) \in R.$$

:::

::: {#def-irreflexive .definition name="Irreflexive"}

$R$ on $A$ is *irreflexive* iff
$$\forall a \in A,\quad (a,a) \notin R.$$

:::

::: {#def-symmetric .definition name="Symmetric"}

$R$ on $A$ is *symmetric* iff
$$\forall x,y \in A,\quad (x,y) \in R \implies (y,x) \in R.$$

:::

::: {#def-antisymmetric .definition name="Antisymmetric"}

$R$ on $A$ is *antisymmetric* iff
$$\forall x,y \in A,\quad \big[(x,y) \in R \wedge (y,x) \in R\big] \implies x = y.$$

:::

::: {#def-asymmetric .definition name="Asymmetric"}

$R$ on $A$ is *asymmetric* iff
$$\forall x,y \in A,\quad (x,y) \in R \implies (y,x) \notin R.$$

:::

::: {#def-transitive .definition name="Transitive"}

$R$ on $A$ is *transitive* iff
$$\forall x,y,z \in A,\quad \big[(x,y) \in R \wedge (y,z) \in R\big] \implies (x,z) \in R.$$

:::

::: {#exm-properties-1 .example}

On $\mathbb{Z}$: $=,\ \le,\ \ge$ are reflexive; $<,\ >$ are irreflexive. $=$ is symmetric; $<,\le,>,\ge$ are not. $=,\le,\ge$ are antisymmetric. $<,\ >$ are asymmetric. $=,<,\le,>,\ge$ are all transitive; $\neq$ is not.

:::

::: {#prp-properties-1 .proposition}

$$R \text{ asymmetric} \implies R \text{ antisymmetric} \wedge R \text{ irreflexive}.$$
The converse is false.

:::

::: {.proof}

Suppose $R$ is asymmetric. If $(x,y) \in R$ and $(y,x) \in R$ simultaneously held for $x \neq y$, this would contradict asymmetry directly, so antisymmetry holds. If $(a,a) \in R$ for some $a$, then taking $x=y=a$ in the asymmetry condition gives $(a,a) \in R \implies (a,a) \notin R$, a contradiction; so $R$ is irreflexive.

For the converse: $\le$ on $\mathbb{Z}$ is antisymmetric (if $x\le y$ and $y\le x$ then $x=y$) but not irreflexive ($a \le a$ holds for all $a$), hence not asymmetric.

:::

::: {#exm-checking-all-properties-on-a .example name="Checking all properties on a concrete relation"}

Let $A = \{a,b,c,d\}$ and
$$R = \{(a,a),(a,c),(a,d),(b,a),(b,b),(b,c),(b,d),(c,b),(c,c),(d,b),(d,d)\}.$$

- *Reflexive*: yes, since $(a,a),(b,b),(c,c),(d,d) \in R$.

- *Symmetric*: no, since $(a,c) \in R$ but $(c,a) \notin R$.

- *Antisymmetric*: no, since $(b,c),(c,b) \in R$ with $b \neq c$.

- *Transitive*: no, since $(a,c),(c,b) \in R$ but $(a,b) \notin R$.

:::

::: {#prp-properties-under-union-and-intersection .proposition name="Properties under union and intersection"}

Let $R,S$ be relations on $A$.
$$\begin{aligned}
R,S \text{ reflexive} &\implies R\cup S,\ R\cap S \text{ reflexive}, \\
R,S \text{ symmetric} &\implies R\cup S,\ R\cap S \text{ symmetric}, \\
R,S \text{ transitive} &\implies R\cap S \text{ transitive (but not necessarily } R\cup S\text{)}.
\end{aligned}$$

:::

::: {.proof}

*Reflexive:* $R,S$ reflexive $\implies \forall a\in A,\ (a,a)\in R \wedge (a,a)\in S \implies (a,a) \in R\cup S \text{ and } (a,a)\in R\cap S$.

*Symmetric:* If $(x,y) \in R\cup S$, then $(x,y)\in R$ or $(x,y)\in S$; symmetry of the relation containing it gives $(y,x)$ in that same relation, hence $(y,x)\in R\cup S$. If $(x,y)\in R\cap S$, then $(x,y)$ is in both, so by symmetry $(y,x)$ is in both, hence $(y,x)\in R\cap S$.

*Transitive ($\cap$ only):* If $(x,y),(y,z) \in R\cap S$, both pairs lie in $R$, so transitivity of $R$ gives $(x,z)\in R$; both pairs also lie in $S$, so $(x,z)\in S$; hence $(x,z)\in R\cap S$. Union fails in general: a chain $x\to y$ witnessed only by $R$ and $y\to z$ witnessed only by $S$ need not put $(x,z)$ in $R$ or in $S$ individually.

:::
