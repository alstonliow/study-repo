::: {.problem #prob-mit6042f10-6-q3 origin="external" source="mit6042f10-6-q3"}
In this problem we study partial orders (posets). Recall that a weak partial order $\preceq$ on a set $X$ is reflexive ($x \preceq x$), anti-symmetric ($x \preceq y \land y \preceq x \to x = y$), and transitive ($x \preceq y \land y \preceq z \to x \preceq z$). Note that it may be the case that neither $x \preceq y$ nor $y \preceq x$. A *chain* is a list of distinct elements $x_1, \ldots, x_i$ in $X$ for which $x_1 \preceq x_2 \preceq \cdots \preceq x_i$. An *antichain* is a subset $S$ of $X$ such that for all distinct $x, y \in S$, neither $x \preceq y$ nor $y \preceq x$.

The aim of this problem is to show that any sequence of $(n - 1)(m - 1) + 1$ integers either contains a non-decreasing subsequence of length $n$ or a decreasing subsequence of length $m$. Note that the given sequence may be out of order, so, for instance, it may have the form $1, 5, 3, 2, 4$ if $n = m = 3$. In this case the longest non-decreasing and longest decreasing subsequences have length 3 (for instance, consider $1, 2, 4$ and $5, 3, 2$).

(a) Label the given sequence of $(n - 1)(m - 1) + 1$ integers $a_1, a_2, \ldots, a_{(n-1)(m-1)+1}$. Show the following relation $\preceq$ on $\{1, 2, 3, \ldots, (n - 1)(m - 1) + 1\}$ is a weak poset: $i \preceq j$ if and only if $i \le j$ and $a_i \le a_j$ (as integers).

For the next part, we will need to use Dilworth's theorem, as covered in lecture. Recall that Dilworth's theorem states that if $(X, \preceq)$ is any poset whose longest chain has length $n$, then $X$ can be partitioned into $n$ disjoint antichains.

(b) Show that in any sequence of $(n - 1)(m - 1) + 1$ integers, either there is a non-decreasing subsequence of length $n$ or a decreasing subsequence of length $m$.

(c) Construct a sequence of $(n - 1)(m - 1)$ integers, for arbitrary $n$ and $m$, that has no non-decreasing subsequence of length $n$ and no decreasing subsequence of length $m$. Thus in general, the result you obtained in the previous part is best-possible.

*Note (these notes):* The theorem quoted as Dilworth's here (longest chain of length $n$ gives a partition into $n$ antichains) is its dual, often called Mirsky's theorem.
:::
