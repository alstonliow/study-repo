---
title: "Relations and Counting Relations"
sources: [fit1058-cn-2.17, fit1058-cn-2.18]
requires: [math/discrete/sets/cartesian-product, math/discrete/sets/power-set]
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Relations; Counting relations. -->

## Relations

::: {#def-ternary-relation .definition name="Ternary relation"}

A *ternary relation* on sets $A,B,C$ is a subset of $A \times B \times C$: a set of triples $(x,y,z)$ with $x\in A,\ y\in B,\ z\in C$.

:::

::: {#def-ary-relation .definition name="$n$-ary relation"}

An *$n$-ary relation* on sets $A_1,A_2,\dots,A_n$ is a subset
$$R \subseteq A_1 \times A_2 \times \cdots \times A_n,$$
i.e. a set of $n$-tuples $(x_1,\dots,x_n)$ with $x_i \in A_i$ for each $i$. Each $A_i$ is the $i$-th *domain*; $n$ is the *degree*. An $n$-ary relation is also called an *$n$-ary predicate*.

:::

## Counting relations

::: {#thm-counting-binary-relations .theorem name="Counting binary relations"}

For finite $A,B$ with $|A|=m,\ |B|=n$:
$$\#\{\text{binary relations from } A \text{ to } B\} = 2^{mn}.$$
In particular, with $A=B$, $|A|=m$:
$$\#\{\text{binary relations on } A\} = 2^{m^2}.$$

:::

::: {#fig-relations-counting-1}

```{=latex}
\begin{tikzpicture}[x=0.9cm, y=0.9cm]
  \foreach \r/\a in {0/a,1/b,2/c} {
    \foreach \c/\b in {0/a,1/b,2/c}
      \filldraw[fill=black!5, draw=white, line width=1.5pt] (\c,-\r) rectangle (\c+1,-\r-1);
    \node[left, font=\small] at (0,-\r-0.5) {$\a$};
    \node[above, font=\small] at (\r+0.5,0) {$\a$};
  }
  \foreach \c/\r in {0/0, 1/0, 2/1, 0/2}
    \filldraw[fill=defc!45, draw=white, line width=1.5pt] (\c,-\r) rectangle (\c+1,-\r-1);
  \node[left, font=\small] at (-0.35,-1.5) {$x$}; \node[above, font=\small] at (1.5,0.4) {$y$};
\end{tikzpicture}
```

A relation on $\{a,b,c\}$ is a choice of cells $(x,y)$ in this $3\times3$ grid; the one shown is $\{(a,a),(a,b),(b,c),(c,a)\}$. Each of the $9$ cells is in or out, giving $2^9$ relations

:::

::: {.proof}

A binary relation from $A$ to $B$ is exactly a subset of $A \times B$, so the count equals $|\mathcal{P}(A\times B)| = 2^{|A\times B|}$ (@sec-math-discrete-sets-power-set). Since $|A\times B| = mn$ (@sec-math-discrete-sets-cartesian-product), this is $2^{mn}$. The case $A=B$ substitutes $n=m$.

:::

::: {#cor-counting-ary-relations .corollary name="Counting $n$-ary relations"}

For finite $A_1,\dots,A_n$ with $|A_i|=m_i$:
$$\#\{n\text{-ary relations on } A_1,\dots,A_n\} = 2^{m_1 m_2 \cdots m_n}.$$
If all $A_i = A$ with $|A|=m$: $2^{m^n}$.

:::

::: {.proof}

Identical argument: an $n$-ary relation is a subset of $A_1\times\cdots\times A_n$, of size $\prod_i m_i$ (@sec-math-discrete-sets-cartesian-product generalized), so the count is $2^{\prod_i m_i}$.

:::

::: {#exm-counting-relations-with-a-given .example name="Counting relations with a given property"}

Reflexive relations on $A$ with $|A|=m$: the $m$ diagonal pairs $(a,a)$ are forced *in*, leaving $m^2 - m$ off-diagonal pairs free to choose independently, so there are $2^{m^2-m}$ reflexive relations on $A$.

:::
