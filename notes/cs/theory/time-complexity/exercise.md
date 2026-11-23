<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 7.13; 18.404J PS4 Q1 -->
::: {.problem #prob-sipser3e-7-q13 origin="external" source="sipser3e-7-q13"}
Let
$$\mathit{MODEXP}=\{\langle a,b,c,p\rangle\mid a,b,c,\text{ and } p \text{ are positive binary integers such that } a^b\equiv c\pmod p\}.$$
Show that $\mathit{MODEXP}\in\mathrm P$. (Note that the most obvious algorithm doesn't run in polynomial time. Hint: Try it first where $b$ is a power of 2.)
:::

<!-- Sipser 7.15; 18.404J PS4 Q2 -->
::: {.problem #prob-sipser3e-7-q15 origin="external" source="sipser3e-7-q15"}
Show that $\mathrm P$ is closed under the star operation. (Hint: Use dynamic programming. On input $y=y_1\cdots y_n$ for $y_i\in\Sigma$, build a table indicating for each $i\le j$ whether the substring $y_i\cdots y_j\in A^*$ for any $A\in\mathrm P$.)
:::

<!-- Sipser 7.51; 18.404J PS4 Q7 -->
::: {.problem #prob-sipser3e-7-q51 origin="external" source="sipser3e-7-q51"}
This problem investigates *resolution*, a method for proving the unsatisfiability of cnf-formulas. Let $\phi=C_1\land C_2\land\cdots\land C_m$ be a formula in cnf, where the $C_i$ are its clauses. Let $\mathcal C=\{C_i\mid C_i \text{ is a clause of } \phi\}$. In a *resolution step*, we take two clauses $C_a$ and $C_b$ in $\mathcal C$, which both have some variable $x$ occurring positively in one of the clauses and negatively in the other. Thus, $C_a=(x\lor y_1\lor y_2\lor\cdots\lor y_k)$ and $C_b=(\overline x\lor z_1\lor z_2\lor\cdots\lor z_l)$, where the $y_i$ and $z_i$ are literals. We form the new clause $(y_1\lor y_2\lor\cdots\lor y_k\lor z_1\lor z_2\lor\cdots\lor z_l)$ and remove repeated literals. Add this new clause to $\mathcal C$. Repeat the resolution steps until no additional clauses can be obtained. If the empty clause $(\,)$ is in $\mathcal C$, then declare $\phi$ unsatisfiable.

Say that resolution is *sound* if it never declares satisfiable formulas to be unsatisfiable. Say that resolution is *complete* if all unsatisfiable formulas are declared to be unsatisfiable.

a. Show that resolution is sound and complete.

b. Use part (a) to show that $\mathit{2SAT}\in\mathrm P$.
:::
