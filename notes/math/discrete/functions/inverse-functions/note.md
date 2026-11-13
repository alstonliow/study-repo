---
title: "Inverse functions"
sources: [fit1058-cn-2.8]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Inverse functions. -->

::: {.remark name="Why uniqueness can fail"}

Let $f: A \to B$. For a given $y \in B$, trying to go “backwards” can fail in two distinct ways:

- *Non-uniqueness*: there exist $x_1 \neq x_2 \in A$ with $f(x_1) = f(x_2) = y$.

- *Non-existence*: $y$ lies in the codomain but not the image, so no $x \in A$ satisfies $f(x)=y$.

Both failures are ruled out exactly when $f$ is, respectively, injective and surjective.

:::

::: {#def-inverse-function .definition name="Inverse function"}

If $f: A \to B$ is such that every $y \in B$ has a *unique* $x \in A$ with $f(x) = y$, the *inverse function* $f^{-1} : B \to A$ is defined by
$$f^{-1}(y) = \text{the unique } x \in A \text{ such that } f(x) = y.$$
Equivalently, as a set of ordered pairs (the graph of $f$, reversed):
$$f^{-1} = \{(y,x) : (x,y) \in f\} = \{(f(x),x) : x \in A\}.$$

:::

::: {#thm-inverse-functions-1 .theorem}

$f: A \to B$ has an inverse function if and only if $f$ is a bijection.

:::

::: {.proof}

($\Rightarrow$) If $f^{-1}$ exists, every $y \in B$ has *some* preimage (so $f$ is surjective) and *at most one* preimage (so $f$ is injective, since two preimages of the same $y$ would break the “unique $x$” requirement in the definition of $f^{-1}$). Hence $f$ is a bijection.

($\Leftarrow$) If $f$ is a bijection, surjectivity guarantees every $y \in B$ has *at least one* preimage, and injectivity guarantees *at most one*; together, exactly one. This unique preimage is exactly what $f^{-1}(y)$ requires, so $f^{-1}$ is well-defined.

:::

::: {.remark name="When invertibility fails"}

Neither the `Employer` function (not injective: two computers both mapped to Harvard College Observatory) nor the squaring function $\mathbb{R}\to \mathbb{R}$ (not injective: $2^2=(-2)^2$; also not surjective onto all of $\mathbb{R}$) is invertible.

:::

::: {#prp-undoes-and-vice-versa .proposition name="$f^{-1}$ undoes $f$, and vice versa"}

If $f: A \to B$ is a bijection, then for all $x \in A$ and all $y \in B$:
$$f^{-1}(f(x)) = x, \qquad f(f^{-1}(y)) = y.$$

:::

::: {.proof}

Let $x \in A$ and $y = f(x)$. By definition, $f^{-1}(y)$ is the unique element of $A$ mapping to $y$ under $f$ – and $x$ is such an element, so $f^{-1}(f(x)) = f^{-1}(y) = x$. The second identity is symmetric: apply the same argument with the roles of $f, f^{-1}$ swapped, using that $f^{-1}$ is itself a bijection (below).

:::

::: {#prp-inverse-functions-1 .proposition}

If $f$ is a bijection, so is $f^{-1}$, and $(f^{-1})^{-1} = f$.

:::

::: {.proof}

$f^{-1}: B \to A$ is injective and surjective by the symmetry of the defining property (unique $x$ for each $y$ $\Leftrightarrow$ unique $y$ for each $x$, since $f$ itself is a bijection), hence $f^{-1}$ is a bijection and has its own inverse. That inverse must send each $x$ back to the $y$ with $f^{-1}(y)=x$, i.e. $y=f(x)$ – exactly $f$. So $(f^{-1})^{-1}=f$.

:::

::: {#def-preimage-of-a-set .definition name="Preimage of a set"}

For $f: A \to B$ (*not* necessarily a bijection) and $S \subseteq B$, the *preimage* (or *inverse image*) of $S$ under $f$ is
$$f^{-1}(S) = \{a \in A : f(a) \in S\}.$$

:::

::: {.remark name="Overloaded notation – read carefully"}

$f^{-1}(S)$ (preimage of a *set*, defined for *any* function $f$) and $f^{-1}(y)$ (the *inverse function* applied to a point, defined *only when $f$ is a bijection*) use the same symbol $f^{-1}$ but are different concepts. When $f$ is a bijection, $f^{-1}(\{y\}) = \{f^{-1}(y)\}$ – the set-level and point-level notions agree – but $f^{-1}(S)$ makes sense even when no bijection (or even no inverse function) exists.

:::

::: {#exm-inverse-functions-1 .example}

For $f: \mathbb{R}\to \mathbb{R},\ f(x) = x^2$ (not a bijection, so $f^{-1}$ as a function does not exist), the preimage of $S = [4,9]$ is
$$f^{-1}([4,9]) = \{x \in \mathbb{R}: x^2 \in [4,9]\} = [-3,-2] \cup [2,3].$$

:::
