<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-6-q4" status="draft"}
Measure as in the comparison table of @sec-math-discrete-graph-communication-networks, counting the edges from input terminal to output terminal, with $N=2^n$.

| diameter | switch size(s) | # switches | congestion | LMC | CML |
|---|---|---|---|---|---|
| $\log_2N+4$ | $1\times2$, $2\times2$, $2\times1$ | $3N\log_2N+3N$ | $1$ | $2\log_2N+3$ | $\sqrt N$ or $\sqrt{N/2}$ |

1. *Diameter.* The shortest route goes terminal, input switch, $b_i$, through the butterfly ($\log_2N$ edges from $b_i$ to $z_j$), output switch, terminal: $\log_2N+4$ edges.

2. *Switches.* $N$ input switches ($1\times2$), $N$ output switches ($2\times1$), the Beneš net with $2N\log_2N$ switches and the butterfly with $N(\log_2N+1)$, all $2\times2$: $3N\log_2N+3N$ in total.

3. *Congestion.* Routing every packet through the Beneš part achieves congestion $1$ (@thm-benes-congestion); the input and output switches carry one packet each. So the congestion is $1$.

4. *LMC.* For some permutations any two packets through the butterfly collide, so a congestion-$1$ routing must in the worst case send the packets through the Beneš part, whose paths have $2\log_2N-1$ edges from $a_i$ to $y_j$ (the Beneš diameter $2\log_2N+1$ counts two terminal edges); adding the two edges at each end gives $2\log_2N+3$ edges from terminal to terminal.

5. *CML.* Minimum latency forces every packet through the butterfly, which then has its own congestion, $\sqrt N$ for even $n$ and $\sqrt{N/2}$ for odd $n$.
:::

::: {.solution for="prob-mit6042f10-6-q5" status="draft"}
Paths are unique (@prp-butterfly-size), so a permutation determines the routing.

(a) A packet passes through a switch $v$ at level $i$ only if it starts at one of the $2^i$ inputs that reach $v$ and ends at one of the $2^{n-i}$ outputs reachable from $v$. Distinct packets have distinct inputs and distinct outputs, so at most $\min(2^i,2^{n-i})\le2^{n/2}=\sqrt N$ packets pass through $v$.

(b) Let $v$ be the switch at level $n/2$ whose label is all $0$s. It is reached from exactly $2^{n/2}$ inputs $I$ and reaches exactly $2^{n/2}$ outputs $O$. Choose a permutation that maps $I$ bijectively onto $O$ (and the other inputs onto the other outputs arbitrarily). Then all $2^{n/2}=\sqrt N$ packets from $I$ pass through $v$. With (a), the congestion of $B_n$ is exactly $\sqrt N$.
:::
