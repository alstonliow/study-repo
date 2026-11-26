---
title: "Linear Probing"
sources: [mit6851-10]
requires: [cs/data-structures/independent-hash-families, math/probability/tail-bounds/chernoff-bounds]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 10, in our own wording; proofs written out in steps. The proof is the lecture's "dangerous interval" argument for totally random hashing; the constants were not rechecked beyond the inequalities written below. -->

In *linear probing* a key $x$ is stored in the first free slot among $h(x),h(x)+1,h(x)+2,\dots$ (modulo $m$). It looks bad because runs of full slots grow ("the rich get richer"), yet it is fast in practice because successive probes hit the same cache line.

::: {#thm-linear-probing .theorem name="Linear probing with a random hash function"}

Let $h$ be a totally random hash function and let $n$ keys be stored in a table of $m=3n$ slots. Then a search, insert or delete takes $O(1)$ expected time.

:::

::: {.proof}

1. *Reduction to runs.* The time of an operation on $x$ is at most the length of the maximal run of full slots containing (or ending next to) the slot $h(x)$. It suffices to bound the expected length of that run by a constant.

2. *Dangerous nodes.* Imagine a perfect binary tree whose leaves are the slots; a node of height $j$ stands for an interval of $2^j$ slots. Call a node *dangerous* if more than $\tfrac23\cdot2^j$ keys *hash* to it (this depends only on $h$, not on where the keys end up).

3. *Probability.* The expected number of keys hashing into a node of height $j$ is $\mu=2^j\cdot n/m=2^j/3$, and "dangerous" means exceeding $2\mu$. By the Chernoff bound (@thm-chernoff-bound),
$$
\Pr[\text{dangerous}]\le\Bigl(\frac{e}{4}\Bigr)^{\mu}=\Bigl(\frac e4\Bigr)^{2^j/3},
$$
which is doubly exponentially small in $j$.

4. *A long run contains a dangerous node.* Let a run have length in $[2^\ell,2^{\ell+1})$ and consider the nodes of height $j=\ell-3$ that it overlaps. The first four of them cover more than $3\cdot2^{j}$ slots of the run (only the first can be partly outside), and every key in those slots hashed to one of those four nodes (a key landing in a run started inside it cannot have hashed to the left of the run). If none of the four were dangerous, at most $4\cdot\tfrac23\cdot2^j=\tfrac83\cdot2^j<3\cdot2^j$ keys could occupy them, a contradiction.

5. *Expected run length.* A run of length about $2^\ell$ through the position of $x$ lies within $2^{\ell+1}$ of it, which touches $O(1)$ nodes of height $\ell-3$; by a union bound the probability that it exists is $O(1)\cdot(e/4)^{2^{\ell-3}/3}$. So the expected length is $\sum_\ell2^{\ell+1}\cdot O\bigl((e/4)^{2^{\ell-3}/3}\bigr)=O(1)$, since the terms decrease doubly exponentially.

:::

::: {#rmk-linear-probing-1 .remark name="Load factor and independence"}

For a table of $(1+\varepsilon)n$ slots the expected time is $O(1/\varepsilon^2)$ (Knuth's old result). It is $O(1)$ already for $5$-independent families (Pagh, Pagh and Ružić); $O(\log n)$-independence was known earlier; $2$-independent families and some $4$-independent ones need $\Omega(\log n)$; and simple tabulation hashing (@def-simple-tabulation) matches the random-function bound.

:::
