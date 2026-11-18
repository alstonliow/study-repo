---
title: "L'Hôpital's Rule"
sources: [mit1801-34]
requires: [math/calculus/single-variable/applications-of-derivatives/mean-value-theorem]
aliases: [math/calculus/applications-of-derivatives/lhopitals-rule]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 34, in our own wording; proofs written out in steps. Numbers checked in Python. -->

::: {#thm-cauchy-mean-value .theorem name="Cauchy mean value theorem"}

If $f,g$ are continuous on $[a,b]$, differentiable on $(a,b)$, and $g'\neq0$ there, then for some $c\in(a,b)$
$$\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)} .$$

:::

::: {.proof}

1. $g(b)\neq g(a)$, for otherwise @thm-rolle would give a zero of $g'$.

2. Let $h(x)=f(x)-Kg(x)$ with $K=\dfrac{f(b)-f(a)}{g(b)-g(a)}$; then $h(a)=h(b)$.

3. By @thm-rolle, $h'(c)=f'(c)-Kg'(c)=0$ for some $c$, which is the claim.

:::

::: {#thm-lhopital .theorem name="L'Hôpital's rule"}

Suppose $f(x)\to0$ and $g(x)\to0$ as $x\to a$ (or both tend to $\pm\infty$), and $g'\neq0$ near $a$. If $\lim_{x\to a}\dfrac{f'(x)}{g'(x)}=L$, then
$$\lim_{x\to a}\frac{f(x)}{g(x)}=L .$$
The same holds for one-sided limits and for $a=\pm\infty$.

:::

::: {.proof}

1. We prove the case $0/0$ with $x\to a^+$. Define $f(a)=g(a)=0$; then $f,g$ are continuous on $[a,x]$.

2. By @thm-cauchy-mean-value, $\dfrac{f(x)}{g(x)}=\dfrac{f(x)-f(a)}{g(x)-g(a)}=\dfrac{f'(c_x)}{g'(c_x)}$ for some $c_x\in(a,x)$.

3. As $x\to a^+$, $c_x\to a^+$, so the right side tends to $L$. The left limit is the same, and the other cases are similar (for $x\to\infty$, substitute $x=1/t$).

:::

::: {#exm-lhopital .example name="Typical uses"}

- $\displaystyle\lim_{x\to0}\frac{\sin 5x}{x}=\lim_{x\to0}\frac{5\cos5x}{1}=5$.
- $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^2}=\lim\frac{\sin x}{2x}=\lim\frac{\cos x}2=\frac12$ (the rule applied twice).
- $\displaystyle\lim_{x\to\infty}\frac{x^n}{e^x}=0$ after $n$ applications: exponentials beat powers.
- $\displaystyle\lim_{x\to\infty}\frac{\ln x}{x^a}=\lim\frac{1/x}{ax^{a-1}}=0$ for $a>0$: powers beat logarithms.

:::

::: {#exm-lhopital-other-forms .example name="Other indeterminate forms"}

Rewrite $0\cdot\infty$, $1^\infty$, $0^0$ and $\infty^0$ as quotients first. For $x^x$ as $x\to0^+$: $\ln x^x=x\ln x=\dfrac{\ln x}{1/x}\to\lim\dfrac{1/x}{-1/x^2}=\lim(-x)=0$, so $x^x\to e^0=1$.

:::

::: {#rmk-lhopital-check .remark name="Check the form first"}

The rule needs $0/0$ or $\infty/\infty$. For $\lim_{x\to1}\frac{x+1}{x}=2$, differentiating top and bottom would wrongly give $1$.

:::
