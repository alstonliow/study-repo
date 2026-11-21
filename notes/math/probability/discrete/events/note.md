---
title: "Events"
sources: [fit1058-cn-9.4, fit1058-cn-9.5, fit1058-cn-9.6, cs70-13.3.5, cs70-14.4.3]
requires: [math/probability/discrete/sample-spaces, math/discrete/counting/inclusion-exclusion]
aliases: [math/probability/events]   # old ids (moved)
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

::: {#thm-general-case .theorem name="General case" generalizes="thm-inclusion-exclusion"}

$$\Pr\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^n (-1)^{k+1}\sum_{i_1<\cdots<i_k} \Pr(A_{i_1}\cap\cdots\cap A_{i_k}).$$

:::

::: {#fig-events-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (-2.2,-2.0) rectangle (2.2,1.9);
\draw[tintA] (-0.55,0.35) circle (1.05);
\draw[tintB] (0.55,0.35) circle (1.05);
\draw[tintC] (0,-0.6) circle (1.05);
\draw (-0.55,0.35) circle (1.05) (0.55,0.35) circle (1.05) (0,-0.6) circle (1.05);
\node[lab] at (-1.1,0.9) {$A_1$};
\node[lab] at (1.1,0.9) {$A_2$};
\node[lab] at (0,-1.35) {$A_3$};
\node[lab, tick] at (0,0.05) {$+3-3+1$};
\end{tikzpicture}
\end{center}
```

Inclusion–exclusion for three events: a point in all three is counted $3$ times by the single terms, removed $3$ times by the pairs and added back once by the triple, so it counts exactly once

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

## The union bound

::: {#thm-union-bound .theorem name="Union bound"}

For any events $A_1,\dots,A_n$,
$$\Pr(A_1\cup\cdots\cup A_n)\le\Pr(A_1)+\cdots+\Pr(A_n).$$
Equality holds when the events are pairwise mutually exclusive.

:::

::: {.proof}

We use induction on $n$.

1. For $n=1$ both sides are $\Pr(A_1)$.

2. For two events, inclusion-exclusion (@thm-general-case) gives $\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)\le\Pr(A)+\Pr(B)$, since $\Pr(A\cap B)\ge0$.

3. Let $n\ge2$ and assume the bound for $n-1$ events. Apply step 2 to $A=A_1\cup\cdots\cup A_{n-1}$ and $B=A_n$, then the induction hypothesis to $\Pr(A)$:
   $$\Pr(A_1\cup\cdots\cup A_n)\le\Pr(A_1\cup\cdots\cup A_{n-1})+\Pr(A_n)\le\sum_{i=1}^{n}\Pr(A_i).$$

4. If the events are pairwise mutually exclusive, every intersection has probability $0$, so each step is an equality (@prp-events-1).

:::

::: {#fig-events-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (-2.4,-1.4) rectangle (2.4,1.4);
\draw[regionA] (-0.6,0) circle (1.1);
\draw[regionB, fill=none] (0.6,0) circle (1.1);
\begin{scope}\clip (-0.6,0) circle (1.1);\fill[shade] (0.6,0) circle (1.1);\end{scope}
\draw (0.6,0) circle (1.1);
\node[lab] at (-1.15,0) {$A$};
\node[lab] at (1.15,0) {$B$};
\end{tikzpicture}
\end{center}
```

$\Pr(A)+\Pr(B)$ counts the shaded overlap twice, so it is at least $\Pr(A\cup B)$: this is @thm-union-bound for two events

:::

::: {#rmk-events-4 .remark name="When to use it"}

Inclusion-exclusion is exact but needs the probabilities of all $2^n-1$ intersections. The union bound needs only the single events. It overestimates, but it is often good enough to show that a union of rare events is still rare, as in hashing and load balancing.

:::
