<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-11-q2" status="draft"}
Write $H=H(X_1)$ and $A=A_\epsilon^{(n)}$.

(a) $-\frac1n\log_2p(X_1,\dots,X_n)=\frac1n\sum_{i=1}^{n}\log_2\frac1{p(X_i)}$, an average of i.i.d. bounded variables (finite alphabet) with mean $H$. The strong law of large numbers gives almost sure convergence (Homework 2, Problem 4 proves it under the finite fourth moment we have here).

(b) Almost sure convergence implies convergence in probability (@thm-convergence-implications), so $P\bigl(|-\frac1n\log_2p(X_{1:n})-H|>\epsilon\bigr)<\epsilon$ for large $n$, and the complement of that event is $\{X_{1:n}\in A\}$.

(c) Upper bound: $1\ge\sum_{x\in A}p(x)\ge|A|\,2^{-n(H+\epsilon)}$. Lower bound: for large $n$, $1-\epsilon<P(A)=\sum_{x\in A}p(x)\le|A|\,2^{-n(H-\epsilon)}$ (a union bound over the sequences of $A$).

(d) Take $\epsilon=\delta/2$. Then
$$P(B_n)\le P(B_n\cap A)+P(A^c)\le|B_n|\,2^{-n(H-\epsilon)}+P(A^c)\le2^{-n\delta/2}+P(A^c)\to0.$$

(e) $\log_2|A|\le n(H+\epsilon)$ by (c), so
$$E[L_n]\le P(A)\bigl(2+n(H+\epsilon)\bigr)+P(A^c)\bigl(1+n\lceil\log_2|\mathcal X|\rceil\bigr).$$
Dividing by $n$ and using $P(A^c)\to0$ from (b), $\limsup_nE[L_n]/n\le H+\epsilon$. (See also @thm-source-coding.)
:::

::: {.solution for="prob-guessing-tree-code" status="draft"}
```{.python}
def guess_counts(freqs):
    """freqs[i] > 0 is the weight of the i-th word in alphabetical order. Build the
    search tree by repeatedly merging the adjacent pair of nodes with the smallest
    total weight (the leftmost such pair on ties). Return, for each word, its depth
    in the tree: the number of questions needed to identify it."""
    nodes = [(f, [i]) for i, f in enumerate(freqs)]     # (weight, words below)
    depth = [0] * len(freqs)
    while len(nodes) > 1:
        k = min(range(len(nodes) - 1), key=lambda j: nodes[j][0] + nodes[j + 1][0])
        (a, wa), (b, wb) = nodes[k], nodes[k + 1]
        for i in wa + wb:                               # every word below moves one level down
            depth[i] += 1
        nodes[k:k + 2] = [(a + b, wa + wb)]
    return depth
```

1. Each node is stored as (weight, words below it). A merge replaces two adjacent nodes by one, so the list stays in alphabetical order.
2. A merge puts both nodes one level deeper, so it adds one to the depth of every word below them. After $n-1$ merges one node is left and the depths are final.
3. The question at a node is whether the secret comes after the last word of the left subtree, so the depths are the question counts. The depths are the codeword lengths of a prefix code, so the mean depth is at least the entropy (@thm-source-coding). The greedy tree need not be the best order-preserving tree: merging the cheapest adjacent pair is a heuristic, not an optimality guarantee.
:::
