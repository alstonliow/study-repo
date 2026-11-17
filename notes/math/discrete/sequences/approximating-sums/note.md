---
title: "Approximating Sums and Products"
sources: [mcs-13.1, mcs-13.2, mcs-13.3, mcs-13.4, mcs-13.5]
requires: [math/discrete/sequences/sums-and-series, math/discrete/sequences/big-o]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Sections 13.1-13.5, in our own wording; proofs written out in steps. Calculus (integrals, logarithms) is assumed. -->

## Annuities: geometric sums at work

::: {#exm-annuity-value .example name="The value of an annuity"}

An annuity pays $m$ dollars at the start of each of $n$ years. If money earns interest at rate $p$ per year, a dollar paid $k$ years from now is worth $x^k$ dollars today, where $x=\frac1{1+p}$. So the annuity is worth
$$V=\sum_{k=0}^{n-1}m\,x^k=m\,\frac{1-x^n}{1-x}=m\,\frac{1+p-(1+p)^{1-n}}{p}$$
by the geometric sum formula (@exm-well-ordering-geometric-sum). For example, $m=50\,000$, $n=20$ and $p=6\%$ give $V\approx607\,906$, far less than the $1\,000\,000$ paid in total. As $n\to\infty$, $V\to\frac{m(1+p)}p$: even an annuity paying forever has a finite value (@thm-convergence-condition).

:::

## Sums by integrals

::: {#thm-integral-bounds .theorem name="Bounding a sum by integrals"}

Let $f$ be a non-negative function on $[1,n]$, let $S=\sum_{i=1}^nf(i)$ and $I=\int_1^nf(x)\,dx$.

1. If $f$ is increasing, then $I+f(1)\le S\le I+f(n)$.
2. If $f$ is decreasing, then $I+f(n)\le S\le I+f(1)$.

:::

::: {.proof}

1. Let $f$ be increasing. On $[i,i+1]$ we have $f(i)\le f(x)\le f(i+1)$, so $f(i)\le\int_i^{i+1}f\le f(i+1)$ for $1\le i\le n-1$.

2. Summing the right inequalities over $i=1,\dots,n-1$ gives $I\le\sum_{i=2}^nf(i)=S-f(1)$; summing the left ones gives $\sum_{i=1}^{n-1}f(i)=S-f(n)\le I$.

3. For decreasing $f$ the inequalities in step 1 reverse, and so do the conclusions.

:::

::: {#exm-sum-of-square-roots .example name="Sums of powers"}

For $f(x)=\sqrt x$ (increasing), $\int_1^n\sqrt x\,dx=\frac23\bigl(n^{3/2}-1\bigr)$, so
$$\tfrac23n^{3/2}+\tfrac13\le\sum_{i=1}^n\sqrt i\le\tfrac23n^{3/2}+\sqrt n-\tfrac23,$$
and $\sum_{i=1}^n\sqrt i\sim\frac23n^{3/2}$. In the same way $\sum_{i=1}^ni^k\sim\frac{n^{k+1}}{k+1}$ for every real $k>0$; for whole numbers $k$ there are exact formulas, such as $\sum i^2=\frac{n(n+1)(2n+1)}6$, which can be guessed from this leading term and proved by induction.

:::

::: {#cor-harmonic-bounds .corollary name="Size of the harmonic numbers"}

For $n\ge1$, $\ln(n+1)\le H_n\le1+\ln n$, where $H_n=\sum_{i=1}^n\frac1i$ (@def-harmonic-numbers). So $H_n\sim\ln n$.

:::

::: {.proof}

1. $f(x)=\frac1x$ is decreasing, with $\int_1^n\frac{dx}x=\ln n$. By @thm-integral-bounds, $H_n\le\ln n+1$.

2. For the lower bound, apply the same comparison on $[1,n+1]$: $\frac1i\ge\int_i^{i+1}\frac{dx}x$ for each $i$, and summing over $i=1,\dots,n$ gives $H_n\ge\ln(n+1)$.

:::

::: {#exm-book-overhang .example name="Stacking books over the edge of a table"}

Stack $n$ identical books of length $1$, one on top of another, each pushed out as far as possible beyond the one below without the stack toppling. Counting from the top, the stack of the top $k$ books balances on book $k+1$ when its centre of mass lies over the edge of that book. One computes that book $k+1$ can stick out $\frac1{2k}$ beyond the one below it, so the whole stack overhangs the table by
$$\sum_{k=1}^n\frac1{2k}=\frac{H_n}2\ \ge\ \frac{\ln(n+1)}2,$$
which grows without bound: with enough books the top book is as far out as you like. Four books already overhang by $\frac{H_4}2=\frac{25}{24}>1$, so the top book lies entirely beyond the table.

:::

## Products and Stirling's formula

To approximate a product, take logarithms and approximate the resulting sum.

::: {#prp-factorial-bounds .proposition name="Bounds on $n!$"}

For $n\ge1$,
$$\Bigl(\frac ne\Bigr)^n e\ \le\ n!\ \le\ \Bigl(\frac ne\Bigr)^n e\,n.$$

:::

::: {.proof}

1. $\ln n!=\sum_{i=1}^n\ln i$, and $f(x)=\ln x$ is increasing, with $\int_1^n\ln x\,dx=\bigl[x\ln x-x\bigr]_1^n=n\ln n-n+1$.

2. By @thm-integral-bounds, $n\ln n-n+1+\ln1\le\ln n!\le n\ln n-n+1+\ln n$.

3. Exponentiate: $e\,(n/e)^n\le n!\le e\,n\,(n/e)^n$.

:::

::: {#thm-stirling .theorem name="Stirling's formula"}

$$n!\sim\sqrt{2\pi n}\,\Bigl(\frac ne\Bigr)^n\qquad\text{as }n\to\infty.$$

:::

::: {#rmk-approximating-sums-stirling .remark name="How good is it"}

We do not prove Stirling's formula; @prp-factorial-bounds gives it up to a factor between $e$ and $en$, and the precise constant $\sqrt{2\pi}$ needs more analysis. In fact $\sqrt{2\pi n}(n/e)^ne^{1/(12n+1)}\le n!\le\sqrt{2\pi n}(n/e)^ne^{1/(12n)}$, so the relative error is already below $1\%$ for $n\ge10$. A typical use: $\binom{2n}n=\frac{(2n)!}{(n!)^2}\sim\frac{4^n}{\sqrt{\pi n}}$.

:::
