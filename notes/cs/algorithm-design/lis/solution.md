<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046r-5-q1" status="draft"}
1. *Order.* Sort the blocks by length, then width, both non-increasing: $O(n\log n)$. In any valid tower each block has $l$ and $w$ no larger than the block below it, so reading the tower from bottom to top gives the blocks in an order consistent with this sorted order (blocks with equal bases can be swapped freely). So we may assume a tower uses the blocks in increasing sorted index from bottom to top.

2. *Subproblems.* $H[i]$ = the height of the tallest tower whose *top* block is $B_i$.

3. *Relation.* The block under $B_i$, if any, is some earlier $B_j$ with a larger-or-equal base:
$$H[i]=h_i+\max\Bigl(\{0\}\cup\{H[j]: j<i,\ l_i\le l_j,\ w_i\le w_j\}\Bigr).$$

4. *Answer.* $\max_i H[i]$, computed for $i=1,\dots,n$ in order.

*Time.* $O(n)$ choices for each of $n$ subproblems: $O(n^2)$.
:::

::: {.solution for="prob-mit6006-16-q1" status="draft"}
1. *What each subproblem asks.* $x(i)=1+\max\{x(j):j>i,\ A[j]>A[i]\}$ (or $1$ if no such $j$). This is a range-maximum query over the already solved suffix, restricted to keys greater than $A[i]$.

2. *Data structure.* Keep an AVL tree storing one node per solved index $j$, keyed by $(A[j],j)$. Augment every node with $m=$ the largest $x(j)$ in its subtree. The augmentation depends only on the node and its two children, so it is maintained through insertions and rotations in $O(1)$ per changed node.

3. *Query.* To find $\max\{x(j):A[j]>a\}$, walk from the root down the search path for $a$. Whenever the walk goes left from a node with key greater than $a$, that node and its whole right subtree have keys $>a$: take its $x$ and its right child's $m$. Taking the maximum of these $O(\log|A|)$ candidates answers the query in $O(\log|A|)$.

4. *Algorithm.* For $i=|A|-1$ down to $0$: query with $a=A[i]$, set $x(i)=1+\text{answer}$ (or $1$ if no key is larger), and insert $(A[i],i)$ with value $x(i)$. Record the index that achieved the maximum as the parent pointer.

5. *Time.* $|A|$ subproblems with one query and one insertion each: $O(|A|\log|A|)$. The answer is still $\max_ix(i)$.
:::
