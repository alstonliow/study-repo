<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-10-q20" status="draft"}
Probabilities are over the branches (coin flips) of the machine.

1. *$\mathrm{RP}\cap\mathrm{coRP}\subseteq\mathrm{ZPP}$.* Let $M_1$ be an RP machine for $A$ (never accepts a string outside $A$) and $M_2$ a coRP machine for $A$ (never rejects a string in $A$). On $w$, run $M_1$ twice and $M_2$ twice. If some run of $M_1$ accepts, accept. Else if some run of $M_2$ rejects, reject. Else output *?*.

2. *Check.* The answers given are never wrong. If $w\in A$, *?* needs both runs of $M_1$ to reject, with probability at most $\tfrac14$; the case $w\notin A$ is symmetric. So *?* has probability at most $\tfrac13$, and the worst-case running time, hence also the average, is polynomial.

3. *$\mathrm{ZPP}\subseteq\mathrm{RP}$.* Let $M$ be a ZPP-machine for $A$ with average running time at most $p(n)$. By Markov's inequality, $M$ runs longer than $6p(n)$ steps with probability at most $\tfrac16$. Let $M_1$ simulate $M$ for $6p(n)$ steps and accept iff $M$ accepts within that time.

4. *Check.* If $w\notin A$, $M$ never accepts, so $M_1$ always rejects. If $w\in A$, $M_1$ fails only if $M$ outputs *?* (probability at most $\tfrac13$) or runs too long (at most $\tfrac16$). So it accepts with probability at least $\tfrac12$, and $A\in\mathrm{RP}$.

5. *$\mathrm{ZPP}\subseteq\mathrm{coRP}$.* The same machine, rejecting iff $M$ rejects within the time, shows $A\in\mathrm{coRP}$.
:::

::: {.solution for="prob-sipser3e-10-q19" status="draft"}
1. *$\mathrm{RP}\subseteq\mathrm{NP}$ always.* An RP machine is a polynomial-time NTM. It has an accepting branch iff $w\in A$: for $w\in A$ at least half the branches accept, and for $w\notin A$ none do.

2. *$\mathit{SAT}\in\mathrm{RP}$, assuming $\mathrm{NP}\subseteq\mathrm{BPP}$.* Then $\mathit{SAT}\in\mathrm{BPP}$. By amplification (majority vote over polynomially many runs) there is a polynomial-time machine $B$ for $\mathit{SAT}$ with error at most $\tfrac1{4n}$ on formulas with $n$ variables.

3. *Search.* Given $\phi(x_1,\dots,x_n)$: for $i=1,\dots,n$, set $x_i=0$ if $B$ says the formula with $x_1,\dots,x_{i-1}$ fixed and $x_i=0$ is satisfiable, and $x_i=1$ otherwise. Finally, accept iff the assignment found satisfies $\phi$.

4. *No false accepts.* If $\phi$ is unsatisfiable, the final check always fails, so the algorithm never accepts.

5. *Enough true accepts.* If $\phi$ is satisfiable, with probability at least $1-n\cdot\tfrac1{4n}=\tfrac34$ all $n$ answers of $B$ are correct. Then the partial assignment stays extendable to a satisfying one at every step: if $x_i=0$ does not keep it satisfiable, $x_i=1$ must. So the final assignment satisfies $\phi$, and the algorithm accepts with probability at least $\tfrac34\ge\tfrac12$.

6. *All of NP.* RP is closed under polynomial-time reductions, and every $A\in\mathrm{NP}$ reduces to $\mathit{SAT}$. So $\mathrm{NP}\subseteq\mathrm{RP}$, and with step 1, $\mathrm{NP}=\mathrm{RP}$.
:::
