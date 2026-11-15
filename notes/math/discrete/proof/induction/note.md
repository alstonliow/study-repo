---
title: "Proof by mathematical induction"
sources: [fit1058-cn-3.10, fit1058-cn-3.13]
requires: [math/discrete/proof/induction-examples, math/discrete/sets/set-operations, math/discrete/proof/contradiction]
status: draft
---

<!-- Migrated from 1058note notes/chapters/03-proofs.tex: Proof by mathematical induction. -->

::: {.remark name="Principle of mathematical induction"}

To prove $S(n)$ holds for all $n \in \mathbb{N}$ (or all $n \ge n_0$):

- **Base case**: prove $S(1)$ (or $S(n_0)$).

- **Inductive step**: prove, for all $k$:
  $$S(k) \implies S(k+1)$$
  (the assumption $S(k)$ here is the *inductive hypothesis*).

Conclude $S(n)$ holds for all $n$.

:::

::: {#fig-induction-1}

```{=latex}
\begin{tikzpicture}
  \foreach \i/\ang/\f in {1/-38/25, 2/-24/25, 3/-10/25, 4/0/8, 5/0/8, 6/0/8, 7/0/8} {
    \draw[fill=primary!\f, rotate around={\ang:(\i*0.95+0.13,0)}] (\i*0.95-0.13,0) rectangle (\i*0.95+0.13,1.5);
  }
  \draw (0.4,0) -- (7.4,0);
  \foreach \i/\t in {1/{S(1)}, 2/{S(2)}, 3/{S(3)}, 4/{S(4)}, 5/{S(5)}, 6/{S(6)}} \node[tick] at (\i*0.95,-0.3) {$\t$};
  \node[tick] at (7*0.95,-0.3) {$\cdots$};
  \draw[map, accent, emph] (-0.4,1.45) -- (0.45,1.15);
  \node[tick, text=accent, anchor=east] at (-0.4,1.45) {base case};
\end{tikzpicture}
```

Induction as a row of dominoes: the base case knocks over $S(1)$, and the inductive step $S(k)\implies S(k+1)$ makes each domino knock over the next

:::

::: {#thm-generalized-de-morgan-s-law .theorem name="Generalized De Morgan's law, CN Thm 18"}

For all $n \in \mathbb{N}$ and sets $A_1,\dots,A_n$:
$$\overline{A_1 \cup A_2 \cup \cdots \cup A_n} = \overline{A_1} \cap \overline{A_2} \cap \cdots \cap \overline{A_n}.$$

:::

::: {.proof}

Let $S(n)$ be this identity for a given $n$.

**Base case** ($n=1$):
$$\overline{A_1} = \overline{A_1}.$$

**Inductive step**: assume $S(k)$, i.e.
$$\overline{A_1\cup\cdots\cup A_k} = \overline{A_1}\cap\cdots\cap\overline{A_k}.$$
Then
$$\overline{A_1\cup\cdots\cup A_k \cup A_{k+1}} = \overline{(A_1\cup\cdots\cup A_k) \cup A_{k+1}} = \overline{(A_1\cup\cdots\cup A_k)} \cap \overline{A_{k+1}}$$
by ordinary De Morgan’s law (@sec-math-discrete-sets-set-operations). Applying $S(k)$ to the first factor:
$$= (\overline{A_1}\cap\cdots\cap\overline{A_k})\cap\overline{A_{k+1}} = \overline{A_1}\cap\cdots\cap\overline{A_{k+1}},$$
which is $S(k+1)$.

By induction, $S(n)$ holds for all $n$.

:::

::: {#exm-induction-1 .example name="$3\mid n^3-n$"}

For all $n\in\mathbb{N}$: $3 \mid (n^3-n)$.

:::

::: {.proof}

**Base case** ($n=0$): $n^3-n=0$, and $3\mid 0$.

**Inductive step**: assume $3\mid(k^3-k)$ for some $k\ge0$, i.e. $k^3-k=3m$ for some $m\in\mathbb{Z}$. Consider $n=k+1$:
$$(k+1)^3-(k+1) = k^3+3k^2+3k+1-k-1 = (k^3-k) + 3k^2+3k = 3m+3k^2+3k = 3(m+k^2+k).$$
This is $3$ times an integer, so $3\mid\big((k+1)^3-(k+1)\big)$.

By induction, $3\mid(n^3-n)$ for all $n\in\mathbb{N}$.

:::

<!-- Added 2026-11-15 from CN §3.10 (own wording and proof). -->

::: {#exm-induction-sum-first-n .example name="Sum of the first $n$ positive integers"}

For all $n\in\mathbb{N}$:
$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}.$$

:::

::: {.proof}

1. Let $S(n)$ be the statement $1 + 2 + \cdots + n = \frac{n(n+1)}{2}$.

2. **Base case** ($n=1$): the left side is $1$ and the right side is $\frac{1\cdot2}{2} = 1$.

3. **Inductive step**: assume $S(k)$ for some $k\ge1$. Then
$$1 + \cdots + k + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2},$$
which is $S(k+1)$.

4. By induction, $S(n)$ holds for all $n\in\mathbb{N}$.

:::

::: {#def-well-ordering-property .definition name="Well-ordering property"}

Every nonempty subset of $\mathbb{N}$ has a least element.

:::

<!-- Added 2026-11-15 from CN §3.10 (own wording). -->

::: {#exm-interesting-numbers .example name="Every natural number is interesting"}

Every natural number is interesting.

:::

::: {.proof}

1. Suppose, for contradiction, that some natural number is uninteresting.

2. Then the set of uninteresting natural numbers is nonempty, so by well-ordering it has a least element $m$.

3. But being *the smallest uninteresting number* is an interesting property, so $m$ is interesting.

4. This contradicts the choice of $m$, so every natural number is interesting.

:::

::: {.remark name="What the joke shows"}

"Interesting" is vague, so this is not a real proof. Its shape is useful, though: it is a proof by contradiction (@sec-math-discrete-proof-contradiction), and it picks the *least* counterexample, whose minimality often gives the extra fact needed to finish. The same idea drives @thm-well-ordering-mathematical-induction.

:::

::: {#thm-well-ordering-mathematical-induction .theorem name="Well-ordering $\implies$ mathematical induction"}

If the well-ordering property holds for $\mathbb{N}$, then the principle of mathematical induction is valid.

:::

::: {.proof}

Suppose $S(1)$ holds and $S(k)\implies S(k+1)$ for all $k\ge1$. Suppose, for contradiction, $S(n)$ fails for some $n$. Let
$$F = \{n\in\mathbb{Z}^+ : S(n) \text{ is false}\}.$$
$F\neq\emptyset$ by assumption, so by well-ordering, $F$ has a least element $m$. Since $S(1)$ holds, $m\neq1$, so $m\ge2$ and $m-1\ge1$. Since $m$ is the *least* element of $F$, $m-1\notin F$, i.e. $S(m-1)$ holds. But then the inductive step gives $S(m-1)\implies S(m)$, so $S(m)$ holds – contradicting $m\in F$.

So $F=\emptyset$: $S(n)$ holds for all $n$.

:::

::: {#def-principle-of-strong-induction-formal .definition name="Principle of strong induction, formal statement"}

To prove $S(n)$ for all $n\ge n_0$:

- **Base case**: prove $S(n_0)$.

- **Inductive step**: prove, for all $k\ge n_0$: if $S(n_0),S(n_0+1),\dots,S(k)$ *all* hold, then $S(k+1)$ holds.

:::

::: {.remark name="Strong vs.\ weak induction – equivalent in power"}

Strong induction’s hypothesis is more generous (all of $S(n_0),\dots,S(k)$, not just $S(k)$), but this doesn’t let you prove anything weak induction can’t – any strong-induction proof can be mechanically rewritten as a weak-induction proof of the stronger statement $T(n) = S(n_0)\wedge\cdots\wedge S(n)$. Strong induction is a convenience, not a logically stronger tool. See @sec-math-discrete-proof-induction-examples for worked examples of both.

:::

<!-- Added 2026-11-15 from CN §3.13 (own wording). -->

::: {.remark name="Mathematical induction vs statistical induction"}

In statistics, *induction* means drawing general conclusions from data. Those conclusions may be wrong, because the data contain randomness and error, so statistical induction is not logical deduction and cannot be a step in a proof. Mathematical induction is different: it is a rigorous deductive method, and a correct induction proof establishes its statement with certainty.

:::
