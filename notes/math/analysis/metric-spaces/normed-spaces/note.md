---
title: "Normed Spaces and Equivalence of Norms"
sources: [camib-at-a4, camib-at-m1, camii-lans-1]
requires: [math/analysis/metric-spaces/metric-spaces, math/analysis/real/sequences/monotone-sequences, math/linear-algebra/systems/vectors-and-dot-products]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Sections 4.1 and 4.4, and Metric and Topological Spaces (Easter 2015 lecture notes), Section 1.3, in our own wording; the two sources are merged into one block per item; examples ours (checked numerically); proofs written out in steps. -->

On a vector space the natural metrics come from a length function. In finite dimensions every such length gives the same convergent sequences; in infinite dimensions this fails.

::: {#def-norm .definition name="Norm, normed space"}

A *norm* on a real vector space $V$ is a function $\|\cdot\|:V\to\mathbb R$ such that for all $v,w\in V$ and $\lambda\in\mathbb R$:

1. $\|v\|\ge0$, with equality if and only if $v=0$;
2. $\|\lambda v\|=|\lambda|\,\|v\|$;
3. $\|v+w\|\le\|v\|+\|w\|$.

A *normed space* is a vector space with a norm. It is a metric space with $d(v,w)=\|v-w\|$, and all metric notions (convergence, continuity, ...) refer to this metric.

:::

The metric axioms follow from the norm axioms; for the triangle inequality, $\|u-w\|=\|(u-v)+(v-w)\|\le\|u-v\|+\|v-w\|$. Also $\bigl|\|v\|-\|w\|\bigr|\le\|v-w\|$ (apply the triangle inequality to $v=(v-w)+w$ and to $w$), so the norm is a continuous function on $V$.

::: {#exm-norms .example name="Norms"}

1. On $\mathbb R^n$: $\|x\|_1=\sum_i|x_i|$, $\|x\|_2=\bigl(\sum_ix_i^2\bigr)^{1/2}$ and $\|x\|_\infty=\max_i|x_i|$.
2. On $C[a,b]$: the *uniform norm* $\|f\|_\infty=\sup_{[a,b]}|f|$ and $\|f\|_1=\int_a^b|f|$, giving the metrics $d_\infty$ and $d_1$ of @exm-metric-spaces.

For $\|\cdot\|_1$ and $\|\cdot\|_\infty$ all axioms are immediate. For $\|\cdot\|_2$ the triangle inequality is @cor-triangle-inequality-inner-product; more generally it holds for every norm coming from an inner product.

:::

::: {#fig-normed-spaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[->, faint] (-1.8,0) -- (1.9,0); \draw[->, faint] (0,-1.8) -- (0,1.9);
\draw[emph] (1.3,0) -- (0,1.3) -- (-1.3,0) -- (0,-1.3) -- cycle;
\draw[hl] (0,0) circle (1.3);
\draw[faint, dashed] (-1.3,-1.3) rectangle (1.3,1.3);
\node[lab] at (0.45,0.45) {$\lVert x\rVert_1\le1$}; \node[lab, below right] at (0.95,-0.95) {$\lVert x\rVert_2\le1$}; \node[lab, right] at (1.3,1.4) {$\lVert x\rVert_\infty\le1$};
\end{tikzpicture}
\end{center}
```

Unit balls of three norms on $\mathbb R^2$: a diamond for $\lVert\cdot\rVert_1$, the disc for $\lVert\cdot\rVert_2$ (orange) and a square for $\lVert\cdot\rVert_\infty$ (dashed).

:::

::: {#def-inner-product .definition name="Inner product"}

An *inner product* on a real vector space $V$ is a function $\langle\cdot,\cdot\rangle:V\times V\to\mathbb R$ that is linear in each variable, symmetric ($\langle v,w\rangle=\langle w,v\rangle$) and positive definite ($\langle v,v\rangle>0$ for $v\ne0$).

:::

Examples: the dot product on $\mathbb R^n$, and $\langle f,g\rangle=\int_a^bfg$ on $C[a,b]$ (@def-function-inner-product).

::: {#thm-inner-product-norm .theorem name="Cauchy–Schwarz; an inner product gives a norm" related="thm-cauchy-schwarz-inner-product"}

For an inner product, $|\langle v,w\rangle|\le\|v\|\,\|w\|$ where $\|v\|=\sqrt{\langle v,v\rangle}$, and $\|\cdot\|$ is a norm.

:::

::: {.proof}

1. If $w=0$ both sides are $0$. Otherwise, for every $t\in\mathbb R$,
$$0\le\langle v-tw,v-tw\rangle=\|v\|^2-2t\langle v,w\rangle+t^2\|w\|^2.$$

2. Take $t=\frac{\langle v,w\rangle}{\|w\|^2}$: this gives $0\le\|v\|^2-\frac{\langle v,w\rangle^2}{\|w\|^2}$, which is the inequality.

3. Norm axioms 1 and 2 follow from positive definiteness and bilinearity. For the triangle inequality, $\|v+w\|^2=\|v\|^2+2\langle v,w\rangle+\|w\|^2\le\|v\|^2+2\|v\|\|w\|+\|w\|^2=(\|v\|+\|w\|)^2$.

:::

## Equivalent norms

::: {#def-lipschitz-equivalent-norms .definition name="Lipschitz equivalent norms"}

Norms $\|\cdot\|$ and $\|\cdot\|'$ on $V$ are *Lipschitz equivalent* if there are $0<A\le B$ with $A\|v\|\le\|v\|'\le B\|v\|$ for all $v\in V$; that is, their metrics are Lipschitz equivalent (@def-lipschitz-equivalent-metrics).

:::

::: {#fig-normed-spaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.8,0) -- (1.9,0); \draw[->, faint] (0,-1.8) -- (0,1.9);
\draw[emph] (-0.92,-0.92) rectangle (0.92,0.92); \draw[hl] (0,0) circle (1.3); \draw[emph] (-1.3,-1.3) rectangle (1.3,1.3);
\node[lab, right] at (1.35,1.0) {$\lVert x\rVert_\infty\le1$}; \node[lab] at (0.2,0.55) {$\lVert x\rVert_\infty\le\frac1{\sqrt2}$};
\end{tikzpicture}
\end{center}
```

Each unit ball fits inside a scaled copy of the other: $\lVert x\rVert_\infty\le\lVert x\rVert_2\le\sqrt2\,\lVert x\rVert_\infty$ on $\mathbb R^2$. Lipschitz equivalent norms are exactly those whose balls nest like this.

:::

::: {#exm-norms-not-equivalent .example name="Inequivalent norms on $C[0,1]$"}

Let $f_n\in C[0,1]$ be the tent of height $1$ on $[0,\frac2n]$ (zero outside). Then $\|f_n\|_\infty=1$ and $\|f_n\|_1=\frac1n$. So $f_n\to0$ in $\|\cdot\|_1$ but not in $\|\cdot\|_\infty$, and no constant $B$ has $\|f\|_\infty\le B\|f\|_1$ for all $f$. (The other inequality, $\|f\|_1\le\|f\|_\infty$, does hold.)

:::

::: {#fig-normed-spaces-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (3.5,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.0) node[lab, above] {$y$};
\fill[tintA] (0,0) -- (1.500,1.6) -- (3.000,0) -- cycle; \draw[emph] (0,0) -- (1.500,1.6) -- (3.000,0) -- (3.0,0);
\fill[tintB] (0,0) -- (0.500,1.6) -- (1.000,0) -- cycle; \draw[hl] (0,0) -- (0.500,1.6) -- (1.000,0) -- (3.0,0);
\draw[faint] (-0.06,1.600) -- (0.06,1.600); \node[lab, tick, left] at (-0.05,1.600) {$1$};\draw[faint] (3.000,-0.06) -- (3.000,0.06); \node[lab, tick, below] at (3.000,-0.05) {$1$};\node[lab, above] at (1.5,1.6) {$n=2$}; \node[lab, above] at (0.5,1.6) {$n=6$};
\end{tikzpicture}
\end{center}
```

Tents of height $1$ on $[0,\frac2n]$: the sup norm stays $1$ while the area $\lVert f_n\rVert_1=\frac1n$ shrinks, so the two norms are not equivalent on $C[0,1]$.

:::

::: {#prp-convergence-coordinatewise .proposition name="Convergence in $\mathbb R^n$ is coordinatewise"}

A sequence $x^{(k)}\to x$ in $(\mathbb R^n,\|\cdot\|_2)$ if and only if $x^{(k)}_i\to x_i$ in $\mathbb R$ for each coordinate $i=1,\dots,n$.

:::

::: {.proof}

1. For each $i$, $|x^{(k)}_i-x_i|\le\|x^{(k)}-x\|_2$, so convergence in $\mathbb R^n$ gives convergence of each coordinate.

2. Conversely, $\|x^{(k)}-x\|_2\le\sum_{i=1}^n|x^{(k)}_i-x_i|$, a sum of $n$ null sequences, which is null.

:::

::: {#thm-bolzano-weierstrass-rn .theorem name="Bolzano–Weierstrass theorem in $\mathbb R^n$" generalizes="thm-bolzano-weierstrass"}

Every bounded sequence in $(\mathbb R^n,\|\cdot\|_2)$ has a convergent subsequence.

:::

::: {.proof}

1. Let $\|x^{(k)}\|_2\le C$ for all $k$; then every coordinate sequence is bounded by $C$.

2. By @thm-bolzano-weierstrass the first coordinates have a convergent subsequence. Along it, the second coordinates still form a bounded sequence, so a further subsequence makes them converge too; the first coordinates still converge along it.

3. After $n$ such steps we have a subsequence along which every coordinate converges. By @prp-convergence-coordinatewise it converges in $\mathbb R^n$.

:::

::: {#thm-norms-equivalent-finite-dimension .theorem name="All norms on a finite-dimensional space are equivalent"}

Any two norms on a finite-dimensional real vector space are Lipschitz equivalent.

:::

::: {.proof}

1. *Reduce to $\mathbb R^n$.* Lipschitz equivalence is an equivalence relation, so it is enough to show every norm $\|\cdot\|$ is equivalent to one fixed norm. Choosing a basis $e_1,\dots,e_n$ identifies $V$ with $\mathbb R^n$; we compare $\|\cdot\|$ with $\|\cdot\|_2$ on the coordinates.

2. *Upper bound.* For $x=\sum x_ie_i$, by the triangle inequality and @thm-cauchy-schwarz-inner-product,
$$\|x\|\le\sum_i|x_i|\,\|e_i\|\le\Bigl(\sum_i\|e_i\|^2\Bigr)^{1/2}\|x\|_2=B\|x\|_2.$$
In particular $\bigl|\|x\|-\|y\|\bigr|\le\|x-y\|\le B\|x-y\|_2$, so $\|\cdot\|$ is continuous with respect to $\|\cdot\|_2$.

3. *The minimum on the sphere.* Let $S=\{x:\|x\|_2=1\}$ and $m=\inf_S\|x\|$. Take $x^{(k)}\in S$ with $\|x^{(k)}\|\to m$. By @thm-bolzano-weierstrass-rn a subsequence converges in $\|\cdot\|_2$ to some $x$, and $\|x\|_2=1$ because $\|\cdot\|_2$ is continuous. By step 2, $\|x\|=m$. Since $x\ne0$, $m>0$.

4. *Lower bound.* For $x\ne0$, $\frac x{\|x\|_2}\in S$, so $\bigl\|\frac x{\|x\|_2}\bigr\|\ge m$, that is, $\|x\|\ge m\|x\|_2$.

5. So $m\|x\|_2\le\|x\|\le B\|x\|_2$ for all $x$.

:::

Consequently, in a finite-dimensional space the convergent sequences, the continuous maps, the bounded sets, and (later) the open sets, complete spaces and compact sets are the same for every norm. On $\mathbb R^n$ we may use whichever norm is convenient.
