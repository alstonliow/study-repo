---
title: "Injections, surjections, bijections"
sources: [fit1058-cn-2.7]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Injections, surjections, bijections. -->

::: {#def-injective-one-to-one .definition name="Injective / one-to-one"}

$f: A \to B$ is *injective* (an *injection*, *one-to-one*) if distinct arguments always give distinct values:
$$\forall x_1, x_2 \in A,\quad x_1 \neq x_2 \implies f(x_1) \neq f(x_2).$$

:::

::: {.remark name="Contrapositive phrasing"}

Equivalently (contrapositive):
$$\forall x_1, x_2 \in A,\quad f(x_1) = f(x_2) \implies x_1 = x_2.$$
This is the form most useful in proofs: assume $f(x_1)=f(x_2)$ and derive $x_1=x_2$.

:::

::: {.remark name="Injections preserve information"}

Every $y$ in the image of an injection has a *unique* preimage, so knowing $y$ determines $x$ uniquely. A non-injective function is *lossy* (some inputs become indistinguishable from their output); an injective one is *lossless*.

:::

::: {#def-surjective-onto .definition name="Surjective / onto"}

$f: A \to B$ is *surjective* (a *surjection*, *onto*) if
$$\forall y \in B,\ \exists x \in A \text{ such that } f(x) = y,$$
i.e. the image equals the codomain.

:::

::: {#def-bijective .definition name="Bijective"}

$f$ is *bijective* (a *bijection*, *one-to-one correspondence*) if it is both injective and surjective.

:::

::: {.remark name="Permutation"}

A bijection $f: A \to A$ (domain = codomain) is also called a *permutation* of $A$ – usually reserved for finite $A$.

:::

::: {#thm-finite-equal-size-domain-codomain .theorem name="Finite equal-size domain/codomain"}

Let $f: A \to B$ with $A, B$ finite and $|A| = |B|$. Then $f$ is injective $\iff$ $f$ is surjective $\iff$ $f$ is bijective.

:::

::: {.proof name="Proof by induction on $n = |A| = |B|$"}

We show: $f$ injective $\implies$ $f$ bijective. (The surjective case is symmetric, swapping the roles of $A$ and $B$ throughout.)

**Base case** ($n=0$): $A = B = \emptyset$. The unique function $\emptyset \to \emptyset$ is vacuously injective and vacuously surjective, hence bijective.

**Inductive step**: Suppose the claim holds for all injective functions between finite sets of size $n-1$. Let $f: A \to B$ be injective with $|A| = |B| = n \ge 1$.

Pick any $a \in A$ and let $b = f(a)$. Set $A' = A \setminus \{a\}$, $B' = B \setminus \{b\}$, and let $f' = f|_{A'}$ be the restriction of $f$ to $A'$.

- *$f'$ maps into $B'$*: for $x \in A'$ we have $x \neq a$, so by injectivity of $f$, $f(x) \neq f(a) = b$; hence $f(x) \in B \setminus \{b\} = B'$.

- *$f'$ is injective*: it is a restriction of the injective function $f$.

- $|A'| = |B'| = n-1$.

By the inductive hypothesis, $f' : A' \to B'$ is bijective, in particular surjective onto $B'$.

Now take any $y \in B$. Either $y = b$, in which case $y = f(a)$; or $y \in B'$, in which case surjectivity of $f'$ gives some $x \in A'$ with $f(x) = f'(x) = y$. Either way, $y$ has a preimage under $f$. So $f$ is surjective onto $B$, and being injective by hypothesis, $f$ is bijective.

By induction, the claim holds for all $n \ge 0$.

:::

::: {.remark}

This theorem requires *finite* $A, B$ of equal size – it fails for infinite sets (e.g. $f:\mathbb{N}\to\mathbb{N},\ f(x)=2x$ is injective but not surjective, despite $|\mathbb{N}|=|\mathbb{N}|$ in the infinite-cardinality sense).

:::

::: {.remark name="Proof strategies for injectivity and surjectivity"}

To prove $f: A \to B$ is **injective**: let $x_1, x_2 \in A$ be arbitrary with $f(x_1) = f(x_2)$, and show $x_1 = x_2$ follows (direct proof of the contrapositive form).

To prove $f$ is **not injective**: exhibit specific $x_1 \neq x_2 \in A$ with $f(x_1) = f(x_2)$ (one counterexample suffices).

To prove $f$ is **surjective**: let $y \in B$ be arbitrary, and *construct* (or show the existence of) some $x \in A$ with $f(x) = y$ – typically by solving $f(x) = y$ for $x$ in terms of $y$ and checking $x \in A$.

To prove $f$ is **not surjective**: exhibit a specific $y \in B$ for which no $x \in A$ satisfies $f(x) = y$ (one counterexample suffices).

:::
