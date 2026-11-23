<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 3.12; 18.404J PS2 Q2 -->
::: {.problem #prob-sipser3e-3-q12 origin="external" source="sipser3e-3-q12"}
A *Turing machine with left reset* is similar to an ordinary Turing machine, but the transition function has the form
$$\delta\colon Q\times\Gamma\longrightarrow Q\times\Gamma\times\{\mathrm R,\mathrm{RESET}\}.$$
If $\delta(q,a)=(r,b,\mathrm{RESET})$, when the machine is in state $q$ reading an $a$, the machine's head jumps to the left-hand end of the tape after it writes $b$ on the tape and enters state $r$. Note that these machines do not have the usual ability to move the head one symbol left. Show that Turing machines with left reset recognize the class of Turing-recognizable languages.
:::

<!-- Sipser 3.18; 18.404J PS2 Q3 -->
::: {.problem #prob-sipser3e-3-q18 origin="external" source="sipser3e-3-q18"}
Show that a language is decidable iff some enumerator enumerates the language in the standard string order.
:::
