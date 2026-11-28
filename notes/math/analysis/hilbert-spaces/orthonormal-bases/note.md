---
title: "Orthonormal Systems, Bessel's Inequality and Hilbert Bases"
sources: [camii-lan-4, camii-lans-4]
requires: [math/analysis/hilbert-spaces/hilbert-spaces, math/analysis/function-spaces/stone-weierstrass]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Sections 4.3 and 4.4, and Example Sheet 4 (question 1), in our own wording; proofs written out in steps. The finite orthonormal case and Parseval are in math/linear-algebra/inner-product-spaces/inner-products. -->

In infinite dimensions "basis" means a maximal orthonormal system, and expansions are infinite series. Every separable Hilbert space then looks like $\ell^2$.

::: {#def-orthonormal-system .definition name="Orthonormal system and Hilbert basis"}

A subset $S$ of an inner product space is an *orthonormal system* if its elements are unit vectors, pairwise orthogonal. It is *maximal* (an *orthonormal basis* or *Hilbert basis* when the space is a Hilbert space) if it is not contained in a strictly larger orthonormal system.

:::

::: {#lem-bessel .lemma name="Bessel's inequality"}

Let $(e_n)$ be an orthonormal sequence in an inner product space. Then $\sum_n|\langle x,e_n\rangle|^2\le\|x\|^2$ for every $x$.

:::

::: {.proof}

1. For $N\ge1$ let $x_N=\sum_{n\le N}\langle x,e_n\rangle e_n$. Then $x-x_N\perp e_n$ for $n\le N$, so $x-x_N\perp x_N$.

2. By Pythagoras $\|x\|^2=\|x-x_N\|^2+\|x_N\|^2\ge\sum_{n\le N}|\langle x,e_n\rangle|^2$.

3. Let $N\to\infty$.

:::

::: {#thm-hilbert-basis-expansion .theorem name="Characterisations of a Hilbert basis"}

Let $(e_n)$ be an orthonormal sequence in a Hilbert space $H$. The following are equivalent: (i) $(e_n)$ is maximal; (ii) $\{e_n\}^\perp=\{0\}$; (iii) the span of the $e_n$ is dense; (iv) $x=\sum_n\langle x,e_n\rangle e_n$ (convergent in norm) for every $x\in H$; (v) Parseval's identity $\|x\|^2=\sum_n|\langle x,e_n\rangle|^2$ for every $x$.

:::

::: {.proof}

1. (i) $\Leftrightarrow$ (ii): if $x\ne0$ is orthogonal to all $e_n$, then $(e_n)\cup\{x/\|x\|\}$ is a larger orthonormal system; conversely a larger one contains a unit vector orthogonal to all $e_n$.

2. (ii) $\Leftrightarrow$ (iii): by @cor-double-perp, $\operatorname{span}\{e_n\}$ is dense iff $\{e_n\}^\perp=0$.

3. (ii) $\Rightarrow$ (iv): by Bessel, $\sum|\langle x,e_n\rangle|^2<\infty$, so the partial sums $x_N$ are Cauchy ($\|x_M-x_N\|^2=\sum_{N<n\le M}|\langle x,e_n\rangle|^2$) and converge to some $y$. By continuity of the inner product $\langle x-y,e_k\rangle=0$ for all $k$, so $x=y$.

4. (iv) $\Rightarrow$ (v): $\|x_N\|^2=\sum_{n\le N}|\langle x,e_n\rangle|^2\to\|x\|^2$ by continuity of the norm.

5. (v) $\Rightarrow$ (ii): if all $\langle x,e_n\rangle=0$ then $\|x\|^2=0$.

:::

::: {#fig-orthonormal-bases-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, emph] (0,0) -- (2,0) node[lab, right] {$e_1$}; \draw[->, emph] (0,0) -- (0,2) node[lab, above] {$e_2$};
\draw[->, hl] (0,0) -- (1.5,1.2) node[lab, right] {$x$};
\draw[faint, dashed] (1.5,0) -- (1.5,1.2) -- (0,1.2);
\node[lab, below] at (1.5,0) {$\langle x,e_1\rangle$}; \node[lab, left] at (0,1.2) {$\langle x,e_2\rangle$};
\end{tikzpicture}
\end{center}
```

Coordinates of $x$ along an orthonormal system; Parseval says the squares add up to $\|x\|^2$.

:::

::: {#thm-separable-hilbert-l2 .theorem name="Separable Hilbert spaces are $\ell^2$"}

A Hilbert space is separable if and only if it has a countable orthonormal basis (finite or infinite). Every infinite-dimensional separable Hilbert space is isometrically isomorphic to $\ell^2$ via $x\mapsto(\langle x,e_n\rangle)_n$.

:::

::: {.proof}

1. If $H$ is separable, take a countable dense set and run Gram–Schmidt (@thm-gram-schmidt-abstract) on the linearly independent subfamily obtained by deleting dependent elements. This produces a countable orthonormal system whose span contains the dense set, so is dense: by @thm-hilbert-basis-expansion it is a basis.

2. Conversely, finite rational (or $\mathbb Q+i\mathbb Q$) combinations of a countable orthonormal basis form a countable set, dense by (iii).

3. For the isomorphism, $U:H\to\ell^2$, $Ux=(\langle x,e_n\rangle)$ is well defined by Bessel, linear, and isometric by Parseval. It is onto: for $a\in\ell^2$ the partial sums of $\sum a_ne_n$ are Cauchy (by Pythagoras) and converge to some $x$ with $Ux=a$.

:::

::: {#exm-orthonormal-bases .example name="Examples of bases"}

(i) In $\ell^2$ the unit vectors $(e_n)$ form an orthonormal basis, and the bilateral version $(e_n)_{n\in\mathbb Z}$ in $\ell^2(\mathbb Z)$.

(ii) In $L^2(S^1)$ with $\langle f,g\rangle=\frac1{2\pi}\int_0^{2\pi}f\bar g$, the functions $e^{ikt}$, $k\in\mathbb Z$, form an orthonormal basis: they are orthonormal, and their span (the trigonometric polynomials) is dense in $C(S^1)$ by the Stone–Weierstrass theorem (@thm-stone-weierstrass-complex), hence dense in $L^2$. So every $f\in L^2$ equals its Fourier series in $L^2$ norm, and $\sum|\hat f(k)|^2=\|f\|^2$.

(iii) Non-separable Hilbert spaces (such as $\ell^2(\mathbb R)$) have uncountable bases; maximal systems exist in general by Zorn's lemma (@lem-zorn).

:::
