<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 1.60; 18.404J PS1 Q4 -->
::: {.problem #prob-sipser3e-1-q60 origin="external" source="sipser3e-1-q60"}
Let $\Sigma=\{\mathtt a,\mathtt b\}$. For each $k\ge1$, let $C_k$ be the language consisting of all strings that contain an $\mathtt a$ exactly $k$ places from the right-hand end. Thus $C_k=\Sigma^*\mathtt a\Sigma^{k-1}$. Describe an NFA with $k+1$ states that recognizes $C_k$ in terms of both a state diagram and a formal description.
:::

<!-- Sipser 1.61; 18.404J PS1 Q5 -->
::: {.problem #prob-sipser3e-1-q61 origin="external" source="sipser3e-1-q61"}
Consider the languages $C_k$ defined in Problem 1.60. Prove that for each $k$, no DFA can recognize $C_k$ with fewer than $2^k$ states.
:::
