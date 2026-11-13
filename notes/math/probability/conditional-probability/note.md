---
title: "Independence and Conditional Probability"
sources: [fit1058-cn-9.7, fit1058-cn-9.8]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Independent events; Conditional probability. -->

## Independent events

::: {#def-independent .definition name="Independent"}

Events $A,B$ are *independent* if $\Pr(A\cap B) = \Pr(A)\cdot\Pr(B)$.

:::

::: {#exm-conditional-probability-1 .example}

Throw two dice. Let $A$: the first die shows $3$, and $B$: the second shows $5$. Then $\Pr(A)=\Pr(B)=\frac16$ and $A\cap B=\{(3,5)\}$, so $\Pr(A\cap B)=\frac1{36}=\Pr(A)\Pr(B)$. The events are independent, as expected for two separate dice.

:::

::: {#exm-independence-can-be-subtle .example name="Independence can be subtle"}

Now let $A$: the total is $7$, and $B$: the second die is one more than the first, capped at $6$, so $B=\{(1,2),(2,3),(3,4),(4,5),(5,6),(6,6)\}$. Both events depend on both dice, yet $\Pr(A)=\Pr(B)=\frac16$ and $A\cap B=\{(3,4)\}$, so $\Pr(A\cap B)=\frac1{36}=\Pr(A)\Pr(B)$. They are independent.

:::

::: {.remark name="Reason from the definition"}

Independence must be checked from the probabilities, not from intuition about “separate mechanisms”. Note also that independent is different from mutually exclusive: if $\Pr(A),\Pr(B)>0$ and $A\cap B=\emptyset$, then $\Pr(A\cap B)=0\ne\Pr(A)\Pr(B)$.

:::

::: {#def-mutual-independence-events .definition name="Mutual independence, $n$ events"}

$A_1,\dots,A_n$ are *mutually independent* if for *every* subset $\{i_1,\dots,i_k\}\subseteq\{1,\dots,n\}$,
$$\Pr(A_{i_1}\cap\cdots\cap A_{i_k}) = \Pr(A_{i_1})\cdots\Pr(A_{i_k}).$$

:::

::: {#exm-network-reliability .example name="Network reliability"}

Each link of a network survives with probability $p$, independently.

- Two links in series, $S$–$M$–$T$: a path survives iff both links do, so the probability is $p\cdot p=p^2$.

- Two parallel links between $S$ and $T$: a path survives iff at least one link does. The complement is that both fail, with probability $(1-p)^2$, so the probability is $1-(1-p)^2=2p-p^2$.

:::

## Conditional probability

::: {#def-conditional-probability .definition name="Conditional probability"}

For $\Pr(B)>0$, the probability of $A$ *given* $B$ is
$$\Pr(A\mid B) = \frac{\Pr(A\cap B)}{\Pr(B)}.$$

:::

::: {.remark name="Restricting the sample space"}

Conditioning on $B$ means treating $B$ as the new sample space: we keep only the outcomes in $B$ and rescale their probabilities so they add up to $1$.

:::

::: {#exm-conditional-probability-1-2 .example}

In Scrabble, $\Pr(\text{vowel})=0.42$ is not the proportion of *letter* tiles that are vowels, because of the two blanks. Since every vowel tile is non-blank,
$$\Pr(\text{vowel}\mid\text{not blank})=\frac{\Pr(\text{vowel})}{\Pr(\text{not blank})}=\frac{0.42}{0.98}\approx0.43.$$

:::

::: {#prp-independence-restated .proposition name="Independence restated"}

If $\Pr(B)>0$, then $A,B$ are independent if and only if $\Pr(A\mid B)=\Pr(A)$.

:::

::: {.proof}

$\Pr(A\mid B)=\Pr(A)$ iff $\Pr(A\cap B)/\Pr(B)=\Pr(A)$ iff $\Pr(A\cap B)=\Pr(A)\Pr(B)$.

:::

::: {.remark name="Meaning"}

$A$ and $B$ are independent exactly when learning that $B$ happened does not change the probability of $A$.

:::

::: {#prp-multiplication-rule .proposition name="Multiplication rule"}

$\Pr(A\cap B) = \Pr(B)\cdot\Pr(A\mid B)$.

:::
