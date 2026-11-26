---
title: "Compressed and Compact Suffix Arrays"
sources: [mit6851-18]
requires: [cs/algorithm-topics/suffix-arrays, cs/advanced-data-structures/rank-and-select]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 18 (a simplified version of Grossi–Vitter for a binary alphabet), in our own wording; proofs written out in steps. The space accounting of the compact version and the survey of results are only summarised. Not tested by computation. -->

A suffix array stores $n$ integers of $\log_2n$ bits each, $\Theta(n\log n)$ bits for a text that needs only $n\log_2|\Sigma|$ bits. A *compressed* suffix array replaces it by a structure of $O(n\log|\Sigma|)$ bits that still answers "what is $\mathrm{SA}[i]$?". Pattern search then runs by binary search on $\mathrm{SA}$ as in @def-suffix-array.

::: {#def-sa-levels .definition name="Levels of a suffix array"}

Let $T_0=T$ over the binary alphabet and $\mathrm{SA}_0=\mathrm{SA}$. Level $k+1$ is obtained by pairing letters: $T_{k+1}=\langle(T_k[2j],T_k[2j+1])\ :\ j\ge0\rangle$ has half the length $n_{k+1}=n_k/2$, and $\mathrm{SA}_{k+1}=\tfrac12\cdot(\text{the entries of }\mathrm{SA}_k\text{ that are even})$ (the even suffixes of $T_k$ keep their order). Define for an index $i$ of $\mathrm{SA}_k$

* $\text{is-even}_k(i)=1$ if $\mathrm{SA}_k[i]$ is even, else $0$;
* $\text{even-succ}_k(i)=i$ if $\mathrm{SA}_k[i]$ is even, otherwise the index $j$ with $\mathrm{SA}_k[j]=\mathrm{SA}_k[i]+1$;
* $\text{even-rank}_k(i)=$ the number of even suffixes among $\mathrm{SA}_k[1..i]$, computed as $\operatorname{rank}_1$ of the bit vector $\text{is-even}_k$.

:::

::: {#lem-sa-recurrence .lemma name="One level up"}

$$
\mathrm{SA}_k[i]=2\cdot\mathrm{SA}_{k+1}\bigl[\text{even-rank}_k(\text{even-succ}_k(i))\bigr]-\bigl(1-\text{is-even}_k(i)\bigr).
$$

:::

::: {.proof}

1. If $\mathrm{SA}_k[i]$ is even, even-succ is $i$ itself, and the suffix is the $\text{even-rank}_k(i)$th even suffix, whose position in $T_{k+1}$ is half of $\mathrm{SA}_k[i]$: this is the first term with the correction $0$.

2. If $\mathrm{SA}_k[i]$ is odd, the suffix one position later is even and sits at index $j=\text{even-succ}_k(i)$ of $\mathrm{SA}_k$. By step 1 the first term gives $\mathrm{SA}_k[j]$, and $\mathrm{SA}_k[i]=\mathrm{SA}_k[j]-1$.

:::

To use the lemma one must evaluate $\text{even-succ}_k$ without storing it. The odd suffixes are ordered by their first letter of $T_k$ and then by the even suffix that follows, so the entries $(T_k[\mathrm{SA}_k[i]],\ \text{even-succ}_k(i))$ are sorted, and only the first-letter part changes slowly. Store the leading $\log n_k$ bits of the values by a unary differential encoding (about $\tfrac32n_k$ bits, recovered with $\operatorname{rank}$ and $\operatorname{select}$) and the remaining $2^k$ bits (the letter of $T_k$) explicitly.

::: {#thm-compact-suffix-array .theorem name="Compact suffix array (Grossi–Vitter, simplified)"}

Keep $1+1/\varepsilon$ levels $k=0,\varepsilon\ell,2\varepsilon\ell,\dots$ with $\ell=\lg\lg n$ and, at a kept level, call a suffix "even" if its position is divisible by $2^{\varepsilon\ell}$. Then $\mathrm{SA}[i]$ can be computed in $O(\log^{\varepsilon'}n)$ time for every $\varepsilon'>\varepsilon$, in $O(n\log|\Sigma|)$ bits (for a binary alphabet, $(6+1/\varepsilon)n+o(n)$ bits), and the last level, of $n/\log n$ entries, is stored as an ordinary suffix array.

:::

::: {.proof}

1. *Query.* To get $\mathrm{SA}_{k\varepsilon\ell}[i]$, follow $\text{even-succ}$ at most $2^{\varepsilon\ell}$ times until the index reaches a suffix at an even position, recur on the next kept level with the even-rank of that index, multiply the answer by $2^{\varepsilon\ell}$, and subtract the number of steps taken, exactly as in @lem-sa-recurrence.

2. *Time.* There are $O(1/\varepsilon)$ levels, each costing $2^{\varepsilon\ell}\cdot O(1)=O(\log^\varepsilon n)$ steps of $O(1)$ rank and select operations (or $\log\log n$ factors absorbed by increasing $\varepsilon$).

3. *Space.* Each kept level stores the bit vector $\text{is-even}$ with its rank structure ($n_k+o(n_k)$ bits) and the encoding of even-succ ($O(n_k)$ bits); the lengths $n_{k}$ shrink geometrically along the kept levels, so the total over $1+1/\varepsilon$ levels is $O(n)$ bits, and the final explicit array has $O(n)$ bits.

:::

::: {#rmk-compact-suffix-arrays-1 .remark name="Further results (not proved)"}

The lecture lists: Ferragina–Manzini (the FM-index, space about $5H_k(T)n$ bits, pattern search in $O(|P|+|\text{output}|\log^\varepsilon n)$ time; counting in $O(|P|)$); Sadakane (space $\tfrac1\varepsilon H_0(T)n$, good for large alphabets); and succinct versions (space $H_k(T)n+o(n)$ bits) by Grossi–Gupta–Vitter and Ferragina–Manzini–Mäkinen–Navarro. Here $H_k$ is the $k$th-order empirical entropy. Compact suffix *trees* are obtained with additional structures for the tree shape.

:::
