---
title: "Compact Metric Spaces"
sources: [camib-at-a4, camib-at-a5, camib-at-m4]
requires: [math/analysis/metric-spaces/completeness]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Sections 4.3 and 5.4 (the characterisation by total boundedness is non-examinable there), and Metric and Topological Spaces (Easter 2015 lecture notes), Section 4.3, in our own wording; examples ours; proofs written out in steps. Open-cover compactness, and its equivalence with the sequential version for metric spaces, are in math/analysis/topology/compact-spaces. -->

Closed bounded intervals have two key properties: every sequence has a convergent subsequence (@thm-bolzano-weierstrass) and every open cover has a finite subcover (@thm-heine-borel-interval). In metric spaces the two properties agree (@thm-compact-iff-sequentially-compact); here we use the first.

::: {#def-sequentially-compact .definition name="Sequentially compact"}

A metric space $X$ is *sequentially compact* if every sequence in $X$ has a subsequence converging to a point of $X$. A subset $K\subseteq X$ is sequentially compact if it is so as a subspace: every sequence in $K$ has a subsequence converging to a point of $K$.

:::

::: {#thm-compact-complete-bounded .theorem name="Compact spaces are complete and bounded"}

A sequentially compact metric space is complete and bounded. Consequently a sequentially compact subset of any metric space is closed and bounded.

:::

::: {.proof}

1. *Complete.* A Cauchy sequence has a convergent subsequence by compactness, so it converges (@prp-cauchy-sequences-metric, part 3).

2. *Bounded.* Suppose not. Fix $x_0$ and choose $x_n$ with $d(x_n,x_0)>n$. A convergent subsequence $x_{n_k}\to x$ would give $d(x_{n_k},x_0)\le d(x_{n_k},x)+d(x,x_0)$, bounded in $k$, contradicting $d(x_{n_k},x_0)>n_k\to\infty$.

3. *Subsets.* A sequentially compact subset is complete, hence closed by @thm-closed-subspace-complete, and bounded by step 2.

:::

::: {#thm-heine-borel-rn .theorem name="Heine–Borel theorem in $\mathbb R^n$ (sequential form)" generalizes="thm-heine-borel-interval"}

A subset $K\subseteq\mathbb R^n$ (with any norm) is sequentially compact if and only if it is closed and bounded.

:::

::: {.proof}

1. *Only if:* @thm-compact-complete-bounded.

2. *If:* by @thm-norms-equivalent-finite-dimension we may use $\|\cdot\|_2$. A sequence in $K$ is bounded, so by @thm-bolzano-weierstrass-rn it has a subsequence converging to some $x\in\mathbb R^n$; $x\in K$ because $K$ is closed (@prp-closed-iff-complement-open).

:::

::: {#exm-closed-bounded-not-compact .example name="Closed and bounded is not enough in general"}

In $C[0,1]$ with $\|\cdot\|_\infty$, let $g_n$ be a tent of height $1$ supported in $[2^{-n},2^{-n+1}]$. The supports do not overlap, so $\|g_m-g_n\|_\infty=1$ for $m\ne n$; no subsequence is Cauchy, so none converges. Yet all $g_n$ lie in the closed unit ball $\{\|f\|_\infty\le1\}$, which is closed and bounded. Similarly a discrete space with infinitely many points is complete and bounded but not compact.

:::

## Total boundedness

What closed and bounded misses in infinite dimensions is a finiteness condition at every scale.

::: {#def-totally-bounded .definition name="Totally bounded"}

A metric space $X$ is *totally bounded* if for every $\varepsilon>0$ it is covered by finitely many balls of radius $\varepsilon$.

:::

::: {#thm-compact-iff-complete-totally-bounded .theorem name="Compact means complete and totally bounded"}

A metric space is sequentially compact if and only if it is complete and totally bounded.

:::

::: {.proof}

1. *Compact implies totally bounded.* Suppose that for some $\varepsilon>0$ no finitely many $\varepsilon$-balls cover $X$. Choose $x_1$; given $x_1,\dots,x_n$, the balls $B_\varepsilon(x_i)$ do not cover $X$, so choose $x_{n+1}$ outside all of them. Then $d(x_m,x_n)\ge\varepsilon$ for $m\ne n$, so no subsequence is Cauchy and none converges. Completeness is @thm-compact-complete-bounded.

2. *Conversely,* let $X$ be complete and totally bounded and $(x_n)$ a sequence. Cover $X$ by finitely many balls of radius $1$; one of them contains $x_n$ for infinitely many $n$. Let $S_1$ be this infinite set of indices.

3. *Repeat at smaller scales.* Given an infinite index set $S_k$, cover $X$ by finitely many balls of radius $2^{-k-1}$; one contains $x_n$ for infinitely many $n\in S_k$. Let $S_{k+1}\subseteq S_k$ be those indices. All $x_n$ with $n\in S_k$ lie in one ball of radius $2^{-k}$, so are within $2^{1-k}$ of each other.

4. *Diagonal subsequence.* Choose $n_1<n_2<\cdots$ with $n_k\in S_k$. For $j\ge k$, both $n_j$ and $n_k$ lie in $S_k$, so $d(x_{n_j},x_{n_k})<2^{1-k}$. The subsequence is Cauchy, hence converges because $X$ is complete.

:::

A subset of $\mathbb R^n$ is bounded if and only if it is totally bounded (a bounded set lies in a cube, which is covered by finitely many small cubes), so @thm-heine-borel-rn is the special case of @thm-compact-iff-complete-totally-bounded for closed subsets of the complete space $\mathbb R^n$.
