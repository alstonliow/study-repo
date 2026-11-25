::: {.problem #prob-mit6046s15-3-q1 origin="external" source="mit6046s15-3-q1"}
**Variants on van Emde Boas**

For each of the following variants on the van Emde Boas data structures (presented in Lecture 4 and CLRS, Section 20.3), carefully describe what changes are needed to the pseudocode (from either lecture or the textbook), and analyze the costs of the vEB operations INSERT, DELETE, and SUCCESSOR, comparing them with the costs of the same operations for the original vEB structure.

(a) Instead of dividing the structure into $u^{1/2}$ groups of $u^{1/2}$ numbers each, use $u^{1/3}$ groups of $u^{2/3}$ numbers each.

(b) In addition to excluding the minimum element from lower-level vEB structures, also exclude the maximum element from lower-level vEB structures (and store it in the already existing max attribute). (Use the original division into $u^{1/2}$ groups of $u^{1/2}$ numbers here.)
:::
