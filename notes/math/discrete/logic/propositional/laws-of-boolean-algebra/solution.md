<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-propositional-08"}
**(a)** Switches $x,y$ in series (current must pass through both):
$$x\wedge y$$

Switches $x,y$ in parallel (current can pass through either):
$$x\vee y$$

**(b)** Left circuit: $v$–$y$ in series form one branch, $w$–$z$ in series form another branch, and the two branches are in parallel:
$$(v\wedge y)\vee(w\wedge z)$$

Right circuit: $v$–$w$ in parallel form one stage, $y$–$z$ in parallel form another stage, and the two stages are in series:
$$(v\vee y)\wedge(w\vee z)$$

Comparing the two expressions: swapping $\wedge\leftrightarrow\vee$ throughout one expression gives the other. The two circuits are *duals* of each other, and the two Boolean expressions are dual expressions.

**(c)** This is a bridge (Wheatstone) circuit, with $x$ as the bridging switch. We compute by case analysis on $x$.

*When $x$ is False* (the bridge is open, so the circuit reduces to the non-crossed form from (b)):
$$\neg x\wedge\big((v\wedge y)\vee(w\wedge z)\big)$$

*When $x$ is True* (the bridge is closed, shorting the two middle nodes together, so $v,w$ become parallel into the shared node, and $y,z$ become parallel out of it, in series with each other):
$$x\wedge (v\vee w)\wedge(y\vee z)$$

Combining the two cases:
$$\big(x\wedge(v\vee w)\wedge(y\vee z)\big)\vee\big(\neg x\wedge((v\wedge y)\vee(w\wedge z))\big)$$

**Simplification.** Expanding $x\wedge(v\vee w)\wedge(y\vee z)$ by distributivity:
$$x\wedge(v\vee w)\wedge(y\vee z) \equiv (x\wedge v\wedge y)\vee(x\wedge v\wedge z)\vee(x\wedge w\wedge y)\vee(x\wedge w\wedge z)$$

and the other branch is already
$$\neg x\wedge((v\wedge y)\vee(w\wedge z)) \equiv (\neg x\wedge v\wedge y)\vee(\neg x\wedge w\wedge z).$$

Collecting all six terms:
$$(x\wedge v\wedge y)\vee(x\wedge v\wedge z)\vee(x\wedge w\wedge y)\vee(x\wedge w\wedge z)\vee(\neg x\wedge v\wedge y)\vee(\neg x\wedge w\wedge z)$$

The pairs $(x\wedge v\wedge y)\vee(\neg x\wedge v\wedge y)$ and $(x\wedge w\wedge z)\vee(\neg x\wedge w\wedge z)$ each factor out, using $x\vee\neg x\equiv\mathsf{True}$:
$$(x\wedge v\wedge y)\vee(\neg x\wedge v\wedge y)\equiv (v\wedge y)\wedge(x\vee\neg x)\equiv v\wedge y,$$
$$(x\wedge w\wedge z)\vee(\neg x\wedge w\wedge z)\equiv (w\wedge z)\wedge(x\vee\neg x)\equiv w\wedge z.$$

The remaining two terms, $(x\wedge v\wedge z)$ and $(x\wedge w\wedge y)$, do not simplify further. Hence:
$$(v\wedge y)\vee(w\wedge z)\vee(x\wedge v\wedge z)\vee(x\wedge w\wedge y)$$
:::

::: {.solution for="prob-propositional-04" status="draft"}
The laws are
$$P\wedge(Q\vee R) = (P\wedge Q)\vee(P\wedge R),\qquad P\vee(Q\wedge R) = (P\vee Q)\wedge(P\vee R).$$
Prove each by cases on $P$.

1. *First law, $P$ false.* Both sides are false: the left because of
   $P\wedge\ldots$, the right because both disjuncts contain $P\wedge$.

2. *First law, $P$ true.* The left side is $Q\vee R$. The right side is
   $(\mathrm T\wedge Q)\vee(\mathrm T\wedge R) = Q\vee R$.

3. *Second law, $P$ true.* Both sides are true.

4. *Second law, $P$ false.* The left side is $Q\wedge R$. The right side is
   $(\mathrm F\vee Q)\wedge(\mathrm F\vee R) = Q\wedge R$.

In every case the two sides agree, so both laws hold.
:::

::: {.solution for="prob-propositional-05" status="draft"}
Yes, parentheses are needed: the two readings are not equivalent.

1. Take $a = \mathrm F$ and $c = \mathrm T$. Then $a\wedge(b\vee c)$ is false
   but $(a\wedge b)\vee c$ is true.

2. $a\wedge(b\vee c)$ implies $(a\wedge b)\vee c$. If the left side is true,
   then $a$ is true and one of $b,c$ is true. If $b$ is true, then $a\wedge b$
   is true; if $c$ is true, the right side is true directly.

3. The converse fails, by the assignment in step 1.

(By the usual convention that $\wedge$ binds more tightly than $\vee$,
$a\wedge b\vee c$ means $(a\wedge b)\vee c$, but it is safer to write the
parentheses.)
:::

::: {.solution for="prob-propositional-07" status="draft"}
$$\begin{aligned}
&(\neg X\wedge\neg Y)\vee(\neg X\wedge Y)\vee(X\wedge Y)\\
&= \bigl(\neg X\wedge(\neg Y\vee Y)\bigr)\vee(X\wedge Y) && \text{distributive law}\\
&= \neg X\vee(X\wedge Y) && \neg Y\vee Y = \mathrm T\\
&= (\neg X\vee X)\wedge(\neg X\vee Y) && \text{distributive law}\\
&= \neg X\vee Y.
\end{aligned}$$
This is $X\Rightarrow Y$.
:::

::: {.solution for="prob-propositional-13" status="draft"}
There is exactly one distributive law: $\wedge$ distributes over $\oplus$,
but not the other way round.

1. $P\wedge(Q\oplus R) = (P\wedge Q)\oplus(P\wedge R)$. If $P$ is false,
   both sides are false. If $P$ is true, both sides are $Q\oplus R$.

2. $P\oplus(Q\wedge R)\ne(P\oplus Q)\wedge(P\oplus R)$ in general. Take
   $P = Q = \mathrm T$ and $R = \mathrm F$: the left side is
   $\mathrm T\oplus\mathrm F = \mathrm T$, the right side is
   $\mathrm F\wedge\mathrm T = \mathrm F$.

This matches ordinary arithmetic: $\oplus$ is addition mod $2$ and $\wedge$
is multiplication mod $2$. Multiplication distributes over addition, but
addition does not distribute over multiplication.
:::
