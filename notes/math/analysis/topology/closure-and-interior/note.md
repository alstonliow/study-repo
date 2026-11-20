---
title: "Closed Sets, Closure and Interior"
sources: [camib-at-m2]
requires: [math/analysis/topology/topological-spaces]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Metric and Topological Spaces (Easter 2015 lecture notes), Sections 2.3-2.4, in our own wording; examples ours; proofs written out in steps. -->

Closed sets are the complements of open sets. Every set lies between a largest open subset, its interior, and a smallest closed superset, its closure.

::: {#def-closed-set-topological .definition name="Closed set" generalizes="def-limit-point-metric"}

A subset $C$ of a topological space $X$ is *closed* if $X\setminus C$ is open.

:::

In a metric space this agrees with "contains all its limit points" by @prp-closed-iff-complement-open. Taking complements in @def-topology: $\emptyset$ and $X$ are closed, any intersection of closed sets is closed, and a finite union of closed sets is closed.

::: {#prp-hausdorff-points-closed .proposition name="Points are closed in Hausdorff spaces"}

If $X$ is Hausdorff, every singleton $\{x\}$ is closed.

:::

::: {.proof}

1. For each $y\ne x$ choose disjoint open $U_y\ni x$ and $V_y\ni y$. Then $x\notin V_y$.

2. So $X\setminus\{x\}=\bigcup_{y\ne x}V_y$ is a union of open sets, hence open.

:::

The converse fails: in the cofinite topology on an infinite set, singletons are closed, but any two non-empty open sets meet (their complements are finite and $X$ is infinite), so the space is not Hausdorff.

## Closure

::: {#def-closure .definition name="Closure, dense set"}

The *closure* $\overline A$ of $A\subseteq X$ is the intersection of all closed sets containing $A$. A set $A$ is *dense* in $X$ if $\overline A=X$.

:::

::: {#prp-closure-properties .proposition name="Characterising the closure"}

Let $A\subseteq X$.

1. $\overline A$ is the smallest closed set containing $A$; $A$ is closed if and only if $A=\overline A$.
2. $x\in\overline A$ if and only if every open neighbourhood of $x$ meets $A$.
3. If $a_n\in A$ and $a_n\to x$, then $x\in\overline A$. In a metric space, conversely, every $x\in\overline A$ is the limit of a sequence in $A$.

:::

::: {.proof}

1. $\overline A$ is closed as an intersection of closed sets, contains $A$, and is contained in every closed set containing $A$ by definition. If $A$ is closed it is one of the sets intersected, so $\overline A\subseteq A$.

2. Suppose some open $U\ni x$ misses $A$. Then $X\setminus U$ is closed and contains $A$, so $\overline A\subseteq X\setminus U$ and $x\notin\overline A$. Conversely, if $x\notin\overline A$, then $U=X\setminus\overline A$ is an open neighbourhood of $x$ missing $A$.

3. If $a_n\to x$ and $U\ni x$ is open, then $a_n\in U$ for large $n$, so $U$ meets $A$; by part 2, $x\in\overline A$. In a metric space, if $x\in\overline A$, part 2 applied to $U=B_{1/n}(x)$ gives $a_n\in A$ with $d(a_n,x)<\frac1n$, so $a_n\to x$.

:::

::: {#exm-closure-and-interior-1 .example name="Closures and dense sets"}

1. In $\mathbb R$, $\overline{(0,1)}=[0,1]$, and $\mathbb Q$ is dense: every open interval contains a rational (@thm-archimedean-property). So is $\mathbb R\setminus\mathbb Q$.
2. In a metric space $\overline{B_r(x)}\subseteq\overline B_r(x)$, since the closed ball is closed; equality can fail. In a discrete space $B_1(x)=\{x\}$ is closed, while $\overline B_1(x)=X$.
3. In the cofinite topology on an infinite set, every infinite subset is dense, since the only closed set containing it is $X$.

:::

## Interior

::: {#def-interior .definition name="Interior"}

The *interior* $\operatorname{Int}A$ of $A\subseteq X$ is the union of all open sets contained in $A$.

:::

::: {#prp-interior-properties .proposition name="Interior and closure are dual"}

1. $\operatorname{Int}A$ is the largest open set contained in $A$; $x\in\operatorname{Int}A$ if and only if some open neighbourhood of $x$ lies in $A$.
2. $X\setminus\operatorname{Int}A=\overline{X\setminus A}$.

:::

::: {.proof}

1. The interior is open as a union of open sets and lies in $A$; every open set in $A$ is one of the sets in the union. The pointwise description is the definition of the union.

2. By part 1, $x\notin\operatorname{Int}A$ if and only if no open neighbourhood of $x$ lies in $A$, that is, every open neighbourhood of $x$ meets $X\setminus A$. By @prp-closure-properties this means $x\in\overline{X\setminus A}$.

:::

For example $\operatorname{Int}[0,1]=(0,1)$ in $\mathbb R$, and $\operatorname{Int}\mathbb Q=\emptyset$, matching $\overline{\mathbb R\setminus\mathbb Q}=\mathbb R$. The *boundary* $\partial A=\overline A\setminus\operatorname{Int}A$ of $[0,1]$ is $\{0,1\}$, and that of $\mathbb Q$ is $\mathbb R$.
