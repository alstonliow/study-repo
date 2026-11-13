---
title: "Representing Graphs"
sources: [fit1058-cn-11.4, fit1058-cn-11.3]
requires: [math/discrete/functions/special-functions, math/discrete/graph/basic-definitions, math/discrete/relations/binary-relations]
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Representing graphs; Graphs and relations. -->

## Representing graphs

### Edge list

::: {#def-edge-list .definition name="Edge list"}

The *edge list* of $G$ lists the vertex set and every edge $\{v,w\}$ explicitly.

:::

### Adjacency matrix

::: {#def-adjacency-matrix .definition name="Adjacency matrix"}

For $V=\{v_1,\dots,v_n\}$, the *adjacency matrix* is the $n\times n$ matrix $A$ with $A_{ij}=1$ if $v_i\sim v_j$, and $A_{ij}=0$ otherwise.

:::

::: {#exm-representing-graphs-1 .example}

For the graph of @sec-math-discrete-graph-basic-definitions, restricted to $\{a,b,c,d,e\}$ in that order,
$$A =
\begin{pmatrix}
0 & 1 & 1 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 \\
1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}.$$
For instance $a\sim c$ because the entry in row $a$, column $c$ is $1$; the last row is all zero because $e$ is isolated.

:::

::: {.remark name="Shape of the matrix"}

$A$ is symmetric because edges are unordered, and its diagonal is all $0$ because a simple graph has no loops. It is exactly the zero-one matrix of the adjacency relation (@sec-math-discrete-functions-special-functions).

:::

### Adjacency list

::: {#def-adjacency-list .definition name="Adjacency list"}

For each vertex $v$, store the list $N(v)$ of its neighbours. The *adjacency list* of $G$ is the collection of these $n$ lists.

:::

::: {#exm-representing-graphs-2 .example}

The graph of @sec-math-discrete-graph-basic-definitions has adjacency list
$$a: b,c \qquad b: a,c \qquad c: a,b,d \qquad d: c \qquad e: \text{--} \qquad f: g \qquad g: f$$
From it we read off at once that $N(c)=\{a,b,d\}$, that $e$ has no neighbours, and that the leaves are $d,f,g$.

:::

::: {.remark name="Most common in practice"}

The adjacency list is the most widely used representation in computers: it is compact, and it makes searching the neighbourhood of a vertex fast, which many graph algorithms need.

:::

### Incidence matrix

::: {#def-incidence-matrix .definition name="Incidence matrix"}

For $V=\{v_1,\dots,v_n\}$ and $E=\{e_1,\dots,e_m\}$, the *incidence matrix* $M$ is the $n\times m$ matrix with $M_{ij}=1$ if $v_i$ is incident with $e_j$, and $M_{ij}=0$ otherwise.

:::

::: {.remark name="Columns"}

Each column of $M$ contains exactly two $1$’s, one for each endpoint of that edge.

:::

::: {#prp-mmt .proposition name="Incidence matrix and adjacency matrix (extra)"}

Let $G$ be a simple graph with adjacency matrix $A$ and incidence matrix $M$, and let $D=\operatorname{diag}\bigl(\deg(v_1),\dots,\deg(v_n)\bigr)$. Then $MM^{\mathsf T}=A+D$.

:::

::: {.proof}

By the definition of matrix multiplication, $(MM^{\mathsf T})_{ij}=\sum_{k}M_{ik}M_{jk}$ counts the edges incident with both $v_i$ and $v_j$. If $i=j$, this counts the edges at $v_i$, which is $\deg(v_i)=D_{ii}$. If $i\ne j$, the only possible such edge is $\{v_i,v_j\}$, so the count is $1$ if $v_i\sim v_j$ and $0$ otherwise, which is $A_{ij}$.

:::

::: {.remark name="Comparison of representations"}

Up to a constant factor:
$$\begin{array}{l|cccc}
 & \text{edge list} & \text{adjacency list} & \text{adjacency matrix} & \text{incidence matrix}\\\hline
\text{space} & |E| & n+|E| & n^2 & n|E|\\
\text{test } v\sim w & \text{scan list} & \deg(v) & 1 & \text{scan row}\\
\text{list } N(v) & \text{scan list} & \deg(v) & n & \text{scan row}
\end{array}$$
Sparse graphs favour lists; dense graphs, or computations using matrix algebra, favour matrices.

:::

## Graphs and relations

::: {#prp-representing-graphs-1 .proposition}

Simple graphs on $V$ correspond exactly to irreflexive symmetric binary relations on $V$.

:::

::: {.proof}

Given a simple graph $G=(V,E)$, define $R\subseteq V\times V$ by $(v,w)\in R$ iff $\{v,w\}\in E$. Then $R$ is irreflexive, since there are no loops, and symmetric, since $\{v,w\}=\{w,v\}$. Conversely, an irreflexive symmetric $R$ on $V$ gives the simple graph with $E=\{\{v,w\}:(v,w)\in R\}$, and these two constructions undo each other.

:::

::: {.remark name="Dropping the conditions"}

Dropping irreflexivity allows loops; dropping symmetry gives directed graphs. An arbitrary binary relation on $V$ (@sec-math-discrete-relations-binary-relations) is the same thing as a directed graph with loops allowed.

:::
