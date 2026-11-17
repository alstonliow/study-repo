---
title: "Iterated Functions"
sources: [fit1058-cn-2.9]
requires: [math/discrete/functions/composition]
status: draft
---

<!-- Split from math/discrete/functions/composition on 2026-11-17 (block ids unchanged). Migrated from 1058note notes/chapters/02-functions.tex: Composition (iterated composition). -->

::: {#def-iterated-composition .definition name="Iterated composition"}

For $f: A \to A$ and $n \in \mathbb{Z}^+$:
$$f^{(n)} = \underbrace{f \circ f \circ \cdots \circ f}_{n \text{ copies}}.$$

:::

<!-- Added 2026-11-15 from CN §2.9 (own wording): three iterated compositions. -->

::: {#exm-iterated-lcg .example name="A pseudorandom number generator"}

A *linear congruential generator* is a function of the form
$$L : [0, M-1]_{\mathbb{Z}} \to [0, M-1]_{\mathbb{Z}}, \qquad L(x) = (ax + c) \bmod M.$$
Starting from a *seed* $s$, the iterates $L(s), L^{(2)}(s), L^{(3)}(s), \dots$ are used as numbers that look random at first glance. A classic choice is $a = 1103515245$, $c = 12345$, $M = 2^{31}$ (keep the last $31$ bits). Its randomness is weak, so in practice it is combined with other methods.

:::

::: {#exm-iterated-kaprekar .example name="Kaprekar's constant 6174"}

For an integer $x$ with at most four digits, write its four digits (with leading zeros) in decreasing order and in increasing order, and let $K(x)$ be the difference of these two numbers. For example, starting from $3524$:
$$3524 \overset{K}{\longmapsto} 5432-2345 = 3087 \overset{K}{\longmapsto} 8730-0378 = 8352 \overset{K}{\longmapsto} 8532-2358 = 6174 \overset{K}{\longmapsto} 6174.$$
If all four digits of $x$ are equal, then $K(x) = 0$. Otherwise the iterates reach $6174$ after at most seven steps, so
$$K^{(7)}(x) = \begin{cases} 0, & \text{all digits of } x \text{ equal},\\ 6174, & \text{otherwise.}\end{cases}$$
$K$ is not an injection: $x$ and any number formed by rearranging its digits have the same image.

:::

::: {#exm-iterated-collatz .example name="The Collatz function"}

Define $C : \mathbb{N} \to \mathbb{N}$ by
$$C(x) = \begin{cases} 3x + 1, & x \text{ odd},\\ x/2, & x \text{ even}.\end{cases}$$
Starting from $6$:
$$6 \mapsto 3 \mapsto 10 \mapsto 5 \mapsto 16 \mapsto 8 \mapsto 4 \mapsto 2 \mapsto 1 \mapsto 4 \mapsto 2 \mapsto 1 \mapsto \cdots$$
Once the iterates reach $1$, they cycle through $4, 2, 1$ for ever.

:::

::: {#rmk-composition-3 .remark name="Collatz's conjecture"}

It is conjectured that for every $x \in \mathbb{N}$ there is some $n$ with $C^{(n)}(x) = 1$. This is *Collatz's conjecture* (the "$3x+1$ problem"), and it is still unsolved: a very simple iterated function can raise very hard questions.

:::
