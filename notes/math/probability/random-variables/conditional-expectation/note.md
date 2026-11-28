---
title: "Conditional Expectation"
sources: [mcs-18.4]
requires: [math/probability/random-variables/expectation-and-variance]
aliases: [math/probability/discrete/conditional-expectation]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Section 18.4, in our own wording; proofs written out in steps. -->

::: {#def-conditional-expectation .definition name="Conditional expectation"}

Let $X$ be a random variable and $A$ an event with $\Pr(A)>0$. The *conditional expectation* of $X$ given $A$ is
$$E[X\mid A]=\sum_xx\Pr(X=x\mid A),$$
the expectation of $X$ under the conditional probabilities $\Pr(\,\cdot\mid A)$ (@def-conditional-probability), when the sum converges absolutely.

:::

For a fair die $D$, $E[D\mid D\text{ is even}]=\frac{2+4+6}3=4$, while $E[D]=\frac72$.

::: {#thm-total-expectation .theorem name="Law of total expectation"}

If the events $A_1,A_2,\dots$ partition the sample space and each has positive probability, then
$$E[X]=\sum_iE[X\mid A_i]\Pr(A_i).$$

:::

::: {.proof}

1. By the law of total probability (@thm-law-of-total-probability), $\Pr(X=x)=\sum_i\Pr(X=x\mid A_i)\Pr(A_i)$ for every value $x$.

2. Multiply by $x$ and sum over $x$. The double sum converges absolutely (its absolute version is $E[|X|]$, computed the same way), so the order of summation may be exchanged:
   $$E[X]=\sum_x\sum_ix\Pr(X=x\mid A_i)\Pr(A_i)=\sum_i\Pr(A_i)\sum_xx\Pr(X=x\mid A_i)=\sum_iE[X\mid A_i]\Pr(A_i).$$

:::

::: {#fig-conditional-expectation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r) at (0,0) {$E[X]$};
\node[box] (a0) at (4,1.3) {$E[X\mid A_1]$};
\draw (r.east) -- node[edge label] {$\Pr(A_1)$} (a0.west);
\node[box] (a1) at (4,0) {$E[X\mid A_2]$};
\draw (r.east) -- node[edge label] {$\Pr(A_2)$} (a1.west);
\node[box] (a2) at (4,-1.3) {$E[X\mid A_3]$};
\draw (r.east) -- node[edge label] {$\Pr(A_3)$} (a2.west);
\end{tikzpicture}
\end{center}
```

The law of total expectation: average the conditional means $E[X\mid A_i]$ over the partition, weighting each by $\Pr(A_i)$

:::

Linearity holds for conditional expectations too: $E[aX+bY\mid A]=aE[X\mid A]+bE[Y\mid A]$, by @thm-linearity-of-expectation applied to the conditional probability.

::: {#exm-mean-time-to-failure .example name="Mean time to failure"}

A system fails each hour, independently, with probability $p>0$. Let $C$ be the hour of the first failure, and $m=E[C]$. Condition on the first hour (assuming $m$ is finite, which holds because $\Pr(C>k)=(1-p)^k$ decays geometrically):

1. With probability $p$ it fails in hour $1$: $E[C\mid\text{fail in hour 1}]=1$.

2. With probability $1-p$ it survives hour $1$, and from then on the process starts afresh, so $E[C\mid\text{survive hour 1}]=1+m$.

3. By @thm-total-expectation, $m=p\cdot1+(1-p)(1+m)$, so $pm=1$ and $m=\frac1p$.

This is the mean of the geometric distribution (@prp-standard-distributions-1-4), found without summing a series.

:::

::: {#fig-conditional-expectation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r) at (0,0) {hour $1$};
\node[box] (f) at (3.6,0.9) {fails: $C=1$};
\node[hl box] (s) at (3.6,-0.9) {survives: $C=1+C'$};
\draw[map] (r) -- node[edge label, above left] {$p$} (f);
\draw[map] (r) -- node[edge label, below left] {$1-p$} (s);
\node[lab, right, align=left] at (6.1,-0.9) {$C'$ has the same\\distribution as $C$};
\end{tikzpicture}
\end{center}
```

Conditioning on the first hour in @exm-mean-time-to-failure. After a survival the process starts afresh, so the remaining time $C'$ has mean $m$, which gives $m=p\cdot1+(1-p)(1+m)$.

:::

::: {#exm-conditional-expectation-two-children .example name="Waiting for a pattern"}

Flip a fair coin until heads appears twice in a row, and let $T$ be the number of flips. Let $a=E[T]$ and $b$ the expected number of further flips when the last flip was heads. Conditioning on the next flip:
$$a=1+\tfrac12b+\tfrac12a,\qquad b=1+\tfrac12\cdot0+\tfrac12a.$$
Substituting the second into the first, $a=1+\frac12+\frac14a+\frac12a$, so $a=6$. This is the first-step method of @exm-two-heads, which is the law of total expectation applied to the first step.

:::
