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

<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-7-q28" status="draft"}
We assume, as in the book's figure, that turning a card over swaps its two columns and keeps its rows.

1. *In NP.* The certificate is the side chosen for each card. Checking that every hole position is blocked takes polynomial time.

2. *Reduction from $\mathit{{\ne}SAT}$* (NP-complete, @prob-sipser3e-7-q26). Let $\phi$ be a 3cnf-formula with variables $x_1,\dots,x_n$ and clauses $c_1,\dots,c_m$. Give the box $m$ rows and make one card per variable. Card $i$ has a column $T_i$ that is blocked at row $j$ iff $x_i$ appears in $c_j$, and a column $F_i$ that is blocked at row $j$ iff $\overline{x_i}$ appears in $c_j$; all other positions are holes.

3. *Meaning of a placement.* Read "card $i$ with $T_i$ on the left" as $x_i$ true. Then the left column of the box is blocked at row $j$ iff some literal of $c_j$ is true. The right column holds the other column of each card, so it is blocked at row $j$ iff some literal of $c_j$ is false.

4. *Correctness.* All positions are blocked iff every clause has a true literal and a false literal, that is, iff the assignment is a $\ne$-assignment. So the puzzle is solvable iff $\phi\in\mathit{{\ne}SAT}$.

5. The cards are built in polynomial time, so $\mathit{PUZZLE}$ is NP-complete.
:::

::: {.solution for="prob-sipser3e-7-q37" status="draft"}
1. *In NP.* The certificate is a sequence of at most $t$ nondeterministic choices. The verifier simulates $M$ on $x$ along those choices for at most $t$ steps and checks that it accepts. Because $t$ is given in unary, $t\le|\langle M,x,\#^t\rangle|$, so this takes polynomial time.

2. *NP-hard.* Let $A\in\mathrm{NP}$ be decided by an NTM $N$ in time $n^k$ (for $n\ge2$; fix small inputs separately). Map $x\mapsto\langle N,x,\#^{|x|^k}\rangle$. The map takes polynomial time, since writing $|x|^k$ symbols is polynomial.

3. *Correctness.* $x\in A$ iff some branch of $N$ accepts $x$, and every branch halts within $|x|^k$ steps. So $x\in A$ iff $N$ accepts $x$ within $|x|^k$ steps on some branch, that is, iff the image is in $U$.

4. So $A\le_{\mathrm p}U$ for every $A\in\mathrm{NP}$, and $U$ is NP-complete.
:::

::: {.solution for="prob-sipser3e-7-q26" status="draft"}
A $\ne$-assignment is exactly one where every clause has at least one true literal and at least one false literal.

(a) Negating every variable turns true literals into false ones and vice versa. So each clause still has one of each, and the negation is again a $\ne$-assignment.

(b)

1. *Satisfiable gives a $\ne$-assignment.* Let $\alpha$ satisfy $\phi$, and extend it with $b$ false. For clause $c_i$: if $y_1$ or $y_2$ is true, set $z_i$ false; then $(y_1\lor y_2\lor z_i)$ has a true and a false literal, and $(\overline{z_i}\lor y_3\lor b)$ has $\overline{z_i}$ true and $b$ false. Otherwise $y_3$ is true; set $z_i$ true; then the first clause has $z_i$ true and $y_1$ false, and the second has $y_3$ true and $\overline{z_i}$ false.

2. *A $\ne$-assignment gives a satisfying one.* Let $\beta$ be a $\ne$-assignment of the new formula. By (a) we may assume $b$ is false. If $y_1$ and $y_2$ are both false, the first clause forces $z_i$ true. Then the second clause has $\overline{z_i}$ and $b$ false, so $y_3$ must be true. Either way $c_i$ has a true literal, so $\beta$ restricted to the original variables satisfies $\phi$.

3. The new formula has $2m$ clauses, $m$ the number of clauses of $\phi$, and is built in polynomial time.

(c) $\mathit{{\ne}SAT}\in\mathrm{NP}$: the certificate is the assignment. By (b), $\mathit{3SAT}\le_{\mathrm p}\mathit{{\ne}SAT}$, and $\mathit{3SAT}$ is NP-complete, so $\mathit{{\ne}SAT}$ is NP-complete.
:::

::: {.solution for="prob-sipser3e-7-q27" status="draft"}
1. *In NP.* The certificate is the set $S$; count the edges that cross the cut.

2. *Construction.* Let $\phi$ be a 3cnf-formula with $n$ variables and $c\ge1$ clauses. Clauses containing both $x$ and $\overline x$ always have a true and a false literal, so drop them first. Build $G$ as in the hint. Each variable gadget is a complete bipartite graph $K_{3c,3c}$ between the $x$-nodes and the $\overline x$-nodes. Each occurrence of a literal in a clause gets its own node of that literal's gadget (there are at most $3c$ occurrences), and the three nodes of a clause are joined in a triangle. Set $k=9c^2n+2c$.

3. *Two counting facts.*
   - A triangle has at most $2$ cut edges, and exactly $2$ iff its nodes are not all on one side.
   - Suppose $p$ of the $x$-nodes and $q$ of the $\overline x$-nodes lie in $S$. Then the gadget has $pq+(3c-p)(3c-q)$ uncut edges. This is $0$ when $(p,q)\in\{(3c,0),(0,3c)\}$ and at least $3c$ otherwise (check the corners of the region).

4. *($\Rightarrow$)* Given a $\ne$-assignment, put the nodes of true literals in $S$ and the nodes of false literals in $T$. Every gadget is fully cut ($9c^2$ edges), and every triangle has a true and a false node ($2$ edges). The cut has size $k$.

5. *($\Leftarrow$)* Take a cut of size at least $k$. If some gadget were not fully cut, the total would be at most $9c^2n-3c+2c<k$. So every gadget puts all $x$-nodes on one side and all $\overline x$-nodes on the other. Set $x$ true iff its $x$-nodes are in $S$. The triangles must then give all $2c$ remaining edges, so each clause has a node in $S$ (a true literal) and a node in $T$ (a false literal). This is a $\ne$-assignment.

6. The graph has polynomial size, so $\mathit{{\ne}SAT}\le_{\mathrm p}\mathit{MAX\text-CUT}$, and $\mathit{MAX\text-CUT}$ is NP-complete.
:::

::: {.solution for="prob-sipser3e-7-q36" status="draft"}
Call the problem $\mathit{DFA\text-FIT}$.

1. *In NP.* The certificate is the transition table $\delta$ on $Q\times\{0,1\}$, of polynomial size. Check $\delta(q_0,s_i)=r_i$ for each $i$ by running the strings.

2. *Forcing transitions.* Suppose a state $X$ has a string $a_X$ with a pair $(a_X,X)$, and every transition on the way is already forced. Then the pair $(a_X\sigma,Y)$ forces $\delta(X,\sigma)=Y$. Give every state such an address: the routing states form a binary tree rooted at $q_0$ (each internal node goes to its two children), and every other state is a child of a leaf. All transitions are forced this way except the *free* ones named below. Unused transitions go to a sink $R$ with $\delta(R,0)=\delta(R,1)=R$.

3. *States for the formula.* Reduce from $\mathit{3SAT}$, with variables $x_1,\dots,x_n$ and clauses $c_1,\dots,c_m$. Besides the routing states and $R$, use:
   - $T$ and $F$ with $\delta(T,0)=F$, $\delta(F,0)=T$ and $\delta(T,1)=\delta(F,1)=Z$;
   - for each variable, $p_j$ and $u_j$ with $\delta(u_j,0)=p_j$;
   - for each clause, $g_k$, a label $Y_k$, and one state $L_{k,t}$ for each of its three literals, with $\delta(L_{k,t},0)=Y_k$, and $\delta(L_{k,t},1)=u_j$ if the literal is $x_j$, or $p_j$ if it is $\overline{x_j}$.

   The free transitions are $\delta(p_j,0)$ and $\delta(g_k,0)$.

4. *Labels.* Route the leaf edges so that $Z$ is entered only on $0$ and each $Y_k$ only on $1$. Then $T$ and $F$ are the only states with a $1$-transition to $Z$, and the $L_{k,t}$ are the only states with a $0$-transition to $Y_k$.

5. *Constraint pairs.*
   - $(a_{p_j}01,\ Z)$ forces $\delta(p_j,0)\in\{T,F\}$; read $\delta(p_j,0)=T$ as "$x_j$ true".
   - $(a_{g_k}00,\ Y_k)$ forces $\delta(g_k,0)$ to be one of $L_{k,1},L_{k,2},L_{k,3}$: the clause picks one of its literals.
   - $(a_{g_k}0100,\ T)$ says the picked literal is true. For $x_j$ the path is $L\to u_j\to p_j\to\delta(p_j,0)$, which must be $T$. For $\overline{x_j}$ the path is $L\to p_j\to\delta(p_j,0)\to$ its negation, which must be $T$, so $\delta(p_j,0)=F$.

6. *Correctness.* If $\phi$ is satisfiable, set $\delta(p_j,0)$ by the assignment and let each $g_k$ pick a true literal; all pairs hold. Conversely, a DFA meeting all pairs gives an assignment through $\delta(p_j,0)$ in which every clause has a true literal.

7. *Size.* There are $O(n+m)$ states, and the pairs have length $O(\log(n+m))$ and are distinct. So the map takes polynomial time, $\mathit{3SAT}\le_{\mathrm p}\mathit{DFA\text-FIT}$, and the problem is NP-complete.
:::
