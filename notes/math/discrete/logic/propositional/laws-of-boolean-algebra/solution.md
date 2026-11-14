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

::: {.solution for="prob-propositional-04"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-propositional-05"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-propositional-07"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-propositional-13"}
<!-- TODO: solution -->
:::
