<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-predicate-01" status="draft"}
A predicate with no arguments has nothing to vary, so it has a single fixed
truth value. It is a proposition: either True or False.
:::

::: {.solution for="prob-predicate-07" status="draft"}
| | predicates | functions | variables (domain) | constants | proposition? |
|---|---|---|---|---|---|
| (a) | $\ge$ | squaring | $x\in\mathbb R$ (bound) | $0$ | yes, **true** |
| (b) | $<$ | squaring | $x\in\mathbb R$ (free) | $0$ | no: $x$ is free |
| (c) | $=$ | $2^x$, squaring | $x\in\mathbb N$ (bound) | $2$ | yes, **false**: $x = 0$ gives $1\ne0$ |
| (d) | $<$ | none | $x\in\mathbb R$ (free), $y\in\mathbb R$ (bound) | $0$ | no: $x$ is free |
| (e) | $<$ | none | $x,y,z\in\mathbb R$ (bound) | none | yes, **false**: take $x = z$ |
| (f) | none | none | $x,y$ Boolean (bound) | none | yes, **true**: $x = \mathrm T$, $y = \mathrm F$ |

Notes:

- (c) is false over $\mathbb N$ even though $2^x = x^2$ holds for $x = 2$ and
  $x = 4$; a universal statement needs every $x$.
- (d) is true for every value of $x$ once $x$ is fixed (if $x<0$, then
  $x<y$ for all positive $y$), but as written it has a free variable.
- (e) would be true if it required $x<z$ first, as in
  $\forall x\forall z\,(x<z\Rightarrow\exists y\,(x<y\wedge y<z))$: the
  reals are dense.
- In (f), $\neg(x\Rightarrow y)$ uses only connectives; $x,y$ are
  propositional variables.
:::

::: {.solution for="prob-predicate-08" status="draft"}
- Predicates: $\subseteq$ (binary, used twice).
- Functions: the power set function $\mathcal P$.
- Variables: $A$ and $B$, ranging over sets; both are bound by $\forall$.
- Connective: $\Rightarrow$.

In words: *for all sets $A$ and $B$, if $A$ is a subset of $B$, then the power
set of $A$ is a subset of the power set of $B$* (Exercise 1.7).
:::
