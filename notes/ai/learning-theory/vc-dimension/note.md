---
title: "VC Dimension"
sources: [cs229-8]
requires: [ai/learning-theory/empirical-risk-minimization, ai/machine-learning/linear-classification]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 8.3.3 (the case of infinite H: shattering, VC dimension, Vapnik's uniform convergence theorem and its sample complexity corollary), in our own wording. The proof that halfspaces in R^d have VC dimension d+1 (with Radon's lemma) is our own; Vapnik's theorem is stated without proof, as in the source. Proofs written out in steps. -->

The bound of @cor-erm-finite needs a finite class. Linear classifiers form an infinite class, yet on any finite data set they can produce only finitely many labellings. The VC dimension measures how rich those labellings can be.

::: {#def-vc-dimension .definition name="Shattering, VC dimension"}

A hypothesis class $\mathcal H$ of functions $\mathcal X\to\{0,1\}$ *shatters* a finite set $T=\{\mathbf{x}^{(1)},\dots,\mathbf{x}^{(m)}\}\subseteq\mathcal X$ if every one of the $2^m$ labellings of $T$ is produced by some $h\in\mathcal H$. The *Vapnik–Chervonenkis dimension* $\operatorname{VC}(\mathcal H)$ is the size of the largest set that $\mathcal H$ shatters ($\infty$ if arbitrarily large sets are shattered).

To show $\operatorname{VC}(\mathcal H)\ge m$ it is enough to find *one* set of $m$ points that is shattered; to show $\operatorname{VC}(\mathcal H)<m$ one must show that *no* set of $m$ points is shattered.

:::

::: {#exm-vc-dimension-intervals .example name="Thresholds and intervals on the line"}

1. The thresholds $h_a(x)=\mathbf 1\{x\ge a\}$ shatter any single point but no pair $x_1<x_2$: the labelling $(1,0)$ would need $x_1\ge a>x_2$. So their VC dimension is $1$.
2. The intervals $h_{a,b}(x)=\mathbf 1\{a\le x\le b\}$ shatter any two distinct points but no three $x_1<x_2<x_3$: the labelling $(1,0,1)$ would need an interval containing $x_1$ and $x_3$ but not $x_2$. So their VC dimension is $2$.

:::

::: {#lem-radon .lemma name="Radon's lemma"}

Any $d+2$ points in $\mathbb{R}^d$ can be split into two disjoint groups whose convex hulls intersect.

:::

::: {.proof}

1. The $d+2$ vectors $(\mathbf{x}^{(i)},1)\in\mathbb{R}^{d+1}$ are linearly dependent, so there are numbers $\lambda_i$, not all zero, with $\sum_i\lambda_i\mathbf{x}^{(i)}=\mathbf{0}$ and $\sum_i\lambda_i=0$.

2. Let $I=\{i:\lambda_i>0\}$ and $J=\{i:\lambda_i\le0\}$. Because the $\lambda_i$ sum to $0$ and are not all $0$, both $I$ and $J$ are nonempty, and $\Lambda=\sum_{i\in I}\lambda_i=\sum_{j\in J}(-\lambda_j)>0$.

3. The point $\mathbf{p}=\sum_{i\in I}\frac{\lambda_i}\Lambda\mathbf{x}^{(i)}=\sum_{j\in J}\frac{-\lambda_j}\Lambda\mathbf{x}^{(j)}$ is a convex combination of the points of $I$ and also of the points of $J$.

:::

::: {#thm-vc-halfspaces .theorem name="VC dimension of linear classifiers"}

The linear classifiers $h(\mathbf{x})=\mathbf 1\{\mathbf{w}^{\mathsf T}\mathbf{x}+b\ge0\}$ on $\mathbb{R}^d$ have VC dimension $d+1$.

:::

::: {.proof}

*At least $d+1$.*

1. Take the points $\mathbf{0},\mathbf{e}_1,\dots,\mathbf{e}_d$ and any labelling. Put $w_i=1$ if $\mathbf{e}_i$ is labelled $1$ and $w_i=-1$ otherwise, and $b=\tfrac12$ if $\mathbf{0}$ is labelled $1$ and $b=-\tfrac12$ otherwise.

2. Then $\mathbf{w}^{\mathsf T}\mathbf{0}+b=b$ has the right sign, and $\mathbf{w}^{\mathsf T}\mathbf{e}_i+b=w_i\pm\tfrac12$ has the sign of $w_i$. So all $2^{d+1}$ labellings are produced.

*Less than $d+2$.*

3. Take any $d+2$ points and split them into $I$ and $J$ as in @lem-radon, with a common point $\mathbf{p}=\sum_{i\in I}\mu_i\mathbf{x}^{(i)}=\sum_{j\in J}\nu_j\mathbf{x}^{(j)}$ (convex weights $\mu$, $\nu$).

4. Suppose a classifier labels $I$ with $1$ and $J$ with $0$, and let $f(\mathbf{x})=\mathbf{w}^{\mathsf T}\mathbf{x}+b$. Since $f$ is affine, $f(\mathbf{p})=\sum_{i\in I}\mu_if(\mathbf{x}^{(i)})\ge0$ and $f(\mathbf{p})=\sum_{j\in J}\nu_jf(\mathbf{x}^{(j)})<0$, a contradiction.

5. So no set of $d+2$ points is shattered.

:::

::: {#thm-vc-uniform-convergence .theorem name="Vapnik's uniform convergence bound"}

There is a universal constant $c$ such that, if $\operatorname{VC}(\mathcal H)=D<\infty$, then for every $\delta\in(0,1)$, with probability at least $1-\delta$ over a training set of size $N\ge D$,

$$
\lvert\varepsilon(h)-\hat\varepsilon(h)\rvert\le c\sqrt{\frac DN\log\frac ND+\frac1N\log\frac1\delta}\qquad\text{for all }h\in\mathcal H,
$$

and consequently $\varepsilon(\hat h)\le\varepsilon(h^\star)+2c\sqrt{\frac DN\log\frac ND+\frac1N\log\frac1\delta}$ for the ERM classifier $\hat h$.

:::

<!-- The proof (symmetrization and the Sauer–Shelah lemma) is not given in the source and is not written out here; TODO if a learning theory course (STATS 214) supplies it. -->

::: {#cor-vc-sample-complexity .corollary name="Sample complexity is linear in the VC dimension"}

For fixed accuracy $\gamma$ and confidence $1-\delta$, ERM over $\mathcal H$ achieves $\varepsilon(\hat h)\le\varepsilon(h^\star)+2\gamma$ once $N=O_{\gamma,\delta}\bigl(\operatorname{VC}(\mathcal H)\bigr)$.

:::

::: {.proof}

1. In @thm-vc-uniform-convergence put $N=sD$ with $s\ge1$. The bound becomes $c\sqrt{\frac{\log s}s+\frac{\log(1/\delta)}{sD}}\le c\sqrt{\frac{\log s+\log(1/\delta)}s}$.

2. The right-hand side tends to $0$ as $s\to\infty$ and does not involve $D$, so some $s_0$ depending only on $\gamma$, $\delta$ and $c$ makes it at most $\gamma$. Then $N=s_0D$ examples suffice.

:::

::: {#rmk-vc-dimension-1 .remark name="Parameters and VC dimension"}

For linear classifiers the VC dimension $d+1$ equals the number of parameters, and for many classes the two are roughly proportional, matching the discretization argument of @sec-ai-learning-theory-empirical-risk-minimization. The match is not exact (a one-parameter class like $\mathbf 1\{\sin(a x)\ge0\}$ has infinite VC dimension), and VC bounds are worst-case over distributions, so they say little about heavily over-parametrized networks that generalize well (@sec-ai-machine-learning-bias-variance-tradeoff).

:::
