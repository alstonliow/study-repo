---
title: "Independence and Conditional Probability"
sources: [fit1058-cn-9.7, fit1058-cn-9.8, cs70-13.3.7, cs70-14.1, cs70-14.4]
requires: [math/probability/discrete/events]
aliases: [math/probability/conditional-probability]   # old ids (moved)
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

::: {#rmk-conditional-probability-1 .remark name="Reason from the definition"}

Independence must be checked from the probabilities, not from intuition about “separate mechanisms”. Note also that independent is different from mutually exclusive: if $\Pr(A),\Pr(B)>0$ and $A\cap B=\emptyset$, then $\Pr(A\cap B)=0\ne\Pr(A)\Pr(B)$.

:::

::: {#def-mutual-independence-events .definition name="Mutual independence, $n$ events"}

$A_1,\dots,A_n$ are *mutually independent* if for *every* subset $\{i_1,\dots,i_k\}\subseteq\{1,\dots,n\}$,
$$\Pr(A_{i_1}\cap\cdots\cap A_{i_k}) = \Pr(A_{i_1})\cdots\Pr(A_{i_k}).$$

:::

::: {#prp-mutual-independence-complements .proposition name="Mutual independence with complements"}

$A_1,\dots,A_n$ are mutually independent exactly when
$$\Pr(B_1\cap\cdots\cap B_n)=\Pr(B_1)\cdots\Pr(B_n)$$
for every choice of $B_i\in\{A_i,\overline{A_i}\}$, $i=1,\dots,n$. The definition above asks for the product formula on every subset of at least two events; this form asks for it on all $n$ events at once, but with each event possibly replaced by its complement. Proving the equivalence is an exercise.

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

::: {#rmk-conditional-probability-2 .remark name="Restricting the sample space"}

Conditioning on $B$ means treating $B$ as the new sample space: we keep only the outcomes in $B$ and rescale their probabilities so they add up to $1$.

:::

::: {#fig-conditional-probability-1}

```{=latex}
\begin{tikzpicture}
  \draw (-1.7,-1.55) rectangle (3.0,1.6);
  \node[anchor=north west] at (-1.7,1.6) {$U$};
  \fill[accentSoft] (1.3,0) circle (1.2);
  \fill[tintA] (0,0) circle (1.2);
  \begin{scope}
    \clip (0,0) circle (1.2);
    \fill[accentLight] (1.3,0) circle (1.2);
  \end{scope}
  \draw (0,0) circle (1.2);
  \draw[accent, bold] (1.3,0) circle (1.2);
  \node at (-0.6,0) {$A$}; \node at (1.95,0) {$B$};
  \node[note] at (0.65,0) {$A\cap B$};
\end{tikzpicture}
```

Conditioning on $B$: $B$ (outlined) becomes the new sample space, and $\Pr(A\mid B)$ is the share of $B$ taken up by $A\cap B$

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

::: {#rmk-conditional-probability-3 .remark name="Meaning"}

$A$ and $B$ are independent exactly when learning that $B$ happened does not change the probability of $A$.

:::

::: {#prp-multiplication-rule .proposition name="Multiplication rule"}

$\Pr(A\cap B) = \Pr(B)\cdot\Pr(A\mid B)$.

:::

::: {.proof}

If $\Pr(B)>0$, multiply both sides of @def-conditional-probability by $\Pr(B)$.

:::

::: {#thm-chain-rule .theorem name="Product rule (chain rule)"}

For events $A_1,\dots,A_n$ with $\Pr(A_1\cap\cdots\cap A_{n-1})>0$,
$$\Pr(A_1\cap\cdots\cap A_n)=\Pr(A_1)\,\Pr(A_2\mid A_1)\,\Pr(A_3\mid A_1\cap A_2)\cdots\Pr(A_n\mid A_1\cap\cdots\cap A_{n-1}).$$

:::

::: {.proof}

We use induction on $n$.

1. For $n=1$ both sides are $\Pr(A_1)$.

2. Let $n\ge2$ and assume the formula for $n-1$ events. Put $C=A_1\cap\cdots\cap A_{n-1}$, so $\Pr(C)>0$.

3. By @prp-multiplication-rule, $\Pr(A_1\cap\cdots\cap A_n)=\Pr(C\cap A_n)=\Pr(C)\,\Pr(A_n\mid C)$.

4. Each intersection $A_1\cap\cdots\cap A_j$ with $j\le n-1$ contains $C$, so it has positive probability, and the induction hypothesis applies to $\Pr(C)$. Substituting it into step 3 gives the formula for $n$ events.

:::

::: {#rmk-conditional-probability-4 .remark name="Read it as a sequence of choices"}

The product rule fits experiments that happen in stages, such as dealing cards one by one: multiply the probability of each stage given everything before it. With mutually independent events every conditional probability equals the unconditional one, and the rule becomes a plain product.

:::
