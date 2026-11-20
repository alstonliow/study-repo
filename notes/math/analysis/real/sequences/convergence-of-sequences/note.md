---
title: "Convergence of Sequences"
sources: [cama1-2]
requires: [math/analysis/real/real-numbers/ordered-fields-and-completeness, math/calculus/single-variable/limits/limits-of-sequences]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 2.1–2.3, in our own wording; proofs written out in steps. The definition of a limit and the limit laws are already in @sec-math-calculus-single-variable-limits-limits-of-sequences; this note adds the lemmas that make those laws rigorous. -->

A *sequence* is a function $\mathbb N\to\mathbb R$ (or $\mathbb C$), written $(a_n)$. Convergence $a_n\to\ell$ is defined in @def-limit-of-a-sequence: for every $\varepsilon>0$ the terms are *eventually always* within $\varepsilon$ of $\ell$.

## Uniqueness and boundedness

::: {#thm-limit-unique .theorem name="Limits are unique"}

A sequence has at most one limit.

:::

::: {.proof}

1. Suppose $a_n\to x$ and $a_n\to y$, and let $\varepsilon>0$.

2. Choose $N$ so large that $|a_n-x|<\varepsilon/2$ and $|a_n-y|<\varepsilon/2$ for all $n\ge N$ (take the larger of the two thresholds).

3. By the triangle inequality, $|x-y|\le|x-a_N|+|a_N-y|<\varepsilon$.

4. A non-negative number smaller than every $\varepsilon>0$ is $0$, so $x=y$.

:::

::: {#def-bounded-sequence .definition name="Bounded sequence"}

$(a_n)$ is *bounded* if there is $C$ with $|a_n|\le C$ for all $n$, and *eventually bounded* if there are $C$ and $N$ with $|a_n|\le C$ for all $n\ge N$.

:::

An eventually bounded sequence is bounded: only the finitely many terms $a_1,\dots,a_{N-1}$ remain, so $|a_n|\le\max\{|a_1|,\dots,|a_{N-1}|,C\}$ for all $n$. In proofs it is usually enough to show eventual boundedness.

::: {#lem-convergent-bounded .lemma name="Convergent sequences are bounded"}

If $a_n\to\ell$, then $(a_n)$ is bounded.

:::

::: {.proof}

1. Taking $\varepsilon=1$, there is $N$ with $|a_n-\ell|<1$ for all $n\ge N$.

2. Then $|a_n|\le|\ell|+|a_n-\ell|<|\ell|+1$ for $n\ge N$, so $(a_n)$ is eventually bounded, hence bounded.

:::

::: {#lem-bounded-times-null .lemma name="Bounded times null"}

If $(a_n)$ is bounded and $b_n\to 0$, then $a_nb_n\to 0$.

:::

::: {.proof}

1. Let $C>0$ with $|a_n|\le C$ for all $n$, and let $\varepsilon>0$.

2. Choose $N$ with $|b_n|<\varepsilon/C$ for all $n\ge N$.

3. Then $|a_nb_n|\le C|b_n|<\varepsilon$ for all $n\ge N$.

:::

::: {#rmk-convergence-of-sequences-1 .remark name="Proofs of the product and quotient laws" related="prp-limit-laws"}

The two lemmas give the product and quotient laws of @prp-limit-laws, which the earlier note uses without proof.

1. *Product.* Write $a_nb_n-ab=(a_n-a)b_n+a(b_n-b)$. The sequence $(b_n)$ is bounded (@lem-convergent-bounded) and $a_n-a\to0$, so the first term tends to $0$ (@lem-bounded-times-null); so does the second. Hence $a_nb_n\to ab$.

2. *Reciprocal.* Let $b_n\ne0$, $b_n\to b\ne0$. Eventually $|b_n-b|<|b|/2$, so $|b_n|>|b|/2$ and $\left|\frac{1}{b_nb}\right|<\frac{2}{|b|^2}$; thus $\frac1{b_nb}$ is eventually bounded. Since $\frac1{b_n}-\frac1b=(b-b_n)\cdot\frac1{b_nb}$ and $b-b_n\to0$, the lemma gives $\frac1{b_n}\to\frac1b$.

3. *Quotient.* $\frac{a_n}{b_n}=a_n\cdot\frac1{b_n}\to a\cdot\frac1b$ by steps 1 and 2.

:::

## Inequalities and the sandwich rule

::: {#lem-limit-preserves-inequality .lemma name="Limits preserve weak inequalities"}

If $a_n\to a$ and $a_n\le x$ for all $n$, then $a\le x$.

:::

::: {.proof}

1. Suppose $a>x$ and take $\varepsilon=a-x>0$.

2. For some $N$, $|a_N-a|<a-x$, so $a_N>a-(a-x)=x$, contradicting $a_N\le x$.

:::

Strict inequalities are not preserved: $1/n>0$ for all $n$, but the limit is $0$.

::: {#thm-sandwich-sequences .theorem name="Sandwich rule" related="thm-squeeze-functions"}

If $a_n\le c_n\le b_n$ for all $n$ and $a_n\to x$, $b_n\to x$, then
$$c_n\to x.$$

:::

::: {.proof}

1. Let $\varepsilon>0$ and choose $N$ with $|a_n-x|<\varepsilon$ and $|b_n-x|<\varepsilon$ for all $n\ge N$.

2. For $n\ge N$, $x-\varepsilon<a_n\le c_n\le b_n<x+\varepsilon$, so $|c_n-x|<\varepsilon$.

:::

::: {#exm-convergence-of-sequences-1 .example name="Using the rules instead of $\varepsilon$"}

$\dfrac{n^2+3}{(n+5)(2n-1)}\to\dfrac12$. Divide numerator and denominator by $n^2$:
$$\frac{n^2+3}{(n+5)(2n-1)}=\frac{1+3/n^2}{(1+5/n)(2-1/n)}.$$
Here $1/n\to0$ (@thm-archimedean-property), so $3/n^2\to 0$, $5/n\to0$, and the limit laws give $\frac{1+0}{(1+0)(2-0)}=\frac12$. Once the rules are proved, no $\varepsilon$ is needed.

:::

::: {#exm-exponential-beats-polynomial .example name="Exponentials beat polynomials"}

For every $k\in\mathbb N$ and $\delta>0$,
$$\frac{n^k}{(1+\delta)^n}\to0.$$

1. All terms of the binomial expansion of $(1+\delta)^n$ are non-negative, so keeping one of them gives $(1+\delta)^n\ge\binom{n}{k+1}\delta^{k+1}$ (@thm-binomial-theorem).

2. For $n\ge 2k$, each of the $k+1$ factors $n,n-1,\dots,n-k$ is at least $n/2$, so $\binom{n}{k+1}\ge\dfrac{(n/2)^{k+1}}{(k+1)!}$.

3. Combining, for $n\ge 2k$,
$$0\le\frac{n^k}{(1+\delta)^n}\le\frac{2^{k+1}(k+1)!}{\delta^{k+1}}\cdot\frac1n,$$
a constant times $1/n$, which tends to $0$. The sandwich rule (@thm-sandwich-sequences) finishes the proof.

:::
