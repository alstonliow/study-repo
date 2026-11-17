<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-proofs-03" status="draft"}
<!-- TODO: the Course Notes number their theorems differently; this answer
     uses the results as they appear in these notes. Owner to check. -->
Using the results of the Sets, Functions and Relations parts of these notes.
Some classifications are a matter of interpretation.

(a) **Implications** ("if … then …"): the cardinality results such as
    @thm-power-set-1, @prp-cartesian-product-1, @thm-counting-all-functions,
    @thm-counting-injections, @thm-counting-bijections-permutations and
    @thm-counting-binary-relations (if the sets have these sizes, then …);
    @prp-inverse-functions-1; @prp-composition-preserves-injectivity-surjectivity;
    @prp-properties-1; @thm-equivalence-relations-1 (if $R$ is an
    equivalence relation, then its classes form a partition).

(b) **Equivalences** ("if and only if"): @thm-inverse-functions-1,
    @thm-finite-equal-size-domain-codomain, @prp-symmetric-difference-1,
    @prp-composing-with-its-inverse.

(c) **Existential statements**: none of these assert existence on their own.
    The closest is @thm-inverse-functions-1 ("has an inverse function"),
    whose ($\Leftarrow$) direction proves that an inverse exists.

(d) **Universal statements**: essentially all of them. A theorem about
    "sets $A,B$" or "a function $f$" with no quantifier written is still
    asserted for *all* such objects; for example, De Morgan's laws
    (@thm-de-morgan-s-laws) hold for all sets $A,B$. Implications and
    equivalences of this kind are universally quantified implications and
    equivalences.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-1-q6" status="draft"}
(a) False. Seat the five people around a round table and let each person be friends exactly with their two neighbours. Any three people include two who are not neighbours, so no three are all friends. Any three people out of five around a circle include two neighbours, so no three are all strangers.

(b) True.

1. Fix a person $A$. Each of the other $5$ people is a friend or a stranger of $A$, so by the pigeonhole principle (@thm-pigeonhole) $A$ has at least $3$ friends or at least $3$ strangers. By symmetry, suppose $B,C,D$ are friends of $A$.

2. If two of $B,C,D$ are friends, those two and $A$ are three mutual friends.

3. Otherwise $B,C,D$ are three mutual strangers.
:::

::: {.solution for="prob-mit6042f10-1-q5" status="draft"}
*Contrapositive:* if $r^{1/5}$ is rational, then $r$ is rational.

Proof: suppose $r^{1/5}=\frac pq$ with integers $p,q$, $q\ne0$. Then $r=\bigl(r^{1/5}\bigr)^5=\frac{p^5}{q^5}$, a quotient of integers with $q^5\ne0$, so $r$ is rational. Since a statement and its contrapositive are equivalent, the original statement holds.
:::

::: {.solution for="prob-mit6042f10-9-q1" status="draft"}
(a) Split $\{1,\dots,2n\}$ into the $n$ pairs $\{1,2\},\{3,4\},\dots,\{2n-1,2n\}$. By the pigeonhole principle (@thm-pigeonhole), two of the $n+1$ chosen numbers lie in the same pair, so they are consecutive, $k$ and $k+1$. Any common divisor divides $(k+1)-k=1$, so they are relatively prime.

(b) A connected graph with $n\ge2$ vertices has no isolated vertex, so every degree lies in $\{1,\dots,n-1\}$. Then $n$ vertices take at most $n-1$ values, and two share a degree by the pigeonhole principle. (This is @thm-equal-degree.)
:::
