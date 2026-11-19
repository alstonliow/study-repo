<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs188hw-6-q1" status="draft"}
Each orientation of the $k$ edges has probability $2^{-k}$. Independence with nothing observed is guaranteed exactly when every path is blocked, and with no evidence a path is blocked exactly when it contains a v-structure (@def-d-separation). The answers to parts 5 and 6 were checked by enumerating all orientations in Python for $n\le7$.

1. **$\frac14$.** The rumour must pass from $C$ (the only member of $A,B,C$ next to $G$) to $G$ and from $G$ to $F$ (a member of $D,E,F$): the edges $C\to G$ and $G\to F$, each with probability $\frac12$.
2. **$\frac12$.** The only path is $B$–$C$–$G$–$F$. It is blocked if $C$ is a collider ($B\to C\leftarrow G$, probability $\frac14$) or $G$ is a collider ($C\to G\leftarrow F$, probability $\frac14$). The first needs $G\to C$ and the second $C\to G$, so the events are disjoint and the probability is $\frac14+\frac14$.
3. **$\frac1{16}$.** The new edge closes the cycle $B$–$C$–$G$–$F$–$D$–$B$ of five edges. The network is undefined exactly when this cycle is directed (@def-bayesian-network needs an acyclic graph), which happens for $2$ of the $2^{5}$ orientations of its edges; edges outside the cycle cannot create a directed cycle.
4. **$\frac14$:** only $X_1\to X_2\leftarrow X_3$ blocks the path.
5. **$\frac{2^{n-1}-n}{2^{n-1}}$.** Write the orientation of the $n-1$ edges as a word in $R$ (pointing right) and $L$ (pointing left). Node $X_i$ is a collider when edge $i-1$ is $R$ and edge $i$ is $L$, so the path is blocked iff the word contains $RL$. The words without $RL$ are $L^{a}R^{n-1-a}$, $a=0,\dots,n-1$: $n$ of them. So the probability is $1-\frac{n}{2^{n-1}}$.
6. **$\frac{2^{n-2}-(n-1)}{2^{n-1}-n}$.** Among the $2^{n-1}-n$ words containing $RL$, count those starting with $L$: the first letter $L$ cannot be part of an $RL$, so the rest, a word of length $n-2$, must contain $RL$, which leaves $2^{n-2}-(n-1)$ words. For $n=3$ this is $0$: the only blocking orientation has $X_1\to X_2$.
:::
