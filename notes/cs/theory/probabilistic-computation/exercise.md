<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 10.20; 18.404J PS6 Q6 -->
::: {.problem #prob-sipser3e-10-q20 origin="external" source="sipser3e-10-q20"}
Define a *ZPP-machine* to be a probabilistic Turing machine that is permitted three types of output on each of its branches: *accept*, *reject*, and *?*. A ZPP-machine $M$ decides a language $A$ if $M$ outputs the correct answer on every input string $w$ (*accept* if $w\in A$ and *reject* if $w\notin A$) with probability at least $\tfrac23$, and $M$ never outputs the wrong answer. On every input, $M$ may output *?* with probability at most $\tfrac13$. Furthermore, the average running time over all branches of $M$ on $w$ must be bounded by a polynomial in the length of $w$. Show that $\mathrm{RP}\cap\mathrm{coRP}=\mathrm{ZPP}$, where $\mathrm{ZPP}$ is the collection of languages that are recognized by ZPP-machines.
:::

<!-- Sipser 10.19; 18.404J PS6 Q7 -->
::: {.problem #prob-sipser3e-10-q19 origin="external" source="sipser3e-10-q19"}
Show that if $\mathrm{NP}\subseteq\mathrm{BPP}$, then $\mathrm{NP}=\mathrm{RP}$.
:::
