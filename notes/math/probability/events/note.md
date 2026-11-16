---
title: "Events"
sources: [fit1058-cn-9.4, fit1058-cn-9.5, fit1058-cn-9.6, cs70-13.3.5]
requires: [math/probability/sample-spaces, math/discrete/counting/inclusion-exclusion]
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Mutually exclusive events; Operations on events; Inclusion-Exclusion for probabilities. -->

## Mutually exclusive events

::: {#def-mutually-exclusive .definition name="Mutually exclusive"}

Events $A,B$ are *mutually exclusive* if $A\cap B=\emptyset$.

:::

::: {#prp-events-1 .proposition}

If $A,B$ are mutually exclusive, then $\Pr(A\cup B)=\Pr(A)+\Pr(B)$.

:::

::: {.proof}

Each $x\in A\cup B$ lies in exactly one of $A$ and $B$, so $\Pr(A\cup B)=\sum_{x\in A\cup B}\Pr(x)=\sum_{x\in A}\Pr(x)+\sum_{x\in B}\Pr(x)=\Pr(A)+\Pr(B)$.

:::

::: {#exm-events-1 .example}

For two dice, $\Pr(\text{total}\le5)=10/36$ and $\Pr(\text{total}\ge10)=6/36$. These events are disjoint, so $\Pr(\text{total}\le5\text{ or }\ge10)=16/36=4/9$.

:::

## Operations on events

::: {#prp-complement .proposition name="Complement"}

$\Pr(\overline{A}) = 1-\Pr(A)$.

:::

::: {.proof}

$A$ and $\overline A$ are mutually exclusive with union $U$, so $\Pr(A)+\Pr(\overline A)=\Pr(U)=1$.

:::

::: {#fig-events-1}

```{=latex}
\begin{tikzpicture}
  \begin{scope}[xshift=0cm]
    \fill[shade] (0.85,0) circle (0.75); \fill[shade] (1.75,0) circle (0.75);
    \draw (-0.4,-1.1) rectangle (3.0,1.1);
    \draw (0.85,0) circle (0.75); \draw (1.75,0) circle (0.75);
    \node at (0.45,0) {$A$}; \node at (2.15,0) {$B$};
    \node at (1.3,-1.5) {$A\cup B$};
  \end{scope}
  \begin{scope}[xshift=4.0cm]
    \fill[shade] (0.85,0) circle (0.75); \begin{scope}\clip (0.85,0) circle (0.75); \fill[white] (1.75,0) circle (0.75);\end{scope}
    \draw (-0.4,-1.1) rectangle (3.0,1.1);
    \draw (0.85,0) circle (0.75); \draw (1.75,0) circle (0.75);
    \node at (0.45,0) {$A$}; \node at (2.15,0) {$B$};
    \node at (1.3,-1.5) {$A\setminus B$};
  \end{scope}
  \begin{scope}[xshift=8.0cm]
    \fill[shade, even odd rule] (-0.4,-1.1) rectangle (3.0,1.1) (0.85,0) circle (0.75);
    \draw (-0.4,-1.1) rectangle (3.0,1.1);
    \draw (0.85,0) circle (0.75); \draw (1.75,0) circle (0.75);
    \node at (0.45,0) {$A$}; \node at (2.15,0) {$B$};
    \node at (1.3,-1.5) {$\overline{A}$};
  \end{scope}
\end{tikzpicture}
```

Operations on events as regions of the sample space (shaded)

:::

::: {#exm-events-1-2 .example}

In “dice cricket”, each throw of a fair die is the runs scored off one delivery, except that $5$ means out. So $\Pr(\text{not out})=1-\frac16=\frac56$.

:::

::: {#prp-difference-and-monotonicity .proposition name="Difference and monotonicity"}

If $A\subseteq B$, then $\Pr(B\setminus A)=\Pr(B)-\Pr(A)$, and hence $\Pr(A)\le\Pr(B)$.

:::

::: {.proof}

$B$ is the disjoint union of $A$ and $B\setminus A$, so $\Pr(B)=\Pr(A)+\Pr(B\setminus A)$. Both claims follow, the second because $\Pr(B\setminus A)\ge0$.

:::

::: {#rmk-events-1 .remark name="In words"}

You cannot make something less likely by creating more ways for it to happen.

:::

::: {#exm-events-2 .example}

In Scrabble, $\Pr(\text{vowel})=0.42$ and $\Pr(\text{letter, not blank})=0.98$. Every vowel tile is a letter tile, so $\Pr(\text{consonant})=0.98-0.42=0.56$.

:::

## Inclusion-Exclusion for probabilities

::: {#prp-events-1-2 .proposition}

$\Pr(A\cup B) = \Pr(A)+\Pr(B)-\Pr(A\cap B)$.

:::

::: {.proof}

$A\cup B$ is the disjoint union of $A$ and $B\setminus A$, and $B\setminus A=B\setminus(A\cap B)$ with $A\cap B\subseteq B$. So $\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)$ by the previous two theorems.

:::

::: {#thm-general-case .theorem name="General case"}

$$\Pr\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^n (-1)^{k+1}\sum_{i_1<\cdots<i_k} \Pr(A_{i_1}\cap\cdots\cap A_{i_k}).$$

:::

::: {#rmk-events-2 .remark name="Same proof as for counting"}

The proof is the same as for inclusion-exclusion on set sizes (@sec-math-discrete-counting-inclusion-exclusion), with $\Pr$ in place of $|\cdot|$.

:::

<!-- Added 2026-11-15 from CN §9.6 (own wording). -->

::: {#thm-ie-probability-intersection .theorem name="Inclusion-exclusion, intersection form"}

$$\Pr\left(\bigcap_{i=1}^n A_i\right) = \sum_{k=1}^n (-1)^{k+1}\sum_{i_1<\cdots<i_k} \Pr(A_{i_1}\cup\cdots\cup A_{i_k}).$$

:::

::: {#rmk-events-3 .remark name="Proof and relation to counting"}

This is the probability version of the dual form for set sizes (@cor-ie-dual), with the same proof. When all outcomes are equally likely, $\Pr(A) = |A|/|U|$, and both forms reduce to the counting versions: inclusion-exclusion for counting is a special case of inclusion-exclusion for probability.

:::
