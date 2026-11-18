<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-8-q2" status="draft"}
(a) *In NP:* a certificate is three distinct assignments; check that each satisfies $\phi$. *NP-hard*, from SAT: given $\phi$ on variables $x_1,\dots,x_n$, let $\phi'=\phi\land(z_1\lor z_2)$ with two new variables. Every satisfying assignment of $\phi$ extends to exactly three of $\phi'$ ($z_1z_2\in\{01,10,11\}$), and every satisfying assignment of $\phi'$ restricts to one of $\phi$. So $\phi$ is satisfiable iff $\phi'$ has at least three satisfying assignments.

(b) DONUT with all profits $1$ is independent set, which is NP-complete (@thm-independent-set-np-complete, by a reduction from 3SAT). So map an independent-set instance $(G,k)$ to $(G,p\equiv1,k)$. If a polynomial-time algorithm found a maximum-profit set $U$, we could decide DONUT by comparing $\sum_{u\in U}p(u)$ with $k$, and so solve an NP-complete problem in polynomial time, which gives P = NP (@prp-np-complete-consequences).

(c) *Decision version:* given the tasks and an integer $P$, is there a schedule with profit at least $P$? *In NP:* the certificate is the chosen tasks with their start times; check that they do not overlap, that each finishes by its deadline, and that the profits add up to at least $P$. *NP-hard*, from subset sum (@thm-subset-sum-np-complete): for numbers $s_1,\dots,s_n$ and target $T$, make tasks with $t_j=p_j=s_j$ and $d_j=T$, and ask for profit $P=T$. A subset with sum $T$ runs back to back in $[0,T]$ with profit $T$. Conversely, a schedule with profit at least $T$ uses total time at least $T$ inside $[0,T]$, so exactly $T$: its tasks form a subset with sum $T$.
:::

::: {.solution for="prob-mit6046r-8-q1" status="draft"}
1. *In NP.* The certificate is the order of the vertices along the path. Check that it lists each vertex once and that consecutive vertices are joined by edges: $O(|V|+|E|)$.

2. *Reduction.* Given $G$, pick any vertex $v$. Build $G'$ by replacing $v$ with two vertices $v_{\text{out}}$ (keeping the edges leaving $v$) and $v_{\text{in}}$ (keeping the edges entering $v$), and adding new vertices $s,t$ with edges $s\to v_{\text{out}}$ and $v_{\text{in}}\to t$. This takes polynomial time.

3. *Cycle $\Rightarrow$ path.* A Hamiltonian cycle $v\to u_1\to\dots\to u_{n-1}\to v$ in $G$ gives the path $s\to v_{\text{out}}\to u_1\to\dots\to u_{n-1}\to v_{\text{in}}\to t$ in $G'$, which visits every vertex once.

4. *Path $\Rightarrow$ cycle.* In $G'$, $s$ has no incoming edges and $t$ no outgoing ones, so a Hamiltonian path must start at $s$ and end at $t$. Hence it has the form $s\to v_{\text{out}}\to\dots\to v_{\text{in}}\to t$, and merging $v_{\text{out}}$ and $v_{\text{in}}$ back into $v$ gives a Hamiltonian cycle in $G$.

So Hamiltonian Cycle $\le_p$ Hamiltonian Path, and Hamiltonian Path is NP-complete.
:::

::: {.solution for="prob-mit6046r-8-q2" status="draft"}
Here $A=\sum_i a_i$. Write $X=\{x_1,\dots,x_q\}$, $Y=\{y_1,\dots,y_q\}$, $Z=\{z_1,\dots,z_q\}$, and let $N(a)$ be the number of triples containing element $a$.

1. *In NP.* The certificate is the partition; check the size and sum of each group in polynomial time.

2. *Trivial case.* If some element lies in no triple, output a fixed "no" instance of 4-Partition. Otherwise every $N(a)\ge 1$.

3. *Numbers.* Choose a base $r=100q$, large enough that no sum of four numbers below ever carries between digits. Create:
   - for each $x_i$: one *actual* number $10r^4+ir^3+1$ and $N(x_i)-1$ *dummy* numbers $11r^4+ir^3+1$;
   - for each $y_j$: one actual $10r^4+jr^2+2$ and $N(y_j)-1$ dummies $11r^4+jr^2+2$;
   - for each $z_k$: one actual $10r^4+kr+4$ and $N(z_k)-1$ dummies $8r^4+kr+4$;
   - for each triple $(x_i,y_j,z_k)\in T$: a *triple* number $10r^4-ir^3-jr^2-kr+8$.

   Element $a$ gets $N(a)$ numbers in total, so there are $4|T|$ numbers, i.e. $|T|$ groups, and the target is $t=40r^4+15$. Every number lies between $8r^4$ and $11r^4+r^4$, inside $(t/5,t/3)$.

4. *Matching $\Rightarrow$ partition.* For each triple $(x_i,y_j,z_k)$ in the matching, group its triple number with the actual numbers of $x_i,y_j,z_k$: the sum is $40r^4+15$. Each remaining triple $(x_i,y_j,z_k)$ is grouped with one dummy each of $x_i,y_j,z_k$: $10+11+11+8=40$, so again $40r^4+15$. Element $a$ lies in exactly one matched triple and $N(a)-1$ unmatched ones, so each number is used exactly once.

5. *Partition $\Rightarrow$ matching.* Take a group with sum $t$.
   - *Last digit.* The constant terms are $1,2,4,8$, and four of them sum to $15$ only as $1+2+4+8$. So the group has one triple number $(i,j,k)$, one $x$-number, one $y$-number and one $z$-number.
   - *Digits $r,r^2,r^3$.* The digit of $r$ is $k'-k$ where $z_{k'}$ is the $z$-number, and it must be $0$; so $k'=k$. Likewise the $y$- and $x$-numbers belong to $y_j$ and $x_i$.
   - *Digit $r^4$.* The leading parts sum to $40$ only as $10+10+10+10$ (all actual) or $10+11+11+8$ (all dummy).

   So each group is a triple of $T$ together with all actual or all dummy numbers of its three elements. Each element has exactly one actual number, so the groups that use actual numbers give triples covering every element exactly once: a 3-dimensional matching.

6. The construction is polynomial in $q$ and $|T|$, and its numbers have $O(\log q)$ digits in base $r$. So 3DM $\le_p$ 4-Partition, and 4-Partition is NP-complete. (Because the numbers are polynomially bounded, this even shows strong NP-completeness.)
:::

::: {.solution for="prob-mit6046r-8-q5" status="draft"}
1. *In NP.* The certificate is an assignment. Evaluate every clause and count the satisfied ones: polynomial time.

2. *Reduction.* Given $(G,k)$ with $V=\{1,\dots,n\}$, use a variable $x_i$ for each vertex ("$i$ is in the clique") and one extra variable $z$. Clauses:
   - for each *non-edge* $\{i,j\}\notin E$: $(\lnot x_i\lor\lnot x_j)$;
   - for each vertex $i$: $(x_i\lor z)$ and $(x_i\lor\lnot z)$.

   Set the threshold $k'=m+n+k$, where $m$ is the number of non-edges.

3. *Counting.* For any assignment, each vertex pair of clauses has one satisfied clause if $x_i$ is false (exactly one of $z,\lnot z$ is true) and two if $x_i$ is true. So the number of satisfied clauses is
$$(\text{satisfied non-edge clauses})+n+|\{i:x_i=\text{TRUE}\}|.$$

4. *Clique $\Rightarrow$ assignment.* If $U$ is a clique with $|U|\ge k$, set $x_i$ true exactly for $i\in U$. Every non-edge has an endpoint outside $U$, so all $m$ non-edge clauses hold, and the count is $m+n+|U|\ge k'$.

5. *Assignment $\Rightarrow$ clique.* Take an assignment with at least $k'$ satisfied clauses. While some non-edge clause $(\lnot x_i\lor\lnot x_j)$ fails, set $x_i$ false. This satisfies that clause, loses exactly one vertex clause, and makes no other non-edge clause false, so the count does not drop. When it stops, all $m$ non-edge clauses hold, so the true variables form a clique $U$, and by step 3, $m+n+|U|\ge k'$, i.e. $|U|\ge k$.

So Clique $\le_p$ Max2SAT, and Max2SAT is NP-complete.

*Note (these notes).* The recitation writes the second vertex clause as $(x_i\land\lnot z)$, which is not a disjunction of two literals; $(x_i\lor\lnot z)$, as used above, is what the counting needs.
:::
