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

::: {#fig-cauchy-sequences-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.6,0) node[lab, right] {$n$};
\draw[->, faint] (0,-0.2) -- (0,2.8) node[lab, above] {$a_n$};
\node[dot] at (0.310,1.044) {};
\node[dot] at (0.620,0.965) {};
\node[dot] at (0.930,1.706) {};
\node[dot] at (1.240,1.469) {};
\node[dot] at (1.550,1.181) {};
\node[dot] at (1.860,1.472) {};
\node[dot] at (2.170,1.517) {};
\node[dot] at (2.480,1.280) {};
\node[dot] at (2.790,1.378) {};
\node[dot] at (3.100,1.509) {};
\node[dot] at (3.410,1.354) {};
\node[dot] at (3.720,1.337) {};
\node[dot] at (4.030,1.477) {};
\node[dot] at (4.340,1.408) {};
\node[dot] at (4.650,1.329) {};
\node[dot] at (4.960,1.436) {};
\node[dot] at (5.270,1.441) {};
\node[dot] at (5.580,1.343) {};
\node[dot] at (5.890,1.398) {};
\node[dot] at (6.200,1.453) {};
\fill[tintA] (2.4,1.25) rectangle (6.4,1.55); \draw[decorate, decoration={brace, amplitude=3pt, mirror}] (6.45,1.25) -- node[lab, right=3pt] {$<\varepsilon$} (6.45,1.55);
\draw[dashed, faint] (2.4,-0.1) -- (2.4,2.6); \node[lab, below] at (2.4,-0.1) {$N$};
\end{tikzpicture}
\end{center}
```

A Cauchy sequence: after $N$, any two terms are within $\varepsilon$ of each other, so the tail fits in a strip of width $\varepsilon$. The definition never mentions the limit; completeness supplies it.

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

::: {#fig-cauchy-sequences-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.6,0) node[lab, right] {$n$};
\draw[->, faint] (0,-0.2) -- (0,2.8) node[lab, above] {$a_n$};
\node[dot] at (0.310,1.044) {};
\node[dot] at (0.620,0.965) {};
\node[dot] at (1.240,1.469) {};
\node[dot] at (1.550,1.181) {};
\node[dot] at (2.170,1.517) {};
\node[dot] at (2.480,1.280) {};
\node[dot] at (3.100,1.509) {};
\node[dot] at (3.410,1.354) {};
\node[dot] at (4.030,1.477) {};
\node[dot] at (4.340,1.408) {};
\node[dot] at (4.960,1.436) {};
\node[dot] at (5.270,1.441) {};
\node[dot] at (5.890,1.398) {};
\node[dot] at (6.200,1.453) {};
\node[hl dot] at (0.930,1.706) {};
\node[hl dot] at (1.860,1.472) {};
\node[hl dot] at (2.790,1.378) {};
\node[hl dot] at (3.720,1.337) {};
\node[hl dot] at (4.650,1.329) {};
\node[hl dot] at (5.580,1.343) {};
\draw[faint, dashed] (0,1.4) -- (6.4,1.4) node[lab, right] {$a$};
\end{tikzpicture}
\end{center}
```

If a subsequence (orange) converges to $a$ and the whole sequence is Cauchy, the other terms are close to the subsequence terms and hence close to $a$.

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

::: {#fig-cauchy-sequences-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.3,0) -- (6.3,0);
\node[dot] at (0.300,0.000) {};\node[lab, tick, above] at (0.3,0.12) {$1$};
\node[dot] at (2.600,0.000) {};\node[lab, tick, above] at (2.6,0.12) {$1.4$};
\node[dot] at (4.000,0.000) {};\node[lab, tick, above] at (4.0,0.12) {$1.41$};
\node[dot] at (4.900,0.000) {};\node[lab, tick, above] at (4.9,0.12) {$1.414$};\node[hollow dot] at (5.900,0.000) {};
\node[lab, below] at (5.9,-0.1) {$\sqrt2$};
\end{tikzpicture}
\end{center}
```

Not to scale. In $\mathbb Q$ the truncations $1,1.4,1.41,\dots$ of $\sqrt2$ form a Cauchy sequence with no limit: $\mathbb Q$ is not complete. $\mathbb R$ fills in such gaps.

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
