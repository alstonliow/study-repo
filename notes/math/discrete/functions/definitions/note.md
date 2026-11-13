---
title: "Functions: Definitions and Notation"
sources: [fit1058-cn-2.1, fit1058-cn-2.3]
requires: [math/discrete/functions/injections-surjections-bijections]
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Definitions; Notation. -->

## Definitions

::: {#def-function .definition name="Function"}

A function $f$ consists of: a set called the *domain*; a set called the *codomain*; and a rule assigning, to each $x$ in the domain, a unique value $f(x)$ in the codomain.

:::

```{=latex}
\begin{center}
\begin{tikzcd}[row sep=small, column sep=huge]
1 \arrow[r, "f"] & p \\
2 \arrow[r, "f"'] & q \\
3 \arrow[r, "f"] & r
\end{tikzcd}
\end{center}
```

A function $f:\{1,2,3\}\to\{p,q,r\}$, each argument pointing to its unique value

::: {.remark name="Alternative phrasing"}

Let $A,B$ be nonempty sets. A *function* $f$ from $A$ to $B$ is an assignment of exactly one element of $B$ to each element of $A$. We write $f(a)=b$ if $b$ is the element assigned to $a$, and $f: A \to B$.

:::

::: {.remark}

$x$ is the *argument* (parameter, input); $f(x)$ is the *value* (output).

:::

::: {#def-equality-of-functions .definition name="Equality of functions"}

$f = g$ iff $\operatorname{dom}(f) = \operatorname{dom}(g)$, their codomains agree, and $f(x) = g(x)$ for every $x \in \operatorname{dom}(f)$.

:::

::: {#exm-definitions-1 .example}

Let $\mathrm{CubeSum4}_\mathbb{Z}(w,x,y,z) = w^3+x^3+y^3+z^3$ on $\operatorname{dom}= \mathbb{Z}^4$, and $\mathrm{CubeSum4}_\mathbb{R}$ the same rule on $\operatorname{dom}= \mathbb{R}^4$. Despite the identical rule, these are *different* functions, since equality of functions requires equal domains.

:::

### Domain

::: {#def-domain .definition name="Domain"}

The *domain* of $f$, written $\operatorname{dom}(f)$, is exactly the set of valid arguments: $f(x)$ must be defined for every $x \in \operatorname{dom}(f)$, and undefined for every $x \notin \operatorname{dom}(f)$.

:::

::: {.remark name="The domain as a promise"}

Specifying $\operatorname{dom}(f)$ commits $f$ to working correctly on *every* member of it – no more, no less. A larger domain is a bigger promise (more work to guarantee); a smaller domain that still covers the intended use case is often preferable.

:::

### Codomain & co.

::: {#def-codomain .definition name="Codomain"}

The *codomain* of $f$ is a set containing every possible value $f(x)$ for $x \in \operatorname{dom}(f)$, but is allowed to be a *loose* superset – it may contain elements never actually attained.

:::

::: {#def-image .definition name="Image"}

The *image* of $f$ is the exact set of attained values, $\{f(x) : x \in \operatorname{dom}(f)\}$ – a subset of the codomain, not necessarily proper.

:::

::: {.remark}

CN deliberately avoids the word “range”, since usage is inconsistent (sometimes the image, sometimes the codomain). Rosen uses “range” for what CN calls the image.

:::

::: {.remark name="Why allow looseness at all?"}

The image is often hard, or even provably impossible, to compute exactly (e.g. a function whose value depends on uncomputable properties of programs), while a simple superset codomain is easy to state. So we specify a codomain we’re confident covers every value, rather than insisting on the exact image.

:::

::: {#def-image-of-a-set .definition name="Image of a set"}

For $f: A \to B$ and $S \subseteq A$, the *image of $S$ under $f$* is
$$f(S) = \{f(s) : s \in S\} \subseteq B.$$
(The image of $f$ itself, above, is the special case $f(A)$.)

:::

::: {.remark name="Onto / surjective"}

If the codomain equals the image, $f$ is *onto* (*surjective*), a *surjection*. (Formal treatment in @sec-math-discrete-functions-injections-surjections-bijections.)

:::

### Rule

::: {#def-rule .definition name="Rule"}

The *rule* of $f$ specifies, for each $x \in \operatorname{dom}(f)$, what $f(x)$ is – it need not specify *how* to compute it (no algorithm required).

:::

::: {#def-graph-of-a-function .definition name="Graph of a function"}

The *graph* of $f$ is $\{(x, f(x)) : x \in \operatorname{dom}(f)\}$, the set of all argument–value pairs.

:::

::: {#exm-definitions-2 .example}

A function on the finite domain $\{1,2,3,4\}$ can be given as a finite graph, e.g. $\{(1,a),(2,a),(3,b),(4,c)\}$ (its image is $\{a,b,c\}$, a proper subset of a larger codomain). A function on an infinite domain typically needs a rule rather than a listed graph: the squaring function on $\mathbb{Z}$ has graph $\{(x,x^2):x\in\mathbb{Z}\}$.

:::

## Notation

::: {#def-function-declaration .definition name="Function declaration"}

$$f : \text{domain} \to \text{codomain}, \qquad f(x) = \text{expression in } x.$$
Equivalently, the rule may be given with a *mapping arrow*: $x \mapsto \text{expression in } x$ (note: $\mapsto$ for the rule, $\to$ for domain/codomain – do not conflate them).

:::

::: {#exm-definitions-1-2 .example}

$f : \mathbb{R}\to \mathbb{R},\ f(x) = x^2$, equivalently $f: \mathbb{R}\to \mathbb{R},\ x \mapsto x^2$. The codomain need not be the tightest possible: $\mathbb{R}_0^+$ (the image) would also be valid, but a codomain like $\mathbb{R}\cup \{0,-\sqrt2,-42\}$, while technically valid, is needlessly cluttered.

:::
