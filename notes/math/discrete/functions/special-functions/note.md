---
title: "Special Functions and Restrictions"
sources: [fit1058-cn-2.4, fit1058-cn-2.5, fit1058-cn-2.6]
requires: [math/discrete/functions/definitions, math/discrete/functions/inverse-functions]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Some special functions; Functions with multiple arguments and values; Restrictions. -->

## Some special functions

::: {#def-empty-function .definition name="Empty function"}

$$\emptyset : \emptyset \to \emptyset$$
Empty domain, empty codomain, vacuous rule.

:::

::: {#def-identity-function .definition name="Identity function"}

For a set $A$:
$$i_A : A \to A, \qquad i_A(x) = x.$$

:::

::: {#def-indicator-characteristic-function .definition name="Indicator (characteristic) function"}

For $A \subseteq D$:
$$\chi_A : D \to \{0,1\}, \qquad
\chi_A(x) =
\begin{cases}
1, & x \in A; \\
0, & x \notin A.
\end{cases}$$
Depends on $D$, not just $A$: different domains give different indicator functions.

:::

::: {#exm-special-functions-1 .example}

$$\chi_{A \cup B}(x) = \max\{\chi_A(x), \chi_B(x)\} \quad \text{for all } x.$$

:::

::: {#def-constant-function .definition name="Constant function"}

For a domain $D$ and object $a$:
$$c_a : D \to \{a\}, \qquad c_a(x) = a.$$

:::

::: {#def-floor-and-ceiling .definition name="Floor and ceiling"}

For $x \in \mathbb{R}$:
$$\lfloor x \rfloor = \max\{n \in \mathbb{Z}: n \le x\}, \qquad
\lceil x \rceil = \min\{n \in \mathbb{Z}: n \ge x\}.$$

:::

::: {.remark name="Contrast with CN's @sec-math-discrete-functions-definitions"}

CN’s definition of a function already *is* what Rosen calls a *total* function: $\operatorname{dom}(f)$ equals the declared domain exactly, with no gaps. Rosen’s “partial function from $A$ to $B$” allows $\operatorname{dom}(f)\subsetneq A$ – a total function on the smaller set $\operatorname{dom}(f)\subseteq A$.

:::

::: {#exm-special-functions-2 .example}

$f:\mathbb{R}\to\mathbb{R}$, $f(x)=1/x$ is a partial function on $\mathbb{R}$ (undefined at $0$); as a *total* function it is $f:\mathbb{R}\setminus\{0\}\to\mathbb{R}$ – same rule, different declared domain (CN’s @sec-math-discrete-functions-definitions view of the domain as an exact promise).

:::

## Functions with multiple arguments and values

::: {#def-multiple-arguments-via-cartesian-product .definition name="Multiple arguments via Cartesian product"}

A function of two arguments $f(x,y)$, $x \in X, y \in Y$, value in $C$, is formally $f: X \times Y \to C$ – a function of *one* argument, the ordered pair $(x,y)$, with $f(x,y)$ shorthand for $f((x,y))$. Extends to any number of arguments via $X_1 \times \cdots \times X_n$.

:::

::: {.remark name="Notation styles"}

$f(x,y)$ is *prefix* notation (name before arguments). *Infix* (name between, e.g. $x+y$) and *postfix* (name after) also occur.

:::

::: {#def-multiple-tuple-valued-outputs .definition name="Multiple (tuple-valued) outputs"}

A function returning a pair is $f: X \to Y \times Z$; its value is a single element $(y,z) \in Y \times Z$, viewable as “two outputs.” Extends to any number of returned values.

:::

## Restrictions

::: {#def-restriction .definition name="Restriction"}

For $f: A \to B$ and $X \subseteq A$, the *restriction* of $f$ to $X$, written $f|_X$ (or $f\restriction_X$), is
$$f|_X : X \to B, \qquad f|_X(x) = f(x) \text{ for all } x \in X.$$

:::

::: {.remark name="Why restrict?"}

A smaller domain means: a smaller stored representation (fewer ordered pairs to list); a smaller “promise” to keep (less testing if implemented); sometimes simpler analysis; and sometimes *stronger properties* unavailable to the original function.

:::

::: {#exm-special-functions-1-2 .example}

Let $f: \mathbb{R}\to \mathbb{R},\ f(x)=x^2$. Its restriction $f|_{\mathbb{R}_0^+} : \mathbb{R}_0^+ \to \mathbb{R}$ is strictly increasing throughout its domain (unlike $f$, which decreases on $\mathbb{R}_0^-$), and every $y$ in its image has a *unique* preimage $\sqrt{y}$ – whereas under $f$ itself, each nonzero $y$ in the image has two preimages, $\pm\sqrt{y}$. (This makes $f|_{\mathbb{R}_0^+}$ invertible, unlike $f$ – see @sec-math-discrete-functions-inverse-functions.)

:::
