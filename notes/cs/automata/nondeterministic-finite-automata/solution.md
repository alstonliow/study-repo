<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-1-q60" status="draft"}
1. *Idea.* Stay in a start state while reading, and guess the $\mathtt a$ that is exactly $k$ places from the end; then count the remaining $k-1$ symbols.

2. *Formal description.* $N=(Q,\Sigma,\delta,q_0,F)$ with $Q=\{q_0,q_1,\dots,q_k\}$, $F=\{q_k\}$ and
$$\delta(q_0,\mathtt a)=\{q_0,q_1\},\quad \delta(q_0,\mathtt b)=\{q_0\},\quad \delta(q_i,\sigma)=\{q_{i+1}\}\ (1\le i<k,\ \sigma\in\Sigma),$$
and $\delta(q_k,\sigma)=\emptyset$, with no $\varepsilon$-moves.

3. *State diagram.* $q_0$ has a self-loop labelled $\mathtt{a,b}$ and an edge labelled $\mathtt a$ to $q_1$; then a chain $q_1\to q_2\to\cdots\to q_k$ with each edge labelled $\mathtt{a,b}$; $q_k$ is the only accept state and has no outgoing edges.

4. *Correctness.* A branch is in $q_k$ at the end iff it moved to $q_1$ on an $\mathtt a$ that was followed by exactly $k-1$ more symbols, that is, iff the input is in $\Sigma^*\mathtt a\Sigma^{k-1}=C_k$.
:::

::: {.solution for="prob-sipser3e-1-q61" status="draft"}
1. Suppose a DFA $M$ with fewer than $2^k$ states recognizes $C_k$. There are $2^k$ strings of length $k$, so by pigeonhole two different ones, $u\ne v$, lead $M$ from the start state to the same state.

2. Let $i$ be a position where they differ; without loss of generality $u$ has $\mathtt a$ there and $v$ has $\mathtt b$.

3. Append $z=\mathtt b^{i-1}$. In $uz$ (length $k+i-1$) the symbol at position $i$ is exactly $k$ places from the right-hand end, and it is $\mathtt a$, so $uz\in C_k$. In $vz$ that symbol is $\mathtt b$, so $vz\notin C_k$.

4. But $M$ is in the same state after $u$ and after $v$, so it ends in the same state on $uz$ and on $vz$, and accepts both or neither. Contradiction; hence every DFA for $C_k$ has at least $2^k$ states.
:::
