---
title: "Graph Isomorphism"
sources: [mcs-11.4]
requires: [math/discrete/graph/degree]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Section 11.4, in our own wording; proofs written out in steps. -->

::: {#def-graph-isomorphism .definition name="Isomorphism"}

Graphs $G_1=(V_1,E_1)$ and $G_2=(V_2,E_2)$ are *isomorphic*, written $G_1\cong G_2$, if there is a bijection $f:V_1\to V_2$ such that for all $u,v\in V_1$,
$$\{u,v\}\in E_1\iff\{f(u),f(v)\}\in E_2.$$
Such an $f$ is an *isomorphism*. Isomorphic graphs are the same graph with the vertices renamed.

:::

Isomorphism is an equivalence relation on graphs: the identity is an isomorphism, the inverse of an isomorphism is one, and so is a composition of two.

::: {#prp-isomorphism-invariants .proposition name="What an isomorphism preserves"}

If $f:G_1\to G_2$ is an isomorphism, then:

1. $G_1$ and $G_2$ have the same numbers of vertices and of edges;
2. $\deg f(v)=\deg v$ for every vertex $v$, so the two graphs have the same degree sequence;
3. $f$ maps walks, paths and cycles of $G_1$ to walks, paths and cycles of the same length in $G_2$; in particular connectedness and the length of a shortest cycle are preserved.

:::

::: {.proof}

1. $f$ is a bijection on vertices, and $\{u,v\}\mapsto\{f(u),f(v)\}$ is a bijection from $E_1$ to $E_2$ by the definition.

2. The neighbours of $v$ are mapped bijectively onto the neighbours of $f(v)$, by the same definition.

3. Consecutive vertices of a walk are adjacent, so their images are adjacent; distinct vertices have distinct images because $f$ is injective. Applying the same to $f^{-1}$ shows that nothing new appears in $G_2$.

:::

::: {#exm-isomorphism-same-degrees .example name="Same degrees, not isomorphic"}

Let $G_1$ be a cycle on $6$ vertices and $G_2$ two disjoint triangles. Both have $6$ vertices, $6$ edges, and every vertex has degree $2$. But $G_1$ is connected and $G_2$ is not; also $G_2$ has a cycle of length $3$ and $G_1$ does not. So $G_1\not\cong G_2$.

:::

::: {#rmk-isomorphism-hard .remark name="Testing isomorphism"}

To show that two graphs are isomorphic, exhibit a bijection and check the edges. To show that they are not, find a property preserved by isomorphism (an *invariant*) on which they differ. Checking all $n!$ bijections is hopeless for large $n$; no polynomial-time algorithm for graph isomorphism is known, although it is believed not to be among the hardest problems in NP.

:::
