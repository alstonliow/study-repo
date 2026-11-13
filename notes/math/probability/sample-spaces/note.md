---
title: "Probability and Sample Spaces"
sources: [fit1058-cn-9.1, fit1058-cn-9.2, fit1058-cn-9.3]
requires: [math/discrete/sequences/sums-and-series]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: The nature of randomness; Probability; Choice of sample space. -->

## The nature of randomness

::: {.remark name="Three sources of randomness"}

Randomness may come from a genuinely unpredictable physical process (a quantum measurement), from a deterministic process too complex to model exactly (a coin toss), or simply from an observer’s ignorance of a fixed but unknown outcome (a coin lying face down some distance away). Probability theory treats all three in the same way.

:::

## Probability

::: {#def-sample-space-event .definition name="Sample space, event"}

A random experiment has a set $U$ of all possible outcomes, called the *sample space*. An *event* is a subset $A\subseteq U$.

:::

::: {#def-probability-equally-likely-case .definition name="Probability, equally likely case"}

If $U$ is finite and every outcome is equally likely, then
$$\Pr(A) = \frac{|A|}{|U|}.$$

:::

::: {#exm-sample-spaces-1 .example}

For a fair coin, $U=\{\text{Heads},\text{Tails}\}$, and $\Pr(\emptyset)=0$, $\Pr(\{\text{Heads}\})=\Pr(\{\text{Tails}\})=\frac12$, $\Pr(U)=1$. For a fair die, $U=\{1,\dots,6\}$, so $\Pr(\text{odd})=\Pr(\{1,3,5\})=\frac12$, $\Pr(\text{square})=\Pr(\{1,4\})=\frac13$ and $\Pr(\text{not }1)=\frac56$.

:::

::: {#def-probability-general-case .definition name="Probability, general case"}

Assign a probability $\Pr(x)\in[0,1]$ to each outcome $x\in U$ so that $\sum_{x\in U}\Pr(x)=1$. The probability of an event is then $\Pr(A)=\sum_{x\in A}\Pr(x)$.

:::

::: {.remark name="Special cases"}

Always $\Pr(\emptyset)=0$ and $\Pr(U)=1$. The equally likely case is $\Pr(x)=1/|U|$ for every $x$. Outcomes need not be equally likely: in Scrabble, a tile drawn from the bag of $100$ is a blank with probability $2/100$.

:::

::: {#exm-infinite-sample-space .example name="Infinite sample space"}

Let $U=\mathbb{N}$ with $\Pr(n)=1/2^n$. This is a valid assignment, since $\sum_{n\ge1}1/2^n=\frac{1/2}{1-1/2}=1$ (@sec-math-discrete-sequences-sums-and-series). Then
$$\Pr(\text{odd}) = \sum_{k=1}^\infty \frac{1}{2^{2k-1}} = \frac{1/2}{1-1/4} = \frac{2}{3}.$$

:::

## Choice of sample space

::: {.remark name="Prefer equally likely outcomes"}

For two dice, the $11$ possible totals $2,\dots,12$ are not equally likely. Treating the dice as an *ordered* pair $(d_1,d_2)$ gives $36$ outcomes that *are* equally likely, each with probability $1/36$. A finer sample space with uniform probabilities is usually easier to work with. (An *unordered* pair would not do: $\{1,2\}$ arises in two ways but $\{1,1\}$ in only one.)

:::

::: {#exm-sample-spaces-1-2 .example}

The total is $8$ for the outcomes $(2,6),(3,5),(4,4),(5,3),(6,2)$, so $\Pr(\text{total is }8)=5/36$.

:::
