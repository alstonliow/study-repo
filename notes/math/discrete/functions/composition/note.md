---
title: "Composition"
sources: [fit1058-cn-2.9, fit1058-cn-2.11]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Composition; Loose composition. -->

## Composition

::: {#def-composition .definition name="Composition"}

For $f: A \to B$ and $g: B \to C$, the *composition* $g \circ f : A \to C$ is
$$(g \circ f)(x) = g(f(x)).$$

:::

::: {.remark name="Order of writing vs.\ order of application"}

$g \circ f$ is read right-to-left in application ($f$ first, then $g$), matching the order inside $g(f(x))$ – but this is the *reverse* of our usual left-to-right reading order. Read carefully.

:::

::: {.remark name="Compatibility requirement"}

$g \circ f$ is defined only when $\mathrm{codomain}(f) = \mathrm{domain}(g)$: whatever $f$ guarantees to produce must be exactly what $g$ is guaranteed to handle. If this fails, the composition is simply undefined – not partially defined, not an error to patch around.

:::

::: {#prp-not-commutative-but-associative .proposition name="Not commutative, but associative"}

In general $g \circ f \neq f \circ g$ (indeed one side may not even be defined). But for $f: A\to B,\ g: B\to C,\ h: C\to D$:
$$h \circ (g \circ f) = (h \circ g) \circ f,$$
so $h \circ g \circ f$ is unambiguous without parentheses.

:::

::: {.proof}

Both sides are functions $A \to D$. For any $x \in A$:
$$\big(h \circ (g \circ f)\big)(x) = h\big((g\circ f)(x)\big) = h(g(f(x))) = (h \circ g)(f(x)) = \big((h \circ g) \circ f\big)(x).$$
Equal on every input, so the functions are equal.

:::

::: {#prp-role-of-the-identity .proposition name="Role of the identity"}

For $f: A \to A$ a bijection: $f \circ f^{-1} = i_A$ and $f^{-1} \circ f = i_A$. For any $g: C \to D$: $g \circ i_C = g$ and $i_D \circ g = g$.

:::

::: {#def-iterated-composition .definition name="Iterated composition"}

For $f: A \to A$ and $n \in \mathbb{Z}^+$:
$$f^{(n)} = \underbrace{f \circ f \circ \cdots \circ f}_{n \text{ copies}}.$$

:::

::: {#prp-composition-preserves-injectivity-surjectivity .proposition name="Composition preserves injectivity/surjectivity"}

Let $f: A \to B$, $g: B \to C$.

(i) If $f,g$ are both injective, so is $g \circ f$.

(ii) If $f,g$ are both surjective, so is $g \circ f$.

(iii) If $f,g$ are both bijective, so is $g \circ f$.

:::

::: {.proof}

\(i\) Suppose $(g\circ f)(x_1) = (g\circ f)(x_2)$, i.e. $g(f(x_1)) = g(f(x_2))$. Since $g$ is injective, $f(x_1) = f(x_2)$; since $f$ is injective, $x_1 = x_2$.

\(ii\) Let $z \in C$. Since $g$ is surjective, $z = g(y)$ for some $y \in B$; since $f$ is surjective, $y = f(x)$ for some $x \in A$. Then $(g\circ f)(x) = g(f(x)) = g(y) = z$.

\(iii\) Immediate from (i) and (ii).

:::

## Loose composition

::: {#def-loose-composition .definition name="Loose composition"}

For $f: A \to B$ and $g: C \to D$ (no requirement that $B = C$), the *loose composition* $g \mathbin{\mathaccent"705E\relax\circ} f$ is
$$g \mathbin{\mathaccent"705E\relax\circ} f : \{x \in A : f(x) \in C\} \to D, \qquad (g \mathbin{\mathaccent"705E\relax\circ} f)(x) = g(f(x)).$$

:::

::: {.remark name="Always defined, but harder to use"}

Unlike ordinary (“tight”) composition, loose composition is defined for *any* $f,g$ – if $B \cap C = \emptyset$, it degenerates to the empty function. The cost: determining its domain requires inspecting the *rule* of $f$ (which inputs land in $C$), not just $f$’s stated codomain – so it is harder to reason about mechanically. This course uses tight composition throughout.

:::
