<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-9-q17" status="draft"}
Fix the input alphabet $\Sigma$ and encode 2DFAs over $\Sigma$ as strings over $\Sigma$.

1. *The language.* $D=\{\langle M\rangle\mid M \text{ is a 2DFA that does not accept } \langle M\rangle\}$.

2. *$D\in\mathrm P$.* On input $w$, reject unless $w=\langle M\rangle$ for a 2DFA $M$. As in @prob-sipser3e-5-q26, $M$ on an input of length $n$ has at most $|Q|(n+2)^2$ configurations, and if it has not accepted after that many steps it never will. Simulate that many steps, each in polynomial time, and accept iff $M$ has not accepted. This is polynomial, since $|Q|\le n$.

3. *No 2DFA recognizes $D$.* Suppose a 2DFA $M_0$ did. Then $\langle M_0\rangle\in D$ iff $M_0$ does not accept $\langle M_0\rangle$ (definition of $D$) iff $\langle M_0\rangle\notin D$ (since $M_0$ recognizes $D$). This is a contradiction.
:::
