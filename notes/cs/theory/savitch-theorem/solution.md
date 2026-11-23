<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-8-q8" status="draft"}
1. *To NFAs.* Convert $R$ and $S$ to NFAs $N_R,N_S$ with $O(|R|)$ and $O(|S|)$ states, a polynomial-time construction. Let $q$ be the total number of states.

2. *Inequivalence is in NPSPACE.* $R$ and $S$ are inequivalent iff some string is accepted by exactly one of the NFAs. Guess such a string symbol by symbol, and keep only the sets of states each NFA can be in ($q$ bits). Accept if at some point exactly one of the sets contains an accept state.

3. *Bounding the guess.* There are at most $2^q$ pairs of state sets, so if a witness exists, one of length less than $2^q$ exists. A counter of $q$ bits stops the guessing there. The space is $O(q)$.

4. By Savitch's theorem $\mathrm{NPSPACE}=\mathrm{PSPACE}$, so $\overline{EQ_{\mathsf{REX}}}\in\mathrm{PSPACE}$. $\mathrm{PSPACE}$ is closed under complement (run the decider and swap the answers), so $EQ_{\mathsf{REX}}\in\mathrm{PSPACE}$.
:::

::: {.solution for="prob-sipser3e-8-q13" status="draft"}
1. *In PSPACE.* An LBA with $q$ states and tape alphabet $\Gamma$ has at most $q\,n\,|\Gamma|^n$ configurations on an input of length $n$. Simulate $M$ on $w$ inside the $n$ cells, with a step counter of $O(n\log|\Gamma|+\log n+\log q)$ bits. Accept if $M$ accepts. Reject if it rejects or exceeds the bound, since then it repeats a configuration and loops.

2. *PSPACE-hard.* Let $A\in\mathrm{PSPACE}$ be decided by a TM $M$ in space $n^k$. Build an LBA $M'$ whose input is $w$ followed by padding symbols $\#$. $M'$ treats each $\#$ as a blank and simulates $M$ on $w$; it accepts iff $M$ does.

3. *The map.* $f(w)=\langle M',w\#^{|w|^k}\rangle$. $M$ never uses more than $|w|^k$ cells (for $|w|\ge2$; small inputs separately), so $M'$ stays within its input, and $w\in A$ iff $f(w)\in A_{\mathsf{LBA}}$.

4. $f$ takes polynomial time, so $A\le_{\mathrm p}A_{\mathsf{LBA}}$ for every $A\in\mathrm{PSPACE}$. Hence $A_{\mathsf{LBA}}$ is PSPACE-complete.
:::
