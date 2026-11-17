::: {.problem #prob-mit6042f10-5-q3 origin="external" source="mit6042f10-5-q3"}
An $n$-node graph is said to be *tangled* if there is an edge leaving every set of $\lceil n/3 \rceil$ or fewer vertices. As a special case, the graph consisting of a single node is considered tangled. (Recall that the notation $\lceil x \rceil$ refers to the smallest integer greater than or equal to $x$.)

(a) Find the error in the proof of the following claim.

**Claim.** Every non-empty, tangled graph is connected.

*Proof.* The proof is by strong induction on the number of vertices in the graph. Let $P(n)$ be the proposition that if an $n$-node graph is tangled, then it is connected. In the base case, $P(1)$ is true because the graph consisting of a single node is defined to be tangled and is trivially connected.

In the inductive step, for $n \ge 1$ assume $P(1), \ldots, P(n)$ to prove $P(n + 1)$. That is, we want to prove that if an $(n + 1)$-node graph is tangled, then it is connected. Let $G$ be a tangled, $(n + 1)$-node graph. Arbitrarily partition $G$ into two pieces so that the first piece contains exactly $\lceil n/3 \rceil$ vertices, and the second piece contains all remaining vertices. Note that since $n \ge 1$, the graph $G$ has a least two vertices, and so both pieces contain at least one vertex. By induction, each of these two pieces is connected. Since the graph $G$ is tangled, there is an edge leaving the first piece, joining it to the second piece. Therefore, the entire graph is connected. This shows that $P(1), \ldots, P(n)$ imply $P(n + 1)$, and the claim is proved by strong induction.

(b) Draw a tangled graph that is not connected.

(c) An $n$-node graph is said to be *mangled* if there is an edge leaving every set of $\lceil n/2 \rceil$ or fewer vertices. Again, as a special case, the graph consisting of a single node is considered mangled. Prove the following claim. Hint: Prove by contradiction.

**Claim.** Every non-empty, mangled graph is connected.
:::
