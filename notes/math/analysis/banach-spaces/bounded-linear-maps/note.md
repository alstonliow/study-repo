---
title: "Banach Spaces, Bounded Linear Maps and the Dual Space"
sources: [camii-lan-1]
requires: [math/analysis/metric-spaces/continuous-maps]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Sections 1.1-1.5, in our own wording; proofs written out in steps. The remarks on topological vector spaces (Minkowski functional) in the lecture notes are not written out here. -->

In finite dimensions every linear map is continuous and every norm is complete. In infinite dimensions neither is automatic, so the objects of study are complete normed spaces and the linear maps that respect the norm.

::: {#def-banach-space .definition name="Banach space"}

A normed space $(X,\|\cdot\|)$ is a *Banach space* if it is complete as a metric space for $d(x,y)=\|x-y\|$: every Cauchy sequence converges.

:::

::: {#exm-banach-spaces .example name="Banach spaces"}

Finite-dimensional normed spaces are Banach (@thm-rn-complete). For a set $S$, the bounded functions with the sup norm are Banach (@thm-bounded-functions-complete); for a compact Hausdorff space $K$, $C(K)$ is a closed subspace of the bounded functions, hence Banach. On the other hand, the space of continuous functions on $[0,1]$ with the norm $\|f\|_1=\int_0^1|f|$ is a normed space that is **not** complete: a sequence of continuous functions can converge in $L^1$ to a step function.

:::

::: {#def-bounded-linear-map .definition name="Bounded linear map, operator norm"}

Let $X,Y$ be normed spaces. A linear map $T:X\to Y$ is *bounded* if there is $C\ge0$ with $\|Tx\|\le C\|x\|$ for all $x\in X$. The set of bounded linear maps is $B(X,Y)$, and $B(X)=B(X,X)$. The *operator norm* is
$$\|T\|=\sup_{\|x\|\le1}\|Tx\|=\sup_{x\ne0}\frac{\|Tx\|}{\|x\|},$$
the least $C$ that works, so that $\|Tx\|\le\|T\|\,\|x\|$.

:::

::: {#fig-bounded-linear-maps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,0) circle (0.9); \node[lab] at (0,0) {$B_X(1)$};
\draw[faint] (5,0) ellipse (1.8 and 1.0); \node[lab] at (5,-1.3) {$B_Y(\|T\|)$};
\draw[hl] (5,0.1) ellipse (1.2 and 0.6); \node[lab] at (5,0.1) {$T(B_X(1))$};
\draw[map] (1.1,0) -- (3.0,0); \node[lab, above] at (2.05,0) {$T$};
\end{tikzpicture}
\end{center}
```

A bounded operator maps the unit ball into the ball of radius $\|T\|$.

:::

::: {#prp-bounded-iff-continuous .proposition name="Bounded means continuous"}

For a linear map $T:X\to Y$ between normed spaces, the following are equivalent: (i) $T$ is continuous; (ii) $T$ is continuous at $0$; (iii) $T$ is bounded.

:::

::: {.proof}

1. (i) $\Rightarrow$ (ii) is trivial.

2. (ii) $\Rightarrow$ (iii). The set $T^{-1}(B_Y(1))$ is a neighbourhood of $0$, so it contains a ball $B_X(\varepsilon)$. Then $\|x\|<\varepsilon$ implies $\|Tx\|<1$. By linearity, $\|Tx\|\le\varepsilon^{-1}\|x\|$ for every $x$.

3. (iii) $\Rightarrow$ (i). If $\|Tx\|\le C\|x\|$ then $\|Tx-Ty\|=\|T(x-y)\|\le C\|x-y\|$, so $T$ is Lipschitz.

:::

::: {#thm-operator-space-complete .theorem name="Completeness of $B(X,Y)$"}

$B(X,Y)$ with the operator norm is a normed space, and it is a Banach space whenever $Y$ is a Banach space.

:::

::: {.proof}

1. That $\|\cdot\|$ is a norm on $B(X,Y)$ is routine: $\|T\|=0$ forces $Tx=0$ for all $x$, and the triangle inequality is inherited from $Y$.

2. Let $(T_n)$ be Cauchy in $B(X,Y)$. For each $x$, $\|T_nx-T_mx\|\le\|T_n-T_m\|\|x\|$, so $(T_nx)$ is Cauchy in $Y$ and converges, say to $Tx$. The map $T$ is linear, being a pointwise limit of linear maps.

3. *$T$ is bounded.* A Cauchy sequence is bounded, so $\|T_n\|\le M$ for all $n$. Then $\|Tx\|=\lim\|T_nx\|\le M\|x\|$.

4. *$T_n\to T$ in norm.* Given $\varepsilon>0$ choose $N$ with $\|T_n-T_m\|<\varepsilon$ for $n,m\ge N$. For $\|x\|\le1$ and $n\ge N$, letting $m\to\infty$ in $\|T_nx-T_mx\|<\varepsilon$ gives $\|T_nx-Tx\|\le\varepsilon$. Taking the supremum over $x$, $\|T_n-T\|\le\varepsilon$.

:::

::: {#def-continuous-dual .definition name="Dual space of a normed space"}

For a normed space $X$ over $\mathbb F\in\{\mathbb R,\mathbb C\}$, the *dual space* is $X^*=B(X,\mathbb F)$, whose elements are the *bounded (continuous) functionals*. The algebraic dual of @def-dual-space consists of all linear functionals, bounded or not.

:::

::: {#cor-dual-banach .corollary name="The dual is always Banach"}

For every normed space $X$ (complete or not), $X^*$ is a Banach space.

:::

::: {.proof}

Apply @thm-operator-space-complete with $Y=\mathbb F$, which is complete.

:::

::: {#def-dual-operator .definition name="Adjoint (dual operator) of a bounded map"}

For $T\in B(X,Y)$, the *adjoint* is $T^*:Y^*\to X^*$, $T^*g=g\circ T$. It is linear, and bounded with $\|T^*\|\le\|T\|$.

:::

::: {.proof}

1. $g\circ T$ is linear and $|g(Tx)|\le\|g\|\|T\|\|x\|$, so $\|T^*g\|\le\|T\|\|g\|$ and $T^*g\in X^*$.

2. Linearity of $g\mapsto g\circ T$ is clear, and step 1 gives $\|T^*\|\le\|T\|$.

:::

::: {#rmk-bounded-linear-maps-1 .remark name="Equality of norms"}

In fact $\|T^*\|=\|T\|$, but this needs the Hahn–Banach theorem (@sec-math-analysis-banach-spaces-double-dual). For finite-dimensional spaces $T^*$ is the transpose, as in the algebraic dual map of @def-dual-map.

:::

::: {#def-normed-isomorphism .definition name="Isomorphism of normed spaces"}

$T\in B(X,Y)$ is an *isomorphism* if it is bijective with $T^{-1}\in B(Y,X)$, i.e. a linear homeomorphism; it is an *isometric isomorphism* if moreover $\|Tx\|=\|x\|$. Two norms on a vector space are equivalent exactly when the identity is an isomorphism. In finite dimensions all norms are equivalent (@thm-norms-equivalent-finite-dimension), so an $n$-dimensional normed space is isomorphic to $\mathbb F^n$ and its dual is again $n$-dimensional; in infinite dimensions the dual can look quite different from the space (@sec-math-analysis-banach-spaces-sequence-spaces).

:::
