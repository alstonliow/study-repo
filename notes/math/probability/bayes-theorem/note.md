---
title: "Bayes' Theorem"
sources: [fit1058-cn-9.9]
requires: [math/discrete/sets/partitions]
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

::: {#thm-bayes-theorem .theorem name="Bayes' Theorem"}

With $B_1,\dots,B_n$ as above and $\Pr(A)>0$,
$$\Pr(B_j\mid A) = \frac{\Pr(A\mid B_j)\Pr(B_j)}{\Pr(A)} = \frac{\Pr(A\mid B_j)\Pr(B_j)}{\sum_{i=1}^n \Pr(A\mid B_i)\Pr(B_i)}.$$

:::

::: {.proof}

By the definition and the multiplication rule, $\Pr(B_j\mid A) = \Pr(A\cap B_j)/\Pr(A) = \Pr(A\mid B_j)\Pr(B_j)/\Pr(A)$. Then substitute the law of total probability for $\Pr(A)$.

:::

::: {.remark name="Prior and posterior"}

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
