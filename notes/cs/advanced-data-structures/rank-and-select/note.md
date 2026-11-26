---
title: "Rank and Select on Bit Vectors"
sources: [mit6851-17]
requires: [cs/advanced-data-structures/range-minimum-query]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 17, in our own wording; proofs written out in steps. The select structure is only outlined (owner scope: brief). -->

Space-efficient data structures count *bits*, not words. The two basic operations on a bit vector, rank and select, are the building blocks for succinct trees and compressed text indexes.

::: {#def-succinct .definition name="Implicit, succinct and compact"}

Let $\mathrm{OPT}$ be the information-theoretic minimum, in bits, needed to store an object of a given class (for example $\lceil\log_2 C_n\rceil\approx2n$ for binary tries with $n$ nodes, $C_n$ the Catalan number). A data structure is *implicit* if it uses $\mathrm{OPT}+O(1)$ bits, *succinct* if $\mathrm{OPT}+o(\mathrm{OPT})$ bits, and *compact* if $O(\mathrm{OPT})$ bits. Most "linear-space" structures that use $O(n)$ words are not compact, since they use $\Theta(w\cdot\mathrm{OPT})$ bits.

:::

::: {#def-rank-select .definition name="Rank and select"}

For a bit string $B[1..n]$,

$$
\operatorname{rank}(i)=\sum_{k\le i}B[k]\quad(\text{the number of }1\text{s up to position }i),\qquad
\operatorname{select}(j)=\text{the position of the }j\text{th }1.
$$

Then $\operatorname{rank}(\operatorname{select}(j))=j$.

:::

::: {#thm-rank .theorem name="Constant-time rank with $o(n)$ extra bits (Jacobson)"}

A bit string of length $n$ can be preprocessed so that $\operatorname{rank}$ takes $O(1)$ time, using $O(n\log\log n/\log n)=o(n)$ bits in addition to the string itself.

:::

::: {.proof}

1. *Lookup table.* Let $b=\tfrac12\log_2n$. For every bit string of length $b$ and every position inside it store the rank in the string: $2^b=\sqrt n$ strings, $b$ positions each and $\log_2b$ bits per answer, which is $O(\sqrt n\log n\log\log n)=o(n)$ bits.

2. *Chunks.* Split $B$ into chunks of $\log_2^2n$ bits and store, at the start of each chunk, the number of $1$s before it, using $\log_2n$ bits each: $\tfrac n{\log^2n}\cdot\log n=O(n/\log n)$ bits. (Storing such numbers for each block of length $b$ directly would need $\Theta(n)$ bits, which is too much.)

3. *Subchunks.* Split each chunk into subchunks of $b$ bits and store, at the start of each subchunk, the number of $1$s since the start of its chunk. This is at most $\log^2n$, so $O(\log\log n)$ bits: $\tfrac nb\cdot O(\log\log n)=O(n\log\log n/\log n)$ bits.

4. *Query.* $\operatorname{rank}(i)$ is the sum of the stored count of the chunk of $i$, the stored count of its subchunk, and one table lookup for the position inside the subchunk: $O(1)$ time.

:::

::: {#fig-rank-and-select-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0) rectangle +(0.5,0.5); \node[lab] at (0.25,0.25) {$1$};
\draw[cell frame] (0.5,0) rectangle +(0.5,0.5); \node[lab] at (0.75,0.25) {$0$};
\draw[cell frame] (1.0,0) rectangle +(0.5,0.5); \node[lab] at (1.25,0.25) {$1$};
\draw[cell frame] (1.5,0) rectangle +(0.5,0.5); \node[lab] at (1.75,0.25) {$1$};
\draw[cell frame] (2.0,0) rectangle +(0.5,0.5); \node[lab] at (2.25,0.25) {$0$};
\draw[cell frame] (2.5,0) rectangle +(0.5,0.5); \node[lab] at (2.75,0.25) {$0$};
\draw[cell frame] (3.0,0) rectangle +(0.5,0.5); \node[lab] at (3.25,0.25) {$1$};
\draw[cell frame] (3.5,0) rectangle +(0.5,0.5); \node[lab] at (3.75,0.25) {$0$};
\draw[cell frame] (4.0,0) rectangle +(0.5,0.5); \node[lab] at (4.25,0.25) {$1$};
\draw[cell frame] (4.5,0) rectangle +(0.5,0.5); \node[lab] at (4.75,0.25) {$1$};
\draw[cell frame] (5.0,0) rectangle +(0.5,0.5); \node[lab] at (5.25,0.25) {$0$};
\draw[cell frame] (5.5,0) rectangle +(0.5,0.5); \node[lab] at (5.75,0.25) {$1$};
\draw[cell frame] (6.0,0) rectangle +(0.5,0.5); \node[lab] at (6.25,0.25) {$0$};
\draw[cell frame] (6.5,0) rectangle +(0.5,0.5); \node[lab] at (6.75,0.25) {$0$};
\draw[cell frame] (7.0,0) rectangle +(0.5,0.5); \node[lab] at (7.25,0.25) {$0$};
\draw[cell frame] (7.5,0) rectangle +(0.5,0.5); \node[lab] at (7.75,0.25) {$1$};
\draw[hl] (0.0,-0.15) -- (3.95,-0.15);
\draw[hl] (4.0,-0.15) -- (7.95,-0.15);
\node[lab] at (2,-0.5) {chunk $1$: $0$};
\node[lab] at (6,-0.5) {chunk $2$: $4$};
\node[lab] at (1.0,-1.05) {sub: $0$};
\node[lab] at (3.0,-1.05) {sub: $3$};
\node[lab] at (5.0,-1.05) {sub: $0$};
\node[lab] at (7.0,-1.05) {sub: $3$};
\end{tikzpicture}
\end{center}
```

The two levels of counts (ones before each chunk; ones before each subchunk inside its chunk) for a $16$-bit string with chunks of $8$ and subchunks of $4$ bits (the sizes are only for the picture). Then $\operatorname{rank}(14)=4\,(\text{chunk})+3\,(\text{subchunk})+0\,(\text{table: the two bits }0,0)=7$.

:::

::: {#prp-select .proposition name="Select (Clark–Munro)"}

$\operatorname{select}$ can also be answered in $O(1)$ time with $o(n)$ extra bits, by the same idea of indirection applied to chunks that contain an equal number of $1$s rather than an equal number of positions: store the position of every $(\log n\log\log n)$th $1$; a chunk between two stored positions with more than $(\log n\log\log n)^2$ bits is *sparse*, and the positions of all its $1$s are stored explicitly (there are few such chunks); a shorter chunk is handled again by one more level of the same kind and then by a lookup table for strings of $\tfrac12\log_2n$ bits. Both $\operatorname{rank}$ and $\operatorname{select}$ can be improved to $O(n/\log^kn)$ extra bits for any constant $k$.

:::

::: {#rmk-rank-select-1 .remark name="Uses"}

Rank and select turn a bit string into a navigable structure: the level-order encoding of a binary trie (@thm-level-order-trie) and the balanced-parenthesis encoding of a tree (@def-balanced-parentheses) both need only these two operations, and a compact suffix array (@thm-compact-suffix-array) needs them for its even-suffix bit vectors. Static bit vectors with rank are also the basis of wavelet trees (not covered in the lecture).

:::
