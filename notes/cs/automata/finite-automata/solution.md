<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-1-q32" status="draft"}
1. *A DFA for $B^{\mathcal R}$.* Reading $w^{\mathcal R}$ means reading the columns of $w$ from the least significant bit upwards, which is the order in which addition is done by hand. Use the states $c_0,c_1$ (current carry $0$ or $1$) and a dead state $d$; the start state and the only accept state are $c_0$.

2. *Transitions.* In state $c_r$, on a column with top bits $a,b$ and bottom bit $s$: if $a+b+r\equiv s \pmod 2$, go to $c_{r'}$ with $r'=1$ iff $a+b+r\ge2$; otherwise go to $d$. The state $d$ loops on every symbol.

3. *Correctness.* By induction on the number of columns read, the DFA is in $c_r$ exactly when the low-order bits read so far satisfy "bottom = top + middle" with outgoing carry $r$. The whole string is a correct sum iff this holds at the end with no carry left over, that is, in state $c_0$. So the DFA recognizes $B^{\mathcal R}$.

4. *Back to $B$.* Regular languages are closed under reversal (Problem 1.31), and $B=(B^{\mathcal R})^{\mathcal R}$, so $B$ is regular.
:::

::: {.solution for="prob-sipser3e-1-q41" status="draft"}
1. Let $M_A=(Q_A,\Sigma,\delta_A,q_A,F_A)$ and $M_B=(Q_B,\Sigma,\delta_B,q_B,F_B)$ be DFAs for $A$ and $B$.

2. Build $M$ with states $Q_A\times Q_B\times\{0,1\}$, start state $(q_A,q_B,0)$ and accept states $F_A\times F_B\times\{0\}$. The bit says whose turn it is:
$$\delta((p,q,0),c)=(\delta_A(p,c),q,1),\qquad \delta((p,q,1),c)=(p,\delta_B(q,c),0).$$

3. On $w=a_1b_1\cdots a_kb_k$ the first component runs $M_A$ on $a_1\cdots a_k$, the second runs $M_B$ on $b_1\cdots b_k$, and the bit is $0$ at the end. A string of odd length ends with bit $1$ and is rejected, as it must be.

4. So $M$ accepts exactly the perfect shuffle of $A$ and $B$ (for $k=0$, the empty string is accepted iff $\varepsilon\in A$ and $\varepsilon\in B$, as required), and the perfect shuffle is regular.
:::

::: {.solution for="prob-sipser3e-1-q59" status="draft"}
1. *Merging a pair.* Call a string $u$ a merging word for states $p\ne q$ if $\delta(p,u)=\delta(q,u)$. Since $M$ has a synchronizing sequence $s$, every pair has one ($s$ itself).

2. *Short merging words.* Consider the graph whose nodes are the unordered pairs $\{p,q\}$, with an edge labelled $\sigma$ from $\{p,q\}$ to $\{\delta(p,\sigma),\delta(q,\sigma)\}$. A shortest merging word for $\{p,q\}$ is a shortest path from $\{p,q\}$ to a node with $\delta(p,u)=\delta(q,u)$. A shortest path does not repeat a node, and there are at most $\binom k2$ pairs with $p\ne q$, so some merging word has length at most $\binom k2$.

3. *Greedy merging.* Let $X=Q$. While $|X|\ge2$, pick $p\ne q$ in $X$, take a short merging word $u$ for them, append $u$ to the sequence built so far, and replace $X$ by $\delta(X,u)$. The set never grows, and it loses at least one element per round, so there are at most $k-1$ rounds.

4. *Length.* The concatenation $s'$ maps every state to the single state left in $X$, so it is a synchronizing sequence, of length at most $(k-1)\binom k2\le k^3$.

5. *Improvement.* The argument already gives $(k-1)\binom k2<k^3/2$. Choosing the pair more carefully gives about $k^3/6$; Černý's conjecture says $(k-1)^2$ always suffices, and it is still open.
:::
