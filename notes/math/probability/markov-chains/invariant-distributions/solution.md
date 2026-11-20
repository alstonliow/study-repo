<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-3-q5" status="draft"}
(a) The state is the order of the books on the shelf. From a permutation $\sigma$, moving book $j$ to the front gives a permutation $\sigma_j$; the $N$ choices give $N$ distinct results (they have different front books), one of which is $\sigma$ itself (moving the front book). So $P(\sigma,\sigma_j)=1/N$ for each $j$, and $P(\sigma,\tau)=0$ for every other $\tau$.

(b) The uniform distribution $\pi(\sigma)=1/N!$. A permutation $\tau$ with front book $j$ is reached in one step exactly from the $N$ permutations obtained by inserting book $j$ into one of the $N$ positions of the rest of $\tau$, each with probability $1/N$. So every column of $P$ sums to $1$: $P$ is doubly stochastic, and $\sum_\sigma\frac1{N!}P(\sigma,\tau)=\frac1{N!}$, which is the invariance equation (@def-invariant-distribution). The chain is irreducible (any order can be built by moving books to the front in reverse order), so the stationary distribution is unique.
:::

::: {.solution for="prob-mit6041f10-8-q1" status="draft"}
(a) Let the state be the number $i\in\{0,\dots,5\}$ of pairs at the front door in the morning (so $5-i$ are at the back).

1. For $1\le i\le4$: leave by the front and return by the back moves a pair to the back, $i\to i-1$ with probability $\frac14$; leave by the back and return by the front gives $i\to i+1$ with probability $\frac14$; otherwise the state stays, probability $\frac12$.
2. For $i=0$: leaving by the front he runs barefoot and nothing moves; only "back out, front in" changes the state. So $0\to1$ with probability $\frac14$ and $0\to0$ with probability $\frac34$. Symmetrically $5\to4$ with probability $\frac14$ and $5\to5$ with probability $\frac34$.

(b) The chain is irreducible and aperiodic, and its transition matrix is symmetric, hence doubly stochastic, so the uniform distribution $\pi_i=\frac16$ is invariant (@thm-invariant-iff-constant). He runs barefoot in state $0$ when leaving by the front and in state $5$ when leaving by the back, so the long-run fraction (@thm-markov-fraction-of-time) is
$$\pi_0\cdot\tfrac12+\pi_5\cdot\tfrac12=\tfrac16.$$
:::
