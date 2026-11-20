---
title: "Continuous Maps between Metric Spaces"
sources: [camib-at-a4, camib-at-a5, camib-at-m1]
requires: [math/analysis/metric-spaces/compact-metric-spaces, math/analysis/real/integration/integrable-functions]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Sections 4.4 and 5.5, and Metric and Topological Spaces (Easter 2015 lecture notes), Section 1.4, in our own wording; the sources are merged into one block per item; examples ours; proofs written out in steps. -->

Continuity (@def-continuity-metric) can be stated with open sets alone. On compact spaces continuous maps behave as on closed intervals: they are bounded, attain their extrema and are uniformly continuous.

::: {#thm-continuity-open-sets .theorem name="Continuity through open sets"}

For a map $f:X\to Y$ between metric spaces the following are equivalent:

1. $f$ is continuous;
2. $f^{-1}(V)$ is open in $X$ for every open $V\subseteq Y$;
3. $f^{-1}(C)$ is closed in $X$ for every closed $C\subseteq Y$.

:::

::: {.proof}

1. *(1) implies (2).* Let $V$ be open and $a\in f^{-1}(V)$. Choose $\varepsilon$ with $B_\varepsilon(f(a))\subseteq V$, then $\delta$ from continuity at $a$. Then $f(B_\delta(a))\subseteq B_\varepsilon(f(a))\subseteq V$, so $B_\delta(a)\subseteq f^{-1}(V)$.

2. *(2) implies (1).* Let $a\in X$ and $\varepsilon>0$. The ball $B_\varepsilon(f(a))$ is open (@lem-open-ball-open), so $f^{-1}(B_\varepsilon(f(a)))$ is an open set containing $a$, and contains some $B_\delta(a)$. That is the $\varepsilon$-$\delta$ condition.

3. *(2) is equivalent to (3)*, because $f^{-1}(Y\setminus C)=X\setminus f^{-1}(C)$ and closed sets are the complements of open sets (@prp-closed-iff-complement-open).

:::

::: {#exm-continuous-maps-1 .example name="Sets defined by continuous inequalities"}

$\{(x,y)\in\mathbb R^2:x^2+y^2<1,\ y>x^3\}$ is open, being $f^{-1}(0,\infty)\cap g^{-1}(0,\infty)$ for the continuous $f(x,y)=1-x^2-y^2$ and $g(x,y)=y-x^3$. Replacing $<,>$ by $\le,\ge$ gives a closed set.

:::

## Continuous maps on compact spaces

::: {#thm-continuous-image-compact .theorem name="Continuous images of compact spaces are compact"}

If $X$ is sequentially compact and $f:X\to Y$ is continuous, then $f(X)$ is sequentially compact.

:::

::: {.proof}

1. Let $(y_n)$ be a sequence in $f(X)$ and write $y_n=f(x_n)$.

2. Some subsequence $x_{n_k}\to x\in X$, and by @prp-sequential-continuity-metric $y_{n_k}=f(x_{n_k})\to f(x)\in f(X)$.

:::

::: {#cor-extreme-value-compact .corollary name="Extreme value theorem on compact spaces" generalizes="thm-extreme-value-proof"}

A continuous $f:X\to\mathbb R$ on a non-empty sequentially compact metric space is bounded and attains its supremum and infimum.

:::

::: {.proof}

1. $f(X)\subseteq\mathbb R$ is sequentially compact by @thm-continuous-image-compact, hence closed and bounded by @thm-compact-complete-bounded.

2. Let $s=\sup f(X)$, finite by step 1. Points of $f(X)$ converge to $s$ (choose $y_n\in f(X)$ with $y_n>s-\frac1n$), so $s\in f(X)$ since $f(X)$ is closed. The infimum is similar.

:::

::: {#def-uniform-continuity-metric .definition name="Uniformly continuous, Lipschitz" generalizes="def-uniform-continuity"}

A map $f:X\to Y$ between metric spaces is *uniformly continuous* if
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x,x'\in X\quad d_X(x,x')<\delta\Rightarrow d_Y(f(x),f(x'))<\varepsilon,$$
and *Lipschitz* with constant $K$ if $d_Y(f(x),f(x'))\le K\,d_X(x,x')$ for all $x,x'$.

:::

A Lipschitz map is uniformly continuous (take $\delta=\varepsilon/K$), and a uniformly continuous map is continuous. Neither converse holds: $\sqrt x$ on $[0,1]$ is uniformly continuous (@thm-uniform-continuity-compact) but not Lipschitz, since $\frac{\sqrt x-0}{x-0}=\frac1{\sqrt x}$ is unbounded.

::: {#thm-uniform-continuity-compact-metric .theorem name="Continuous on compact implies uniformly continuous" generalizes="thm-uniform-continuity-compact"}

A continuous map from a sequentially compact metric space to a metric space is uniformly continuous.

:::

::: {.proof}

1. Suppose not: there are $\varepsilon>0$ and $x_n,x_n'$ with $d(x_n,x_n')<\frac1n$ but $d(f(x_n),f(x_n'))\ge\varepsilon$.

2. Pass to a subsequence with $x_{n_k}\to x$. Then $d(x'_{n_k},x)\le d(x'_{n_k},x_{n_k})+d(x_{n_k},x)\to0$, so $x'_{n_k}\to x$ too.

3. By continuity at $x$, $d(f(x_{n_k}),f(x'_{n_k}))\le d(f(x_{n_k}),f(x))+d(f(x),f(x'_{n_k}))\to0$, contradicting step 1.

:::

## Linear maps

::: {#thm-linear-maps-continuous .theorem name="Linear maps on finite-dimensional spaces are continuous"}

Let $V,W$ be normed spaces with $V$ finite-dimensional, and $T:V\to W$ linear. Then there is $C$ with $\|Tv\|\le C\|v\|$ for all $v$; hence $T$ is Lipschitz and continuous.

:::

::: {.proof}

1. Choose a basis $e_1,\dots,e_n$ of $V$ and write $v=\sum v_ie_i$. Then
$$\|Tv\|=\Bigl\|\sum v_iTe_i\Bigr\|\le\sum_i|v_i|\,\|Te_i\|\le\Bigl(\max_i\|Te_i\|\Bigr)\|v\|_1,$$
where $\|v\|_1=\sum|v_i|$ is a norm on $V$.

2. By @thm-norms-equivalent-finite-dimension, $\|v\|_1\le B\|v\|$ for some $B$. So $\|Tv\|\le C\|v\|$ with $C=B\max_i\|Te_i\|$.

3. Then $\|Tv-Tv'\|=\|T(v-v')\|\le C\|v-v'\|$.

:::

::: {#exm-unbounded-linear-map .example name="A discontinuous linear map"}

On the polynomials on $[0,1]$ with $\|\cdot\|_\infty$, differentiation $D$ is linear but not continuous: $p_n(x)=x^n$ has $\|p_n\|_\infty=1$ while $\|Dp_n\|_\infty=n$. So no $C$ has $\|Dp\|\le C\|p\|$; and $\frac1np_n\to0$ while $D(\frac1np_n)=x^{n-1}\not\to0$. Finite dimension is essential in @thm-linear-maps-continuous.

:::
