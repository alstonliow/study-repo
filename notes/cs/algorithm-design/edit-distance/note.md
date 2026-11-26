---
title: "Edit Distance"
sources: []
requires: [cs/algorithm-design/lcs]
status: draft
---

<!-- Added 2026-11-26 for the CSES problem Edit Distance, in our own wording. TODO: add a source. -->

How many single-character edits turn one string into another? This is the *Levenshtein distance*, solved by a table like the one for longest common subsequences (@sec-cs-algorithm-design-lcs).

::: {#def-edit-distance .definition name="Edit distance"}

For strings $A=a_1\dots a_m$ and $B=b_1\dots b_n$, an *edit* is the insertion of a character, the deletion of a character, or the replacement of a character by another one. The edit distance $d(A,B)$ is the smallest number of edits that turn $A$ into $B$. Let $D(i,j)=d(a_1\dots a_i,\,b_1\dots b_j)$.

:::

::: {#thm-edit-distance .theorem name="Edit distance recurrence"}

$D(i,0)=i$, $D(0,j)=j$, and for $i,j\ge1$

$$
D(i,j)=\min\bigl\{D(i-1,j)+1,\; D(i,j-1)+1,\; D(i-1,j-1)+[a_i\ne b_j]\bigr\}.
$$

The table is filled in $O(mn)$ time and $d(A,B)=D(m,n)$.

:::

::: {.proof}

1. *Base cases.* Turning a prefix of length $i$ into the empty string needs $i$ deletions, and the other way round $j$ insertions; fewer edits cannot change the length by $i$.

2. *Last column of an optimal edit sequence.* Align the two strings: every optimal sequence of edits can be written as an alignment in which each position of $A$ is matched to a position of $B$, deleted, or replaced, and each remaining position of $B$ is inserted. Look at how the last characters $a_i$ and $b_j$ are treated.

3. *Cases.* Either $a_i$ is deleted (cost $1$ plus an optimal alignment of $a_1..a_{i-1}$ with $b_1..b_j$), or $b_j$ is inserted (cost $1$ plus $D(i,j-1)$), or $a_i$ is matched with $b_j$ (cost $[a_i\ne b_j]$ plus $D(i-1,j-1)$). Each remainder must itself be optimal, otherwise it could be replaced to improve the whole.

4. *Time.* $(m+1)(n+1)$ entries with three lookups each.

:::

::: {#exm-edit-distance-1 .example name="LOVE to MOVIE"}

For $A=\text{LOVE}$ and $B=\text{MOVIE}$ the distance is $2$: replace L by M, and insert I before E. The table below (rows $A$, columns $B$) ends in $D(4,5)=2$.

:::

::: {#fig-edit-distance-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm,y=0.8cm]
\foreach \r/\row in {0/{0,1,2,3,4,5},1/{1,1,2,3,4,5},2/{2,2,1,2,3,4},3/{3,3,2,1,2,3},4/{4,4,3,2,2,2}} {
  \foreach \v [count=\c from 0] in \row {
    \draw[cell frame] (\c,-\r) rectangle +(0.8,0.8);
    \node[lab] at (\c+0.4,-\r+0.4) {$\v$};
  }
}
\foreach \ch [count=\c from 1] in {M,O,V,I,E} {\node[lab] at (\c+0.4,1.1) {\ch};}
\foreach \ch [count=\r from 1] in {L,O,V,E} {\node[lab] at (-0.4,-\r+0.4) {\ch};}
\draw[hl cell] (5,-4) rectangle +(0.8,0.8);
\end{tikzpicture}
\end{center}
```

@exm-edit-distance-1: the table $D$ for LOVE and MOVIE, with $D(4,5)=2$ highlighted.

:::

::: {#rmk-edit-distance-1 .remark name="Related problems"}

With only insertions and deletions the distance is $m+n-2\,\mathrm{LCS}(A,B)$ (@sec-cs-algorithm-design-lcs). Keeping only two rows of the table reduces the memory to $O(n)$, and an optimal sequence of edits is recovered by following back from $(m,n)$ to a predecessor attaining the minimum.

:::
