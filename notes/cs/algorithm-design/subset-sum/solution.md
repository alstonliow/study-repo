<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006r-18-q2" status="draft"}
Let $S=\sum_{a\in A}a$. If $A_1$ has sum $t$, the difference is $|S-2t|$, so we want a subset sum $t\le S/2$ that is as large as possible.

1. *Subproblems.* $x(i,t)$ = whether some subset of the first $i$ items has sum exactly $t$, for $0\le i\le n$ and $0\le t\le\lfloor S/2\rfloor$.

2. *Relation.* $x(i,t)=x(i-1,t)\ \lor\ \bigl(t\ge a_i \land x(i-1,t-a_i)\bigr)$ (leave out item $i$, or use it).

3. *Base.* $x(0,0)=$ true and $x(0,t)=$ false for $t>0$.

4. *Answer.* Take the largest $t$ with $x(n,t)$ true. Follow the choices back to get $A_1$, set $A_2=A\setminus A_1$; the difference is $S-2t$.

*Time.* $O(nS)$, pseudopolynomial: polynomial in $n$ and in the size of the numbers, but not in their bit lengths. (The decision version, Partition, is NP-complete, so a polynomial-time algorithm is not expected.)
:::
