<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-6-q3" status="draft"}
Let $L=(n-1)(m-1)+1$.

(a) *Reflexive:* $i\le i$ and $a_i\le a_i$. *Antisymmetric:* $i\preceq j$ and $j\preceq i$ give $i\le j\le i$, so $i=j$. *Transitive:* $i\le j\le k$ and $a_i\le a_j\le a_k$ give $i\preceq k$.

(b) A chain $i_1\preceq\cdots\preceq i_k$ of distinct indices is exactly a non-decreasing subsequence $a_{i_1}\le\dots\le a_{i_k}$ with $i_1<\dots<i_k$. Two distinct indices $i<j$ are incomparable exactly when $a_i>a_j$, so an antichain, listed in increasing order of index, is a decreasing subsequence. Suppose there is no non-decreasing subsequence of length $n$, so the longest chain has length $c\le n-1$. By the stated theorem, the $L$ indices split into $c\le n-1$ antichains; by the pigeonhole principle one of them has at least $\lceil L/(n-1)\rceil=m$ elements. It is a decreasing subsequence of length $m$. (The levels in @thm-parallel-schedule give such a partition.)

(c) Use $m-1$ blocks of $n-1$ numbers each: block $b=1,\dots,m-1$ is the increasing run $(m-1-b)(n-1)+1,\ \dots,\ (m-1-b)(n-1)+(n-1)$, and every number in a later block is smaller than every number in an earlier block. A non-decreasing subsequence stays inside one block, so it has at most $n-1$ terms; a decreasing subsequence takes at most one term from each block, so it has at most $m-1$ terms.
:::
