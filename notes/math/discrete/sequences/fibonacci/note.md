---
title: "The Fibonacci sequence"
sources: [fit1058-cn-6.7]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/06-sequences-series.tex: The Fibonacci sequence. -->

::: {#def-fibonacci-sequence .definition name="Fibonacci sequence"}

$f_1=1$, $f_2=1$, and $f_n=f_{n-1}+f_{n-2}$ for $n\ge3$. It begins $1,1,2,3,5,8,13,21,34,55,\dots$

:::

::: {.remark name="No obvious formula"}

The recurrence does not suggest a formula. But the ratio $f_{n+1}/f_n$ seems to settle down (e.g. $f_{10}/f_9=55/34\approx1.618$), suggesting exponential growth at some fixed rate. We explore this with upper and lower bounds.

:::

### Upper bounds

::: {#prp-fibonacci-1 .proposition}

$f_n \le 2^n$ for all $n\ge1$.

:::

::: {.proof}

We use strong induction, with base cases $f_1=1\le2$ and $f_2=1\le4$. For the inductive step, let $k\ge2$ and assume the bound for $k$ and $k-1$. Then $f_{k+1}=f_k+f_{k-1}\le2^k+2^{k-1}<2^{k+1}$.

:::

::: {.remark name="Tightening the bound"}

The inductive step only used $2^k+2^{k-1}\le2^{k+1}$, i.e. (dividing by $2^{k-1}$) $2+1\le2^2$. Any $r$ with $r+1\le r^2$ would work in place of $2$, so the smallest such $r$ gives the best bound of this form.

:::

::: {#prp-best-bound-of-this-form .proposition name="Best bound of this form"}

Let $\varphi = \dfrac{1+\sqrt5}{2}\approx1.618$, the positive root of $r^2=r+1$. Then $f_n \le \varphi^n$ for all $n\ge1$.

:::

::: {.proof}

As before, by strong induction. The base cases are $f_1=1\le\varphi$ and $f_2=1\le\varphi^2$. For the inductive step, $f_{k+1}=f_k+f_{k-1}\le\varphi^k+\varphi^{k-1}=\varphi^{k-1}(\varphi+1)=\varphi^{k+1}$.

:::

### Lower bounds

::: {#prp-fibonacci-2 .proposition}

$f_n \ge \varphi^{n-2}$ for all $n\ge1$.

:::

::: {.proof}

By strong induction. The base cases are $f_1=1\ge\varphi^{-1}$ and $f_2=1=\varphi^0$. For the inductive step, $f_{k+1}=f_k+f_{k-1}\ge\varphi^{k-2}+\varphi^{k-3}=\varphi^{k-3}(\varphi+1)=\varphi^{k-1}$.

:::

### Asymptotic behaviour

::: {.remark name="Squeezing $f_n$"}

Together the bounds give $\varphi^{n-2} \le f_n \le \varphi^n$, i.e. $\varphi^{-2} \le f_n/\varphi^n \le 1$. So $f_n/\varphi^n$ stays between two constants: $f_n$ grows like $\varphi^n$, up to a bounded factor. The number $\varphi$ is the *golden ratio*.

:::

### An exact formula

::: {.remark name="Why two roots are needed"}

Since $\varphi^2=\varphi+1$, multiplying by $\varphi^{n-2}$ shows that $\varphi^n$ satisfies the Fibonacci recurrence. But a formula $\alpha\varphi^n$ has only one free constant, and cannot match both initial terms $f_1=f_2=1$. The other root of $r^2=r+1$, namely $\psi=\frac{1-\sqrt5}{2}\approx-0.618$, also gives a solution $\psi^n$. Since the recurrence is linear, $\alpha\varphi^n+\beta\psi^n$ is a solution for any $\alpha,\beta$, and now there are two constants to match the two initial terms.

:::

::: {#thm-binet .theorem name="Binet's formula"}

For all $n\ge1$,
$$f_n = \frac{\varphi^n - \psi^n}{\sqrt5}, \qquad \varphi=\frac{1+\sqrt5}{2},\quad \psi=\frac{1-\sqrt5}{2}.$$

:::

::: {.proof}

By the note above, $f_n = \alpha\varphi^n + \beta\psi^n$ satisfies the recurrence for any $\alpha,\beta$. Matching $f_1=f_2=1$ gives $\alpha\varphi+\beta\psi = 1$ and $\alpha\varphi^2+\beta\psi^2 = 1$. Solving, using $\varphi-\psi=\sqrt5$, gives $\alpha=\frac1{\sqrt5}$ and $\beta=-\frac1{\sqrt5}$. Since a sequence satisfying the recurrence is determined by its first two terms, $f_n=(\varphi^n-\psi^n)/\sqrt5$ for all $n$.

:::

::: {.remark name="Consistency with the bounds"}

Since $|\psi|<1$, $\psi^n\to0$, so $f_n \approx \varphi^n/\sqrt5$ for large $n$, consistent with $\varphi^{-2}\le f_n/\varphi^n\le1$. In fact $f_n$ is the integer nearest to $\varphi^n/\sqrt5$, since $|\psi^n/\sqrt5|<\frac12$. It is surprising that a formula full of $\sqrt5$ always gives integers: the irrational parts cancel.

:::
