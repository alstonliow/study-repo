<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-8-q1" status="draft"}
A 0-1 knapsack (@exm-knapsack) in which leftover capacity costs $s$ per unit.

1. *Subproblems:* $x(i,j)$, the largest profit from orders $i,\dots,n-1$ when $j$ barrels are still unsold, counting the storage cost of the barrels left at the end; $0\le i\le n$, $0\le j\le m$.
2. *Relation:* order $i$ is skipped or filled: $x(i,j)=\max\{x(i+1,j),\ p_i+x(i+1,j-a_i)\ \text{(if }a_i\le j)\}$.
3. *Order:* decreasing $i$.
4. *Base:* $x(n,j)=-sj$ (store the rest).
5. *Original:* $x(0,m)$; parent pointers give the orders to fill.
6. *Time:* $(n+1)(m+1)$ subproblems with $O(1)$ work: $O(nm)$.

This is **pseudopolynomial**: $m$ is a number in the input, not the number of input items. (Checked against brute force on small cases.)
:::

::: {.solution for="prob-mit6006s20-8-q2" status="draft"}
*Structure.* If pins $i<k$ are knocked down together, every pin between them falls earlier, so no throw pairs a pin between $i$ and $k$ with a pin outside $[i,k]$: such a throw would need $i$ or $k$ to fall first and also to fall later. So throws nest like parentheses, and we use substring subproblems (@exm-bowling, @exm-arithmetic-parenthesization).

1. *Subproblems:* for $0\le a\le b\le n$, $x(a,b)$, the best score from pins $a,\dots,b-1$; and $y(a,b)$, the best score from these pins when *all* of them must be knocked down.
2. *Relation:* look at the first pin $a$:
   $$y(a,b)=\max\Bigl\{v_a+y(a+1,b),\ v_av_{a+1}+y(a+2,b),\ \max_{a+1<k<b}\bigl(v_av_k+y(a+1,k)+y(k+1,b)\bigr)\Bigr\},$$
   and $x(a,b)$ is the same with $x$ in place of $y$ in the terms after pin $a$'s partner, plus the option $x(a+1,b)$ of leaving pin $a$ standing. The split term $v_av_k$ needs all pins strictly between $a$ and $k$ knocked down first, which is $y(a+1,k)$.
3. *Order:* increasing $b-a$.
4. *Base:* $x(a,a)=y(a,a)=0$; the adjacent-pair option needs $a+1<b$.
5. *Original:* $x(0,n)$.
6. *Time:* $O(n^2)$ subproblems with $O(n)$ work: $O(n^3)$, which is **polynomial**.

(Checked against an exhaustive search over all throw sequences on small cases.)
:::

::: {.solution for="prob-mit6006s20-8-q3" status="draft"}
Track the sums of three of the parts; the fourth is what is left.

1. *Subproblems:* $x(i,s_1,s_2,s_3)$: can $a_i,\dots,a_{n-1}$ be split among the four parts so that parts $1,2,3$ receive exactly $s_1,s_2,s_3$ more? For $0\le i\le n$ and $0\le s_1,s_2,s_3\le m$.
2. *Relation:* $a_i$ goes to one of the four parts: $x(i,s_1,s_2,s_3)$ is true iff $x(i+1,s_1,s_2,s_3)$ (part $4$), or $s_1\ge a_i$ and $x(i+1,s_1-a_i,s_2,s_3)$, or the same for $s_2$ or $s_3$.
3. *Order:* decreasing $i$.
4. *Base:* $x(n,s_1,s_2,s_3)$ is true iff $s_1=s_2=s_3=0$.
5. *Original:* among all $(s_1,s_2,s_3)$ with $x(0,s_1,s_2,s_3)$ true, take one minimising $\max\{s_1,s_2,s_3,m-s_1-s_2-s_3\}$, and follow parent pointers to the parts.
6. *Time:* $(n+1)(m+1)^3$ subproblems with $O(1)$ work: $O(nm^3)$. This is **pseudopolynomial**, as it depends on the size of the sum $m$.
:::

::: {.solution for="prob-mit6006s20-8-q4" status="draft"}
*Word counts.* The uncorrupted logs have $O(m^2n)$ logs of at most $m$ characters, $O(m^3n)$ characters in all. Split them into words and count each word in a hash table keyed by the word; hashing a word costs time proportional to its length, so this takes $O(m^3n)$ expected time.

*Restoring one log* $\ell$ of length at most $m$:

1. *Subproblems:* $x(i)$, the largest total $\sum f(w)$ over restorations of the suffix $\ell[i:]$, for $0\le i\le|\ell|$.
2. *Relation:* guess the first word $\ell[i:j]$: $x(i)=\max_{i<j\le|\ell|}\bigl\{f(\ell[i:j])+x(j)\bigr\}$ (a word not in $L_u$ counts $0$).
3. *Order:* decreasing $i$. 4. *Base:* $x(|\ell|)=0$.
5. *Original:* $x(0)$, with parent pointers giving the words.
6. *Time:* $O(m)$ subproblems, each trying $O(m)$ words, each looked up in $O(m)$ time: $O(m^3)$ per log.

Over the $n$ logs, together with the counting, the total is $O(m^3n)$ (expected, because of hashing). This is **polynomial**: $m$ bounds the lengths of strings that are part of the input.
:::
