---
title: "Linear-Time Suffix Array Construction (DC3)"
sources: [mit6851-16]
requires: [cs/strings/suffix-arrays]
aliases: [cs/algorithm-topics/dc3-suffix-arrays]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 16, following Kärkkäinen–Sanders–Burkhardt as presented there, in our own wording; proofs written out in steps. The lecture's variant recurses on the positions $\equiv 0,1 \pmod 3$ and sorts the positions $\equiv 2$ afterwards; this variant was implemented and tested against sorting all suffixes on 3000 random strings (alphabet sizes 2, 3 and 26). The example is our own. -->

Prefix doubling (@thm-prefix-doubling) builds a suffix array in $O(n\log n)$. The DC3 ("difference cover mod 3") algorithm needs $O(n+\operatorname{sort}(\Sigma))$ time, and with @prp-suffix-tree-array it yields the suffix tree in linear time.

::: {#def-dc3 .definition name="DC3"}

Replace the letters of $T[0..n-1]$ by their ranks among the letters occurring in $T$ (after sorting the alphabet), and extend $T$ by sentinels smaller than every letter. For $r\in\{0,1,2\}$ let $T_r$ be the text of *megaletters* (triples)

$$
T_r=\bigl\langle (T[3i+r],T[3i+r+1],T[3i+r+2])\ :\ i\ge0\bigr\rangle,
$$

so that $T_r[i..]$ represents the suffix $T[3i+r..]$. DC3 does the following.

1. Radix-sort the triples of $T_0$ and $T_1$ together and replace each by its rank (equal triples get equal ranks); this is a text $U=\langle T_0,\,\#,\,T_1\rangle$ over an alphabet of size $\le2n/3$, with a separator $\#$ smaller than all ranks.

2. If all ranks are distinct, the suffix order of $U$ is read off directly. Otherwise compute the suffix array of $U$ **recursively**. This sorts all suffixes of $T$ starting at positions $\not\equiv2\pmod 3$.

3. Sort the suffixes at positions $\equiv2\pmod 3$ by radix sort on the pair $\bigl(T[j],\ \text{rank of the suffix at }j+1\bigr)$, where position $j+1\equiv0$ was ranked in step 2.

4. *Merge* the two sorted lists with a linear merge, comparing suffixes $j\equiv2$ with $i\not\equiv2$ in $O(1)$ time:
   * $i\equiv0$: compare $\bigl(T[j],\ \mathrm{rank}(j+1)\bigr)$ with $\bigl(T[i],\ \mathrm{rank}(i+1)\bigr)$ ($j+1\equiv0$, $i+1\equiv1$ are both ranked);
   * $i\equiv1$: compare $\bigl(T[j],T[j+1],\mathrm{rank}(j+2)\bigr)$ with $\bigl(T[i],T[i+1],\mathrm{rank}(i+2)\bigr)$ ($j+2\equiv1$, $i+2\equiv0$).

:::

::: {#exm-dc3-1 .example name="banana"}

For $T=\text{banana}$ the triples at the positions $0,3$ (class $0$) are $ban,ana$ and at $1,4$ (class $1$) are $ana,na\$$. The sorted triples are $ana$ (positions $3$ and $1$, equal), $ban$ (position $0$), $na\$$ (position $4$), so the ranks are $1,2,1$ and $3$ and $U=\langle2,1,\#,1,3\rangle$. Two suffixes have equal first triples, so a recursion (or a comparison of the following triples) is needed to order positions $1$ and $3$.

:::

::: {#thm-dc3 .theorem name="DC3 builds a suffix array in linear time"}

DC3 returns the suffix array of $T$ and runs in $O(n+\operatorname{sort}(\Sigma))$ time.

:::

::: {.proof}

1. *Reduction.* $T_r[i..]$ compares exactly as the suffix $T[3i+r..]$ does, because a megaletter is compared letter by letter. So the suffix order of $U$ gives the order of the suffixes of $T$ at positions $\not\equiv2$; the separator keeps suffixes of the two halves from running into each other.

2. *Size.* $U$ has about $\tfrac23n$ megaletters, over an alphabet of size at most $\tfrac23n$ after ranking. The triples are sorted by a three-pass radix sort in $O(n)$ time, because the letters are integers $\le n$ (this is why the alphabet is ranked first).

3. *Class $2$.* The suffix $T[j..]$ with $j\equiv2$ is the letter $T[j]$ followed by the suffix at $j+1\equiv0$, whose rank is known, so one two-key radix sort (the second key already as a rank) orders them in $O(n)$.

4. *Merging.* The two lists are each sorted and are merged in $O(n)$ if every comparison costs $O(1)$. For $i\equiv0$ and $j\equiv2$ the suffix after one letter starts at $\equiv1$ and $\equiv0$, both ranked; for $i\equiv1$ and $j\equiv2$ the suffixes after two letters start at $\equiv0$ and $\equiv1$, both ranked. Two suffixes of $T_0\cup T_1$ are compared by their ranks.

5. *Time.* $T(n)=T(2n/3)+O(n)$, which is $O(n)$.

:::

::: {#rmk-dc3-1 .remark name="In practice"}

DC3 is the standard linear-time construction taught for suffix arrays; contest solutions mostly use prefix doubling with radix sort ($O(n\log n)$) or SA-IS, since the constant factor of DC3 is large. The LCP array then follows from @thm-kasai in linear time, and the suffix tree from @prp-suffix-tree-array.

:::
