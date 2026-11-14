<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-propositional-06" status="draft"}
1. $A\Rightarrow C$ is equivalent to $\neg A\vee C$. With
   $A = P_1\wedge\cdots\wedge P_n$:
   $$(P_1\wedge\cdots\wedge P_n)\Rightarrow C\ =\ \neg(P_1\wedge\cdots\wedge P_n)\vee C.$$

2. By De Morgan's law for $n$ terms (apply the two-term law $n-1$ times),
   $$\neg(P_1\wedge\cdots\wedge P_n) = \neg P_1\vee\cdots\vee\neg P_n.$$

3. Substituting gives $\neg P_1\vee\cdots\vee\neg P_n\vee C$.
:::

::: {.solution for="prob-propositional-09" status="draft"}
No. Negating an implication does not reverse it:
$$\neg(P\Rightarrow Q) = \neg(\neg P\vee Q) = P\wedge\neg Q,\qquad P\Leftarrow Q = Q\Rightarrow P = P\vee\neg Q.$$

- They are not equivalent: with $P = Q = \mathrm T$, the first is false and
  the second is true.
- $\neg(P\Rightarrow Q)$ implies $P\Leftarrow Q$: whenever $P\wedge\neg Q$
  is true, $P$ is true, so $P\vee\neg Q$ is true.
- The converse fails, by the same assignment $P = Q = \mathrm T$.
:::

::: {.solution for="prob-propositional-11" status="draft"}
$P\oplus Q$ is true exactly when $P$ and $Q$ differ.

| $P$ | $Q$ | $P\oplus Q$ | $(P\wedge\neg Q)\vee(\neg P\wedge Q)$ | $(P\vee Q)\wedge(\neg P\vee\neg Q)$ |
|---|---|---|---|---|
| F | F | F | F | F |
| F | T | T | T | T |
| T | F | T | T | T |
| T | T | F | F | F |

(a) The middle expression is true exactly when one of $P,Q$ is true and the
    other false. Its column matches $P\oplus Q$.

(b) The last expression says "at least one is true" and "at least one is
    false". Its column also matches.
:::

::: {.solution for="prob-propositional-12" status="draft"}
(a) $P\vee Q = P\oplus Q\oplus(P\wedge Q)$.

    Check: if exactly one is true, the result is $\mathrm T\oplus\mathrm F = \mathrm T$.
    If both are true, it is $\mathrm F\oplus\mathrm T = \mathrm T$. If both
    are false, every part is false.

(b) $P\wedge Q = (P\vee Q)\oplus(P\oplus Q)$.

    Check: if both are true, it is $\mathrm T\oplus\mathrm F = \mathrm T$.
    If exactly one is true, it is $\mathrm T\oplus\mathrm T = \mathrm F$.
    If both are false, it is $\mathrm F\oplus\mathrm F = \mathrm F$.
:::
