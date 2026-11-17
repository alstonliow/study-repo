---
title: "Designing Subproblems"
sources: [mit6006-16, mit6006r-16]
requires: [cs/dynamic-programming/recursive-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 16 and Recitation 16, in our own wording; examples our own (checked by computation); proofs written out in steps. -->

The hard part of dynamic programming is choosing subproblems. Natural choices are prefixes, suffixes or substrings of a sequence, and pairs of these for several sequences. When the natural subproblems do not carry enough information, *constrain* or *expand* them.

## Two sequences: longest common subsequence

A *subsequence* of a string keeps some of its characters in order, not necessarily next to each other.

::: {#exm-lcs .example name="Longest common subsequence"}

Given strings $A$ and $B$, find a longest string that is a subsequence of both. For example, ALGORITHM and LOGARITHM have the common subsequence LORITHM of length $7$, and none longer.

1. *Subproblems:* $x(i,j)$, the length of a longest common subsequence of the suffixes $A[i:]$ and $B[j:]$, for $0\le i\le|A|$, $0\le j\le|B|$.
2. *Relation:*
   $$x(i,j)=\begin{cases}1+x(i+1,j+1)&\text{if }A[i]=B[j],\\\max\{x(i+1,j),\,x(i,j+1)\}&\text{otherwise.}\end{cases}$$
3. *Order:* decreasing $i+j$ (or: decreasing $i$, and for each $i$ decreasing $j$).
4. *Base:* $x(|A|,j)=x(i,|B|)=0$.
5. *Original:* $x(0,0)$; storing which case gave each value (parent pointers) recovers the subsequence.
6. *Time:* $(|A|+1)(|B|+1)$ subproblems with $O(1)$ work: $O(|A|\cdot|B|)$.

:::

::: {#lem-lcs-relation .lemma name="Why the LCS relation is right"}

Let $a=A[i]$ and $b=B[j]$ be the first characters of the two suffixes.

1. If $a=b$, some longest common subsequence of $A[i:]$ and $B[j:]$ starts with this pair matched to each other.
2. If $a\ne b$, every common subsequence either does not use $a$ or does not use $b$.

:::

::: {.proof}

1. Take a longest common subsequence $S$. If it uses neither $a$ nor $b$, putting the common character $a=b$ in front gives a longer one, a contradiction. If its first character comes from $a$ but is matched with a later $b'=a$ in $B[j:]$ (or symmetrically), matching it with $b$ instead still works, since $b$ comes before $b'$. So we can assume $S$ starts with $a$ matched to $b$, and the rest of $S$ is a common subsequence of $A[i+1:]$ and $B[j+1:]$; so $x(i,j)=1+x(i+1,j+1)$.

2. If both $a$ and $b$ were used, each would be the first character of the subsequence (nothing comes before them in their strings), so they would be matched to each other, which needs $a=b$. Hence the best is found in $A[i+1:],B[j:]$ or in $A[i:],B[j+1:]$.

:::

## Constraining: longest increasing subsequence

::: {#exm-lis .example name="Longest increasing subsequence"}

Given a sequence $A$, find a longest strictly increasing subsequence. For $5,2,8,6,3,6,9,7$ one answer is $2,3,6,9$, of length $4$.

The natural subproblem "a longest increasing subsequence of $A[i:]$" does not combine well: knowing such a subsequence of $A[i+1:]$ does not tell us whether $A[i]$ can be put in front. So we *constrain* the subproblem to start at $A[i]$.

1. *Subproblems:* $x(i)$, the length of a longest increasing subsequence of $A[i:]$ that *starts with* $A[i]$, for $0\le i<|A|$.
2. *Relation:* guess the second element:
   $$x(i)=\max\bigl(\{1+x(j):i<j<|A|,\ A[j]>A[i]\}\cup\{1\}\bigr),$$
   where $1$ is the case that $A[i]$ is the last element.
3. *Order:* decreasing $i$. 4. *Base:* none needed (the option $1$ covers the end).
5. *Original:* $\max_ix(i)$ (guess the first element), with parent pointers to recover a subsequence.
6. *Time:* $|A|$ subproblems with $O(|A|)$ work each: $O(|A|^2)$. (With an augmented balanced search tree the work per subproblem drops to $O(\log|A|)$.)

:::

## Expanding: a two-player game

::: {#exm-coin-game .example name="Alternating coin game"}

Coins with values $v_0,\dots,v_{n-1}$ lie in a row. Two players alternately take the first or the last remaining coin; I move first. How much can I guarantee, if my opponent also plays as well as possible? For $5,10,100,25$ I can guarantee $105$ of the $140$: I take $5$, and whatever the opponent takes, I then get $100$.

*First solution*, using that the game is zero-sum (I get exactly what the opponent does not).

1. *Subproblems:* $x(i,j)$, the most that the player to move can guarantee from coins $i,\dots,j$, for $0\le i\le j<n$.
2. *Relation:* the player takes coin $i$ or coin $j$; the opponent then guarantees $x(i+1,j)$ or $x(i,j-1)$ of the rest:
   $$x(i,j)=\max\Bigl\{\sum_{k=i}^jv_k-x(i+1,j),\ \sum_{k=i}^jv_k-x(i,j-1)\Bigr\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i)=v_i$. 5. *Original:* $x(0,n-1)$.
6. *Time:* $\Theta(n^2)$ subproblems; with all sums $\sum_{k=i}^jv_k$ precomputed from prefix sums, $O(1)$ work each, $\Theta(n^2)$ in total.

*Second solution*, by *expanding* the subproblems with whose turn it is.

1. *Subproblems:* $x(i,j,p)$, the most that *I* can guarantee from coins $i,\dots,j$ when player $p\in\{\text{me},\text{you}\}$ moves next.
2. *Relation:*
   $$x(i,j,\text{me})=\max\{v_i+x(i+1,j,\text{you}),\ v_j+x(i,j-1,\text{you})\},$$
   $$x(i,j,\text{you})=\min\{x(i+1,j,\text{me}),\ x(i,j-1,\text{me})\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i,\text{me})=v_i$, $x(i,i,\text{you})=0$.
5. *Original:* $x(0,n-1,\text{me})$. 6. *Time:* $\Theta(n^2)$.

:::

::: {#rmk-subproblem-design-expansion .remark name="Constraint and expansion"}

If the relation lacks information to check a condition of the problem, or there is no natural smaller subproblem to recurse on, add a constraint (LIS: the subsequence starts here) or extra parameters (the coin game: whose turn). More subproblems give the relation more to work with; the usual trade-off is between the number of subproblems and the work per subproblem.

:::
