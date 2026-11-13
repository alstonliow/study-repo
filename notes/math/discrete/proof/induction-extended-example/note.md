---
title: "Induction: extended example"
sources: [fit1058-cn-3.12]
requires: [math/discrete/relations/binary-relations]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/03-proofs.tex: Induction: extended example. -->

::: {.remark name="Setup"}

$m$ job positions $A$ ($|A|=m$), $n$ applicants $B$ ($|B|=n$), a *shortlist relation* $S \subseteq A\times B$.

For $X \subseteq A$, write
$$S(X) = \bigcup_{a\in X} S(a)$$
(@sec-math-discrete-relations-binary-relations notation) for the combined shortlist of positions in $X$.

A valid assignment (every position filled, no applicant doubled) is exactly an *injection* $A \to B$ contained in $S$.

:::

::: {#thm-necessity-cn-thm-20 .theorem name="Necessity, CN Thm 20"}

If $S$ contains an injection with domain $A$, then $|X| \le |S(X)|$ for every $X \subseteq A$.

:::

::: {.proof}

An injection assigns distinct applicants to distinct positions, so the positions in $X$ alone already require $|X|$ distinct applicants, all drawn from $S(X)$.

:::

::: {#thm-sufficiency-cn-thm-21 .theorem name="Sufficiency, CN Thm 21"}

If $|X| \le |S(X)|$ for every $X \subseteq A$, then $S$ contains an injection with domain $A$.

:::

::: {.proof}

Induction on $m=|A|$.

**Base case** ($m=1$):

$A=\{a\}$; the condition with $X=\{a\}$ gives $|S(a)|\ge1$, so pick any $(a,b)\in S$ – this single pair is an injection with domain $A$.

**Inductive step**: assume the theorem for all relations with domain-size $\le m$. Let $|A|=m+1$ and suppose $|X|\le|S(X)|$ for all $X\subseteq A$.

**Case 1**: every nonempty proper $X\subsetneq A$ has *strict* slack,
$$|X| \le |S(X)|-1.$$

Pick any $(a,b)\in S$. Restrict $S$ to
$$T = S \cap \big((A\setminus\{a\})\times(B\setminus\{b\})\big),$$
i.e. drop $a$ and $b$. For $X\subseteq A\setminus\{a\}$, the strict slack gives $|T(X)|\ge|X|$ even after excluding $b$.

Since $|A\setminus\{a\}|=m$, the inductive hypothesis applies: $T$ contains an injection $g$ with domain $A\setminus\{a\}$.

Then $g \cup \{(a,b)\}$ is an injection with domain $A$, contained in $S$.

**Case 2**: some nonempty proper $X\subsetneq A$ has *exact* fit,
$$|X|=|S(X)|.$$

Apply the inductive hypothesis to $S$ restricted to $X\times S(X)$ (domain size $|X|\le m$): get an injection $g: X \to S(X)$.

For the rest, $A\setminus X$: for any $Z\subseteq A\setminus X$, a counting argument using $|X\cup Z|\le|S(X\cup Z)|$ and $|S(X)|=|X|$ shows
$$|Z| \le |S(Z)\setminus S(X)|.$$

So the relation $U = S \cap \big((A\setminus X)\times(B\setminus S(X))\big)$ satisfies the same slack condition on domain $A\setminus X$ (size $\le m$), so by the inductive hypothesis, $U$ contains an injection $h$ with domain $A\setminus X$.

Since $g,h$ have disjoint domains ($X$, $A\setminus X$) and disjoint codomains ($S(X)$, $B\setminus S(X)$), $g\cup h$ is an injection with domain $A$, contained in $S$.

Cases 1 and 2 are exhaustive, completing the inductive step. By induction, the theorem holds for all $m$.

:::

::: {#cor-cn-cor-22 .corollary name="CN Cor. 22"}

$S \subseteq A\times B$ contains an injection with domain $A$ $\iff$ $|X|\le|S(X)|$ for every $X\subseteq A$.

:::

::: {.remark name="Why this matters"}

This gives easily *verifiable* evidence in both directions: a “yes” is witnessed by the injection itself (checkable directly); a “no” is witnessed by a single offending set $X$ with $|X|>|S(X)|$ – no need to search the whole space of possible assignments. This is a defect-form statement of *Hall’s marriage theorem*.

:::
