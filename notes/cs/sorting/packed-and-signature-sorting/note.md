---
title: "Packed Sorting and Signature Sort"
sources: [mit6851-14]
requires: [cs/sorting/radix-sort, cs/data-structures/perfect-hashing]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 14, in our own wording; proofs written out in steps. The bitonic-merge bit tricks and the trie construction are only described, not worked out in full. -->

Integer sorting on the word RAM: $n$ integers of $w$ bits. Radix sort gives $O(n\cdot\lceil w/\log n\rceil)$, van Emde Boas trees $O(n\log w)$ (improved to $O(n\log\frac w{\log n})$), Han and Thorup $O(n\sqrt{\log\log n})$ randomised. Whether $O(n)$ is possible for all $w$ is open. The *signature sort* of Andersson, Hagerup, Nilsson and Raman sorts in $O(n)$ time when $w\ge\log^{2+\varepsilon}n$ (the lecture's typeset statement of the range is garbled; the condition used in its proof is $w\ge\log^{2+\varepsilon}n\log\log n$). By Thorup's equivalence a sorting algorithm with $O(S(n,w))$ time per key gives a priority queue with $O(S(n,w))$ time per insert, delete and find-min.

::: {#def-bitonic .definition name="Bitonic sequence and bitonic sort"}

A sequence is *bitonic* if it is a cyclic shift of a sequence that first increases and then decreases. To sort a bitonic sequence of even length $m$, compare the element $i$ with the element $i+m/2$ for all $i<m/2$ and swap if out of order, then recurse on both halves. After the first round every element of the left half is $\le$ every element of the right half and both halves are bitonic, so after $O(\log m)$ rounds the sequence is sorted.

:::

::: {#thm-word-merge .theorem name="Merging two words"}

Let two words each contain $k$ sorted $b$-bit integers, each integer preceded by one spare zero bit. They can be merged into one sorted run of $2k$ integers in $O(\log k)$ time.

:::

::: {.proof}

1. Concatenating the first word with the reverse of the second gives a bitonic sequence. Reversing a word is done by swapping its two halves with masks and shifts and then recursing on both halves in parallel, one level per $O(1)$ time: $O(\log k)$ in all.

2. One round of bitonic sort is $O(1)$ word operations: copy the left halves with the spare bit set to $1$, shift the right halves into place, subtract; the spare bit of each field of the difference is $1$ exactly when the left element is not smaller. Masking these bits and spreading them to full fields gives masks that select, by AND and OR, which element goes left and which goes right.

3. There are $O(\log k)$ rounds, each $O(1)$.

:::

::: {#thm-packed-sorting .theorem name="Packed sorting"}

If the word size satisfies $w\ge2(b+1)\log n\log\log n$, then $n$ integers of $b$ bits can be sorted in $O(n)$ time.

:::

::: {.proof}

1. Pack $k=\log n\log\log n$ integers into a word. A word is sorted by merge sort using @thm-word-merge as the merge: $T(k)=2T(k/2)+O(\log k)=O(k)$.

2. Two sorted lists of $r$ words are merged in $O(r\log k)$ time: merge the first two words; the lower word of the result holds the $k$ smallest of all elements and is output; the upper word is put back in front of the list that contains its maximum element (the elements that may still come later); repeat.

3. Merge sort the $n/k$ words with this merge, using the sort of step 1 as the base case. There are $\log(n/k)$ levels, each costing $O\bigl(\tfrac nk\log k\bigr)=O\bigl(\tfrac n{\log n}\bigr)$ since $\log k=O(\log\log n)$. The levels cost $O(n)$ in total, and the $n/k$ base cases cost $O(k)$ each, again $O(n)$.

:::

::: {#thm-signature-sort .theorem name="Signature sort"}

If $w\ge\log^{2+\varepsilon}n\cdot\log\log n$ for a constant $\varepsilon>0$, then $n$ integers of $w$ bits can be sorted in $O(n)$ time (randomised, for the hashing).

:::

::: {.proof}

1. Cut each integer into $\log^{\varepsilon'}n$ chunks of equal size and replace each chunk by a hash of $O(\log n)$ bits (a perfect hash computed by multiplication and masking, linear time). Hashing does not keep the order of the chunks but keeps their equality, so each integer becomes a *signature* of $O(\log^{1+\varepsilon'}n)$ bits.

2. Sort the signatures with packed sorting (@thm-packed-sorting), which now applies.

3. In the sorted list build a compressed trie of the signatures over the alphabet of chunk hashes, inserting them left to right. The longest common prefix with the previous signature comes from the most significant set bit of an XOR, and the walk up the right spine is charged to the decrease of the spine, as in the construction of a Cartesian tree (@thm-cartesian-linear): $O(n)$ in total.

4. The trie has the correct shape for the integers but its sibling order is by hash value. Sort the children of every node by the *actual* chunks, recursively, with keys (node, actual chunk, edge index), which are shorter than the original keys; after a constant number of levels the keys are small enough for packed sorting as the base case.

5. Permute the child edges accordingly and read the leaves in order.

:::
