<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-5-q26" status="draft"}
(a)

1. On an input $x$ of length $n$, a configuration of a 2DFA $M$ is its state together with the two head positions, each in $\{0,\dots,n+1\}$. So there are at most $|Q|(n+2)^2$ configurations.

2. $M$ is deterministic. If it runs for more than $|Q|(n+2)^2$ steps, some configuration repeats, and from then on $M$ loops forever without accepting.

3. *Decider.* On $\langle M,x\rangle$, simulate $M$ on $x$ for $|Q|(n+2)^2$ steps. Accept if it reaches the accept state; otherwise reject.

(b)

1. *Reduction from $A_{\mathsf{TM}}$.* Given $\langle M,w\rangle$, build a 2DFA $D$ that accepts exactly the accepting computation histories $C_1\#C_2\#\cdots\#C_l$ of $M$ on $w$. Pad every configuration with blanks to a common length.

2. *Checks that need one head.* $D$ checks that $C_1$ is the start configuration of $M$ on $w$ ($w$ is built into $D$'s states), that $C_l$ contains $q_{\text{accept}}$, and that all configurations have the same length, using one head on each of two neighbouring blocks.

3. *Checking one step.* To check that $C_{i+1}$ follows from $C_i$, put head 1 at the start of $C_i$ and head 2 at the start of $C_{i+1}$, and move both right in step. At each position, $D$ remembers the last three symbols under head 1 in its finite control. The symbol under head 2 must be the one that $M$'s transition function determines from that window. After the block, head 1 moves on to the start of $C_{i+1}$ and head 2 to the start of $C_{i+2}$.

4. *Correctness.* $L(D)$ is the set of accepting histories, so $L(D)=\emptyset$ iff $M$ does not accept $w$. The map $\langle M,w\rangle\mapsto\langle D\rangle$ is computable. A decider for $E_{\mathsf{2DFA}}$ would therefore decide $A_{\mathsf{TM}}$, so $E_{\mathsf{2DFA}}$ is undecidable.
:::

::: {.solution for="prob-sipser3e-5-q21" status="draft"}
1. *The map.* Send a PCP instance $P$ to the grammar $G$ of the hint; it is computable from $P$. We show that $P$ has a match iff $G$ is ambiguous.

2. *A match gives two derivations.* Let $i_1,\dots,i_l$ be a match, so $t_{i_1}\cdots t_{i_l}=b_{i_1}\cdots b_{i_l}$. Then
$$t_{i_1}\cdots t_{i_l}\,\mathtt a_{i_l}\cdots\mathtt a_{i_1}=b_{i_1}\cdots b_{i_l}\,\mathtt a_{i_l}\cdots\mathtt a_{i_1}.$$
This string has a leftmost derivation starting $S\Rightarrow T$ and another starting $S\Rightarrow B$. So $G$ is ambiguous.

3. *$T$ and $B$ alone are unambiguous.* Every string derived from $T$ has the form $t_{i_1}\cdots t_{i_l}\mathtt a_{i_l}\cdots\mathtt a_{i_1}$. The new symbols $\mathtt a_j$ occur only in the suffix, and reading that suffix from the right gives the sequence $i_1,\dots,i_l$, which fixes the rule used at each step. So each string has only one derivation from $T$; the same holds for $B$.

4. *Ambiguity gives a match.* If $G$ is ambiguous, some string has two derivations. By step 3, one starts $S\Rightarrow T$ and the other $S\Rightarrow B$. Both index sequences are read off the same $\mathtt a$-suffix, so they are equal, and comparing the prefixes gives $t_{i_1}\cdots t_{i_l}=b_{i_1}\cdots b_{i_l}$: a match.

5. A decider for $\mathit{AMBIG}_{\mathsf{CFG}}$ would therefore decide PCP. PCP is undecidable, so $\mathit{AMBIG}_{\mathsf{CFG}}$ is undecidable.
:::
