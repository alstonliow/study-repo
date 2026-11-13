---
title: Unordered Selection without Replacement
sources: [fit1058-cn-8.8]
requires: [math/discrete/counting/selection, math/discrete/counting/sum-and-product-rules]
level: core
status: draft
---

<!-- Migrated from 1058note 08-counting-combinatorics.tex, §8.8. -->

::: {#prp-binomial-formula .proposition}
$$
\binom{n}{r} = \frac{n!}{(n-r)!\,r!} = \frac{(n)_r}{r!}.
$$
:::

::: {.remark name="Dividing out the order"}
Already @sec-math-discrete-sets-power-set; each $r$-subset corresponds to $r!$ ordered sequences (@sec-math-discrete-counting-selection), collapsed by dividing.
:::

::: {#thm-division-rule .theorem name='Division rule ("Second Rule of Counting") (extra)'}
Let $A,B$ be finite and let $f:A\to B$ be *$m$-to-one*, i.e. every $b\in B$ has exactly $m$ preimages. Then
$$
|B| = \frac{|A|}{m}.
$$
:::

::: {.proof}
Each $a\in A$ has exactly one image, so the preimage sets $f^{-1}(b)$, $b\in B$, are pairwise disjoint with union $A$. By the sum rule (@sec-math-discrete-counting-sum-and-product-rules),
$$
|A| = \sum_{b\in B}\left|f^{-1}(b)\right| = \sum_{b\in B} m = m\,|B|.
$$
:::

::: {.remark name="The hypothesis is essential"}
Every $b$ must have the *same* number $m$ of preimages. @sec-math-discrete-counting-stars-and-bars shows a natural situation where this fails.
:::

::: {#exm-poker-hands .example name="Poker hands"}
Let $A$ be the set of ordered $5$-card deals, $B$ the set of $5$-card hands, and let $f$ send a deal to its set of cards. Each hand arises from exactly $5!$ deals, so $f$ is $5!$-to-one and
$$
|B| = \frac{52\cdot51\cdot50\cdot49\cdot48}{5!} = \frac{52!}{47!\,5!} = 2\,598\,960.
$$
:::

::: {#prp-pascal-identity .proposition name="Pascal's identity, combinatorial proof"}
$$
\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}.
$$
:::

::: {.proof}
Fix element $x\in A$, $|A|=n$. Every $r$-subset of $A$ either contains $x$ (choose the remaining $r-1$ from $A\setminus\{x\}$: $\binom{n-1}{r-1}$ ways) or excludes $x$ (choose all $r$ from $A\setminus\{x\}$: $\binom{n-1}{r}$ ways) -- exhaustive, mutually exclusive cases.
:::

::: {#cor-alternating-sum .corollary name="Alternating sum"}
For $n\ge1$,
$$
\sum_{k=0}^n(-1)^k\binom{n}{k}=0.
$$
:::

::: {.proof}
Let $|A|=n\ge1$ and fix $a\in A$. The map $X\mapsto X\triangle\{a\}$ (add $a$ if absent, remove it if present) is a bijection from the even-size subsets of $A$ to the odd-size ones. So there are equally many of each, i.e. $\sum_{k \text{ even}}\binom nk=\sum_{k \text{ odd}}\binom nk$, which is the claim.
:::

::: {.remark name="Why $n\ge1$"}
The hypothesis $n\ge1$ is needed: for $n=0$ the sum is $\binom00=1$. This corollary drives the combinatorial proof of inclusion--exclusion in @sec-math-discrete-counting-inclusion-exclusion.
:::

::: {.remark name="Combinatorial proofs"}
To prove an identity combinatorially, show that both sides count the same set. Either count one set in two ways (*double counting*), or exhibit a bijection between the sets counted by the two sides (@thm-bijection-rule). Pascal's identity above is a double-counting proof, and so is the next one.
:::

::: {#prp-hockey-stick .proposition name="Hockey-stick identity (extra)"}
For $0\le k<n$,
$$
\binom{n}{k+1}=\binom{n-1}{k}+\binom{n-2}{k}+\cdots+\binom{k}{k}=\sum_{i=1}^{n-k}\binom{n-i}{k}.
$$
:::

::: {.proof}
**Left side**: $\binom{n}{k+1}$ counts the $(k+1)$-subsets $X\subseteq\{1,\dots,n\}$.

**Right side** (classify $X$ by its minimum): Suppose $\min X=i$. Then $X=\{i\}\cup Y$, where $Y$ is a $k$-subset of $\{i+1,\dots,n\}$, a set with $n-i$ elements. So there are $\binom{n-i}{k}$ such $X$.

- $Y$ needs $k$ elements, so $n-i\ge k$, i.e. $1\le i\le n-k$.
- Every $X$ has exactly one minimum, so these cases are disjoint and exhaustive.

By the sum rule (@sec-math-discrete-counting-sum-and-product-rules),
$$
\binom{n}{k+1}=\sum_{i=1}^{n-k}\binom{n-i}{k}.
$$
:::

::: {#exm-hockey-stick .example}
$n=5$, $k=1$: $\binom52=10$, and $\binom41+\binom31+\binom21+\binom11=4+3+2+1=10$. The $2$-subsets of $\{1,\dots,5\}$ with minimum $1,2,3,4$ number $4,3,2,1$ respectively.
:::

::: {.remark name="Name"}
In Pascal's triangle the summands lie along a diagonal, and the left-hand side sits just off the end of that diagonal, giving a hockey-stick shape.
:::
