<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-1-08" status="draft"}
1. By De Morgan's law, $\overline{A\cup B} = \overline A\cap\overline B$.

2. For any event $E$, $\Pr(E) = 1 - \Pr(\overline E)$, because $E$ and
   $\overline E$ are disjoint and their union is the whole sample space.

3. Apply step 2 with $E = A\cup B$, then step 1:
   $$\Pr(A\cup B) = 1 - \Pr(\overline{A\cup B}) = 1 - \Pr(\overline A\cap\overline B).$$
:::

::: {.solution for="prob-probability-1-09" status="draft"}
Let $P(n)$ be the statement for $n$ sets.

1. *Base case $n=0$.* The union of no sets is $\emptyset$, and
   $\Pr(\emptyset) = 0$, which is the empty sum. (For $n = 1$ both sides
   are $\Pr(A_1)$.)

2. *Inductive step.* Assume $P(n)$, and let $A_1,\dots,A_{n+1}$ be mutually
   disjoint. Put $B = A_1\sqcup\cdots\sqcup A_n$.

3. $B$ and $A_{n+1}$ are disjoint: an element of both would lie in some
   $A_k$ with $k\le n$ and in $A_{n+1}$, which are disjoint.

4. By the additivity axiom for two disjoint events and then $P(n)$:
   $$\Pr(B\sqcup A_{n+1}) = \Pr(B) + \Pr(A_{n+1}) = \sum_{k=1}^n\Pr(A_k) + \Pr(A_{n+1}) = \sum_{k=1}^{n+1}\Pr(A_k).$$

5. This is $P(n+1)$. By induction, $P(n)$ holds for all $n\in\mathbb N$.
:::

::: {.solution for="prob-probability-1-12" status="draft"}
A fixed-point-free permutation is a *derangement*. Let $D_n$ be the number of
derangements of an $n$-set, so the probability is $D_n/n!$.

- $n = 2$: only the swap, so $D_2 = 1$ and the probability is $\frac12$.
- $n = 3$: the two $3$-cycles, so $D_3 = 2$ and the probability is $\frac26 = \frac13$.
- $n = 5$: by inclusion–exclusion,
  $$D_5 = 5!\Bigl(1 - \frac1{1!} + \frac1{2!} - \frac1{3!} + \frac1{4!} - \frac1{5!}\Bigr) = 120 - 120 + 60 - 20 + 5 - 1 = 44,$$
  so the probability is $\frac{44}{120} = \frac{11}{30}\approx 0.367$.

The probabilities approach $1/e\approx 0.368$ as $n$ grows.
:::
