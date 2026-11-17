---
title: "Composition"
sources: [fit1058-cn-2.9, fit1058-cn-2.11]
requires: [math/discrete/functions/inverse-functions]
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Composition; Loose composition. -->

## Composition

::: {#def-composition .definition name="Composition"}

For $f: A \to B$ and $g: B \to C$, the *composition* $g \circ f : A \to C$ is
$$(g \circ f)(x) = g(f(x)).$$

:::

::: {#fig-composition-1}

```{=latex}
\begin{tikzpicture}
  \node[set, label=above:$A$] at (0,0) {};
  \node[set, label=above:$B$] at (3.4,0) {};
  \node[set, label=above:$C$] at (6.8,0) {};
  \node[dot, label={[lab]left:$x$}] (x) at (0,0.3) {};
  \node[dot, label={[lab]above:$f(x)$}] (y) at (3.4,0.3) {};
  \node[dot, label={[lab]above:$g(f(x))$}] (z) at (6.8,0.3) {};
  \draw[map] (x) -- node[lab, above] {$f$} (y);
  \draw[map] (y) -- node[lab, above] {$g$} (z);
  \draw[map, accent, emph] (x) .. controls (1.8,-2.0) and (5.0,-2.0) .. node[lab, below, text=accent] {$g\circ f$} (z);
\end{tikzpicture}
```

$g\circ f$ sends $x$ straight to $g(f(x))$: first $f$, then $g$

:::

::: {#rmk-composition-1 .remark name="Order of writing vs.\ order of application"}

$g \circ f$ is read right-to-left in application ($f$ first, then $g$), matching the order inside $g(f(x))$ – but this is the *reverse* of our usual left-to-right reading order. Read carefully.

:::

::: {#rmk-composition-2 .remark name="Compatibility requirement"}

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

<!-- Added 2026-11-15 from CN §2.9 (own wording and proofs). -->

::: {#thm-composition-bijection-finite .theorem name="Bijective composition, equal finite sizes"}

Let $f: A \to B$ and $g: B \to C$, where $A$, $B$, $C$ are finite and $|A| = |B| = |C|$. Then
$$g \circ f \text{ is a bijection} \iff f \text{ and } g \text{ are both bijections.}$$

:::

::: {.proof}

1. All three functions go between finite sets of the same size, so each is a bijection if and only if it is an injection (@thm-finite-equal-size-domain-codomain).

2. ($\Leftarrow$) If $f$ and $g$ are bijections, then $g \circ f$ is a bijection by @prp-composition-preserves-injectivity-surjectivity (iii).

3. ($\Rightarrow$) Assume $g \circ f$ is a bijection. First, $f$ is injective: if $f(a) = f(b)$, then $g(f(a)) = g(f(b))$, and since $g \circ f$ is injective, $a = b$.

4. By step 1, $f$ is therefore a bijection; in particular it is surjective.

5. Next, $g$ is injective. Let $g(y_1) = g(y_2)$. Since $f$ is surjective, $y_1 = f(x_1)$ and $y_2 = f(x_2)$ for some $x_1, x_2 \in A$. Then $(g\circ f)(x_1) = (g \circ f)(x_2)$, so $x_1 = x_2$ and hence $y_1 = y_2$.

6. By step 1, $g$ is a bijection too.

:::

::: {#rmk-composition-4 .remark name="The size condition matters"}

Without equal sizes the theorem fails. Take $f: \{1\} \to \{1,2\}$ with $f(1)=1$, and $g: \{1,2\} \to \{1\}$. Then $g \circ f: \{1\} \to \{1\}$ is a bijection, but $f$ is not surjective and $g$ is not injective.

:::

::: {#thm-inverse-of-composition .theorem name="Inverse of a composition"}

If $f: A \to B$ and $g: B \to C$ are bijections, then
$$(g \circ f)^{-1} = f^{-1} \circ g^{-1}.$$

:::

::: {.proof}

1. $g \circ f$ is a bijection (@prp-composition-preserves-injectivity-surjectivity), so $(g\circ f)^{-1}: C \to A$ exists (@thm-inverse-functions-1). Also $f^{-1}$ and $g^{-1}$ exist, so $f^{-1}\circ g^{-1}: C \to A$ is defined.

2. Using associativity (@prp-not-commutative-but-associative) and the identity rules (@prp-role-of-the-identity):
$$(g\circ f)\circ(f^{-1}\circ g^{-1}) = g \circ (f \circ f^{-1}) \circ g^{-1} = g \circ i_B \circ g^{-1} = g \circ g^{-1} = i_C.$$

3. In the same way,
$$(f^{-1}\circ g^{-1})\circ(g\circ f) = f^{-1} \circ (g^{-1} \circ g) \circ f = f^{-1} \circ i_B \circ f = i_A.$$

4. So $f^{-1}\circ g^{-1}$ undoes $g \circ f$ on both sides, and it is the inverse of $g\circ f$.

:::

::: {#rmk-composition-5 .remark name="Socks and shoes"}

The order reverses: to undo "first $f$, then $g$", undo $g$ first. You put on socks, then shoes; you take off shoes, then socks.

:::

## Loose composition

::: {#def-loose-composition .definition name="Loose composition"}

For $f: A \to B$ and $g: C \to D$ (no requirement that $B = C$), the *loose composition* $g \mathbin{\hat{\circ}} f$ is
$$g \mathbin{\hat{\circ}} f : \{x \in A : f(x) \in C\} \to D, \qquad (g \mathbin{\hat{\circ}} f)(x) = g(f(x)).$$

:::

::: {#rmk-composition-6 .remark name="Always defined, but harder to use"}

Unlike ordinary (“tight”) composition, loose composition is defined for *any* $f,g$ – if $B \cap C = \emptyset$, it degenerates to the empty function. The cost: determining its domain requires inspecting the *rule* of $f$ (which inputs land in $C$), not just $f$’s stated codomain – so it is harder to reason about mechanically. This course uses tight composition throughout.

:::
