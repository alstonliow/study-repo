---
title: "Degree"
sources: [fit1058-cn-11.7]
requires: [math/discrete/graph/basic-definitions]
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Degree. -->

::: {#def-degree .definition name="Degree"}

The *degree* of $v$ is $\deg(v) = |N(v)|$, the number of neighbours of $v$. Write $\deg_G(v)$ when the graph needs to be specified.

:::

::: {.remark name="Isolated vertices and leaves"}

In a simple graph, $\deg(v)$ is also the number of edges at $v$. So $v$ is isolated iff $\deg(v)=0$, and a leaf iff $\deg(v)=1$. In the graph of @sec-math-discrete-graph-basic-definitions, $\deg(c)=3$, $\deg(a)=\deg(b)=2$, $\deg(d)=\deg(f)=\deg(g)=1$, $\deg(e)=0$.

:::

::: {#thm-handshake .theorem name="Handshaking lemma"}

For every graph,  $\displaystyle\sum_{v\in V} \deg(v) = 2|E|$.

:::

::: {.proof}

Each edge $\{v,w\}$ contributes exactly $1$ to $\deg(v)$ and $1$ to $\deg(w)$, so $2$ to the sum. Adding over all edges gives $2|E|$.

:::

::: {.proof name="Alternative proof, via the adjacency matrix"}

The number of $1$’s in the column of $v$ is $\deg(v)$, so $\sum_v\deg(v)$ is the total number of $1$’s in $A$. Each edge $\{v,w\}$ gives exactly two of them, $A_{vw}$ and $A_{wv}$, so the total is $2|E|$.

:::

::: {#exm-degree-1 .example}

In the graph of @sec-math-discrete-graph-basic-definitions, the degrees add up to $2+2+3+1+0+1+1=10=2\cdot5$.

:::

::: {#cor-odd-degree .corollary}

In every graph, the number of vertices of odd degree is even.

:::

::: {.proof}

The sum $\sum_v\deg(v)=2|E|$ is even. Split it into the sum over even-degree vertices, which is even, and the sum over odd-degree vertices, which must therefore also be even. A sum of $k$ odd numbers has the same parity as $k$, so $k$ is even.

:::

::: {#cor-avg-degree .corollary name="Average degree"}

A graph with $n$ vertices and $m$ edges has average degree $\dfrac1n\sum_{v}\deg(v) = \dfrac{2m}{n}$.

:::

::: {.proof}

Divide @thm-handshake by $n$.

:::

::: {.remark name="Range of the average"}

Since $0\le\deg(v)\le n-1$, the average degree lies between $0$ (the null graph $\overline{K_n}$) and $n-1$ (the complete graph $K_n$). The formula $2m/n$ uses only the global counts $n$ and $m$, yet tells us about local structure.

:::

::: {.remark name="Directed graphs (extra)"}

For a directed graph, let $\deg^-(v)$ and $\deg^+(v)$ be the in-degree and out-degree of $v$. Each arc $(v,w)$ contributes $1$ to $\deg^+(v)$ and $1$ to $\deg^-(w)$, so $\sum_v\deg^-(v)=\sum_v\deg^+(v)=|E|$.

:::

::: {#thm-equal-degree .theorem name="CN Thm 56"}

In every graph with at least two vertices, there are two vertices with the same degree.

:::

::: {.proof}

Let $G$ have $n\ge2$ vertices. The possible degrees are $0,1,\dots,n-1$, which is $n$ values. We use proof by cases, depending on whether $G$ has a vertex of degree $n-1$.

**Case 1** ($G$ has no vertex of degree $n-1$): Then the degrees lie in $\{0,\dots,n-2\}$, which has only $n-1$ values. With $n$ vertices, two of them must share a degree.

**Case 2** ($G$ has a vertex $v$ of degree $n-1$): Then $v$ is adjacent to every other vertex, so no vertex has degree $0$. The degrees lie in $\{1,\dots,n-1\}$, again only $n-1$ values for $n$ vertices, so two vertices share a degree.

:::

::: {.remark name="The key observation"}

Degrees $0$ and $n-1$ cannot both occur: a vertex of degree $n-1$ is adjacent to everything, and a vertex of degree $0$ to nothing. So the $n$ vertices have at most $n-1$ values available.

:::

::: {.remark name="Necessary conditions on degree lists"}

For $d_1,\dots,d_n$ (with $0\le d_i\le n-1$) to be the degrees of a graph on $n$ vertices, it is necessary that $\sum_i d_i$ is even (@thm-handshake), that the number of odd $d_i$ is even (@cor-odd-degree), and, if $n\ge2$, that the $d_i$ are not all different (@thm-equal-degree). These conditions are not sufficient, as the next example shows.

:::

::: {#exm-degree-2 .example}

The list $3,3,1,1$ passes all three tests, but no graph on $4$ vertices has these degrees: the two vertices of degree $3$ would each be adjacent to all other vertices, so the remaining two vertices would have degree at least $2$, not $1$.

:::
