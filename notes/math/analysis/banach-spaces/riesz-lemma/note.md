---
title: "Riesz's Lemma and Compactness of the Unit Ball"
sources: [camii-lan-1, camii-lans-2]
requires: [math/analysis/banach-spaces/bounded-linear-maps]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 1.6, and Example Sheet 2 (question 4), in our own wording; proofs written out in steps. All norms on a finite-dimensional space being equivalent is not repeated (see math/analysis/metric-spaces/normed-spaces). -->

Finite-dimensional normed spaces behave like $\mathbb R^n$: closed bounded sets are compact. This note shows that the converse holds, so compactness of the unit ball characterises finite dimension.

::: {#prp-finite-dim-complete-closed .proposition name="Finite-dimensional subspaces are complete and closed"}

Every finite-dimensional normed space is complete, and every finite-dimensional subspace $Y$ of a normed space $X$ is closed. Every linear map from a finite-dimensional normed space to a normed space is continuous.

:::

::: {.proof}

1. By @thm-norms-equivalent-finite-dimension a norm on an $n$-dimensional space is equivalent to the Euclidean norm of the coordinates; the Euclidean space $\mathbb F^n$ is complete (@thm-rn-complete), and completeness is preserved by equivalent norms.

2. A complete subspace of a metric space is closed (@thm-closed-subspace-complete), giving closedness of $Y$.

3. If $T:V\to W$ is linear and $V$ has a basis $v_1,\dots,v_n$, then $\|T\sum a_iv_i\|\le\max_i\|Tv_i\|\sum|a_i|\le C\|\sum a_iv_i\|$ because $\sum|a_i|$ is an equivalent norm on $V$.

:::

::: {#lem-riesz .lemma name="Riesz's lemma"}

Let $Y$ be a proper closed subspace of a normed space $X$ and let $\theta\in(0,1)$. Then there is $x\in X$ with $\|x\|=1$ and $\operatorname{dist}(x,Y)\ge\theta$.

:::

::: {.proof}

1. Pick $z\in X\setminus Y$. Since $Y$ is closed, $d=\operatorname{dist}(z,Y)>0$.

2. Since $\theta<1$ we have $d/\theta>d$, so there is $y_0\in Y$ with $\|z-y_0\|\le d/\theta$.

3. Put $x=(z-y_0)/\|z-y_0\|$. For $y\in Y$,
$$\|x-y\|=\frac{\|z-y_0-\|z-y_0\|y\|}{\|z-y_0\|}\ge\frac{d}{\|z-y_0\|}\ge\theta,$$
because $y_0+\|z-y_0\|y\in Y$ and so is at distance at least $d$ from $z$.

:::

::: {#fig-riesz-lemma-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) circle (1.6);
\draw[emph] (-2.6,-0.8) -- (2.6,0.8) node[lab, right] {$Y$};
\node[hl dot] at (-0.55,1.5) {}; \node[lab, above] at (-0.55,1.5) {$x$};
\draw[hl] (-0.55,1.5) -- (-0.1,-0.03); \node[lab, left] at (-0.45,0.8) {$\ge\theta$};
\end{tikzpicture}
\end{center}
```

Riesz's lemma: a unit vector $x$ at distance at least $\theta$ from the closed subspace $Y$.

:::

::: {#thm-unit-ball-compact .theorem name="Compact unit ball characterises finite dimension"}

For a normed space $X$ the following are equivalent: (i) $X$ is finite-dimensional; (ii) the closed unit ball is compact; (iii) every bounded sequence has a convergent subsequence.

:::

::: {.proof}

1. (i) $\Rightarrow$ (ii). $X\cong\mathbb F^n$ by an isomorphism, and the closed unit ball is closed and bounded, hence compact by Heine–Borel (@thm-heine-borel-rn); homeomorphisms preserve compactness.

2. (ii) $\Leftrightarrow$ (iii) is sequential compactness of the ball (@thm-compact-iff-sequentially-compact), scaled.

3. (iii) $\Rightarrow$ (i). Suppose $X$ is infinite-dimensional. Pick $x_1$ with $\|x_1\|=1$. Given $x_1,\dots,x_n$ let $Y_n=\operatorname{span}(x_1,\dots,x_n)$, a proper closed subspace (@prp-finite-dim-complete-closed). By @lem-riesz with $\theta=\tfrac12$ choose $x_{n+1}$ of norm $1$ with $\operatorname{dist}(x_{n+1},Y_n)\ge\tfrac12$.

4. Then $\|x_m-x_n\|\ge\tfrac12$ for $m>n$, so $(x_n)$ is a bounded sequence with no Cauchy subsequence, contradicting (iii).

:::

::: {#exm-riesz-no-convergent .example name="Orthonormal vectors give a sequence with no convergent subsequence"}

In $\ell^p$ the unit vectors $e_n$ satisfy $\|e_m-e_n\|_p=2^{1/p}$ for $m\ne n$ and in $c_0$ or $\ell^\infty$ they satisfy $\|e_m-e_n\|=1$. They are in the closed unit ball but have no convergent subsequence, so these balls are not compact.

:::
