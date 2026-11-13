---
title: "Predicates"
sources: [fit1058-cn-5.1, fit1058-cn-5.2, fit1058-cn-5.3, fit1058-cn-5.4]
requires: [math/discrete/functions/special-functions, math/discrete/relations/binary-relations, math/discrete/relations/counting]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/05-predicate-logic.tex: Relations, predicates, and truth-valued functions; Variables and constants; Predicates and variables; Arguments of predicates. -->

## Relations, predicates, and truth-valued functions

::: {#def-predicate .definition name="Predicate"}

A *predicate* is a relation (@sec-math-discrete-relations-binary-relations, @sec-math-discrete-relations-counting), used with intent to do logic with it. A predicate with $k$ arguments is *$k$-ary*.

:::

::: {#def-predicate-as-a-truth-valued .definition name="Predicate as a truth-valued function"}

A $k$-ary relation $R \subseteq A_1\times\cdots\times A_k$ can equivalently be viewed as a function
$$R : A_1\times\cdots\times A_k \to \{T,F\}, \qquad R(a_1,\dots,a_k) = T \iff (a_1,\dots,a_k)\in R.$$
Rosen also calls this a *propositional function*.

:::

::: {.remark name="Substitution yields a proposition"}

Giving specific values to every argument of a predicate produces a proposition (definite truth value).

:::

::: {.remark name="Equality is always available"}

$=$ is a predicate assumed available for *every* domain – without it, no domain of objects could even be meaningfully discussed.

:::

::: {#def-property .definition name="Property"}

A unary predicate (*property*) $P(x)$ on domain $D$ corresponds to the set $\{x\in D : P(x)\}$.

:::

## Variables and constants

::: {#def-variable .definition name="Variable"}

A name for an object, without specifying it exactly, used to reason about an unknown or arbitrary member of its *domain*.

:::

::: {.remark name="Domain"}

$Domain$ also call $domain of discourse$ or $universe of discourse$.

:::

::: {#def-constant .definition name="Constant"}

An object belonging to the domain of some variable – a specific, named member of that domain.

:::

::: {.remark name="Every variable has a domain"}

E.g. “let $x\in\mathbb{Z}$” declares $x$ with domain $\mathbb{Z}$; a Boolean variable always has domain $\{T,F\}$.

:::

## Predicates and variables

::: {#def-free-variable .definition name="Free variable"}

A variable in a predicate expression not (yet) assigned a value.

:::

::: {.remark name="Truth value requires all arguments fixed"}

An expression with $\ge1$ free variable is not a proposition (no truth value). Only when *every* free variable is assigned a value from its domain does the expression become a proposition.

:::

::: {.remark name="Domain matching is mandatory"}

Any value or variable placed into an argument of a predicate must belong to that argument’s declared domain – mismatched domains make the expression ill-formed, not just false.

:::

::: {.remark name="Prefix vs.\ infix notation"}

Newly defined predicates typically use prefix notation, $R(a,b)$; predicates for ordering/equality/equivalence conventionally use infix notation, $a<b$, $a=b$ (@sec-math-discrete-functions-special-functions).

:::

## Arguments of predicates

::: {#def-term-recursive .definition name="Term, recursive"}

A *term* of domain $D$ is one of:

- a constant from $D$;

- a variable with domain $D$;

- a function with codomain $D$, each of whose arguments is given a term of matching domain.

:::

::: {.remark name="Recursion bottoms out"}

Terms are built from constants/variables/functions to arbitrary finite depth (composition, nested function calls), but never infinitely – every term has a finite construction.

:::

::: {#exm-predicates-1 .example}

Let $a,b$ be variables with domain $\mathbb{R}$. The expression
$$a^2+b^2$$
is a term of domain $\mathbb{R}$.

To see this, first consider $a^2$. The squaring function
$$\operatorname{square}:\mathbb{R}\to\mathbb{R}$$
has codomain $\mathbb{R}$, and its argument $a$ is a term of domain $\mathbb{R}$. Therefore,
$$a^2=\operatorname{square}(a)$$
is a term of domain $\mathbb{R}$.

Similarly, since $b$ is a term of domain $\mathbb{R}$,
$$b^2=\operatorname{square}(b)$$
is also a term of domain $\mathbb{R}$.

Finally, consider the real addition function
$$+:\mathbb{R}\times\mathbb{R}\to\mathbb{R}.$$
Its two arguments must each be terms of domain $\mathbb{R}$. Since both $a^2$ and $b^2$ are terms of domain $\mathbb{R}$, they can be given to the two arguments of the addition function. Hence,
$$a^2+b^2$$
is a term of domain $\mathbb{R}$.

:::

::: {#exm-predicates-2 .example}

Let $\mathbb P$ be the domain of people, and suppose that
$$\operatorname{FatherOf}:\mathbb P\to\mathbb P$$
and
$$\operatorname{MotherOf}:\mathbb P\to\mathbb P.$$
If $Y$ is a variable with domain $\mathbb P$, then
$$\operatorname{FatherOf}(Y)$$
is a term of domain $\mathbb P$. Consequently,
$$\operatorname{MotherOf}(\operatorname{FatherOf}(Y))$$
is also a term of domain $\mathbb P$.

:::
