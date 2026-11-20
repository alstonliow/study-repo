<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-3-q6" status="draft"}
$A$ is *sequentially closed* if the limit of every convergent sequence in $A$ lies in $A$.

(a)

1. In the co-countable topology, $x_n \to x$ iff $x_n = x$ for all large $n$. Indeed, if $x_n \ne x$ for infinitely many $n$, the set $S = \{x_n : x_n \ne x\}$ is countable, so $X \setminus S$ is an open neighbourhood of $x$ missing infinitely many terms.

2. Hence every subset of $X$ is sequentially closed: a convergent sequence in $A$ is eventually equal to its limit, which is therefore in $A$.

3. The closed sets are $X$ and the countable subsets. For $p \in X$, $A = X \setminus \{p\}$ is uncountable and not $X$, so it is not closed, though it is sequentially closed.

(b)

1. *Closed implies sequentially closed* (in any space). Let $A$ be closed, $a_n \in A$, $a_n \to x$. If $x \notin A$, the open set $X \setminus A$ contains $x$, so it contains $a_n$ for large $n$, which is impossible.

2. *Converse.* Let $\mathcal B$ be a countable base and $A$ sequentially closed. Take $x \in \overline A$ and list the members of $\mathcal B$ containing $x$ as $B_1, B_2, \dots$ (repeating if there are finitely many). Put $V_n = B_1 \cap \cdots \cap B_n$, an open neighbourhood of $x$.

3. Since $x \in \overline A$, each $V_n$ meets $A$; choose $a_n \in V_n \cap A$.

4. $a_n \to x$: an open $U \ni x$ contains some $B_k \ni x$, and $a_n \in V_n \subset B_k \subset U$ for $n \ge k$.

5. So $x \in A$. Hence $\overline A \subset A$, and $A$ is closed.
:::
