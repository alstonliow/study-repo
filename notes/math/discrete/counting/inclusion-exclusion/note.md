---
title: Inclusion-Exclusion
sources: [fit1058-cn-8.3]
requires: [math/discrete/counting/combinations]
level: core
status: draft
---

<!-- Migrated from 1058note 08-counting-combinatorics.tex, §8.3. -->

::: {#prp-ie-two-sets .proposition name="Two sets"}
$$
|A\cup B| = |A|+|B|-|A\cap B|.
$$
:::

::: {.remark name="Correcting the double count"}
Already proved at @sec-math-discrete-sets-set-operations. $|A|+|B|$ double-counts $A\cap B$; subtracting once corrects it.
:::

::: {#prp-ie-three-sets .proposition name="Three sets"}
$$
|A\cup B\cup C| = |A|+|B|+|C| - |A\cap B|-|A\cap C|-|B\cap C| + |A\cap B\cap C|.
$$
:::

::: {.remark name="Why the correction pattern"}
Summing $|A|+|B|+|C|$ counts elements in exactly two sets twice, elements in all three sets three times. Subtracting all pairwise intersections fixes the double-count but now over-corrects triple-members (removed three times, once per pair, instead of the needed two). Adding back $|A\cap B\cap C|$ restores them to count $1$.
:::

::: {#thm-inclusion-exclusion .theorem name="General inclusion-exclusion"}
For finite $A_1,\dots,A_n$:
$$
\left|\bigcup_{i=1}^n A_i\right| = \sum_{k=1}^n (-1)^{k+1} \sum_{1\le i_1<\cdots<i_k\le n} |A_{i_1}\cap\cdots\cap A_{i_k}|.
$$
:::

::: {.proof name="Proof by induction on $n$"}
**Base case** ($n=1$): both sides equal $|A_1|$.

**Inductive step**: Assume the formula for $n$ sets. Write $U=A_1\cup\cdots\cup A_n$. Then
$$
\left|\bigcup_{i=1}^{n+1}A_i\right| = |U \cup A_{n+1}| = |U| + |A_{n+1}| - |U\cap A_{n+1}|
$$
by the two-set formula. Since $U\cap A_{n+1} = \bigcup_{i=1}^n (A_i\cap A_{n+1})$ (distributive law, @sec-math-discrete-sets-set-operations), the inductive hypothesis applies to *both* $|U|$ and $|U\cap A_{n+1}|$ (the latter as a union of $n$ sets $A_i\cap A_{n+1}$):
$$
|U| = \sum_{k=1}^n(-1)^{k+1}\!\!\sum_{i_1<\cdots<i_k\le n}\!\! |A_{i_1}\cap\cdots\cap A_{i_k}|,
$$
$$
|U\cap A_{n+1}| = \sum_{k=1}^n(-1)^{k+1}\!\!\sum_{i_1<\cdots<i_k\le n}\!\! |A_{i_1}\cap\cdots\cap A_{i_k}\cap A_{n+1}|.
$$
The first sum ranges over all size-$k$ subsets of $\{1,\dots,n\}$ (excluding $A_{n+1}$); the second, negated, ranges over all size-$(k{+}1)$ subsets of $\{1,\dots,n+1\}$ that *include* $A_{n+1}$ (re-indexing $k\to k-1$). Together with the standalone $|A_{n+1}|$ term (the $k=1$, subset $\{n{+}1\}$ case), every subset of $\{1,\dots,n+1\}$ of every size $k=1,\dots,n+1$ is covered exactly once, with sign $(-1)^{k+1}$:
$$
\left|\bigcup_{i=1}^{n+1}A_i\right| = \sum_{k=1}^{n+1}(-1)^{k+1}\!\!\sum_{i_1<\cdots<i_k\le n+1}\!\! |A_{i_1}\cap\cdots\cap A_{i_k}|.
$$
:::

::: {.proof name="Alternative proof: per-element count"}
It suffices to show that the right-hand side counts each element $a$ exactly as the left-hand side does: once if $a$ lies in the union, and $0$ times otherwise.

**Case 1** ($a\notin\bigcup_i A_i$): Then $a$ lies in no $A_i$, hence in no intersection $A_{i_1}\cap\cdots\cap A_{i_k}$. It is counted $0$ times.

**Case 2** ($a\in\bigcup_i A_i$): Let
$$
M=\{\,i : a\in A_i\,\},\qquad m=|M|\ge1.
$$
Then $a\in A_{i_1}\cap\cdots\cap A_{i_k}$ iff $\{i_1,\dots,i_k\}\subseteq M$. For each $k\le m$, exactly $\binom{m}{k}$ of the $k$-subsets of indices lie inside $M$ (none for $k>m$), and each contributes $1$ with sign $(-1)^{k+1}$. So $a$ is counted
$$
\sum_{k=1}^{m}(-1)^{k+1}\binom{m}{k}
$$
times.

**Evaluating the sum**: By @cor-alternating-sum (valid since $m\ge1$),
$$
0=\sum_{k=0}^{m}(-1)^k\binom{m}{k} = 1-\sum_{k=1}^{m}(-1)^{k+1}\binom{m}{k},
$$
so $a$ is counted exactly once.
:::

::: {#exm-ie-triple-member .example}
An element lying in all of $A,B,C$ is counted $3-3+1=1$ times by the three-set formula: the case $m=3$.
:::

::: {#cor-ie-dual .corollary name="Dual form -- intersection via unions"}
$$
\left|\bigcap_{i=1}^n A_i\right| = \sum_{k=1}^n (-1)^{k+1} \sum_{1\le i_1<\cdots<i_k\le n} |A_{i_1}\cup\cdots\cup A_{i_k}|.
$$
:::

::: {.remark name="Proof strategy"}
Either repeat the induction above with $\cup\leftrightarrow\cap$ swapped throughout, or apply the theorem above to $\overline{A_1},\dots,\overline{A_n}$ and De Morgan's laws (@sec-math-discrete-sets-set-operations).
:::
