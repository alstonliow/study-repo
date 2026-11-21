---
title: "Compact Spaces"
sources: [camib-at-m4]
requires: [math/analysis/topology/subspace-product-quotient, math/analysis/real/continuity/compactness-of-closed-intervals]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Metric and Topological Spaces (Easter 2015 lecture notes), Sections 4.1-4.3, in our own wording; the converse direction of the metric equivalence (via the Lebesgue number) is our own write-up of the standard proof; examples ours; proofs written out in steps. -->

Compactness turns local information at every point into global information, by passing from infinitely many open sets to finitely many. For closed bounded intervals this is the Heine–Borel theorem (@thm-heine-borel-interval); here it becomes a definition.

::: {#def-compact-space .definition name="Open cover, compact space" generalizes="def-open-cover"}

An *open cover* of a topological space $X$ is a collection of open sets whose union is $X$; a *subcover* is a subcollection that still covers $X$. $X$ is *compact* if every open cover has a finite subcover. A subset is compact if it is compact in the subspace topology; equivalently, every cover of it by open sets of $X$ has a finite subcover.

:::

::: {#fig-compact-spaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (2.014,0.000) -- (2.071,0.115) -- (2.091,0.234) -- (2.070,0.354) -- (2.004,0.469) -- (1.892,0.575) -- (1.741,0.666) -- (1.558,0.738) -- (1.353,0.791) -- (1.137,0.824) -- (0.922,0.840) -- (0.713,0.843) -- (0.517,0.838) -- (0.335,0.830) -- (0.164,0.823) -- (0.000,0.820) -- (-0.164,0.823) -- (-0.335,0.830) -- (-0.517,0.838) -- (-0.713,0.843) -- (-0.921,0.840) -- (-1.137,0.824) -- (-1.353,0.791) -- (-1.558,0.738) -- (-1.741,0.666) -- (-1.892,0.575) -- (-2.004,0.469) -- (-2.070,0.354) -- (-2.091,0.234) -- (-2.071,0.115) -- (-2.014,0.000) -- (-1.930,-0.107) -- (-1.829,-0.205) -- (-1.719,-0.294) -- (-1.607,-0.377) -- (-1.497,-0.455) -- (-1.390,-0.532) -- (-1.284,-0.608) -- (-1.174,-0.686) -- (-1.055,-0.764) -- (-0.922,-0.840) -- (-0.770,-0.911) -- (-0.600,-0.972) -- (-0.412,-1.019) -- (-0.210,-1.050) -- (-0.000,-1.060) -- (0.210,-1.050) -- (0.412,-1.019) -- (0.600,-0.972) -- (0.770,-0.911) -- (0.922,-0.840) -- (1.055,-0.764) -- (1.174,-0.686) -- (1.284,-0.608) -- (1.390,-0.532) -- (1.497,-0.455) -- (1.607,-0.377) -- (1.719,-0.294) -- (1.829,-0.205) -- (1.930,-0.107) -- cycle;
\draw[emph] (2.014,0.000) -- (2.071,0.115) -- (2.091,0.234) -- (2.070,0.354) -- (2.004,0.469) -- (1.892,0.575) -- (1.741,0.666) -- (1.558,0.738) -- (1.353,0.791) -- (1.137,0.824) -- (0.922,0.840) -- (0.713,0.843) -- (0.517,0.838) -- (0.335,0.830) -- (0.164,0.823) -- (0.000,0.820) -- (-0.164,0.823) -- (-0.335,0.830) -- (-0.517,0.838) -- (-0.713,0.843) -- (-0.921,0.840) -- (-1.137,0.824) -- (-1.353,0.791) -- (-1.558,0.738) -- (-1.741,0.666) -- (-1.892,0.575) -- (-2.004,0.469) -- (-2.070,0.354) -- (-2.091,0.234) -- (-2.071,0.115) -- (-2.014,0.000) -- (-1.930,-0.107) -- (-1.829,-0.205) -- (-1.719,-0.294) -- (-1.607,-0.377) -- (-1.497,-0.455) -- (-1.390,-0.532) -- (-1.284,-0.608) -- (-1.174,-0.686) -- (-1.055,-0.764) -- (-0.922,-0.840) -- (-0.770,-0.911) -- (-0.600,-0.972) -- (-0.412,-1.019) -- (-0.210,-1.050) -- (-0.000,-1.060) -- (0.210,-1.050) -- (0.412,-1.019) -- (0.600,-0.972) -- (0.770,-0.911) -- (0.922,-0.840) -- (1.055,-0.764) -- (1.174,-0.686) -- (1.284,-0.608) -- (1.390,-0.532) -- (1.497,-0.455) -- (1.607,-0.377) -- (1.719,-0.294) -- (1.829,-0.205) -- (1.930,-0.107) -- cycle;
\draw[hl, dashed] (-1.4,0.2) circle (0.75);
\draw[hl, dashed] (-0.5,0.75) circle (0.7);
\draw[hl, dashed] (-0.4,-0.55) circle (0.75);
\draw[hl, dashed] (0.6,0.35) circle (0.8);
\draw[hl, dashed] (1.5,0.3) circle (0.7);
\draw[hl, dashed] (0.9,-0.7) circle (0.65);
\draw[faint, dashed] (-1.0,1.2) circle (0.3);
\draw[faint, dashed] (1.9,-0.9) circle (0.35);
\draw[faint, dashed] (0.1,1.3) circle (0.3);
\end{tikzpicture}
\end{center}
```

A compact space: from any open cover, finitely many sets (orange) already cover it; the rest of the cover (grey) can be dropped.

:::

::: {#exm-compact-spaces .example name="Compact and not"}

1. Every finite space is compact, and so is every space with finitely many open sets (for instance an indiscrete space).
2. $[a,b]$ is compact by @thm-heine-borel-interval.
3. $\mathbb R$ is not compact: the cover by the intervals $(-n,n)$ has no finite subcover. Nor is $(0,1]$: the cover by $(\frac1n,1]$ has none.
4. An infinite discrete space is not compact: the singletons are an open cover with no proper subcover.

:::

::: {#prp-compact-closed-subsets .proposition name="Closed subsets and compact subsets"}

1. A closed subset of a compact space is compact.
2. A compact subset of a Hausdorff space is closed.

:::

::: {.proof}

1. Let $C\subseteq X$ be closed and $\{U_\alpha\}$ a cover of $C$ by open sets of $X$. Adding the open set $X\setminus C$ gives an open cover of $X$; take a finite subcover. Dropping $X\setminus C$, which contains no point of $C$, leaves finitely many $U_\alpha$ covering $C$.

2. Let $K\subseteq X$ be compact and $x\notin K$. For each $y\in K$ choose disjoint open $U_y\ni x$ and $V_y\ni y$. The $V_y$ cover $K$; take $V_{y_1},\dots,V_{y_n}$ covering $K$. Then $U=U_{y_1}\cap\dots\cap U_{y_n}$ is an open neighbourhood of $x$ missing $V_{y_1}\cup\dots\cup V_{y_n}\supseteq K$. So $X\setminus K$ is open.

:::

::: {#prp-continuous-image-compact-topological .proposition name="Continuous images of compact spaces are compact" generalizes="thm-continuous-image-compact"}

If $X$ is compact and $f:X\to Y$ is continuous, then $f(X)$ is compact. In particular a continuous $f:X\to\mathbb R$ on a non-empty compact space is bounded and attains its maximum and minimum.

:::

::: {.proof}

1. Let $\{V_\alpha\}$ cover $f(X)$ by open sets of $Y$. The sets $f^{-1}(V_\alpha)$ form an open cover of $X$; finitely many, $f^{-1}(V_{\alpha_1}),\dots,f^{-1}(V_{\alpha_n})$, cover $X$. Then $V_{\alpha_1},\dots,V_{\alpha_n}$ cover $f(X)$.

2. For $Y=\mathbb R$: $f(X)$ is compact, so bounded (the intervals $(-n,n)$ cover it, and finitely many do) and closed (part 2 of @prp-compact-closed-subsets). Its supremum is a limit of points of $f(X)$, hence lies in $f(X)$ (@prp-closure-properties); likewise its infimum.

:::

::: {#prp-compact-hausdorff-homeomorphism .proposition name="Continuous bijections from compact to Hausdorff spaces"}

A continuous bijection $f:X\to Y$ from a compact space to a Hausdorff space is a homeomorphism.

:::

::: {.proof}

1. We show $f^{-1}$ is continuous: for closed $C\subseteq X$, $(f^{-1})^{-1}(C)=f(C)$ must be closed in $Y$.

2. $C$ is compact (@prp-compact-closed-subsets, part 1), so $f(C)$ is compact (@prp-continuous-image-compact-topological), so $f(C)$ is closed in the Hausdorff space $Y$ (@prp-compact-closed-subsets, part 2).

:::

This finishes the circle in @exm-quotient-spaces: $[0,1]/{\sim}$ is compact as the image of $[0,1]$ under the continuous $q$, and $S^1$ is Hausdorff. In @exm-homeomorphisms, $[0,1)$ is not compact, which is why the same map failed there.

## Products and the Heine–Borel theorem

::: {#thm-product-compact .theorem name="Products of compact spaces are compact"}

If $X$ and $Y$ are compact, so is $X\times Y$ with the product topology.

:::

::: {.proof}

1. Let $\mathcal U$ be an open cover of $X\times Y$. Each point $(x,y)$ lies in some member of $\mathcal U$, hence in an open box $A\times B$ contained in that member. It suffices to cover $X\times Y$ by finitely many such boxes, since each lies in one member of $\mathcal U$.

2. *One slice.* Fix $x\in X$. The boxes $A\times B$ (each inside a member of $\mathcal U$) with $x\in A$ cover $\{x\}\times Y$, and $\{x\}\times Y\cong Y$ is compact. So finitely many, $A_1\times B_1,\dots,A_k\times B_k$, cover it. Let $W_x=A_1\cap\dots\cap A_k$, an open neighbourhood of $x$. Then these $k$ boxes cover the whole *tube* $W_x\times Y$: a point $(x',y)$ with $x'\in W_x$ has $y\in B_i$ for some $i$, and $x'\in A_i$.

3. *All slices.* The sets $W_x$ cover the compact space $X$; finitely many, $W_{x_1},\dots,W_{x_m}$, suffice. The corresponding tubes cover $X\times Y$, and each is covered by finitely many boxes. So finitely many boxes cover $X\times Y$.

:::

::: {#fig-compact-spaces-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.4,0) node[lab, right] {$X$}; \draw[->, faint] (0,-0.2) -- (0,2.8) node[lab, above] {$Y$};
\draw[emph] (0.3,0.3) rectangle (4.0,2.4);
\fill[tintA] (1.6,0.3) rectangle (2.4,2.4); \draw[faint, dashed] (1.6,0.3) -- (1.6,2.4); \draw[faint, dashed] (2.4,0.3) -- (2.4,2.4);
\draw[hl] (2.0,0.3) -- (2.0,2.4); \node[lab, below] at (2.0,0.25) {$x$}; \node[lab, below] at (1.6,-0.05) {$U$};
\foreach \y/\h in {0.3/0.7, 0.9/0.8, 1.6/0.8} {\draw[faint] (1.75,\y) rectangle (2.25,\y+\h);}
\end{tikzpicture}
\end{center}
```

Tube lemma: the slice $\{x\}\times Y$ (orange) is compact, so finitely many basic boxes cover it, and their common $X$-part $U$ gives a tube $U\times Y$ covered by finitely many sets. Finitely many tubes then cover $X\times Y$.

:::

::: {#thm-heine-borel-rn-compact .theorem name="Heine–Borel theorem in $\mathbb R^n$" generalizes="thm-heine-borel-interval"}

A subset of $\mathbb R^n$ is compact if and only if it is closed and bounded.

:::

::: {.proof}

1. *Compact implies closed and bounded.* $\mathbb R^n$ is a metric space, hence Hausdorff, so a compact $K$ is closed (@prp-compact-closed-subsets). The open balls $B_N(0)$, $N=1,2,\dots$, cover $K$; finitely many do, so $K$ lies in one of them.

2. *Closed and bounded implies compact.* A bounded $K$ lies in a cube $[-N,N]^n$. By @thm-heine-borel-interval and @thm-product-compact applied $n-1$ times, the cube is compact in the product topology, which is the topology of $\mathbb R^n$ (@prp-product-topology-properties). $K$ is closed in the cube, so compact by @prp-compact-closed-subsets.

:::

## Compactness in metric spaces

::: {#lem-lebesgue-number .lemma name="Lebesgue number lemma"}

Let $X$ be a sequentially compact metric space and $\mathcal U$ an open cover. Then there is $\delta>0$ such that every ball $B_\delta(x)$ lies inside some member of $\mathcal U$.

:::

::: {.proof}

1. Suppose not. Then for each $n$ there is $x_n$ such that $B_{1/n}(x_n)$ lies in no member of $\mathcal U$.

2. A subsequence converges, $x_{n_k}\to x$. Choose $U\in\mathcal U$ containing $x$ and $\varepsilon>0$ with $B_\varepsilon(x)\subseteq U$.

3. Take $k$ with $\frac1{n_k}<\frac\varepsilon2$ and $d(x_{n_k},x)<\frac\varepsilon2$. By the triangle inequality $B_{1/n_k}(x_{n_k})\subseteq B_\varepsilon(x)\subseteq U$, contradicting step 1.

:::

::: {#fig-compact-spaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (2.014,0.000) -- (2.071,0.115) -- (2.091,0.234) -- (2.070,0.354) -- (2.004,0.469) -- (1.892,0.575) -- (1.741,0.666) -- (1.558,0.738) -- (1.353,0.791) -- (1.137,0.824) -- (0.922,0.840) -- (0.713,0.843) -- (0.517,0.838) -- (0.335,0.830) -- (0.164,0.823) -- (0.000,0.820) -- (-0.164,0.823) -- (-0.335,0.830) -- (-0.517,0.838) -- (-0.713,0.843) -- (-0.921,0.840) -- (-1.137,0.824) -- (-1.353,0.791) -- (-1.558,0.738) -- (-1.741,0.666) -- (-1.892,0.575) -- (-2.004,0.469) -- (-2.070,0.354) -- (-2.091,0.234) -- (-2.071,0.115) -- (-2.014,0.000) -- (-1.930,-0.107) -- (-1.829,-0.205) -- (-1.719,-0.294) -- (-1.607,-0.377) -- (-1.497,-0.455) -- (-1.390,-0.532) -- (-1.284,-0.608) -- (-1.174,-0.686) -- (-1.055,-0.764) -- (-0.922,-0.840) -- (-0.770,-0.911) -- (-0.600,-0.972) -- (-0.412,-1.019) -- (-0.210,-1.050) -- (-0.000,-1.060) -- (0.210,-1.050) -- (0.412,-1.019) -- (0.600,-0.972) -- (0.770,-0.911) -- (0.922,-0.840) -- (1.055,-0.764) -- (1.174,-0.686) -- (1.284,-0.608) -- (1.390,-0.532) -- (1.497,-0.455) -- (1.607,-0.377) -- (1.719,-0.294) -- (1.829,-0.205) -- (1.930,-0.107) -- cycle;
\draw[emph] (2.014,0.000) -- (2.071,0.115) -- (2.091,0.234) -- (2.070,0.354) -- (2.004,0.469) -- (1.892,0.575) -- (1.741,0.666) -- (1.558,0.738) -- (1.353,0.791) -- (1.137,0.824) -- (0.922,0.840) -- (0.713,0.843) -- (0.517,0.838) -- (0.335,0.830) -- (0.164,0.823) -- (0.000,0.820) -- (-0.164,0.823) -- (-0.335,0.830) -- (-0.517,0.838) -- (-0.713,0.843) -- (-0.921,0.840) -- (-1.137,0.824) -- (-1.353,0.791) -- (-1.558,0.738) -- (-1.741,0.666) -- (-1.892,0.575) -- (-2.004,0.469) -- (-2.070,0.354) -- (-2.091,0.234) -- (-2.071,0.115) -- (-2.014,0.000) -- (-1.930,-0.107) -- (-1.829,-0.205) -- (-1.719,-0.294) -- (-1.607,-0.377) -- (-1.497,-0.455) -- (-1.390,-0.532) -- (-1.284,-0.608) -- (-1.174,-0.686) -- (-1.055,-0.764) -- (-0.922,-0.840) -- (-0.770,-0.911) -- (-0.600,-0.972) -- (-0.412,-1.019) -- (-0.210,-1.050) -- (-0.000,-1.060) -- (0.210,-1.050) -- (0.412,-1.019) -- (0.600,-0.972) -- (0.770,-0.911) -- (0.922,-0.840) -- (1.055,-0.764) -- (1.174,-0.686) -- (1.284,-0.608) -- (1.390,-0.532) -- (1.497,-0.455) -- (1.607,-0.377) -- (1.719,-0.294) -- (1.829,-0.205) -- (1.930,-0.107) -- cycle;
\draw[faint, dashed] (-1.4,0.2) circle (0.75);
\draw[faint, dashed] (-0.5,0.75) circle (0.7);
\draw[faint, dashed] (-0.4,-0.55) circle (0.75);
\draw[faint, dashed] (0.6,0.35) circle (0.8);
\draw[faint, dashed] (1.5,0.3) circle (0.7);
\draw[faint, dashed] (0.9,-0.7) circle (0.65);
\draw[regionB] (0.5,0.25) circle (0.32); \node[dot] at (0.5,0.25) {}; \node[lab, right] at (2.3,0.9) {every $\delta$-ball lies in one set};
\end{tikzpicture}
\end{center}
```

Lebesgue number: for an open cover of a compact metric space there is $\delta>0$ such that each ball of radius $\delta$ (orange) lies inside a single set of the cover.

:::

::: {#thm-compact-iff-sequentially-compact .theorem name="Compact and sequentially compact agree for metric spaces"}

A metric space is compact if and only if it is sequentially compact (@def-sequentially-compact).

:::

::: {.proof}

1. *Compact implies sequentially compact.* Let $(x_n)$ have no convergent subsequence. Then no point $y$ is the limit of a subsequence, so some ball $B_{r_y}(y)$ contains $x_n$ for only finitely many $n$ (otherwise, choosing $x_{n_k}\in B_{1/k}(y)$ with $n_k$ increasing gives a subsequence converging to $y$). These balls cover $X$; finitely many cover $X$, and together they contain $x_n$ for only finitely many $n$, which is absurd.

2. *Sequentially compact implies compact.* Let $\mathcal U$ be an open cover and $\delta$ a Lebesgue number (@lem-lebesgue-number). $X$ is totally bounded (@thm-compact-iff-complete-totally-bounded), so finitely many balls $B_\delta(x_1),\dots,B_\delta(x_m)$ cover $X$. Each lies in some $U_i\in\mathcal U$, and $U_1,\dots,U_m$ cover $X$.

:::

So for metric spaces the results of @sec-math-analysis-metric-spaces-compact-metric-spaces and of this note apply to the same spaces: compact metric spaces are complete and totally bounded, continuous real functions on them attain their bounds and are uniformly continuous.
