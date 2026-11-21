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

::: {#fig-closure-and-interior-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (1.484,0.000) -- (1.526,0.115) -- (1.541,0.234) -- (1.525,0.354) -- (1.476,0.469) -- (1.394,0.575) -- (1.283,0.666) -- (1.148,0.738) -- (0.997,0.791) -- (0.838,0.824) -- (0.679,0.840) -- (0.525,0.843) -- (0.381,0.838) -- (0.247,0.830) -- (0.121,0.823) -- (0.000,0.820) -- (-0.121,0.823) -- (-0.247,0.830) -- (-0.381,0.838) -- (-0.525,0.843) -- (-0.679,0.840) -- (-0.838,0.824) -- (-0.997,0.791) -- (-1.148,0.738) -- (-1.283,0.666) -- (-1.394,0.575) -- (-1.476,0.469) -- (-1.525,0.354) -- (-1.541,0.234) -- (-1.526,0.115) -- (-1.484,0.000) -- (-1.422,-0.107) -- (-1.348,-0.205) -- (-1.267,-0.294) -- (-1.184,-0.377) -- (-1.103,-0.455) -- (-1.024,-0.532) -- (-0.946,-0.608) -- (-0.865,-0.686) -- (-0.777,-0.764) -- (-0.679,-0.840) -- (-0.568,-0.911) -- (-0.442,-0.972) -- (-0.303,-1.019) -- (-0.154,-1.050) -- (-0.000,-1.060) -- (0.154,-1.050) -- (0.303,-1.019) -- (0.442,-0.972) -- (0.568,-0.911) -- (0.679,-0.840) -- (0.777,-0.764) -- (0.865,-0.686) -- (0.946,-0.608) -- (1.024,-0.532) -- (1.103,-0.455) -- (1.184,-0.377) -- (1.267,-0.294) -- (1.348,-0.205) -- (1.422,-0.107) -- cycle;
\draw[emph] (1.484,0.000) -- (1.526,0.115) -- (1.541,0.234) -- (1.525,0.354) -- (1.476,0.469) -- (1.394,0.575) -- (1.283,0.666) -- (1.148,0.738) -- (0.997,0.791) -- (0.838,0.824) -- (0.679,0.840) -- (0.525,0.843) -- (0.381,0.838) -- (0.247,0.830) -- (0.121,0.823) -- (0.000,0.820) -- (-0.121,0.823) -- (-0.247,0.830) -- (-0.381,0.838) -- (-0.525,0.843) -- (-0.679,0.840) -- (-0.838,0.824) -- (-0.997,0.791) -- (-1.148,0.738) -- (-1.283,0.666) -- (-1.394,0.575) -- (-1.476,0.469) -- (-1.525,0.354) -- (-1.541,0.234) -- (-1.526,0.115) -- (-1.484,0.000) -- (-1.422,-0.107) -- (-1.348,-0.205) -- (-1.267,-0.294) -- (-1.184,-0.377) -- (-1.103,-0.455) -- (-1.024,-0.532) -- (-0.946,-0.608) -- (-0.865,-0.686) -- (-0.777,-0.764) -- (-0.679,-0.840) -- (-0.568,-0.911) -- (-0.442,-0.972) -- (-0.303,-1.019) -- (-0.154,-1.050) -- (-0.000,-1.060) -- (0.154,-1.050) -- (0.303,-1.019) -- (0.442,-0.972) -- (0.568,-0.911) -- (0.679,-0.840) -- (0.777,-0.764) -- (0.865,-0.686) -- (0.946,-0.608) -- (1.024,-0.532) -- (1.103,-0.455) -- (1.184,-0.377) -- (1.267,-0.294) -- (1.348,-0.205) -- (1.422,-0.107) -- cycle;
\node[hl dot] at (1.47,0.2) {}; \node[lab, right] at (1.55,0.2) {$x\in\overline A$};
\draw[faint, dashed] (1.47,0.2) circle (0.45);
\node[dot] at (2.9,-0.6) {}; \draw[faint, dashed] (2.9,-0.6) circle (0.45); \node[lab, right] at (3.35,-0.6) {$y\notin\overline A$};
\node[lab] at (-0.3,0) {$A$};
\end{tikzpicture}
\end{center}
```

$x\in\overline A$ exactly when every open neighbourhood of $x$ meets $A$; a point such as $y$ has a neighbourhood that misses $A$.

:::

::: {#exm-closure-and-interior-1 .example name="Closures and dense sets"}

1. In $\mathbb R$, $\overline{(0,1)}=[0,1]$, and $\mathbb Q$ is dense: every open interval contains a rational (@thm-archimedean-property). So is $\mathbb R\setminus\mathbb Q$.
2. In a metric space $\overline{B_r(x)}\subseteq\overline B_r(x)$, since the closed ball is closed; equality can fail. In a discrete space $B_1(x)=\{x\}$ is closed, while $\overline B_1(x)=X$.
3. In the cofinite topology on an infinite set, every infinite subset is dense, since the only closed set containing it is $X$.

:::

::: {#fig-closure-and-interior-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.2,0) -- (6.2,0);
\draw[faint] (0.000,-0.08) -- (0.000,0.08);
\draw[faint] (0.750,-0.08) -- (0.750,0.08);
\draw[faint] (0.857,-0.08) -- (0.857,0.08);
\draw[faint] (1.000,-0.08) -- (1.000,0.08);
\draw[faint] (1.200,-0.08) -- (1.200,0.08);
\draw[faint] (1.500,-0.08) -- (1.500,0.08);
\draw[faint] (1.714,-0.08) -- (1.714,0.08);
\draw[faint] (2.000,-0.08) -- (2.000,0.08);
\draw[faint] (2.250,-0.08) -- (2.250,0.08);
\draw[faint] (2.400,-0.08) -- (2.400,0.08);
\draw[faint] (2.571,-0.08) -- (2.571,0.08);
\draw[faint] (3.000,-0.08) -- (3.000,0.08);
\draw[faint] (3.429,-0.08) -- (3.429,0.08);
\draw[faint] (3.600,-0.08) -- (3.600,0.08);
\draw[faint] (3.750,-0.08) -- (3.750,0.08);
\draw[faint] (4.000,-0.08) -- (4.000,0.08);
\draw[faint] (4.286,-0.08) -- (4.286,0.08);
\draw[faint] (4.500,-0.08) -- (4.500,0.08);
\draw[faint] (4.800,-0.08) -- (4.800,0.08);
\draw[faint] (5.000,-0.08) -- (5.000,0.08);
\draw[faint] (5.143,-0.08) -- (5.143,0.08);
\draw[faint] (5.250,-0.08) -- (5.250,0.08);
\draw[faint] (6.000,-0.08) -- (6.000,0.08);
\fill[tintB] (2.6,-0.2) rectangle (2.9,0.2); \node[lab, above] at (2.75,0.25) {any open interval}; \node[lab, below] at (3,-0.25) {meets $\mathbb Q$};
\end{tikzpicture}
\end{center}
```

Part 1: rationals with small denominators already crowd $[0,1]$; by the Archimedean property every open interval contains one, so $\overline{\mathbb Q}=\mathbb R$.

:::

## Interior

::: {#def-interior .definition name="Interior"}

The *interior* $\operatorname{Int}A$ of $A\subseteq X$ is the union of all open sets contained in $A$.

:::

::: {#fig-closure-and-interior-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (1.600,0.000) -- (1.665,0.120) -- (1.703,0.249) -- (1.706,0.381) -- (1.670,0.511) -- (1.593,0.632) -- (1.479,0.739) -- (1.333,0.825) -- (1.165,0.890) -- (0.984,0.931) -- (0.800,0.953) -- (0.621,0.958) -- (0.451,0.954) -- (0.292,0.945) -- (0.143,0.938) -- (0.000,0.935) -- (-0.143,0.938) -- (-0.292,0.945) -- (-0.451,0.954) -- (-0.621,0.958) -- (-0.800,0.953) -- (-0.984,0.931) -- (-1.165,0.890) -- (-1.333,0.825) -- (-1.479,0.739) -- (-1.593,0.632) -- (-1.670,0.511) -- (-1.706,0.381) -- (-1.703,0.249) -- (-1.665,0.120) -- (-1.600,0.000) -- (-1.517,-0.110) -- (-1.427,-0.209) -- (-1.337,-0.299) -- (-1.253,-0.384) -- (-1.178,-0.467) -- (-1.110,-0.554) -- (-1.045,-0.647) -- (-0.976,-0.745) -- (-0.897,-0.849) -- (-0.800,-0.953) -- (-0.681,-1.051) -- (-0.538,-1.138) -- (-0.373,-1.207) -- (-0.191,-1.250) -- (-0.000,-1.265) -- (0.191,-1.250) -- (0.373,-1.207) -- (0.538,-1.138) -- (0.681,-1.051) -- (0.800,-0.953) -- (0.897,-0.849) -- (0.976,-0.745) -- (1.045,-0.647) -- (1.110,-0.554) -- (1.178,-0.467) -- (1.253,-0.384) -- (1.337,-0.299) -- (1.427,-0.209) -- (1.517,-0.110) -- cycle;
\draw[hl] (1.600,0.000) -- (1.665,0.120) -- (1.703,0.249) -- (1.706,0.381) -- (1.670,0.511) -- (1.593,0.632) -- (1.479,0.739) -- (1.333,0.825) -- (1.165,0.890) -- (0.984,0.931) -- (0.800,0.953) -- (0.621,0.958) -- (0.451,0.954) -- (0.292,0.945) -- (0.143,0.938) -- (0.000,0.935) -- (-0.143,0.938) -- (-0.292,0.945) -- (-0.451,0.954) -- (-0.621,0.958) -- (-0.800,0.953) -- (-0.984,0.931) -- (-1.165,0.890) -- (-1.333,0.825) -- (-1.479,0.739) -- (-1.593,0.632) -- (-1.670,0.511) -- (-1.706,0.381) -- (-1.703,0.249) -- (-1.665,0.120) -- (-1.600,0.000);
\draw[faint, dashed] (-1.600,0.000) -- (-1.517,-0.110) -- (-1.427,-0.209) -- (-1.337,-0.299) -- (-1.253,-0.384) -- (-1.178,-0.467) -- (-1.110,-0.554) -- (-1.045,-0.647) -- (-0.976,-0.745) -- (-0.897,-0.849) -- (-0.800,-0.953) -- (-0.681,-1.051) -- (-0.538,-1.138) -- (-0.373,-1.207) -- (-0.191,-1.250) -- (-0.000,-1.265) -- (0.191,-1.250) -- (0.373,-1.207) -- (0.538,-1.138) -- (0.681,-1.051) -- (0.800,-0.953) -- (0.897,-0.849) -- (0.976,-0.745) -- (1.045,-0.647) -- (1.110,-0.554) -- (1.178,-0.467) -- (1.253,-0.384) -- (1.337,-0.299) -- (1.427,-0.209) -- (1.517,-0.110) -- (1.600,0.000);
\draw[regionB] (-0.2,0.1) circle (0.4); \node[dot] at (-0.2,0.1) {}; \node[lab, below] at (-0.2,0.1) {interior point};
\node[lab, above right] at (1.2,0.9) {boundary points in $A$}; \node[lab, below right] at (1.1,-1.0) {boundary points not in $A$};
\end{tikzpicture}
\end{center}
```

A set $A$ that contains only part of its boundary (solid, not dashed). Its interior $A^\circ$ leaves out the whole boundary; its closure $\overline A$ adds the whole boundary, so $A^\circ\subseteq A\subseteq\overline A$.

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
