---
title: "Bayes' Theorem"
sources: [fit1058-cn-9.9]
requires: [math/probability/conditional-probability, math/discrete/sets/partitions]
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Bayes' Theorem. -->

::: {#thm-law-of-total-probability .theorem name="Law of total probability"}

If $B_1,\dots,B_n$ partition $U$ (@sec-math-discrete-sets-partitions) and each $\Pr(B_i)>0$, then
$$\Pr(A) = \sum_{i=1}^n \Pr(A\mid B_i)\Pr(B_i).$$

:::

::: {.proof}

$A$ is the disjoint union of the sets $A\cap B_i$, since the $B_i$ are pairwise disjoint and cover $U$. So $\Pr(A)=\sum_i\Pr(A\cap B_i)=\sum_i\Pr(A\mid B_i)\Pr(B_i)$ by the multiplication rule.

:::

<!-- Added 2026-11-15 from CN §9.9 (own wording and proof). -->

::: {#thm-bayes-two-events .theorem name="Bayes' Theorem, two events"}

If $\Pr(A) > 0$ and $\Pr(B) > 0$, then
$$\Pr(A\mid B) = \frac{\Pr(B\mid A)\Pr(A)}{\Pr(B)}.$$

:::

::: {.proof}

1. By the multiplication rule (@prp-multiplication-rule), $\Pr(A\cap B) = \Pr(B)\Pr(A\mid B)$.

2. Swapping the roles of $A$ and $B$, also $\Pr(A\cap B) = \Pr(A)\Pr(B\mid A)$.

3. Equate the right sides and divide by $\Pr(B)$.

:::

::: {#rmk-bayes-theorem-1 .remark name="Extended form"}

The next theorem is the same rule when the condition is split over a partition $B_1,\dots,B_n$ and $\Pr(A)$ is expanded by the law of total probability.

:::

::: {#thm-bayes-theorem .theorem name="Bayes' Theorem"}

With $B_1,\dots,B_n$ as above and $\Pr(A)>0$,
$$\Pr(B_j\mid A) = \frac{\Pr(A\mid B_j)\Pr(B_j)}{\Pr(A)} = \frac{\Pr(A\mid B_j)\Pr(B_j)}{\sum_{i=1}^n \Pr(A\mid B_i)\Pr(B_i)}.$$

:::

::: {.proof}

By the definition and the multiplication rule, $\Pr(B_j\mid A) = \Pr(A\cap B_j)/\Pr(A) = \Pr(A\mid B_j)\Pr(B_j)/\Pr(A)$. Then substitute the law of total probability for $\Pr(A)$.

:::

::: {#rmk-bayes-theorem-2 .remark name="Prior and posterior"}

$\Pr(B_j)$ is the *prior* probability of $B_j$, before observing $A$; $\Pr(B_j\mid A)$ is the *posterior*, after observing $A$. Bayes’ Theorem is the rule for updating beliefs in the light of evidence, and is a basic tool of statistics and machine learning.

:::

::: {#exm-three-coins .example name="Three coins"}

A coin is chosen at random from three: Fair, DoubleHead and DoubleTail, each with prior probability $\frac13$. It is tossed once and shows Heads. By the law of total probability,
$$\Pr(\text{Heads})=\tfrac12\cdot\tfrac13+1\cdot\tfrac13+0\cdot\tfrac13=\tfrac12.$$
By Bayes’ Theorem,
$$\Pr(\text{Fair}\mid\text{Heads})=\frac{\frac12\cdot\frac13}{\frac12}=\frac13,\qquad
\Pr(\text{DoubleHead}\mid\text{Heads})=\frac{1\cdot\frac13}{\frac12}=\frac23,$$
$$\Pr(\text{DoubleTail}\mid\text{Heads})=\frac{0\cdot\frac13}{\frac12}=0.$$
So one toss leaves our belief in Fair unchanged, rules out DoubleTail, and doubles our belief in DoubleHead.

:::

::: {#fig-bayes-theorem-1}

```{=latex}
\begin{tikzpicture}[coin/.style={box, lbl}, leaf/.style={lbl, anchor=west}]
  \node[dot] (r) at (0,0) {};
  \node[coin] (F) at (3,1.8) {Fair};
  \node[coin] (D) at (3,0) {DoubleHead};
  \node[coin] (T) at (3,-1.8) {DoubleTail};
  \foreach \c in {F,D,T} \draw (r) -- node[edge label] {$\tfrac13$} (\c.west);
  \node[leaf, text=accent] (FH) at (6.2,2.3) {Heads: $\tfrac13\cdot\tfrac12=\tfrac16$};
  \node[leaf, text=muted] (FT) at (6.2,1.3) {Tails};
  \node[leaf, text=accent] (DH) at (6.2,0.5) {Heads: $\tfrac13\cdot1=\tfrac13$};
  \node[leaf, text=muted] (DT) at (6.2,-0.5) {Tails};
  \node[leaf, text=accent] (TH) at (6.2,-1.3) {Heads: $\tfrac13\cdot0=0$};
  \node[leaf, text=muted] (TT) at (6.2,-2.3) {Tails};
  \draw (F.east) -- node[edge label] {$\tfrac12$} (FH.west);
  \draw (F.east) -- node[edge label] {$\tfrac12$} (FT.west);
  \draw (D.east) -- node[edge label] {$1$} (DH.west);
  \draw (D.east) -- node[edge label] {$0$} (DT.west);
  \draw (T.east) -- node[edge label] {$0$} (TH.west);
  \draw (T.east) -- node[edge label] {$1$} (TT.west);
\end{tikzpicture}
```

The three coins as a tree: $\Pr(\text{Heads})$ is the sum of the highlighted leaves, $\tfrac16+\tfrac13+0=\tfrac12$

:::
