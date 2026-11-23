<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-9-q19" status="draft"}
1. *Two oracle questions.* Given $\phi(x_1,\dots,x_n)$, let $x'$ be a fresh copy of the variables and form
$$\psi=\phi(x)\land\phi(x')\land\bigvee_{i=1}^n(x_i\oplus x'_i).$$
It has polynomial size and is built in polynomial time.

2. $\psi$ is satisfiable iff $\phi$ has two different satisfying assignments.

3. *Decision.* Ask the oracle whether $\phi$ is satisfiable and whether $\psi$ is satisfiable. Accept iff the answers are "yes" and "no": then $\phi$ has at least one satisfying assignment and not two, so exactly one.

4. This is a polynomial-time machine with a $\mathit{SAT}$ oracle, so $\mathit{USAT}\in\mathrm P^{\mathit{SAT}}$.
:::
