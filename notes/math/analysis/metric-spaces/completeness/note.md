---
title: "Completeness"
sources: [camib-at-a4, camib-at-a5, camib-at-m4]
requires: [math/analysis/metric-spaces/normed-spaces, math/analysis/metric-spaces/open-and-closed-sets, math/analysis/real/uniform-convergence/uniform-convergence]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Sections 4.2 and 5.3, and Metric and Topological Spaces (Easter 2015 lecture notes), Section 4.4, in our own wording; the sources are merged into one block per item; examples ours; proofs written out in steps. -->

A Cauchy sequence is one whose terms get close to each other. In $\mathbb R$ every Cauchy sequence converges (@thm-general-principle-of-convergence); spaces with this property are called complete, and they are where limits can be produced without knowing them in advance.

::: {#def-cauchy-sequence-metric .definition name="Cauchy sequence, complete space" generalizes="def-cauchy-sequence"}

A sequence $(x_n)$ in a metric space $(X,d)$ is *Cauchy* if
$$\forall\varepsilon>0\ \exists N\ \forall m,n\ge N\quad d(x_m,x_n)<\varepsilon.$$
$X$ is *complete* if every Cauchy sequence in $X$ converges to a point of $X$. A complete normed space is a *Banach space*.

:::

::: {#prp-cauchy-sequences-metric .proposition name="Basic facts about Cauchy sequences"}

In a metric space:

1. every convergent sequence is Cauchy;
2. every Cauchy sequence is bounded (it lies in some ball);
3. a Cauchy sequence with a convergent subsequence converges, to the same limit.

:::

::: {.proof}

1. If $x_n\to x$, take $N$ with $d(x_n,x)<\frac\varepsilon2$ for $n\ge N$; then $d(x_m,x_n)\le d(x_m,x)+d(x,x_n)<\varepsilon$ for $m,n\ge N$.

2. Take $N$ for $\varepsilon=1$. Every $x_n$ lies in the ball about $x_N$ of radius $1+\max_{n<N}d(x_n,x_N)$.

3. Let $x_{n_k}\to x$ and $\varepsilon>0$. Take $N$ with $d(x_m,x_n)<\frac\varepsilon2$ for $m,n\ge N$, and $k$ with $n_k\ge N$ and $d(x_{n_k},x)<\frac\varepsilon2$. Then for $n\ge N$, $d(x_n,x)\le d(x_n,x_{n_k})+d(x_{n_k},x)<\varepsilon$.

:::

::: {#exm-incomplete-spaces .example name="Incomplete spaces"}

1. $(0,1)$ with the usual metric: $x_n=\frac1n$ is Cauchy but its limit $0$ is not in the space.
2. $\mathbb Q$: the decimal truncations $1,\ 1.4,\ 1.41,\dots$ of $\sqrt2$ form a Cauchy sequence with no rational limit.
3. $C[0,1]$ with $\|\cdot\|_1$: let $f_n$ be $0$ on $[0,\frac12]$, rise linearly to $1$ on $[\frac12,\frac12+\frac1n]$, and be $1$ after. For $m,n\ge N$, $f_m$ and $f_n$ differ only on $[\frac12,\frac12+\frac1N]$, by at most $1$, so $\|f_m-f_n\|_1\le\frac1N$. A limit $f$ would have to be $0$ on $[0,\frac12)$ and $1$ on $(\frac12,1]$, which no continuous function is.

Completeness is not a topological property: $x\mapsto\tan(\pi(x-\frac12))$ is a continuous bijection $(0,1)\to\mathbb R$ with continuous inverse, so the two spaces are homeomorphic (@def-homeomorphism), yet only $\mathbb R$ is complete.

:::

::: {#thm-rn-complete .theorem name="Finite-dimensional normed spaces are complete" generalizes="thm-general-principle-of-convergence"}

$\mathbb R^n$ is complete in any norm, and so is every finite-dimensional normed space.

:::

::: {.proof}

1. By @thm-norms-equivalent-finite-dimension all norms on a finite-dimensional space are Lipschitz equivalent, and Lipschitz equivalent norms have the same Cauchy sequences and the same convergent sequences. So it suffices to treat $\mathbb R^n$ with $\|\cdot\|_2$ (via a basis).

2. Let $(x^{(k)})$ be Cauchy in $\mathbb R^n$. Since $|x^{(k)}_i-x^{(l)}_i|\le\|x^{(k)}-x^{(l)}\|_2$, each coordinate sequence is Cauchy in $\mathbb R$, hence converges by @thm-general-principle-of-convergence.

3. By @prp-convergence-coordinatewise, $(x^{(k)})$ converges in $\mathbb R^n$.

:::

::: {#thm-closed-subspace-complete .theorem name="Complete subspaces"}

Let $Y$ be a subspace of a metric space $X$.

1. If $Y$ is complete, then $Y$ is closed in $X$.
2. If $X$ is complete and $Y$ is closed in $X$, then $Y$ is complete.

:::

::: {.proof}

1. Let $y_n\in Y$ converge to $x\in X$. The sequence is Cauchy (@prp-cauchy-sequences-metric), so it converges in $Y$ to some $y$; by uniqueness of limits in $X$ (@prp-limit-unique-metric), $x=y\in Y$. By @prp-closed-iff-complement-open, $Y$ is closed.

2. A Cauchy sequence in $Y$ is Cauchy in $X$, so it converges in $X$; its limit lies in $Y$ because $Y$ is closed.

:::

So a subset of $\mathbb R^n$ is complete exactly when it is closed.

## Spaces of functions

::: {#thm-bounded-functions-complete .theorem name="The uniform norm is complete"}

Let $E$ be a set and $B(E;\mathbb R^m)$ the vector space of bounded functions $E\to\mathbb R^m$, with $\|f\|_\infty=\sup_{x\in E}\|f(x)\|_2$. Then $B(E;\mathbb R^m)$ is complete. If $E$ is a metric space, the bounded continuous functions form a closed subspace, hence are complete as well; in particular $C([a,b];\mathbb R^m)$ with $\|\cdot\|_\infty$ is a Banach space.

:::

::: {.proof}

1. *Pointwise limit.* Let $(f_n)$ be Cauchy in $\|\cdot\|_\infty$. For each $x$, $\|f_n(x)-f_k(x)\|_2\le\|f_n-f_k\|_\infty$, so $(f_n(x))$ is Cauchy in $\mathbb R^m$ and converges by @thm-rn-complete. Call the limit $f(x)$.

2. *Uniform convergence.* Given $\varepsilon>0$, take $N$ with $\|f_n-f_k\|_\infty<\varepsilon$ for $n,k\ge N$. For fixed $n\ge N$ and $x$, let $k\to\infty$: $\|f_n(x)-f(x)\|_2\le\varepsilon$. So $\sup_x\|f_n(x)-f(x)\|_2\le\varepsilon$ for $n\ge N$.

3. *$f$ is bounded*, since $\|f(x)\|_2\le\|f_N(x)\|_2+\varepsilon$ for all $x$. So $f\in B(E;\mathbb R^m)$ and $\|f_n-f\|_\infty\to0$.

4. *Continuity is preserved.* If $E$ is a metric space and all $f_n$ are continuous, $f$ is continuous by the proof of @thm-uniform-limit-continuous with $|\cdot|$ replaced by $d_E$ and $\|\cdot\|_2$. So the continuous functions form a closed subset, complete by @thm-closed-subspace-complete. For compact $E=[a,b]$ every continuous function is bounded (@thm-extreme-value-proof applied to $\|f\|_2$), so this subspace is all of $C([a,b];\mathbb R^m)$.

:::

For $m=1$ this is the general principle of uniform convergence (@thm-uniform-cauchy-criterion) restated: a space of functions with the uniform norm is complete. With the integral norm it is not (@exm-incomplete-spaces).
