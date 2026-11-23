<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-10-q21" status="draft"}
1. *In coNP.* For the complement: guess an input on which $B_1$ and $B_2$ output different values, and evaluate both by following their paths in polynomial time. So $\overline{EQ_{\mathsf{BP}}}\in\mathrm{NP}$.

2. *A branching program for a cnf-formula.* Let $\phi=C_1\land\cdots\land C_m$. For each clause, place a node for each literal in order. Literal $\ell$ queries its variable: if $\ell$ is true, go to the first node of the next clause (or to output $1$ after $C_m$); if it is false, go to the next literal of the same clause (or to output $0$ after the last one). This $B_\phi$ computes $\phi$ and has $O(|\phi|)$ nodes.

3. *Reduction.* Let $B_0$ be the branching program that always outputs $0$. Map $\phi\mapsto\langle B_\phi,B_0\rangle$. Then $\phi$ is unsatisfiable iff $B_\phi\equiv B_0$, so $\overline{\mathit{SAT}}\le_{\mathrm p}EQ_{\mathsf{BP}}$.

4. $\overline{\mathit{SAT}}$ is coNP-complete, so $EQ_{\mathsf{BP}}$ is coNP-hard, and with step 1 it is coNP-complete.
:::
