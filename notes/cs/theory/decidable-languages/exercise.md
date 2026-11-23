<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 4.24; 18.404J PS2 Q5 -->
::: {.problem #prob-sipser3e-4-q24 origin="external" source="sipser3e-4-q24"}
A *useless state* in a pushdown automaton is never entered on any input string. Consider the problem of determining whether a pushdown automaton has any useless states. Formulate this problem as a language and show that it is decidable.
:::

<!-- Sipser 4.27; 18.404J PS2 Q6 (the problem set cites a 2nd-edition number that is 4.25 or 4.27 in the 3rd; 4.27 chosen, owner decision 2026-11-23) -->
::: {.problem #prob-sipser3e-4-q27 origin="external" source="sipser3e-4-q27"}
Let $E=\{\langle M\rangle\mid M \text{ is a DFA that accepts some string with more 1s than 0s}\}$. Show that $E$ is decidable. (Hint: Theorems about CFLs are helpful here.)
:::

<!-- Sipser 4.14; 18.404J PS3 Q7 -->
::: {.problem #prob-sipser3e-4-q14 origin="external" source="sipser3e-4-q14"}
Let $\Sigma=\{0,1\}$. Show that the problem of determining whether a CFG generates some string in $1^*$ is decidable. In other words, show that
$$\{\langle G\rangle\mid G \text{ is a CFG over } \{0,1\} \text{ and } 1^*\cap L(G)\ne\emptyset\}$$
is a decidable language.
:::
