<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-functions-23" status="draft"}
A binary relation on an $n$-set $A$ is any subset of $A\times A$, so there are
$2^{n^2}$ of them.

A reflexive relation must contain the $n$ pairs $(a,a)$ and may contain any of
the other $n^2-n$ pairs, so there are $2^{n^2-n}$ of them.

So the number of relations that are not reflexive is
$$2^{n^2} - 2^{n^2-n}.$$
:::

::: {.solution for="prob-functions-24" status="draft"}
A ternary relation is obtained by choosing three columns in order: a first,
second and third coordinate. Choosing the same columns in a different order
gives a different relation, since its triples are ordered differently.

With three different columns there are
$$n(n-1)(n-2)$$
choices. If a column may be used more than once, there are $n^3$.
:::
