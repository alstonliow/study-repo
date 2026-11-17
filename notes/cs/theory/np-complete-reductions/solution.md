<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-8-q2" status="draft"}
(a) *In NP:* a certificate is three distinct assignments; check that each satisfies $\phi$. *NP-hard*, from SAT: given $\phi$ on variables $x_1,\dots,x_n$, let $\phi'=\phi\land(z_1\lor z_2)$ with two new variables. Every satisfying assignment of $\phi$ extends to exactly three of $\phi'$ ($z_1z_2\in\{01,10,11\}$), and every satisfying assignment of $\phi'$ restricts to one of $\phi$. So $\phi$ is satisfiable iff $\phi'$ has at least three satisfying assignments.

(b) DONUT with all profits $1$ is independent set, which is NP-complete (@thm-independent-set-np-complete, by a reduction from 3SAT). So map an independent-set instance $(G,k)$ to $(G,p\equiv1,k)$. If a polynomial-time algorithm found a maximum-profit set $U$, we could decide DONUT by comparing $\sum_{u\in U}p(u)$ with $k$, and so solve an NP-complete problem in polynomial time, which gives P = NP (@prp-np-complete-consequences).

(c) *Decision version:* given the tasks and an integer $P$, is there a schedule with profit at least $P$? *In NP:* the certificate is the chosen tasks with their start times; check that they do not overlap, that each finishes by its deadline, and that the profits add up to at least $P$. *NP-hard*, from subset sum (@thm-subset-sum-np-complete): for numbers $s_1,\dots,s_n$ and target $T$, make tasks with $t_j=p_j=s_j$ and $d_j=T$, and ask for profit $P=T$. A subset with sum $T$ runs back to back in $[0,T]$ with profit $T$. Conversely, a schedule with profit at least $T$ uses total time at least $T$ inside $[0,T]$, so exactly $T$: its tasks form a subset with sum $T$.
:::
