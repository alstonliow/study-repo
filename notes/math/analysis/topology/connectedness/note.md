---
title: "Connectedness"
sources: [camib-at-m3]
requires: [math/analysis/topology/subspace-product-quotient]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Metric and Topological Spaces (Easter 2015 lecture notes), Section 3, in our own wording; the proof that [0,1] is connected is derived from the intermediate value theorem already in the notes; examples ours; proofs written out in steps. -->

A space is connected if it does not fall apart into two open pieces. Connectedness is the topological content of the intermediate value theorem, and it distinguishes spaces that are not homeomorphic.

::: {#def-connected .definition name="Connected space"}

A topological space $X$ is *disconnected* if $X=U\cup V$ for disjoint non-empty open sets $U,V$, and *connected* otherwise. A subset is connected if it is connected in the subspace topology.

:::

If $X=U\cup V$ is such a splitting, $U$ and $V$ are both open and closed. So $X$ is connected if and only if its only subsets that are both open and closed are $\emptyset$ and $X$.

::: {#prp-connected-two-valued .proposition name="Connectedness through two-valued maps"}

$X$ is connected if and only if every continuous map $f:X\to\{0,1\}$, where $\{0,1\}$ has the discrete topology, is constant.

:::

::: {.proof}

1. If $X=U\cup V$ is a splitting, the map that is $0$ on $U$ and $1$ on $V$ is continuous (the preimages of the four subsets of $\{0,1\}$ are $\emptyset,U,V,X$) and not constant.

2. Conversely, if $f:X\to\{0,1\}$ is continuous and not constant, $U=f^{-1}(0)$ and $V=f^{-1}(1)$ split $X$.

:::

::: {#thm-connected-subsets-of-r .theorem name="The connected subsets of $\mathbb R$ are the intervals"}

A subset $A\subseteq\mathbb R$ is connected if and only if it is an interval: whenever $a<c<b$ with $a,b\in A$, also $c\in A$.

:::

::: {.proof}

1. *Not an interval implies disconnected.* If $a<c<b$ with $a,b\in A$ and $c\notin A$, then $A\cap(-\infty,c)$ and $A\cap(c,\infty)$ are disjoint, open in $A$, non-empty and cover $A$.

2. *Intervals are connected.* Let $A$ be an interval and $f:A\to\{0,1\}$ continuous. Regarded as a map into $\mathbb R$ it is still continuous (open subsets of $\mathbb R$ meet $\{0,1\}$ in open sets). If $f(a)=0$ and $f(b)=1$ with $a,b\in A$, then $f$ is continuous on the interval between $a$ and $b$, which lies in $A$, and by the intermediate value theorem (@thm-intermediate-value-proof) it takes the value $\frac12$, which is impossible. So $f$ is constant, and $A$ is connected by @prp-connected-two-valued.

:::

::: {#prp-continuous-image-connected .proposition name="Continuous images of connected spaces are connected"}

If $X$ is connected and $f:X\to Y$ is continuous, then $f(X)$ is connected.

:::

::: {.proof}

1. Let $g:f(X)\to\{0,1\}$ be continuous. Then $g\circ f:X\to\{0,1\}$ is continuous (@prp-subspace-continuity), hence constant.

2. Since every point of $f(X)$ is $f(x)$ for some $x$, $g$ is constant. Apply @prp-connected-two-valued.

:::

::: {#thm-intermediate-value-topological .theorem name="Intermediate value theorem, topological form" generalizes="thm-intermediate-value-proof"}

If $X$ is connected, $f:X\to\mathbb R$ is continuous, and $f(x)<c<f(y)$ for some $x,y\in X$, then $f(z)=c$ for some $z\in X$.

:::

::: {.proof}

By @prp-continuous-image-connected, $f(X)$ is connected, so it is an interval (@thm-connected-subsets-of-r) containing $f(x)$ and $f(y)$, hence $c$.

:::

::: {#exm-connectedness-invariant .example name="Telling spaces apart"}

1. $\mathbb R\not\cong\mathbb R^2$. A homeomorphism $f$ would restrict to a homeomorphism $\mathbb R\setminus\{0\}\to\mathbb R^2\setminus\{f(0)\}$. The first space is disconnected; the second is path-connected, hence connected (@prp-path-connected-connected).
2. $[0,1)\not\cong S^1$. Removing the point $\frac12$ disconnects $[0,1)$, while removing any point $q$ leaves $S^1\setminus\{q\}$ connected (it is a path-connected arc). A homeomorphism $f$ would give $[0,1)\setminus\{\frac12\}\cong S^1\setminus\{f(\frac12)\}$.

:::

## Path-connectedness

::: {#def-path-connected .definition name="Path, path-connected"}

A *path* from $x$ to $y$ in $X$ is a continuous $\gamma:[0,1]\to X$ with $\gamma(0)=x$, $\gamma(1)=y$. $X$ is *path-connected* if any two points are joined by a path.

:::

Paths can be reversed, $\gamma(1-t)$, and joined: if $\gamma$ goes from $x$ to $y$ and $\sigma$ from $y$ to $z$, let $\tau(t)=\gamma(2t)$ for $t\le\frac12$ and $\tau(t)=\sigma(2t-1)$ for $t\ge\frac12$. Then $\tau$ is continuous: for closed $C$, $\tau^{-1}(C)$ is the union of the closed sets $\{t\le\frac12:\gamma(2t)\in C\}$ and $\{t\ge\frac12:\sigma(2t-1)\in C\}$. So "joined by a path" is an equivalence relation; its classes are the *path components*.

::: {#prp-path-connected-connected .proposition name="Path-connected implies connected"}

Every path-connected space is connected.

:::

::: {.proof}

1. Let $f:X\to\{0,1\}$ be continuous and $x,y\in X$. Take a path $\gamma$ from $x$ to $y$.

2. $f\circ\gamma:[0,1]\to\{0,1\}$ is continuous and $[0,1]$ is connected (@thm-connected-subsets-of-r), so $f\circ\gamma$ is constant and $f(x)=f(y)$. By @prp-connected-two-valued, $X$ is connected.

:::

Convex subsets of $\mathbb R^n$, such as balls, are path-connected through straight segments $t\mapsto(1-t)x+ty$. So is $\mathbb R^n\setminus\{p\}$ for $n\ge2$: two points can be joined by at most two segments avoiding $p$.

::: {#exm-topologists-sine-curve .example name="Connected but not path-connected"}

Let $S=\{(x,\sin\frac1x):0<x\le1\}$ and $T=S\cup(\{0\}\times[-1,1])$ in $\mathbb R^2$.

1. *$T$ is connected.* $S$ is path-connected, being the image of $(0,1]$ under a continuous map. Let $f:T\to\{0,1\}$ be continuous; it is constant on $S$, say $0$. Every point $(0,y)$ with $|y|\le1$ is a limit of points of $S$ (take $x_n\to0$ with $\sin\frac1{x_n}=y$), so $f(0,y)=0$ by continuity.

2. *$T$ is not path-connected.* Suppose $\gamma=(\gamma_1,\gamma_2)$ is a path in $T$ from $(0,0)$ to $(1,\sin1)$. Let $t_0=\sup\{t:\gamma_1(t)=0\}$; by continuity $\gamma_1(t_0)=0$, and $\gamma_1>0$ on $(t_0,1]$. Continuity of $\gamma_2$ at $t_0$ gives $\delta>0$ with $|\gamma_2(t)-\gamma_2(t_0)|<\frac12$ for $t\in[t_0,t_0+\delta]$. But $\gamma_1$ maps $[t_0,t_0+\delta]$ onto an interval $[0,\eta]$ with $\eta>0$ (@thm-intermediate-value-proof), and on $(0,\eta]$ the function $\sin\frac1x$ takes both values $1$ and $-1$. So $\gamma_2=\sin\frac1{\gamma_1}$ takes values $1$ and $-1$ on $(t_0,t_0+\delta]$, contradicting the bound.

:::

::: {#prp-open-connected-path-connected .proposition name="Open connected subsets of $\mathbb R^n$ are path-connected"}

If $U\subseteq\mathbb R^n$ is open and connected, it is path-connected.

:::

::: {.proof}

1. If $U=\emptyset$ there is nothing to show. Otherwise fix $x\in U$ and let $P$ be the set of points of $U$ joined to $x$ by a path in $U$; $x\in P$.

2. *$P$ is open.* If $y\in P$, choose a ball $B_r(y)\subseteq U$. Each $z$ in the ball is joined to $y$ by a segment in the ball, so to $x$ by a joined path; $B_r(y)\subseteq P$.

3. *$U\setminus P$ is open.* If $y\in U\setminus P$ and $B_r(y)\subseteq U$, no point of the ball lies in $P$: otherwise joining through it would connect $y$ to $x$.

4. $U$ is connected and $P\ne\emptyset$, so $U\setminus P=\emptyset$ and $P=U$.

:::

## Components

::: {#prp-union-connected .proposition name="Unions of connected sets with a common point"}

If each $Y_\alpha\subseteq X$ is connected and $\bigcap_\alpha Y_\alpha\ne\emptyset$, then $\bigcup_\alpha Y_\alpha$ is connected.

:::

::: {.proof}

1. Let $f:\bigcup Y_\alpha\to\{0,1\}$ be continuous and $p\in\bigcap Y_\alpha$.

2. Each restriction $f|_{Y_\alpha}$ is continuous, hence constant, equal to $f(p)$. So $f$ is constant.

:::

::: {#def-connected-component .definition name="Connected component"}

The *component* $C(x)$ of a point $x\in X$ is the union of all connected subsets of $X$ containing $x$.

:::

By @prp-union-connected, $C(x)$ is connected, so it is the largest connected set containing $x$. If $C(x)\cap C(y)\ne\emptyset$, then $C(x)\cup C(y)$ is connected and contains $x$, so $C(y)\subseteq C(x)$, and symmetrically. Hence the components partition $X$. Each path component lies inside a component, and for open subsets of $\mathbb R^n$ the two notions agree (@prp-open-connected-path-connected applied to the components, which are open there since balls are connected). For $\mathbb Q$ the components are single points, although $\mathbb Q$ has no isolated points.
