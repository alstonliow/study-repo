---
title: "Lebesgue Measure and a Non-Measurable Set"
sources: [camii-pm-1]
requires: [math/analysis/measure-theory/caratheodory-extension, math/analysis/real/continuity/compactness-of-closed-intervals]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 1.1, in our own wording; proofs written out in steps. -->

Lebesgue measure gives every interval its length. We build it by Carathéodory's theorem from the ring of finite unions of half-open intervals.

::: {#lem-length-countably-additive .lemma name="Length is countably additive on the ring of intervals"}

Let $\mathcal A$ be the ring of finite unions of intervals $(a,b]\subseteq\mathbb R$; every member can be written as a finite disjoint union $A=\bigcup_{i=1}^k(a_i,b_i]$. Then

$$
\mu(A)=\sum_{i=1}^k(b_i-a_i)
$$

is well defined and countably additive on $\mathcal A$.

:::

::: {.proof}

1. *Well defined and additive.* Two disjoint representations of $A$ have a common refinement, obtained by cutting at all their end points; refining one interval $(a,b]$ at points $a<c_1<\dots<c_m<b$ does not change the total length. So all representations give the same value, and additivity follows by concatenating representations.

2. *Reduction.* Let $A=\bigcup_nA_n$ with disjoint $A_n\in\mathcal A$ and $A\in\mathcal A$. Put $B_n=A\setminus(A_1\cup\dots\cup A_n)\in\mathcal A$. By additivity $\mu(A)=\mu(A_1)+\dots+\mu(A_n)+\mu(B_n)$, so it is enough to show that $\mu(B_n)\to0$ for every decreasing sequence $B_n\downarrow\emptyset$ in $\mathcal A$.

3. Suppose instead $\mu(B_n)\ge2\varepsilon>0$ for all $n$. Shrinking each interval of $B_n$ slightly from the left, choose $C_n\in\mathcal A$ with $\overline{C_n}\subseteq B_n$ and $\mu(B_n\setminus C_n)\le\varepsilon2^{-n}$.

4. Put $D_n=C_1\cap\dots\cap C_n$. Then $B_n\setminus D_n\subseteq\bigcup_{k\le n}(B_k\setminus C_k)$, so $\mu(B_n\setminus D_n)\le\varepsilon$ and $\mu(D_n)\ge\varepsilon>0$. In particular $D_n\neq\emptyset$.

5. The sets $K_n=\overline{C_1}\cap\dots\cap\overline{C_n}\supseteq D_n$ are non-empty, closed, bounded and decreasing. By the Heine–Borel theorem (@thm-heine-borel-interval) and the finite-intersection property of compact sets, $\bigcap_nK_n\neq\emptyset$. But $K_n\subseteq B_n$, so $\bigcap_nB_n\neq\emptyset$, a contradiction.

:::

::: {#thm-lebesgue-measure .theorem name="Existence and uniqueness of Lebesgue measure"}

There is a unique Borel measure $\lambda$ on $\mathbb R$ with

$$
\lambda((a,b])=b-a\qquad\text{for all }a<b .
$$

It is called *Lebesgue measure*; it is σ-finite and gives $\lambda([a,b])=\lambda((a,b))=b-a$.

:::

::: {.proof}

1. *Existence.* $\sigma(\mathcal A)=\mathcal B$ (@def-borel-sigma-algebra), so by @lem-length-countably-additive and Carathéodory's theorem (@thm-caratheodory-extension) the length function extends to a measure on $\mathcal B$.

2. *Uniqueness.* The intervals $(n,n+1]$, $n\in\mathbb Z$, lie in the π-system of half-open intervals, cover $\mathbb R$, and have finite measure. By @cor-uniqueness-sigma-finite two Borel measures giving every $(a,b]$ its length are equal.

3. *Points and closed intervals.* $\{b\}=\bigcap_n(b-\tfrac1n,b]$, so by continuity from above $\lambda(\{b\})=\lim\tfrac1n=0$. Adding or removing end points does not change the measure.

:::

::: {#fig-lebesgue-measure-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.2,0) -- (8.2,0);
\draw[bold] (0.5,0) -- (1.6,0);
\draw[bold] (2.4,0) -- (2.9,0);
\draw[bold] (4.0,0) -- (5.6,0);
\draw[bold] (6.7,0) -- (7.3,0);
\draw[hl] (0.3,0.35) -- (1.9,0.35);
\draw[accent] (0.3,0.27) -- (0.3,0.43); \fill[accent] (1.9,0.35) circle (1.6pt);
\draw[hl] (2.2,0.35) -- (3.1,0.35);
\draw[accent] (2.2,0.27) -- (2.2,0.43); \fill[accent] (3.1,0.35) circle (1.6pt);
\draw[hl] (3.8,0.35) -- (4.9,0.35);
\draw[accent] (3.8,0.27) -- (3.8,0.43); \fill[accent] (4.9,0.35) circle (1.6pt);
\draw[hl] (4.7,0.6) -- (5.8,0.6);
\draw[accent] (4.7,0.52) -- (4.7,0.68); \fill[accent] (5.8,0.6) circle (1.6pt);
\draw[hl] (6.5,0.35) -- (7.5,0.35);
\draw[accent] (6.5,0.27) -- (6.5,0.43); \fill[accent] (7.5,0.35) circle (1.6pt);
\node[lab, below] at (4,-0.1) {a Borel set $B$ (black) and a cover by intervals $(a_k,b_k]$ (above)};
\end{tikzpicture}
\end{center}
```

Lebesgue measure of a set is the infimum of the total length of countable covers by half-open intervals; on Borel sets this outer measure is countably additive.

:::

The same construction in $\mathbb R^d$, starting from boxes $\prod_{i}(a_i,b_i]$ with volume $\prod_i(b_i-a_i)$, gives Lebesgue measure $\lambda^d$ on $\mathcal B(\mathbb R^d)$; it is also the product measure of $d$ copies of $\lambda$ (@sec-math-analysis-measure-theory-product-measures).

::: {#prp-lebesgue-translation-invariant .proposition name="Translation invariance"}

$\lambda(A+x)=\lambda(A)$ for all $A\in\mathcal B$ and $x\in\mathbb R$. Conversely, a translation-invariant Borel measure $\nu$ on $\mathbb R$ with $\nu((0,1])=1$ equals $\lambda$.

:::

::: {.proof}

1. Translation $y\mapsto y-x$ is continuous, so $A+x$ is Borel for Borel $A$ (the sets $A$ with $A+x\in\mathcal B$ form a σ-algebra containing the open sets). Then $\lambda_x(A)=\lambda(A+x)$ is a Borel measure with $\lambda_x((a,b])=b-a$, so $\lambda_x=\lambda$ by uniqueness.

2. For the converse, $(0,1]$ is the disjoint union of $n$ translates of $(0,\tfrac1n]$, so $\nu((0,\tfrac1n])=\tfrac1n$, and then $\nu((p,q])=q-p$ for all rationals $p<q$ by additivity and invariance.

3. For real $a<b$ choose rationals $p_n\downarrow a$ and $q_n\uparrow b$. Continuity from below on $(p_n,q_n]\uparrow(a,b)$ gives $\nu((a,b))=b-a$ for all real $a<b$, and continuity from above on $(a,b+\tfrac1n)\downarrow(a,b]$ then gives $\nu((a,b])=b-a$. Uniqueness finishes the proof.

:::

::: {#rmk-lebesgue-measure-null-sets .remark name="Null sets" related="def-measure-zero"}

A set $A\subseteq\mathbb R$ has measure zero in the sense of @def-measure-zero exactly when its outer measure $\lambda^*(A)$ is $0$: covers by open intervals and by half-open intervals of nearly the same total length are interchangeable. So countable sets and the Cantor set are Lebesgue null.

:::

## A set that is not Lebesgue measurable

::: {#thm-vitali-set .theorem name="Vitali's non-measurable set"}

Assuming the axiom of choice, there is a subset of $[0,1)$ that is not Lebesgue measurable (not in the completion of $\mathcal B$). In particular Lebesgue measure cannot be extended to all subsets of $\mathbb R$ as a translation-invariant measure.

:::

::: {.proof}

1. On $[0,1)$ let $x\sim y$ when $x-y\in\mathbb Q$. This is an equivalence relation; by the axiom of choice pick a set $S$ containing exactly one point of each class.

2. For each rational $r\in[0,1)$ let $S_r=\{s+r\bmod1:\ s\in S\}$. The sets $S_r$ are disjoint: if $s+r\equiv s'+r'\pmod 1$ then $s\sim s'$, so $s=s'$ and $r=r'$. They cover $[0,1)$: every $x$ is equivalent to some $s\in S$, and $x-s\bmod1$ is a rational $r$.

3. Suppose $S$ were measurable. $S_r$ is the translate of $S\cap[0,1-r)$ by $r$ together with the translate of $S\cap[1-r,1)$ by $r-1$, so by translation invariance $\lambda(S_r)=\lambda(S)$.

4. Countable additivity over the countably many $r$ gives $1=\lambda([0,1))=\sum_r\lambda(S)$, which is $0$ or $\infty$. This contradiction shows $S$ is not measurable.

:::
