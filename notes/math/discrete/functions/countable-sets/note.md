---
title: "Countable Sets"
sources: [cs70-11]
requires: [math/discrete/functions/inverse-functions]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 11 (cs70-11), in our own wording; proofs written out in steps. -->

## Comparing infinite sets

::: {#def-same-cardinality .definition name="Same cardinality, countable"}

Sets $A$ and $B$ have the *same cardinality* if there is a bijection $A\to B$ (@def-bijective). A set is *countable* if there is a bijection between it and $\mathbb N$ or a subset of $\mathbb N$; otherwise it is *uncountable*. Every finite set is countable, since a set of size $m$ is in bijection with $\{0,1,\dots,m-1\}$.

:::

::: {#exm-countable-sets-n-z .example name="Plus one, twice as many, and both signs"}

1. $n\mapsto n+1$ is a bijection $\mathbb N\to\mathbb Z^+$: removing one element does not change the size.

2. $n\mapsto2n$ is a bijection from $\mathbb N$ to the even natural numbers: its inverse is $m\mapsto\frac m2$.

3. $f:\mathbb N\to\mathbb Z$ with $f(x)=\frac x2$ for even $x$ and $f(x)=-\frac{x+1}2$ for odd $x$ lists $0,-1,1,-2,2,\dots$. It is injective: if $f(x)=f(y)$, both values have the same sign, so $x,y$ are both even or both odd, and solving either formula gives $x=y$. It is surjective: $y\ge0$ is $f(2y)$, and $y<0$ is $f(-2y-1)$. So $\mathbb Z$ is countable.

:::

::: {#prp-injection-into-countable .proposition name="Injections and images"}

1. If there is an injection $f:A\to\mathbb N$, then $A$ is countable.

2. If $A$ is countable and $f:A\to B$ is surjective, then $B$ is countable.

:::

::: {.proof}

1. $f$ is a bijection from $A$ onto its image $f(A)$, which is a subset of $\mathbb N$.

2. Let $g$ be an injection from $A$ into $\mathbb N$ (a bijection onto a subset, by countability). For $b\in B$, the set $\{g(a):f(a)=b\}$ is a non-empty set of natural numbers, so it has a least element $h(b)$ (@def-well-ordering-property). Different $b$ have disjoint sets $f^{-1}(b)$, and $g$ is injective, so $h(b)\ne h(b')$ for $b\ne b'$. By part 1, $B$ is countable.

:::

::: {#thm-cantor-bernstein .theorem name="Cantor–Bernstein theorem"}

If there are injections $A\to B$ and $B\to A$, then there is a bijection $A\to B$.

:::

::: {#rmk-countable-sets-cantor-bernstein .remark name="Comparing sizes"}

An injection $A\to B$ says that $A$ is no larger than $B$. The theorem, stated here without proof (the proof is not easy), says that "no larger in both directions" means "the same size". In practice, part 1 of @prp-injection-into-countable is enough to show that a set is countable.

:::

## Pairs, rationals and strings

::: {#thm-pairs-countable .theorem name="Pairs of natural numbers"}

The map $\pi(m,n)=\frac{(m+n)(m+n+1)}2+n$ is a bijection $\mathbb N\times\mathbb N\to\mathbb N$.

:::

::: {.proof}

1. Group the pairs by $s=m+n$. The group for $s$ has the $s+1$ pairs $(s,0),(s-1,1),\dots,(0,s)$, and $\pi$ sends them to $T_s,T_s+1,\dots,T_s+s$, where $T_s=\frac{s(s+1)}2$.

2. $T_{s+1}=T_s+s+1$, so these blocks of numbers are consecutive and do not overlap: block $s$ ends at $T_s+s=T_{s+1}-1$ and block $s+1$ starts at $T_{s+1}$. Since $T_0=0$, the blocks cover all of $\mathbb N$.

3. Within a block, $\pi$ is the bijection $n\mapsto T_s+n$. So every natural number is the image of exactly one pair.

:::

::: {#fig-countable-sets-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.15cm,y=1.15cm]
\draw[->, muted] (-0.5,-0.5) -- (5,-0.5) node[lab, right] {$m$};
\draw[->, muted] (-0.5,-0.5) -- (-0.5,4.8) node[lab, above] {$n$};
\foreach \k in {0,...,4} {\node[tick] at (\k,-0.8) {$\k$}; \node[tick] at (-0.8,\k) {$\k$};}
\node[small vertex] (p00) at (0,0) {0};
\node[small vertex] (p10) at (1,0) {1};
\node[small vertex] (p01) at (0,1) {2};
\node[small vertex] (p20) at (2,0) {3};
\node[small vertex] (p11) at (1,1) {4};
\node[small vertex] (p02) at (0,2) {5};
\node[small vertex] (p30) at (3,0) {6};
\node[small vertex] (p21) at (2,1) {7};
\node[small vertex] (p12) at (1,2) {8};
\node[small vertex] (p03) at (0,3) {9};
\node[small vertex] (p40) at (4,0) {10};
\node[small vertex] (p31) at (3,1) {11};
\node[small vertex] (p22) at (2,2) {12};
\node[small vertex] (p13) at (1,3) {13};
\node[small vertex] (p04) at (0,4) {14};
\draw[->, primary] (p10) -- (p01);
\draw[->, primary] (p20) -- (p11);
\draw[->, primary] (p11) -- (p02);
\draw[->, primary] (p30) -- (p21);
\draw[->, primary] (p21) -- (p12);
\draw[->, primary] (p12) -- (p03);
\draw[->, primary] (p40) -- (p31);
\draw[->, primary] (p31) -- (p22);
\draw[->, primary] (p22) -- (p13);
\draw[->, primary] (p13) -- (p04);
\end{tikzpicture}
\end{center}
```

The pairing function $\pi$ numbers the pairs $(m,n)$ diagonal by diagonal: $m+n=0$, then $m+n=1$, and so on, each diagonal from bottom right to top left.

:::

::: {#cor-rationals-countable .corollary name="The rationals are countable"}

$\mathbb Z\times\mathbb Z$ and $\mathbb Q$ are countable.

:::

::: {.proof}

1. With $f:\mathbb N\to\mathbb Z$ the bijection of @exm-countable-sets-n-z, $(a,b)\mapsto\pi(f^{-1}(a),f^{-1}(b))$ is a bijection $\mathbb Z\times\mathbb Z\to\mathbb N$.

2. Write each rational as $\frac ab$ in lowest terms with $b>0$ (and $0=\frac01$). This is an injection $\mathbb Q\to\mathbb Z\times\mathbb Z$, and composing with step 1 gives an injection into $\mathbb N$. Apply @prp-injection-into-countable.

:::

::: {#rmk-countable-sets-spiral .remark name="A picture"}

Walking along the diagonals $m+n=0,1,2,\dots$ of the grid of pairs, or along a spiral through the integer grid, visits every point once. That is all the formula $\pi$ says. There are infinitely many rationals between any two natural numbers, and still only as many rationals as natural numbers.

:::

::: {#prp-finite-strings-countable .proposition name="Finite strings are countable"}

For a finite alphabet $\Sigma$, the set $\Sigma^*$ of all finite strings (@def-cardinality-and-standard-sets-1) is countable.

:::

::: {.proof}

List the strings by length, and those of the same length in alphabetical order: for $\{0,1\}^*$ this is $\varepsilon,0,1,00,01,10,11,000,\dots$. Each length contributes finitely many strings, so every string appears at a finite position, exactly once. Sending a string to its position is a bijection with $\mathbb N$.

:::

::: {#exm-countable-polynomials .example name="Polynomials with natural-number coefficients"}

Write the coefficients of a polynomial in binary, from the highest power down, and separate them by the symbol $2$, writing nothing for a zero coefficient. For $5x^5+2x^4+7x^3+4x+6$ the coefficients $5,2,7,0,4,6$ become the blocks $101,10,111,\varepsilon,100,110$ and the ternary string
$$1012102111221002110.$$
The polynomial can be read back from the string, block by block, so this is an injection into $\{0,1,2\}^*$, which is countable (@prp-finite-strings-countable). So the set of such polynomials is countable.

:::
