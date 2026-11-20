---
title: "Continuous Induction and Heine–Borel"
sources: [cama1-4]
requires: [math/analysis/real/continuity/extreme-and-intermediate-values]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 4.2 (a starred, non-examinable section), in our own wording; proofs written out in steps. Kept because the Heine–Borel theorem is the first appearance of compactness, which the metric-space and measure-theory notes build on. -->

Induction on $\mathbb N$ moves from $n$ to $n+1$. On an interval there is no "next" point, but the least upper bound property supports a continuous version: push forward a little, and pass to limits from the left.

::: {#thm-continuous-induction .theorem name="Continuous induction"}

Let $a<b$ and $A\subseteq[a,b]$ satisfy

1. $a\in A$;
2. if $x\in A$ and $x\ne b$, then some $y>x$ lies in $A$;
3. if every interval $(x-\varepsilon,x]$ with $\varepsilon>0$ meets $A$, then $x\in A$.

Then $b\in A$.

:::

::: {.proof}

1. $A$ is non-empty and bounded above by $b$; let $s=\sup A$.

2. For every $\varepsilon>0$, $s-\varepsilon$ is not an upper bound, so some point of $A$ lies in $(s-\varepsilon,s]$. By condition 3, $s\in A$.

3. If $s\ne b$, condition 2 gives a point of $A$ greater than $s$, contradicting that $s$ is an upper bound. So $b=s\in A$.

:::

A common way to use it: take $A=\{x\in[a,b]:\text{some property holds on }[a,x]\}$.

::: {#exm-compactness-of-closed-intervals-1 .example name="Boundedness by continuous induction"}

Let $f:[a,b]\to\mathbb R$ be continuous and $A=\{x\in[a,b]: f\text{ is bounded on }[a,x]\}$.

1. $a\in A$, since $f$ is bounded on $\{a\}$.

2. Continuity at any $x$ gives $\delta_x>0$ with $|f(y)-f(x)|<1$ for $|y-x|<\delta_x$, so $f$ is bounded by $|f(x)|+1$ on $(x-\delta_x,x+\delta_x)\cap[a,b]$.

3. If $x\in A$ and $x\ne b$, then $f$ is bounded on $[a,x]$ and on $[x,y]$ for $y=\min(x+\delta_x/2,b)$, hence on $[a,y]$: condition 2 holds.

4. If every $(x-\varepsilon,x]$ meets $A$, pick $y\in A$ with $y>x-\delta_x$. Then $f$ is bounded on $[a,y]$ and on $[y,x]$, hence on $[a,x]$: condition 3 holds.

5. So $b\in A$: $f$ is bounded on $[a,b]$, the first half of @thm-extreme-value-proof.

:::

## Open covers

::: {#def-open-cover .definition name="Cover by open intervals, finite subcover"}

A *cover* of $A\subseteq\mathbb R$ by open intervals is a family $\{I_\gamma:\gamma\in\Gamma\}$ of open intervals with $A\subseteq\bigcup_{\gamma\in\Gamma}I_\gamma$. A *finite subcover* is a finite subfamily $I_{\gamma_1},\dots,I_{\gamma_n}$ that still covers $A$.

:::

Not every cover has a finite subcover: the intervals $(\frac1n,1)$, $n\ge2$, cover $(0,1)$, but finitely many of them only reach down to the largest $\frac1n$ used.

::: {#thm-heine-borel-interval .theorem name="Heine–Borel theorem for intervals"}

Every cover of a closed bounded interval $[a,b]$ by open intervals has a finite subcover.

:::

::: {.proof}

1. Let $A=\{x\in[a,b]:[a,x]\text{ is covered by finitely many }I_\gamma\}$. We check the three conditions of @thm-continuous-induction.

2. $a$ lies in some $I_\gamma$, which alone covers $[a,a]$; so $a\in A$.

3. Let $x\in A$, $x\ne b$. Some $I_\gamma\ni x$; being open, it contains $[x,y]$ for some $y\in(x,b]$. Adding $I_\gamma$ to the finite family covering $[a,x]$ covers $[a,y]$, so $y\in A$.

4. Suppose every $(x-\varepsilon,x]$ meets $A$. Some $I_\gamma\ni x$ contains $(x-\varepsilon,x]$ for some $\varepsilon>0$. Pick $y\in A\cap(x-\varepsilon,x]$; a finite family covering $[a,y]$, together with $I_\gamma$, covers $[a,x]$. So $x\in A$.

5. By continuous induction $b\in A$, i.e. $[a,b]$ has a finite subcover.

:::

This property is called *compactness*: closed bounded intervals are compact, and open or unbounded intervals are not (the cover above, or the cover of $\mathbb R$ by the intervals $(-n,n)$).

::: {#exm-compactness-of-closed-intervals-2 .example name="Boundedness by Heine–Borel"}

Again let $f:[a,b]\to\mathbb R$ be continuous, with $\delta_x$ as in @exm-compactness-of-closed-intervals-1. The intervals $(x-\delta_x,x+\delta_x)$, $x\in[a,b]$, cover $[a,b]$; by @thm-heine-borel-interval finitely many, centred at $x_1,\dots,x_n$, already do. On the $i$-th of them $|f|<|f(x_i)|+1$, so on all of $[a,b]$
$$|f|<\max_i|f(x_i)|+1.$$
A local bound at each point becomes a global bound: this is the typical use of compactness.

:::
