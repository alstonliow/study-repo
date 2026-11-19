<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-3-q5" status="draft"}
(a) The state is the order of the books on the shelf. From a permutation $\sigma$, moving book $j$ to the front gives a permutation $\sigma_j$; the $N$ choices give $N$ distinct results (they have different front books), one of which is $\sigma$ itself (moving the front book). So $P(\sigma,\sigma_j)=1/N$ for each $j$, and $P(\sigma,\tau)=0$ for every other $\tau$.

(b) The uniform distribution $\pi(\sigma)=1/N!$. A permutation $\tau$ with front book $j$ is reached in one step exactly from the $N$ permutations obtained by inserting book $j$ into one of the $N$ positions of the rest of $\tau$, each with probability $1/N$. So every column of $P$ sums to $1$: $P$ is doubly stochastic, and $\sum_\sigma\frac1{N!}P(\sigma,\tau)=\frac1{N!}$, which is the invariance equation (@def-invariant-distribution). The chain is irreducible (any order can be built by moving books to the front in reverse order), so the stationary distribution is unique.
:::
