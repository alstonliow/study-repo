<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006-16-q2" status="draft"}
1. *Subproblems for the sums.* $S(i,j)=\sum_{k=i}^jv_k$ for $0\le i\le j<n$.

2. *Relation.* $S(i,j)=S(i,j-1)+v_j$, with base $S(i,i)=v_i$. Order: increasing $j-i$ (or, for each $i$, increasing $j$).

3. *Cost of the sums.* $\Theta(n^2)$ subproblems, $O(1)$ work each: $\Theta(n^2)$.

4. *Game DP.* With $S$ stored in a table, each $x(i,j)=\max\{S(i,j)-x(i+1,j),\ S(i,j)-x(i,j-1)\}$ takes $O(1)$. So all $\Theta(n^2)$ subproblems take $\Theta(n^2)$ time, and so does the whole algorithm.
:::
