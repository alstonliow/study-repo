---
title: "Metric Spaces"
sources: [camib-at-a5, camib-at-m1]
requires: [math/analysis/real/continuity/continuous-functions]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 5.1, and Metric and Topological Spaces (Easter 2015 lecture notes), Sections 1.1-1.2, in our own wording; the two sources cover the same definitions and are merged here into one block each; examples ours; proofs written out in steps. -->

Convergence and continuity in $\mathbb R$ use only the distance $|x-y|$ and three of its properties. A metric space is a set with a distance function having those properties, and the definitions carry over unchanged.

::: {#def-metric-space .definition name="Metric space"}

A *metric* on a set $X$ is a function $d:X\times X\to\mathbb R$ such that for all $x,y,z\in X$:

1. $d(x,y)\ge0$, with equality if and only if $x=y$ (positivity);
2. $d(x,y)=d(y,x)$ (symmetry);
3. $d(x,z)\le d(x,y)+d(y,z)$ (triangle inequality).

A *metric space* is a pair $(X,d)$ of a set and a metric on it.

:::

::: {#exm-metric-spaces .example name="Metric spaces"}

1. $\mathbb R$ with $d(x,y)=|x-y|$, and $\mathbb R^n$ with the Euclidean metric $d_2(x,y)=\|x-y\|_2=\bigl(\sum_i(x_i-y_i)^2\bigr)^{1/2}$; its triangle inequality is @thm-cauchy-schwarz.
2. Any set $X$ with the *discrete metric*: $d(x,y)=1$ if $x\ne y$ and $d(x,x)=0$.
3. Binary strings of length $n$ with the *Hamming distance*: the number of positions in which two strings differ. If $x$ and $z$ differ in position $i$, then $y$ differs in position $i$ from $x$ or from $z$, which gives the triangle inequality.
4. The continuous functions $C[a,b]$ with the *uniform metric* $d_\infty(f,g)=\sup_{x\in[a,b]}|f(x)-g(x)|$. The supremum is finite by @thm-extreme-value-proof, and $|f(x)-h(x)|\le|f(x)-g(x)|+|g(x)-h(x)|\le d_\infty(f,g)+d_\infty(g,h)$ for each $x$ gives the triangle inequality.
5. The same set $C[a,b]$ with $d_1(f,g)=\int_a^b|f-g|$. Positivity uses continuity: if $|f-g|$ is positive at one point it is positive on an interval, so its integral is positive.

:::

::: {#def-metric-subspace .definition name="Metric subspace"}

If $(X,d)$ is a metric space and $Y\subseteq X$, the restriction of $d$ to $Y\times Y$ is a metric on $Y$. With it, $Y$ is a *subspace* of $X$.

:::

For example, every subset of $\mathbb R^n$ is a metric space with the Euclidean metric.

## Convergence and continuity

::: {#def-convergence-metric .definition name="Convergence in a metric space"}

A sequence $(x_n)$ in $(X,d)$ *converges* to $x\in X$, written $x_n\to x$, if $d(x_n,x)\to0$, that is,
$$\forall\varepsilon>0\ \exists N\ \forall n\ge N\quad d(x_n,x)<\varepsilon.$$

:::

::: {#prp-limit-unique-metric .proposition name="Limits are unique" generalizes="thm-limit-unique"}

If $x_n\to x$ and $x_n\to y$ in a metric space, then $x=y$.

:::

::: {.proof}

1. For every $n$, $0\le d(x,y)\le d(x,x_n)+d(x_n,y)$ by symmetry and the triangle inequality.

2. The right-hand side tends to $0$, so $d(x,y)=0$ and $x=y$ by positivity.

:::

In $C[a,b]$, convergence in $d_\infty$ is exactly uniform convergence (@def-uniform-convergence); convergence in $d_1$ is weaker. The tents of @exm-pointwise-integrals-fail, scaled to height $1$, have $d_1$-distance $\frac1n$ from $0$ but $d_\infty$-distance $1$.

::: {#def-continuity-metric .definition name="Continuity between metric spaces" generalizes="def-continuity-epsilon-delta"}

Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces. A function $f:X\to Y$ is *continuous at* $a\in X$ if
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x\in X\quad d_X(x,a)<\delta\Rightarrow d_Y(f(x),f(a))<\varepsilon,$$
and *continuous* if it is continuous at every point of $X$.

:::

::: {#prp-sequential-continuity-metric .proposition name="Sequential continuity" generalizes="thm-sequential-continuity"}

$f:X\to Y$ is continuous at $a$ if and only if $f(x_n)\to f(a)$ for every sequence $x_n\to a$ in $X$.

:::

::: {.proof}

1. *Continuity implies sequential continuity.* Let $x_n\to a$ and $\varepsilon>0$. Take $\delta$ from continuity, then $N$ with $d_X(x_n,a)<\delta$ for $n\ge N$. Then $d_Y(f(x_n),f(a))<\varepsilon$ for $n\ge N$.

2. *Conversely,* suppose $f$ is not continuous at $a$. Then for some $\varepsilon>0$ and every $n$ there is $x_n$ with $d_X(x_n,a)<\frac1n$ but $d_Y(f(x_n),f(a))\ge\varepsilon$. So $x_n\to a$ while $f(x_n)\not\to f(a)$.

:::

Compositions of continuous maps are continuous, by the same proof as in $\mathbb R$ or by @prp-sequential-continuity-metric.

## Equivalent metrics

::: {#def-lipschitz-equivalent-metrics .definition name="Lipschitz equivalent metrics"}

Two metrics $d,d'$ on $X$ are *Lipschitz equivalent* if there are constants $0<A\le B$ with
$$A\,d(x,y)\le d'(x,y)\le B\,d(x,y)\qquad\text{for all }x,y\in X.$$

:::

Lipschitz equivalent metrics have the same convergent sequences, with the same limits, and hence (by @prp-sequential-continuity-metric) the same continuous functions. On $\mathbb R^n$, $\|x\|_\infty\le\|x\|_2\le\sqrt n\,\|x\|_\infty$, where $\|x\|_\infty=\max_i|x_i|$, so $d_2$ and $d_\infty$ are Lipschitz equivalent.

::: {#exm-metric-spaces-bounded-metric .example name="Same convergence without Lipschitz equivalence"}

On $\mathbb R$ let $d'(x,y)=\min\{1,|x-y|\}$. It is a metric: for the triangle inequality, if $d'(x,y)$ or $d'(y,z)$ equals $1$ the right-hand side is at least $1\ge d'(x,z)$, and otherwise it is $|x-y|+|y-z|\ge|x-z|\ge d'(x,z)$. Also $d'(x_n,x)\to0$ if and only if $|x_n-x|\to0$, so $d$ and $d'$ have the same convergent sequences. They are not Lipschitz equivalent: $d'(0,n)=1$ while $|0-n|=n$, so no $A>0$ has $A|x-y|\le d'(x,y)$ for all $x,y$. The space $(\mathbb R,d')$ is bounded, $(\mathbb R,|\cdot|)$ is not: boundedness depends on more than the convergent sequences.

:::
