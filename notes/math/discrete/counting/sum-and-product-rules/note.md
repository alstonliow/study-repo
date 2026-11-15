---
title: Counting by Addition and Multiplication
sources: [fit1058-cn-8.1, fit1058-cn-8.2]
requires: []
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

::: {#fig-sum-and-product-rules-1}

```{=latex}
\begin{tikzpicture}[x=1cm, y=0.55cm, leaf/.style={font=\small}]
  \node[dot] (r) at (0,0) {};
  \foreach \i/\y in {1/3.3, 2/0, 3/-3.3} {
    \node[vertex, minimum size=5.5mm] (s\i) at (2,\y) {$\i$};
    \draw (r) -- (s\i);
    \foreach \b/\dy in {a/0.8, b/-0.8} {
      \node[leaf, anchor=west] (l\i\b) at (4,\y+\dy) {$(\i,\b)$};
      \draw (s\i) -- (l\i\b.west);
    }
  }
  \node[font=\scriptsize, text=notec] at (1.4,5.2) {step 1: $3$ options};
  \node[font=\scriptsize, text=notec] at (4.4,5.2) {step 2: $2$ options};
\end{tikzpicture}
```

A task in two independent steps, with $3$ and then $2$ options, has $3\cdot2=6$ outcomes, one for each leaf

:::

::: {#exm-product-rule-table .example}
An $r\times c$ table: summing every entry via nested loops costs $rc$ additions -- exactly $|\{1,\dots,r\}\times\{1,\dots,c\}|$.
:::
