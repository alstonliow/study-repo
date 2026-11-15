---
title: Selection and Ordered Selection
sources: [fit1058-cn-8.5, fit1058-cn-8.6, fit1058-cn-8.7]
requires: [math/discrete/counting/sum-and-product-rules]
status: draft
---

<!-- Migrated from 1058note 08-counting-combinatorics.tex, §8.5–8.7. -->

## Selection

::: {#rmk-selection-1 .remark name="Four kinds of selection"}

|  | **order matters** | **order irrelevant** |
|:--|:--|:--|
| **with replacement** | ordered, w/ replacement (@sec-math-discrete-counting-selection) | unordered, w/ replacement (@sec-math-discrete-counting-stars-and-bars) |
| **without replacement** | ordered, w/o replacement (@sec-math-discrete-counting-selection) | unordered, w/o replacement (@sec-math-discrete-counting-combinations) |

:::

## Ordered selection with replacement

::: {#prp-ordered-with-replacement .proposition}
The number of length-$r$ sequences over an $n$-element set $A$ is
$$
|A\times\cdots\times A| = n^r
$$
(@sec-math-discrete-sets-cartesian-product, @sec-math-discrete-sets-cardinality-and-standard-sets for the string special case, @sec-math-discrete-functions-counting for counting functions).
:::

## Ordered selection without replacement

::: {#def-falling-factorial .definition name="Falling factorial, permutations"}
$$
(n)_r = n(n-1)(n-2)\cdots(n-r+1) = \frac{n!}{(n-r)!}, \qquad \text{also written } {}_nP_r \text{ or } P(n,r).
$$
:::

::: {#fig-selection-1}

```{=latex}
\begin{tikzpicture}[x=1cm, y=0.55cm]
  \node[dot] (r) at (0,0) {};
  \foreach \f/\y/\rest in {a/3.3/{b,c}, b/0/{a,c}, c/-3.3/{a,b}} {
    \node[small vertex] (s\f) at (2,\y) {$\f$};
    \draw (r) -- (s\f);
    \foreach \g [count=\n] in \rest {
      \pgfmathsetmacro{\dy}{\n==1 ? 0.8 : -0.8}
      \node[lbl, anchor=west] (l\f\g) at (4,\y+\dy) {$\f\g$};
      \draw (s\f) -- (l\f\g.west);
    }
  }
\end{tikzpicture}
```

Ordered selections of $2$ from $\{a,b,c\}$ without replacement: $3$ choices, then $2$, giving $(3)_2=6$ sequences

:::

::: {.proof name="Derivation"}
Choice $k$ (for $k=1,\dots,r$) has $n-(k-1)$ options remaining (the $k-1$ prior choices excluded). By the product rule (@sec-math-discrete-counting-sum-and-product-rules):
$$
n\cdot(n-1)\cdots(n-r+1).
$$
:::

::: {#rmk-selection-2 .remark name="Counting injections"}
Already the counting-injections theorem of @sec-math-discrete-functions-counting.
:::
