---
title: "Probability Spaces and Independence of σ-Algebras"
sources: [camii-pm-1]
requires: [math/analysis/measure-theory/measures, math/probability/foundations/conditional-probability]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 1.2, in our own wording; proofs written out in steps. The Borel–Cantelli lemmas are already in math/probability/continuous/modes-of-convergence (lem-borel-cantelli) and are only referenced here. The example on runs is our own. -->

::: {#def-probability-space-measure .definition name="Probability space (measure-theoretic)" related="def-sample-space-event"}

A *probability space* $(\Omega,\mathcal F,\Pr)$ is a measure space with $\Pr(\Omega)=1$. Points $\omega\in\Omega$ are *outcomes*, sets in $\mathcal F$ are *events*, and $\Pr(A)$ is the *probability* of $A$.

:::

All rules of elementary probability (complements, inclusion–exclusion, the union bound) are properties of measures (@prp-measure-continuity); countable additivity adds continuity: $\Pr(A_n)\to\Pr(A)$ when $A_n\uparrow A$ or $A_n\downarrow A$.

::: {#def-independence-sigma-algebras .definition name="Independence of events and of σ-algebras" generalizes="def-mutual-independence-events"}

Events $(A_i)_{i\in I}$ are *independent* if for every finite set $J\subseteq I$

$$
\Pr\Big(\bigcap_{i\in J}A_i\Big)=\prod_{i\in J}\Pr(A_i).
$$

Sub-σ-algebras $(\mathcal A_i)_{i\in I}$ of $\mathcal F$ are *independent* if every choice $A_i\in\mathcal A_i$ gives independent events. Random variables are *independent* if the σ-algebras $\sigma(X_i)$ they generate are.

:::

Events $A_n$ are independent exactly when the σ-algebras $\sigma(A_n)=\{\emptyset,A_n,A_n^c,\Omega\}$ are; this is an exercise in complements.

::: {#thm-independence-pi-systems .theorem name="Independence can be checked on π-systems"}

Let $\mathcal A_1,\dots,\mathcal A_n\subseteq\mathcal F$ be π-systems with $\Omega\in\mathcal A_k$ for each $k$, and suppose

$$
\Pr(A_1\cap\dots\cap A_n)=\Pr(A_1)\cdots\Pr(A_n)\qquad\text{for all }A_k\in\mathcal A_k .
$$

Then $\sigma(\mathcal A_1),\dots,\sigma(\mathcal A_n)$ are independent. The same holds for an infinite family if the identity holds for every finite subfamily.

:::

::: {.proof}

1. Because $\Omega\in\mathcal A_k$, choosing $A_k=\Omega$ for $k\notin J$ gives the product identity for every subfamily $J$. So it is enough to prove the full product identity with $A_k\in\sigma(\mathcal A_k)$.

2. Fix $A_2\in\mathcal A_2,\dots,A_n\in\mathcal A_n$, and let $\mu(A)=\Pr(A\cap A_2\cap\dots\cap A_n)$ and $\nu(A)=\Pr(A)\Pr(A_2)\cdots\Pr(A_n)$. These are finite measures on $\mathcal F$ with equal total mass (take $A=\Omega\in\mathcal A_1$) that agree on $\mathcal A_1$.

3. By uniqueness of extension (@thm-uniqueness-of-extension) they agree on $\sigma(\mathcal A_1)$. So the hypothesis holds with $\mathcal A_1$ replaced by $\sigma(\mathcal A_1)$, which is again a π-system containing $\Omega$.

4. Repeat the argument for the second slot, then the third, and so on. After $n$ steps every $\mathcal A_k$ has been replaced by $\sigma(\mathcal A_k)$.

5. For infinite families, independence is a condition on finite subfamilies, so the finite case applies.

:::

::: {#cor-independence-grouping .corollary name="Grouping independent σ-algebras"}

If $\mathcal A_1,\mathcal A_2,\dots$ are independent and $I_1,I_2,\dots$ are disjoint sets of indices, then the σ-algebras $\mathcal G_j=\sigma\big(\bigcup_{i\in I_j}\mathcal A_i\big)$ are independent.

:::

::: {.proof}

1. Let $\mathcal P_j$ be the collection of finite intersections $A_{i_1}\cap\dots\cap A_{i_r}$ with distinct $i_s\in I_j$ and $A_{i_s}\in\mathcal A_{i_s}$, together with $\Omega$. It is a π-system generating $\mathcal G_j$.

2. A finite intersection of members of different $\mathcal P_j$ is an intersection of events from distinct $\mathcal A_i$, so its probability factorises, first over $i$ and then, regrouping, over $j$.

3. @thm-independence-pi-systems gives the independence of the $\mathcal G_j$.

:::

## Limits of events

::: {#def-limsup-liminf-events .definition name="lim sup and lim inf of events"}

For events $A_1,A_2,\dots$,

$$
\limsup_nA_n=\bigcap_{m}\bigcup_{n\ge m}A_n=\{A_n\text{ infinitely often}\},\qquad\liminf_nA_n=\bigcup_m\bigcap_{n\ge m}A_n=\{A_n\text{ eventually}\}.
$$

:::

Both are events, $(\limsup_nA_n)^c=\liminf_nA_n^c$, and $\mathbf 1_{\limsup A_n}=\limsup_n\mathbf 1_{A_n}$. The two Borel–Cantelli lemmas (@lem-borel-cantelli) decide when $\Pr(\limsup_nA_n)$ is $0$ or $1$; the first needs only countable subadditivity, so it holds in every measure space, and the second needs independence, through the identity $\Pr\big(\bigcap_{n=m}^MA_n^c\big)=\prod_{n=m}^M(1-\Pr(A_n))\le\exp\big(-\sum_{n=m}^M\Pr(A_n)\big)$.

::: {#exm-long-runs .example name="Long runs of heads"}

Toss a fair coin independently forever. Let $A_n$ be the event that tosses $n,n+1,\dots,n+\ell_n-1$ are all heads.

1. If $\ell_n=\lceil2\log_2n\rceil$, then $\Pr(A_n)=2^{-\ell_n}\le n^{-2}$, which is summable. So almost surely only finitely many $A_n$ occur: runs starting at $n$ are eventually shorter than $2\log_2n$.

2. For a lower bound cut the tosses into consecutive disjoint blocks, the $k$-th of length $L_k=\lfloor\log_2k\rfloor$ (empty for $k=1$), and let $B_k$ be the event that block $k$ is all heads. The $B_k$ depend on disjoint sets of tosses, so they are independent (@cor-independence-grouping), and $\Pr(B_k)=2^{-L_k}\ge1/k$ has divergent sum. By the second Borel–Cantelli lemma infinitely many $B_k$ occur almost surely.

3. Block $k$ ends by time $n=L_1+\dots+L_k\le k\log_2k$, so $\log_2k\ge\log_2n-\log_2\log_2n$. Together with part 1: almost surely, the longest run of heads among the first $n$ tosses lies between about $\log_2n-\log_2\log_2n-1$ (for infinitely many $n$) and $2\log_2n$ (for all large $n$); it grows like $\log_2n$.
:::

::: {#fig-probability-spaces-and-independence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (-0.20,-0.2) rectangle (0.20,0.2); \node[tick] at (0.00,0) {T};
\draw[cell frame] (0.22,-0.2) rectangle (0.62,0.2); \node[tick] at (0.42,0) {H};
\draw[cell frame] (0.64,-0.2) rectangle (1.04,0.2); \node[tick] at (0.84,0) {H};
\draw[cell frame] (1.06,-0.2) rectangle (1.46,0.2); \node[tick] at (1.26,0) {T};
\draw[cell frame] (1.48,-0.2) rectangle (1.88,0.2); \node[tick] at (1.68,0) {H};
\draw[cell frame] (1.90,-0.2) rectangle (2.30,0.2); \node[tick] at (2.10,0) {T};
\draw[cell frame] (2.32,-0.2) rectangle (2.72,0.2); \node[tick] at (2.52,0) {T};
\draw[cell frame] (2.74,-0.2) rectangle (3.14,0.2); \node[tick] at (2.94,0) {H};
\draw[cell frame] (3.16,-0.2) rectangle (3.56,0.2); \node[tick] at (3.36,0) {H};
\draw[cell frame] (3.58,-0.2) rectangle (3.98,0.2); \node[tick] at (3.78,0) {H};
\draw[cell frame] (4.00,-0.2) rectangle (4.40,0.2); \node[tick] at (4.20,0) {T};
\draw[cell frame] (4.42,-0.2) rectangle (4.82,0.2); \node[tick] at (4.62,0) {H};
\draw[cell frame] (4.84,-0.2) rectangle (5.24,0.2); \node[tick] at (5.04,0) {T};
\draw[cell frame] (5.26,-0.2) rectangle (5.66,0.2); \node[tick] at (5.46,0) {T};
\draw[cell frame] (5.68,-0.2) rectangle (6.08,0.2); \node[tick] at (5.88,0) {H};
\draw[cell frame] (6.10,-0.2) rectangle (6.50,0.2); \node[tick] at (6.30,0) {T};
\draw[hl cell] (6.52,-0.2) rectangle (6.92,0.2); \node[tick] at (6.72,0) {H};
\draw[hl cell] (6.94,-0.2) rectangle (7.34,0.2); \node[tick] at (7.14,0) {H};
\draw[hl cell] (7.36,-0.2) rectangle (7.76,0.2); \node[tick] at (7.56,0) {H};
\draw[hl cell] (7.78,-0.2) rectangle (8.18,0.2); \node[tick] at (7.98,0) {H};
\draw[cell frame] (8.20,-0.2) rectangle (8.60,0.2); \node[tick] at (8.40,0) {T};
\draw[cell frame] (8.62,-0.2) rectangle (9.02,0.2); \node[tick] at (8.82,0) {T};
\draw[cell frame] (9.04,-0.2) rectangle (9.44,0.2); \node[tick] at (9.24,0) {H};
\draw[cell frame] (9.46,-0.2) rectangle (9.86,0.2); \node[tick] at (9.66,0) {T};
\draw[faint] (-0.18,-0.35) -- (-0.18,-0.45) -- (0.18,-0.45) -- (0.18,-0.35);
\draw[faint] (0.24,-0.35) -- (0.24,-0.45) -- (0.60,-0.45) -- (0.60,-0.35);
\draw[faint] (0.66,-0.35) -- (0.66,-0.45) -- (1.44,-0.45) -- (1.44,-0.35);
\draw[faint] (1.50,-0.35) -- (1.50,-0.45) -- (2.28,-0.45) -- (2.28,-0.35);
\draw[faint] (2.34,-0.35) -- (2.34,-0.45) -- (3.12,-0.45) -- (3.12,-0.35);
\draw[faint] (3.18,-0.35) -- (3.18,-0.45) -- (3.96,-0.45) -- (3.96,-0.35);
\draw[faint] (4.02,-0.35) -- (4.02,-0.45) -- (5.22,-0.45) -- (5.22,-0.35);
\draw[faint] (5.28,-0.35) -- (5.28,-0.45) -- (6.48,-0.45) -- (6.48,-0.35);
\draw[faint] (6.54,-0.35) -- (6.54,-0.45) -- (8.16,-0.45) -- (8.16,-0.35);
\draw[faint] (8.22,-0.35) -- (8.22,-0.45) -- (9.84,-0.45) -- (9.84,-0.35);
\node[tick, right] at (10.1,-0.45) {disjoint blocks of growing length};
\end{tikzpicture}
\end{center}
```

Disjoint blocks of tosses give independent events (here one block is all heads). In the example, block $k$ has length $\lfloor\log_2k\rfloor$ is all heads with probability at least $1/k$, so by the second Borel–Cantelli lemma infinitely many blocks are all heads.

:::
