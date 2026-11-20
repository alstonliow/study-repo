---
title: "Cauchy Sequences and Completeness"
sources: [cama1-2]
requires: [math/analysis/real/sequences/monotone-sequences]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 2.4, in our own wording; proofs written out in steps. -->

A Cauchy sequence is one whose terms eventually crowd together, with no limit mentioned. In $\mathbb R$ this is the same as convergence, which lets us prove that a sequence converges without guessing its limit. The decimal approximations $3,\ 3.1,\ 3.14,\ 3.141,\dots$ of $\pi$ are Cauchy in $\mathbb Q$ although their limit is not in $\mathbb Q$.

::: {#def-cauchy-sequence .definition name="Cauchy sequence"}

$(a_n)$ is a *Cauchy sequence* if
$$\forall\varepsilon>0\ \exists N\ \forall p,q\ge N\quad |a_p-a_q|<\varepsilon.$$

:::

::: {#lem-convergent-is-cauchy .lemma name="Convergent sequences are Cauchy"}

If $a_n\to a$, then $(a_n)$ is Cauchy.

:::

::: {.proof}

1. Let $\varepsilon>0$ and choose $N$ with $|a_n-a|<\varepsilon/2$ for $n\ge N$.

2. For $p,q\ge N$, $|a_p-a_q|\le|a_p-a|+|a-a_q|<\varepsilon$.

:::

::: {#lem-cauchy-convergent-subsequence .lemma name="A Cauchy sequence follows its subsequences"}

If $(a_n)$ is Cauchy and some subsequence $a_{n_k}\to a$, then $a_n\to a$.

:::

::: {.proof}

1. Let $\varepsilon>0$. Choose $N$ with $|a_p-a_q|<\varepsilon/2$ for $p,q\ge N$.

2. Choose $K$ with $n_K\ge N$ and $|a_{n_K}-a|<\varepsilon/2$ (possible because $n_k\to\infty$ and $a_{n_k}\to a$).

3. For $n\ge N$, $|a_n-a|\le|a_n-a_{n_K}|+|a_{n_K}-a|<\varepsilon$.

:::

::: {#thm-general-principle-of-convergence .theorem name="General principle of convergence"}

A sequence of real numbers converges if and only if it is Cauchy.

:::

::: {.proof}

1. Convergent sequences are Cauchy by @lem-convergent-is-cauchy. Conversely let $(a_n)$ be Cauchy.

2. *Bounded.* With $\varepsilon=1$ there is $N$ such that $|a_n-a_N|<1$ for all $n\ge N$, so $|a_n|<|a_N|+1$ eventually; hence $(a_n)$ is bounded.

3. *Convergent subsequence.* By @thm-bolzano-weierstrass some subsequence converges, say to $a$.

4. By @lem-cauchy-convergent-subsequence, $a_n\to a$.

:::

::: {#def-complete-ordered-field .definition name="Complete ordered field"}

An ordered field is *complete* if every Cauchy sequence in it converges.

:::

So $\mathbb R$ is a complete ordered field, and $\mathbb Q$ is not. Completeness alone does not characterise $\mathbb R$: adjoining all limits of Cauchy sequences to the non-Archimedean field of rational functions (@sec-math-analysis-real-real-numbers-ordered-fields-and-completeness) gives a complete ordered field that is still not Archimedean. With the Archimedean property added, completeness is equivalent to the other two forms of the axiom.

::: {#thm-complete-archimedean-monotone .theorem name="Complete and Archimedean gives monotone sequences property"}

If an ordered field is Archimedean and every Cauchy sequence converges, then every increasing sequence that is bounded above converges.

:::

::: {.proof}

1. We show the contrapositive for an increasing sequence $(a_n)$: if it is not Cauchy, it is not bounded above. (If it is Cauchy, it converges by assumption.)

2. Not Cauchy means there is $\varepsilon>0$ such that for every $N$ some $p>q\ge N$ have $|a_p-a_q|\ge\varepsilon$. As the sequence increases, $a_p\ge a_q+\varepsilon\ge a_N+\varepsilon$.

3. So for every $N$ there is $p>N$ with $a_p\ge a_N+\varepsilon$. Starting from $n_1=1$ and applying this repeatedly gives indices $n_1<n_2<\cdots$ with $a_{n_{k+1}}\ge a_{n_k}+\varepsilon$.

4. By induction $a_{n_k}\ge a_{n_1}+(k-1)\varepsilon$, and by the Archimedean property $(k-1)\varepsilon$ exceeds every bound. So $(a_n)$ is not bounded above.

:::

Together with @thm-monotone-convergence and @thm-monotone-sequences-equivalent, for an ordered field we have: least upper bound property $\Leftrightarrow$ monotone sequences property $\Leftrightarrow$ Archimedean and complete.

::: {#rmk-cauchy-sequences-1 .remark name="Why Cauchy's form is useful"}

The definition of convergence begins with $\exists\ell$, a quantifier over all real numbers; the Cauchy condition only quantifies over natural numbers (by the Archimedean property it suffices to take $\varepsilon=1/m$). Practically, it lets us prove convergence of series (@sec-math-analysis-real-series-absolute-convergence) and later of sequences in metric spaces without naming the limit.

:::
