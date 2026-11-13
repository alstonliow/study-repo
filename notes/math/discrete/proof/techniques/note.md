---
title: "Proof by Manipulation, Construction and Cases"
sources: [fit1058-cn-3.6, fit1058-cn-3.7, fit1058-cn-3.8]
requires: [math/discrete/proof/finding-proofs]
status: draft
---

<!-- Migrated from 1058note notes/chapters/03-proofs.tex: Proof by symbolic manipulation; Proof by construction; Proof by cases. -->

## Proof by symbolic manipulation

::: {.remark name="The pattern"}

A chain of equations, each step justified by a known law (axiom or previously proved fact), linking the two sides of the claim.

:::

::: {#exm-difference-of-two-squares .example name="Difference of two squares"}

$$(x-y)(x+y) = x^2 - y^2.$$

:::

::: {.proof}

$$\begin{aligned}
(x-y)(x+y) &= x^2 + xy - yx - y^2 && \text{(distributive law)} \\
&= x^2 + xy - xy - y^2 && \text{(commutativity of multiplication)} \\
&= x^2 - y^2 && \text{(additive cancellation)}.
\end{aligned}$$

:::

## Proof by construction

::: {.remark name="Pattern"}

Describe a specific object precisely, and show it exists and satisfies the required conditions – a *constructive* proof of an existential statement (@sec-math-discrete-proof-finding-proofs). Theorem 14 (‘rotator’ is a palindrome) is an example.

:::

::: {.remark name="Two mistakes to avoid"}

- Using construction to attempt a *universal* statement: exhibiting one object with a property never establishes that *every* object has it.

- Mistaking an illustrative example for a proof: an example can clarify a proof’s ideas, but is not itself a proof unless the statement being proved is genuinely existential.

:::

::: {#exm-ramanujan-s-taxicab-number-extra .example name="Ramanujan's taxicab number (extra)"}

There is a positive integer expressible as the sum of two positive cubes in two genuinely different ways.

:::

::: {.proof}

$$1729 = 10^3 + 9^3 = 1000 + 729 = 12^3 + 1^3 = 1728 + 1.$$
Both decompositions use positive integers, and $\{10,9\} \neq \{12,1\}$, so these are two different ways.

:::

::: {.remark}

This is the smallest such number – hence its fame as the “taxicab number,” from the (possibly apocryphal) anecdote of Hardy visiting Ramanujan in a taxi numbered 1729.

:::

## Proof by cases

::: {#exm-nonconstructive-existence-via-cases .example name="Nonconstructive existence via cases"}

There exist irrational numbers $x, y$ such that $x^y$ is rational.

:::

::: {.proof}

Consider $\sqrt{2}^{\sqrt{2}}$. Either it is rational or it is irrational – these are the only two (exhaustive) cases.

**Case 1: $\sqrt{2}^{\sqrt{2}}$ is rational.** Take $x = y = \sqrt{2}$, both irrational, with $x^y$ rational by assumption. Done.

**Case 2: $\sqrt{2}^{\sqrt{2}}$ is irrational.** Take $x = \sqrt{2}^{\sqrt{2}}$ (irrational, by this case’s assumption) and $y = \sqrt{2}$ (irrational). Then
$$x^y = \left(\sqrt{2}^{\sqrt{2}}\right)^{\sqrt{2}} = \sqrt{2}^{\sqrt{2}\cdot\sqrt{2}} = \sqrt{2}^2 = 2,$$
which is rational. Done.

Either way, such $x,y$ exist.

:::

::: {.remark name="Strikingly nonconstructive"}

This proves the statement true *without ever determining which case actually holds* – we don’t know, from this proof alone, whether $\sqrt2^{\sqrt2}$ itself is rational or irrational. (It is, in fact, irrational – even transcendental, by the Gelfond–Schneider theorem – but that fact is not needed here.) This is the clearest illustration of the constructive/nonconstructive distinction from @sec-math-discrete-proof-finding-proofs.

:::
