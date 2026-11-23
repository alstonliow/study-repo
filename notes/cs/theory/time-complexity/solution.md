<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-7-q13" status="draft"}
1. *Repeated squaring.* Let $b=b_{m-1}\cdots b_0$ in binary. Set $r\gets1$, and for $i=m-1$ down to $0$: $r\gets r^2\bmod p$, and if $b_i=1$ then $r\gets r\cdot a\bmod p$.

2. *Correctness.* After processing the bits $b_{m-1}\cdots b_i$, we have $r\equiv a^{\lfloor b/2^i\rfloor}\pmod p$, since squaring doubles the exponent and multiplying by $a$ adds the next bit. At the end $r\equiv a^b\pmod p$, and we accept iff $r=c\bmod p$.

3. *Time.* There are $m$ rounds, $m$ the length of $b$. Every intermediate value is below $p^2$ (reduce $a$ mod $p$ first), so each multiplication and division takes time polynomial in the length of $p$.

4. The total is polynomial in the input length, so $\mathit{MODEXP}\in\mathrm P$. (Computing $a^b$ first and then reducing would not be: $a^b$ can have exponentially many bits.)
:::

::: {.solution for="prob-sipser3e-7-q15" status="draft"}
1. Let $M$ decide $A\in\mathrm P$ in polynomial time. On input $y=y_1\cdots y_n$: if $n=0$, accept, since $\varepsilon\in A^*$.

2. *Table.* For $1\le i\le j\le n$, let $T[i,j]$ be true iff $y_i\cdots y_j\in A^*$. Fill the table in order of increasing length $j-i+1$: $T[i,j]$ is true iff $M$ accepts $y_i\cdots y_j$, or $T[i,k]$ and $T[k+1,j]$ are both true for some $i\le k<j$.

3. *Correctness.* A nonempty string is in $A^*$ iff it is in $A$ or it splits into two nonempty parts that are both in $A^*$ (cut after the first piece). The entries used for $T[i,j]$ belong to shorter substrings, so they are already filled. Accept iff $T[1,n]$ is true.

4. *Time.* There are $O(n^2)$ entries. Each needs one run of $M$, polynomial in $n$, and $O(n)$ lookups, so the total time is polynomial and $A^*\in\mathrm P$.
:::

::: {.solution for="prob-sipser3e-7-q51" status="draft"}
(a) *Soundness.*

1. If an assignment satisfies $C_a=(x\lor y_1\lor\cdots\lor y_k)$ and $C_b=(\overline x\lor z_1\lor\cdots\lor z_l)$, it satisfies the resolvent. If $x$ is true, $C_b$ forces some $z_j$ to be true; if $x$ is false, $C_a$ forces some $y_i$ to be true.

2. So by induction every clause added to $\mathcal C$ is satisfied by every assignment that satisfies $\phi$. The empty clause is satisfied by no assignment, so it is never added when $\phi$ is satisfiable.

(a) *Completeness*, by induction on the number $n$ of variables of an unsatisfiable cnf-formula $\phi$.

1. *$n=0$.* A cnf-formula with no variables is satisfiable unless it contains the empty clause, so $(\,)\in\mathcal C$ from the start.

2. *Restrictions.* For $n>0$, pick a variable $x$. Let $\phi|_{x=1}$ drop the clauses containing $x$ and delete $\overline x$ from the others; define $\phi|_{x=0}$ symmetrically. Both are unsatisfiable and have fewer variables, so by induction resolution derives $(\,)$ from each.

3. *Lifting a derivation.* Replay the derivation from $\phi|_{x=1}$ on the original clauses of $\phi$. Every clause of $\phi|_{x=1}$ is a clause of $\phi$ with at most $\overline x$ removed, and the steps resolve on variables other than $x$. So each replayed clause equals the corresponding clause of the derivation, possibly with $\overline x$ added. Hence resolution on $\phi$ derives $(\,)$ or $(\overline x)$. In the same way it derives $(\,)$ or $(x)$.

4. *Finish.* If it derives $(x)$ and $(\overline x)$, one more step gives $(\,)$. The procedure adds every clause it can derive, so $(\,)\in\mathcal C$ and $\phi$ is declared unsatisfiable.

(b)

1. If $\phi$ is a 2cnf-formula, every resolvent of two clauses with at most two literals has at most two literals. Over $n$ variables there are only $O(n^2)$ such clauses.

2. So $\mathcal C$ grows to at most $O(n^2)$ clauses. Each round tries all pairs in polynomial time and adds at least one new clause, or stops.

3. By (a), $\phi$ is unsatisfiable iff $(\,)$ appears. Answering the opposite decides $\mathit{2SAT}$ in polynomial time.
:::
