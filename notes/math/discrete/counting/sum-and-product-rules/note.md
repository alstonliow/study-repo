---
title: Counting by Addition and Multiplication
sources: [fit1058-cn-8.1, fit1058-cn-8.2]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note 08-counting-combinatorics.tex, §8.1–8.2. -->

## Counting by addition

::: {#thm-sum-rule .theorem name="Sum rule"}
If $A,B$ are disjoint finite sets, then $|A\cup B|=|A|+|B|$. More generally, for pairwise disjoint $A_1,\dots,A_m$:
$$
|A_1\cup A_2\cup\cdots\cup A_m| = |A_1|+|A_2|+\cdots+|A_m|.
$$
:::

::: {.remark name="Counting meaning"}
Already established set-theoretically at @sec-math-discrete-sets-set-operations. Combinatorially: choosing one item from $m$ pairwise disjoint option-sets has $\sum_i|A_i|$ total possibilities.
:::

::: {#exm-sum-rule-lists .example}
Two disjoint lists, lengths $r,c$; concatenating and summing all entries costs $r+c$ additions.
:::

::: {#thm-bijection-rule .theorem name='Bijection rule ("Zeroth Rule of Counting")'}
If there is a bijection $f: A\to B$ between finite sets $A,B$, then
$$
|A| = |B|.
$$
:::

::: {.remark name="Counting by correspondence"}
Every combinatorial argument below rests on this: to count a hard set, put it in one-to-one correspondence with an easy one. Bijections: @sec-math-discrete-functions-injections-surjections-bijections. Used for subsets $\leftrightarrow$ bit strings (@sec-math-discrete-sets-power-set), derangements (@sec-math-discrete-counting-derangements) and multisets $\leftrightarrow$ $0/1$ strings (@sec-math-discrete-counting-stars-and-bars).
:::

## Counting by multiplication

::: {#thm-product-rule .theorem name="Product rule"}
For finite $A,B$: $|A\times B| = |A|\cdot|B|$. More generally, for a task done in $m$ independent steps, with $n_i$ options at step $i$:
$$
\text{total options} = n_1\cdot n_2\cdots n_m.
$$
:::

::: {.remark name="Independence of the steps"}
Already established at @sec-math-discrete-sets-cartesian-product. "Independent" is essential: the count of options at step $i$ must not depend on earlier choices.
:::

::: {#exm-product-rule-table .example}
An $r\times c$ table: summing every entry via nested loops costs $rc$ additions -- exactly $|\{1,\dots,r\}\times\{1,\dots,c\}|$.
:::
