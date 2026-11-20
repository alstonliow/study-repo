---
title: "Ordered Fields and Completeness"
sources: [cama1-1, cama1-2]
requires: [math/discrete/relations/partial-orders, math/discrete/sets/subsets]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 1 and 2.1, in our own wording; proofs written out in steps. -->

The real numbers are not defined here as infinite decimals but by the properties they have: they form an ordered field in which every bounded set has a least upper bound. Everything in real analysis is derived from these axioms.

## Ordered fields

::: {#def-field .definition name="Field"}

A *field* is a set $F$ with two operations $+$ and $\times$ such that for all $a,b,c\in F$:

1. both operations are associative and commutative;
2. there are elements $0\ne 1$ with $a+0=a$ and $a\times 1=a$;
3. every $a$ has an additive inverse $-a$ with $a+(-a)=0$, and every $a\ne 0$ has a multiplicative inverse $a^{-1}$ with $a\times a^{-1}=1$;
4. $a\times(b+c)=a\times b+a\times c$.

:::

$\mathbb Q$, $\mathbb R$, $\mathbb C$ and the integers modulo a prime $p$ (@def-finite-field) are fields; $\mathbb Z$ is not, since $2$ has no multiplicative inverse in $\mathbb Z$.

::: {#def-ordered-field .definition name="Ordered field"}

An *ordered field* is a field $F$ with a strict linear order $<$ (@def-comparable-linear-order) that respects the operations: for all $x,y,z\in F$,
$$x<y \;\Rightarrow\; x+z<y+z, \qquad x<y \text{ and } z>0 \;\Rightarrow\; xz<yz.$$

:::

::: {#lem-square-nonnegative .lemma name="Squares are non-negative"}

In an ordered field, $x^2\ge 0$ for every $x$; in particular $1=1^2>0$.

:::

::: {.proof}

1. If $x=0$, then $x^2=0$.

2. If $x>0$, multiplying $0<x$ by $x>0$ gives $0<x^2$.

3. If $x<0$, adding $-x$ to both sides gives $0<-x$, so by step 2, $0<(-x)^2=x^2$.

4. Finally $1\ne 0$ and $1=1^2\ge 0$, so $1>0$.

:::

## Suprema and the least upper bound property

::: {#def-supremum-infimum .definition name="Upper bound, supremum, infimum"}

Let $X$ be an ordered set and $A\subseteq X$. An *upper bound* of $A$ is an $x\in X$ with $a\le x$ for all $a\in A$; if one exists, $A$ is *bounded above*. An upper bound $s$ is the *supremum* (least upper bound) of $A$, written $\sup A$, if no smaller element is an upper bound:
$$\text{(i) } a\le s \text{ for all } a\in A, \qquad \text{(ii) for every } y<s \text{ there is } a\in A \text{ with } a>y.$$
If $\sup A\in A$, it is the *maximum* $\max A$. Lower bounds, the *infimum* $\inf A$ and the minimum are defined in the same way with the order reversed.

:::

::: {#exm-supremum-in-q .example name="Suprema that do and do not exist"}

In $\mathbb R$, $\sup(0,1)=1$ but $(0,1)$ has no maximum, while $\max[0,1]=1$.

In $\mathbb Q$, the set $A=\{x\in\mathbb Q: x^2<2\}$ is bounded above (by $2$) but has no supremum in $\mathbb Q$: its supremum in $\mathbb R$ would be $\sqrt2$, which is irrational, and every rational upper bound $q>\sqrt 2$ can be lowered to a rational between $\sqrt2$ and $q$.

:::

::: {#def-least-upper-bound-property .definition name="Least upper bound property"}

An ordered set has the *least upper bound property* if every non-empty subset that is bounded above has a supremum.

:::

In an ordered field, the least upper bound property implies the corresponding property for infima: if $A$ is non-empty and bounded below, then $-A=\{-a:a\in A\}$ is bounded above and $\inf A=-\sup(-A)$.

::: {#def-real-numbers .definition name="Real numbers"}

The *real numbers* $\mathbb R$ form an ordered field with the least upper bound property.

:::

::: {#rmk-ordered-fields-and-completeness-1 .remark name="Existence and uniqueness"}

One can construct such a field (from $\mathbb Q$, by Dedekind cuts or by Cauchy sequences) and show that any two are isomorphic as ordered fields, so the definition describes exactly one object. These constructions are not needed for what follows: all results are deduced from the axioms.

:::

## The Archimedean property

In any field, write $2=1+1$, $3=2+1$, and so on; in an ordered field these are all positive and increasing, by @lem-square-nonnegative.

::: {#thm-archimedean-property .theorem name="Archimedean property"}

In an ordered field with the least upper bound property, the set $\{1,2,3,\dots\}$ is not bounded above. Equivalently, for every $x$ there is a natural number $n>x$, and
$$\lim_{n\to\infty}\frac1n=0.$$

:::

::: {.proof}

1. Suppose $\{1,2,3,\dots\}$ were bounded above. By the least upper bound property it would have a supremum $s$.

2. Since $s-1<s$, the number $s-1$ is not an upper bound, so some natural number $n$ satisfies $n>s-1$.

3. Then $n+1>s$, and $n+1$ is again in the set, contradicting that $s$ is an upper bound. So the set is not bounded above, which is the second form.

4. For the limit (@def-limit-of-a-sequence): given $\varepsilon>0$, pick a natural number $N>1/\varepsilon$ by the second form. For all $n\ge N$, $0<1/n\le 1/N<\varepsilon$.

:::

::: {#rmk-ordered-fields-and-completeness-2 .remark name="An ordered field that is not Archimedean"}

The least upper bound property is really needed. Take the field of rational functions $P(x)/Q(x)$ with real coefficients. Two different rational functions agree at only finitely many points, so one of them is larger than the other for all large $x$; call that one the larger. This makes the rational functions an ordered field. The constants $1,2,3,\dots$ are its natural numbers, and the function $x$ exceeds every one of them, so they are bounded above.

:::
