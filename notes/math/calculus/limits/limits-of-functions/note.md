---
title: "Limits of Functions"
sources: [mit1801-2]
requires: [math/calculus/limits/functions-and-graphs, math/discrete/sequences/limits]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 2, in our own wording; proofs written out in steps. -->

::: {#def-limit-of-a-function .definition name="Limit of a function"}

Let $f$ be defined near $a$ (except possibly at $a$). We write
$$\lim_{x\to a}f(x)=L$$
if for every $\varepsilon>0$ there is $\delta>0$ such that $0<\lvert x-a\rvert<\delta$ implies $\lvert f(x)-L\rvert<\varepsilon$.

:::

The value $f(a)$ plays no role: the limit only describes $f$ at points near $a$. This is the function version of @def-limit-of-a-sequence.

::: {#def-one-sided-limit .definition name="One-sided limits"}

$\lim_{x\to a^+}f(x)=L$ (right-hand limit) means the condition of @def-limit-of-a-function holds for $a<x<a+\delta$; $\lim_{x\to a^-}f(x)=L$ (left-hand limit) uses $a-\delta<x<a$.

:::

::: {#prp-limit-from-one-sided .proposition name="Two one-sided limits"}

$\lim_{x\to a}f(x)=L$ if and only if both one-sided limits exist and equal $L$.

:::

::: {.proof}

1. If the two-sided condition holds with some $\delta$, it holds in particular on each side.

2. Conversely, if $\delta_+$ works on the right and $\delta_-$ on the left, then $\delta=\min(\delta_+,\delta_-)$ works on both sides at once.

:::

::: {#prp-limit-laws-functions .proposition name="Limit laws for functions"}

If $\lim_{x\to a}f(x)=L$ and $\lim_{x\to a}g(x)=M$, then
$$\lim_{x\to a}(f\pm g)=L\pm M,\qquad \lim_{x\to a}fg=LM,\qquad \lim_{x\to a}\frac fg=\frac LM\ \ (M\neq0).$$

:::

The proofs are the same as for sequences (@prp-limit-laws). Together with $\lim_{x\to a}x=a$ they give $\lim_{x\to a}p(x)=p(a)$ for every polynomial $p$, and the same for rational functions where the denominator is not zero.

::: {#thm-squeeze-functions .theorem name="Squeeze theorem"}

If $g(x)\le f(x)\le h(x)$ for $x$ near $a$ and $\lim_{x\to a}g(x)=\lim_{x\to a}h(x)=L$, then $\lim_{x\to a}f(x)=L$.

:::

::: {.proof}

1. Given $\varepsilon>0$, choose $\delta$ so small that, for $0<\lvert x-a\rvert<\delta$, both $L-\varepsilon<g(x)$ and $h(x)<L+\varepsilon$, and the inequalities $g\le f\le h$ hold.

2. Then $L-\varepsilon<g(x)\le f(x)\le h(x)<L+\varepsilon$, so $\lvert f(x)-L\rvert<\varepsilon$.

:::

::: {#exm-limit-cancel .example name="Cancelling a common factor"}

$\displaystyle\lim_{x\to1}\frac{x^2-1}{x-1}=\lim_{x\to1}(x+1)=2$: the two functions agree for $x\neq1$, which is all the limit sees.

:::

::: {#exm-one-sided-different .example name="Different one-sided limits"}

For $f(x)=x/\lvert x\rvert$ we have $\lim_{x\to0^+}f=1$ and $\lim_{x\to0^-}f=-1$, so $\lim_{x\to0}f$ does not exist. For $1/x$ the one-sided limits at $0$ are $+\infty$ and $-\infty$ (the function is unbounded on both sides).

:::

::: {#def-limit-at-infinity .definition name="Limit at infinity"}

$\lim_{x\to\infty}f(x)=L$ means: for every $\varepsilon>0$ there is $N$ with $\lvert f(x)-L\rvert<\varepsilon$ for all $x>N$. Similarly for $x\to-\infty$.

:::

For example $\lim_{x\to\infty}\frac{3x^2+1}{x^2-5}=3$, by dividing top and bottom by $x^2$.
